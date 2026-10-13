# Exact rational Gauss-fiber census for the Asgarli–Ghioca tangent-filling curve
## Finding
Let \(q\ge 11\) be a prime power with \(\operatorname{char}(\mathbb F_q)>3\), and let
\[
C_q:\quad x^{q-1}+y^{q-1}+z^{q-1}-3(x+y+z)^{q-1}=0.
\]
Asgarli and Ghioca prove that this is an irreducible tangent-filling plane curve and that its \(\mathbb F_q\)-points are precisely the points with \(xyz(x+y+z)
e0\); its unique singular point is \([1:1:1]\). On the smooth rational locus, the Gauss map is the restriction of the cubic rational map
\[
\gamma_q([x:y:z])=[yz(2x-y-z):xz(2y-x-z):xy(2z-x-y)].
\]
Every rational Gauss fiber has size at most two. If \(q\equiv1\pmod 3\), the fiber census is
\[
N_1=9q-33,\qquad N_2=\frac{(q-5)(q-7)}2,
\]
where \(N_i\) is the number of rational tangent lines containing exactly \(i\) smooth \(\mathbb F_q\)-tangency points. Thus the number of distinct rational tangent lines arising from smooth rational points is
\[
N_1+N_2=\frac{q^2+6q-31}2.
\]
If \(q\equiv2\pmod3\), then
\[
N_1=7q-23,\qquad N_2=\frac{(q-5)^2}2,
\qquad N_1+N_2=\frac{q^2+4q-21}2.
\]
The singleton-fiber points are exactly the smooth rational points on
\[
R=0\quad\text{or}\quad D=0\quad\text{or}\quad H=0,
\]
where
\[
R=x^2+y^2+z^2-xy-xz-yz,
\]
\[
D=(x+y+z)(xy+xz+yz)-9xyz,
\]
and \(H=0\) is the union of the six lines
\[
x=y,\ x=z,\ y=z,\ 2x=y+z,\ 2y=x+z,\ 2z=x+y.
\]

## Assumptions and scope
The statement concerns only tangents at smooth \(\mathbb F_q\)-points of \(C_q\). A line counted by \(N_2\) is certainly a bitangent in the ordinary sense because it is tangent at two distinct rational smooth points, but the claim does not classify any additional non-rational tangencies that the same line might have. The formulas are proved for every prime power \(q\ge11\) of characteristic greater than \(3\), not merely for prime fields.

## Proof
Write \(s=x+y+z\). For a rational point with \(xyzs
e0\), Fermat gives \(x^{q-2}=x^{-1}\) and similarly for \(y,z,s\). The tangent-line coefficients from the defining equation are therefore projectively
\[
\left[\frac3s-\frac1x:\frac3s-\frac1y:\frac3s-\frac1z\right].
\]
Multiplication by \(sxyz\) gives the displayed cubic map \(\gamma_q\).

Normalize a rational point by \(s=1\), writing \(a=x/s\), \(b=y/s\), \(c=z/s\), so \(a+b+c=1\) and \(abc
e0\). Its tangent vector is
\[
[3-a^{-1}:3-b^{-1}:3-c^{-1}].
\]
Suppose another normalized point \((a',b',c')\) has the same tangent line. Then, for some scalar \(\lambda\),
\[
\frac1{a'}=3(1-\lambda)+\frac\lambda a,
\quad
\frac1{b'}=3(1-\lambda)+\frac\lambda b,
\quad
\frac1{c'}=3(1-\lambda)+\frac\lambda c.
\]
Let \(e_2=ab+ac+bc\), \(e_3=abc\). Clearing denominators in \(a'+b'+c'=1\) gives
\[
-\lambda(\lambda-1)\left((9e_2-27e_3-2)\lambda-3e_2+27e_3\right)=0.
\]
The root \(\lambda=0\) gives \((1/3,1/3,1/3)\), the singular point where the Gauss vector vanishes; \(\lambda=1\) gives the original point. Consequently there is at most one further smooth rational point in the fiber.

Set
\[
R_0=1-3e_2,\qquad D_0=e_2-9e_3.
\]
When nondegenerate, the second scalar is
\[
\lambda_2=\frac{3D_0}{3D_0-2R_0}.
\]
Moreover
\[
\lambda_2+3(1-\lambda_2)a
=\frac{3(D_0-2aR_0)}{3D_0-2R_0},
\]
and similarly for \(b,c\). Thus a distinct second smooth rational point exists exactly away from the zero loci of \(R_0\), \(D_0\), \(3D_0-2R_0\), and the three expressions \(D_0-2aR_0\), \(D_0-2bR_0\), \(D_0-2cR_0\).

Returning to homogeneous coordinates, put
\[
R=x^2+y^2+z^2-xy-xz-yz,
\quad
D=(x+y+z)(xy+xz+yz)-9xyz.
\]
The exceptional factors reduce to the six lines because
\[
D-2xR=-(x-y)(x-z)(2x-y-z),
\]
\[
D-2yR=-(x-y)(y-z)(x-2y+z),
\]
\[
D-2zR=(x-z)(y-z)(x+y-2z),
\]
and
\[
3D-2(x+y+z)R=-(x-2y+z)(x+y-2z)(2x-y-z).
\]
Hence the singleton points are exactly the smooth rational points on \(R\cup D\cup H\).

It remains to count this exceptional set. The six lines in \(H\) all pass through \([1:1:1]\). Each has exactly three points on the boundary \(xyz(x+y+z)=0\); after removing those and the singular point, each contributes \(q-3\) points. Their smooth contributions are pairwise disjoint, so
\[
\#(H\cap C_q^{\rm sm}(\mathbb F_q))=6q-18.
\]
The conic \(R=0\) is a pair of conjugate lines through \([1:1:1]\). It splits over \(\mathbb F_q\) exactly when \(q\equiv1\pmod3\). In the split case each line contributes \(q-4\) smooth points off the four boundary lines and the common singular point, hence \(2q-8\) in total; in the nonsplit case its only rational point is their intersection \([1:1:1]\), so it contributes none.

The cubic \(D=0\) is a nodal rational cubic with node \([1:1:1]\). In the chart \(z=1\), set \(x=1+u\), \(y=1+v\). Then
\[
D=u^2v+uv^2+2u^2-2uv+2v^2.
\]
A line \(v=mu\) through the node meets the cubic again at
\[
u=-\frac{2(m^2-m+1)}{m(m+1)},
\]
with the usual projective interpretation at exceptional slopes. The two normalization points above the node satisfy \(m^2-m+1=0\). They are rational exactly when \(q\equiv1\pmod3\). Thus \(D(\mathbb F_q)\) has \(q\) points in the split-node case and \(q+2\) in the nonsplit-node case. Besides the node, exactly six rational points of \(D\) lie on \(xyz(x+y+z)=0\), namely the three coordinate vertices and \([0:1:-1]\), \([1:0:-1]\), \([1:-1:0]\). Therefore the smooth contribution of \(D\) is \(q-7\) when \(q\equiv1\pmod3\) and \(q-5\) when \(q\equiv2\pmod3\).

These three exceptional pieces are disjoint on the smooth rational locus. For \(R\cap D\), normalize \(x+y+z=1\): \(R=0\) forces \(e_2=1/3\) and \(D=0\) forces \(e_3=1/27\), so \(x,y,z\) are all \(1/3\), the excluded singular point. Restricting \(R\) and \(D\) to any of the six lines of \(H\) likewise leaves only the singular point or boundary points.

Hence the singleton count is \(6q-18+(2q-8)+(q-7)=9q-33\) in the split case and \(6q-18+(q-5)=7q-23\) in the nonsplit case. Finally, four lines in general position are removed from \(\mathbb P^2(\mathbb F_q)\), so the smooth rational locus has
\[
(q^2+q+1)-(4q-2)-1=(q-1)(q-2)
\]
points. Since every Gauss fiber has size one or two, \(N_2=((q-1)(q-2)-N_1)/2\), which yields the stated formulas.

## Verification
The accompanying verifier checks the homogeneous factor identities exactly using integer polynomial arithmetic and independently enumerates the rational Gauss fibers over several prime fields, including both congruence classes modulo \(3\). It also checks that the singleton points from direct tangent-line fibers coincide with the union \(R\cup D\cup H\) in those witnesses. The proof above, rather than the finite tests, establishes the result for every admitted prime power.

## Relationship to prior work
Asgarli and Ghioca introduce tangent-filling curves, prove that the displayed degree-\(q-1\) curve is irreducible and tangent-filling for \(q\ge11\) in characteristic greater than \(3\), identify its rational points, and determine its unique singular point. Their paper also discusses Gauss maps and general bitangent bounds, but its explicit-example section does not give the rational Gauss-fiber census above. Searches by the source identifier, exact defining equation, “Gauss map”, “bitangent”, “rational tangent”, and equivalent fiber-count formulations did not locate this exact census in the inspected source or indexed comparison records.

## Limitations
This is a statement about the map on smooth \(\mathbb F_q\)-points. It does not determine the complete geometric Gauss map over an algebraic closure, the full singularity scheme of the dual curve, or whether a tangent line counted here has additional non-rational tangency points. The originality search cannot exclude an unindexed calculation in finite-geometry or dual-curve literature under different terminology.

## References
1. S. Asgarli and D. Ghioca, “Tangent-filling plane curves over finite fields,” arXiv:2302.13420, first public version 26 February 2023; Bulletin of the Australian Mathematical Society 109 (2024), 301–315, DOI 10.1017/S0004972723000382.
2. A. H. Wallace, “Tangency and duality over arbitrary fields,” Proceedings of the London Mathematical Society (3) 6 (1956), 321–342, cited by Asgarli–Ghioca for Gauss-map background.
