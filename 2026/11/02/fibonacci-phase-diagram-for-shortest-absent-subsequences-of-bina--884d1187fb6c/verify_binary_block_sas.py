"""Independent literal subsequence enumeration and structural-check verifier."""
from itertools import product
from functools import lru_cache

def is_subsequence(u,w):
    it=iter(w)
    return all(any(y==x for y in it) for x in u)

def count_fib(n):
    a,b=0,1
    for _ in range(n): a,b=b,a+b
    return a

def predicted_set(a,b,m):
    if a==b==1:
        return {'1'*t+'0'*(m+1-t) for t in range(m+1)} | {'1'*(m+1)}
    if a==1:
        return {'0'*(m+1), '1'+'0'*m}
    if b==1:
        return {'1'*(m+1), '1'*m+'0'}
    k=2*m-1
    R=[a if j==1 else (b-1 if j%2==0 else a-1) for j in range(1,k+1)]
    out=set()
    def walk(j,ts):
        if j>k:
            if ts[-1]=='E' and a>2:return
            u=''.join(('0' if j%2 else '1') if t=='E' else ('1' if j%2 else '0') for j,t in enumerate(ts,1))+'0'
            out.add(u);return
        for nxt in 'EL':
            if ts[-1]=='E' and (nxt!='L' or R[j-2]!=1):continue
            walk(j+1,ts+nxt)
    walk(2,'L')
    return out

def expected_length_count(a,b,m):
    if a==1 or b==1:
        return m+1, (m+2 if a==b==1 else 2)
    k=2*m
    if a==b==2: return k,count_fib(k)
    if a==2 or b==2: return k, 2**(m-1)
    return k,1

def main():
    cases=words_checked=missing_checked=0
    for a in range(1,7):
      for b in range(1,7):
       for m in range(1,7):
        w=('0'*a+'1'*b)*m
        length,target_count=expected_length_count(a,b,m)
        structural=predicted_set(a,b,m)
        assert len(structural)==target_count,(a,b,m,len(structural),target_count)
        assert all(is_subsequence(v,w) for r in range(length) for v in map(''.join,product('01',repeat=r))),(a,b,m,'universality')
        actual=set()
        for tup in product('01',repeat=length):
            v=''.join(tup)
            words_checked+=1
            if not is_subsequence(v,w): actual.add(v)
        assert actual==structural,(a,b,m,sorted(actual^structural)[:5])
        missing_checked+=len(actual);cases+=1
    print('VERIFY_OK instances=%d literal_targets=%d classified_shortest_absent=%d'%(cases,words_checked,missing_checked))
if __name__=='__main__':main()
