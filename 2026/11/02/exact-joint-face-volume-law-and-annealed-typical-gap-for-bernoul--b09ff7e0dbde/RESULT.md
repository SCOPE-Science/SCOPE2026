# Exact joint face–volume law and annealed–typical gap for Bernoulli-thinned cross-polytopes

## Finding
For every integer \(d\ge2\), independently retain each of the \(2d\) vertices \(\pm e_i\) of the standard cross-polytope with probability \(0<p<1\). Let \(Q_d\) be their convex hull when at least one vertex survives. The entire intrinsic combinatorial type and volume are determined by the numbers \(K\) of coordinate pairs retained twice and \(L\) retained once. If \(K\ge1\), \(Q_d\) is an \(L\)-fold pyramid over the \(K\)-dimensional cross-polytope, with dimension \(K+L\), intrinsic volume \(2^K/(K+L)!\), and complete face polynomial
\[
\mathcal F_{Q_d}(t)=\bigl((1+2t)^K+t^{K+1}\bigr)(1+t)^L.
\]
Here \(\mathcal F_P(t)=\sum_{j=-1}^{\dim P} f_j(P)t^{j+1}\) includes the empty and full faces. If \(K=0\) and \(L\ge1\), the hull is a regular simplex of dimension \(L-1\), with intrinsic volume \(\sqrt L/(L-1)!\) and face polynomial \((1+t)^L\). If \(K=L=0\), the selection is empty.

Write \(A_d=\{\dim Q_d=d\}\) and \(\rho=p/(2-p)\). Then
\[
\mathbb P(A_d)=[p(2-p)]^d-[2p(1-p)]^d,
\quad
\mathbb P(K=k\mid A_d)=\frac{\binom dk\rho^k(1-\rho)^{d-k}}{1-(1-\rho)^d},\quad 1\le k\le d.
\]
On \(A_d\), put \(R_d=\operatorname{Vol}_d(Q_d)/\operatorname{Vol}_d(C_d)\), where \(C_d=\operatorname{conv}\{\pm e_i:1\le i\le d\}\), and let \(Z_d=\mathcal F_{Q_d}(1)\) count all faces including the empty and full faces. Then their **complete joint law** is the above truncated-binomial law of \(K\) under the mapping
\[
(R_d,Z_d)=(2^{K-d},\;2^{d-K}(3^K+1)).
\]
In particular,
\[
\mathbb E(R_d\mid A_d)=\frac{(1+\rho)^d-(1-\rho)^d}{2^d[1-(1-\rho)^d]},
\]
\[
\mathbb E(Z_d\mid A_d)=\frac{(2+\rho)^d+(2-\rho)^d-2[2(1-\rho)]^d}{1-(1-\rho)^d},
\quad
\mathbb E\bigl[\operatorname{Vol}_d(Q_d)/\operatorname{Vol}_d(C_d)\bigr]=p^d[1-(1-p)^d],
\]
where lower-dimensional hulls contribute zero to ambient volume.

For each fixed \(0<p<1\), as \(d\to\infty\) under the conditional law given \(A_d\),
\[
\left(\frac{\log Z_d}{d},\frac{\log R_d}{d}\right)
\longrightarrow
\left(\log2+\rho\log\frac32,(\rho-1)\log2\right)
\quad\text{in probability}.
\]
The centered vector divided by \(\sqrt d\) converges in distribution to
\[
\sqrt{\rho(1-\rho)}\left(\log\frac32,\log2\right)G,
\qquad G\sim N(0,1),
\]
with centers \(d[\log2+\rho\log(3/2)]\) and \(d(\rho-1)\log2\), respectively. In contrast, the exponential growth rates of the conditional means are \(\log(2+\rho)\) for \(Z_d\) and \(\log[(1+\rho)/2]\) for \(R_d\); each is strictly larger than its corresponding typical rate for \(0<\rho<1\). Thus mean and typical complexity/relative volume differ exponentially.

## Assumptions and scope
The independent survival probability is common to all vertices and fixed strictly between zero and one for the asymptotic statements. Coordinate signs and labels carry the ordinary Euclidean metric. The full-dimensional event is essential for the logarithm of the ambient-dimensional volume; without it, the volume can be zero. The face polynomial counts the empty face and the polytope itself, so subtract two for the number of nonempty proper faces of a nonempty polytope. All formulas are exact for integer \(d\ge2\), except where limits are explicitly stated.

## Proof
**1. Coordinate-pair classification.** For each coordinate independently, both signs survive with probability \(p^2\), exactly one with probability \(2p(1-p)\), and neither with probability \((1-p)^2\). Thus \((K,L,d-K-L)\) is multinomial with these three probabilities. Permuting and changing coordinate signs sends every outcome with given \((K,L)\) to \(\operatorname{conv}(\pm e_1,\dots,\pm e_K,e_{K+1},\dots,e_{K+L})\). When \(K\ge1\), the first \(2K\) vertices make a cross-polytope, and adjoining each remaining positive unit vector is a pyramid whose apex is orthogonal to the previous affine span at distance one. The intrinsic dimension is \(K+L\); successive pyramid volume factors give \(2^K/(K+L)!\). Each pyramid multiplies the face polynomial by \(1+t\), while a cross-polytope has the proper-face counts \(f_{j-1}=2^j\binom Kj\) for \(0\le j\le K\) and a unique full face. This proves its polynomial. When \(K=0\) and \(L\ge1\), the selected standard basis vectors form a simplex; the Gram matrix of its \(L-1\) edge vectors is \(I+\mathbf1\mathbf1^T\), of determinant \(L\), proving the stated intrinsic volume. If no vertices survive, the hull is empty.

**2. Exact joint distribution.** To span the full ambient space, no coordinate can be absent; at least one coordinate pair must be retained twice, since \(d\) single vertices span only affine dimension \(d-1\). Thus \(A_d\) is exactly \(\{K+L=d,K\ge1\}\). Conditional on no missing coordinate, each coordinate is doubly represented independently with probability \(\rho=p^2/[p^2+2p(1-p)]=p/(2-p)\). Truncation at \(K\ge1\) gives the claimed finite law. Since \(\operatorname{Vol}_d(C_d)=2^d/d!\), the volume ratio is \(R_d=2^{K-d}\); evaluating the face polynomial at \(t=1\) yields \(Z_d=2^{d-K}(3^K+1)\). Applying the truncated-binomial probability generating function to these two functions gives both conditional means. Without conditioning, expanding over the full-dimensional configurations yields \(\mathbb E R_d=2^{-d}\{[2p]^d-[2p(1-p)]^d\}\), which equals the displayed formula.

**3. High-dimensional laws.** The conditioning differs from an ordinary \(\operatorname{Bin}(d,\rho)\) law only by excluding the event \(K=0\), whose probability \((1-\rho)^d\) tends exponentially to zero. Hence the binomial law of large numbers and central limit theorem apply without a change in limiting distribution. The identities
\[
\log R_d=(K-d)\log2,
\quad \log Z_d=d\log2+K\log(3/2)+\log(1+3^{-K})
\]
show that the final remainder is bounded by \(\log2\), and vanishes after either \(d\) or \(\sqrt d\) normalization. The exact conditional mean formulas imply
\[
\lim_{d\to\infty}d^{-1}\log\mathbb E Z_d=\log(2+\rho),\qquad
\lim_{d\to\infty}d^{-1}\log\mathbb E R_d=\log\frac{1+\rho}{2}.
\]
For \(0<\rho<1\), strict concavity of the logarithm applied to the mixtures \((1-\rho)2+3\rho\) and \((1-\rho)1+2\rho\) proves that both mean exponents strictly exceed their typical exponents. The latter mixture is divided by two, producing exactly the claimed volume rate.

## Verification
The provided `verify.py` reconstructs full face lattices from convex-hull supporting facets in every canonical type with \(2\le d\le5\), checks Euclidean volumes, and checks all conditional and unconditional probability/moment formulas using rational arithmetic for \(2\le d\le8\) and three rational survival probabilities. It also checks the strict mean–typical inequalities at four numerical parameters. It reports `ALL_CHECKS_PASSED`. These finite calculations are cross-checks and do not prove the asymptotic results; those follow from the binomial limit theorems and the bounded logarithmic remainder in the proof.

## Relationship to prior work
Bonnet and O'Reilly study the facets and heights of random polytopes generated by independently sampled *continuous* uniform sphere points, including dimension-growing regimes [1]. Newman introduces independent vertex retention in a more general two-step random-polytope model and proves bounds for that model [2]. Their mathematical settings motivate exactly solvable benchmarks for vertex reduction, but neither inspected primary text states this fixed-cross-polytope full joint face–volume law or the strict separation of its mean and typical exponents. The pyramid face-polynomial identity is standard; novelty is not asserted for that standalone identity. Related results for randomly retained vertices of a three-dimensional cube concern a different original polytope and do not imply the present dimension-uniform cross-polytope classification.

## Limitations
The result does not extend automatically to general centrally symmetric vertex configurations, nonuniform correlated retention or continuously sampled points. The Gaussian limit is conditional on full dimension, an event whose unconditioned probability typically decays exponentially for fixed \(p<1\). Historical priority may be affected by older specialized face-enumeration work not captured by the bounded searches.

## References
[1] G. Bonnet and E. O'Reilly, *Facets of spherical random polytopes*, arXiv:1908.04033, first public version 2019-08-12; published in Mathematische Nachrichten (2022). https://arxiv.org/abs/1908.04033

[2] A. Newman, *Doubly random polytopes*, arXiv:2006.07000, first public version 2020-06-12; Random Structures & Algorithms 61 (2022), 364–382. https://arxiv.org/abs/2006.07000
