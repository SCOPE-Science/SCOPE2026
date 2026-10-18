# Crofton-random regular-simplex sections: exact face means and a logarithmic complexity law

## Finding
Let \(n\ge3\), let \(\Delta_{n-1}=\operatorname{conv}\{e_1,\ldots,e_n\}\) in its intrinsic Euclidean affine space, and intersect it with a random affine hyperplane drawn from motion-invariant hyperplane measure conditioned on meeting the simplex. Let \(Q_n\) be the resulting \((n-2)\)-polytope and let \(f_j(Q_n)\) count its \(j\)-faces. For independent standard Gaussians \(G_1,\ldots,G_m\), write \(G_{(1)}\le\cdots\le G_{(m)}\) and \(R_m=\mathbb E(G_{(m)}-G_{(1)})\). Then for every \(0\le j\le n-2\),
\[
\boxed{\mathbb E f_j(Q_n)=\binom n{j+2}\frac{R_{j+2}}{R_n}.}\tag{1}
\]
In particular, since \(R_2=2/\sqrt\pi\) and \(R_n\sim2\sqrt{2\log n}\),
\[
\mathbb E f_0(Q_n)\sim\frac{n^2}{2\sqrt{2\pi\log n}}.\tag{2}
\]
For an oriented version of the sampled plane, let \(K_n\) be the number of simplex vertices strictly below it. For every \(1\le k\le n-1\), its exact law is
\[
\boxed{\mathbb P(K_n=k)=\frac{\mathbb E(G_{(k+1)}-G_{(k)})}{R_n}.}\tag{3}
\]
The section has the combinatorial type of the product \(\Delta_{k-1}\times\Delta_{n-k-1}\). Consequently, for \(M_n=\min(K_n,n-K_n)\),
\[
\boxed{\frac{\log M_n}{\log n}\Longrightarrow 1-U^2,\qquad U\sim\operatorname{Uniform}(0,1).}\tag{4}
\]
More generally, for each fixed nonnegative integer \(J\), the joint logarithmic face-count limit is
\[
\boxed{\left(\frac{\log f_j(Q_n)}{\log n}\right)_{j=0}^{J}
\Longrightarrow (j+2-U^2)_{j=0}^{J}.}\tag{5}
\]
Here the same random variable \(U\) appears in every coordinate. In particular, the typical vertex-count exponent varies continuously between one and two, whereas its mean is nearly quadratic.

## Assumptions and scope
The affine span of \(\Delta_{n-1}\) is \(c_n+L_n\), with \(c_n=(1/n,\ldots,1/n)\) and \(L_n=\{x\in\mathbb R^n:\sum_i x_i=0\}\). Represent hyperplanes by \(\langle u,x-c_n\rangle=t\), with \(u\in S(L_n)\) and signed offset \(t\in\mathbb R\), identifying \((u,t)\) and \((-u,-t)\). The sampling law is the invariant measure \(d\sigma(u)\,dt\), restricted to hyperplanes intersecting the relative interior of the simplex and normalized to probability one. Thus the *marginal* law of \(u\) is proportional to the width of the simplex in direction \(u\); it is not Haar-uniform after conditioning. Almost surely no simplex vertex lies on the sampled hyperplane, so all face counts and ranks are unambiguous. Formula (1) holds at every permitted finite \(n\); (2), (4), and (5) are asymptotic statements as \(n\to\infty\). Standard Gaussian order statistics are defined separately for each sample size \(m\).

## Proof
**1. The Crofton normalization and section-face correspondence.** For a fixed normal \(u\), set \(a_i=\langle u,e_i-c_n\rangle=u_i\), and write \(w_S(u)=\max_{i\in S}a_i-\min_{i\in S}a_i\) for a nonempty vertex subset \(S\). Exactly the offsets in the interval \((\min_i a_i,\max_i a_i)\) give an interior simplex section; their total Lebesgue measure is \(w_{[n]}(u)\). For \(0\le j\le n-2\), each \(j\)-dimensional face of a generic section is the transversal intersection with exactly one \((j+1)\)-dimensional face of the simplex. The latter is indexed by a subset \(S\) with \(|S|=j+2\), and the section meets its relative interior precisely when \(\min_{i\in S}a_i<t<\max_{i\in S}a_i\). Therefore, integrating the face count first in \(t\),
\[
\mathbb E f_j(Q_n)
=\frac{\displaystyle\sum_{|S|=j+2}\int_{S(L_n)}w_S(u)\,d\sigma(u)}
{\displaystyle\int_{S(L_n)}w_{[n]}(u)\,d\sigma(u)}.\tag{6}
\]
No extra orientation factor appears because numerator and denominator use the same measure.

**2. Gaussian range evaluation.** Let \(G=(G_1,\ldots,G_n)\) have independent standard-normal coordinates and let \(Y=G-\overline G\mathbf1\), where \(\overline G=n^{-1}\sum_iG_i\). The direction \(u=Y/\|Y\|\) is Haar on \(S(L_n)\), independent of its radial length \(r=\|Y\|\), whose expectation is finite and nonzero. For every fixed subset \(S\) of cardinality \(m\), translation by \(\overline G\) cancels in the range, so
\[
R_m=\mathbb E\bigl[rw_S(u)\bigr]
=(\mathbb Er)\int_{S(L_n)}w_S(u)\,d\sigma(u).
\]
Substitution in (6) proves (1). The alternative absolutely convergent one-dimensional formula
\[
R_m=\int_{-\infty}^{\infty}\bigl(1-\Phi(z)^m-(1-\Phi(z))^m\bigr)\,dz\tag{7}
\]
follows by integrating the two tails of the sample maximum, where \(\Phi\) is the standard-normal CDF. In particular \(R_2=\mathbb E|G_1-G_2|=2/\sqrt\pi\). Gaussian upper and lower tail bounds for the maximum imply \(R_n\sim2\sqrt{2\log n}\); using \(\binom n2\sim n^2/2\) gives (2).

**3. Exact rank law and face-vector formula.** Fix \(u\) with distinct coordinate heights \(a_{(1)}<\cdots<a_{(n)}\). The offsets producing \(K_n=k\) are exactly \((a_{(k)},a_{(k+1)})\), of length \(a_{(k+1)}-a_{(k)}\). Integrating these lengths over \(u\) and using the independent Gaussian radius as above gives (3). Exactly \(k\) simplex vertices lie on one side and \(n-k\) on the other; the section is combinatorially \(\Delta_{k-1}\times\Delta_{n-k-1}\). A \(j\)-face arises from a \((j+2)\)-subset meeting both sides, hence
\[
f_j(Q_n)=\binom n{j+2}-\binom{K_n}{j+2}-\binom{n-K_n}{j+2},\tag{8}
\]
with \(\binom ab=0\) when \(a<b\). In particular \(f_0(Q_n)=K_n(n-K_n)\). Formula (8) also follows directly from the face correspondence in Step 1.

**4. An exact endpoint-rank identity.** For an integer \(m<n/2\), summing (3) over the first \(m\) gaps and, by Gaussian reflection symmetry, the last \(m\) gaps yields
\[
\mathbb P(M_n\le m)
=\frac{2\,\mathbb E(G_{(m+1)}-G_{(1)})}{R_n}.\tag{9}
\]
Fix \(0<\gamma<1\), set \(m=\lfloor n^\gamma\rfloor\), and write \(b_n=\sqrt{2\log n}\). Standard Gaussian tail estimates, e.g. \(\mathbb P(G<-z)\asymp z^{-1}e^{-z^2/2}\) for large \(z\), show by a binomial concentration argument that
\[
G_{(1)}/b_n\to-1,\qquad G_{(m+1)}/b_n\to-\sqrt{1-\gamma},\qquad G_{(n)}/b_n\to1
\]
in probability. For clarity, if \(z=(\sqrt{1-\gamma}\pm\delta)b_n\), the expected number of observations below \(-z\) is \(n^{1-(\sqrt{1-\gamma}\pm\delta)^2+o(1)}\). Its exponent is respectively smaller or greater than \(\gamma\), and Markov's inequality or a binomial Chernoff bound places the \((m+1)\)-st order statistic between the corresponding thresholds with probability tending to one. The endpoint order statistics follow from the same tail estimates. Moreover \(\mathbb E(\max_i|G_i|)^2\le2\log(2n)+2\) by integrating the Gaussian union bound, so all three variables divided by \(b_n\) have uniformly bounded second moments. Their convergence therefore also holds in \(L^1\). Consequently
\[
\frac{\mathbb E(G_{(m+1)}-G_{(1)})}{R_n}\longrightarrow
\frac{1-\sqrt{1-\gamma}}2.\tag{10}
\]
Equations (9) and (10) give \(\mathbb P(\log M_n/\log n\le\gamma)\to1-\sqrt{1-\gamma}\). At \(\gamma\le0\) the limiting CDF is zero; at \(\gamma\ge1\) it is one because \(1\le M_n\le n/2\). This is precisely the law of \(1-U^2\), proving (4).

**5. Joint face-count exponents.** The limit in (4) lies strictly between zero and one almost surely. Therefore \(M_n\to\infty\) and \(M_n/n\to0\) in probability, and for each fixed \(j\ge0\) the binomial identity (8) gives, uniformly along such sequences,
\[
f_j(Q_n)=\frac{M_n n^{j+1}}{(j+1)!}(1+o_{\mathbb P}(1)).\tag{11}
\]
Taking logarithms, dividing by \(\log n\), and applying the same random \(M_n\) simultaneously for finitely many \(j\) proves (5).

## Verification
Run `python3 verify.py` using the included standalone standard-library checker. It exhaustively verifies both face-count identities for every rank and face index in dimensions \(3\le n\le12\), checks quadrature identities for Gaussian mean ranges and rank gaps at four sizes, verifies the exact small-sample normal ranges, and independently estimates the Crofton-weighted face means from 33,000 random unit normals at dimensions four, seven, and ten. Execution prints `VERIFY_OK`. These are finite consistency tests, not proofs of the Gaussian extreme-quantile limit, which is supplied analytically in Steps 4–5.

## Relationship to prior work
Birkemeyer, Brose, Brandenburg, and Prün (2026), *Combinatorial slicing problems of polytopes: How (not) to reconstruct a polytope from its slices*, establish a combinatorial description of simplex sections, including product-of-simplices structure. The present result uses that geometry but assigns **motion-invariant conditional probabilities** and derives a new noncentral high-dimensional complexity law. De Loera, Lopez-Campos, and Torres (2024/2025), *On the Number of Vertices in Hyperplane Cross-Sections of Convex Polytopes*, investigate extreme slice vertex counts, attainable sequences, and gaps, not the invariant distribution or its Gaussian rank representation. The published *Exact mean and chi-square fluctuations of Haar central simplex-section vertex counts* studies **centroidal** hyperplanes with Haar normals; its mean is of quadratic order and its limiting fluctuation is chi-square. A generic Crofton-random **affine** hyperplane has a width-biased normal and a random offset; equations (2) and (4) give fundamentally different asymptotics. The general Gaussian-order-statistic and Crofton integration tools are classical; neither is claimed as new in isolation.

## Limitations
This theorem addresses only regular simplices, exact Crofton-invariant affine-hyperplane sampling, and the fixed-index logarithmic asymptotic regime. It does not claim finite-dimensional closed elementary forms for all Gaussian expected gaps, a quantitative rate of convergence in (4)–(5), or extension to nonregular simplices or multiple intersecting planes. An older equivalent identity in unindexed integral-geometric literature remains possible; the main novelty assessment concerns the integrated exact-law/logarithmic-limit theorem rather than claiming a new Gaussian tail principle. The 1994 Baryshnikov–Vitale paper on regular simplices and Gaussian samples was accessible only at abstract level, leaving a residual historical-overlap risk; independent scientific certification has not been performed.

## References
1. J. Birkemeyer, J. Brose, M. Brandenburg, and C. Prün, *Combinatorial slicing problems of polytopes: How (not) to reconstruct a polytope from its slices*, arXiv:2609.16195, first public September 14, 2026. https://arxiv.org/abs/2609.16195
2. J. A. De Loera, G. Lopez-Campos, and A. J. Torres, *On the Number of Vertices in Hyperplane Cross-Sections of Convex Polytopes*, arXiv:2412.12419, first public December 17, 2024. https://arxiv.org/html/2412.12419v3
3. *Exact mean and chi-square fluctuations of Haar central simplex-section vertex counts*, published mathematical research record (2026). https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-exact-mean-and-chi-square-fluctuations-of-haar-central-simplex-s--d3f9b0447a8e
4. Y. Baryshnikov and R. A. Vitale, *Regular simplices and Gaussian samples*, Discrete & Computational Geometry 11 (1994), 141–147. https://doi.org/10.1007/BF02574000
5. G. Ambrus and B. Gárgyán, *Minimal central slices of the regular simplex*, arXiv:2609.12714, first public September 11, 2026. https://arxiv.org/abs/2609.12714
