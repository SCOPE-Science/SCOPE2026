# Sharp sample-incidence cost for full-capacity cyclic adjacent-pair testing

## Finding

**Theorem.** Fix any integer \(m\ge2\) and set \(n=2^m-1\). Arrange \(n\) items on a labeled cycle, and allow as the unknown positive set only the empty set or one of the \(n\) edges (the two consecutive endpoints of that edge). Test pools are arbitrary subsets of items, chosen nonadaptively, with a noiseless positive result exactly when the pool meets the positive set. Then \(m\) tests, the information-theoretic minimum, suffice; among *all* such \(m\)-test schemes the exact minimum total number of item-to-pool incidences is

\[
W_{\min}(m)=m2^{m-2}.
\]

Indeed, every test in an incidence-optimal scheme contains exactly \(2^{m-2}\) items, and the selected items in each test form an independent set of the cycle (no adjacent selected pair). Conversely a valid \(m\)-test scheme with independent pool sets achieves the lower bound. A uniform explicit construction simultaneously attains these equalities for every \(m\ge2\).

## Assumptions and scope

Index the cycle vertices by \(i\in\{0,1,\ldots,n-1\}\), with indices modulo \(n\). An \(m\)-test scheme is an incidence matrix \(H\in\{0,1\}^{m\times n}\); the column at item \(i\) is its mask \(a_i\in\{0,1\}^m\). The observed mask under defective edge \(\{i,i+1\}\) is the coordinatewise Boolean OR

\[
u_i=a_i\lor a_{(i+1)\bmod n}.
\]

The empty defective set yields the zero mask. Thus exact decoding means that the \(n\) edge masks \(u_i\) are distinct and nonzero. The incidence cost \(W(H)=\sum_{i=0}^{n-1}\mathrm{wt}(a_i)=\sum_{j=0}^{m-1}|P_j|\), where \(P_j\) is the set of items included in test \(j\). Zero columns and repeated columns are permitted, provided all allowed configurations remain distinguishable. All tests are noiseless; no claim is made for isolated defectives, arbitrary pairs, longer intervals, false outcomes, or dilution.

## Proof

**Counting lower bound and equality characterization.** Since the \(n=2^m-1\) edge masks are distinct and nonzero, they must be exactly the complete set of nonzero binary \(m\)-masks. Therefore, in each coordinate \(j\), precisely \(2^{m-1}\) of the edge masks have a one. A chosen item in pool \(P_j\) can make at most two of these edge masks one, because that item has exactly two incident cycle edges. Consequently

\[
2^{m-1}\le 2|P_j|\qquad\Longrightarrow\qquad |P_j|\ge2^{m-2}.
\]

Summing over \(m\) pools proves \(W(H)\ge m2^{m-2}\). Equality in the sum holds if and only if equality holds in every coordinate's inequality. For any coordinate, equality means that the two incident-edge sets contributed by the selected vertices are pairwise disjoint: if two selected items shared an incident edge then the total number of positive edge outcomes would be strictly less than twice the pool size. Such overlap occurs exactly when the pool contains two neighboring cycle items. Thus equality holds precisely when every pool is an independent vertex set, and then every pool has size \(2^{m-2}\) by the fixed edge-output count.

**Construction.** Interpret \(m\)-bit masks as integers between \(0\) and \(2^m-1\), with bit zero the least significant bit. Set the item mask \(a_i\) equal to the binary expansion of the integer

\[
b_i=\begin{cases}
i,&i\text{ is even},\\
1,&i\equiv1\pmod4,\\
0,&i\equiv3\pmod4.
\end{cases}
\]

Every even index is within the valid mask range, and the final index \(n-1=2^m-2\) is even. In each complete four-index block, the consecutive edge OR masks are, as ordinary integers,

\[
\begin{aligned}
 b_{4r}\lor b_{4r+1}&=4r+1,\\
 b_{4r+1}\lor b_{4r+2}&=4r+3,\\
 b_{4r+2}\lor b_{4r+3}&=4r+2,\\
 b_{4r+3}\lor b_{4r+4}&=4r+4.
\end{aligned}
\]

Each displayed formula applies when its leftmost index is at most \(n-2\). The final wraparound edge, from \(n-1\) to \(0\), has OR mask \(n-1=2^m-2\) because \(b_0=0\). Together the edge outcomes are exactly every integer from \(1\) through \(n\) once each: in each four-block the four outputs are merely the permutation \((4r+1,4r+3,4r+2,4r+4)\), and the final block contributes its first three entries. This proves distinguishability.

**Sharp incidence and balance.** Test zero contains precisely the item indices congruent to \(1\) modulo \(4\), which number \(2^{m-2}\). For every higher bit \(1\le j<m\), a selected item must have an even index whose \(j\)-th bit is one; among the even integers from \(0\) to \(2^m-2\), there are exactly \(2^{m-2}\) such indices. Every pool contains no adjacent items: the zeroth-bit indices are separated by four, and every higher-bit pool consists entirely of even indices with neither \(0\) nor the wraparound adjacency selected. All \(m\) pools therefore have size \(2^{m-2}\), yielding \(W(H)=m2^{m-2}\), which meets the lower bound. \(\square\)

## Verification

Run the accompanying standalone Python program with `python verify.py`. It uses integer bit masks to enumerate all adjacent-pair responses, checks that they are the complete nonzero output space, checks every pool size and adjacency constraint, and confirms the incidence formula for each \(2\le m\le13\). Representative incidence totals are \(2,6,16,40,96\) for \(m=2,3,4,5,6\), respectively. This finite computation tests the implementation and edge boundaries only; the preceding symbolic argument is the proof for every integer \(m\ge2\).

## Relationship to prior work

Colbourn and Müller–Jimbo study consecutive-positive group testing and stronger two-consecutive-positive-detectable matrices. The latter distinguish individual-item masks and adjacent unions as well, unlike the restricted exact-pair-or-empty model here. Bousquet–Dailly–Duchêne–Kheddouci–Parreau study union vertex-distinguishing edge colorings: on a cycle, their vertex labels are unions of edge color sets, equivalent to the adjacent-OR model under the cycle's edge-to-item duality. They determine the *number of colors* for cycles under a nonempty edge-label constraint, not the minimum aggregate size of those edge labels. Thus the information-theoretic \(m\)-test count itself is not offered here as an original general insight. The present claim concerns the additional exact resource objective \(W(H)\), its equality conditions, and an explicit simultaneous minimum-incidence, perfectly balanced construction even when empty item masks are permitted. Later work on balanced constant-weight Gray codes for consecutive positives imposes fixed item weight and extra uniqueness/error-detection constraints and therefore does not assert this variable-weight all-output cost minimum.

## Limitations

The design includes a zero item mask, and for \(m\ge3\) also repeated masks, so it does **not** identify a single positive item, distinguish arbitrary defective subsets, or satisfy stronger two-consecutive-positive-detectable conditions. It has no built-in noise resilience; biological sampling may need fixed positive replication per item, which this scheme intentionally does not provide. The originality comparison includes an accessible full original coloring article, author thesis and full later pooling article, but some historical related manuscripts and a recent conference manuscript could not be completely inspected, leaving a bibliographic risk of unrecognized earlier equivalent cost minimization. No independence or external validation is asserted.

## References

1. N. Bousquet, A. Dailly, É. Duchêne, H. Kheddouci, and A. Parreau, *A Vizing-like theorem for union vertex-distinguishing edge coloring*, arXiv:1605.02588, first posted 2016-05-09; Discrete Applied Mathematics 232 (2017), 88–98. The preprint is the date anchor, not its journal publication.
2. M. Müller and M. Jimbo, *Consecutive positive detectable matrices and group testing for consecutive positives*, Discrete Mathematics 279 (2004), 369–381, doi:10.1016/S0012-365X(03)00282-6.
3. M. Jimbo and M. Müller, *Combinatorial problems arising from pooling designs for DNA library screening*, Le Matematiche 59 (2004), publicly hosted at the journal's article page.
4. G. He and collaborators, *Unbiased and error-detecting combinatorial pooling experiments with balanced constant-weight Gray codes for consecutive positives detection*, Bioinformatics 41 (2025), btaf611, doi:10.1093/bioinformatics/btaf611.
5. N. T. Thao and V. K. Vu, *Low-Weight Gray Codes for Limited Resources Group Testing of Consecutive Positives*, ISIT (2026), doi:10.1109/ISIT62367.2026.11653620 (conference abstract consulted; full manuscript not available).
6. M. Cheraghchi, A. Karbasi, S. Mohajer, and V. Saligrama, *Graph-Constrained Group Testing*, arXiv:1001.1445 (2010).
