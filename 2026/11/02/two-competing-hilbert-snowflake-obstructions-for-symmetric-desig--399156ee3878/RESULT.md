# Two competing Hilbert-snowflake obstructions for symmetric-design incidence graphs

## Finding
Let \(\mathcal D\) be a symmetric \(2\)-\((v,k,\lambda)\) block design with \(2\le k<v\), \(1\le\lambda<k\), and \(r=k-\lambda\ge2\). Its incidence graph \(G\) has \(v\) point vertices and \(v\) block vertices, with every graph edge of length one. The result depends only on \((v,k,\lambda)\), not on the design's isomorphism class.

Let \(s=\sqrt r\) and let \(p_s\in(0,1)\) be the unique solution of
\[
s(3^{p_s}-1)=2^{p_s}.
\]
Set \(u_s=2^{p_s}\) and \(R=(k+s)/(k-1)\). Define the supremal negative-type exponent \(\wp(G)\) as the supremum of all \(p\ge0\) for which \(\sum_{x,y}z_xz_yd_G(x,y)^p\le0\) for all real \(z\) with \(\sum_x z_x=0\); at \(p=0\), put zero on the diagonal and one off the diagonal.

**Exact phase law:** If \(u_s<R\), then \(\wp(G)=p_s\). If \(u_s=R\), then \(\wp(G)=p_s\) with a simultaneous degeneracy. If \(u_s>R\), then \(\wp(G)=p_g<p_s\), where \(p_g\) is the unique solution in \((0,p_s)\) of
\[
(v-1)2^{p_g}-(v-k)3^{p_g}-k=0.
\]
In each case the powered metric has *strict* negative type for \(0\le p<\wp(G)\), nonstrict negative type at \(p=\wp(G)\), and no negative type at any larger \(p\).

At its critical exponent, the zero-sum equality space has dimension \(v-1\), \(v\), or \(1\) in the three cases \(u_s<R\), \(u_s=R\), or \(u_s>R\), respectively. Equivalently, the minimum affine dimension of an isometric Euclidean realization of the snowflake \(d_G^{\wp(G)/2}\) is \(v\), \(v-1\), or \(2v-2\). For \(0\le p<\wp(G)\), the minimum affine dimension is \(2v-1\).

**Projective-plane/complementary-plane transition:** For every existing finite projective plane of order \(q\ge2\), its point-line incidence graph always lies in the \(v-1\)-dimensional-equality-space (spectral) phase. The graph joining a point to every *nonincident* line has the same critical exponent and the same equality-space dimension when \(q=2\), but lies in the one-dimensional-equality-space (global) phase for every \(q\ge3\). Here \(v=q^2+q+1\). As \(q\to\infty\) along existing plane orders, the two exponents have sharply different scales:
\[
\wp(G_{\mathrm{inc}})=\frac{1}{\log 3}\,q^{-1/2}+O(q^{-1}),\qquad
\wp(G_{\mathrm{noninc}})=\frac{1}{\log 2}\,q^{-2}+O(q^{-3}).
\]
These statements include arbitrary non-Desarguesian planes whenever they exist.

## Assumptions and scope
A symmetric \(2\)-\((v,k,\lambda)\) design consists of \(v\) points and \(v\) blocks, each block containing \(k\) points, each point in \(k\) blocks, and each pair of distinct points in exactly \(\lambda\) blocks. The assumptions imply \(v\ge3\), \(k>r\), and the parameter identity \(k(k-1)=\lambda(v-1)\), equivalently \(r(v-1)=k(v-k)\). A point and a nonincident block are separated by three edges, two distinct points (or blocks) by two edges, and incident point-block pairs by one edge. The graph is connected with diameter three. The nontrivial restriction \(r\ge2\) excludes the previously characterized crown-graph case \(r=1\).

Negative type concerns the real zero-sum quadratic form of \(d^p\); a Hilbert embedding of the snowflake \(d^{p/2}\) means squared Euclidean distances equal \(d^p\). No existence assertion for unavailable block-design parameters or projective-plane orders is made.

## Proof
Let \(N\) be the \(v\times v\) point-block incidence matrix. Counting shared blocks gives
\[
N\mathbf 1=k\mathbf1,\qquad N^{\mathsf T}\mathbf1=k\mathbf1,\qquad
NN^{\mathsf T}=rI+\lambda J.
\]
Thus the nonconstant singular values of \(N\) are all exactly \(s=\sqrt r\). For \(a=2^p\) and \(b=3^p\), the full powered-distance matrix is
\[
D_p=\begin{pmatrix}a(J-I)&bJ-(b-1)N\\ bJ-(b-1)N^{\mathsf T}&a(J-I)\end{pmatrix}.
\]
The real zero-sum subspace decomposes orthogonally into the one-dimensional span of \((\mathbf1,-\mathbf1)\) and the \(2v-2\)-dimensional space \(\mathbf1^\perp\oplus\mathbf1^\perp\). On the first component \(D_p\) has eigenvalue
\[
g(p)=(v-1)2^p-(v-k)3^p-k.
\]
On the second it has exactly two eigenvalues, each of multiplicity \(v-1\):
\[
\eta_\pm(p)=-2^p\pm s(3^p-1).
\]
The negative branch \(\eta_-\) is always strictly negative. The ratio \(s(3^p-1)/2^p=s((3/2)^p-(1/2)^p)\) increases strictly from zero to infinity; hence \(\eta_+\) crosses zero exactly once at \(p_s\). Since \(s>1\), this occurs strictly between zero and one.

At \(p=p_s\), write \(u_s=2^{p_s}\) and \(3^{p_s}=1+u_s/s\). Using \(v=(k^2-r)/(k-r)\) and \(v-k=r(k-1)/(k-r)\), direct substitution gives the *exact phase identity*
\[
g(p_s)=\frac{k-s}{k-r}\big((k-1)u_s-k-s\big).
\]
Its prefactor is positive. When \(u_s>R\), \(g(0)=-1<0<g(p_s)\). The derivative \(g'(p)=(v-1)(\log2)2^p-(v-k)(\log3)3^p\) has at most one zero, so \(g\) crosses zero exactly once in \((0,p_s)\). When \(u_s\le R\), \(D_{p_s}\) is conditionally negative semidefinite. By the standard strict-downward negative-type property, \(D_p\) is conditionally negative *definite* for every \(0<p<p_s\). For completeness, this follows from Schoenberg positivity of \(e^{-tD_{p_s}}\) and the integral representation of \(d^p\) as a positive mixture of \(1-e^{-td^{p_s}}\): for each nonzero zero-sum vector, the quadratic form is strictly negative because \(e^{-tD_{p_s}}\to I\) as \(t\to\infty\). The case \(p=0\) is the negative identity on the zero-sum subspace. Above \(p_s\), \(\eta_+>0\), completing the global threshold proof.

In the spectral phase, the endpoint equality vectors are exactly
\[
\bigl(x,-N^{\mathsf T}x/s\bigr),\qquad x\perp\mathbf1.
\]
In the global phase they are multiples of \((\mathbf1,-\mathbf1)\). At equality of thresholds both spaces occur, orthogonally. The centered Schoenberg Gram matrix is \(-\tfrac12 P D_pP\) with \(P=I-J/(2v)\), so its rank equals \(2v-1\) minus the zero-sum equality dimension. These ranks are the asserted minimum affine Hilbert dimensions.

For a projective plane, \((v,k,\lambda)=(q^2+q+1,q+1,1)\), so \(s=\sqrt q\). For its complementary design, \((v,k,\lambda)=(q^2+q+1,q^2,q^2-q)\), with the *same* \(s\). Put \(\alpha=\log_2 3\), so \(3/2<\alpha<5/3\) and \(u_s=s(u_s^\alpha-1)\). Convexity gives \(u_s^\alpha-1\ge\alpha(u_s-1)\), hence \(u_s-1\le1/(\alpha s-1)<(s+1)/s^2\) for \(s\ge\sqrt2\). This is exactly \(u_s<R\) for the original design.

For complementary planes with \(q\ge4\), convexity also gives \(u_s^\alpha-1\le(3\alpha/2)(u_s-1)\), since \(1<u_s<2\). Consequently \(u_s-1>1/((3\alpha/2)s)>(s+1)/(s^4-1)\) for \(s\ge2\), as \(3\alpha/2<5/2\) and \(s^4-1\ge(5/2)s(s+1)\) for \(s\ge2\). This is \(u_s>R\) for the complement. For \(q=3\), the defining equation at \(p=1/2\) has negative left-minus-right value \(3-\sqrt3-\sqrt2<0\); thus \(u_s>\sqrt2>(9+\sqrt3)/8=R\). For \(q=2\), the defining equation has positive left-minus-right value at \(p=3/4\), since \(3^{3/4}>1+2^{1/4}\); hence \(u_s<2^{3/4}<7/4<(4+\sqrt2)/3=R\). The phase classification follows.

Finally, expansion of \(s(3^{p_s}-1)=2^{p_s}\) at \(p_s=0\) gives \(p_s=(\log3)^{-1}s^{-1}+O(s^{-2})\). For complementary planes in the global phase, the scalar equation simplifies to
\[
(q+1)\left[q(2^{p_g}-1)-(3^{p_g}-1)\right]=1.
\]
Taylor expansion and uniqueness give \(p_g=((q+1)(q\log2-\log3))^{-1}+O(q^{-4})=(\log2)^{-1}q^{-2}+O(q^{-3})\). This completes the proof.

## Verification
The accompanying executable `verify.py` builds ten incidence graphs from first principles: projective planes over the prime fields of orders \(2,3,5,7\), their complementary designs, and a cyclic symmetric \(2\)-\((11,5,2)\) design and complement. It independently reconstructs every shortest-path metric by breadth-first search, verifies the design identity and incidence singular values, and compares the full centered powered-distance spectrum with the theorem at six exponents per graph, including both sides of the critical exponent. It also verifies the critical rank and phase. These finite tests supplement, and do not replace, the all-parameter proof.

To replay, run `python verify.py` with NumPy installed. The output lists all ten cases and their critical exponent, phase, equality nullity, and minimum affine dimension. No external data files are required.

## Relationship to prior work
Obata and Zakiyyah (2018) establish the conditional-negative-definiteness criterion for unpowered graph-distance matrices, and compute several unpowered graph cases. Lou, Obata, and Huang (2020) compute quadratic embedding constants for joins and related families, again for the unpowered distance kernel. Choudhury and Nandi (arXiv first posted June 27, 2023) study unpowered quadratic embedding constants and distance-spectrum identities. Abiad et al. (2023) identify symmetric-design incidence graphs within diameter-three distance-regular graphs, but study Laplacian group inverses and the M-property. The exact fractional-power threshold, competing endpoint eigenspaces, design-complement phase switch, and unequal large-order scales stated here do not follow as explicitly stated results from these inspected papers. The general spectral methodology and Schoenberg characterization are not claimed as new. The \(r=1\) crown-graph specialization is deliberately excluded as previously treated. Historical priority for an equivalent powered-distance association-scheme formula cannot be ruled out.

## Limitations
The conclusion applies to unweighted, finite, symmetric \(2\)-design incidence graphs with \(k-\lambda\ge2\) and to the real powered-distance negative-type form. It does not treat arbitrary asymmetric designs, weighted incidence graphs, non-Hilbert target spaces, or every distance-regular graph. A hypothetical resonance \(u_s=R\) is characterized but its occurrence or impossibility for admissible nontrivial designs is not asserted. The asymptotics concern existing projective-plane orders tending to infinity, not all integers. All originality judgments are provisional pending independent historical review; no independent proof audit is claimed.

## References
- P. N. Choudhury and R. Nandi, *Quadratic embedding constants of graphs: Bounds and distance spectra*, arXiv:2306.15589, first version June 27, 2023. https://arxiv.org/abs/2306.15589
- N. Obata and A. Y. Zakiyyah, *Distance matrices and quadratic embedding of graphs*, Electronic Journal of Graph Theory and Applications 6 (2018), 37–60. https://doi.org/10.5614/ejgta.2018.6.1.4
- Z. Lou, N. Obata and Q. Huang, *Quadratic Embedding Constants of Graph Joins*, arXiv:2001.06752, first version January 19, 2020. https://arxiv.org/abs/2001.06752
- A. Abiad, Á. Carmona, A. M. Encinas et al., *The M-matrix group inverse problem for distance-biregular graphs*, Computational and Applied Mathematics 42 (2023), article 158. https://doi.org/10.1007/s40314-023-02301-1
- I. J. Schoenberg, *Metric spaces and positive definite functions*, Transactions of the American Mathematical Society 44 (1938), 522–536. https://doi.org/10.2307/1989894
