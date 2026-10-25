"""Independent finite checks of strong-majority edge colouring constructions."""
from math import ceil

def valid(mat, colors):
    m, n = len(mat), len(mat[0]); lim = (m + n - 2)//2
    assert all(len(row)==n and all(0 <= v < colors for v in row) for row in mat)
    for i in range(m):
        for j in range(n):
            for color in range(colors):
                count = sum(mat[i][k]==color for k in range(n) if k!=j) + sum(mat[k][j]==color for k in range(m) if k!=i)
                assert count <= lim, (m,n,i,j,color,count,lim)

special_44 = [[0,1,0,0],[2,2,0,1],[0,1,1,2],[2,2,1,0]]
special_47 = [[2,1,1,2,2,0,0],[0,1,2,0,2,1,1],[1,0,0,1,0,2,2],[2,0,0,2,0,1,1]]
valid(special_44,3); valid(special_47,3)
valid([[(i+j)%4 for j in range(4)] for i in range(3)],4)
valid([[(i+j)%4 for j in range(5)] for i in range(4)],4)
for n in range(2,101):
    if n%2==0:
        row=[j//(n//2) for j in range(n)]
        valid([row,row],2)
    else:
        row=[0]*(n//2)+[1]*(n//2)+[2]
        valid([row,row],3)
count=0
for m in range(3,17):
  for n in range(m,17):
    cond=ceil(m/3)+ceil(n/3) <= (m+n-2)//2
    if cond:
        valid([[(i+j)%3 for j in range(n)] for i in range(m)],3)
        count+=1
    else:
        assert (m,n) in {(3,4),(4,4),(4,5),(4,7)},(m,n)
print('VERIFY_OK periodic_pairs=',count,'two_row_instances=',99,'finite_exceptions=4')
