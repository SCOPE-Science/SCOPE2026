"""Exact independent checks for three-marker circular palindrome classification."""
from itertools import combinations


def cyc_word(a,b,c):
    return '1'+'0'*a+'1'+'0'*b+'1'+'0'*c


def direct_palindromes(w):
    n=len(w); doubled=w+w
    return {doubled[i:i+k] for i in range(n) for k in range(1,n+1)
            if doubled[i:i+k]==doubled[i:i+k][::-1]}


def claimed_count(a,b,c):
    x,y,z=sorted((a,b,c)); n=a+b+c+3
    if x==z: return n+x//2
    if x==y or y==z: return n+(n-1)//2
    return n+1+x+y


def predicted_max(n):
    if n==3:return 3
    repeat=n+(n-1)//2
    if n<6:return repeat
    return max(repeat,(5*n)//3-2)


def optimal_gap_condition(a,b,c):
    x,y,z=sorted((a,b,c));n=x+y+z+3
    if x==z:return n==3
    if x==y or y==z:return n+(n-1)//2==predicted_max(n)
    return (5*n)//3-2==predicted_max(n) and z==(n+2)//3


def check():
    # A second implementation, based on literal cyclic starts/lengths,
    # independently tests every gap triple up to length 36.
    tested=0
    for n in range(3,37):
        actual_best=0;actual_opt=[];pred_opt=[]
        for a in range(n-2):
            for b in range(n-2-a):
                c=n-3-a-b
                if c<0:continue
                w=cyc_word(a,b,c)
                got=len(direct_palindromes(w))
                expected=claimed_count(a,b,c)
                assert got==expected,(n,(a,b,c),got,expected)
                actual_best=max(actual_best,got)
                if optimal_gap_condition(a,b,c):pred_opt.append((a,b,c))
                tested+=1
        assert actual_best==predicted_max(n),(n,actual_best,predicted_max(n))
        # Equality characterization is checked separately, without relying
        # on the formula to compute measured palindrome counts.
        for a in range(n-2):
            for b in range(n-2-a):
                c=n-3-a-b
                actual=(len(direct_palindromes(cyc_word(a,b,c)))==actual_best)
                assert actual==optimal_gap_condition(a,b,c),(n,a,b,c)
    # Every arrangement is considered: not merely one representative of each necklace.
    print('VERIFY_OK',tested,'ordered gap triples (lengths 3..36)')

if __name__=='__main__':check()
