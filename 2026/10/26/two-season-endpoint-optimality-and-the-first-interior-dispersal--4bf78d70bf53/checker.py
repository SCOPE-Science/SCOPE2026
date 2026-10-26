"""Exact finite checks for symmetric-migration alternating-environment growth."""
import json
from pathlib import Path
from sympy import Matrix, eye, diag, Rational, sqrt, simplify


def root_diag(values):
    return diag(*[sqrt(value) for value in values])


def spectral_norm_identity(n, d, C, a, b):
    D1 = diag(*a)
    D2 = diag(*b)
    M = (1-d)*eye(n)+d*C
    A = root_diag(b)*M*root_diag(a)
    P = M*D2*M*D1
    H = root_diag(a)*P*root_diag([Rational(1,x) for x in a])
    return all(simplify(z)==0 for z in (H-A.T*A))


def run():
    examples = [
        (2, Matrix([[0,1],[1,0]]), [4,9], [25,16]),
        (2, Matrix([[0,Rational(1,2)],[Rational(1,2),0]]), [1,16], [36,9]),
        (3, Matrix([[0,Rational(1,3),Rational(1,3)],
                    [Rational(1,3),0,Rational(1,3)],
                    [Rational(1,3),Rational(1,3),0]]), [1,4,9], [16,9,4]),
        (4, Matrix([[0,Rational(1,3),0,Rational(1,3)],
                    [Rational(1,3),0,Rational(1,3),0],
                    [0,Rational(1,3),0,Rational(1,3)],
                    [Rational(1,3),0,Rational(1,3),0]]), [1,4,9,16], [25,16,9,4]),
    ]
    rates = [Rational(0), Rational(1,9), Rational(1,4), Rational(1,2),
             Rational(2,3), Rational(7,8), Rational(1)]
    checked = 0
    for n,C,a,b in examples:
        for d in rates:
            assert spectral_norm_identity(n,d,C,a,b)
            checked += 1

    # Two-sites alternate optimal no-dispersal / full-dispersal at an exact cost threshold.
    a,b = Rational(9), Rational(4)
    c = Rational(2,3)
    F = Matrix([[0,1],[1,0]])
    D1,D2 = diag(a,b),diag(b,a)
    two_season = {}
    for d in [Rational(0), Rational(1,4), Rational(1,2),Rational(3,4), Rational(1)]:
        M=(1-d)*eye(2)+d*c*F
        P=M*D2*M*D1
        assert P.det() >= 0 and P.trace() > 0
        if 0 < d < 1:
            # Both eigenvalues of P lie in [0,36) because trace<72 and
            # det(36 I-P)>0 with positivity of eigenvalues.
            assert P.trace()<72 and (36*eye(2)-P).det()>0
        else:
            assert max(P.eigenvals().keys()) == 36
        two_season[str(d)] = {'trace':str(P.trace()), 'determinant':str(P.det())}

    D2=diag(1,4);D3=diag(4,1)
    tri = {}
    for d in [Rational(0),Rational(1,2),Rational(1)]:
        M=(1-d)*eye(2)+d*F
        P=M*D3*M*D2*M
        eigenvalues=set(P.eigenvals())
        expected=({Rational(4)} if d==0 else
                  ({Rational(0),Rational(25,4)} if d==Rational(1,2)
                   else {Rational(-4),Rational(4)}))
        assert eigenvalues==expected
        exact_eigen=[str(x) for x in sorted(eigenvalues)]
        tri[str(d)]={'matrix':[[str(P[i,j]) for j in range(2)] for i in range(2)],
                     'eigenvalues':exact_eigen,'spectral_radius':str(Rational(25,4) if d==Rational(1,2) else 4)}
    return {'schema_version':1,'arithmetic':'exact rational and symbolic matrices',
            'two_season_similarity_identities_checked':checked,
            'two_season_tie_example':two_season,
            'three_season_interior_example':tri,
            'limits':'Finite checks illustrate algebra; the unrestricted theorem is proved separately.'}

if __name__=='__main__':
    cert=run()
    out=Path(__file__).with_name('verification_certificate.json')
    out.write_text(json.dumps(cert,ensure_ascii=False,indent=2,sort_keys=True)+'\n',encoding='utf8')
    print(json.dumps({'result':'pass','identities':cert['two_season_similarity_identities_checked'],'certificate':str(out.name)},sort_keys=True))
