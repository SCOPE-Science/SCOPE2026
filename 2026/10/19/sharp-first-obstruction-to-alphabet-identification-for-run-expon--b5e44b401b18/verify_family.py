"""Exact run lists and energy of a ternary family under pairwise letter merges."""
from fractions import Fraction


def runs(word):
    n = len(word)
    ans = []
    for i in range(n):
        for p in range(1, (n - i) // 2 + 1):
            if i > 0 and word[i-1] == word[i+p-1]:
                continue
            j = i+p
            while j < n and word[j] == word[j-p]:
                j += 1
            if j-i < 2*p:
                continue
            if any(all(word[t] == word[t-d] for t in range(i+d, j)) for d in range(1,p)):
                continue
            ans.append((i+1, j, p))
    return sorted(ans)


def energy(runs_list):
    return sum((Fraction(j-i+1,p) for i,j,p in runs_list),Fraction(0))


def family(k):
    w='0011011211'+'2'*k
    return [w,w.replace('1','0'),w.replace('2','0'),w.replace('2','1')]


def expected(k):
    n=10+k
    return [
        [(1,2,1),(2,7,3),(3,4,1),(6,7,1),(6,11,3),(9,10,1),(11,n,1)],
        [(1,7,1),(6,11,3),(9,10,1),(11,n,1)],
        [(1,2,1),(2,11,3),(3,4,1),(6,7,1),(9,10,1),(11,n,1)],
        [(1,2,1),(2,7,3),(3,4,1),(6,n,1)],
    ]


def main():
    # The proof reduces the infinite family to k=2,...,9 and a tail lemma;
    # extra values here are regression tests, not the argument for infinity.
    for k in list(range(2,10))+[10,12,20,40]:
        rr=[runs(w) for w in family(k)]
        for i in range(4):
            assert rr[i]==sorted(expected(k)[i]),(k,i,rr[i],expected(k)[i])
        actual=[energy(x) for x in rr]
        want=[Fraction(k+12),Fraction(k+11),Fraction(k)+Fraction(34,3),Fraction(k+11)]
        assert actual==want,(k,actual,want)
        assert all(x<actual[0] for x in actual[1:])
    print('FAMILY_VERIFY_OK canonical_12=001101121122 k=2..9 and supplementary k=10,12,20,40')


if __name__=='__main__':
    main()
