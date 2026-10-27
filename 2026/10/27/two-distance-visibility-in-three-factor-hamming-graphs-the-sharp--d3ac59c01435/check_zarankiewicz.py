"""Check explicit C4-free square matrices and sharp small-order pair bounds."""
from math import comb

M={
2:['11','10'],
3:['110','011','101'],
4:['1110','1001','0101','0011'],
5:['11010','01101','00110','00011','10001'],
6:['110100','011010','001101','000110','100011','010001'],
}
def has_four_cycle(rows):
    n=len(rows)
    for i in range(n):
        for j in range(i+1,n):
            if sum(rows[i][c]=='1' and rows[j][c]=='1' for c in range(n))>=2:return True
    return False

def lower_pair_cost(n,m):
    q,r=divmod(m,n)
    return (n-r)*comb(q,2)+r*comb(q+1,2)

for n,rows in M.items():
    assert len(rows)==n and all(len(x)==n for x in rows)
    total=sum(row.count('1') for row in rows)
    assert not has_four_cycle(rows)
    assert lower_pair_cost(n,total+1)>comb(n,2)
    assert total=={2:3,3:6,4:9,5:12,6:16}[n]
    print(n,total,'upper_by_pair_count',True)

for n in range(7,31):
    rows=[''.join('1' if (j-i)%n in (0,1,3) else '0' for j in range(n))
          for i in range(n)]
    assert not has_four_cycle(rows)
    assert sum(row.count('1') for row in rows)==3*n
print('C4_FREE_CONSTRUCTIONS_OK')
