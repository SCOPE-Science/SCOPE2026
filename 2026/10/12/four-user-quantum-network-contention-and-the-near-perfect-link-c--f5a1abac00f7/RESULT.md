# Four-user quantum-network contention and the near-perfect-link crossover

## Finding

The smallest nontrivial random multi-session chain has an exact finite-size transport-capacity law, a strictly positive contention correction, and a sharp scaling crossover near perfect elementary links.

For an integer \(N\ge4\), write \(\mathcal C_N(p)\) for the **network-wide**, not per-session, expected one-slot perfect-output entanglement transport on the chain specified below. With \(0\le p\le1\), define
\[
T_s=\sum_{\substack{a,b,c\ge1\\a+b+c=s}}\bigl(\min\{a,c\}+2b\bigr),\qquad s\ge3.
\]
Then the following identities are exact for every \(N\ge4\):
\[
\boxed{\frac{\mathcal C_N(p)}{a_N}=\frac{4}{N(N-1)}\sum_{h=1}^{N-1}(N-h)h p^h-\frac{1}{3\binom N4}\sum_{s=3}^{N-1}(N-s)T_s p^s.}
\]
The second term, denoted \(\Delta_N(p)/a_N\), is the **exact loss due to competition between the two requested paths**. It is strictly positive for \(p>0\). Its coefficients have the explicit parity formulas
\[
T_{2m}=2\binom{2m}{3}+\frac{m(m-1)(4m+1)}6,\qquad m\ge2,
\]
\[
T_{2m+1}=2\binom{2m+1}{3}+\frac{m(m+1)(4m-1)}6,\qquad m\ge1.
\]
For every fixed \(0<p<1\), the sharp contention-loss asymptotic is
\[
\boxed{\lim_{N\to\infty}\frac{N^3\Delta_N(p)}{a_N}=\frac{8p^3(3+2p)}{(1-p)^4(1+p)}.}
\]
In particular \(\mathcal C_N(p)\sim4a_Np/[N(1-p)^2]\), but the exact competition is two orders smaller in \(N\) than the principal capacity term.

For each \(\lambda\ge0\), take near-perfect link probabilities \(p_N=e^{-\lambda/N}\) (including the deterministic endpoint \(\lambda=0\)). The critical scaling limit exists:
\[
\boxed{\lim_{N\to\infty}\frac{\mathcal C_N(p_N)}{a_N N}=\Phi(\lambda):=\int_0^1u(1-u)\left(4-\frac{10}{3}u^2\right)e^{-\lambda u}\,du.}
\]
The function \(\Phi\) is strictly decreasing on \([0,\infty)\), with \(\Phi(0)=1/2\), \(\Phi(\lambda)>0\), and \(\Phi(\lambda)\sim4/\lambda^2\) as \(\lambda\to\infty\). Hence fixed imperfect links and links with failure probability of order \(1/N\) belong to distinct capacity regimes.

## Assumptions and scope

There are \(N\) nodes labeled \(0,\ldots,N-1\) in a line with physical spacing \(a_N>0\). Each of the \(N-1\) edges independently supplies exactly one ideal Bell pair with probability \(p\) in a single activation slot and supplies none otherwise. Four distinct active nodes are sampled uniformly and then paired into two unordered, endpoint-disjoint communication sessions by a uniformly random perfect matching. The demand and all successful edges are announced to the allowed adaptive local-operations-and-classical-communication strategy. Ideal local swapping and classical communication are allowed without additional slot costs. Each delivered, counted output must be a perfect Bell pair, meaning Bell fidelity exactly one. Transport equals the sum of hop distances times \(a_N\) over the delivered pairs. Only this single slot is used; no interslot aggregation, distillation of imperfect pairs, fairness requirement, or noisy swap is present. These are the perfect-output single-slot resource-layer assumptions of [1], with one link opportunity per edge and exactly four active users.

The assertions concern the supremum over all such admissible strategies, not the success probability of a fixed preselected routing schedule. The endpoint case \(p=1\) is included by direct deterministic interpretation.

## Proof

**1. Quantum cut converse and attainability.** Across any edge cut, the supplied pure resource has Schmidt rank one if the link fails and rank two if it succeeds. Local operations and classical communication cannot increase Schmidt rank in any conditional branch. Two simultaneously delivered perfect Bell pairs crossing a cut would have Schmidt rank four across that cut, which is impossible with one elementary Bell pair. Conversely, whenever a requested path has all its edges open, ideal Bell swaps along it deliver one perfect pair. Therefore, for each realized matching and open-edge pattern, the optimal transport is the maximum total length of simultaneously available paths with disjoint edge sets, multiplied by \(a_N\). This independently recovers the two-session case of the interval-allocation principle in [1, Appendix C, Eq. (41)].

**2. Conditional expectation for two demands.** Put the four selected positions in increasing order \(x_1<x_2<x_3<x_4\), and define the positive gaps \(g_1=x_2-x_1\), \(g_2=x_3-x_2\), \(g_3=x_4-x_3\) and span \(s=g_1+g_2+g_3\). There are exactly three equally likely matchings. The matching \((x_1,x_2),(x_3,x_4)\) has disjoint paths and no contention. The crossing matching \((x_1,x_3),(x_2,x_4)\) loses \((g_2+\min\{g_1,g_3\})p^s\) relative to the sum of the individual expected path transports: both paths are available simultaneously precisely when all \(s\) edges are open, and then only the longer path can be used. For the nested matching \((x_1,x_4),(x_2,x_3)\), the corresponding loss is \(g_2p^s\). Averaging over matchings gives the conditional contention loss \(\bigl(\min\{g_1,g_3\}+2g_2\bigr)p^s/3\).

**3. Exact averaging.** Any specified unordered node pair appears as a demanded session with probability \(4/[N(N-1)]\). There are \(N-h\) node pairs separated by \(h\) hops, and such a path is available with probability \(p^h\). This yields the first term of the capacity identity, the capacity without competition. Each positive gap triple with sum \(s\) has exactly \(N-s\) possible translations along the chain. Uniform selection from \(\binom N4\) four-subsets and the preceding conditional loss yield the second term exactly. For the coefficients, the sum of the \(2g_2\) terms over positive compositions is \(2\binom s3\), while
\[
\sum_{\substack{g_1,g_2,g_3\ge1\\g_1+g_2+g_3=s}}\min\{g_1,g_3\}=\sum_{k=1}^{\lfloor(s-1)/2\rfloor}\binom{s-2k+1}{2}.
\]
Summing the odd or even quadratic sequences establishes the two parity formulas.

**4. Fixed-link sharp loss.** For \(0<p<1\), exponential decay makes the series of polynomially growing coefficients absolutely convergent. Dominated convergence, using \(3\binom N4\sim N^4/8\), gives
\[
\lim_{N\to\infty}\frac{N^3\Delta_N(p)}{a_N}=8\sum_{s\ge3}T_sp^s.
\]
Reversing the positive sums and writing \(A=\sum_{j\ge1}p^j=p/(1-p)\), \(B=\sum_{j\ge1}jp^j=p/(1-p)^2\), and \(E=\sum_{a,c\ge1}\min\{a,c\}p^{a+c}=p^2/[(1-p)^2(1-p^2)]\), the series is \(AE+2A^2B=p^3(3+2p)/[(1-p)^4(1+p)]\). The baseline series gives the stated leading \(4a_Np/[N(1-p)^2]\) term.

**5. Near-perfect-link crossover.** Set \(p_N=e^{-\lambda/N}\). In the first exact finite sum, let \(u=h/N\). Riemann-sum convergence after division by \(a_NN\) gives \(4\int_0^1u(1-u)e^{-\lambda u}\,du\). The explicit parity formulas imply \(T_s=(5/12)s^3+O(s^2)\), uniformly in integers \(s\ge3\). The loss sum therefore converges, on the same normalization, to \((10/3)\int_0^1u^3(1-u)e^{-\lambda u}\,du\). Subtraction proves the formula for \(\Phi\). Its integrand is \(u(1-u)(4-10u^2/3)>0\) for \(0<u<1\), so differentiating under the integral shows strict decrease. Elementary polynomial integration gives \(\Phi(0)=1/2\). Rescaling \(v=\lambda u\) and dominated convergence gives \(\lambda^2\Phi(\lambda)\to4\), completing the proof.

## Verification

The standalone standard-library program `verify.py` checks the coefficient count against an independent positive-composition enumeration, compares the exact closed formula against exhaustive enumeration of all four-node selections, all three pairings, and every open-edge mask for \(4\le N\le8\) at five rational probabilities, and checks the derived fixed-link and near-perfect asymptotic constants against larger finite sizes. It prints `VERIFY_OK 56` on success. The exhaustive finite checks are not the proof for arbitrary \(N\); the preceding combinatorial identities and convergence arguments supply that proof.

For illustration, at \(N=4\) and \(p=1/2\), the two isolated-path benchmark is \(23/24\), the exact contention loss is \(1/8\), and the achievable optimum is \(5/6\), in units of \(a_N\).

## Relationship to prior work

Kim and Popovski [1] formulate the distance-weighted quantum-network resource model, establish a general interval integer-allocation formula for perfect-output chain transport (Appendix C, Eq. (41)), and prove fixed-\(p\) scaling for arbitrary even user count. Their general formula is the foundational cut characterization from which the special four-user model can be analyzed; it is not claimed here as new. The distinct contribution is the closed all-\(N,p\) averaging over the first genuinely competing random matching, its exact and strictly positive contention deficit, its sharp \(N^{-3}\) fixed-link coefficient, and its near-perfect-link \(N(1-p)\)-scale crossover. The fixed-\(p\) limit in [1] does not itself furnish the varying-\(p\) crossover law.

Pant and collaborators [2] study simultaneous entanglement flows on a two-dimensional repeater grid with different routing and local-state-information assumptions. Halder and collaborators [3] consider optimization and resource allocation with memory and fidelity constraints. Neither of these studied passages supplies the random-four-user exact expectation or the crossover in this model. The mathematical identities are compatible with general interval packing and Bernoulli network reliability methods; equivalence to an earlier unindexed formula is a residual priority risk.

## Limitations

This exact capacity is for perfect Bell outputs in the single-slot, single-link-opportunity ideal resource layer; the formula is **not** asserted at a relaxed fidelity threshold such as \(0.95\), for longer aggregation windows, for shared endpoint requests, for non-chain topologies, or for finite-speed/noisy physical-layer protocols. The result does not establish novelty by database-search absence alone. Some published general optimization formulas can be specialized algorithmically to the same finite model; the new mathematical content is the explicit averaging and limiting analysis. Finite enumerations verify examples but cannot certify a general infinite statement independently.

## References

[1] J. Kim and P. Popovski, *Scaling Laws of Quantum Networks: An Entanglement Transport Framework*, arXiv:2609.39690v1 (first public version 2026-09-30), especially Sections 2 and 4 and Appendix C. https://arxiv.org/pdf/2609.39690

[2] M. Pant et al., *Routing entanglement in the quantum internet*, npj Quantum Information **5**, 25 (2019), DOI:10.1038/s41534-019-0139-x. https://www.nature.com/articles/s41534-019-0139-x

[3] J. Halder et al., *Optimal routing and end-to-end entanglement distribution in quantum networks*, Scientific Reports **14**, 19262 (2024), DOI:10.1038/s41598-024-70114-1. https://www.nature.com/articles/s41598-024-70114-1
