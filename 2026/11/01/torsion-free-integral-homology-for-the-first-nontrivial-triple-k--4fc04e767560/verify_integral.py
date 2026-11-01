"""Exact integral homology verification for both finite Morse certificates.
Run with Python 3 and SymPy after the C++ certificate generator.
"""
from pathlib import Path
from sympy import ZZ, Matrix
from sympy.matrices.normalforms import smith_normal_form

def read_matrix(d, prefix):
    tokens = Path(f'{prefix}{d}.txt').read_text(encoding='ascii').split()
    r, c = map(int, tokens[:2])
    values = list(map(int, tokens[2:]))
    assert len(values) == r * c
    return Matrix(r, c, values)

def verify(prefix, dimensions, ranks, critical):
    A, B, C = (read_matrix(d, prefix) for d in (7, 8, 9))
    assert tuple(x.shape for x in (A,B,C)) == dimensions
    assert A*B == Matrix.zeros(A.rows,B.cols)
    assert B*C == Matrix.zeros(B.rows,C.cols)
    for d, mat, rank in zip((7,8,9),(A,B,C),ranks):
        smith = smith_normal_form(mat, domain=ZZ)
        diag = [abs(int(smith[i,i])) for i in range(min(smith.rows,smith.cols)) if smith[i,i] != 0]
        assert diag == [1]*rank, (prefix,d,diag)
        print(f'{prefix}{d} shape={mat.rows}x{mat.cols} Smith=1^{rank} zero={min(mat.rows,mat.cols)-rank}')
    # For this augmented complex the only critical degrees are 6,7,8,9.
    assert (critical[0]-ranks[0], critical[1]-ranks[0]-ranks[1],
            critical[2]-ranks[1]-ranks[2], critical[3]-ranks[2]) == (29,0,0,7)
    print(f'{prefix}: integral groups Z^29 in degree 6, Z^7 in degree 9, zero otherwise')

if __name__ == '__main__':
    verify('boundary', ((60,41),(41,11),(11,8)), (31,10,1), (60,41,11,8))
    verify('reverse_boundary', ((45,27),(27,16),(16,12)), (16,11,5), (45,27,16,12))
    print('INTEGRAL_HOMOLOGY_CERTIFICATE_OK')
