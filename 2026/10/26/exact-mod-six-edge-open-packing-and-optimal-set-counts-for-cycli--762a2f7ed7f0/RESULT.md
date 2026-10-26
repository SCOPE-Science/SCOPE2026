# Exact mod-six edge open packing and optimal-set counts for cyclic prisms

## Finding

For the prism graph \(P_n=C_n\square K_2\), with \(n\ge7\), let \(\rho_e^o(P_n)\) be the maximum cardinality of an edge open packing and let \(M_n\) be the number of distinct edge subsets attaining that cardinality. Then

\[
\rho_e^o(P_n)=\begin{cases}n,&n\equiv0\pmod6,\\n-1,&n\not\equiv0\pmod6,\end{cases}
\qquad
M_n=\begin{cases}6,&n\equiv0\pmod6,\\4n,&n\equiv3,5\pmod6,\\2n,&n\equiv1,2,4\pmod6.\end{cases}
\]

The graph's \(3n\) edges are distinguished. The result simultaneously classifies which cyclic prisms achieve the standard cubic-graph upper bound and enumerates **all** maximum packings. It does not claim a new general upper bound.

## Assumptions and scope

Graphs are finite, simple and undirected. An *edge open packing* is an edge subset \(Q\) such that for any distinct \(e,f\in Q\), there is **no third edge** \(g\in E(P_n)\setminus\{e,f\}\) joining an endpoint of \(e\) to an endpoint of \(f\). Edges of \(Q\) may be incident; requiring a matching would define a different invariant. All indices below lie in the fixed cyclic group \(\mathbb Z/n\mathbb Z\); the hypothesis \(n\ge7\) ensures the radius-two neighborhoods used below do not overlap anomalously.

Put \(t_i=((i,0),(i+1,0))\), \(b_i=((i,1),(i+1,1))\), and \(r_i=((i,0),(i,1))\). A packing selects, in each column \(i\), the bitmask \(p_i\) encoding \(t_i,b_i,r_i\) by bits \(1,2,4\), respectively; \(|p_i|\) denotes the number of its set bits. Because \(t_i\) and \(b_i\) have \(r_i\) as a common third edge, the only possible local masks are

\[
\mathcal P=\{0,1,2,4,5,6\}.
\]

## Proof

**1. Exact local condition.** For \(a,b\in\mathcal P\), define two symmetric-in-edges but directionally encoded forbidden predicates

\[
\begin{aligned}
F_1(a,b)&=[(a\mathbin{\&}4\ne0\ \land\ b\ne0)\ \lor\ (a\mathbin{\&}1\ne0\ \land\ b\mathbin{\&}2\ne0)\ \lor\ (a\mathbin{\&}2\ne0\ \land\ b\mathbin{\&}1\ne0)],\\
F_2(a,b)&=[(a\mathbin{\&}1\ne0\ \land\ b\mathbin{\&}5\ne0)\ \lor\ (a\mathbin{\&}2\ne0\ \land\ b\mathbin{\&}6\ne0)].
\end{aligned}
\]

Here \(\&\) is bitwise AND and square brackets denote a truth value. Directly inspect the possible third edges between two selected edges: within one column the forbidden pair is top and bottom; for columns \(i,i+1\) the exclusion is \(F_1(p_i,p_{i+1})\); for \(i,i+2\) it is \(F_2(p_i,p_{i+2})\); at larger cyclic separation there is no third edge. The check covers the reversed offsets by using the predecessor's mask as the first argument. Therefore \((p_i)_{i\in\mathbb Z/n\mathbb Z}\) represents an edge open packing **if and only if**

\[
F_1(p_i,p_{i+1})=F_2(p_i,p_{i+2})=0
\quad\text{for every }i\in\mathbb Z/n\mathbb Z.
\]

**2. Cyclic transfer.** Construct the 17-state set

\[
\mathcal S=\{(a,b)\in\mathcal P^2:F_1(a,b)=0\}.
\]

There is a directed transition \((a,b)\to(b,c)\) precisely when \(F_1(b,c)=F_2(a,c)=0\). It has cardinality weight \(|c|\). The graph has exactly 37 such transitions. A cyclic sequence of \(n\) transitions, beginning and ending at a state with the same fixed column indices, corresponds bijectively to one feasible edge subset on the labeled prism; the total weight is the packing cardinality. In particular, taking the trace, rather than a path count with unfixed endpoints, imposes every wrap-around constraint exactly once.

**3. Nonnegative deficiency and finite identities.** Define an integer potential \(h:\mathcal S\to\{0,-1\}\) by

\[
h(a,b)=-1\quad\text{for }(a,b)\in\{(0,5),(0,6),(1,5),(2,6)\},
\qquad h(a,b)=0\text{ otherwise}.
\]

Give the transition \((a,b)\to(b,c)\) the adjusted deficiency

\[
\delta=1-|c|+h(a,b)-h(b,c).
\]

Direct inspection of all 37 explicitly specified transitions gives \(\delta\in\{0,1\}\) in every case. Because the potential telescopes around any closed walk, a length-\(n\) cyclic packing has total deficiency exactly \(n-|Q|\). Let \(B_0,B_1\) be the integer \(17\times17\) adjacency matrices retaining transitions of deficiency zero and one, respectively. They have 24 and 13 unit entries. The following two finite, *integer-exact* calculations are part of the proof and are reproducible by the accompanying `verify.py`:

\[
B_0^8=B_0^2,\qquad
\bigl(\operatorname{tr}(B_1B_0^{j-1})\bigr)_{j=1}^{8}=(1,1,4,2,4,6,2,2).
\]

For clarity, the zero-deficiency directed graph has exactly one simple directed cycle, namely

\[
(0,1)\to(1,5)\to(5,0)\to(0,2)\to(2,6)\to(6,0)\to(0,1).
\]

The finite checker constructs all matrices from the Boolean predicates, multiplies integer matrices, and exhaustively identifies simple cycles, without floating-point computations or a pre-stored result table. Thus every closed length-\(n\) zero-deficiency walk consists of repetitions of the displayed six-cycle: there are precisely six such indexed walks when \(6\mid n\), and none otherwise. Since all deficiencies are nonnegative, \(|Q|\le n\), with equality in precisely those cases.

**4. Exactly one unit of deficiency otherwise.** Let

\[
a_n=\operatorname{tr}(B_1B_0^{n-1}).
\]

The matrix identity implies \(a_{n+6}=a_n\) whenever \(n\ge3\). From the exact trace values for \(3\le n\le8\), it follows that for every \(n\ge7\):

\[
a_n=\begin{cases}
6,&n\equiv0\pmod6,\\
4,&n\equiv3,5\pmod6,\\
2,&n\equiv1,2,4\pmod6.
\end{cases}
\]

Every length-\(n\) closed walk with total deficiency one has exactly one unit-deficiency transition. There are exactly \(n a_n\) such indexed walks: choose the position of that transition, and count the other \(n-1\) zero-deficiency transitions by the trace. All these counts are positive. If \(6\nmid n\), no deficiency-zero walk exists, so the optimum cardinality is \(n-1\) with \(n a_n\) optimum configurations. If \(6\mid n\), the maximum is \(n\) and its six configurations were counted in the preceding step. These are precisely the stated formulas. \(\square\)

## Verification

The self-contained Python 3 program `verify.py` is part of the result package. It constructs the 17-state transfer and the two matrices directly, verifies every transition deficiency, checks the exact matrix identity and all base traces, and enumerates simple directed cycles. Independently, it builds ordinary graph edges and tests the third-edge definition directly, verifies local predicates on prism orders \(7\) through \(14\), enumerates all feasible edge subsets on orders \(7\) through \(11\), and cross-checks a separate weighted transfer through order \(84\). The recorded standard output is embedded as `verification_output.txt`.

The finite matrix identities above are **exact lemmas establishing the all-orders theorem**, not a claim that bounded computational experiments alone prove infinitely many cases. The direct graph checks give separate finite corroboration of the local predicate construction.

## Relationship to prior work

Chelladurai and coauthors introduced edge open packing and computed values for several standard graph classes in *Edge open packing sets in graphs* (2022), DOI 10.1051/ro/2022171. Brešar and Samadi (arXiv:2403.00750, Theorem 4.1) gave the general bound \(\rho_e^o(G)\le |E(G)|/\delta(G)\), which reads \(\rho_e^o(P_n)\le n\), and characterized equality graphs in general. Brešar, Dravec, Hedžet and Samadi (arXiv:2406.04020, Corollary 5.3) proved a Cartesian-product **lower bound**; their Proposition 5.9 treats a different vertex-packing quantity for prisms. These provide the natural context but do not themselves state the exact residue-dependent edge open packing values together with the complete optimal-set counts. In particular, the present result does not claim the general bound or the product inequality as new.

Relevant equivalent descriptions include a largest color class of an injective edge coloring and a maximum disjoint union of induced stars. Priority comparisons explicitly considered these aliases, exact cardinalities, Cartesian products, and earlier general upper/lower bounds; absence of a found covering theorem is not an unconditional novelty guarantee.

## Limitations

The result is restricted to ordinary cyclic prisms with \(n\ge7\); small triangular/square/pentagonal prisms and wider grids are excluded because the proof's local conflict geometry may differ. The theorem does not enumerate non-optimal EOP sets or classify injective edge colorings using multiple color classes. The finite-state proof and computational checks were assessed in the same review process; no independent scientific audit or exhaustive priority certification has been performed. Equivalent unpublished or differently indexed induced-star / edge-conflict results remain possible.

## References

1. C. Gayathri et al., “Edge open packing sets in graphs,” *RAIRO – Operations Research* 56 (2022), 3765–3776, DOI: 10.1051/ro/2022171. Open text: https://www.numdam.org/item/10.1051/ro/2022171.pdf (verified public online date: 2022-11-01).
2. B. Brešar and B. Samadi, “Edge open packing: complexity, algorithmic aspects, and bounds,” arXiv:2403.00750, version 1 dated 2024-03-01. Full text: https://arxiv.org/html/2403.00750v1.
3. B. Brešar, V. Dravec, T. Hedžet and B. Samadi, “Induced matching vs edge open packing: trees and product graphs,” arXiv:2406.04020, first posted 2024-06-06. Full text: https://arxiv.org/html/2406.04020v2.
