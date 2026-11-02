# Sharp small-population bounds for the Product-Gap facility mechanism

## Finding

For every integer \(k\ge3\), with exactly \(n=k+1\) pairwise distinct agents on the real line, the Product-Gap mechanism has worst-case utilitarian approximation ratio **\(k-\tfrac12\)**, understood as a nonattained supremum. If one of the shortest elementary gaps lies between two nonendpoint positions (an interior gap), the sharp conditional supremum improves to **\(k-1\)**.

More precisely, let \(g_j=x_{j+1}-x_j>0\) for \(1\le j\le k\), \(H=\sum_{j=1}^{k}1/g_j\), and \(\delta=\min_j g_j\). Then

\[
\operatorname{OPT}_k=\delta,\qquad
\mathbb E[\operatorname{SC}(\operatorname{PG}_k)]
=\frac{k+1+\sum_{j=1}^{k-1}\frac{\min(g_j,g_{j+1})}{\max(g_j,g_{j+1})}}{2H}.
\]

The complete law of the omitted report is

\[
\Pr(I=i)=\begin{cases}
(2Hg_1)^{-1},&i=1,\\
(2Hg_k)^{-1},&i=k+1,\\
(1/g_{i-1}+1/g_i)/(2H),&2\le i\le k.
\end{cases}
\]

## Assumptions and scope

There are exactly \(k+1\) labeled agents, \(k\ge3\), with strictly ordered and distinct true/reported positions \(x_1<\cdots<x_{k+1}\) in \(\mathbb R\). Exactly \(k\) facilities are placed at a random subset of \(k\) reports. For a selected subset \(S=\{s_1<\cdots<s_k\}\), its unnormalized Product-Gap weight is \(w(S)=\prod_{a=1}^{k-1}(x_{s_{a+1}}-x_{s_a})\). Each agent pays her distance to the *nearest* facility; social cost sums those distances. The comparator \(\operatorname{OPT}_k\) permits facilities anywhere on the real line, not merely at reports. The approximation ratio is evaluated at truthful, positive-optimum profiles; no incentive conclusion follows for \(k\ge4\). Identical-location profiles have zero optimum under the original zero-cost fallback and are not in the ratio statement.

## Proof

**1. Unrestricted optimum.** Any assignment to \(k\) facilities of \(k+1\) agents gives at least two agents the same nearest facility. By the triangle inequality, the sum of those agents' costs is at least their separation, hence at least \(\delta\). Conversely, choose a shortest adjacent pair, locate one facility at one of its endpoints, and a facility at every other agent except the other endpoint. This costs exactly \(\delta\). The argument permits arbitrary off-report facilities, proving \(\operatorname{OPT}_k=\delta\).

**2. Exact omission weights.** Put \(P=\prod_{j=1}^k g_j>0\). Omitting endpoint \(1\) leaves the selected-gap product \(P/g_1\); omitting endpoint \(k+1\) gives \(P/g_k\). Omitting interior agent \(i\) replaces adjacent gaps \(g_{i-1},g_i\) by their sum, so its selected-gap weight is

\[
w_i=P\frac{g_{i-1}+g_i}{g_{i-1}g_i}
=P(g_{i-1}^{-1}+g_i^{-1}),\quad 2\le i\le k.
\]

Each reciprocal \(1/g_j\) occurs exactly twice in the sum of all omission weights, including the endpoint terms. Hence \(Z_k=\sum_{i=1}^{k+1}w_i=2PH\), which immediately yields the stated omission probabilities.

**3. Exact expected social cost.** All selected agents pay zero. The omitted endpoint pays its adjacent gap, and an omitted interior agent \(i\) pays \(\min(g_{i-1},g_i)\). Thus

\[
\begin{aligned}
Z_k\mathbb E[\operatorname{SC}] &= P+P+\sum_{i=2}^{k}P\left(\frac1{g_{i-1}}+\frac1{g_i}\right)\min(g_{i-1},g_i)\\
&=P\left[2+\sum_{j=1}^{k-1}\left(1+\frac{\min(g_j,g_{j+1})}{\max(g_j,g_{j+1})}\right)\right].
\end{aligned}
\]

Dividing by \(2PH\) gives the formula.

**4. Sharp global bound.** Normalize \(q_j=\delta/g_j\), so \(0<q_j\le1\), and choose \(s\) with \(q_s=1\). The ratio is

\[
R=\frac{k+1+\sum_{j=1}^{k-1}\rho_j}{2\sum_{j=1}^kq_j},\quad
\rho_j=\frac{\min(q_j,q_{j+1})}{\max(q_j,q_{j+1})}.
\]

If \(s=1\) (the right-end case is symmetric), \(\rho_1=q_2\) and all remaining \(k-2\) ratios are at most \(1\). Consequently

\[
R\le\frac{2k-1+q_2}{2(1+q_2)}<k-\tfrac12.
\]

If \(2\le s\le k-1\), then \(\rho_{s-1}=q_{s-1}\), \(\rho_s=q_{s+1}\), and at most \(k-3\) others are each at most \(1\). With \(u=q_{s-1}+q_{s+1}>0\),

\[
R\le\frac{2k-2+u}{2(1+u)}<k-1<k-\tfrac12.
\]

The same interior inequality applies whenever *any* minimizer is interior, regardless of ties. Each inequality is strict because every gap is finite and positive.

**5. Both bounds are optimal as suprema.** Take \((g_1,\ldots,g_k)=(1,L,\ldots,L)\) with \(L>1\). Direct substitution gives

\[
R_{\mathrm{end}}(L)=\frac{(2k-1)L+1}{2(L+k-1)}\longrightarrow k-\tfrac12
\quad(L\to\infty).
\]

For \(k\ge3\), take \((g_1,\ldots,g_k)=(L,1,L,\ldots,L)\). Its unique shortest gap is interior; in the ratio formula the two neighboring local ratios tend to zero, the other \(k-3\) local ratios tend to one, and \(\sum_j q_j\to1\). Therefore \(R\to(2k-2)/2=k-1\). Both limits are nonattained in the domain of strictly positive finite real gaps. This establishes every assertion.

## Verification

The accompanying `verify_gap_product.py` independently enumerates all \(k\)-subsets of the \(k+1\) reports, computes their weights and nearest-facility costs with exact rational arithmetic, and compares to the closed formula. It checks every positive integer gap profile with \(2\le k\le8\) and \(1\le g_j\le4\) (87,376 profiles), the universal bound, the interior-shortest-gap refinement, and both extremal families at several finite scales. Execute `python3 verify_gap_product.py` next to this file. Output: `VERIFY_OK exact_profiles=87376 k=2..8 integer_gaps=1..4 endpoint_and_interior_asymptotic_families=checked`. The \(k=2\) computations provide a boundary sanity check; the new theorem is asserted for \(k\ge3\). Finite enumeration is not used as proof of the infinite assertions.

## Relationship to prior work

Jia [1, Sections 3–5, especially the Product-Gap definition, Theorems 1 and 3] proves the all-population sharp \(2k\) factor. Chan, Lin and Wang [2, Section 5 and Lemma 5] independently establish the same general welfare guarantee for Gap-Product. Their sharpness families use many repeated agents and do not imply sharpness for exactly \(k+1\) distinct agents. Both sources discuss the \(k=n-1\) regime via *other* randomized mechanisms, not this exact Product-Gap omission distribution or its spatial refinement. A prior small-profile result [3] already gives the corresponding \(k=2,n=3\) approximation supremum \(3/2\); the novel theorem starts at \(k=3\) and treats all larger facility counts in one sharp statement. Standard gap-product algebra underlies the derivation; that algebra by itself is not claimed to be new.

## Limitations

Only distinct-location profiles with exactly one more agent than facilities are covered. The ratio guarantee for Product-Gap does not imply strategyproofness when \(k\ge4\). The two suprema are approached but never attained by a finite strictly positive-gap profile. Published-coverage comparisons were directed at the two originating full preprints and relevant special-population literature; an independently formulated earlier identity or bound may remain unindexed. This is a theorem about the specified mechanism, not a lower bound on *all* facility mechanisms.

## References

[1] J. Jia, *Product Gap Mechanisms for Multi-Facility Location*, arXiv:2608.19633v1 (first publicly available 2026-08-20), https://arxiv.org/abs/2608.19633.

[2] H. Chan, J. Lin and C. Wang, *Randomized Strategyproof Facility Location: Two Facilities and Beyond*, arXiv:2608.22484v1 (first publicly available 2026-08-23), https://arxiv.org/abs/2608.22484.

[3] *Sharp three- and four-agent approximation ratios for distance-proportional two-facility sampling*, previous mathematical record `df6f1e6a-67c4-4ed5-92cb-490502f75905` (two-facility \(k=2\) case; bibliographic identifier internal to its deposited record).
