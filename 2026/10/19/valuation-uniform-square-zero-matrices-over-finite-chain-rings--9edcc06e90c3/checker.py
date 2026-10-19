"""Direct exhaustive checks for square-zero 2x2 matrix counts over finite chain rings."""
from itertools import product


def formula(q, length):
    return q ** (4 * (length // 2)) + ((length + 1) // 2) * (q*q - 1) * q ** (2*length-2)


def v_p(x, p, length):
    if x == 0:
        return length
    v = 0
    while v < length and x % p == 0:
        x //= p
        v += 1
    return v


def check_mod_p_power(p, length):
    M = p ** length
    counts = [0] * (length + 1)
    for a,b,c,d in product(range(M),repeat=4):
        if ((a*a + b*c) % M == 0 and b*(a+d) % M == 0
                and c*(a+d) % M == 0 and (d*d+b*c) % M == 0):
            counts[min(v_p(z,p,length) for z in (a,b,c,d))] += 1
    expected = []
    for val in range(length):
        if 2*val < length:
            expected.append((p*p-1)*p**(2*length-2))
        else:
            expected.append(p**(4*(length-val))-p**(4*(length-val-1)))
    expected.append(1)
    assert counts == expected, (p,length,counts,expected)
    assert sum(counts) == formula(p,length)
    return counts


def mul_f4(x, y):
    # F_4 = F_2[u]/(u^2+u+1), represented by bit vectors.
    a,b=x&1,(x>>1)&1
    c,d=y&1,(y>>1)&1
    return (a*c ^ b*d) | ((a*d ^ b*c ^ b*d)<<1)


def mul_f4_t(x,y,length):
    # Ring F4[t]/t^length with base-4 digit coefficients.
    a=[(x>>(2*j))&3 for j in range(length)]
    b=[(y>>(2*j))&3 for j in range(length)]
    out=[0]*length
    for i in range(length):
        for j in range(length-i):
            out[i+j] ^= mul_f4(a[i],b[j])
    return sum(v<<(2*j) for j,v in enumerate(out))


def check_f4(length):
    size=4**length
    mult=[[mul_f4_t(i,j,length) for j in range(size)] for i in range(size)]
    count=[0]*(length+1)
    def val(x):
        if x==0: return length
        v=0
        while x & 3 == 0:
            x >>= 2
            v+=1
        return v
    for a,b,c,d in product(range(size),repeat=4):
        bc=mult[b][c]
        s=a^d
        if (mult[a][a]^bc)==0 and mult[b][s]==0 and mult[c][s]==0 and (mult[d][d]^bc)==0:
            count[min(val(z) for z in (a,b,c,d))] +=1
    target=[]
    for v in range(length):
        if 2*v <length:
            target.append((4**2-1)*4**(2*length-2))
        else:
            target.append(4**(4*(length-v))-4**(4*(length-v-1)))
    target.append(1)
    assert count == target,(length,count,target)
    return count


def main():
    samples=[(2,1),(2,2),(2,3),(2,4),(3,1),(3,2),(3,3),(5,1),(5,2)]
    for p,n in samples:
        values=check_mod_p_power(p,n)
        print('Z/%dZ'% (p**n), 'q',p,'length',n,'valuation_counts',values,'total',sum(values))
    for length in (1,2):
        values=check_f4(length)
        print('F4[t]/t^%d'%length,'q',4,'valuation_counts',values,'total',sum(values))
    print('VERIFY_OK')

if __name__ == '__main__':
    main()
