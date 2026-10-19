# Degree-spectrum rigidity in edge-Kempe reconfiguration of circular ladders

## Finding

For each integer \(n\ge3\), let \(L_n=C_n\square K_2\) have a top rim, a bottom rim, and \(n\) spokes. Fix a graph vertex \(x\), together with three distinct prescribed names for the colors on its three incident edges. The **vertex-fixed edge-Kempe graph** \(K_x(L_n)\) has vertices all proper edge-colorings with these names fixed at \(x\), and edges for a single interchange of two colors along a full connected alternating cycle disjoint from \(x\). All colors are distinguished; the local normalization chooses exactly one representative of each global color-permutation orbit.

Write \(N_n=|V(K_x(L_n))|\). If \(n\) is odd, then
\[
N_n=\frac{2^n-2}{6},\qquad K_x(L_n)\text{ is }(n-3)\text{-regular},\qquad |E(K_x(L_n))|=\frac{N_n(n-3)}2.
\]
If \(n\) is even, then
\[
N_n=\frac{2^n+8}{6},\qquad
\{\deg(v):v\in V(K_x(L_n))\}
=\{\underbrace{n-3,\ldots,n-3}_{N_n-2},\ n-1,\ 1\},
\]
and
\[
|E(K_x(L_n))|=\frac{(N_n-2)(n-3)+n}{2}.
\]
This is a **multiset** equality; at \(n=4\) both the generic degree and the degree-one exception equal one. The unique degree-\(n-1\) coloring has identical two-color alternating rims, and the unique exceptional degree-one coloring has oppositely alternating rims and monochromatic spokes. Here uniqueness is after fixing the three named colors at \(x\). The first case \(n=3\) is a single isolated vertex.

## Assumptions and scope

Vertices are \(u_i,v_i\) for \(i\in\mathbb Z/n\mathbb Z\), with edges \(u_iu_{i+1}\), \(v_iv_{i+1}\), \(u_iv_i\). Let \(a_i,b_i,c_i\in\{0,1,2\}\) be their colors, respectively. Each graph vertex sees each of three colors once. A bichromatic component in a proper cubic three-edge coloring is an even cycle, and a local edge-Kempe switch exchanges its two colors. Every local switch counted in \(K_x\) must avoid all edges incident to \(x\), equivalently avoid \(x\). Parallelism and other prism definitions are not implicit: the graph is exactly the Cartesian product stated, including the triangular-prism case.

## Proof

**1. Dichotomy of all colorings.** At column \(i\), the triples \((a_{i-1},a_i,c_i)\) and \((b_{i-1},b_i,c_i)\) are each all-distinct. If \(a_{i-1}=b_{i-1}\), then \(a_i=b_i\), each equal to the third color outside the pair comprising \(a_{i-1}\) and \(c_i\). If \(a_{i-1}\ne b_{i-1}\), then \(c_i\) is their missing third color, while \((a_i,b_i)=(b_{i-1},a_{i-1})\). Thus equality of the two rim colors persists around the entire cycle. There are two disjoint families.

In family **D** both rims carry one common cyclic word \(w=(a_0,\dots,a_{n-1})\) with adjacent entries distinct, and each spoke is forced to the third color outside its two adjacent rim colors. Conversely every such word gives a valid coloring. By the cycle chromatic-polynomial identity, their named number is \(2^n+2(-1)^n\). In family **O**, successive ordered pairs of rim colors alternate by swapping, and every spoke has their common missing third color. This closes exactly when \(n\) is even, in which case there are six named colorings (one for each ordered pair of distinct initial rim colors); otherwise there are none. Every proper coloring uses all three colors at each vertex. Hence global color permutation acts freely in orbits of size six, and fixing the three prescribed labels around \(x\) takes one representative from each orbit. The asserted vertex counts follow.

**2. Bichromatic cycle counts.** For a family-D coloring and a color \(q\), let \(r_q\) be its number of appearances in the common rim word. If \(r_q>0\), deleting the \(q\)-colored edges from both rims leaves \(r_q\) pairs of congruent rim paths. The spokes of the other two colors connect corresponding path endpoints, yielding precisely \(r_q\) bichromatic cycles in colors other than \(q\). If \(r_q=0\), the word alternates the other two colors (possible only for even \(n\)), all spokes have color \(q\), and the corresponding bichromatic graph comprises the two intact rim cycles. Therefore the total number \(F\) of bichromatic cycles (summed over the three pairs) is \(n\) when all three colors appear on the rim, and \(n+2\) in the two-color alternating-rim case. There is one orbit of the latter for even \(n\).

In family O (even \(n\)), the color pair excluding the spoke color makes the two separate rim cycles, while either color pair containing the spoke color makes one spanning alternating cycle. Its total number of bichromatic cycles is therefore \(F=2+1+1=4\). Family O also has exactly one color-permutation orbit.

**3. Degree.** At a fixed vertex \(x\), exactly one bichromatic cycle for each of the three color pairs passes through \(x\): these are the cycles containing the respective two incident edges. Thus precisely \(F-3\) bichromatic cycles avoid \(x\). Switching a cycle avoiding \(x\) produces another valid normalized coloring; switches of distinct cycles lead to distinct colorings, since their changed edge sets or exchanged color pairs differ. Consequently \(\deg_{K_x}=F-3\). Family D using three rim colors has degree \(n-3\). Family D using two has degree \(n-1\); family O has degree \(1\). Their orbit counts give the degree multiset. The edge formulas follow from the handshake lemma. This proof covers every integer \(n\ge3\) without finite-case extrapolation.

## Verification

The standalone program `prism_verify.py` enumerates named proper colorings directly by backtracking and normalizes at one vertex. For each named-color pair, it builds all maximal alternating cycles from graph edges and explicitly performs every cycle switch disjoint from the anchor. It asserts the complete degree multiset and vertex count for \(3\le n\le11\), independently of the formulas for individual cycles. `prism_verify_output.json` records the checked cases, including 341 normalized colorings at \(n=11\). An independently organized transfer-word checker (`prism_transfer_verify.py`) enumerates cyclic rim words and the separate complementary-rim family for \(3\le n\le12\), reproducing the degree spectra in `prism_transfer_verify_output.json`. The infinite statement is proved by the preceding combinatorial argument, not by these finite checks.

## Relationship to prior work

Belcastro and Haas, *Counting edge-Kempe-equivalence classes for 3-edge-colored cubic graphs* (arXiv:1209.1730, first posted 2012-09-08), prove edge-Kempe connectivity results, including for prism families. Their *Edge-Kempe-equivalence graphs of class-1 regular graphs* (Australasian Journal of Combinatorics 69 (2017), 197–214) defines the vertex-fixed graph, proves its general degree relation in Theorem 2.15, and determines the **crossed**-prism graphs in Theorem 4.2. The closing paragraph of Section 4 explicitly distinguishes ordinary prisms and observes that proving their vertex-fixed graph structure is harder. The present result gives the exact degree multiset, number of states and number of edges for **ordinary circular ladders**, rather than the full isomorphism type conjectured there. Global connectivity, where already known, is not claimed as new. Relevant searches found no prior result deriving this precise parity-dependent local spectrum; lack of retrieval is not proof of priority.

## Limitations

This theorem establishes vertex and edge counts and the full degree spectrum, not the complete adjacency structure, mixing time, diameter, Hamiltonicity, or exact graph isomorphism class of \(K_x(L_n)\). It is about ordinary circular ladders, not crossed prisms. The exceptional degrees may coincide with generic degree at small \(n\). The finite programs verify only the stated initial orders. Unindexed or otherwise unavailable published descriptions could imply this spectrum; publication priority has not been independently established. No independent external scientific audit is claimed.

## References

1. s.-m. belcastro and R. Haas, *Counting edge-Kempe-equivalence classes for 3-edge-colored cubic graphs*, arXiv:1209.1730v1 (publicly posted 2012-09-08); subsequently *Discrete Mathematics* 325 (2014), 77–84. https://arxiv.org/abs/1209.1730
2. s.-m. belcastro and R. Haas, *Edge-Kempe-equivalence graphs of class-1 regular graphs*, *Australasian Journal of Combinatorics* 69(2) (2017), 197–214. https://ajc.maths.uq.edu.au/pdf/69/ajc_v69_p197.pdf
3. J. McDonald, B. Mohar and D. Scheide, *Kempe equivalence of edge-colorings in subcubic and subquartic graphs*, *Journal of Graph Theory* 70(2) (2012), 226–239. https://doi.org/10.1002/jgt.20613
