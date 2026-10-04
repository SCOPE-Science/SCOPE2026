# The critical logarithm is necessary for planar \(W_1\) empirical quantization
## Finding
For a probability measure \(\mu\) on \(\mathbb R^2\), let
\[
e_{N;2,1}(\mu):=\inf_{x_1,\ldots,x_N\in\mathbb R^2}W_1\!\left(\mu,\frac1N\sum_{i=1}^N\delta_{x_i}\right),
\]
and define the second-moment minimax error
\[
E_N:=\sup\left\{e_{N;2,1}(\mu):\int_{\mathbb R^2}\|x\|^2\,d\mu(x)\le1\right\}.
\]
There are absolute constants \(c,C>0\) and \(N_0\) such that, for every integer \(N\ge N_0\),
\[
c\sqrt{\frac{\log N}{N}}\le E_N\le C\sqrt{\frac{\log(1+N)}{N}}.
\]
Thus the logarithmic correction in the critical case \((d,p,q)=(2,1,2)\) has the correct minimax order: it cannot in general be removed under only a bounded second moment.

## Assumptions and scope
The quantizing measure has exactly \(N\) equal weights, with repeated quantizer locations allowed. The target measure is arbitrary on \(\mathbb R^2\) subject only to \(\int\|x\|^2d\mu\le1\). The lower-bound target may depend on \(N\), as is appropriate for the minimax quantity \(E_N\). The result does not assert a logarithmic lower bound for any one fixed measure, does not identify the sharp constant, and does not treat other critical triples \((d,p,q)\).

## Proof
The upper bound is Theorem 1.1 of Seeger specialized to \((d,p,q)=(2,1,2)\): at the critical dimension \(d=pq/(q-p)=2\), it gives
\[
e_{N;2,1}(\mu)\le C\left(\int\|x\|^2d\mu(x)\right)^{1/2}N^{-1/2}\sqrt{\log(1+N)}.
\]
It remains to prove the matching lower order.

First use an exact matching identity. For any indexed multiset \(Z=(z_1,\ldots,z_{2N})\subset\mathbb R^d\), put
\[
\mu_Z=\frac1{2N}\sum_{a=1}^{2N}\delta_{z_a}.
\]
Then
\[
e_{N;d,1}(\mu_Z)=\frac1{2N}\min_{\Pi}\sum_{\{a,b\}\in\Pi}\|z_a-z_b\|,
\]
where \(\Pi\) ranges over perfect matchings of the \(2N\) indexed atoms. For the upper inequality, choose one quantizer location on the segment joining each matched pair and split its mass equally between the pair. For the reverse inequality, scale any optimal transport plan by \(2N\). The resulting finite transportation problem has integer supplies \(2\) at the \(N\) quantizer locations and unit demands at the \(2N\) indexed target atoms. Its constraint matrix is the bipartite incidence matrix, so an optimal basic solution may be taken integral. Each quantizer therefore serves exactly two indexed target atoms. The triangle inequality says that its transport cost is at least the distance between those two atoms, and the induced pairing has cost at least the minimum perfect-matching cost.

Now fix a sufficiently large \(N\) and set
\[
K=\left\lfloor\frac{\log N}{4\log 8}\right\rfloor,
\qquad R_j=8^j,
\qquad
m_j=\left\lfloor\sqrt{\frac{N}{64KR_j^2}}\right\rfloor
\]
for \(0\le j<K\). For all sufficiently large \(N\), every \(m_j\ge2\). At scale \(j\), place \(L_j=2m_j^2\) points on the rectangular grid
\[
G_j=\left\{\left(R_j+\frac{(a+1/2)R_j}{m_j},\ R_j+\frac{(b+1/2)R_j}{2m_j}\right):0\le a<m_j,\ 0\le b<2m_j\right\}.
\]
Take one copy of every point in every \(G_j\), and fill the remaining indexed atoms up to \(2N\) with copies of the origin. This is possible because
\[
\sum_{j<K}L_j\le\frac{N}{32K}\sum_{j<K}R_j^{-2}<2N.
\]
Let \(\mu_N\) be the uniform measure on these \(2N\) indexed atoms.

Every point in \(G_j\) lies in \([R_j,2R_j]^2\), hence has squared norm at most \(8R_j^2\). Therefore
\[
\int\|x\|^2d\mu_N(x)
\le\frac4N\sum_{j<K}L_jR_j^2
\le\frac4N\sum_{j<K}\frac{N}{32K}
=\frac18.
\]
So \(\mu_N\) is admissible for \(E_N\).

The minimum separation within \(G_j\) is
\[
s_j=\frac{R_j}{2m_j}.
\]
Because consecutive radii differ by the factor \(8\), a point of \(G_j\) is also farther than \(s_j\) from the origin and from every point on every other scale. Hence an edge of any perfect matching that contains a special point from scale \(j\) has length at least \(s_j\) if its other endpoint is the origin, and an edge joining special points from scales \(j\) and \(k\) has length at least \(\max\{s_j,s_k\}\ge(s_j+s_k)/2\). Summing edgewise gives
\[
\min_{\Pi}\sum_{\{a,b\}\in\Pi}\|z_a-z_b\|
\ge\frac12\sum_{j<K}L_js_j
=\frac12\sum_{j<K}m_jR_j.
\]
For sufficiently large \(N\), the quantities inside the floors are at least \(2\), and therefore
\[
m_jR_j\ge\frac1{16}\sqrt{\frac NK}.
\]
Consequently the minimum matching cost is at least \(\sqrt{NK}/32\), and the matching identity yields
\[
e_{N;2,1}(\mu_N)\ge\frac1{64}\sqrt{\frac KN}.
\]
For sufficiently large \(N\),
\[
K\ge\frac{\log N}{8\log8},
\]
so
\[
e_{N;2,1}(\mu_N)\ge\frac1{64\sqrt{8\log8}}\sqrt{\frac{\log N}{N}}.
\]
This proves the lower bound and completes the argument.

## Verification
The proof is analytic. The exact matching identity was checked independently against the transportation formulation, including repeated target locations. The multiscale inequalities use only the displayed grid geometry, the factor-eight separation of scales, and elementary floor estimates. A standalone verifier included with this record checks the construction inequalities over representative large values of \(N\); those finite checks are supplementary and are not used as a substitute for the proof.

## Relationship to prior work
Seeger proves the critical upper bound and explicitly notes that when \(d_*=pq/(q-p)>1\), deciding whether the logarithmic term is necessary requires nontrivial lower bounds. The theorem above answers that question for the first planar case \((d,p,q)=(2,1,2)\).

Quattrocchi studies asymptotics for optimal empirical quantization of fixed measures and gives high-resolution results under stronger moment hypotheses in the regime \(p<d\). Those results do not imply the uniform critical second-moment lower bound here: at \((d,p)=(2,1)\), the natural high-resolution threshold is the second moment itself, whereas the present construction is a minimax family depending on \(N\). Earlier deterministic-empirical approximation results of Chevallier and one-dimensional work of Bencheikh and Jourdain provide upper bounds or different-dimensional analyses, not this critical planar lower bound.

## Limitations
Only the minimax order at \((d,p,q)=(2,1,2)\) is proved. No sharp leading constant is claimed. The construction is singular and depends on \(N\), so it does not establish a logarithmic obstruction for a single fixed absolutely continuous measure. The literature comparison found no implication-equivalent published result, but an older matching or quantization lower bound under different terminology remains a residual originality risk.

## References
1. Benjamin Seeger, *Error estimates for deterministic empirical approximations of probability measures*, arXiv:2510.03451v1, first public October 3, 2025; Electron. Commun. Probab. 31 (2026), DOI:10.1214/26-ECP775.
2. Filippo Quattrocchi, *Asymptotics for Optimal Empirical Quantization of Measures*, arXiv:2408.12924v1, August 23, 2024.
3. Julien Chevallier, *Uniform decomposition of probability measures: quantization, clustering and rate of convergence*, J. Appl. Probab. 55 (2018), 1037–1045.
4. O. Bencheikh and B. Jourdain, *Approximation rate in Wasserstein distance of probability measures on the real line by deterministic empirical measures*, J. Approx. Theory 274 (2022), 105684.
