# Exact three-dimensional ellipsoid benchmark for Janson’s higher-order Godbersen coefficient

## Finding

For every full-dimensional ellipsoid \(E\subset\mathbb R^3\),
\[
W_{2,E}(1,1,1)
=V\!\left(-\Delta_2E[2],\iota_1E[2],\iota_2E[2]\right)
=\frac{\pi^2}{160}|E|^2.
\]
For the Euclidean unit ball \(B^3\), this is
\[
W_{2,B^3}(1,1,1)=\frac{\pi^4}{90}.
\]
Fryš and Kotrbatý prove the universal three-dimensional Janson inequality
\[
W_{2,K}(1,1,1)\le \frac{3}{10}|K|^2.
\]
Consequently the ellipsoid value is exactly the fraction
\[
\frac{\pi^2}{48}
\]
of that universal upper bound.

## Assumptions and scope

Here \(V\) is the six-dimensional mixed volume, \(\Delta_2x=(x,x)\), and \(\iota_1x=(x,0)\), \(\iota_2x=(0,x)\). The notation agrees with the higher-order Godbersen coefficient \(W_{2,K}(1,1,1)\) used by Fryš and Kotrbatý. Ellipsoids are allowed arbitrary translations: mixed volume is translation invariant in each entry, so the calculation reduces to centered ellipsoids.

The claim is an exact evaluation for the affine class of ellipsoids. It does not assert a new universal inequality, an equality characterization for Janson’s inequality, or optimality of ellipsoids within any larger class.

## Proof

Let \(B=B^3\). If \(\Theta\) is uniform on \(S^2\), then
\[
\mathbb E|\langle u,\Theta\rangle|=\frac{\|u\|}{2}.
\]
Therefore the standard Vitale zonoid representation of the Euclidean ball is obtained from the random vector \(X=4\Theta\):
\[
h_B(u)=\mathbb E\,h_{\frac12[-X,X]}(u).
\]
For independent copies \(X_1,\ldots,X_6\), the mixed-volume/random-determinant formula for zonoids gives
\[
W_{2,B}(1,1,1)
=\frac1{6!}\,\mathbb E\left|
\det\begin{pmatrix}
X_1&X_2&X_3&X_4&0&0\\
X_1&X_2&0&0&X_5&X_6
\end{pmatrix}
\right|.
\]
The sign in \(-\Delta_2B\) is immaterial because \(B=-B\). For arbitrary vectors \(a_1,a_2,b_1,b_2,c_1,c_2\in\mathbb R^3\), direct multilinear expansion gives the exact identity
\[
\det\begin{pmatrix}
a_1&a_2&b_1&b_2&0&0\\
a_1&a_2&0&0&c_1&c_2
\end{pmatrix}
=(a_1\times a_2)\cdot\big((b_1\times b_2)\times(c_1\times c_2)\big).
\]
Now let \(U,V\) be independent and uniform on \(S^2\). Since \(\langle U,V\rangle\) is uniform on \([-1,1]\),
\[
\mathbb E\|U\times V\|
=\frac12\int_{-1}^{1}\sqrt{1-t^2}\,dt
=\frac{\pi}{4}.
\]
Rotational invariance also implies that the direction of \(U\times V\), conditional on its magnitude, is uniform on \(S^2\) and independent of that magnitude. Hence, for six independent uniform unit vectors \(U_1,\ldots,U_6\),
\[
\begin{aligned}
&\mathbb E\left|(U_1\times U_2)\cdot\big((U_3\times U_4)\times(U_5\times U_6)\big)\right|\\
&\qquad=\left(\frac{\pi}{4}\right)^3
\left(\frac{\pi}{4}\right)
\left(\frac12\right)
=\frac{\pi^4}{512}.
\end{aligned}
\]
The first three factors are the expected magnitudes of the three pairwise cross products, the fourth is the expected sine of the angle between two independent uniform directions, and the last factor is the expected absolute cosine against a third independent uniform direction.

Since \(X_i=4U_i\), multilinearity of the determinant now yields
\[
W_{2,B}(1,1,1)
=\frac{4^6}{6!}\frac{\pi^4}{512}
=\frac{\pi^4}{90}.
\]
Because \(|B|=4\pi/3\),
\[
\frac{W_{2,B}(1,1,1)}{|B|^2}
=\frac{\pi^2}{160}.
\]
Finally, let \(E=T B+x_0\) with \(T\in\mathrm{GL}(3)\). Translation invariance removes \(x_0\), while the block map \(T\oplus T\) on \(\mathbb R^6\) has determinant \((\det T)^2\). Therefore both \(W_{2,E}(1,1,1)\) and \(|E|^2\) are multiplied by \(|\det T|^2\), proving the same normalized identity for every ellipsoid.

## Verification

The included checker verifies the six-vector determinant identity on all \(3^6\) choices of standard-basis inputs. Because both sides are multilinear in the six vector arguments, agreement on all basis tuples verifies that identity identically. It also checks the exact rational factors
\[
\frac{4^6}{6!\,512}=\frac1{90},\qquad
\frac{1/90}{16/9}=\frac1{160},\qquad
\frac{1/160}{3/10}=\frac1{48}.
\]
The spherical expectations \(\pi/4\) and \(1/2\) are established analytically in the proof rather than by sampling.

## Relationship to prior work

Fryš and Kotrbatý define \(W_{p,K}\), prove Janson’s inequality, and note that in dimension three the multiindex \((1,1,1)\) is the only nontrivial higher-order case. Their proof gives
\[
W_{2,K}(1,1,1)\le\frac3{10}|K|^2,
\]
but does not analyze ellipsoids or provide this exact coefficient; the paper also states that the equality cases of Janson’s inequality remain unresolved. Kotrbatý’s earlier paper introduces the higher-order Godbersen framework and proves important special classes, again without an ellipsoid evaluation of this coefficient.

Breiding, Bürgisser, Lerario, and Mathis prove the general zonoid mixed-volume/random-determinant correspondence used here. That theorem supplies the representation step but not the structured determinant evaluation above: the value \(\pi^4/90\) comes from the additional block-determinant identity and the rotational factorization of four angular expectations.

## Limitations

This is a canonical exact benchmark, not an extremal theorem. It neither proves nor disproves the conjectured simplex equality characterization. The exact value uses rotational symmetry of the Euclidean ball and affine covariance to cover ellipsoids; it does not extend automatically to general centrally symmetric bodies or general zonoids. A residual literature risk is that the same special evaluation may appear in an unindexed computation of higher-order mixed volumes or random determinants.

## References

1. F. Fryš and J. Kotrbatý, *Around higher-order Godbersen conjectures*, arXiv:2609.08612, first public 2026-09-08.
2. J. Kotrbatý, *On a Generalization of Godbersen’s Conjecture*, International Mathematics Research Notices 2025, rnaf341, DOI: 10.1093/imrn/rnaf341.
3. P. Breiding, P. Bürgisser, A. Lerario, and L. Mathis, *The zonoid algebra, generalized mixed volumes, and random determinants*, Advances in Mathematics 402 (2022), 108361, DOI: 10.1016/j.aim.2022.108361.
