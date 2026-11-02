# All forts and inclusion-minimal forts of bouquets of cycles: exact cardinality polynomials

## Finding

Let \(B=B(\ell_1,\ldots,\ell_k)\), with \(k\ge 2\) and each integer \(\ell_i\ge3\), be a bouquet of cycles: form the disjoint cycles \(C_{\ell_i}\) and identify one designated vertex from each as a single common vertex \(v\), leaving every other vertex distinct. Put \(N=1+\sum_{i=1}^k(\ell_i-1)\). A *fort* is a nonempty vertex set \(F\) such that every vertex outside \(F\) has either zero or at least two neighbors in \(F\). A fort is *inclusion-minimal* if it contains no proper nonempty fort.

Let \(H_r(z)\) be the polynomial enumerating complements of independent sets of the path \(P_r\):
\[
H_r(z)=\sum_{T\subseteq V(P_r)\atop T\text{ independent}}z^{r-|T|},\qquad H_0=1,\quad H_1=1+z,\quad H_r=z(H_{r-1}+H_{r-2})\ (r\ge2).
\]
Let \(Q_r(z)\) enumerate complements of **maximal** independent sets:
\[
Q_r(z)=\sum_{T\subseteq V(P_r)\atop T\text{ maximal independent}} z^{r-|T|},\qquad Q_0=Q_1=1,\quad Q_2=2z,\quad Q_r=zQ_{r-2}+z^2Q_{r-3}\ (r\ge3).
\]
For \(r\ge2\), let \(E_r(z)\) enumerate the terms of \(Q_r\) for which neither endpoint of \(P_r\) belongs to \(T\). Explicitly,
\[
E_2=0,\quad E_3=z^2,\quad E_4=0,\quad E_5=z^3,\quad E_r=z^4Q_{r-6}\ \ (r\ge6).
\]
Then the **all-fort** polynomial and **inclusion-minimal-fort** polynomial of \(B\), both weighted by the cardinality of \(F\), are respectively
\[
\boxed{\Phi_B(z)=z\prod_{i=1}^k H_{\ell_i-1}(z)+\prod_{i=1}^k\bigl(1+z^2H_{\ell_i-3}(z)\bigr)-1,}
\]
\[
\boxed{\mathcal M_B(z)=\sum_{i=1}^k z^2Q_{\ell_i-3}(z)+z\prod_{i=1}^k\bigl(Q_{\ell_i-1}(z)-E_{\ell_i-1}(z)\bigr).}
\]
In particular, if \(\operatorname{Fib}_0=0,\operatorname{Fib}_1=1\), the total number of nonempty forts is
\[
\Phi_B(1)=\prod_{i=1}^k\operatorname{Fib}_{\ell_i+1}+\prod_{i=1}^k(1+\operatorname{Fib}_{\ell_i-1})-1.
\]
The polynomial of inclusion-maximal failed **standard** zero forcing initial sets, weighted by their numbers of initially blue vertices, is \(z^N\mathcal M_B(z^{-1})\). In particular, writing \(s=\min_i\lceil\ell_i/2\rceil\), the largest failed set has cardinality
\[
\boxed{F(B)=N-s,}
\]
and there are exactly
\[
\boxed{\sum_{i:\lceil\ell_i/2\rceil=s}\begin{cases}1,&\ell_i\text{ even},\\(\ell_i-1)/2,&\ell_i\text{ odd}\end{cases}}
\]
largest failed sets. This count includes both odd and even shortest effective cycle lengths when they tie, for example cycles of lengths three and four both supply forts of size two.

## Assumptions and scope

Graphs are finite, undirected, simple and labeled. A vertex on a petal other than \(v\) has exactly two neighbors, along that petal, and all petals meet only at \(v\). The path \(P_0\) is the empty graph. *Maximal independent* means inclusion-maximal, not merely of maximum cardinality. *Inclusion-maximal failed zero forcing* is distinct from *maximum-cardinality failed zero forcing*. The two polynomials count labeled vertex sets, not symmetry orbits. The recurrence and polynomial statements remain valid for a single cycle, but the extremal formula is stated only for \(k\ge2\).

## Proof

Write the \(i\)-th petal's noncentral vertices consecutively as \(u_{i,1},\ldots,u_{i,r_i}\), where \(r_i=\ell_i-1\); its edges include \(vu_{i,1}\), \(u_{i,r_i}v\), and consecutive path edges.

**Case 1: \(v\in F\).** Let \(T_i\) consist of the vertices of the \(i\)-th peripheral path that lie outside \(F\). If two consecutive path vertices lie in \(T_i\), consider the first such outside run, starting at an endpoint or just after a selected vertex: one of the boundary outside vertices has exactly one selected neighbor (including \(v\) at an outer endpoint). Thus \(F\) cannot be a fort. Conversely, when every \(T_i\) is independent, each outside peripheral vertex has both neighbors inside \(F\); hence \(F\) is a fort. Each petal contributes \(H_{r_i}\), and the hub contributes the factor \(z\), giving the first term of \(\Phi_B\).

Such a fort is inclusion-minimal exactly when, for each \(i\), \(T_i\) is maximal independent in the peripheral path and contains at least one of its two endpoints. Necessity of maximal independence follows because an additional vertex can otherwise be deleted from \(F\) while preserving the hub. If both endpoints are selected in \(F\), the selected vertices of this one petal alone form a nonempty fort without the hub, so minimality fails. Conversely, maximality of all \(T_i\) forbids any proper subfort retaining \(v\); at least one omitted endpoint in each petal rules out a nonempty subfort omitting \(v\), as proved in Case 2. The allowed weighted contribution from petal \(i\) is \(Q_{r_i}-E_{r_i}\). This gives the second term of \(\mathcal M_B\).

**Case 2: \(v\notin F\).** Call a petal *active* if it meets \(F\). In an active petal, the first selected peripheral vertex must be \(u_{i,1}\), since otherwise its predecessor is outside \(F\) with exactly one selected neighbor; likewise the last must be \(u_{i,r_i}\). Between these endpoints, any pair of consecutive outside vertices creates a boundary outside vertex with exactly one selected neighbor. Conversely, selected endpoints and an independent omitted set inside \(u_{i,2},\ldots,u_{i,r_i-1}\) ensure that all outside peripheral vertices have zero or two selected neighbors. The outside hub then has exactly two selected neighbors from each active petal, so it cannot have exactly one. Inactive petals are completely empty. Consequently each petal contributes either zero selected vertices (weight \(1\)) or a selected set with both endpoints and an independent omitted interior set (weight \(z^2H_{r_i-2}\)); at least one petal must be active. The weighted sum is \(\prod_i(1+z^2H_{\ell_i-3})-1\), the other term of \(\Phi_B\).

An inclusion-minimal fort without the hub has exactly one active petal: if there were two, deleting all selected vertices of one active petal would preserve the fort. Within a single petal, inclusion-minimality requires its omitted interior set to be maximal independent; otherwise an additional interior vertex could be deleted. These conditions are also sufficient. The weighted contribution is \(z^2Q_{\ell_i-3}\) for active petal \(i\), completing the proof of \(\mathcal M_B\).

**Path-polynomial recurrences.** For \(H_r\), split independent sets according as the first path vertex is present or absent. The resulting complementary-size weights give \(H_r=z(H_{r-1}+H_{r-2})\). For maximal independent sets, either the first vertex belongs to \(T\), forcing the second out, or the first is out, forcing the second in and the third out. This gives \(Q_r=zQ_{r-2}+z^2Q_{r-3}\). If neither path endpoint belongs to \(T\), maximality forces vertices two and \(r-1\) into \(T\), and their inner neighbors out; for \(r\ge6\) the remaining free maximal-independent choice is on a path with \(r-6\) vertices, giving \(E_r=z^4Q_{r-6}\). Direct inspection covers \(2\le r\le5\). These are exact weighted bijections, not experimental recurrences.

**Extremal failed sets.** A set of blue vertices is failed under standard zero forcing if and only if the uncolored complement contains a fort: a terminal uncolored set is a fort, and an existing disjoint fort cannot be entered by any forcing step. Thus inclusion-maximal failed sets correspond bijectively to complements of inclusion-minimal forts. In the hub-absent case the smallest fort supported on petal \(i\) has cardinality \(\ell_i-1-\alpha(P_{\ell_i-3})=\lceil\ell_i/2\rceil\). It arises from a **maximum-cardinality** independent set on the interior path, whose number is one for even \(\ell_i\) and \((\ell_i-1)/2\) for odd \(\ell_i\). A hub-containing fort has size at least \(1+\sum_i\lfloor(\ell_i-1)/2\rfloor\); for \(k\ge2\) this is strictly greater than the smallest hub-absent fort size. Hence the smallest fort size is \(s\), and the exact count of smallest forts is the displayed sum over all petals satisfying \(\lceil\ell_i/2\rceil=s\). Taking complements proves both extremal failed-zero-forcing conclusions. Finally, \(H_r(1)=\operatorname{Fib}_{r+2}\) yields the Fibonacci product for \(\Phi_B(1)\).

## Verification

The standalone Python file `CODE/bouquet_verify.py` constructs each graph from its edges, tests the defining fort condition directly for every nonempty subset, and tests inclusion-minimality by comparison with **all proper fort subsets**. It then independently computes both proposed polynomials using path independent-set and maximal-independent-set enumeration. The comparison passed on 47 graph instances, totaling 167,593 nonempty subsets. A second suite directly simulates zero forcing and checks the maximal failed-set polynomial on eight bouquets; weighted recurrences and the boundary-restricted polynomial were independently compared with direct path enumeration through length sixteen. The script exits with assertions on any disagreement. This is finite corroboration only; the arbitrary-parameter proof is the bijective case analysis above.

## Relationship to prior work

Becker, Cameron, Hanely, Ong, and Previte (arXiv:2404.05963, initially public April 9, 2024), study inclusion-minimal forts and give general vertex-sum constructions (Theorem 25, Corollary 26, Proposition 27) and exact minimal-fort counts of complete-graph windmills (Corollary 28). Their windmill of triangles is precisely the specialization \(\ell_1=\cdots=\ell_k=3\); its known number of minimal forts \(2^k+k\) follows from the polynomial here, and is **not claimed as new**. Their general vertex-sum results imply a path toward part of the inclusion-minimal characterization; the complete **all-fort cardinality polynomial**, the explicit peripheral boundary filter, and the mixed-length weighted classifications are not stated in the inspected source. Brimkov and Carlson (arXiv:2204.01887) provide background on minimal zero forcing sets, a different parameter. This work neither claims a new characterization of forts as zero-forcing obstructions nor a new scalar value for the all-triangle case.

## Limitations

The formulas count labeled sets and do not classify automorphism orbits. For arbitrary cactus graphs with several articulation vertices, no formula is asserted. The maximal failed-set statement is about inclusion maximality, while the scalar extremum is the maximum failed cardinality; neither gives the full polynomial of all (not necessarily maximal) failed zero forcing starting sets. Publication priority remains uncertain for unindexed papers and possible unpublished explicit cycle-bouquet enumerations. A published general vertex-sum theorem covers a structural component of the minimal-fort argument; the novel claim depends on the specific full cardinality enumeration and mixed-petal boundary classification. 
## References

1. P. Becker, T. R. Cameron, D. Hanely, B. Ong, and J. P. Previte, *On the number of minimal forts of a graph*, arXiv:2404.05963, first posted 2024-04-09, https://arxiv.org/abs/2404.05963. See Section 5, Theorem 25, Corollary 26, Proposition 27, and Corollary 28.
2. B. Brimkov and C. Carlson, *Minimal zero forcing sets*, arXiv:2204.01887, first posted 2022-04-04, https://arxiv.org/abs/2204.01887.
