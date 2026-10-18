# Complete zero-forcing and minimal-fort symmetry census of the dodecahedral graph

## Finding

Let \(D=GP(10,2)\) be the dodecahedral graph, a cubic graph with 20 vertices. Under ordinary (one-neighbor) zero forcing, the complete polynomial counting zero-forcing subsets is
\[
\begin{aligned}
\mathcal Z_D(z)={}&2040z^{6}+16900z^{7}+62890z^{8}+127480z^{9}\\
&+168244z^{10}+163560z^{11}+125230z^{12}+77460z^{13}\\
&+38760z^{14}+15504z^{15}+4845z^{16}+1140z^{17}\\
&+190z^{18}+20z^{19}+z^{20}.
\end{aligned}
\]
In particular there are exactly 804264 zero-forcing vertex subsets. Among them exactly 3000 are inclusion-minimal, with size counts \(2040\) at size \(6\), \(180\) at size \(7\), and \(780\) at size \(8\). Consequently \(Z(D)=6\), while the largest cardinality of an inclusion-minimal zero-forcing set is \(8\): the graph is not well-forced.

These 3000 inclusion-minimal zero-forcing sets form precisely 30 orbits under the full graph automorphism group of order 120: at size six, 14 orbits of size 120 and six of size 60; at size seven, one orbit of 120 and one of 60; and at size eight, five orbits of 120 and three of 60. In particular 2040 *minimum* sets form exactly 20 orbits. For the 2040 minimum sets, the synchronous zero-forcing propagation-round distribution is \((4:420,5:1020,6:480,7:120)\).

A *fort* is a nonempty vertex set \(F\) such that no vertex of \(V(D)\setminus F\) has exactly one neighbor in \(F\). There are exactly 74170 forts, of which exactly 830 are inclusion-minimal. The inclusion-minimal fort size distribution is \((7:60,8:20,9:200,10:410,11:120,12:20)\). They form precisely 15 automorphism orbits, as follows: at size 7, one orbit of 60; at size 8, one orbit each of 15 and 5; at size 9, one each of 120, 60 and 20; at size 10, one orbit of 120, three of 60, two of 40, and one of 30; at size 11, one of 120; and at size 12, one of 20. Explicit representatives and the 120 automorphisms are supplied in `orbit_certificate.json`.

## Assumptions and scope

All graphs are finite, undirected, and simple. Label the vertex set of \(D\) by \(\{u_i,v_i:0\le i<10\}\), with subscripts modulo 10. Its edges are \(\{u_iu_{i+1},u_iv_i,v_iv_{i+2}:0\le i<10\}\). Integer masks identify \(u_i\) with bit \(i\) and \(v_i\) with bit \(10+i\). A set \(B\) is initially black; each synchronous round colors all currently white vertices having a black neighbor with exactly one white neighbor. It is zero forcing if iteration colors every vertex. A zero-forcing set is *inclusion-minimal* if none of its proper subsets is zero forcing. This differs from *minimum*, meaning a smallest-cardinality zero-forcing set. All numbers and classifications in this result refer exactly to this 20-vertex graph, not to general generalized Petersen graphs.

## Proof

**Fort equivalence.** A black set \(B\) is zero forcing if and only if \(V(D)\setminus B\) contains no fort. If a forcing process halts with nonempty white set \(W\), then no black vertex has exactly one neighbor in \(W\), hence \(W\) is a fort. Conversely, if a nonempty fort \(F\) lies initially in the white set, a first move turning a vertex of \(F\) black would need a black vertex with exactly one white neighbor, contradicting the fort property. Thus no vertex of \(F\) can ever be colored.

**Exhaustive classification.** The standalone `fort.cpp` examines all nonempty bit masks \(F<2^{20}\). It marks \(F\) as a fort precisely when, for each outside vertex, the intersection of its three neighbors with \(F\) has cardinality different from one. Let \(f(F)\in\{0,1\}\) denote this flag and define \(h(W)=\sum_{F\subseteq W}f(F)\). A complete 20-coordinate subset-zeta transform computes \(h(W)\) for **every** \(W\subseteq V(D)\), so \(B\) is zero forcing precisely when \(h(V(D)\setminus B)=0\). Moreover a fort \(F\) is inclusion-minimal precisely when \(f(F)=h(F)=1\). This gives the fort counts and the full forcing polynomial without relying on a propagation algorithm.

Independently `direct.cpp` enumerates all \(2^{20}=1048576\) initially black masks, applies the ordinary color-change rule until success or stalling, and counts coefficients directly. As zero forcing is monotone in its initial set, a successful set \(B\) is inclusion-minimal exactly when every single-vertex deletion fails. The resulting counts agree with the fort-based computation mask by mask. For every minimum mask the direct algorithm also counts synchronous rounds, yielding the displayed distribution. The first nonzero coefficient confirms the already known equality \(Z(D)=6\).

**Full symmetry.** `verify.py` reconstructs the graph and exhaustively backtracks over all bijections on the 20 labeled vertices preserving adjacency. It finds exactly 120 automorphisms, and independently verifies every one preserves all 30 edges. For every representative listed in `orbit_certificate.json`, it applies every automorphism to the mask, checks the resulting orbit cardinality against the certificate, and checks that all orbits are pairwise disjoint and their union is exactly the corresponding complete enumerated set. This proves the complete orbit claims, with no assumption that a displayed subgroup is the full group. The two source programs independently construct adjacency via different formulas; the Python program constructs and rechecks it a third way. Exhaustiveness here is over finite sets and is not a claim for any other order of generalized Petersen graph.

## Verification

In a folder containing `direct.cpp`, `fort.cpp`, `verify.py`, and `orbit_certificate.json`, run:

```sh
g++ -O3 -std=c++17 direct.cpp -o direct
./direct
g++ -O3 -std=c++17 fort.cpp -o fort
./fort
python3 verify.py
```

The programs write `direct_status.bin`, `fort_status.bin`, `minimal_masks.txt`, and `minfort_masks.txt` in that folder. The Python verifier checks **all 1048576 forcing decisions** and the full orbit partition against the JSON certificate. `fort_status.bin` is one byte per mask; `direct_status.bin` is one 32-bit host-native integer per mask (verify on a conventional little-endian system). These generated outputs are not prerequisites supplied separately; they are generated by the included code. Exact successful-check output and assumptions are documented in `VERIFICATION.md`.

## Relationship to prior work

The established ordinary zero-forcing definition and associated minimum-rank bound go back to the AIM Minimum Rank–Special Graphs Work Group, published online November 26, 2007. Rashidi, Shajareh Poursalavati and Tavakkoli prove \(Z(GP(n,2))=6\) for \(n\ge10\), so in particular **the value \(Z(D)=6\) is already known** and is not a novelty claim. Boyer and collaborators introduce the zero-forcing polynomial and establish results for other graph families. Brimkov and Carlson study inclusion-minimal zero forcing, and Grood and collaborators investigate well-forced graphs. The additional claim here is the exact full dodecahedral subset polynomial, the all-minimal forcing and fort censuses, and their full automorphism-orbit structures. The cited works do not explicitly supply those classifications in the inspected text; unindexed prior calculations could overlap.

## Limitations

The evidence is a self-contained exhaustive finite calculation checked by separately constructed forcing and fort enumerators and a complete group-action verifier. It proves only this graph's finite classification; it does not imply a formula for the full generalized Petersen family or establish priority over every unpublished or unindexed computation. The earlier known zero-forcing number is not novel. Scientific review was not independently audited.

## References

1. AIM Minimum Rank–Special Graphs Work Group, *Zero forcing sets and the minimum rank of graphs*, Linear Algebra and its Applications 428 (2008), 1628–1648, DOI: 10.1016/j.laa.2007.10.009; available online 2007-11-26.
2. M. Rashidi, N. Shajareh Poursalavati and A. Tavakkoli, *Computing the zero forcing number for generalized Petersen graphs*, 2020; full paper: https://www.jacodesmath.com/index.php/jacodesmath/article/download/133/109/244.
3. *The zero forcing polynomial of a graph*, arXiv:1801.08910 (first posted 2018-01-26), https://arxiv.org/abs/1801.08910.
4. V. Brimkov and J. Carlson, *Minimal Zero Forcing Sets*, arXiv:2204.01810, https://arxiv.org/abs/2204.01810.
5. *Well-forced graphs*, arXiv:2312.14298, https://arxiv.org/abs/2312.14298.
