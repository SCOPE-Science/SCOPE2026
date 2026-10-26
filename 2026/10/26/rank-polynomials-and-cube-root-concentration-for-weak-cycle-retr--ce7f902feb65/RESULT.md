# Rank polynomials and cube-root concentration for weak cycle retractions

## Finding

Let \(C_n\) be the simple undirected cycle with vertex set \(\mathbb Z/n\mathbb Z\), for each integer \(n\ge3\). Let \(\mathrm{wEnd}(C_n)\) consist of maps that send each edge either to an edge or to a single vertex. Define the image-rank polynomial of its idempotents by
\[
 E_n(z)=\sum_{\substack{f\in\mathrm{wEnd}(C_n)\\ f^2=f}}z^{|\operatorname{im}f|}.
\]
For each integer \(\ell\ge1\), let \(B_\ell\) be the \((\ell+1)\times(\ell+1)\) matrix indexed by \(0,\ldots,\ell\), with entry one when the indices differ by at most one, and entry zero otherwise. Then **every coefficient** of the rank polynomial is given by
\[
\boxed{E_n(z)=z^n+nz+n\sum_{\ell=1}^{\lfloor n/2\rfloor}(B_\ell^{\,n-\ell})_{\ell,0}\,z^{\ell+1}.}
\]
In particular, there are exactly \(n2^{n-2}\) idempotents of rank two, and the number of idempotents of largest proper rank \(\lfloor n/2\rfloor+1\) is \(n\) for even \(n\), or \(n(n+1)/2\) for odd \(n\).

Write \(I_n=E_n(1)\), and select an idempotent uniformly from the \(I_n\) possibilities. Let \(R_n\) denote its image cardinality. Define the positive constants
\[
 a=\left(\frac{2\pi^2}{3\log3}\right)^{1/3},\qquad
 b=\frac32a\log3.
\]
Then
\[
\boxed{\log I_n=n\log3-bn^{1/3}+o(n^{1/3})},
\qquad
\boxed{\frac{R_n}{n^{1/3}}\ \xrightarrow{\ \mathrm P\ }\ a.}
\]
Here the logarithm is natural. The concentration is exponential at the \(n^{1/3}\) scale outside any fixed neighborhood of \(a\). The constants satisfy approximately \(a=1.8160\) and \(b=2.9927\).

## Assumptions and scope

All cycles are simple, undirected and loopless, and all maps are **full** transformations on their vertices. Weak homomorphism means that an edge may be contracted but cannot map to a nonedge with distinct endpoints. Thus this semigroup differs from the ordinary edge-preserving endomorphism monoid and from any partial-isometry monoid. Rank is the number of image vertices. The exact polynomial holds for every integer \(n\ge3\); the limiting claims concern \(n\to\infty\). No field or parity restriction is imposed.

## Proof

**Step 1: images of retractions are intervals.** For any idempotent transformation \(f\), its image equals its set of fixed points, since \(f(f(x))=f(x)\). As the cycle is connected, and adjacent vertices have equal or adjacent images under any weak endomorphism, the image is a connected vertex subset of the cycle. Unless it is the entire vertex set, that subset is a nonempty cyclic arc, uniquely determined by its first vertex and number of edges. If its size is one, the map is constant, yielding \(nz\). If its size is \(n\), the map is a surjective idempotent and therefore the identity, yielding \(z^n\).

**Step 2: exact walk bijection.** For a proper non-singleton image, rotate the vertex names so the fixed arc is \(0,1,\ldots,\ell\), for some \(1\le\ell\le n-2\). The values of the map are forced to be \(f(j)=j\) for \(0\le j\le\ell\). The complementary part of the source cycle is a path of \(n-\ell\) edges from vertex \(\ell\) back to vertex \(0\). Its images must be a walk from \(\ell\) to \(0\), staying within the image arc and taking steps in \(\{-1,0,1\}\). Conversely, every such walk defines a weak endomorphism with the given image fixed pointwise, hence an idempotent. The number of such walks is exactly \((B_\ell^{n-\ell})_{\ell,0}\). Reaching \(0\) from \(\ell\) requires at least \(\ell\) steps, so \(\ell\le\lfloor n/2\rfloor\). Each permitted proper arc has exactly \(n\) rotations, and distinct arcs yield different images. This proves the polynomial. When \(\ell=1\), every entry of \(B_1^{n-1}\) equals \(2^{n-2}\). At the largest allowed \(\ell\), the remaining walk must take only downward steps if \(n=2\ell\), or exactly one zero step if \(n=2\ell+1\). This gives the stated boundary coefficients.

**Step 3: spectral confinement estimate.** The real symmetric matrix \(B_\ell\) has eigenvalues
\[
\lambda_{\ell,j}=1+2\cos\left(\frac{j\pi}{\ell+2}\right),\quad j=1,\ldots,\ell+1,
\]
with orthonormal eigenvectors \(v_j(x)=\sqrt{2/(\ell+2)}\sin((x+1)j\pi/(\ell+2))\). The largest eigenvalue \(\lambda_{\ell,1}\) is positive. Its endpoint contribution is exactly
\[
 c_\ell\lambda_{\ell,1}^{\,n-\ell},\qquad
 c_\ell=\frac{2}{\ell+2}\sin^2\left(\frac{\pi}{\ell+2}\right)=\Theta(\ell^{-3}).
\]
For \(\ell\to\infty\) with \(\ell=O(n^{1/3})\) and \(\ell\ge\delta n^{1/3}\) for any fixed \(\delta>0\), the remaining eigenvalues have absolute value at most \(\lambda_{\ell,1}\exp(-c/\ell^2)\) for some fixed positive \(c\). The total absolute remainder is at most the corresponding spectral norm, so its ratio to the displayed positive leading contribution is at most \(O(\ell^3\exp(-c(n-\ell)/\ell^2))=o(1)\). Uniformly on each compact interval of \(t=\ell/n^{1/3}\in(0,\infty)\), this yields
\[
\log(B_\ell^{\,n-\ell})_{\ell,0}
=n\log3-\left(t\log3+\frac{\pi^2}{3t^2}\right)n^{1/3}+o(n^{1/3}).
\]
The expansion follows by writing \(\log\lambda_{\ell,1}=\log3-\pi^2/[3(\ell+2)^2]+O(\ell^{-4})\).

**Step 4: unique optimum and global tails.** Set \(\Phi(t)=t\log3+\\(\pi^2/(3t^2)\)\) for \(t>0\). It is strictly convex and has unique minimizer \(a=(2\pi^2/(3\log3))^{1/3}\) with \(\Phi(a)=\frac32a\log3=b\). For every admissible \(\ell\), positivity and the spectral norm give \((B_\ell^{n-\ell})_{\ell,0}\le\lambda_{\ell,1}^{n-\ell}\). A uniform bound \(\lambda_{\ell,1}\le 3\exp[-c_0/(\ell+2)^2]\), with \(c_0>0\), implies that \(\ell\le\delta n^{1/3}\) has a deficit at least \(c_1\delta^{-2}n^{1/3}\) from \(n\log3\). Similarly, \(\ell\ge M n^{1/3}\) has a deficit at least \(M(\log3)n^{1/3}\) because \(\lambda_{\ell,1}\le3\). Choosing small \(\delta\) and large \(M\) makes these tails negligible against the unique optimum. On the remaining compact range the uniform estimate of Step 3, strict convexity and the at-most-polynomial number of terms give the Laplace principle
\[
\log\Big(n\sum_{\ell=1}^{\lfloor n/2\rfloor}(B_\ell^{n-\ell})_{\ell,0}\Big)
=n\log3-bn^{1/3}+o(n^{1/3}).
\]
The constant maps and identity are negligible. For any \(\varepsilon>0\), strict separation of \(\Phi\) from its minimum outside \(|t-a|<\varepsilon\) gives \(\Pr(|R_n/n^{1/3}-a|\ge\varepsilon)\le\exp[-c_\varepsilon n^{1/3}+o(n^{1/3})]\), completing the proof.

## Verification

An independent composition-based enumeration of weak cycle endomorphisms for \(3\le n\le9\), retaining only maps satisfying \(f^2=f\), matches the coefficient formula for every rank. The exhaustive counts, written in ascending rank order, are: \(n=3: (3,6,1)\); \(n=4: (4,16,4,1)\); \(n=5: (5,40,15,0,1)\); \(n=6: (6,96,48,6,0,1)\); \(n=7: (7,224,140,28,0,0,1)\); \(n=8: (8,512,392,104,8,0,0,1)\); and \(n=9: (9,1152,1071,342,45,0,0,0,1)\). The standalone verifier recomputes these values and checks the rank-two and maximum-proper-rank specializations through larger sizes. Finite computations do not establish asymptotic limits, which follow from Steps 3 and 4.

## Relationship to prior work

Dimitrova, Fernandes, Koppitz and Quinteiro introduced and structurally studied precisely the full weak endomorphism monoid \(\mathrm{wEnd}(C_n)\), including the image-arc and rank framework, cardinality, Green's relations, regularity and generator ranks. Their results are the starting assumptions, **not** claimed here as new. Their inspected paper does not give the coefficientwise idempotent rank polynomial or the cube-root limiting law above. Pomsri and coauthors enumerate weak graph homomorphisms involving paths, which informs the walk method but does not by itself assert a retraction census or a rank-concentration theorem for cycles. Strict edge-preserving cycle endomorphism retractions differ because zero steps are forbidden, and cannot supply the present weak-semigroup counts.

## Limitations

The result concerns full weak endomorphisms of simple cycles only; it does not classify conjugacy classes of their idempotents, count non-idempotents, or make the same claims for strict endomorphisms or partial maps. The asymptotic gives the first subleading exponential scale and a law of large numbers, not a local limit or multiplicative constant. Novelty conclusions are confined to the inspected literature and prior accessible research; an uncatalogued general retraction-enumeration or confined-walk theorem could subsume aspects of this result. There has been no independent mathematical audit.

## References

1. I. Dimitrova, V. H. Fernandes, J. Koppitz, T. M. Quinteiro, *On monoids of endomorphisms of a cycle graph*, arXiv:2310.04149v1 (first submitted 2023-10-06), https://arxiv.org/abs/2310.04149.
2. *Finding the Number of Weak Homomorphisms of Paths*, *Journal of Mathematics* (2022), DOI:10.1155/2022/2153927, https://doi.org/10.1155/2022/2153927.
