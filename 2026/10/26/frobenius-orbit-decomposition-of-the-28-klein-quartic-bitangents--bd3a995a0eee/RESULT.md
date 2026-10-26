# Frobenius orbit decomposition of the 28 Klein-quartic bitangents over \(\mathbf F_5\)

## Finding

For the smooth plane Klein quartic \(C: X^3Y+Y^3Z+Z^3X=0\) over \(\mathbf F_5\), the geometric set of 28 bitangent lines has Frobenius orbit lengths \(1,3,6,6,6,6\). The only rational bitangent is \(X+Y+Z=0\); all 28 are defined over \(\mathbf F_{5^6}\), and no smaller common extension defines all of them. In particular, the number of \(\mathbf F_{5^n}\)-rational bitangents is \(1+3\mathbf 1_{3\mid n}+24\mathbf 1_{6\mid n}\) for all positive integers \(n\).

The new arithmetic assertion is the full six-orbit Frobenius splitting, not the already-known rational bitangent.

## Assumptions and scope

Work over \(k=\mathbf F_5\) and its algebraic closure. By a geometric bitangent we mean a projective line whose intersection divisor with the smooth plane quartic is twice an effective degree-two divisor (a hyperflex counts). Frobenius means the absolute \(5\)-power automorphism on line coefficients. A line is rational over \(\mathbf F_{5^n}\) when its projective line coefficients can be chosen in that field.

The curve is smooth: its gradient has entries \(3X^2Y+Z^3\), \(X^3+3Y^2Z\), and \(Y^3+3Z^2X\). No singular point lies on a coordinate line. When all coordinates are nonzero, multiplying the three gradient equalities forces \(1=(-3)^3\), or \(28=0\), contrary to characteristic \(5\). A smooth plane quartic has genus three and exactly \(2^{g-1}(2^g-1)=28\) geometric bitangents in characteristic different from two, via odd theta characteristics.

## Proof

Every projective line not passing through \(P=[0:0:1]\) has a unique equation \(Z=uX+vY\). The unique tangent through \(P\) is \(X=0\); its divisor on the quartic is \(3P+[0:1:0]\), so it is not a bitangent. Thus every bitangent occurs in the \((u,v)\)-chart.

Substitution into the quartic gives the binary form
\[
A X^4+B X^3Y+C X^2Y^2+D XY^3+E Y^4,
\quad(A,B,C,D,E)=(u^3,1+3u^2v,3uv^2,u+v^3,v).
\]
For \(u=0\), the coefficient of \(X^4\) is zero but that of \(X^3Y\) is one; this cannot be a scalar multiple of a quadratic square, so \(u\ne0\) on all bitangents.

For \(A\ne0\), comparison with \((aX^2+bXY+cY^2)^2\), permitting a nonzero scalar absorbed into the square over the algebraic closure, shows the quartic is a square if and only if
\[
P=8A^2D-4ABC+B^3=0,\qquad
Q=64A^3E-(4AC-B^2)^2=0.
\]
Indeed choose \(a^2=A\), \(b=B/(2a)\), and \(c=(4AC-B^2)/(8Aa)\). The remaining two coefficient equations are exactly \(P=Q=0\).

An exact resultant computation in \(\mathbf F_5[u,v]\) gives
\[
\operatorname{Res}_v(P,Q)=-4096u^{24}H(u)\quad\text{in }\mathbf F_5[u],
\]
with the factorization
\[
H(u)=(u+1)(u^3+u^2+1)
(u^6-2u^4+u^3+u^2+u+1)
(u^6-2u^5+u^3+2u^2+u+1)
(u^6+u^5-u^3-u^2-2u+1)
(u^6-u^5+u^4-u^3+u^2-u+1).
\]

The factors are distinct and irreducible over \(\mathbf F_5\), of degrees \(1,3,6,6,6,6\); the standalone exact checker verifies both identities and irreducibility. Each factor has nonzero constant term. Since the leading \(v\)-coefficients of \(P,Q\) are respectively \(-u^6\) and \(-9u^8\), every nonzero root of the resultant gives a common \(v\)-root over the algebraic closure. The 28 distinct nonzero \(u\)-roots therefore yield at least 28 distinct geometric bitangents. As there are exactly 28, no other lines exist and each \(u\)-root determines precisely one \(v\). Thus the Frobenius orbit degrees of the \(u\)-roots are exactly the orbit degrees of the bitangent lines, as asserted.

For \(u=v=-1\), direct substitution gives
\[
F(X,Y,-X-Y)=-(X^2+XY+Y^2)^2.
\]
This is the unique length-one orbit. Over \(\mathbf F_{5^n}\), each Frobenius orbit contributes its entire length precisely when its length divides \(n\), proving the counting formula and the minimal common splitting field \(\mathbf F_{5^6}\).

## Verification

Run `python klein_bitangent_verify.py` with SymPy installed. It recomputes the binary-form coefficient conditions, the exact resultant identity modulo \(5\), squarefreeness and irreducibility of all six factors, the unique \(\mathbf F_5\)-pair \((u,v)=(-1,-1)\), and the explicit rational bitangent identity. The checker returns `VERIFY_OK` when all tests pass. The finite computation is exhaustive because the proof reduces all geometric bitangents to the exact eliminant and the classical 28-count, not because of numerical sampling.

## Relationship to prior work

Elkies describes the Klein quartic and exhibits the bitangent \(X+Y+Z=0\); its rationality is not claimed to be new. Dalla Piazza–Fiorentino–Salvati Manni discuss the classical 28-bitangent correspondence. Bethea–Brazelton compute the transitive action of the complex geometric automorphism group on the bitangents. Those statements concern a distinguished line, geometric bitangents and geometric symmetry; none implies the explicit \(\mathbf F_5\)-Frobenius partition or minimal degree-six splitting field. The recorded searches did not locate an equivalent arithmetic classification.

## Limitations

The result is for this explicit \(\mathbf F_5\)-model and its geometric lines; it does not classify twisted Klein quartics, the Galois structure of all characteristic-five moduli, or the distribution at other primes. Some historical sources may contain an equivalent finite-field specialization not identified here. No independent audit has been performed.

## References

1. N. D. Elkies, *The Klein Quartic in Number Theory*, in *The Eightfold Way* (1999), section on the 28 bitangents. https://dash.harvard.edu/entities/publication/73120378-7d3e-6bd4-e053-0100007fdf3b
2. F. Dalla Piazza, A. Fiorentino, R. Salvati Manni, *Plane quartics: the matrix of bitangents*, arXiv:1409.5032 (initial posting September 17, 2014). https://arxiv.org/abs/1409.5032
3. C. Bethea, T. Brazelton, *Bitangents to symmetric quartics*, arXiv:2410.09242, section 4.1 (Klein quartic geometric automorphism action). https://arxiv.org/abs/2410.09242
