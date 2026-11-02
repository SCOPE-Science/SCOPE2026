"""Independent finite checks of the extremal minimal-absent-word theorem."""
from collections import defaultdict


def iterate(level):
    s = '1'
    for _ in range(level):
        s = ''.join('101' if c == '1' else '000' for c in s)
    return s


def factor_positions(w, m):
    out = defaultdict(list)
    for i in range(len(w)-m+1):
        out[w[i:i+m]].append(i)
    return out


def maximal_maws(w, m):
    smaller = set(factor_positions(w, m-1))
    present = set(factor_positions(w,m))
    return {s+t for s in smaller for t in '01'
            if s+t not in present and (s+t)[1:] in smaller}


def check(limit=7):
    for k in range(2, limit+1):
        w=iterate(k)
        g=3**(k-1);h=3**(k-2)
        prev=iterate(k-2)
        block=iterate(k-1)
        f='0'*h+prev+'0'*h
        repeated={u:locs for u,locs in factor_positions(w,g).items() if len(locs)>1}
        assert repeated=={block:[0,2*g],f:[h,2*g-h]},(k,repeated)
        assert all(len(locs)==1 for locs in factor_positions(w,g+1).values()),k
        expected={'0'+block+'0','0'+f+'0','1'+f+'1'}
        result=maximal_maws(w,g+2)
        assert expected==result,(k,expected,result)
        for s in expected:
            assert s not in w and s[:-1] in w and s[1:] in w
        if k <= 4:
            by_length = {}
            for ell in range(2, len(w) + 2):
                maws = maximal_maws(w, ell)
                if maws:
                    by_length[ell] = maws
            assert max(by_length) == g+2
            assert by_length[g+2] == expected
        print(f'k={k}, length={len(w)}, max_MAW_length={g+2}, candidates={len(result)}, repeated_length_g={len(repeated)}')
    print('PASS')

if __name__=='__main__':check()
