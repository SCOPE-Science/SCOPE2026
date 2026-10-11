# Sharp volume interval for concentric bicentric tetrahedra

## Finding
Let \(T\) be a nondegenerate Euclidean tetrahedron with concentric insphere and circumsphere. Write their radii as \(\rho>0\) and \(R\), and put \(q=R/\rho\) and \(Q=q^2\). Then \(T\) exists exactly when \(q\ge3\). For fixed \(q\), the set of all possible tetrahedral volumes is the entire closed interval
\[
[V_-,V_+],
\]
where
\[
V_\pm=\frac{{2\sqrt2}}{{3}}\,\rho^3
\sqrt{{Q^2+18Q-27\ \pm\ \sqrt{{(Q-9)^3(Q-1)}}}}.
\]
When \(q=3\), both endpoints equal \(8\sqrt3\,\rho^3\), and the tetrahedron is regular. When \(q>3\), both bounds are sharp and are attained by distinct additional-symmetry disphenoids.

More precisely, define
\[
u_\pm=\frac{{Q+3\pm\sqrt{{(Q-1)(Q-9)}}}}{{4Q}}.
\]
After a rigid motion, every tetrahedron under discussion has vertices
\[
(\alpha,\beta,\gamma),\quad
(\alpha,-\beta,-\gamma),\quad
(-\alpha,\beta,-\gamma),\quad
(-\alpha,-\beta,\gamma),
\]
with \(\alpha,\beta,\gamma>0\). At the lower-volume endpoint, the normalized squared half-axes \((\alpha^2/R^2,\beta^2/R^2,\gamma^2/R^2)\) are a permutation of \((u_-,u_-,1-2u_-)\); at the upper endpoint they are a permutation of \((u_+,u_+,1-2u_+)\). These are the only endpoint shapes up to congruence.

## Assumptions and scope
The statement concerns ordinary nondegenerate Euclidean tetrahedra having both an insphere tangent to all four faces and a circumsphere through all four vertices, with the two sphere centers identical. The radii \(\rho\) and \(R\) are fixed positive real numbers. No assertion is made for nonconcentric nested spheres or for general ellipsoids.

A classical characterization says that a tetrahedron has coincident incenter and circumcenter if and only if it is an isosceles tetrahedron, equivalently a disphenoid with opposite edges pairwise equal. Katsuura records this equivalence explicitly. The proof below then supplies the metric optimization directly and does not use a pre-existing volume extremum.

## Proof
Translate the common sphere center to the origin. For a disphenoid with centroid at the origin, write its vertices as \(p,q,r,s\), with \(p+q+r+s=0\), and set
\[
u=\frac{p+q}{2},\qquad v=\frac{p+r}{2},\qquad w=\frac{p+s}{2}.
\]
Then
\[
p=u+v+w,\quad q=u-v-w,\quad r=-u+v-w,\quad s=-u-v+w.
\]
The three opposite-edge equalities imply respectively \(v\cdot w=0\), \(u\cdot w=0\), and \(u\cdot v=0\). After an orthogonal change of coordinates, the vertices therefore have the displayed alternating-box form with positive half-axes \(\alpha,\beta,\gamma\).

The common circumradius satisfies
\[
R^2=\alpha^2+\beta^2+\gamma^2.
\]
One face plane is
\[
\frac{x}{\alpha}+\frac{y}{\beta}+\frac{z}{\gamma}=-1,
\]
and the other three have the corresponding sign changes. Hence the common distance from the origin to the four faces is
\[
\rho=\frac{1}{\sqrt{\alpha^{-2}+\beta^{-2}+\gamma^{-2}}}.
\]
Define
\[
a=\frac{\alpha^2}{R^2},\qquad b=\frac{\beta^2}{R^2},\qquad c=\frac{\gamma^2}{R^2}.
\]
Then \(a,b,c>0\) and
\[
a+b+c=1,\qquad \frac1a+\frac1b+\frac1c=Q.
\]
In particular \(Q\ge9\) by the harmonic-arithmetic mean inequality, with equality exactly at \(a=b=c=1/3\). This already gives \(R\ge3\rho\) and the regular equality case.

Put \(s=abc\). The reciprocal-sum identity gives
\[
ab+bc+ca=Qs.
\]
Thus \(a,b,c\) are the three roots of
\[
f_s(t)=t^3-t^2+Qs\,t-s.
\]
Its discriminant is
\[
\operatorname{{disc}}(f_s)
=-s\left(4Q^3s^2-(Q^2+18Q-27)s+4\right).
\]
For \(Q\ge9\), the two positive roots of the quadratic factor are
\[
s_\pm=\frac{{Q^2+18Q-27\pm\sqrt{{(Q-9)^3(Q-1)}}}}{{8Q^3}}.
\]
Hence every feasible triple has \(s\in[s_-,s_+]\).

Conversely, each \(s\in[s_-,s_+]\) gives three positive real roots. Indeed, the discriminant is nonnegative. The endpoint cubics have positive roots, and on the open interval the roots are real and distinct. They cannot consist of one positive and two negative roots: if the negative roots are \(-y,-z\) with \(y,z>0\), then their sum condition gives the positive root \(1+y+z\), whereas positivity of the pair sum would require \(yz>(y+z)+(y+z)^2\), contradicting \(yz\le (y+z)^2/4\). Thus the whole interval of \(s\) is realized by positive \(a,b,c\).

The determinant of the three edge vectors gives
\[
\operatorname{{vol}}(T)=\frac83\alpha\beta\gamma,
\]
so
\[
\operatorname{{vol}}(T)^2
=\frac{{64}}9 R^6s
=\frac{{64}}9\rho^6Q^3s.
\]
Substitution of \(s_\pm\) yields exactly the two displayed formulas for \(V_\pm\). Since the realized values of \(s\) fill the full interval \([s_-,s_+]\), the realized volumes fill \([V_-,V_+]\).

At either endpoint the discriminant vanishes, so exactly two of \(a,b,c\) coincide when \(Q>9\). Writing the repeated root as \(u\) and the third as \(1-2u\), the reciprocal-sum constraint reduces to
\[
2Qu^2-(Q+3)u+2=0.
\]
Its roots are \(u_-\) and \(u_+\) above. Direct substitution shows \(u_-^2(1-2u_-)=s_-\) and \(u_+^2(1-2u_+)=s_+\), proving the endpoint classification.

## Verification
The proof is algebraic and applies for every real \(q\ge3\). The accompanying `verify.py` is only a finite consistency check: it enumerates positive rational triples \((a,b,c)\) on denominator grids, reconstructs \(Q\), checks the claimed volume interval numerically, and separately checks the endpoint formulas over a range of integer \(Q\). It does not substitute for the discriminant proof.

Expected output from the packaged verifier is recorded in `VERIFICATION.md`.

## Relationship to prior work
Gibson, Saldanha, and Tomei study simplices tightly fitted between centered ellipsoids. Their three-dimensional remark gives an explicit alternating tetrahedral family and the tightness equation; in the concentric spherical specialization this is the same one-parameter bicentric family considered here. Their inspected text does not state a volume range, and a full-text term search found no occurrence of “volume.”

Milne gives the Grace--Danielsson existence criterion for a tetrahedron nested between two spheres. At zero center separation it reduces to the familiar necessary and sufficient condition \(R\ge3\rho\), but the inspected text does not determine the attainable volumes. Katsuura records the classical equivalence between coincident incenter/circumcenter and the isosceles-tetrahedron condition; his result supplies the structural reduction, not the sharp volume interval.

The new step is the elimination of the remaining one-dimensional shape freedom at fixed \((R,\rho)\): the cubic discriminant gives the exact product interval, which is exactly the volume interval, and identifies both equality shapes.

## Limitations
The originality comparison is limited to the inspected modern primary sources and targeted searches. Older treatments of isosceles tetrahedra, including classical monographs and Leech's 1950 paper, remain a residual literature risk because not every full text was accessible. The claim is therefore a supported noncoverage assessment, not an assertion of exhaustive historical priority.

The theorem is specific to concentric spheres in dimension three. It does not classify volume for nonconcentric bicentric tetrahedra, higher-dimensional simplices, or general ellipsoids.

## References
1. P. Gibson, N. Saldanha, and C. Tomei, *Higher dimensional versions of theorems of Euler and Fuss*, arXiv:2210.17350v1 (2022).
2. H. Katsuura, *Characterization of an Isosceles Tetrahedron*, Journal for Geometry and Graphics 23 (2019), 37--40.
3. A. Milne, *The Euler and Grace--Danielsson inequalities for nested triangles and tetrahedra: a derivation and generalisation using quantum information theory*, Journal of Geometry 106 (2015), 455--463; arXiv:1404.0525.
