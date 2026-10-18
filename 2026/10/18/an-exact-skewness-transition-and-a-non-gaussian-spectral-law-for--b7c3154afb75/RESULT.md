# An exact skewness transition and a non-Gaussian spectral law for circular geometric graph edge counts

## Finding
Let \(n\ge3\), let \(U_1,\ldots,U_n\) be independent uniform points on the unit circle \(\mathbb R/\mathbb Z\), and connect two vertices whenever their circular distance is less than \(r\), where \(0<r<1/2\). Write \(E_n(r)\) for the number of edges, \(p=2r\), and \(m=\binom n2\). Define
\[
\delta(r)=\begin{cases}r^2(3-8r),&0<r\le1/3,\\(1-2r)^3,&1/3\le r<1/2.\end{cases}
\]
Then \(\mathbb E E_n(r)=mp\), \(\operatorname{Var}(E_n(r))=mp(1-p)\), and the *exact* third centered moment is
\[
\boxed{\mathbb E[(E_n(r)-mp)^3]=mp(1-p)(1-2p)+n(n-1)(n-2)\delta(r).}
\]
Although the variance equals that of an Erdős–Rényi edge count, the third centered moment has a strictly positive geometric correction. Set
\[
r_n=\frac12-\frac1{3+\sqrt{8n-15}}.
\]
For every \(n\ge3\), the third centered moment is strictly positive when \(0<r<r_n\), exactly zero when \(r=r_n\), and strictly negative when \(r_n<r<1/2\). In particular \(r_3=1/3\), and
\[
\frac12-r_n\sim\frac1{\sqrt{8n}}.
\]
For each fixed \(0<r<1/2\), with independent mean-one exponential random variables \((Y_k)_{k\ge1}\), the edge-count fluctuations satisfy
\[
\boxed{\frac{E_n(r)-\binom n2(2r)}n\ \xrightarrow{\mathrm d}\ \sum_{k=1}^{\infty}\frac{\sin(2\pi kr)}{\pi k}(Y_k-1).}
\]
The series converges in \(L^2\), has variance \(r(1-2r)\), and has strictly positive third cumulant \(\delta(r)\), hence is never Gaussian. Consequently the standardized third moment at fixed radius converges to
\[
\frac{2^{3/2}\delta(r)}{[2r(1-2r)]^{3/2}}>0.
\]

## Assumptions and scope
The model has *exactly* \(n\) independently sampled latent positions (not a Poisson number of vertices). Distances use the shorter arc of the unit circle. Edge selection is a deterministic hard threshold; ties at the distance cutoff have probability zero. The finite-size sign theorem assumes integers \(n\ge3\) and a fixed radius \(0<r<1/2\). The spectral limit lets \(n\to\infty\) with \(r\) fixed strictly inside this interval. It makes no claim for radii varying with \(n\), and does not assert a Gaussian limit in the near-complete window.

## Proof
**1. Pairwise-independence and forest lemma.** Put \(I_{ij}=\mathbf 1\{d(U_i,U_j)<r\}\). Translation invariance gives \(\mathbb E(I_{ij}\mid U_i)=p\). More generally, edge indicators indexed by any *forest* are mutually independent: integrate the position of a leaf conditional on all remaining positions, obtaining the constant factor \(p\), and induct. In particular any two distinct edges are independent, so the first two moment formulas follow.

**2. Exact triangle probability.** Order three sampled points cyclically. Their successive circle gaps have the \(\operatorname{Dirichlet}(1,1,1)\) law. All three pairwise distances are at most \(r\) exactly when either (i) one gap is at least \(1-r\), or (ii) every gap is at most \(r\). These events are disjoint for \(r<1/2\). The first has probability \(3r^2\) because each gap has \(\operatorname{Beta}(1,2)\) marginal. The second has probability zero for \(r<1/3\), and \((3r-1)^2\) for \(1/3\le r<1/2\), by inclusion–exclusion on the uniform simplex of gaps. Thus the triangle probability is
\[
T(r)=3r^2+(3r-1)_+^2.
\]
For three edge indicators forming a triangle, pairwise independence gives
\[
\mathbb E[(I_{12}-p)(I_{23}-p)(I_{31}-p)]=T(r)-p^3=\delta(r)>0.
\]

**3. Third cumulant by edge triples.** Expand the cube of \(\sum_{i<j}(I_{ij}-p)\). Terms with three equal edges contribute \(mp(1-p)(1-2p)\). Terms with exactly two equal edges vanish by pairwise independence. Any three distinct edges that do not form a triangle form a forest and also contribute zero. Each triangle contributes \(6\delta(r)\), accounting for its six orderings, giving the stated formula.

**4. Unique finite-size sign transition.** For \(0<r<1/3\), the case \(n=3\) simplifies to
\[
\mathbb E[(E_3(r)-3p)^3]=6r(1-3r)>0.
\]
For larger \(n\), the additional contribution \(6[\binom n3-\binom32]\delta(r)\), after the elementary positive scaling of the diagonal term, can be handled directly by writing the third moment divided by \(\binom n2\) as
\[
p(1-p)(1-2p)+2(n-2)\delta(r).
\]
At \(n=3\) this is positive for \(r<1/3\), and increasing \(n\) makes it strictly larger because \(\delta(r)>0\). For \(r\ge1/3\), put \(q=1-p\). The third moment becomes
\[
\binom n2 q[-1+3q+2(n-3)q^2].
\]
The bracket is strictly increasing in \(q>0\), is negative at \(q=0\), and is nonnegative at \(q=1/3\), with equality only when \(n=3\). Its unique positive root is \(q_n=2/(3+\sqrt{8n-15})\). Since \(r=(1-q)/2\), the unique sign change is \(r_n\), as claimed.

**5. Fourier spectral limit.** The centered connection kernel \(h_r(x,y)=\mathbf1\{d(x,y)<r\}-p\) is degenerate: its conditional expectation given either coordinate is zero. The nonzero Fourier coefficients of its translation-invariant profile are
\[
a_k(r)=\frac{\sin(2\pi kr)}{\pi k},\qquad k\in\mathbb Z\setminus\{0\}.
\]
The coefficients at opposite frequencies agree, and the zero-frequency coefficient vanishes. Write \(Z_{n,k}=n^{-1/2}\sum_{i=1}^n e^{2\pi\mathrm ikU_i}\). For every fixed Fourier cutoff \(K\), the truncated centered edge count divided by \(n\) equals
\[
\sum_{k=1}^{K}a_k(r)(|Z_{n,k}|^2-1).
\]
The multivariate central limit theorem gives independent standard complex Gaussians as the limits of \((Z_{n,k})_{1\le k\le K}\), with independent squared moduli having \(\operatorname{Exp}(1)\) distributions. The truncation remainder is a degenerate order-two \(U\)-statistic whose variance is
\[
\frac{\binom n2}{n^2}\,2\sum_{k>K}a_k(r)^2\le\sum_{k>K}a_k(r)^2\longrightarrow0
\]
uniformly in \(n\). This proves convergence to the stated independent exponential series. Parseval yields \(\sum_{k\ge1}a_k(r)^2=p(1-p)/2=r(1-2r)\). Since \(\sum_k|a_k(r)|^3<\infty\), the limit has third cumulant \(2\sum_{k\ge1}a_k(r)^3\). The convolution identity for a centered triangle identifies this quantity with \(T(r)-p^3=\delta(r)>0\). Thus the limit is non-Gaussian and its standardized third cumulant has the stated value.

## Verification
Run the included `verify.py` with Python 3.10 or later. It uses only the standard library and performs 993 checks, including exact enumeration of three-vertex graphs on discrete circular grids, exact algebraic comparisons of the finite-size sign polynomial at rational radii, and Fourier sum numerical checks for the limiting variance and third cumulant. Discrete-grid enumeration is a finite approximation, not a proof of the continuous theorem. The analytical forest, Dirichlet-gap, polynomial-root, and Fourier-tail arguments above establish the statements for all admissible parameters.

## Relationship to prior work
Wilsher–Dettmann–Ganesh (arXiv:2202.08044v1, 2022) analyze isolated-node Poisson limits for one-dimensional *soft* random geometric graphs on a circle with a Poisson number of nodes, and explicitly distinguish the hard-cutoff model. Their theorem does not give the fixed-vertex hard-model edge-count cumulant or its sign threshold. Liu–Rácz (arXiv:2103.15249v1, 2021) use signed triangles to detect high-dimensional spherical geometry; their Section 4 gives a related general triangle-based statistic, not the finite-size one-dimensional edge-count skewness threshold. Bonnet–Hirsch–Rosen–Willhalm (arXiv:2212.12268v1, 2022) establish high-dimensional sparse random-geometric functional limit theory, with a different limit regime. The Fourier argument uses classical degenerate-\(U\)-statistic and Fourier principles rather than claiming those tools are new. The asserted contribution is the explicit full finite-size third-moment law, its unique radius threshold, and its linkage to an explicit fixed-radius non-Gaussian spectral law.

## Limitations
The result concerns a circle with iid *uniform* positions, fixed deterministic vertex count, and a hard distance threshold. It does not cover nonuniform points, general metric domains, independent edge noise, or a Poisson vertex count without further work. The sign threshold describes the third centered moment (skewness), not stochastic domination or the sign of all higher odd cumulants. The limiting law concerns fixed radii. The historical novelty assessment is based on inspected primary literature and mathematical-record searches, not an independent comprehensive priority certificate; equivalent formulas in broader \(U\)-statistic or random-connection-model literature remain a residual risk.

## References
1. M. Wilsher, C. P. Dettmann, A. J. Ganesh, *The Distribution of the Number of Isolated Nodes in the 1-Dimensional Soft Random Geometric Graph*, arXiv:2202.08044v1 (first posted 2022-02-16), https://arxiv.org/abs/2202.08044.
2. S. Liu, M. Z. Rácz, *Phase transition in noisy high-dimensional random geometric graphs*, arXiv:2103.15249v1 (first posted 2021-03-28), https://arxiv.org/abs/2103.15249.
3. G. Bonnet, C. Hirsch, D. Rosen, D. Willhalm, *Limit theory of sparse random geometric graphs in high dimensions*, arXiv:2212.12268v1 (first posted 2022-12-23), https://arxiv.org/abs/2212.12268.
