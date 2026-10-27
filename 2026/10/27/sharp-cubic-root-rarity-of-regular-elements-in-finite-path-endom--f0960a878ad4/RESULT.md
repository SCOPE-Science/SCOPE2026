# Sharp cubic-root rarity of regular elements in finite path-endomorphism monoids

## Finding

Let \(P_n\) be the loopless undirected path with vertices \(1,\ldots,n\), where \(n\ge2\). Denote its endomorphism monoid by \(E_n=\operatorname{End}(P_n)\), and let \(R_n\) count its *regular* elements: those maps \(f\) for which some \(g\in E_n\) satisfies \(fgf=f\). Then
\[
\lim_{n\to\infty}\frac{1}{n^{1/3}}\log\frac{R_n}{|E_n|}=-\frac32\pi^{2/3}(\log2)^{2/3}.
\]
Thus the proportion of regular endomorphisms decays with a sharp stretched-exponential exponent and constant. The known finite-path regularity criterion is used as an ingredient, not claimed as a new result.

## Assumptions and scope

Paths are finite, simple, undirected and loopless; an endomorphism sends adjacent vertices to adjacent vertices, so \(|f(i+1)-f(i)|=1\). All logarithms are natural. Compositions use the usual convention \((fg)(x)=f(g(x))\). The result is an asymptotic statement for the entire family \(n\to\infty\), not an exact closed formula for \(R_n\) at fixed \(n\).

## Proof

**Step 1: criterion for regularity.** The image of any path endomorphism is a vertex interval \([a,a+h]\), with \(h\ge1\). We recall and justify the established criterion: \(f\) is regular precisely when its nearest-neighbor sequence \(f(1),\ldots,f(n)\) contains a contiguous strictly monotone run whose values traverse the whole interval \([a,a+h]\), either increasing or decreasing.

Indeed, if \(fgf=f\), the restriction of \(g\) to the image of \(f\) is a graph homomorphism selecting distinct preimages of every image vertex. Consequently \(g(a),\ldots,g(a+h)\) is an injective nearest-neighbor walk in a path, necessarily monotone. The composition identity says that \(f\) maps this run bijectively and monotonically onto its image. Conversely, if such a run occurs, its inverse is an endomorphism from the image interval into the original path. Extend it to the vertices on either side of the image interval by alternating between the two vertices nearest the appropriate end of that run. The extension gives \(g\in E_n\) with \(fgf=f\). This equivalence is already present in the finite-path endomorphism literature [1].

**Step 2: killed-walk spectral bounds.** Set \(m=n-1\). For \(1\le h\le m\), let \(A_h\) be the adjacency matrix of the \((h+1)\)-vertex path, and put
\[
\lambda_h=2\cos\frac{\pi}{h+2},\qquad
\varphi_h(j)=\sin\frac{(j+1)\pi}{h+2}\quad (0\le j\le h).
\]
Then \(A_h\varphi_h=\lambda_h\varphi_h\), \(0<\varphi_h(j)\le1\), and the spectral norm of \(A_h\) equals \(\lambda_h\). Writing \(W_{h,k}=\mathbf1^T A_h^k\mathbf1\), one has \(W_{h,k}\le(h+1)\lambda_h^k\). For a walk whose first \(h\) steps follow the monotone increasing run from \(a\) to \(a+h\), the number of choices for its remaining \(m-h\) steps confined to that interval equals \((A_h^{m-h}\mathbf1)_h\). Positivity and \(\mathbf1\ge\varphi_h\) give the lower bound \(\sin(\pi/(h+2))\lambda_h^{m-h}\).

For the upper bound, mark one full monotone run, choose its value interval (\(n-h\) choices), its orientation (two choices) and its location among \(m\) steps (\(m-h+1\) choices). Both the prefix and suffix must stay within the same image interval. Their numbers of completions are bounded by \(\sqrt{h+1}\lambda_h^{\text{length}}\) each, by Cauchy--Schwarz and the spectral norm. Overcounting by marks is harmless. Hence, simultaneously for every \(1\le h\le m\),
\[
(n-h)\sin\frac{\pi}{h+2}\,\lambda_h^{m-h}\le R_n
\le 2\sum_{j=1}^m (n-j)(m-j+1)(j+1)\lambda_j^{m-j}.
\tag{1}
\]
The lower expression uses just walks beginning with their complete increasing monotone run, and the upper expression includes every regular endomorphism.

**Step 3: normalizing by all endomorphisms.** Every starting point and sequence of \(m\) signed steps gives at most one homomorphism; ignoring boundary collisions shows \(|E_n|\le n2^m\). For a starting vertex in the central half of the path, a symmetric \(m\)-step random walk stays within distance \(\lfloor n/4\rfloor-1\) of its initial position with probability \(1-O(1/n)\), by Kolmogorov's maximal inequality. There are \(\Omega(n)\) such starting points. Thus
\[
\log |E_n|=m\log2+O(\log n).
\tag{2}
\]
In particular, this elementary estimate suffices for a sharp logarithmic large-deviation rate.

**Step 4: optimize the competing costs.** From (1), (2) and \(\lambda_j/2=\cos(\pi/(j+2))\), polynomial factors and \(\sin(\pi/(j+2))\) affect logarithms by at most \(O(\log n)\), uniformly when selecting any relevant \(j\). The logarithm of the regular-element proportion is therefore
\[
\log\frac{R_n}{|E_n|}=-\min_{1\le j\le m} F_m(j)+O(\log n),\qquad
F_m(j)=j\log2-(m-j)\log\cos\frac{\pi}{j+2}.
\tag{3}
\]
This relation can also be proved directly by bounding the sum above by its largest term times a polynomial in \(n\), then selecting its maximizing \(j\) in the lower bound. To avoid any near-boundary issue, note that \(\sin(\pi/(j+2))\ge2/(j+2)\) and \(n-j\ge1\), so the logarithmic prefactors are indeed polynomially bounded.

For \(j\sim u m^{1/3}\), with \(u>0\), the expansion \(-\log\cos t=t^2/2+O(t^4)\) gives
\[
\frac{F_m(j)}{m^{1/3}}\longrightarrow u\log2+\frac{\pi^2}{2u^2}.
\]
Indices with \(j/m^{1/3}\to0\) or \(\infty\) cannot minimize asymptotically: the second term or first term of \(F_m\), respectively, dominates \(m^{1/3}\). It follows by uniform convergence on compact positive \(u\)-intervals that
\[
\lim_{m\to\infty}m^{-1/3}\min_j F_m(j)
=\min_{u>0}\left(u\log2+\frac{\pi^2}{2u^2}\right)
=\frac32\pi^{2/3}(\log2)^{2/3},
\]
where the minimizer is \(u=(\pi^2/\log2)^{1/3}\). Dividing (3) by \(n^{1/3}\), noting \(m/n\to1\), proves the claim.

## Verification

The attached standalone script `verify.py` enumerates every endomorphism through order \(12\), tests the monotone-run criterion against the semigroup regularity definition by direct composition through order \(7\), checks both finite bounds, and checks the discrete variational constant at increasing scales. It prints `ALL_REGULAR_PATH_CHECKS_PASSED` upon successful completion. Finite enumeration corroborates but does not prove the limiting theorem; the proof above supplies the uniform estimates.

## Relationship to prior work

Dimitrova, Fernandes, Koppitz and Quinteiro established the finite-path regularity criterion and related monoid structure [1]; Proposition 1.9 in its available manuscript is the decisive predecessor of Step 1. Fernandes and Paulista study directed rather than undirected path endomorphisms [2]. Earlier literature considers overall numbers of path endomorphisms [3]. The contribution claimed here is solely the sharp large-\(n\) logarithmic decay exponent and constant for *regular* undirected-path endomorphisms, established using the spectral confinement cost and marked monotone traversal. None of the materially inspected primary results states this asymptotic rate. This does not certify that it has never appeared elsewhere.

## Limitations

The result is only logarithmically sharp: it does not give a prefactor, an exact count, or a local limit law for the maximizing image range. An equivalent limiting formula in older probability or transformation-semigroup literature remains a possible priority risk. The cited directed-path comparison treats a different monoid. The checker handles only finite instances and numerical variational tests. Independent mathematical review has not been performed.

## References

[1] D. Dimitrova, V. H. Fernandes, J. Koppitz and T. M. Quinteiro, *Ranks of Monoids of Endomorphisms of a Finite Undirected Path*, first public arXiv version 2018-10-22, arXiv:1810.09307, https://arxiv.org/abs/1810.09307. Available manuscript Proposition 1.9.

[2] V. H. Fernandes and P. Paulista, *On the Rank of Monoids of Endomorphisms of a Finite Directed Path*, arXiv:2112.13427, https://arxiv.org/abs/2112.13427.

[3] J. Knauer and collaborators, work on enumeration of path and cycle endomorphisms and weak endomorphisms, published abstracts inspected; relevant publication families available through https://arxiv.org/abs/1810.09307 references.
