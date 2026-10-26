# Exact SLD and two-scale limit for complete bipartite qudit graph states

## Finding

Let \(p\) be prime and let \(m,n\ge2\). For the \(p\)-level graph state associated with the complete bipartite graph \(K_{m,n}\), write its Shor–Laflamme distribution (SLD) as \((A_0,\ldots,A_{m+n})\), and set \(W_{m,n}^{(p)}(z)=\sum_{k=0}^{m+n}A_kz^k\). Define

\[
Z_r(z)=\frac{(1+(p-1)z)^r+(p-1)(1-z)^r}{p},\qquad
N_r(z)=\frac{p-1}{p}\big((1+(p-1)z)^r-(1-z)^r\big).
\]

Then the exact generating polynomial is

\[
W_{m,n}^{(p)}(z)=Z_m(z)Z_n(z)+p^{m-1}z^mN_n(z)+p^{n-1}z^nN_m(z)+(p-1)^2p^{m+n-2}z^{m+n}.
\]

Equivalently, if \(K\) is a random variable with \(\Pr(K=k)=A_k/p^{m+n}\), then for every fixed \(m\), as \(n\to\infty\),

\[
\frac{K}{n}\ \Rightarrow\ \frac1p\,\delta_{(p-1)/p}+\frac{p-1}{p}\,\delta_1.
\]

Thus a fraction \(1/p\) of the stabilizer weight mass lies asymptotically near support fraction \((p-1)/p\), while the remaining fraction \((p-1)/p\) lies near full support. This is a two-scale limit, not a single binomial profile.

## Assumptions and scope

The local dimension \(p\) is prime, the adjacency matrix is the ordinary unweighted adjacency matrix of \(K_{m,n}\) over \(\mathbb F_p\), and \(m\ge2\) is fixed while \(n\to\infty\). The SLD coefficient \(A_k\) counts stabilizer elements whose Pauli support has size \(k\); normalization by \(p^{m+n}\) makes these coefficients a probability distribution. The result does not assert a noise threshold or an entanglement certificate by itself, and it does not cover composite local dimensions or the regime where both part sizes grow proportionally.

## Proof

Let the bipartition be \(A\sqcup B\), with \(|A|=m\) and \(|B|=n\). A stabilizer element is indexed by a vector \(r=(r_A,r_B)\in\mathbb F_p^{m+n}\) and has local pair \((r_i,(\Gamma r)_i)\) at vertex \(i\), where \(\Gamma\) is the adjacency matrix. Put \(S_A=\sum_{i\in A}r_i\) and \(S_B=\sum_{j\in B}r_j\). Since the graph is complete bipartite, \((\Gamma r)_i=S_B\) on \(A\) and \((\Gamma r)_j=S_A\) on \(B\).

For a vector in \(\mathbb F_p^r\), let its support weight be the number of nonzero coordinates. Character orthogonality gives the support-weight enumerator of vectors whose coordinate sum is zero:

\[
Z_r(z)=\frac1p\sum_{a\in\mathbb F_p}\prod_{i=1}^r\left(1+z\sum_{x\in\mathbb F_p\setminus\{0\}}\omega^{ax}\right)
=\frac{(1+(p-1)z)^r+(p-1)(1-z)^r}{p},
\]

where \(\omega\) is any primitive \(p\)-th root of unity. The enumerator for vectors with nonzero coordinate sum is the unrestricted enumerator minus \(Z_r\), hence it is \(N_r(z)\).

Partition all \(r\) into four disjoint cases. If \(S_A=S_B=0\), a vertex is supported exactly when its own coordinate is nonzero, giving \(Z_mZ_n\). If \(S_A=0\) and \(S_B\ne0\), every vertex in \(A\) is supported and the support on \(B\) is exactly the support of \(r_B\); there are \(p^{m-1}\) choices for \(r_A\) with zero sum, giving \(p^{m-1}z^mN_n\). The case \(S_A\ne0\), \(S_B=0\) gives \(p^{n-1}z^nN_m\) by the same argument. If both sums are nonzero, every vertex is supported; each side has respectively \((p-1)p^{m-1}\) and \((p-1)p^{n-1}\) choices, giving \((p-1)^2p^{m+n-2}z^{m+n}\). Summing the four disjoint contributions proves the polynomial identity.

For the limit, choose \(r\) uniformly from \(\mathbb F_p^{m+n}\). The sums \(S_A,S_B\) are independent and uniform, so the four cases have probabilities \(p^{-2}\), \((p-1)p^{-2}\), \((p-1)p^{-2}\), and \((p-1)^2p^{-2}\). The support weight of \(r_B\), before conditioning, is binomial with parameters \(n\) and \((p-1)/p\), hence its ratio to \(n\) converges in probability to \((p-1)/p\). Conditioning on either \(S_B=0\) or \(S_B\ne0\) preserves this convergence because each conditioning event has a fixed positive probability. Since \(m\) is fixed, the first two cases therefore give \(K/n\to(p-1)/p\), with total mass \(1/p\). In the last two cases \(K=n+O(m)\), so \(K/n\to1\), with total mass \((p-1)/p\). This proves the stated weak limit.

## Verification

The polynomial has nonnegative integer coefficients because each term counts a disjoint set of stabilizer labels. Directly, \(W_{m,n}^{(p)}(0)=1\) and \(W_{m,n}^{(p)}(1)=p^{m+n}\), the required identity and total number of stabilizer elements. The accompanying dependency-free checker compares the formula with exhaustive enumeration of all labels for several small prime dimensions and part sizes. These finite checks are consistency checks only; the proof above establishes the result for all stated parameters.

## Relationship to prior work

Miller, Loss, Tavernelli, Kampermann, Bruß, and Wyderka give a graph-theoretic characterization of graph-state SLDs by counting color assignments and derive explicit expressions for selected families, including complete graphs, star graphs, cycle graphs, and the Pusteblume family. Their general counting theorem applies to \(K_{m,n}\), but the inspected text does not state the closed polynomial above or the fixed-side two-atom asymptotic law. The result here is an explicit evaluation and asymptotic analysis of that general invariant for a natural bipartite interaction family; it is not a new general definition of the SLD.

## Limitations

The formula is for prime local dimension and an unweighted complete bipartite graph. The asymptotic statement keeps \(m\) fixed; it does not describe balanced growth with \(m/n\) bounded away from zero. The two-atom limit concerns the normalized support-weight distribution of stabilizer elements, not a complete characterization of entanglement under a specified noise model. A specialized formula may exist in coding-theory literature under alternative weight-enumerator terminology; the literature search did not locate one, so priority is not claimed beyond the inspected sources.

## References

1. D. Miller, D. Loss, I. Tavernelli, H. Kampermann, D. Bruß, and N. Wyderka, “Shor–Laflamme distributions of graph states and noise robustness of entanglement,” arXiv:2207.07665v1, first publicly posted 15 July 2022; published in *Journal of Physics A: Mathematical and Theoretical* 56 (2023), 335303. https://arxiv.org/abs/2207.07665. DOI: https://doi.org/10.1088/1751-8121/ace8d4.
