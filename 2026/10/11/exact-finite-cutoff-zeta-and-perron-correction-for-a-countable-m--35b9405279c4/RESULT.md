# Exact finite-cutoff zeta and Perron correction for a countable Markov map

## Finding

Let \(T:[0,\infty)\to[0,\infty)\) be continuous, affine on each interval \([n-1,n]\) for positive integers \(n\), and specified at nonnegative integers by
\[
T(n)=\begin{cases}0,&n\text{ even},\\4^j+1,&n\text{ odd and }4^{j-1}\le n<4^j,\end{cases}
\]
where \(j\ge1\). For each integer \(r\ge1\), put \(N_r=4^r\) and define the compact invariant survivor
\[
K_r=\{x\in[0,N_r]:T^n(x)\in[0,N_r]\text{ for every integer }n\ge0\}.
\]
Write \(m_1=4\), \(m_j=3\cdot4^{j-1}\) for \(2\le j\le r\), and let the \(r\)-by-\(r\) nonnegative integer matrix \(C_r\) have entries
\[
(C_r)_{jk}=\begin{cases}
m_k,&k\le j,\\
1,&k=j+1,\\
0,&k>j+1.
\end{cases}
\]
Then, for every \(r\ge1\) and every \(n\ge1\),
\[
\#\operatorname{Fix}(T^n|_{K_r})=\operatorname{tr}(C_r^n),\qquad
\zeta_{T|K_r}(z)=\det(I_r-zC_r)^{-1},\qquad
h_{\mathrm{top}}(T|_{K_r})=\log\rho(C_r).
\]
For \(r\ge2\), writing \(m=m_r=3\cdot4^{r-1}\) and \(\lambda_r=\rho(C_r)\), one has the sharp asymptotic
\[
\boxed{\lambda_r=m+\frac13-\frac4{135m}+O(m^{-2})}\quad(r\to\infty).
\]
In particular, \(\#\operatorname{Fix}(T|_{K_r})=4^r\); and, for every \(r\ge2\),
\[
\#\operatorname{Fix}(T^2|_{K_r})=\frac35\,16^r+\frac12\,4^r+\frac{32}{5}.
\]
The constants \(1/3\) and \(-4/135\) quantify the spectral contribution of the single successor state beyond each four-adic step. The rational zeta formula computes periodic-point counts at every period from a matrix of dimension \(r\), instead of \(4^r\).

## Assumptions and scope

The map is the explicitly specified expanding Schweitzer-competition map studied in Kalocsai [1]. Each interval \(I_i=[i-1,i]\) maps onto \([0,4^{\ell(i)}+1]\), with \(\ell(i)=\min\{j\ge1:i\le4^j\}\), and each branch has slope of magnitude at least five. The set \(K_r\) consists of points with *all* nonnegative iterates inside the closed cutoff interval; it is not the entire bounded-orbit set, and no statement concerns periodic-orbit growth on the noncompact full phase space. The zeta function is the Artin–Mazur formal power series, and the entropy is the usual topological entropy for a continuous map of a compact invariant set. Constants in the asymptotic \(O\)-term are absolute and the limit is along integer \(r\to\infty\).

## Proof

**1. Finite-state coding and periodic points.** For \(1\le i\le N_r\), put \(I_i=[i-1,i]\) and let \(A_r\) be the \(N_r\)-by-\(N_r\) zero-one matrix with
\[
(A_r)_{ij}=\mathbf1_{\{1\le j\le\min(4^{\ell(i)}+1,N_r)\}}.
\]
Since each branch is affine, maps over every indicated target interval, and expands by at least five, every allowed infinite itinerary has a unique realization in \(K_r\); nested inverse images of full target intervals have diameter at most \(5^{-n}\). Conversely every survivor admits such an itinerary. The coding is continuous and onto. A survivor at an interior integer boundary has at most two possible itineraries and eventually maps to zero; thus the coding is at most two-to-one. The finite-to-one entropy factor principle (equivalently, cylinder growth for this expanding Markov partition) gives \(h_{\mathrm{top}}(T|_{K_r})=\log\rho(A_r)\).

An allowed closed itinerary of length \(n\) has a unique fixed point of \(T^n\) by contraction of its inverse branches. The only *periodic* integer is zero: even positive integers map to zero, while a positive odd integer maps to a strictly larger positive odd integer, and the odd-integer orbit strictly increases. Zero belongs only to \(I_1\) and has the single constant itinerary. Hence distinct cyclic itinerary words with a specified initial state give distinct periodic points, including all boundary cases, and \(\#\operatorname{Fix}(T^n|_{K_r})=\operatorname{tr}(A_r^n)\).

**2. Exact exponential-to-logarithmic compression.** Partition the state indices into \(G_1=\{1,2,3,4\}\) and \(G_j=\{4^{j-1}+1,\dots,4^j\}\) for \(2\le j\le r\). Every row of \(A_r\) is identical within a group. Write \(A_r=UV\), where \(U\) is the indicator matrix for the groups and the \(j\)-th row of \(V\) is the common zero-one successor row from \(G_j\). The quotient \(VU\) equals \(C_r\): it sees every state in groups at levels at most \(j\), and exactly one state in the next level, except at the terminal cutoff. Consequently \(\operatorname{tr}(A_r^n)=\operatorname{tr}(C_r^n)\) for \(n\ge1\), the nonzero eigenvalues of \(A_r\) and \(C_r\) coincide, and Sylvester's identity gives \(\det(I_{N_r}-zA_r)=\det(I_r-zC_r)\). The exponential trace identity \(\exp(\sum_{n\ge1}\operatorname{tr}(C_r^n)z^n/n)=\det(I_r-zC_r)^{-1}\) proves the zeta formula. The group graph has loops and is strongly connected, so \(C_r\) is primitive, with Perron root \(\lambda_r\).

**3. Sharp Perron asymptotics.** Assume \(r\ge5\). Put \(m=m_r\), \(a=m_{r-1}=m/4\), \(b=m_{r-2}=m/16\), and normalize a positive right Perron vector by \(x_r=1\). Successive rows of \(C_r\) are componentwise nondecreasing, so \(0<x_1\le\dots\le x_r=1\). For each \(j<r\),
\[
\lambda_r x_j=\sum_{k\le j}m_kx_k+x_{j+1}\le4^jx_j+x_{j+1}.
\]
Because \(\lambda_r\ge m\) and \(4^j\le m/3\), it follows that \(x_j\le(3/(2m))x_{j+1}\). The last row gives \(\lambda_r=m+\delta\) with \(\delta=\sum_{k<r}m_kx_k\), so \(0<\delta\le(m/3)x_{r-1}\le1/2\). In particular, \(\delta=O(1)\).

Let \(u=x_{r-1}\), \(v=x_{r-2}\), and \(S=\sum_{k\le r-3}m_kx_k\). The bound just proved gives \(u=O(m^{-1})\), \(v=O(m^{-2})\), and \(S=O(m^{-2})\), since \(\sum_{k\le r-3}m_k=m/48\). The last three eigenvector equations are exactly
\[
(\lambda_r-b)v=u+S,\qquad
(\lambda_r-a)u=1+bv+S,\qquad
\delta=au+bv+S.
\]
All denominators are bounded below by fixed positive multiples of \(m\). Solving and expanding uniformly gives
\[
u=\frac1{\lambda_r-a}+\frac{b}{(\lambda_r-a)^2(\lambda_r-b)}+O(m^{-3}),\qquad
v=\frac1{(\lambda_r-a)(\lambda_r-b)}+O(m^{-3}),
\]
and hence
\[
\delta=\frac{a}{\lambda_r-a}
+\frac{ab}{(\lambda_r-a)^2(\lambda_r-b)}
+\frac{b}{(\lambda_r-a)(\lambda_r-b)}+O(m^{-2}).
\]
Since \(a=m/4\), \(b=m/16\), and \(\lambda_r=m+\delta\), the first term yields \(\delta=1/3+O(m^{-1})\). Substituting this first approximation back into the three displayed terms gives, respectively,
\[
\frac13-\frac4{27m}+O(m^{-2}),\qquad
\frac4{135m}+O(m^{-2}),\qquad
\frac4{45m}+O(m^{-2}).
\]
Adding proves \(\delta=1/3-4/(135m)+O(m^{-2})\), with a uniform bound from the preceding inequalities.

**4. First two fixed-point counts.** The diagonal of \(C_r\) is \((m_1,\ldots,m_r)\), so \(\operatorname{tr}(C_r)=\sum_jm_j=4^r\). Also \(\operatorname{tr}(C_r^2)=\sum_jm_j^2+2\sum_{j<r}m_j\): only adjacent off-diagonal pairs contribute. For \(r\ge2\), the geometric sums are \(\sum_jm_j^2=(3/5)16^r+32/5\) and \(\sum_{j<r}m_j=4^{r-1}\), giving the stated formula.

## Verification

The self-contained Python 3 standard-library file `CHECK.py` checks equality of \(\operatorname{tr}(A_r^n)\) and \(\operatorname{tr}(C_r^n)\) exactly for cutoffs \(r=1,2,3\) and up to seven/four iterates, checks the first two fixed-point counts and exact characteristic coefficients for \(1\le r\le6\), and computes high-precision Perron eigenvectors and the scaled asymptotic residual for \(4\le r\le11\). It printed `CHECK_OK 46`. In particular, it recomputes \(\det(I_2-zC_2)=1-16z+44z^2\). The finite diagnostics do not prove the all-period trace formula or the uniform asymptotic; those follow from the arguments above.

## Relationship to prior work

Kalocsai [1, Sections 1 and 3.3] defines the map, its countable partition, and its expanding symbolic dynamics. The companion article [2, Section 6] already aggregates a *stochastic transition matrix* by these four-adic steps; that aggregation is prior art and is **not** claimed as a new compression principle. Here the object is instead the integer *orbit-counting* adjacency matrix of the compact survivor cutoff. The concrete new determination is the full family of exact finite-cutoff zeta functions and fixed-point counts, together with the sharp two-term spectral correction \(1/3-4/(135m)\). The general fact that an expanding finite Markov model has a determinant zeta function is classical [3]; applying it alone does not give this explicit family or the spectral asymptotic. Ruelle [3] discusses general interval zeta and transfer-operator principles, without examining these four-adic survivor cutoffs. Olivares-Vinales [4] concerns general unimodal/multimodal zeta phenomena, not this specific countable-map finite-cutoff spectrum.

## Limitations

This is a theorem for the particular Schweitzer-competition map and the specific natural cutoff sequence \(N_r=4^r\). Other cutoff sequences, other piecewise-linear Markov maps, rates for invariant probabilities, and an infinite-volume zeta function are not treated. The asymptotic is for the Perron root, not the full spectrum. Generic graph zeta identities and the stochastic step aggregation are established prior tools, not independent novelty claims. No independent external validation has been performed.

## References

[1] Z. Kalocsai, *Symbolic dynamics, shadowing and representation of real numbers with some countably piecewise linear Markov maps*, arXiv:2508.17159v1 (first public 2025-08-23), https://arxiv.org/html/2508.17159v1.

[2] Z. Kalocsai, *Convergence of pushforward measures for certain countably piecewise linear Markov maps*, arXiv:2508.18172v1 (first public 2025-08-25), https://arxiv.org/html/2508.18172v1.

[3] D. Ruelle, *Dynamical zeta functions for maps of the interval*, arXiv:math/9404235v1 (1994), https://arxiv.org/html/math/9404235v1.

[4] J. Olivares-Vinales, *The Artin–Mazur zeta function for interval maps*, arXiv:2405.10560v2 (2024), https://arxiv.org/abs/2405.10560.
