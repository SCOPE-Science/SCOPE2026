# Review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

The proof has two matching parts. For the lower bound, every pendant support is forced into every IO-code by its leaf. The remaining vertices partition into \(p=|V(H)|\) sets \(B_v\) of size \(\Delta+1\), one per skeleton vertex. Any two vertices in the same \(B_v\) are incompatible omissions: either they are the entire neighborhood of a degree-two vertex, violating total domination if both are omitted, or they form the symmetric difference of the neighborhoods of two vertices, violating separation if both are omitted. Hence at most one vertex can be omitted from each \(B_v\), giving \(\gamma^{\mathrm{IOC}}\ge n-p\).

For the upper bound, delete precisely the original skeleton vertices. The remaining graph is a disjoint union of matching edges between each pendant support and its leaf and between each pair of subdivision vertices replacing a skeleton edge. Every noncenter therefore has a distinct singleton trace. Every center has a trace of size exactly \(\Delta\ge3\), and different centers have different neighbor sets. This is an IO-code of size \(n-p\). The order count and the specializations to cycle and path skeletons then follow algebraically.

The structural hypotheses have also been checked directly. Every center has degree \(\Delta\), while every new vertex has degree at most two. The graph is open-twin-free by vertex type and unique local labels. Every cycle lies in the twice-subdivided skeleton core, so its length is three times a skeleton-cycle length and in particular cannot be four.

A finite exact check independently solves the IO-code binary optimization problem for 79 lifted graphs arising from every connected Graph Atlas skeleton on two through five vertices and \(\Delta\in\{3,4,5\}\) when allowed by the degree bound. All instances match the theorem. This supports but is not used in the general proof.

## Originality

The result is assessed as original only to the best of our knowledge. The closest source is Chakraborty--Foucaud--Henning (Discrete Applied Mathematics 386, 2026), which proves the general \((2\Delta-1)/(2\Delta)\) upper bound for open-twin-free \(C_4\)-free graphs of maximum degree at most \(\Delta\). For \(\Delta\ge4\), its concluding section explicitly leaves the large-order tightness question open, reports a construction of density \((2\Delta-4)/(2\Delta-3)\) and a slight refinement, and suggests density \((2\Delta-3)/(2\Delta-2)\) as a desirable improvement. The present cycle-skeleton density \((2\Delta-2)/(2\Delta-1)\) is strictly larger, while path skeletons provide a tree realization converging to the same constant.

Earlier literature was checked under the equivalent OLD/open-neighborhood-locating-dominating terminology as well as identifying-open-code terminology. Chellali--Jafari Rad--Seo--Slater (2014) proves several OLD extremal characterizations and a packing bound for minimum-degree-at-least-three \(C_4\)-free graphs; that theorem does not apply to the present leaf-rich family. Searches for subdivision, double subdivision, twice-subdivided graphs, maximum-degree constructions, OLD trees, and the exact density did not locate the skeleton-lift theorem or its corollaries. No later paper resolving the 2026 construction direction was located in the checked literature.

The principal residual risk is older tree literature using a different construction language. The complete theorem texts of Seo--Slater, *Open neighborhood locating-dominating in trees* (2011, DOI 10.1016/j.dam.2010.12.010), and *Open Locating-Dominating Interpolation for Trees* (Congressus Numerantium 215, 2014) were not both inspected end to end. Available descriptions concern general tree bounds, extremal values, and interpolation. The fact that the 2026 paper cites this literature while still posing the bounded-degree construction gap is evidence against direct coverage, but does not eliminate the possibility of an equivalent unindexed construction.

## Value

The theorem supplies a general exact mechanism rather than one isolated example. It assigns an explicit IO-code number to a lift of every connected skeleton of degree at most \(\Delta\), and the simplest skeletons materially strengthen the best construction benchmark in the recent bounded-degree problem. For every \(\Delta\ge4\), it raises the asymptotic lower construction density to \((2\Delta-2)/(2\Delta-1)\), leaving a gap of only \(1/[2\Delta(2\Delta-1)]\) to the known upper bound. The path specialization shows that the improvement already occurs within trees.

## Limitations

The exact asymptotic extremal constant remains unknown. The construction does not show that the upper bound \((2\Delta-1)/(2\Delta)\) is asymptotically sharp, nor does it classify extremal graphs. For \(\Delta=3\), previously known families attaining density \(5/6\) are stronger than this construction's limiting density \(4/5\). Originality remains subject to the older-tree-literature risk described above.
