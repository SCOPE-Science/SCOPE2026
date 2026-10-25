# The first three unresolved third-power-cycle total three-cut complexes

## Finding
For \(n\in\{13,14,15\}\), let \(G_n=C_n^3\) be the third power of the \(n\)-cycle, and let \(X_n=\Delta_3^t(G_n)\) be its *total three-cut complex*. The following are integral homotopy equivalences:

\[
X_{13}\simeq S^5,\qquad
X_{14}\simeq S^6,\qquad
X_{15}\simeq S^8\vee S^8.
\]

These three values constitute the entire previously untreated interval \((r+1)d+1\le n\le 2rd-r\) from Question 49 of Carnero Bravo [2] in the first case \(r=d=3\). In particular, the upper endpoint has *two* top-dimensional sphere summands, not one.

## Assumptions and scope
The graph \(G_n\) has vertex set \(\mathbb Z/n\mathbb Z=\{0,\ldots,n-1\}\), with distinct vertices adjacent precisely when their cyclic distance \(\min((a-b)\bmod n,(b-a)\bmod n)\) is at most \(3\). A triple \(I\subseteq V(G_n)\) is independent when all three pairwise cyclic distances are at least \(4\).

The faces of \(X_n\) are exactly the subsets \(F\subseteq V(G_n)\) for which \(V(G_n)\setminus F\) contains an independent triple. Equivalently, its facets are the complements \(V(G_n)\setminus I\) of independent triples. Here the word *total* distinguishes \(X_n\) from the ordinary three-cut complex, which allows arbitrary disconnected complementary triples.

Only the three displayed orders are asserted. Homology is integral unless explicitly marked otherwise. In the bitmask certificates, label \(j\) corresponds to bit \(2^j\); the empty face is omitted from the nonempty face-poset matching.

## Proof
**Exhaustive face construction.** Enumerate all three-element subsets of \(\{0,\ldots,n-1\}\), retaining those with pairwise cyclic distances at least four. For each independent triple \(I\), enumerate every nonempty subset of \(V(G_n)\setminus I\). The resulting face sets have, respectively, \(13\), \(28\), and \(50\) independent triples, and \(5434\), \(13106\), and \(28803\) distinct nonempty faces. This construction is exact: every face belongs to a facet of the stipulated form, and all facets are explicitly included.

**Explicit matching.** On each complete nonempty face poset, start with every face unpaired. Given a pivot vertex \(v\), pair each currently unpaired face \(F\) not containing \(v\) with \(F\cup\{v\}\), provided that face is also currently unpaired. Mark both paired and proceed to the next pivot. The pivot orders, one for each graph order, are stored in `morse_certificate.json`. The procedure is unambiguous: the potential pairs at any single pivot form a disjoint collection of two-element orbits under adding/removing \(v\). For machine-level reproducibility the verifier visits masks in increasing order.

The exact pair counts are \(2716\), \(6552\), and \(14400\). The complete unmatched face lists, displayed as pairs (integer bitmask, dimension), are

\[
\begin{array}{c|l}
n & \text{unmatched faces (bitmask, dimension)}\\\hline
13&(1,0),\ (3492,5)\\
14&(2,0),\ (13492,6)\\
15&(2048,0),\ (14042,8),\ (21357,8).
\end{array}
\]

**Acyclicity.** For every face-poset covering relation \(F\subset F\cup\{v\}\), orient it upwards precisely when it is a matched pair and downwards otherwise. The supplied verifier builds the **entire directed Hasse graph**, not a selection of gradient paths. Its covering-relation counts are \(31070\), \(84910\), and \(205800\); an exhaustive topological sort removes all \(5434\), \(13106\), and \(28803\) face-vertices respectively. Consequently all three matchings are acyclic. The program constructs every incidence rather than accepting the counts or acyclicity as assumptions. The full algorithm and concrete pivot orders are a finite, reproducible proof certificate.

**Homotopy conclusion.** Forman's acyclic matching theorem gives a CW complex homotopy equivalent to \(X_n\), having exactly one zero-cell and only one or two further cells of the respective dimensions \(5\), \(6\), or \(8\). Its skeleton immediately below that positive dimension consists of one point. All attaching maps are therefore constant, and the resulting CW complexes are \(S^5\), \(S^6\), and \(S^8\vee S^8\). This proves the stated integral homotopy equivalences, not merely field Betti-number equalities.

## Verification
Run `python verify_morse.py morse_certificate.json` from the extracted file directory to reconstruct the full face sets, every matching pair, every critical face, every codimension-one face relation, and the exhaustive DAG topological sorts. Its recorded output is `verify_morse_output.txt`.

Separately, `python verify_mod2.py` independently enumerates faces by vertex tuples, forms all boundary columns in all dimensions, and computes their exact ranks over \(\mathbb F_2\), without consulting the matching or its certificate. Its recorded output is `verify_mod2_output.txt`. The resulting nonzero reduced Betti numbers are \(\widetilde\beta_5=1\) at \(n=13\), \(\widetilde\beta_6=1\) at \(n=14\), and \(\widetilde\beta_8=2\) at \(n=15\), consistent with the stronger integral homotopy proof.

## Relationship to prior work
Bayer and collaborators [1] introduced total cut complexes and treated cycles, squared cycles, and other graph families; their Section 5 conjecture and tabulated grid values do not classify the third powers at these orders. Chauhan, Shukla and Vinayak [3] concern *total two-cut* complexes of powers of cycles, not the total three-cut complexes here.

Carnero Bravo [2, Theorem 43(c)] proves the one-sphere homotopy classification of the third-power total three-cut complex beginning at \(n=16\), and [2, Proposition 44] treats \(n=12\), where the answer is \(S^2\). Question 49 of [2] expressly asks for the intermediate interval; for \(r=d=3\), it consists of exactly \(n=13,14,15\). The present certificate closes this *first finite instance* of that question without claiming to settle the general parameter range.

## Limitations
No infinite-family formula for other cycle powers, other cut parameters, or higher orders is derived. The finite matching certificates prove these three integral homotopy types only. The mod-two computations are corroborative and do not independently establish integral homotopy. The literature comparison covers identified accessible sources and mathematical-record searches; unindexed overlapping work remains possible. Independent validation has not been performed.

## References
[1] Margaret Bayer, Mark Denker, Marija Jelić Milutinović, Rowan Rowlands, Sheila Sundaram, and Lei Xue, *Total Cut Complexes of Graphs*, arXiv:2209.13503, initial public version 2022-09-27, https://arxiv.org/abs/2209.13503.

[2] Andrés Carnero Bravo, *Total cut complexes and their duals*, arXiv:2602.21427, initial public version 2026-02-24; Theorem 43, Proposition 44, Question 49, https://arxiv.org/abs/2602.21427.

[3] Pratiksha Chauhan, Samir Shukla, and Kumar Vinayak, *Total two-cut complexes of powers of cycle graphs and Cartesian products of certain graphs*, arXiv:2512.04486, initial public version 2025-12-04, https://arxiv.org/abs/2512.04486.

[4] Robin Forman, *Morse theory for cell complexes*, Advances in Mathematics 134 (1998), 90–145. Acyclic matching theorem as recalled in [1, Appendix, Theorem 7.2].
