# Trivial vanishing-cycle monodromy on the accidental rank-four stratum of a determinantal quintic

## Finding

Let \(M\) be the symmetric matrix displayed below, and let \(Q=V(F)\subset\mathbb C^5\), where \(F=\det M\). For the open surface
\[
S=\{(0,s,t,s,0):(s^2-4)(t^2-4)\ne0\}\subset Q,
\]
the following hold simultaneously:

1. The analytic germ of \(Q\) at each point of \(S\), with its marked smooth singular stratum, is a product of a smooth two-dimensional germ and the ordinary surface node \(A^2+B^2+D^2=0\).
2. The reduced integral cohomology of a sufficiently small transverse Milnor fiber is \(\widetilde H^2\cong\mathbb Z\), zero in all other degrees. These groups form the **constant** rank-one integral local system on all of \(S\), not just on a simply connected chart.
3. The hypersurface is rationally smooth along \(S\): at each such point its local rational intersection-cohomology stalk has the same ranks as a smooth complex fourfold point.

Here the vanishing-cycle local system is the one obtained by varying the transverse Milnor fibers of the fixed polynomial \(F\) *along* the critical stratum. It must not be confused with the Picard–Lefschetz monodromy obtained by circling the smoothing parameter, which acts as \(-1\) for a surface node.

## Assumptions and scope

Work over \(\mathbb C\). The coordinates of \(\mathbb C^5\) are \((x,y,z,w,v)\). Fix the boundary traces \((-2,0,0,0,0)\) in Hikami's symmetric-matrix construction for the five-punctured sphere, and set
\[
M=\begin{pmatrix}
2&2&-x&-w&0\\
2&2&0&-y&-v\\
-x&0&2&0&-z\\
-w&-y&0&2&0\\
0&-v&-z&0&2
\end{pmatrix}.
\]
The source identifies the rank-four accidental singular locus \(S\) above (its section 2.2.2). Put \(U=(\mathbb C\setminus\{2,-2\})^2\), parametrized by \((s,t)\), so \(S\cong U\). All analytic statements concern the open subset \(S\) itself; points at which \(s=\pm2\) or \(t=\pm2\) are excluded.

## Proof

**1. A relative polynomial equation.** Introduce global coordinates transverse to \(S\) by
\[
(x,y,z,w,v)=(a,s+d,t,s,b).
\]
The change from \((x,y,z,w,v)\) to \((a,b,d,s,t)\) is invertible and polynomial. An exact determinant expansion gives
\[
\frac{F}{2}
=(s^2-4)(a^2+b^2-tab)+(t^2-4)d^2
+a^2b^2+a^2d^2+2sa^2d-stabd.
\tag{1}
\]
In particular, \(F\) and all of its first derivatives vanish when \(a=b=d=0\). The coordinates \((s,t)\) therefore parametrize a critical submanifold. Its normal Hessian matrix, with normal coordinates ordered \((a,b,d)\), is
\[
H(s,t)=
\begin{pmatrix}
4(s^2-4)&-2t(s^2-4)&0\\
-2t(s^2-4)&4(s^2-4)&0\\
0&0&4(t^2-4)
\end{pmatrix}.
\tag{2}
\]
Consequently
\[
\det H(s,t)=-16(s^2-4)^2(t^2-4)^2\ne0
\quad\text{for all }(s,t)\in U.
\tag{3}
\]
The tangential Hessian blocks vanish since \(F\) and its normal first derivatives vanish identically along the stratum. Thus the full Hessian has rank exactly three and kernel the tangent space of \(S\). The holomorphic implicit-function theorem applied to the normal gradient shows that there are no additional critical points in a sufficiently small analytic neighborhood of any point of \(S\). By the holomorphic Morse lemma with parameters, the marked germ is locally analytically isomorphic to
\[
\bigl(\mathbb C^2,0\bigr)\times
\bigl(\{A^2+B^2+D^2=0\},0\bigr).
\]
This identifies the transverse singularity as \(A_1\), *not* an isolated singularity of the entire four-dimensional hypersurface.

**2. Integral vanishing cycles.** For a nondegenerate complex quadratic form in three variables, the transverse Milnor fiber has the homotopy type of the real sphere \(S^2\). Its sole nonzero reduced integral cohomology is therefore \(\widetilde H^2\cong\mathbb Z\). The local normal forms give a rank-one integral local system on \(U\). The only possible monodromy is multiplication by \(\pm1\).

To determine the sign globally, track changes of quadratic normal coordinates. At overlaps, their linear terms lie in the complex orthogonal group \(O(3,\mathbb C)\); its determinant \(\pm1\) is the induced degree on the oriented real vanishing \(S^2\). Thus the sign local system is precisely the orientation double cover of the nondegenerate normal quadratic bundle. In the fixed global normal framing \((a,b,d)\), that cover is obtained by adjoining a square root of \(\det H\). Equation (3) exhibits the *global nowhere-zero algebraic square root*
\[
\sqrt{\det H}=4i(s^2-4)(t^2-4),
\]
where \(i^2=-1\). Hence the orientation double cover splits on all of \(U\), and **every** loop acts trivially on the integral vanishing class. The existence of a square root on one local chart alone would not establish this conclusion; its global single-valuedness on the twice-punctured parameter factors is essential.

**3. Rational smoothness.** The link of an \(A_1\) complex surface point is \(\mathbb RP^3\), a rational homology three-sphere. Thus an \(A_1\) surface is a rational homology manifold at its node. Products with smooth complex manifolds preserve that local property, proving rational smoothness of \(Q\) along \(S\). No corresponding assertion is made for the other strata.

## Verification

The accompanying `artifacts/check_five_puncture_morse.py` is a standalone exact symbolic calculation using SymPy. It reconstructs \(M\), recomputes its determinant and identity (1), checks the zero first derivatives, computes the full normal Hessian and verifies equation (3). It also checks a rank-four witness and a nonsingular Hessian witness over \(\mathbb Q\). The topological identification and orientation-cover argument are mathematical steps, not outputs of a finite symbolic test.

## Relationship to prior work

Hikami's October 8, 2026 preprint, in equation (2.14) and section 2.2.2, supplies the symmetric determinantal model and *locates* the accidental rank-four stratum. It does not calculate its normal Hessian, analytic \(A_1\) type, or the global integral vanishing-cycle monodromy in the inspected sections. Standard holomorphic Morse theory supplies the general local normal-form and vanishing-cycle principles; those principles are not novel claims here.

Simpson's earlier five-puncture Betti-side work treats Hitchin-fibration compactifications and supplies relevant broad context. Only its published abstract and contents were accessible for comparison, so no assertion about its uninspected details is made. General symmetric determinantal hypersurface theory also provides broader structural context, but does not by itself evaluate the square class in (3) for this special boundary-trace locus.

## Limitations

The result concerns the affine **determinantal quintic**, rather than asserting an identical singularity classification for the full twenty-coordinate character variety. It covers only the stated rank-four surface \(S\), not rank-three or rank-two loci, and does not calculate global cohomology or a compactification's vanishing cycles. Trivial monodromy *along the stratum* must not be misread as trivial Picard–Lefschetz monodromy around the smoothing parameter. The complete Simpson chapter was not available, leaving a specific bibliographic overlap risk. No external independent mathematical verification of the new result is claimed.

## References

- K. Hikami, *Character Variety of the Five-Punctured Sphere and the Determinantal Quintic Hypersurface*, arXiv:2610.12092v1, posted 8 October 2026, especially equation (2.14) and section 2.2.2. https://arxiv.org/html/2610.12092v1
- C. T. Simpson, *An Explicit View of the Hitchin Fibration on the Betti Side for \(\mathbb P^1\) minus Five Points*, in *Geometry and Physics*, vol. II (2018), pp. 705–724. https://doi.org/10.1093/oso/9780198802020.003.0029
- J. Milnor, *Singular Points of Complex Hypersurfaces*, Princeton University Press, 1968 (classical Milnor-fiber foundations).
