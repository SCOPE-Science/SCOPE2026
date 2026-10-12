# Independent corner Poisson clouds and Gaussian inversion fluctuations

## Finding
Let \(\pi_n\) be uniformly distributed over permutations of \(\{1,\ldots,n\}\). Define two point measures on \([0,\infty)^2\) by
\[
\Xi_n^+=\sum_{i=1}^n\delta_{(i/\sqrt n,\,(n+1-\pi_n(i))/\sqrt n)},\qquad
\Xi_n^-=\sum_{i=1}^n\delta_{((n+1-i)/\sqrt n,\,\pi_n(i)/\sqrt n)}.
\]
Also write
\[
K_n=\#\{(i,j):1\le i<j\le n,\ \pi_n(i)>\pi_n(j)\},\qquad
Z_n=\frac{K_n-n(n-1)/4}{n^{3/2}}.
\]
As \(n\to\infty\), in the product of the vague point-measure topologies and the usual real topology,
\[
\boxed{(\Xi_n^+,\Xi_n^-,Z_n)\ \Rightarrow\ (\Pi^+,\Pi^-,G),}
\]
where \(\Pi^+\) and \(\Pi^-\) are independent homogeneous Poisson point processes of intensity one on \([0,\infty)^2\), and \(G\) is an independent Gaussian random variable with mean zero and variance \(1/36\).

In particular, if \(M_n=\max_{1\le i\le n}|\pi_n(i)-i|\), then jointly with \(Z_n\),
\[
\frac{n-M_n}{\sqrt n}\Rightarrow T,\qquad
\mathbb P(T>t)=e^{-t^2}\ \ (t\ge0),\qquad T\perp G.
\]
The last distributional identity is a consequence of the single joint process theorem, not a separate claimed contribution.

## Assumptions and scope
The only probabilistic hypothesis is that each of the \(n!\) permutations is equally likely. The point measures contain all \(n\) permutation-matrix points under opposite-corner scaling; only points in bounded regions contribute to vague limits. Coordinates are nonnegative. No independence is asserted at finite \(n\). The result concerns \(n\to\infty\) and fixed bounded regions in the rescaled corners.

## Proof
**1. Factorial moments of the corner counts.** Fix finitely many pairwise disjoint rectangles in the marked disjoint union of the two corner planes, with bounded coordinates, nonzero area, and boundary of planar Lebesgue measure zero. Let \(A_{n,h}\) be the sets of permutation-matrix cells whose rescaled coordinates belong to rectangle \(h\). For large \(n\), different marked rectangles correspond to disjoint original cells; opposite-corner cells occupy disjoint row and column bands. By Riemann sums,
\[
|A_{n,h}|=n\,|B_h|+o(n).
\]
Every row or column intersects at most \(O(\sqrt n)\) cells in the union \(A_n=\bigcup_h A_{n,h}\), while \(|A_n|=O(n)\). For any fixed \(m\), the number of ordered, distinct cells drawn with prescribed multiplicities \(m_h\) from the \(A_{n,h}\), \(\sum_hm_h=m\), differs from \(\prod_h|A_{n,h}|^{m_h}\) by at most \(O_m(n^{m-1/2})\). Indeed, each forbidden repeated row or column fixes at most \(O(n^{m-1}\sqrt n)\) configurations; all repeated cells are included in that error.

For \(m\) cells having pairwise distinct rows and columns, the probability that a uniform permutation contains all of them is precisely \((n)_m^{-1}\), where \((n)_m=n(n-1)\cdots(n-m+1)\). Consequently, for corner counts \(W_{n,h}=\Xi_n^{\pm}(B_h)\),
\[
\mathbb E\prod_h(W_{n,h})_{m_h}
=\frac{\prod_h|A_{n,h}|^{m_h}+O_m(n^{m-1/2})}{(n)_m}
\longrightarrow\prod_h|B_h|^{m_h}.
\]
These are the joint factorial moments of independent Poisson counts with respective means \(|B_h|\). Since Poisson laws are determined by their factorial moments and the first moments provide tightness on bounded sets, this proves convergence of each finite family of corner counts and hence, using a countable convergence-determining class of rectangles, convergence of the two point processes to independent unit-intensity Poisson processes.

**2. Uniform Gaussian stability under finitely many pinned cells.** Condition on any \(m\) nonconflicting equations \(\pi_n(i_a)=j_a\), with fixed \(m\) as \(n\to\infty\). The remaining \(n-m\) values, read in the increasing order of the remaining positions, form a uniformly random relative permutation. Their internal inversion count therefore has the law of \(K_{n-m}\). All inversions involving at least one pinned position contribute between zero and \(mn\). Also the difference of the unconditioned inversion means \(n(n-1)/4\) and \((n-m)(n-m-1)/4\) is at most \(mn/2\). Thus the law of the centered conditional \(Z_n\) differs from that of
\[
\frac{K_{n-m}-(n-m)(n-m-1)/4}{n^{3/2}}
\]
by a random shift bounded by \(3m/(2\sqrt n)\), uniformly in the chosen pinned cells.

The inversion count has the same distribution as a sum of independent uniforms \(U_j\) on \(\{0,\ldots,j-1\}\), for \(1\le j\le n\). Therefore
\[
\mathbb E K_n=\frac{n(n-1)}4,\qquad
\operatorname{Var}(K_n)=\frac{n(n-1)(2n+5)}{72},
\]
and the triangular-array Lindeberg theorem gives \(Z_n\Rightarrow G\sim N(0,1/36)\). The bounded shift proves uniformly over every admissible set of \(m\) pins that, for each real \(u\),
\[
\mathbb E[e^{iuZ_n}\mid\pi_n(i_a)=j_a,\ 1\le a\le m]
\longrightarrow e^{-u^2/72}.
\]

**3. Joint independence.** Expand each product of falling factorial corner counts as a sum over compatible pinned cells. Multiply by \(e^{iuZ_n}\), condition on the prescribed cells, and use the uniform bound from step 2. For each fixed vector of nonnegative integers \((m_h)\) and real \(u\),
\[
\mathbb E\left[e^{iuZ_n}\prod_h(W_{n,h})_{m_h}\right]
\longrightarrow e^{-u^2/72}\prod_h|B_h|^{m_h}.
\]
Uniform boundedness of factorial moments of every fixed degree supplies the required uniform integrability for subsequential limits. The products of Poisson factorial moments are moment-determinate; alternatively, inclusion-exclusion with Bonferroni bounds identifies the joint characteristic transform on all count-level events. The limit is therefore the product law of the Poisson count vector and \(G\), for every finite family of rectangles. Local tightness yields the asserted joint vague point-process convergence.

**4. Maximum-distance corollary.** For each permutation point \((i,\pi_n(i))\), the sums of its coordinates in the two rescaled corners are respectively \((n+1-(\pi_n(i)-i))/\sqrt n\) and \((n+1+(\pi_n(i)-i))/\sqrt n\). Hence the exact finite identity is
\[
\frac{n-M_n}{\sqrt n}=\min_{\xi\in\Xi_n^+\cup\Xi_n^-}(\xi_1+\xi_2)-\frac1{\sqrt n}.
\]
For \(t\ge0\), the triangle \(\{(x,y)\in[0,\infty)^2:x+y\le t\}\) has area \(t^2/2\); independently in two unit Poisson fields, its combined void probability is \(e^{-t^2}\). The limiting minimum is finite almost surely and does not lie on any deterministic boundary, so the continuous-mapping/void-probability argument proves the Rayleigh-type law and its independence from \(G\).

## Verification
Run the standalone Python 3 script `verify.py` from the same directory. It uses only the standard library. Exact exhaustive checks cover 46,232 permutations over orders two through eight; they verify the inversion mean and variance, the exact maximum/corner identity, the first two factorial moments of corner counts, and the uniform-relative-permutation property under 25 fixed-arc configurations. Successful execution prints `VERIFY_OK`. These finite checks corroborate identities used in the proof; the point-process and Gaussian limits are established analytically, not by finite enumeration.

## Relationship to prior work
Kløve, Lin, Tsai and Tzeng [2], Section 2 and Section 4, study the identical Chebyshev permutation distance and express its finite ball counts as a permanent. Thus the finite marginal distribution of \(M_n\) is already encoded in a known exact combinatorial object. The present result does not claim that permanent identity or the marginal inversion central limit theorem as new. The substantive statement is *joint* convergence of two spatial extreme-point processes with the global inversion fluctuation and their three-way independence. Baxter and Zeilberger [3] prove independent Gaussian limits for inversion count and major index, a different second statistic with no extreme point process. Barbour and Janson [1] provide a functional combinatorial central limit theorem for permutation-sum processes, but do not address this corner Poisson process or its joint law with inversions. Neither known finite Chebyshev ball formula nor the cited joint Gaussian theorem directly implies the three-way Poisson–Gaussian assertion without an additional conditioning argument.

## Limitations
The uniform-permutation hypothesis is essential to the exact \((n)_m^{-1}\) pinned-cell law. This result makes no claim for biased permutation measures, for rates in total variation, for a finite-sample factorization, or for independence of arbitrary rank statistics. A historically earlier or more general corner-process limit could alter priority; the literature comparison is not an independent scholarly audit.

## References
[1] A. D. Barbour and S. Janson, *A functional combinatorial central limit theorem*, arXiv:0907.0347v1 (first public version, 2009-07-02), https://arxiv.org/abs/0907.0347.

[2] T. Kløve, T.-T. Lin, S.-C. Tsai, and W.-G. Tzeng, *Permutation Arrays Under the Chebyshev Distance*, arXiv:0907.2682v1 (first public version, 2009-07-15), https://arxiv.org/abs/0907.2682; see Section 2 and Section 4.

[3] A. Baxter and D. Zeilberger, *The Number of Inversions and the Major Index of Permutations are Asymptotically Joint-Independently Normal*, arXiv:1004.1160v1 (first public version, 2010-04-07), https://arxiv.org/abs/1004.1160.
