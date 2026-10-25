"""Independent four-round Ehrenfeucht--Fraisse adversarial oracle."""
from functools import lru_cache
from verify import ladder


def game4(A,B):
    N,M = len(A),len(B)

    @lru_cache(None)
    def dup(asel,bsel):
        if len(asel)==4:
            return True
        for a in range(N):
            valid=False
            for b in range(M):
                if all((a==u)==(b==v) and bool(A[a]>>u&1)==bool(B[b]>>v&1)
                       for u,v in zip(asel,bsel)):
                    if dup(asel+(a,),bsel+(b,)):
                        valid=True
                        break
            if not valid:
                return False
        for b in range(M):
            valid=False
            for a in range(N):
                if all((a==u)==(b==v) and bool(A[a]>>u&1)==bool(B[b]>>v&1)
                       for u,v in zip(asel,bsel)):
                    if dup(asel+(a,),bsel+(b,)):
                        valid=True
                        break
            if not valid:
                return False
        return True
    return dup((),())

if __name__=='__main__':
    checks=[(8,False,8,True,False),(9,False,9,True,True)]
    for n,t,m,u,target in checks:
        answer=game4(ladder(n,t),ladder(m,u))
        assert answer==target,(n,t,m,u,answer)
        print(f'GAME_OK left=({n},{int(t)}) right=({m},{int(u)}) equivalent={answer}',flush=True)
    print('DIRECT_GAME_OK')
