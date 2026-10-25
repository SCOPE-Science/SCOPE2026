# Gaussian width fluctuations of classical parking-function polytopes and their exposed vertex layers

## Finding
For each integer \(n\ge2\), let \(P_n\subset\mathbb R^n\) be the convex hull of classical parking functions: positive integral vectors whose nondecreasing rearrangement \(b_1\le\cdots\le b_n\) obeys \(b_j\le j\). Let \(U_n\) be uniform on the unit sphere, let \(W_n=h_{P_n}(U_n)+h_{P_n}(-U_n)\), and let \(K_n\) count the coordinates equal to one at the vertex exposed by \(U_n\). This vertex is unique with probability one. Put
\[
\mu=\frac{1+\sqrt2}{\sqrt\pi},\qquad
\sigma^2=\frac{14\pi+12\sqrt3-30\sqrt2-21}{24\pi}>0.
\]
Then, as \(n\to\infty\),
\[
\boxed{\left(\frac{W_n-\mathbb EW_n}{n},\frac{K_n-n/2}{\sqrt n}\right)
\Longrightarrow (Z,V)},
\]
where \(Z\) and \(V\) are **independent**, \(Z\sim N(0,\sigma^2)\), and \(V\sim N(0,1/4)\). In particular, the directional-width fluctuations are Gaussian at the exact order-\(n\) scale, with an explicitly determined nonzero limiting variance, despite a shared directional dependence with the exposed-vertex layer. Moreover the **exact finite-dimensional mean** is
\[
\mathbb EW_n=\binom n2\frac{\mu\,\Gamma(n/2)}{\sqrt2\,\Gamma((n+1)/2)},
\]
and replacing \(\mathbb EW_n\) by \(\mu n^{3/2}/2\) in the central limit theorem leaves the limit unchanged.

## Assumptions and scope
All widths use the ambient Euclidean structure in \(\mathbb R^n\); no lattice normalization or projection to the all-ones hyperplane is applied. The distribution of \(U_n\) is Haar probability on \(S^{n-1}\). Every asymptotic is along positive integer \(n\to\infty\); the theorem does not claim a finite-dimensional Gaussian law. The \(K_n\)-layer convention assigns \(K_n=1\) when every coordinate of the exposing direction is nonnegative, which is the correct lowest vertex layer. The exact mean identity holds for every \(n\ge2\).

## Proof
**1. Support and rank.** Let \(G_1,\ldots,G_n\) be independent standard normals, \(R_n=(\sum_iG_i^2)^{1/2}\), and \(U_n=G/R_n\). The classical vertex description consists of permutations of \((1,\ldots,1,k+1,\ldots,n)\), with \(k\in\{1,\ldots,n\}\). Sort the Gaussian entries as \(G_{(1)}\le\cdots\le G_{(n)}\). Rearrangement and optimization over \(k\) give the exact identities
\[
 h_{P_n}(G)=\sum_iG_i+\sum_{j=1}^n(j-1)(G_{(j)})_+
 =\sum_iG_i+\sum_{i<j}\max(0,G_i,G_j),
\]
\[
 R_nW_n=S_n:=\sum_{i<j}L(G_i,G_j),\quad
 L(x,y)=\max(0,x,y)-\min(0,x,y).
\]
The maximizing vertex has \(K_n=\max(1,J_n)\), where \(J_n=\#\{i:G_i<0\}\); the exceptional case \(J_n=0\) has probability \(2^{-n}\). Thus \(|K_n-J_n|\le1\), and \(J_n\) has the exact \(\mathrm{Binomial}(n,1/2)\) law.

**2. The first Hoeffding projection.** Write \(\phi(t)=(2\pi)^{-1/2}\exp(-t^2/2)\) and \(\Phi(t)=\int_{-\infty}^t\phi(s)\,ds\). The symmetric order-two kernel has
\[
 \mathbb EL(G_1,G_2)=\mu,\qquad
 f(x):=\mathbb E[L(x,G_2)]
 =|x|\Phi(|x|)+\phi(|x|)+\phi(0).
\]
The mean is \(\mu=(1+\sqrt2)/\sqrt\pi\), either by integrating \(f\) or by summing the absolute differences between the three entries \(0,G_1,G_2\). Hoeffding's decomposition reads
\[
 S_n=\binom n2\mu+(n-1)\sum_{i=1}^n(f(G_i)-\mu)+D_n,
 \quad\mathbb ED_n=0,\quad\mathbb E D_n^2=O(n^2).
\]
The final bound follows by orthogonality of distinct degenerate pairs and finite second moments of \(L\). Consequently \(D_n/(n^{3/2})\to0\) in \(L^2\).

**3. Radial correction and joint central limit.** Set \(T_n=\sum_i(G_i^2-1)\). The chi-square expansion gives
\[
 \frac1{R_n}=\frac1{\sqrt n}\left(1-\frac{T_n}{2n}+O_{\mathbb P}(n^{-1})\right).
\]
Using the order-\(n^2\) deterministic part of \(S_n\) and the order-\(n^{3/2}\) random first projection yields
\[
 \frac{W_n-\mathbb EW_n}{n}
 =\frac1{\sqrt n}\sum_{i=1}^n \psi(G_i)+o_{\mathbb P}(1),
 \qquad\psi(x)=f(x)-\mu-\frac\mu4(x^2-1).
\]
Here exact centering is valid because \(\mathbb EW_n-\mu n^{3/2}/2=O(\sqrt n)\). Radial independence implies \(\mathbb EW_n=\mathbb ES_n/\mathbb ER_n\) and \(\mathbb ER_n=\sqrt2\,\Gamma((n+1)/2)/\Gamma(n/2)\), proving the exact mean formula. Meanwhile,
\[
 \frac{K_n-n/2}{\sqrt n}=\frac1{\sqrt n}\sum_{i=1}^n \bigl(\mathbf1_{\{G_i<0\}}-1/2\bigr)+o(1).
\]
The bivariate iid central limit theorem applies, since both summands are square integrable. The function \(\psi\) is even, while the centered indicator is odd; hence their covariance is zero. The joint Gaussian limit therefore has **independent coordinates** and its second variance is \(1/4\).

**4. Exact first variance.** The Gaussian scaling identity for the degree-one homogeneous kernel \(L\) implies
\[
 \mathbb E[(G^2-1)f(G)]=\mu/2.
\]
Indeed, differentiating the expectation of \(L(\sqrt{1+t}G_1,\sqrt{1+t}G_2)\) at \(t=0\), or differentiating the joint Gaussian density, gives \(\mathbb E[L(G_1,G_2)(G_1^2+G_2^2-2)]=\mu\); symmetry divides this by two. For completeness, the following elementary half-normal integral evaluations supply the second moment. With \(T=|G|\) and \(c=\phi(0)\),
\[
\begin{aligned}
 \mathbb E[T^2\Phi(T)^2]&=\frac7{12}+\frac{1+1/\sqrt3}{2\pi},\\
 \mathbb E[\phi(T)^2]&=\frac1{2\pi\sqrt3},\\
 \mathbb E[T\Phi(T)\phi(T)]&=\frac{1+1/\sqrt3}{4\pi},\\
 \mathbb E[T\Phi(T)]&=\frac{1+\sqrt2}{2\sqrt\pi},\\
 \mathbb E[\phi(T)]&=\frac1{2\sqrt\pi}.
\end{aligned}
\]
These follow from \(\mathbb E[g(T)]=2\int_0^\infty g(t)\phi(t)dt\), integration by parts, and Gaussian substitutions. Expanding \(f(G)^2=(T\Phi(T)+\phi(T)+c)^2\) gives
\[
 \mathbb Ef(G)^2=\frac{6\sqrt3+12\sqrt2+7\pi+30}{12\pi}.
\]
Since \(\mathbb E(G^2-1)^2=2\),
\[
 \operatorname{Var}\psi(G)
 =\mathbb Ef(G)^2-\mu^2-\frac\mu2\cdot\frac\mu2
 +\frac{\mu^2}{16}\cdot2
 =\mathbb Ef(G)^2-\frac98\mu^2
 =\frac{14\pi+12\sqrt3-30\sqrt2-21}{24\pi}.
\]
The variance is strictly positive because \(f\) is not a quadratic polynomial; equivalently \(\psi\) is not almost surely constant. This completes the joint limit and all claimed identities.

## Verification
The accompanying standalone `verify.py` checks, from the defining kernel and closed forms, the half-normal integral identities and finite-sample support optimization against direct enumerations of parking-function vertices for small dimensions. Its checks are numerical corroboration; the infinite-dimensional claims are proved above. Separate Monte Carlo simulations for dimensions 16, 64, 256 showed width-fluctuation variances progressing toward \(0.0177789330\) and negligible sample covariance with the centered exposed layer.

## Relationship to prior work
Hanada, Lentfer, and Vindas-Meléndez introduced and studied generalized parking-function polytopes, including the classical vertex representation; Bayer and collaborators established broader generalized-permutahedron descriptions. Behrend's analysis recognizes the classical family as a translate of partial permutohedra. Existing first-order random-width analysis of partial permutohedra identifies the support formula and the limit of width divided by \(n^{3/2}\), but **does not imply the joint second-order Gaussian limit, exact variance, or asymptotic independence** given here. The connection to classical Hoeffding decomposition is an explicit tool, not a novelty claim about U-statistic theory itself. Known central limit theorems for *random parking functions* (chosen discrete words) and the *width of parking-function trees* address different random variables.

## Limitations
The result treats the classical one-parameter parking-function polytope under uniform Euclidean direction, not the full family of generalized parking-function polytopes or uniform-volume random points. No Berry–Esseen rate or large-deviation law is claimed. The support representation and binomial vertex-layer law are antecedents, not separately asserted original discoveries. The originality assessment is limited by the reach of the inspected literature, particularly a later full-length work on faces of parking-function polytopes whose full text could not be completely reviewed. Independent verification has not been performed.

## References
1. M. Hanada, J. Lentfer, and A. R. Vindas-Meléndez, *Generalized parking function polytopes*, arXiv:2212.06885, first public 2022-12-13, https://arxiv.org/abs/2212.06885.
2. M. M. Bayer et al., *Combinatorics of generalized parking-function polytopes*, arXiv:2403.07387, first public 2024-03-12, https://arxiv.org/abs/2403.07387.
3. R. E. Behrend, *Ehrhart polynomials of partial permutohedra*, arXiv:2403.06975, first public 2024-03-11, https://arxiv.org/abs/2403.06975.
4. F. Liu and W. Thawinrak, *Faces of parking function polytopes*, FPSAC 2025 proceedings, https://www.mat.univie.ac.at/~slc/wpapers/FPSAC2025/11.pdf.
5. W. Hoeffding, *A class of statistics with asymptotically normal distribution*, Annals of Mathematical Statistics 19 (1948), 293–325 (classical U-statistic decomposition).
