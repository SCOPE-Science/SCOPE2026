# Independent mathematical audit

## correctness

PASS

On e1=e2=e3=0, the Jacobian has Vandermonde columns (1,-xi,xi²). A rank drop forces at most two values; multiplicities (1,4) force s²=0 after e1, and (2,3) force r=0 then s³=0. Equality of all coordinates is impossible projectively. The resulting smooth connected (2,3) complete intersection has genus 4 by adjunction. A projective fixed point of a three-cycle in characteristic 3 must have a=b=c, then e1,e2,e3 rule it out. The constant C3 action is free, giving a connected finite étale torsor despite 3 dividing the group order. The base-point-free projection [u:v] has degree 6 by its pullback of O(1). Its generic cubic of ordered roots has squarefree discriminant D on the affine base; a transposition negates the nonzero Vandermonde, so adjoining W/v³ gives the degree-two fixed field. The weighted double cover is smooth since the sextic is squarefree with nonzero leading coefficient and characteristic is odd. The identity W=(u+v)³(z³-z), with the generator translating z by 1, gives the full extension and its connectedness gives nontriviality. Independently, near u/v=-1 set s=u/v+1, w=W/v³. Then D=-1+s²-s³+s⁴-s⁶ and w=w0+w0 s²+O(s³) with w0²=-1. The whole polar part of w/s³ is (-w0/s)³-(-w0/s), an explicit local check that no ramification is hidden there. The Cartier coefficients are c2=c4=1, c1=c5=0, and unramified Deuring–Shafarevich gives p-rank 4 upstairs. Independent exact Gröbner reductions confirm the discriminant and Artin–Schreier identities, the translation, squarefreeness, and the empty projective fixed locus: python3 /workspace/branches/independent_reproduction.py bring. The frozen SymPy code was inspected, not executed; finite symbolic checks do not replace the global geometric argument.

## originality

PASS

Credit the known genus-two quotient and fixed-point calculation in characteristic zero and the overlap on good reduction and ordinarity. The supported distinction is the explicit nontrivial étale characteristic-three torsor on the elementary-symmetric model, including its discriminant quotient and Artin–Schreier representative; neither inspected approach gives that identified special-fibre extension.

## value

PASS

For a classical symmetric curve this identifies a concrete unramified nonzero class under a group of order equal to the characteristic. The equations let a researcher work directly with the special-fibre quotient and torsor, rather than extrapolate from characteristic-zero coordinates or merely know the ordinary Newton polygon. The model distinction avoids the degenerate third power-sum equation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
