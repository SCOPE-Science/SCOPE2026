from itertools import combinations

def forest(s,k):
    assert k>=2 and 4<=s<=2*k
    r = min(k,s-1)
    c = s-r
    lengths=[r-c+1]+[1]*(c-1)
    edges=[];next_v=0
    for a in lengths:
        for j in range(a):edges.append((next_v+j,next_v+j+1))
        next_v+=a+1
    assert next_v==s and len(edges)==r
    return edges

def pattern(edges):
    return [[len(set(a)&set(b))>0 for b in edges[:i]] for i,a in enumerate(edges)]

def realized(n, p):
    r=len(p)
    edges=list(combinations(range(n),2))
    def rec(chosen):
        i=len(chosen)
        if i==r:return True
        for e in edges:
            if e in chosen: continue
            if all((bool(set(e)&set(chosen[j]))==p[i][j]) for j in range(i)):
                if rec(chosen+[e]):return True
        return False
    return rec([])

def run():
    count=0
    for k in range(2,6):
        for s in range(4,2*k+1):
            fs=forest(s,k)
            p=pattern(fs)
            assert not realized(s-1,p),(k,s,fs)
            assert realized(s,p),(k,s,fs)
            count+=2
            print('WITNESS_OK k=%d threshold=%d variables=%d components=%d' %
                  (k,s,len(fs),s-len(fs)))
    print('ALL_WITNESS_CHECKS_OK',count)
if __name__=='__main__':run()
