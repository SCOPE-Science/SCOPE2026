# Universal antichain structure and greedy completeness of stable matchings under persistent substitutable choice

## Finding

Consider a finite many-to-many matching market with contracts \(X\) and a single-valued choice function \(C_i:2^{X_i}\to 2^{X_i}\) for each agent \(i\). Suppose every choice is substitutable (SUB) and individually rationally persistent (IRP), as defined below. Let
\[
\mathcal I=\{M\subseteq X:\ C_i(M\cap X_i)=M\cap X_i\text{ for every agent }i\}.
\]
Then \(\mathcal I\) is a nonempty hereditary set family. Its inclusion-maximal elements, or *facets*, are **exactly** the CY-stable matchings. The outcomes of the Symmetric Matching Algorithm (SMA), ranging over all permutations of the contracts, are exactly these facets; in particular, **every** CY-stable matching is reachable by a suitable processing order.

The restriction to a hereditary family is best possible. For every finite \(X=\{x_1,\ldots,x_n\}\) and every nonempty antichain \(\mathcal A\subseteq 2^X\), there is a star market consisting of one firm and \(n\) distinct workers, with one contract per worker, whose choice functions satisfy SUB and IRP and whose entire set of CY-stable matchings is **precisely** \(\mathcal A\). This gives a realization theorem for arbitrary finite stable-outcome antichains, not merely an example with multiple stable matchings.

## Assumptions and scope

A contract \(x\in X\) has two distinct endpoints, one firm and one worker; agents may participate in multiple contracts. Let \(X_i\) denote all contracts incident to agent \(i\), and \(M_i=M\cap X_i\). Choice functions return subsets of offered menus and may return the empty set. The market is finite; no consistency, path independence, responsiveness, or size monotonicity is assumed.

**SUB:** for every agent \(i\) and \(A\subseteq B\subseteq X_i\),
\[
C_i(B)\cap A\subseteq C_i(A).
\]
**IRP:** if \(C_i(S)=S\) and \(x\in X_i\setminus S\) satisfies \(x\in C_i(S\cup\{x\})\), then
\[
S\subseteq C_i(S\cup\{x\}).
\]
A matching \(M\) is individually rational (IR) if \(M\in\mathcal I\). A nonempty \(Z\subseteq X\setminus M\) blocks an IR matching \(M\) when, for every agent \(i\) incident to \(Z\),
\[
Z_i\subseteq C_i(M_i\cup Z_i),\qquad Z_i=Z\cap X_i.
\]
An IR matching is CY-stable when no such \(Z\) exists. SMA starts from the empty matching and processes each contract exactly once; a contract is accepted when **both** endpoints choose it upon adjoining it to their current holdings, and the choice outputs are then used as the new holdings.

An *antichain* is a family of subsets no two distinct members of which contain one another. The antichain can include \(\varnothing\) only when it is the singleton family \(\{\varnothing\}\). The realization theorem includes this degenerate case and all finite \(n\geq0\).

## Proof

**Step 1: hereditary IR complex.** The empty matching is IR because \(C_i(\varnothing)\subseteq\varnothing\). If \(M\in\mathcal I\) and \(T\subseteq M\), then for every agent \(i\) substitutability gives
\[
T_i=C_i(M_i)\cap T_i\subseteq C_i(T_i)\subseteq T_i.
\]
Thus \(C_i(T_i)=T_i\) for every \(i\); hence \(T\in\mathcal I\). In particular, the inclusion-maximal sets of \(\mathcal I\) form a nonempty antichain.

**Step 2: a singleton augmentation is equivalent to a singleton block.** Fix \(M\in\mathcal I\) and \(x\notin M\). If \(x\in C_i(M_i\cup\{x\})\) for both endpoints \(i\) of \(x\), IRP applied to their IR holdings yields \(M_i\subseteq C_i(M_i\cup\{x\})\). Together with acceptance of \(x\) and contraction of choice, this implies \(C_i(M_i\cup\{x\})=M_i\cup\{x\}\). Holdings of all other agents are unchanged, so \(M\cup\{x\}\in\mathcal I\). Conversely, if \(M\cup\{x\}\in\mathcal I\), each endpoint chooses the entire enlarged holding and hence accepts \(x\). Thus a singleton block exists exactly when a one-contract IR augmentation exists.

If a nonempty set \(Z\) blocks \(M\), take any \(x\in Z\). At either endpoint \(i\) of \(x\), SUB applied to \(M_i\cup\{x\}\subseteq M_i\cup Z_i\) and \(x\in C_i(M_i\cup Z_i)\) implies \(x\in C_i(M_i\cup\{x\})\). Therefore every set block yields a singleton block. Since \(\mathcal I\) is hereditary, a nonmaximal \(M\in\mathcal I\) admits a one-element augmentation from some larger member. Hence CY-stability is equivalent to inclusion maximality in \(\mathcal I\).

**Step 3: greedy equivalence and full reachability.** Suppose the SMA has an IR current holding \(H\), and the next contract is \(x\). Step 2 says its two-endpoint acceptance test holds if and only if \(H\cup\{x\}\in\mathcal I\). In the accepted case IRP ensures the updated holdings equal \(H_i\cup\{x\}\), so the new matching really is \(H\cup\{x\}\); in the rejected case it remains \(H\). Thus SMA is the usual greedy algorithm for a hereditary family.

A contract rejected at a holding \(H\) remains infeasible after any subsequent growing holding \(H'\supseteq H\): otherwise heredity of \(\mathcal I\) would make \(H\cup\{x\}\) feasible. The final greedy matching is consequently inclusion-maximal. Conversely, given any facet \(M\in\mathcal I\), process every contract of \(M\) before any contract outside \(M\). Heredity makes each prefix feasible and therefore accepted. Maximality then makes every remaining contract infeasible and rejected. Hence the outcomes across orders are exactly the entire stable family.

**Step 4: realizing any prescribed antichain.** Let \(\mathcal A\subseteq2^X\) be a nonempty antichain, and put
\[
\mathcal D=\{S\subseteq X:\ S\subseteq A\text{ for some }A\in\mathcal A\}.
\]
This is a hereditary family with facets exactly \(\mathcal A\). Create one firm \(f\) incident to every \(x_j\), and for each \(j\) a different worker \(w_j\) incident only to \(x_j\). Let each worker always choose every available contract. Let the firm choose by
\[
C_f(S)=\begin{cases}S,&S\in\mathcal D,\\ \varnothing,&S\notin\mathcal D.\end{cases}
\]
If \(B\in\mathcal D\) and \(A\subseteq B\), then \(A\in\mathcal D\), giving \(C_f(B)\cap A=A=C_f(A)\). If \(B\notin\mathcal D\), then \(C_f(B)=\varnothing\), so SUB holds in either case. Whenever \(S\) is an IR menu for the firm and \(x\) is a challenger, \(C_f(S\cup\{x\})\neq\varnothing\) contains \(x\), hence \(S\cup\{x\}\in\mathcal D\), and the firm chooses the whole expanded menu. This proves IRP. Workers' accept-all choices satisfy both axioms directly. An assignment is IR precisely when it belongs to \(\mathcal D\), so Steps 1–3 give precisely \(\mathcal A\) as both the CY-stable family and the range of SMA across arrival orders.

For example, \(\mathcal A=\{\{x_1\},\{x_2,x_3\}\}\) has stable matchings of different cardinalities; an ordering beginning with \(x_1\) reaches the first, while an ordering beginning with \(x_2,x_3\) reaches the second. No restriction on the pattern of facets beyond being a nonempty antichain can hold on the SUB–IRP domain.

## Verification

The analytic argument proves the theorem for arbitrarily many contracts. As an independent finite stress test, the accompanying standard-library-only Python program enumerates all \(194\) nonempty hereditary systems on \(n\leq4\) labeled contracts, verifies SUB and IRP for each realized firm choice, checks CY-stability against every possible nonempty blocking subset, and executes SMA for every arrival permutation. All cases passed: \(14{,}092\) substitutability comparisons, \(3{,}709\) IRP tests, \(1{,}440\) candidate CY checks, and \(4{,}135\) arrival orders. A separate full enumeration of the \(4{,}096\) possible three-contract star-firm choice tables found \(67\) satisfying both axioms, and all \(67\) passed the stable/facet and all-orders reachability tests. Run \(\texttt{python3 verify.py}\) from the directory containing the embedded script. The computation is supplementary and is not substituted for the general proof.

## Relationship to prior work

Bansal, Bhattacharya, and Khare (2026), in the September version of their paper (arXiv:2603.23038v9), define the precise SUB and IRP axioms, CY-stability and SMA. They prove existence of a CY-stable matching for every processing order and reduce a blocking set to a singleton challenger (Lemma 1, Theorem 1). Their two-contract Example 3 illustrates order dependence, but does not characterize **all** stable outcomes as facets or establish that **every** nonempty antichain is realizable. The universal realization and greedy order-surjectivity proved above extend those existence statements. The paper expressly asks about the structure of CY-stable sets (Section 6).

The March first version (arXiv:2603.23038v1) uses a different General Acyclicity axiom and a Grow-or-Discard algorithm; it discusses possible failure of classical lattice structure, not the SUB–IRP antichain classification. Bando, Hirai, and Imamura (2025, Working Paper UTMD-075, Sections 3 and 5) define maximal choice sets and provide a three-doctor example with three pairwise maximal sets. Importantly, they also study **arbitrary downward-closed feasibility constraints** (general upper bounds) and a priority-based greedy choice/selection mechanism; this is a substantive antecedent of the combinatorial feasible-set perspective. Their priority-prefix choice, however, can violate IRP: with the feasible menus \(\varnothing,\{a\},\{b\}\), the priority \(a\succ b\) makes the firm choose \(\{a\}\) from \(\{a,b\}\), displacing the individually rational \(\{b\}\) when \(a\) arrives. The present theorem concerns **all** SUB–IRP choice profiles and gives a separate IRP-preserving realization of any antichain, plus full SMA order-surjectivity; neither is explicitly established by their priority-prefix analysis. Other classical lattice results assume different choice-consistency conditions. Thus the new theorem is consistent with the closest examples while supplying the unrestricted finite combinatorial realization statement.

## Limitations

The theorem concerns finite contracts, possibly empty menu choices, CY-stability as set blocking, and SUB plus IRP for **both** sides. The antichain construction deliberately uses a severe rejection response on infeasible menus; it is not claimed to be responsive, path-independent, demand-monotone, welfare-optimal, or plausible for every economic application. The conclusion is about the **inclusion** pattern of stable contract sets: it does not prove that no alternative market-specific order on stable matchings can form a lattice, nor any global incentive or comparative-statics theorem. Novelty assessment is provisional pending independent literature audit; older or inaccessible work could contain equivalent universal constructions.

## References

1. V. Bansal, M. Bhattacharya and O. Khare, *Stable Matching with Choice Correspondences: Beyond Path Independence*, arXiv:2603.23038v9, 6 September 2026, https://arxiv.org/html/2603.23038v9 (definitions, Algorithm 1, Lemma 1, Theorem 1, Section 6).
2. V. Bansal, M. Bhattacharya and O. Khare, *Stable Matchings with Choice Correspondences Under Acyclicity*, arXiv:2603.23038v1, publicly posted 24 March 2026, https://arxiv.org/html/2603.23038v1 (Section 4.1 and distinct General Acyclicity model).
3. K. Bando, T. Hirai and K. Imamura, *Stable Matching under Inconsistent Choice Functions*, UTMD-075, 13 February 2025, https://www.mdc.e.u-tokyo.ac.jp/wp/wp-content/uploads/2025/02/UTMD-075.pdf (Sections 3 and 5, Definition 2, Example 2, and general upper-bounds constraints).
4. C. P. Chambers and M. B. Yenmez, *Choice and Matching*, American Economic Journal: Microeconomics 9(3), 2017, 126–147 (original CY-stability and path-independence setting).
