"""Finite, self-contained checks of the explicit tree-product retraction scheme.
Not a substitute for the general proof."""
from itertools import product

def maps(parent_arrays):
    dims=len(parent_arrays)
    levels=[list(range(len(p))) for p in parent_arrays]
    vs=list(product(*levels)) # lex tree parents before children
    to_index={v:i for i,v in enumerate(vs)}
    def older(v):
        if dims==1:
            return (parent_arrays[0][v[0]],)
        if dims==2:
            a,b=v
            if a and b:return (parent_arrays[0][a],parent_arrays[1][b])
            if a:return (parent_arrays[0][a],b)
            return (a,parent_arrays[1][b])
        if v[0]:return (parent_arrays[0][v[0]],)+v[1:]
        sub = maps(parent_arrays[1:])[2]
        return (0,)+sub(v[1:])
    parents={v:older(v) for v in vs[1:]}
    trees=[]
    for arr in parent_arrays:
        da=[[None]*len(arr) for _ in arr]
        for i in range(len(arr)):
            for j in range(len(arr)):
                x=i;ax={};d=0
                while True:
                    ax[x]=d
                    if x==0:break
                    x=arr[x];d+=1
                x=j;d=0
                while x not in ax:
                    x=arr[x];d+=1
                da[i][j]=ax[x]+d
        trees.append(da)
    def dist(x,y):return sum(da[xi][yi] for da,xi,yi in zip(trees,x,y))
    max_lip=0
    for k in range(1,len(vs)+1):
        r={}
        for v in vs:
            w=v
            while to_index[w]>=k:w=parents[w]
            r[v]=w
        for i,x in enumerate(vs):
            for y in vs[i+1:]:
                rat=dist(r[x],r[y])/dist(x,y)
                max_lip=max(rat,max_lip)
                assert rat <= (1 if dims<=2 else 2),(parent_arrays,k,x,y,rat)
    return max_lip,vs,older

if __name__=='__main__':
 for cases in [
   [[0,0],[0,0]],
   [[0,0,1,2],[0,0,0,1]],
   [[0,0,0,0],[0,0,0]],
   [[0,0],[0,0],[0,0]],
   [[0,0,0],[0,0],[0,0]],
   [[0,0,0],[0,0,0],[0,0]],
   [[0,0],[0,0],[0,0],[0,0]],
   [[0,0,1,2],[0,0],[0,0]]]:
  k,vs,p=maps(cases); print('factors',list(map(len,cases)),'vertices',len(vs),'largest-Lipschitz',k)
