# Exact uniform Hilbert geometry of simplices: central balls, median rigidity, and distinct extreme-value limits

## Finding
Let \(S\) be a nondegenerate Euclidean simplex of dimension \(d=m-1\ge1\). In its positive barycentric coordinates \(p=(p_1,\ldots,p_m)\), with \(\sum_i p_i=1\), equip its interior with the **full-cross-ratio** Hilbert metric
\[
H(p,q)=\max_i\log\frac{p_i}{q_i}-\min_i\log\frac{p_i}{q_i}.
\]
Some references use half this value; every result below uses the displayed normalization. Let \(c=(1/m,\ldots,1/m)\) be the centroid, let \(U,V\) be independent uniform points of \(S\) under normalized Euclidean volume, and set \(C_m=H(c,U)\), \(D_m=H(U,V)\).

**Exact central-ball volume and unique optimal centers.** For all \(t>0\) and \(q=e^t\),
\[
\frac{\operatorname{vol}_d\{u\in S:H(c,u)\le t\}}{\operatorname{vol}_d(S)}
=\Pr(C_m\le t)
=\prod_{j=1}^{m-1}\frac{j(q-1)}{m+j(q-1)}.
\]
For each fixed finite \(t>0\), the centroid uniquely maximizes the **Euclidean** volume of a radius-\(t\) Hilbert ball among all interior centers. It also uniquely minimizes \(p\mapsto\mathbb E H(p,U)\). At radius zero every ball has zero Euclidean volume, so uniqueness is not asserted for that case.

**Exact pair-distance distribution and means.** For \(t\ge0\),
\[
\Pr(D_m\le t)=m(q-1)^{m-1}\int_0^1
\frac{u^{m-1}(1-u)^{m-1}}{(1+(q-1)u)^{m-1}}\,du,
\qquad q=e^t,
\]
where the expression is zero at \(t=0\). With \(H_{m-1}=\sum_{j=1}^{m-1}1/j\),
\[
\mathbb E D_m=2H_{m-1},\qquad
\mathbb E C_m=\log m-\sum_{k=1}^{m}(-1)^{k-1}\binom mk\log k.
\]
In the small-radius and large-radius regimes of fixed \(m\), respectively,
\[
\Pr(C_m\le t)=\frac{(m-1)!}{m^{m-1}}t^{m-1}(1+O_m(t)),\quad t\downarrow0;
\qquad
\Pr(C_m>t)\sim mH_{m-1}e^{-t},\quad t\to\infty.
\]

**Two distinct dimensional fluctuation laws.** Let \(G,G_1,G_2\) be independent standard Gumbel variables with CDF \(\Pr(G\le x)=\exp(-e^{-x})\). As \(m\to\infty\),
\[
C_m-\log m-\log\log m\ \Longrightarrow\ G,
\qquad
D_m-2\log m\ \Longrightarrow\ G_1+G_2.
\]
The second limiting distribution has the explicit CDF
\[
\Pr(G_1+G_2\le z)=\int_0^\infty e^{-u-e^{-z}/u}\,du
=2e^{-z/2}K_1(2e^{-z/2}),
\]
where \(K_1\) is the modified Bessel function of the second kind. The general logistic-sample range theorem and the general Gumbel extreme-value facts are classical and are **not** independently claimed as new.

## Assumptions and scope
The simplex may have any Euclidean shape, because both the Hilbert metric and relative Euclidean volume are affine invariant. Its dimension is \(d=m-1\ge1\). The random law is uniform **Euclidean** Lebesgue measure, not Busemann, Holmes--Thompson, or other intrinsic Hilbert volume. All centers must lie in the open simplex. Unique maximizing-volume centers are claimed only for finite strictly positive radii; the distribution formula includes \(t=0\). The asymptotic laws concern simplices of increasing dimension and independent uniform samples in each dimension.

## Proof
### 1. Logarithmic simplex coordinates and the unique maximal-volume center
The barycentric metric formula follows from the line/chord cross ratio: the endpoint facets are determined by the largest and smallest positive barycentric ratios. Define the zero-sum space and centered log-softmax map by
\[
\mathcal H=\{y\in\mathbb R^m:\sum_i y_i=0\},\qquad
\Phi(y)_i=\frac{e^{y_i}}{\sum_j e^{y_j}},\qquad
N(y)=\max_i y_i-\min_i y_i.
\]
Then \(\Phi\) bijects \(\mathcal H\) with the interior of \(S\), with
\(H(\Phi(y),\Phi(z))=N(y-z)\). By the standard softmax Jacobian, the pullback of uniform Euclidean simplex measure to \(\mathcal H\) has a positive density proportional to
\[
f(y)=\left(\sum_i e^{y_i}\right)^{-m}.
\]
Indeed, in independent log-ratio coordinates the Jacobian magnitude equals \(\prod_i\Phi(y)_i\), which on the zero-sum space is \((\sum_i e^{y_i})^{-m}\) up to a fixed factor from the coordinate change. Thus \(f\) is permutation invariant and real analytic. Its log Hessian is strictly negative on \(\mathcal H\), since for nonzero \(v\in\mathcal H\), with \(p_i=\Phi(y)_i\),
\[
\frac{d^2}{ds^2}\log f(y+sv)\big|_{s=0}
=-m\left[\sum_i p_i v_i^2-\left(\sum_i p_i v_i\right)^2\right]<0.
\]
Here the bracket is a strictly positive variance because all \(p_i>0\) and a nonzero zero-sum \(v\) cannot be constant.

For \(t>0\), the closed variation-norm ball \(K_t=\{z\in\mathcal H:N(z)\le t\}\) is compact, convex, symmetric and has nonempty interior. The relative Euclidean volume of a Hilbert radius-\(t\) ball centered at \(\Phi(y)\) is
\[
F_t(y)=A_m\int_{K_t}f(y+z)\,dz,
\]
where \(A_m>0\) is the fixed normalization factor. Prékopa--Leindler says convolution of two log-concave functions is log-concave; applying it to \(f\) and the indicator of \(K_t\) shows \(F_t\) log-concave. The function is permutation invariant, and averaging all coordinate permutations of \(y\in\mathcal H\) gives zero. Jensen's inequality for \(\log F_t\) yields \(F_t(0)\ge F_t(y)\).

Uniqueness requires more than weak log concavity. The integral of the real-analytic function \(f(y+z)\) over the fixed compact set \(K_t\) is real analytic in \(y\). For each nonzero \(v\in\mathcal H\), \(F_t(sv)\to0\) as \(s\to+\infty\): on the bounded \(K_t\) the exponential of the largest directional coordinate in \(\sum_i e^{sv_i+z_i}\) dominates uniformly. If some \(y\ne0\) were another maximizer, log concavity would force \(F_t(sy)=F_t(0)\) on \(0\le s\le1\). Analytic continuation along the real line would make \(F_t(sy)\) constant for all real \(s\), contradicting its decay at \(+\infty\). Therefore only \(y=0\), the centroid, maximizes the ball's relative Euclidean volume.

### 2. Unique mean-distance center
Uniform barycentric coordinates admit the gamma/Dirichlet representation
\[
U_i=\frac{E_i}{\sum_j E_j},\qquad E_1,\ldots,E_m\text{ iid Exp}(1).
\]
For a candidate center \(\Phi(y)\), common normalizations cancel, so
\[
M(y)=\mathbb EH(\Phi(y),U)
=\mathbb E\bigl[\max_i(y_i-\log E_i)-\min_i(y_i-\log E_i)\bigr].
\]
The expectation is finite, convex in \(y\), and invariant under coordinate permutations. Therefore \(y=0\) minimizes \(M\). To prove uniqueness, take any two indices \(i,j\) with \(y_i<y_j\), and let \(y'\) swap these coordinates. Write \(a=(y_i+y_j)/2\). Consider the sample point of logarithmic exponentials with \(z_i=z_j=0\) and \(z_k=y_k-a\) for all other indices \(k\). At this point, the range of \(y-z\) and of \(y'-z\) equals \(y_j-y_i>0\), while the range of \((y+y')/2-z\) equals zero. This strict Jensen inequality persists in an open neighborhood. All \(\log E_i\) have positive density on the entire real line, so the neighborhood has positive probability and \(M((y+y')/2)<M(y)=M(y')\). By convexity and permutation symmetrization \(M(0)\le M((y+y')/2)\), implying \(M(0)<M(y)\) for every nonconstant \(y\). In \(\mathcal H\) this establishes the unique minimizer.

### 3. Exact central-ball distribution, means and endpoint behavior
With the independent exponential representation, \(C_m=\log(E_{(m)}/E_{(1)})\). The minimum \(R=E_{(1)}\) has exponential rate \(m\). By exponential memorylessness, conditionally on \(R=r\), the other \(m-1\) samples equal \(r\) plus independent unit exponentials. Consequently, for \(q=e^t>1\),
\[
\Pr(C_m\le t)
=\int_0^\infty me^{-mr}(1-e^{-(q-1)r})^{m-1}\,dr
=\frac{m}{q-1}B\left(\frac{m}{q-1},m\right)
=\prod_{j=1}^{m-1}\frac{j(q-1)}{m+j(q-1)},
\]
where \(B\) is the beta function. Expanding this exact finite product at \(q-1=0\) proves the small-radius formula; expanding it in reciprocal \(q-1\) gives the large-radius tail.

For the mean, \(\mathbb E\log E_{(1)}=-\gamma-\log m\). Expanding \(\Pr(E_{(m)}\le x)=(1-e^{-x})^m\), and integrating the logarithmic moments of exponential densities, gives
\[
\mathbb E\log E_{(m)}=-\gamma-\sum_{k=1}^m(-1)^{k-1}\binom mk\log k.
\]
Subtracting yields the stated exact \(\mathbb E C_m\).

### 4. Exact two-point law
Represent the independent \(V\) by independent unit exponentials \(F_i\), so that
\[
D_m=\max_i Z_i-\min_i Z_i,\qquad Z_i=\log(E_i/F_i).
\]
The \(Z_i\) are independent standard logistic variables with \(L(z)=e^z/(1+e^z)\). For iid continuous samples, the CDF of the range is
\[
m\int_{-\infty}^\infty L'(z)[L(z+t)-L(z)]^{m-1}\,dz.
\]
Under \(u=L(z)\), one has \(L(z+t)-L(z)=(q-1)u(1-u)/(1+(q-1)u)\), giving the asserted integral. Moreover \(L(Z_i)\) are iid Uniform\((0,1)\), with maximum having Beta\((m,1)\) law. Thus
\[
\mathbb E\max_i Z_i=\mathbb E\log\frac{U_{(m)}}{1-U_{(m)}}
=H_m-\frac1m=H_{m-1}.
\]
By logistic symmetry the expected minimum is its negative; the expected range is \(2H_{m-1}\).

### 5. Distinct Gumbel limits
The maximum of \(m\) independent unit exponentials satisfies \(E_{(m)}/\log m\to1\) in probability, whereas \(mE_{(1)}\) has the exact unit-exponential distribution. Slutsky's theorem therefore yields
\[
C_m-\log m-\log\log m\Longrightarrow-\log E,
\]
for a unit exponential \(E\), which is standard Gumbel. For the logistic sample, for any fixed real \(x,y\),
\[
\Pr\{\max_i Z_i\le\log m+x,\ \min_i Z_i\ge-\log m-y\}
=\bigl[L(\log m+x)-L(-\log m-y)\bigr]^m
\longrightarrow \exp(-e^{-x}-e^{-y}).
\]
The centered maximum and negative minimum therefore converge jointly to **independent** standard Gumbels. Their sum gives the law for \(D_m-2\log m\). Since independent standard Gumbels equal \(-\log E_1\) and \(-\log E_2\) in law, the CDF of their sum is \(\Pr(E_1E_2\ge e^{-z})=\int_0^\infty e^{-u-e^{-z}/u}\,du\), with the displayed modified Bessel representation. This completes the theorem.

## Verification
Run `python3 verify_hilbert_geometry.py` with the Python 3 standard library. The standalone program passes **167 diagnostics**: 70 exact rational comparisons of the beta-product against independent inclusion--exclusion, numerical comparison of the two mean formulas with integrated survival probabilities, independent logistic real-line and quantile-coordinate calculations, strict permutation-Jensen witnesses, direct barycentric metric tests, one-dimensional volume-center tests, finite-radius endpoint checks, and selected Gumbel convergence values. These computations are deliberately not claimed to prove infinitely many dimensions, the use of Prékopa--Leindler, or the analytic uniqueness arguments. Those are proved above.

## Relationship to prior work
Acharya--Gezalyan--Mount (first public January 19, 2026) develop high-dimensional Hilbert-metric classifiers and describe Hilbert balls as finite intersections of halfspaces; they explicitly motivate probability-simplex data. Their result does not determine the Euclidean volume of those balls, the unique volume-maximizing and mean-distance centers, or the full random-distance laws. Nielsen--Sun (2017; 2022/2023) develop the simplex variation-norm isometry, clustering and embeddings. Their log-coordinate isometry, the cross-ratio formula, and the combinatorial ball descriptions are prior mathematics, not newly claimed. Cohen--Fausti consider projective Hilbert distance contraction on probability measures rather than the present Euclidean volume profiles. Classical Dirichlet/exponential representations, Prékopa--Leindler, logistic sample-range integrals and Gumbel extreme-value theory are established and may imply individual probabilistic formulas once the geometric model is identified. The precise all-dimensional geometric synthesis with two center-rigidity assertions and distinct calibrated laws is the present contribution. Older unindexed Hilbert geometry or order-statistics results might contain equivalent statements; the priority check is best knowledge rather than proof of absolute historical uniqueness.

## Limitations
The random law is Euclidean-uniform, **not** the intrinsic Hilbert/Busemann/Holmes--Thompson measure. No claim is made for general polytopes, nonuniform Dirichlet sampling, boundary centers, or algorithmic performance. The center-volume uniqueness excludes zero radius. The full cross-ratio convention differs by a factor two from some Hilbert metric papers. Existing logistic sample-range and extreme-value theorems are acknowledged as prior tools, and independent mathematical verification has not been performed. Published or unindexed older sources might subsume an isolated component or the combined theorem.

## References
1. A. Acharya, A. H. Gezalyan and D. M. Mount, *Classifiers in High Dimensional Hilbert Metrics*, arXiv:2601.13410, first public 2026-01-19; SWAT 2026, DOI 10.4230/LIPIcs.SWAT.2026.1. https://drops.dagstuhl.de/storage/00lipics/lipics-vol370-swat2026/html/LIPIcs.SWAT.2026.1/LIPIcs.SWAT.2026.1.html
2. F. Nielsen and K. Sun, *Clustering in Hilbert simplex geometry*, arXiv:1704.00454 (2017). https://ar5iv.labs.arxiv.org/html/1704.00454
3. F. Nielsen and K. Sun, *Non-linear Embeddings in Hilbert Simplex Geometry*, Proceedings of Machine Learning Research 221 (2023), 254--266; arXiv:2203.11434 (2022). https://proceedings.mlr.press/v221/nielsen23a/nielsen23a.pdf
4. S. N. Cohen and E. Fausti, *Hyperbolic contractivity and the Hilbert metric on probability measures*, arXiv:2309.02413 (2023). https://arxiv.org/abs/2309.02413
5. A. Prékopa, *Logarithmic concave measures with application to stochastic programming*, Acta Scientiarum Mathematicarum 32 (1971), 301--316, for the classical log-concavity convolution principle.
