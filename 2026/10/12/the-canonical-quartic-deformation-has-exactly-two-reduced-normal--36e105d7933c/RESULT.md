# The canonical quartic deformation has exactly two reduced normal-bundle jumps
## Finding
Let \(K\) be an algebraically closed field of characteristic zero and let
\[
X=\operatorname{Bl}_{\Lambda}\mathbf P^3_K
\]
be the blow-up of projective three-space along a line. Iwasaki's Proposition 6.7 studies rational curves of class \((4,2)\) and introduces the deformation
\[
q_{\varepsilon}
=
\bigl(s^4-t^4,\ s^2t^2+\varepsilon s^4,\ t^2,\ s^2-st,\ st\bigr).
\]
The source uses this family only near \(\varepsilon=0\) to prove that the normal-bundle jumping divisor is nonempty and smooth there.

In fact the entire affine parameter line is an unramified family, and its splitting type is completely determined:
\[
N_{q_{\varepsilon}/X}\cong
\begin{cases}
\mathcal O_{\mathbf P^1}(5)\oplus\mathcal O_{\mathbf P^1}(7),&\varepsilon\in\{0,1/4\},\\
\mathcal O_{\mathbf P^1}(6)^{\oplus2},&\varepsilon\notin\{0,1/4\}.
\end{cases}
\]
Moreover, if \(J\) denotes the balanced-to-unbalanced jumping divisor from the source, then the scheme-theoretic pullback of \(J\) to this affine line is
\[
V\bigl(\varepsilon(1-4\varepsilon)\bigr).
\]
Thus the canonical deformation meets \(J\) in exactly two reduced points, not only at the point \(\varepsilon=0\) highlighted in the source.

## Assumptions and scope
The field is algebraically closed of characteristic zero. The result concerns only the explicit class-\((4,2)\) family above in \(\operatorname{Bl}_{\Lambda}\mathbf P^3\). It does not classify every component of the full jumping divisor or assert an analogous two-point statement in positive characteristic.

The source parameter space \(U\) consists of Cox tuples defining honest unramified maps. For the blow-up along a line, the displayed tuple has Cox coordinates \((u_0,u_1,v_2,v_3,w)\), and the induced map to \(\mathbf P^3\) is
\[
[u_0:u_1:w v_2:w v_3].
\]
The normal bundle has rank two and degree \(12\).

## Proof
First, every \(q_{\varepsilon}\) is an honest map. The pair \((v_2,v_3)=(t^2,s(s-t))\) has no common zero on \(\mathbf P^1\). Likewise, \((u_0,u_1,w)\) has no common zero: if \(w=st=0\), then one of \(s,t\) vanishes and \(u_0=s^4-t^4\) is nonzero.

It remains to prove unramifiedness globally in \(\varepsilon\). Specializing the source's Cox differential matrix gives
\[
\Psi_{\varepsilon}=
\begin{pmatrix}
0&4s^3&-4t^3\\
0&4\varepsilon s^3+2st^2&2s^2t\\
t^2&0&2t\\
s^2-st&2s-t&-s\\
-st&t&s
\end{pmatrix}.
\]
Three of its three-by-three minors are
\[
\Delta_{025}=-4t^2(3s^4+t^4),\qquad
\Delta_{034}=-4s(s-t)^2(s^3-st^2-2t^3),
\]
and
\[
\Delta_{234}=4st^2(2s-t).
\]
Here the labels merely record the selected rows. If \(s=0\), then \(\Delta_{025}\neq0\); if \(t=0\), then \(\Delta_{034}\neq0\). If \(st\neq0\) and all maximal minors vanished, \(\Delta_{234}=0\) would force \(t=2s\), but then
\[
\Delta_{025}=-304s^6\neq0
\]
in characteristic zero. Hence \(\Psi_{\varepsilon}\) has rank three at every source point, for every \(\varepsilon\). Therefore the whole affine family lies in \(U\).

For the relative cohomology map detecting the first splitting jump, the appendix of the source performs exact row and column reduction. A fourteen-row block has rank \(14\), with a nonzero minor equal to \(256\), and the induced map on its two-dimensional kernel is
\[
4\begin{pmatrix}
0&4\varepsilon-1\\
\varepsilon&-2
\end{pmatrix}.
\]
Consequently the full sixteen-by-sixteen determinant is
\[
4096\,\varepsilon(1-4\varepsilon).
\]
Away from \(\varepsilon=0,1/4\) the matrix is invertible, so the degree-\(12\) rank-two normal bundle is balanced, namely \(\mathcal O(6)^{\oplus2}\).

At each of the two roots the displayed two-by-two matrix has rank one. Because the complementary block has rank \(14\), the full relative cohomology matrix has rank \(15\), so its kernel is one-dimensional. If
\[
N\cong\mathcal O(a)\oplus\mathcal O(12-a),\qquad a\le6,
\]
then
\[
h^0\bigl(N(-7)\bigr)=6-a.
\]
Thus one-dimensional kernel forces \(a=5\), giving \(N\cong\mathcal O(5)\oplus\mathcal O(7)\) at both roots.

Finally \(\varepsilon(1-4\varepsilon)\) has two distinct simple roots in characteristic zero. Since the source's first jump locus is the determinantal divisor of this square relative cohomology map on \(U\), its pullback to the affine parameter line is precisely the reduced divisor supported at \(0\) and \(1/4\).

## Verification
The accompanying `verify.py` uses only the Python standard library. It reconstructs the three Cox-differential minors as multivariate polynomials, verifies the global rank argument, checks the exact two-by-two determinant and the factor \(4096\varepsilon(1-4\varepsilon)\), checks rank one at both roots, and verifies the rank-two degree-\(12\) splitting calculation. Its recorded output ends in `VERIFY_OK`.

The non-elementary inputs imported from arXiv:2609.39309v1 are the Cox resolution and rank criterion, the identification of the first jump locus with the relative-cohomology determinantal divisor, and the appendix reduction yielding the rank-\(14\) block and the displayed two-by-two quotient matrix.

## Relationship to prior work
Iwasaki constructs relative normal-bundle resolutions and determinantal jumping loci for rational curves in smooth projective toric varieties. In the class-\((4,2)\) blow-up example, Proposition 6.7 identifies \(q_0\), proves \(N_{q_0/X}\cong\mathcal O(5)\oplus\mathcal O(7)\), and introduces \(q_{\varepsilon}\) as a deformation lying in the unramified locus near \(0\). The appendix prints the factorized determinant \(4096\varepsilon(1-4\varepsilon)\), but the proposition does not globalize the deformation to every \(\varepsilon\) or identify the second root as another honest unramified quartic with the same splitting type.

Cela--Lian study interpolation and normal bundles for rational curves in blow-ups of projective space, providing broader existence and generic-splitting context. Their results do not determine the complete splitting profile of this source-specific affine deformation. Targeted searches for the exact tuple, the parameter \(1/4\), the factorized determinant, and equivalent two-jump formulations found no prior statement covering the result above.

## Limitations
The argument uses characteristic zero in the global rank proof and in separating the two determinant roots. The source treats arbitrary characteristic and gives a different determinant behavior in characteristic two; no positive-characteristic classification is claimed here. The result is a complete one-parameter slice, not a global irreducible-component analysis of the full jumping divisor. An unindexed note could contain the same observation because the determinant factor already appears in the source appendix, although the required global membership in \(U\) and the second splitting calculation are not stated there.

## References
1. Hikari Iwasaki, *Normal Bundle Splitting Strata of Rational Curves in Toric Varieties*, arXiv:2609.39309v1, 2026.
2. Alessio Cela and Carl Lian, *Interpolation for rational curves with secants*, arXiv:2607.01432, 2026.
