"""Reproducible finite checks for the two-read deletion graph's degree spectrum.

Uses only the Python standard library. Finite tests are consistency checks,
not a substitute for the all-length proof in RESULT.md.
"""
from collections import Counter
from fractions import Fraction
from itertools import product


def one_deletions(w):
    return {w[:i] + w[i+1:] for i in range(len(w))}


def degree_from_difference_runs(w):
    total = run = 0
    for i in range(len(w) - 1):
        if w[i] != w[i+1]:
            run += 1
        else:
            total += run*(run+1)//2
            run = 0
    return total + run*(run+1)//2


def degree_distribution(n):
    return Counter(degree_from_difference_runs(w)
                   for w in product((0,1), repeat=n))


def polynomial_add(a, b, c=1):
    out = Counter(a)
    for degree, coefficient in b.items():
        out[degree] += c*coefficient
    return Counter({k:v for k,v in out.items() if v})


def predicted_coefficient_by_formal_identity(m, old):
    # (1-z-z R(z,u)) F(z,u)=1+R(z,u)
    # F is the difference-string enumerator; its coefficients are half
    # the corresponding length-(m+1) word histograms.
    if m == 0:
        return Counter({0:1})
    ans = Counter({m*(m+1)//2:1})  # R's coefficient at z^m
    ans = polynomial_add(ans,old[m-1])
    for h in range(1,m):
        shifted=Counter({d+h*(h+1)//2:c for d,c in old[m-h-1].items()})
        ans=polynomial_add(ans,shifted)
    return ans


def check():
    all_binary_graph_pairs=0
    for n in range(1,10):
        words=list(product((0,1),repeat=n))
        balls=[one_deletions(w) for w in words]
        for i,x in enumerate(words):
            brute=sum(len(balls[i]&balls[j]) >= 2
                      for j in range(len(words)) if i != j)
            predicted=degree_from_difference_runs(x)
            assert brute == predicted, (n,x,brute,predicted)
        all_binary_graph_pairs += len(words)*(len(words)-1)//2
    print('PASS: exhaustive binary two-read graph degrees n=1..9')
    print('Distinct unordered center pairs checked:', all_binary_graph_pairs)

    old=[]
    for m in range(0,14):
        histogram=degree_distribution(m+1)
        assert sum(histogram.values())==2**(m+1)
        half=Counter({k:v//2 for k,v in histogram.items()})
        assert all(v%2==0 for v in histogram.values())
        expected=predicted_coefficient_by_formal_identity(m,old)
        assert half==expected,(m,half,expected)
        old.append(half)
        n=m+1
        mean=Fraction(sum(d*c for d,c in histogram.items()),2**n)
        second=Fraction(sum(d*d*c for d,c in histogram.items()),2**n)
        variance=second-mean**2
        pred_mean=Fraction(n-2)+Fraction(1,2**(n-1))
        pred_var=Fraction(6*n-30)+Fraction(2*n*n+6*n+17,2**(n-1))-Fraction(1,4**(n-1))
        assert mean==pred_mean,(n,mean,pred_mean)
        assert variance==pred_var,(n,variance,pred_var)
        assert histogram[0]==2
        assert histogram[n*(n-1)//2]==2 if n>=2 else histogram[0]==2
    print('PASS: formal-series coefficient identity and moments for n=1..14')
    print('PASS: all-degree extremal multiplicities n=1..14')
    print('Sample degree histograms (degree:count):')
    for n in (5,6,7):
        print(n,sorted(degree_distribution(n).items()))

if __name__ == '__main__':
    check()
