# Complete triangle structure of the fifth prime-power Pythagorean box

## Finding

For the fifth prime-power box of Xiao [1], put
\[
\Phi_5=\{2^a3^b5^c7^d11^e:0\le a,b,c,d,e\le4\}.
\]
Let \(G_5\) be the simple graph with vertex set \(\Phi_5\) in which distinct vertices \(u,v\) are adjacent exactly when \(u^2+v^2\) is an integer square. A triangle is an **unordered** three-element clique. Then \(G_5\) has precisely \(288\) triangles, given without repetitions by
\[
\begin{aligned}
\{&k(240,252,275),\;k(1008,1100,1155):\\
 &k=3^b5^c7^d11^e,\quad 0\le b,c\le2,\quad0\le d,e\le3\}.
\end{aligned}
\]
A triple here means its set of three entries, and the two displayed primitive Euler bricks are previously known [2,3]; their identification as bricks is *not* claimed as new.

Form a graph \(I_5\) whose vertices are the \(288\) triangles of \(G_5\), with an edge when two triangles share at least one original vertex. The graph \(I_5\) is exactly the disjoint union of \(174\) isolated vertices and \(57\) single edges. Of the \(57\) pairs, \(9\) share one original vertex and \(48\) share two.

Consequently, the maximum number \(\nu_3(G_5)\) of vertex-disjoint triangles and the minimum number \(\tau_3(G_5)\) of vertices intersecting every triangle both equal
\[
\boxed{\nu_3(G_5)=\tau_3(G_5)=231}.
\]
This determines exact triangle-hypergraph invariants but does not determine the graph's independence number.

## Assumptions and scope

All numbers are ordinary positive integers; all squares are tested with exact integer arithmetic. The graph is induced on exactly the \(5^5=3125\) elements of \(\Phi_5\). The hypotenuse witnessing an edge need **not** lie in the box. The count is for unordered, distinct three-vertex cliques, not labeled triples and not Pythagorean triples having just two graph vertices. A primitive Euler brick is an unordered positive triple with integer pairwise face diagonals and gcd of the three entries equal to one.

## Proof

**Exact finite classification.** Enumerate the \(3125\) vertices by the five nested exponent loops, and sort them increasingly. Unique factorization makes every generated vertex distinct. For each of the \(\binom{3125}{2}=4{,}881{,}250\) unordered pairs \(i<j\), put \(s=v_i^2+v_j^2\) and \(r=\lfloor\sqrt{s}\rfloor\). Insert an edge if and only if the exact integer equality \(r^2=s\) holds. There is no upper bound on the possible hypotenuse beyond what the exact square test enforces. This exhausts all graph edges, giving \(14{,}856\) edges.

For every edge \(i<j\), take the common neighbors \(k>j\). Every unordered graph triangle has a *unique* ordered index triple \(i<j<k\), so this loop examines all triangles exactly once. The resulting exact count is \(288\). Dividing the three increasing labels in each triangle by their gcd produces precisely the following frequency table:

| Primitive labels | Number of triangles |
|---|---:|
| \((240,252,275)\) | \(144\) |
| \((1008,1100,1155)\) | \(144\) |

The attached executable `verify_bricks.py` performs these finite loops with arbitrary-precision integers and `isqrt`; the separately implemented `verify_independent.cpp` reproduces the edge and triangle census with signed 128-bit exact squared integers. Both were executed and passed. The scripts are a complete, executable finite proof of the table, not an inference from sampled data.

**Explicit multiplicative families.** For each of the two primitive triples, the maximum exponent of primes \((2,3,5,7,11)\) among the three coordinates is exactly \((4,2,2,1,1)\). Therefore multiplication of all three coordinates by a positive integer \(k\) keeps them inside \(\Phi_5\) exactly when
\[
k=3^b5^c7^d11^e,\qquad0\le b,c\le2,\quad0\le d,e\le3.
\]
These give \(3\cdot3\cdot4\cdot4=144\) scales per primitive triple. Integer-square face diagonals are preserved by scaling; directly the two seed triples have diagonal triples \((348,365,373)\) and \((1492,1533,1595)\), respectively. Each seed has gcd one, so different scales or different seeds yield different primitive reductions. Thus all \(288\) displayed triples are valid and distinct. The exhaustive table proves there are no others.

**Structural proof of intersections.** The two primitive brick types both have ordered coordinate valuations
\[
(\nu_2(u),\nu_2(v),\nu_2(w))=(4,2,0).
\]
Every allowed multiplier \(k\) is odd. Consequently, two scaled triangles can share a label only in the *same coordinate position*. Within either primitive family, sharing a coordinate forces identical multipliers and hence identical triangles. Between the two families, the three corresponding-coordinate seed ratios are, respectively,
\[
\frac{1008}{240}=\frac{21}{5},\qquad
\frac{1100}{252}=\frac{275}{63},\qquad
\frac{1155}{275}=\frac{21}{5}.
\]
Write \(k_A=3^b5^c7^d11^e\) for a first-family multiplier and \(k_B=3^{b'}5^{c'}7^{d'}11^{e'}\) for a second-family multiplier, with the allowed exponent ranges as above. If \(k_A/k_B=21/5\), the exponent differences are \((b-b',c-c',d-d',e-e')=(1,-1,1,0)\), permitting exactly \(2\cdot2\cdot3\cdot4=48\) pairs; those pairs share the first and third coordinates. If \(k_A/k_B=275/63\), the differences are \((-2,2,-1,1)\), allowing exactly \(1\cdot1\cdot3\cdot3=9\) pairs; those share only the middle coordinate.

The two ratio conditions cannot hold for a fixed multiplier from either family: the first forces \(b\ge1\) and \(c\le1\) in the first family, while the second forces \(b=0\) and \(c=2\). Analogously the second-family exponent conditions are disjoint. Thus the \(57\) intersecting pairs are mutually isolated and \(I_5\) is precisely \(174K_1\sqcup57K_2\). The supplied verifier also exhaustively checks all \(\binom{288}{2}=41{,}328\) triangle pairs, reproducing the \(48+9\) partition.

In a two-vertex component, the two triangles intersect, so a vertex-disjoint triangle packing can use at most one. In an isolated component it can use at most one. Conversely, taking one triangle from each of the \(174+57=231\) components gives a pairwise vertex-disjoint family, because any shared original vertex would create an edge in \(I_5\). Thus \(\nu_3(G_5)=231\).

Every hitting set meets each packed triangle, so \(\tau_3(G_5)\ge231\). Choosing one original vertex from each isolated triangle, and one common original vertex from each overlapping pair, gives a hitting set of \(231\) vertices, hence \(\tau_3(G_5)=231\). The checker separately constructs both sets and verifies their sizes and disjointness/cover properties. This triangle-hypergraph classification does not by itself improve the independently known upper bounds for the graph independence number.

## Verification

Run from the same directory as the attached scripts:

```
python3 verify_bricks.py
g++ -std=c++17 -O2 verify_independent.cpp -o verify_independent
./verify_independent
```

The Python checker creates every vertex and tests every unordered pair; it checks both primitive-type multiplicities, all triangle intersections, and explicit optimal packing and hitting witnesses. The separately implemented C++ checker constructs the adjacency matrix using exact 128-bit products with adjusted square roots and rechecks all triangles and pair overlaps. Expected output contains `vertices=3125`, `edges=14856`, `triangles=288`, `primitive_types=2`, `isolated=174`, `overlap_pairs=57`, and `packing=231` (the Python output gives more detailed labels). No input data files, external packages, or unprovided computations are needed.

## Relationship to prior work

Xiao [1] introduces the prime-power boxes and the associated two-leg Pythagorean independence problem, proving an asymptotic density bound rather than the present exact three-clique and intersection classification. Knill [2] studies the full Babylonian graph on positive integers, identifies triangles with Euler bricks, and explicitly lists both primitive bricks occurring here; that graph and those two bricks are prior art. OEIS A239618 [3] counts primitive Euler bricks by a different coordinate-size cutoff. A public enumeration [4] lists bricks with largest side at most ten million. Neither the inspected source statements nor that bounded enumeration give the exact count, scale law, intersection graph, packing number, or transversal number in the exponent-restricted \(\Phi_5\). The older exact first-four-box independence computations, including the previously known triangle witness at the fifth box, do not imply this classification.

## Limitations

The result concerns only the fixed fifth box, not all boxes or all Euler bricks. The two primitive bricks and the triangle/brick correspondence are historical facts. The complete finite classification depends on executable exhaustive integer arithmetic; no short conceptual parametrization of *all* permitted primitive bricks is established independently of that enumeration. The independence number \(f(5)\) is not computed; the triangle invariants are not asserted to strengthen existing independence bounds. Older unpublished or unindexed exhaustive datasets might imply the same finite enumeration; this remains a literature risk.

## References

[1] Rongzhong Xiao, *Pythagorean pairs in boxes of prime powers*, arXiv:2610.11965v1, 8 October 2026, https://arxiv.org/pdf/2610.11965.

[2] Oliver Knill, *The Babylonian Graph*, arXiv:2205.13285 (2022); full text also accessible at https://www.researchgate.net/publication/360888170_The_Babylonian_Graph.

[3] OEIS A239618, *Number of primitive Euler bricks with side length a < b < c < 10^n*, https://oeis.org/A239618.

[4] T. Grothmann, *List of Euler-Bricks*, finite database of bricks with largest side at most ten million, https://github.com/TobiasGrothmann/list-of-euler-bricks.
