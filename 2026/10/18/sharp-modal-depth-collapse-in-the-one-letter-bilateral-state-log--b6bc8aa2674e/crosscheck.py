"""Independent eight-bit arithmetic implementation of the finite BSL algebra."""
from collections import deque

def fuse(a,b):
    return sum(1<<t for t in range(4) if any((a>>u)&1 and (b>>v)&1
                  for u in range(4) for v in range(4) if (u|v)==t))
def possibility(a):
    return sum(1<<t for t in range(4) if any((a>>s)&1 and s and (s&t)==s
                  for s in range(4)))
def neg(x):return (x[1],x[0])
def meet(x,y):return (x[0]&y[0],fuse(x[1],y[1]))
def join(x,y):return (fuse(x[0],y[0]),x[1]&y[1])
def diamond(x):return (possibility(x[0]),x[1])
def closure(seed):
    seen=set(seed);queue=deque(seed)
    while queue:
        x=queue.popleft()
        for y in list(seen):
            for z in (meet(x,y),join(x,y)):
                if z not in seen: seen.add(z);queue.append(z)
        z=neg(x)
        if z not in seen:seen.add(z);queue.append(z)
    assert all(meet(x,y) in seen and join(x,y) in seen for x in seen for y in seen)
    return seen

def main():
    import json,sys
    A0=closure({(1,15),(14,1),(5,3)})
    A1=closure(A0|{diamond(x) for x in A0})
    A2=closure(A1|{diamond(x) for x in A1})
    assert {len(A0),len(A1),len(A2)}=={39,64,66}
    assert len(A0)==39 and len(A1)==64 and len(A2)==66
    assert all(diamond(x) in A2 for x in A2)
    assert A2-A1=={(10,12),(12,10)}
    if len(sys.argv)>1:
        j=json.load(open(sys.argv[1],encoding='utf8'))
        assert sorted(map(list,A0))==j['depth0_signatures']
        assert sorted(map(list,A1-A0))==j['depth1_new_signatures']
        assert sorted(map(list,A2-A1))==j['depth2_new_signatures']
        assert sorted(map(list,A2))==j['all_signatures']
    print('BILATERAL_BITMASK_CROSSCHECK_OK 39 64 66')
if __name__=='__main__':main()
