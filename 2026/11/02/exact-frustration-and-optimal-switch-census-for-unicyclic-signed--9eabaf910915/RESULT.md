# Exact frustration and optimal-switch census for unicyclic signed line graphs

## Finding

Let \(G\) be a finite connected simple unicyclic graph with unique cycle \(C\). Define
\[
r=|V(C)|,\qquad d_* = \min_{v\in V(C)}\deg_G(v),\qquad t=|\{v\in V(C):\deg_G(v)=d_*\}|.
\]
With the antisymmetric (equivalently, spectral signed) line graph \(\mathcal A(G)\) defined below, its edge-frustration index satisfies
\[
\ell(\mathcal A(G))=\begin{cases}0,&r\text{ even},\\d_*-1,&r\text{ odd}.
\end{cases}
\]
The number of orientations of the **labelled edges** of \(G\) realizing this optimum is
\[
N_G=\begin{cases}
2,&r\text{ even},\\
2t,&r\text{ odd and }d_*=2,\\
4t,&r\text{ odd and }d_*\ge3.
\end{cases}
\]
Two globally reversed orientations induce the same signed adjacency. As the ordinary line graph of connected \(G\) is connected, precisely two orientations induce each signed signature. Consequently the numbers of distinct optimally switched **signatures within the fixed switching class** are \(N_G/2\). This is a count of signatures, not a count of switching-equivalence classes (there is only one switching-equivalence class).

In the odd case the optimal orientations have exactly one vertex admitting both incoming and outgoing edges. This vertex belongs to \(C\) and has degree \(d_*\). Its two cycle edges have opposite incidence. Every noncycle edge incident with it is oriented in the same direction; all other vertices are pure sources or pure sinks. Each such orientation is optimal, and there are no others.

## Assumptions and scope

Graphs are finite, undirected, simple, connected, and have precisely one cycle of length at least three. All vertices and edges are labelled when counting orientations. Fix any orientation of \(E(G)\) and form its oriented incidence matrix \(D\), with entries \(+1\) at the head and \(-1\) at the tail of each edge. The signed line graph \(\mathcal A(G)\), whose vertices are edges of \(G\), has signed adjacency matrix \(D^{\mathsf T}D-2I\). Reversing one edge of \(G\) switches the associated vertex of \(\mathcal A(G)\), so the switching class is independent of the initial orientation.

The edge frustration index \(\ell\) is the smallest number of signed line-graph edges whose deletion balances the signing. Equivalently it is the minimum number of negative edges among all vertex switchings. For any orientation \(\omega\), let \(d^+_\omega(v)\) and \(d^-_\omega(v)\) denote its outdegree and indegree. Counting opposite-incidence pairs at every vertex gives the established identity [1]
\[
\ell(\mathcal A(G))=\min_\omega \sum_{v\in V(G)}d^+_\omega(v)d^-_\omega(v).
\]
We prove the exact unicyclic specialization and the complete set of optimizers.

## Proof

**Even cycle.** A connected unicyclic graph with an even cycle is bipartite. Orient every edge from one bipartition class to the other. Every vertex is a pure source or a pure sink; the displayed cost is zero. Conversely, a zero-cost orientation has no mixed vertices, hence every edge is directed from a pure source to a pure sink. As \(G\) is connected, its bipartition is unique up to interchanging classes. Therefore precisely two edge orientations attain zero.

**Odd-cycle lower bound.** In an orientation of an odd cycle, at least one cycle vertex has one entering and one leaving cycle edge: otherwise source/sink statuses would alternate around an odd cycle. At that vertex \(v\), \(d^+_\omega(v)\ge1\), \(d^-_\omega(v)\ge1\), and \(d^+_\omega(v)+d^-_\omega(v)=\deg_G(v)\). For positive integers with fixed sum \(d\), their product is at least \(d-1\), with equality precisely when one summand equals one. Thus
\[
\sum_{u\in V(G)}d^+_\omega(u)d^-_\omega(u)\ge \deg_G(v)-1\ge d_*-1.
\]
Since every cycle vertex has degree at least two, this bound is strictly positive.

**Construction and upper bound.** Pick any \(v\in V(C)\) of degree \(d_*\). Removing \(v\) from the odd cycle leaves a path on \(r-1\) vertices, an even number. Alternately designate these path vertices as sources and sinks; their endpoints then have opposite statuses. Orient every edge of this path and every tree edge attached to its vertices consistently from sources to sinks, extending the alternating source/sink designation into all attached trees. The two remaining cycle edges at \(v\) consequently have opposite incidence. Finally, orient all noncycle edges incident with \(v\) either towards \(v\) or away from \(v\), and continue the source/sink alternation into the corresponding trees. Then every vertex other than \(v\) is pure. At \(v\), the indegree/outdegree pair is \((1,d_*-1)\) or \((d_*-1,1)\). The objective is exactly \(d_*-1\), achieving the lower bound.

**Rigidity.** An optimal orientation must have some cycle-mixed vertex \(v\). The contribution at this vertex is at least \(d_*-1\), leaving no positive cost available elsewhere. Hence this is the unique mixed vertex in the entire graph, it has degree \(d_*\), and its in/out-degree pair is \((1,d_*-1)\) or its reversal. Its two cycle edges have opposing directions by cycle-mixedness. All remaining vertices are pure and therefore forced to alternate source/sink across their connected forest components. The edge orientations on the trees are uniquely forced once their attachment vertices' statuses are fixed. Consequently every optimal orientation belongs to the construction above.

**Multiplicity.** Choose the unique mixed cycle vertex in \(t\) ways. The path on the remaining \(r-1\) cycle vertices has two alternating source/sink assignments, giving two possible opposing incidences on the cycle edges at \(v\). If \(d_*=2\), no noncycle edge is incident to \(v\) and these are the only choices. If \(d_*\ge3\), all \(d_*-2\) noncycle edges incident to \(v\) must point the same way, but either of the two directions is possible; this doubles the count. Tree orientations are forced. Distinct choices give different edge orientations. This yields \(2t\) or \(4t\) as stated.

**Signed representatives and bound equality.** Global reversal multiplies every column of \(D\) by \(-1\), so leaves \(D^{\mathsf T}D-2I\) unchanged. Conversely, any two sign-switch vectors producing the same signature differ by a switching constant on each connected component of \(L(G)\), and \(L(G)\) is connected. Hence each signature corresponds to exactly two orientations, proving the counts. On odd unicyclic graphs the Max-Cut defect is one. Therefore the general bounds \(\operatorname{def}(G)\le\ell(\mathcal A(G))\le(\Delta(G)-1)\operatorname{def}(G)\) are attained on the left precisely for \(d_*=2\) and on the right precisely for \(d_*=\Delta(G)\), equivalently when all cycle vertices have degree \(\Delta(G)\).

## Verification

The accompanying standalone `verify_unicyclic.py` uses Python 3's standard library. Run `python verify_unicyclic.py` to reproduce `VERIFY_OK exhaustive_unicyclic_graphs_n3_to6=3898 signed_switching_checks=262 sampled_n7_to12=270`. The checker enumerates every labelled connected simple unicyclic graph on three through six vertices and every orientation of its edges. It compares computed optimum costs and counts with the theorem. In 262 small examples it separately enumerates sign switchings of the signed line graph, fixing one switching sign to quotient the ineffective global reversal. A deterministic collection of 270 larger examples supplies further consistency checks. The unbounded claim follows from the preceding proof, not from finite enumeration.

## Relationship to prior work

Bal [1, Section 8, Lemma 2 and Proposition 6] proves the general orientation-minimization identity and the sandwich bounds involving Max-Cut defect, and obtains exact results on cubic graphs and some other families. These general identities are inputs here, not new claims. The exact minimum-degree-on-cycle formula, all-optimum structure, and counts for arbitrary unicyclic graphs do not appear in the inspected full text of [1]. Belardo, Stanić and Zaslavsky [2] give the earlier spectral signed-line-graph definition and related signed total-graph theory, including frustration-related statements, but do not state the unicyclic formulas here. A scan of accessible research records and published literature found no statement implying this full characterization; historical priority is not certified.

## Limitations

The theorem assumes one cycle and finite simple connected graphs. It does not evaluate the frustration index for general cactus graphs or graphs with overlapping cycles. Counts refer to labelled edge orientations and to signatures at fixed labelled signed-line-graph vertices, not graph-isomorphism classes. The primary source already establishes the orientation identity; the new result is its exact unicyclic solution and optimizer census. External independent mathematical audit and comprehensive historical-priority verification have not been performed.

## References

[1] Hartosh Singh Bal, *The Antisymmetric Line Graph*, arXiv:2603.03087, version 1 publicly submitted March 3, 2026; version 2 dated April 17, 2026. https://arxiv.org/abs/2603.03087; Section 8, Lemma 2, Proposition 6, Theorems 6 and 8, Proposition 1 and Corollary 1.

[2] Francesco Belardo, Zoran Stanić and Thomas Zaslavsky, *Total graph of a signed graph*, arXiv:1908.02001v3 (2021), Section 2. https://arxiv.org/abs/1908.02001.
