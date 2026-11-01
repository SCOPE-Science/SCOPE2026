# Sharp pointwise width stability for equiangular polygons with parallel opposite sides

## Finding
Let \(n\ge3\) be an integer, and let \(P\) be a nondegenerate convex equiangular Euclidean \(2n\)-gon. Its consecutive outward unit facet normals are \(u_j=(\cos(j\pi/n),\sin(j\pi/n))\), up to a common rotation. Write \(w_j=h_P(u_j)+h_P(-u_j)\) for its widths in those \(n\) unoriented normal directions, and \(\bar w=n^{-1}\sum_{j=0}^{n-1}w_j\). Define
\[
\Delta(P)=\frac12\max_{0\le j<n}|w_j-\bar w|.
\]
Let \(L(P)\) and \(A(P)\) be its Euclidean perimeter and area, and let \(W(P)\) be the signed oriented area of the Wigner caustic associated with opposite vertex pairs, with its standard half-cycle convention. Then
\[
\boxed{L(P)^2-8n\tan\left(\frac{\pi}{2n}\right)\bigl(A(P)+2|W(P)|\bigr)\ \ge\ 16n^2\tan^2\left(\frac{\pi}{2n}\right)\Delta(P)^2.}
\]
The coefficient \(16n^2\tan^2(\pi/(2n))\) is the largest possible for every \(n\ge3\), with nonregular nondegenerate convex equality examples. More precisely, put \(c=\cos(\pi/n)\) and, for \(j=0,\ldots,n-1\), define
\[
g_j=\frac{1}{n(1-c)}-\frac{\sin(j\pi/n)}{\sin(\pi/n)},
\]
extended \(n\)-periodically. If \(q_j=w_j/2\) and \(H=n^{-1}\sum_{j=0}^{n-1}q_j\), equality holds precisely when
\[
q_j=H+t\,g_{(j-k)\bmod n}
\]
for a real \(t\), some \(k\in\{0,\ldots,n-1\}\), and all \(j\), provided the stated polygon exists with strictly positive edge lengths. In particular, every \(n\) has such nonregular equality polygons: start with a regular \(2n\)-gon of inradius \(H>0\), use the displayed support numbers, and take sufficiently small nonzero \(t\). The constants satisfy
\[
16n^2\tan^2\left(\frac{\pi}{2n}\right)=4\pi^2+\frac{2\pi^4}{3n^2}+O(n^{-4}).
\]

## Assumptions and scope
All polygons here are full dimensional, convex, and have all \(2n\) facets present, with consecutive equal exterior angles \(\pi/n\). Translation of \(P\) does not change the widths or the theorem. The Wigner caustic is the closed polygonal chain obtained from the midpoints of corresponding opposite vertices, traversed once through \(n\) consecutive pairs; signed area is taken by the ordinary shoelace convention. Its absolute oriented area, rather than any unsigned region enclosed by a possibly self-intersecting chain, is used. The nonregular sharpness witnesses can be centrally symmetric. The claim controls widths only at the prescribed facet-normal directions; no assertion about continuous-direction maximal width or Hausdorff distance is made.

## Proof
Write \(N=2n\), \(\alpha=\pi/n\), \(c=\cos\alpha\), and \(Q=(P+(-P))/2\) for the central symmetral. Its support numbers at \(u_j\) are \(q_j=(h_P(u_j)+h_P(u_{j+n}))/2\), with \(q_{j+n}=q_j\). The opposite sides of \(P\) are parallel, so the vertex pairs of \(Q\) and of the Wigner midpoint chain are respectively half-differences and half-sums of opposite vertices of \(P\). Expanding their shoelace expressions (cross terms cancel under the antipodal index shift) yields
\[
W(P)=\frac{A(P)-A(Q)}2.
\]
Brunn--Minkowski gives \(A(Q)\ge A(P)\), so \(A(P)+2|W(P)|=A(Q)\). The same parallelism shows \(L(Q)=L(P)\).

For an equiangular polygon with consecutive support values \(s_j\), elementary intersection of neighboring supporting lines gives edge length
\[
\ell_j=\frac{s_{j-1}+s_{j+1}-2c s_j}{\sin\alpha}.
\]
Consequently \(L(Q)=2\tan(\alpha/2)\sum_{j=0}^{N-1}q_j=4n\tan(\alpha/2)H\), where \(H=n^{-1}\sum_{j=0}^{n-1}q_j\). The area formula \(A(Q)=\tfrac12\sum_j q_j\ell_j\) becomes
\[
A(Q)=\frac1{\sin\alpha}\sum_{j=0}^{N-1}\bigl(q_jq_{j+1}-c q_j^2\bigr).
\]
Set \(v_j=q_j-H\), read modulo \(n\), and observe \(\sum_{j=0}^{n-1}v_j=0\). Direct cancellation of the constant and linear terms yields the **exact deficit identity**
\[
\mathcal D(P):=L(P)^2-8n\tan(\alpha/2)\bigl(A(P)+2|W(P)|\bigr)
=\frac{16n}{1+c}\,E(v),
\]
where
\[
E(v)=\sum_{j=0}^{n-1}\left(c v_j^2-v_jv_{j+1}\right).
\]
On real mean-zero \(n\)-periodic vectors, the self-adjoint circulant operator
\[
(Tv)_j=cv_j-\frac{v_{j-1}+v_{j+1}}2
\]
is positive definite, since its nonconstant Fourier eigenvalues are \(c-\cos(2\pi k/n)>0\), \(1\le k<n\). Thus \(E(v)=\langle v,Tv\rangle\).

The displayed vector \(g\) has zero mean because \(\sum_{j=0}^{n-1}\sin(j\alpha)=\cot(\alpha/2)\), and \(\sin\alpha=(1-c)\cot(\alpha/2)\). The sine addition identity gives
\[
Tg=e_0-\frac1n\mathbf1.
\]
Indeed this follows by the sine recurrence at every index except zero, and at zero from \(g_1=g_{n-1}=g_0-1\). Its energy is therefore
\[
\langle g,Tg\rangle=g_0=\frac1{n(1-c)}.
\]
For an arbitrary index \(k\), translate \(g\) cyclically to \(g^{(k)}\). Cauchy--Schwarz in the positive-definite energy inner product gives
\[
|v_k|^2=|\langle v,Tg^{(k)}\rangle|^2
\le E(v)\,E(g^{(k)})=\frac{E(v)}{n(1-c)}.
\]
Maximizing over \(k\) and substituting into the deficit identity proves
\[
\mathcal D(P)\ge\frac{16n}{1+c}\,n(1-c)\max_k|v_k|^2
=16n^2\tan^2(\alpha/2)\Delta(P)^2.
\]
If \(\Delta(P)>0\), equality in energy Cauchy--Schwarz forces \(v=tg^{(k)}\) for an index attaining the maximum. Conversely such vectors achieve equality, since the evaluation inequality is an equality at \(k\), and hence at the maximal coordinate. For every \(H>0\), \(q_j=H+tg^{(k)}_j\) defines an equiangular centrally symmetric polygon with positive edge lengths whenever \(|t|\) is sufficiently small, as follows from the strict positivity of the regular polygon's edge lengths and continuity of the displayed edge formula. Such polygons have \(P=Q\), \(W=0\), and attain the coefficient sharply; they are nonregular for \(t\ne0\). The limit expansion follows from \(\tan z=z+z^3/3+O(z^5)\).

## Verification
The standalone Python program `verify.py` uses only the standard library. It independently constructs equiangular polygons by intersecting support lines, checks the exact area/perimeter and Wigner relations on noncentrally symmetric polygon samples, verifies the Green-vector recurrence on dimensions \(3\) through \(100\), and checks equality witnesses and the sharp coefficient numerically. These finite tests support the explicit algebraic identities but do not replace the all-dimensional proof. Run with `python verify.py` after extracting the files.

## Relationship to prior work
Konicer, Murawski, Rogala, Wieczorek, and Zwierzyński (2026), Theorem 4.4, prove the underlying discrete Wigner-corrected isoperimetric inequality and characterize its zero-deficit equality family. The new statement fixes a precise nonzero width-discrepancy observable, determines the **optimal finite-side-count pointwise coefficient**, and classifies all sharp nonzero-deficit witnesses by a cyclic Green kernel. Zwierzyński (2015/2016), Theorem 4.4, provides a related smooth-body Hausdorff-stability inequality with coefficient \(4\pi^2\); the finite polygonal constants above tend to that smooth coefficient but are not a specialization of the smooth theorem. Indrei and Nurbekyan (2014) provide polygonal isoperimetric stability through vertex-radius and edge-length variances; those estimates neither determine the present Wigner-corrected width functional nor its sharp constant. Related symmetrization-based mixed-volume identities are established by Zwierzyński (2026), but they do not themselves establish this finite discrete pointwise extremal problem.

## Limitations
This is a restricted equiangular-polygon result: it does not establish the optimal bound for polygons with unequal exterior angles, continuous-direction widths, or a Hausdorff distance to a regular polygon. The full-text accessibility of a closely related August 2026 symmetrization paper was limited; an equivalent historical result in older polygonal discrete Wirtinger literature cannot be excluded solely by database searching. These limitations do not affect the proved inequality or its best coefficient within the stated class. Independent review is not claimed.

## References
- I. Konicer, B. Murawski, B. Rogala, T. Wieczorek, and M. Zwierzyński, *Convex Polygons with Parallel Opposite Sides: Convergence, Reconstruction, and Isoperimetric Inequalities*, arXiv:2606.22612v1 (first public 2026-06-21), especially Section 4, Theorem 4.4 and the Wigner/symmetral area identity.
- M. Zwierzyński, *The improved isoperimetric inequality and the Wigner caustic of planar ovals*, arXiv:1512.06684, Theorem 4.4 (first posted 2015-12-21).
- E. Indrei and L. Nurbekyan, *On the stability of the polygonal isoperimetric inequality*, arXiv:1402.4460 (2014), Introduction and principal variance stability statement.
- M. Zwierzyński, *Mixed Volumes, the Wigner Caustic, and Isoperimetric Inequalities*, arXiv:2608.11068 (2026), abstract and available metadata; related full text not conclusively inspected.
