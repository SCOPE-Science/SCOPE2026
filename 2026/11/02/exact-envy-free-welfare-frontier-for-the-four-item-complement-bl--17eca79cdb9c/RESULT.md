# Exact envy-free welfare frontier for the four-item complement-block instance

## Finding

Consider the four-item-block binary complement valuation family used as the welfare obstruction in Pyne, Viswanathan, Yang and Zick (2026), Theorem 4.7. For every number of agents \(n\ge2\), block count \(t\ge1\), and integer \(\ell\ge1\), the exact maximum utilitarian welfare under complete allocations is

\[
\begin{aligned}
W_{\mathrm{EF}}(n,t)&=W_{\mathrm{EFX}}(n,t)=t+\left\lfloor\frac{t}{n}\right\rfloor,\\
W_{\mathrm{EF}\text{-}\ell}(n,t)&=t+\min\left\{t,\left\lfloor\frac{t+(n-1)\ell}{n}\right\rfloor\right\},\\
W_{\mathrm{unconstrained}}(n,t)&=2t.
\end{aligned}
\]

EF means ordinary envy-freeness, EFX means envy-freeness after deletion of **every** single good from the envied bundle (including goods of zero marginal value), and EF-\(\ell\) means that up to \(\ell\) goods can be deleted from that bundle to eliminate each directed envy. In particular, \(W_{\mathrm{EF1}}=t+\lceil t/n\rceil\). Hence the exact welfare gap between EF1 and even exact EF is one whenever \(n\nmid t\), and zero otherwise.

## Assumptions and scope

There are \(n\) agents and \(4t\) distinct indivisible goods, grouped into \(t\) blocks \(\{a_j,b_j,a'_j,b'_j\}\) for \(1\le j\le t\). All goods are allocated to exactly one agent (no unassigned goods). Agent \(1\) receives one utility unit from each fully contained pair \(\{a_j,a'_j\}\) and \(\{b_j,b'_j\}\), so
\[
v_1(S)=\sum_{j=1}^{t}\bigl(\mathbf1_{\{a_j,a'_j\}\subseteq S}+\mathbf1_{\{b_j,b'_j\}\subseteq S}\bigr).
\]
Each other agent \(i\in\{2,\ldots,n\}\) receives one unit from each fully contained pair \(\{a_j,b_j\}\):
\[
v_i(S)=\sum_{j=1}^{t}\mathbf1_{\{a_j,b_j\}\subseteq S}.
\]
Thus each valuation is additive over its own disjoint complement pairs, but not additive over physical goods. The exact instance is a binary purely complementary SPOC-\(2\) family. No claim is made for arbitrary SPOC valuations, arbitrary item-complement hypergraphs, unequal block weights, or variable-length complements.

## Proof

**Block upper bound.** Call block \(j\) *whole* if all four of its goods are assigned to agent \(1\), and let \(h\) count whole blocks. A whole block contributes exactly two units to utilitarian welfare. Every other block contributes at most one: if another agent completes the horizontal pair \(\{a_j,b_j\}\), no vertical pair can be completed by agent \(1\); otherwise agent \(1\) can complete at most one vertical pair unless the block is whole. Thus every allocation has welfare at most \(t+h\). Giving every block to agent \(1\) attains \(2t\), proving the unrestricted optimum.

**EF-\(\ell\) upper bound.** Every other agent \(i\ge2\) values agent \(1\)'s bundle at least \(h\), on account of the horizontal pairs inside whole blocks. Deleting up to \(\ell\) physical goods destroys at most \(\ell\) disjoint horizontal pairs, so EF-\(\ell\) requires \(v_i(X_i)\ge h-\ell\). At most \(t-h\) horizontal pairs can be contained in the bundles of agents \(2,\ldots,n\), since they cannot use goods from whole blocks, so
\[
(n-1)(h-\ell)\le\sum_{i=2}^{n}v_i(X_i)\le t-h.
\]
Consequently \(h\le\min\{t,\lfloor(t+(n-1)\ell)/n\rfloor\}\). Combining with the block bound gives the asserted EF-\(\ell\) upper bound.

**Attaining the EF-\(\ell\) bound.** Set \(h=\min\{t,\lfloor(t+(n-1)\ell)/n\rfloor\}\). Give \(h\) entire blocks to agent \(1\). Of the other \(t-h\) blocks, give each horizontal pair \(\{a_j,b_j\}\) to one of agents \(2,\ldots,n\), distributing the pairs as evenly as possible. Give all residual \(\{a'_j,b'_j\}\) to agent \(1\). Let \(q_i\) be the number of horizontal pairs held by agent \(i\ge2\). Their counts differ by at most one and each satisfies \(q_i\ge\max\{0,h-\ell\}\), by the choice of \(h\). Other agents see at most \(h\) horizontal pairs in agent \(1\)'s bundle and can destroy \(\min(h,\ell)\) of them with \(\ell\) deletions; agent \(1\) sees no completed vertical pair in another agent's horizontal-only bundle; and an agent with fewer horizontal pairs can destroy the surplus of at most one pair in another agent's bundle using one deletion. Therefore the complete allocation is EF-\(\ell\) and has welfare \(2h+(t-h)=t+h\), attaining the upper bound. The construction remains valid when \(h=t\).

**EFX upper bound.** If \(h\ge1\), select any primed good (say \(a'_j\)) from a whole block in agent \(1\)'s bundle. Deleting that good changes none of the \(h\) completed horizontal pairs viewed by any agent \(i\ge2\). EFX forces \(v_i(X_i)\ge h\) for each of the \(n-1\) other agents. Since their total horizontal utility is at most \(t-h\), we obtain \(nh\le t\). For \(h=0\) the inequality is immediate. Thus \(W_{\mathrm{EFX}}\le t+\lfloor t/n\rfloor\). Ordinary EF is stronger, so the same upper bound applies to EF.

**Attaining the EF bound.** Write \(t=nh+r\), where \(h=\lfloor t/n\rfloor\) and \(0\le r<n\). Allocate \(h\) entire blocks to agent \(1\). Give \(h\) horizontal pairs \(\{a_j,b_j\}\) to each of agents \(2,\ldots,n\), sending the corresponding primed goods to agent \(1\). In the remaining \(r\) blocks give \(\{a_j,a'_j\}\) to agent \(1\) and \(\{b_j,b'_j\}\) to agent \(2\). Agent \(1\)'s own utility is \(2h+r\) and its value for any other's bundle is at most \(r\); every other agent's own utility is \(h\), and every other agent values every other bundle, including agent \(1\)'s, at exactly \(h\). Thus this complete allocation is ordinary envy-free and has welfare \((2h+r)+(n-1)h=t+h\). Because EF implies EFX, both optima equal the upper bound. In the case \(n=2\), the allocations and inequalities remain unchanged. Finally \(W_{\mathrm{EF1}}=t+\lceil t/n\rceil\) follows by substituting \(\ell=1\) in the general EF-\(\ell\) formula.

## Verification

A standalone exhaustive checker, `verify_spoc_frontier.cpp`, reconstructs every complete assignment of the \(4t\) labeled goods to \(n\) agents and directly evaluates all pair-complement utilities, EF, EFX (by deleting every good in every comparison), and EF-\(\ell\) for \(\ell=1,2,3\). All \(1,722,355\) complete assignments in the test ranges \(n=2,\ 1\le t\le5\); \(n=3,\ 1\le t\le3\); and \(n=4,\ 1\le t\le2\) were checked. The computed maxima agree with every formula. Compile using `c++ -std=c++17 -O2 verify_spoc_frontier.cpp -o verifier`, then execute `./verifier`. The infinite-parameter proof is the argument above, not an inference from finite tests.

## Relationship to prior work

Pyne, Viswanathan, Yang and Zick (arXiv:2610.15801, Theorem 4.7) introduce exactly these four-item blocks as an asymptotic welfare obstruction for EF-\(\ell\). Their full-text argument gives an asymptotic existence family with welfare ratio no greater than \(1/2+\varepsilon\), but does not state the exact finite-\(n,t,\ell\) optima, an optimal ordinary EF construction, or the one-unit separation between EF and EF1. The present theorem analyzes only their explicitly defined family; it does not strengthen their general lower-bound theorem to arbitrary valuations. Babaioff, Ezra and Feige (2021) concern matroid-rank/dichotomous-marginal valuations and cannot directly imply this statement because complementary physical goods create non-submodular marginals.

## Limitations

The finding gives the precise welfare frontier of one canonical infinite family, not a global optimal fairness guarantee for the full SPOC class. The result uses all goods being assignable and identical utility weight for each completed pair. Its new finite-parameter formulas might be independently derivable from the original block construction, so publication priority is not independently certified. The exhaustive checker covers only the specified finite ranges; the proof covers every integer \(n\ge2\), \(t\ge1\), \(\ell\ge1\). No independent scientific validation has been performed.

## References

1. S. Pyne, V. Viswanathan, W. Yang, Y. Zick, *Fair Allocation with Dichotomous Preferences over Item Complements*, arXiv:2610.15801v1 (first publicly submitted 2026-10-11), especially Section 2 and Theorem 4.7. https://arxiv.org/html/2610.15801v1
2. M. Babaioff, T. Ezra, U. Feige, *Fair and Truthful Mechanisms for Dichotomous Valuations*, AAAI 2021, DOI:10.1609/aaai.v35i6.16647.
