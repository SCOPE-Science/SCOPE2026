# A global matching-cut sharpening of the vector-chirality QFI witness
## Finding
For every even integer \(N\ge 4\), every \(1\le k\le N\), and every \(k\)-producible state \(\rho^{(k)}\) of a periodic spin-\(1/2\) chain, define the total nearest-neighbour vector chirality
\[
K_{\mathrm{tot}}=\sum_{i=1}^N\kappa_i,\qquad
\kappa_i=S_i^xS_{i+1}^y-S_i^yS_{i+1}^x.
\]
Write \(N=qk+s\) with \(0\le s<k\). Then
\[
F_Q[\rho^{(k)},K_{\mathrm{tot}}]
\le qk^2+s^2+N-\max\{0,\,2k-N\}.
\]
For \(k\le N/2\) this agrees with the finite-size bound in arXiv:2609.39258v1. For \(k>N/2\), where \(q=1\) and \(s=N-k\), it gives the strict improvement
\[
F_Q[\rho^{(k)},K_{\mathrm{tot}}]
\le k^2+(N-k)^2+2(N-k).
\]
The subtraction from the published numerator is \(2k-N\). At \(k=N\) the result becomes \(F_Q\le N^2\).

## Assumptions and scope
The chain has even \(N\ge4\), periodic boundary conditions, and spin \(1/2\) at each site. A pure \(k\)-producible state is a tensor product over blocks \(u\) of sizes \(n_u\le k\); mixed \(k\)-producible states are convex mixtures of such states, with partitions allowed to vary across mixture components. The QFI convention is the one used in arXiv:2609.39258v1, so for a pure state \(F_Q=4\operatorname{Var}\).

The proof uses the source's decomposition
\[
K_{\mathrm{tot}}=K_{\mathrm{odd}}+K_{\mathrm{even}},
\]
where each component is a complete matching of \(N/2\) disjoint nearest-neighbour bonds.

## Proof
Fix a pure \(k\)-producible state and one admissible block partition \(\Gamma\). Consider either complete matching \(\mathcal M\). For a block \(u\), let \(r_u\) be the number of matching edges internal to \(u\), and \(c_u\) the number of matching edges with exactly one endpoint in \(u\). Since every site is incident to exactly one matching edge,
\[
n_u=2r_u+c_u.
\]
The block-allocation calculation in arXiv:2609.39258v1 gives, before its final relaxation,
\[
A_u=\frac{n_u^2+c_u}{16},
\qquad
\operatorname{Var}(K_{\mathcal M})\le \sum_u A_u.
\]

Let \(C_{\mathcal M}\) be the number of matching edges crossing between different blocks. Every crossing edge contributes one incidence to each endpoint block, hence
\[
\sum_u c_u=2C_{\mathcal M}.
\]
Let \(m=\max_u n_u\). If \(m\le N/2\), then trivially \(C_{\mathcal M}\le N/2\), so \(\sum_u c_u\le N\). If \(m>N/2\), choose a largest block. Every crossing edge has at least one endpoint outside that block, because an edge with both endpoints in it is internal. Distinct matching edges have disjoint endpoints, so
\[
C_{\mathcal M}\le N-m,
\qquad
\sum_u c_u\le2(N-m).
\]
Therefore
\[
16\,\operatorname{Var}(K_{\mathcal M})
\le
\sum_u n_u^2+
\begin{cases}
N,&m\le N/2,\\
2(N-m),&m>N/2.
\end{cases}
\]

When \(k\le N/2\), the usual convex partition maximization gives
\[
\sum_u n_u^2\le qk^2+s^2,
\]
and hence the published one-matching bound.

Now assume \(k>N/2\). Then \(q=1\) and \(s=N-k\). If \(m\le N/2\), the largest possible sum of squares is \(N^2/2\), so
\[
16\,\operatorname{Var}(K_{\mathcal M})\le \frac{N^2}{2}+N.
\]
If \(m>N/2\), the remaining block sizes sum to \(N-m\), so their squared sum is at most \((N-m)^2\). Hence
\[
16\,\operatorname{Var}(K_{\mathcal M})
\le f(m):=m^2+(N-m)^2+2(N-m).
\]
For integer \(m\ge N/2+1\), \(f(m)\) is increasing. Thus \(f(m)\le f(k)\). Writing \(d=k-N/2\ge1\),
\[
f(k)-\left(\frac{N^2}{2}+N\right)=2d(d-1)\ge0.
\]
Both cases therefore give
\[
\operatorname{Var}(K_{\mathcal M})
\le\frac{k^2+(N-k)^2+2(N-k)}{16}.
\]
For pure states this implies
\[
F_Q[\rho^{(k)},K_{\mathcal M}]
\le\frac{k^2+(N-k)^2+2(N-k)}4.
\]
The source's QFI triangle inequality for generators,
\[
\sqrt{F_Q[\rho,A+B]}
\le\sqrt{F_Q[\rho,A]}+\sqrt{F_Q[\rho,B]},
\]
applied to the two matchings gives
\[
F_Q[\rho^{(k)},K_{\mathrm{tot}}]
\le k^2+(N-k)^2+2(N-k).
\]
Convexity of the QFI extends the same bound to mixed \(k\)-producible states. Combining the two \(k\)-regimes yields
\[
F_Q[\rho^{(k)},K_{\mathrm{tot}}]
\le qk^2+s^2+N-\max\{0,2k-N\}.
\]

## Verification
The proof is analytic and does not rely on finite enumeration. The accompanying script `artifacts/verify.py` independently enumerates all integer block-size partitions for every even \(N\) from \(4\) through \(30\). It checks that the maximized tightened combinatorial relaxation
\[
\sum_u n_u^2+
\begin{cases}
N,&m\le N/2,\\
2(N-m),&m>N/2
\end{cases}
\]
equals the claimed numerator for every \(k\) in that finite test range. It also checks strict improvement exactly when \(k>N/2\) and the endpoint value \(N^2\) at \(k=N\). These finite checks corroborate but do not replace the proof above.

## Relationship to prior work
Shimokawa, arXiv:2609.39258v1, proves the vector-chirality QFI witness for even periodic spin-\(1/2\) chains. Its exact block allocation is \(A_u=(n_u^2+c_u)/16\), after which it uses the separate inequalities \(c_u\le n_u\), sums to \(\sum_u n_u=N\), and obtains the finite-size numerator \(qk^2+s^2+N\). The present result retains the same local variance and covariance bounds but replaces that last incidence relaxation by a global complete-matching cut count. The anchor also explicitly notes that its final odd/even recombination need not be tight; the present sharpening is different, because it improves each matching bound before recombination.

Hyllus et al., arXiv:1006.4366 and Phys. Rev. A 85, 022321 (2012), establish the standard \(qk^2+s^2\) bound for \(k\)-producible states under linear one-site generators. That result does not cover the two-site vector-chirality generator or its cross-block matching incidences.

## Limitations
No claim is made that the displayed bound is the exact \(k\)-producible maximum. The local covariance inequalities inherited from the anchor may be loose, and the final triangle inequality still optimizes odd and even matchings separately. The argument is specific to even periodic spin-\(1/2\) chains and to the total nearest-neighbour vector-chirality generator above. The improvement is strict only for \(k>N/2\).

## References
1. T. Shimokawa, *Multipartite entanglement hidden in vector-chiral correlations of spin-1/2 chains*, arXiv:2609.39258v1 (2026).
2. P. Hyllus et al., *Fisher information and multiparticle entanglement*, arXiv:1006.4366; Phys. Rev. A 85, 022321 (2012), DOI:10.1103/PhysRevA.85.022321.
