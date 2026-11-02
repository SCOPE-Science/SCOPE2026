# Exact proportional choice numbers for graphs of maximum degree two on at most six vertices

## Finding

**Theorem.** Let \(G\) be a nonempty finite simple graph with \(|V(G)|\le 6\) and maximum degree \(\Delta(G)\le 2\). Then \(G\) is proportionally \(3\)-choosable. More precisely, its proportional choice number is
\[
\chi_{\mathrm{pc}}(G)=\begin{cases}
1,&E(G)=\varnothing,\\
2,&E(G)\ne\varnothing\text{ and }G\text{ is a linear forest whose largest component has}\le5\text{ vertices and all other components have}\le2,\\
3,&\text{otherwise}.
\end{cases}
\]
In particular, \(\chi_{\mathrm{pc}}(P_6)=3\) and \(\chi_{\mathrm{pc}}(C_6)=3\). The upper bound is proved by a finite, exhaustive canonical-list enumeration, with the checker provided as complete source code.

## Assumptions and scope

All graphs are finite and simple. A \(k\)-assignment \(L\) gives each vertex \(v\) exactly \(k\) **distinct** allowed colors. For a color \(c\), let \(\eta_L(c)=|\{v:c\in L(v)\}|\). A proportional \(L\)-coloring is a proper coloring \(f\) with \(f(v)\in L(v)\) such that \(|f^{-1}(c)|\) belongs to \(\{\lfloor\eta_L(c)/k\rfloor,\lceil\eta_L(c)/k\rceil\}\) for every available color. The proportional choice number \(\chi_{\mathrm{pc}}(G)\) is the least \(k\ge1\) such that every \(k\)-assignment admits a proportional coloring. This is the unrestricted-palette definition: the total number of colors may vary between \(3\) and \(18\) in the six-vertex computation.

The theorem concerns only nonempty graphs of order at most six and maximum degree at most two. It neither asserts proportional \(3\)-choosability of longer paths nor provides a general three-color theorem for all graphs of maximum degree two.

## Proof

**1. Four maximal six-vertex graphs suffice.** Every six-vertex graph of maximum degree at most two is a subgraph (on the same labelled vertex set, after relabelling) of one of
\[
C_6,\qquad C_3\sqcup C_3,\qquad C_4\sqcup K_2,\qquad C_5\sqcup K_1.
\]
Indeed, if a component is a triangle, the remaining three vertices induce a maximum-degree-two graph and can be completed to a triangle. A four- or five-cycle likewise leaves at most two or one vertices. Otherwise the graph is a forest of paths, or is the six-cycle itself; concatenate its path components around six positions and add connecting edges to obtain a six-cycle. The subgraph-monotonicity of proportional \(k\)-choosability is Proposition 3 in Mudrock (2026), also established in the foundational literature. Therefore it suffices to prove that all four displayed graphs are proportionally \(3\)-choosable. For a graph on fewer than six vertices, adjoin isolated vertices first and then apply subgraph-monotonicity.

**2. Canonical encoding exhausts arbitrary palettes.** Fix six labelled vertices \(V=\{0,1,2,3,4,5\}\). Each available color \(c\) has a unique, nonempty *incidence support* \(S_c=\{v:c\in L(v)\}\subseteq V\). Up to a bijection of color names, the assignment is specified by exactly one vector \((f_S)_{\varnothing\ne S\subseteq V}\) of nonnegative integers, where \(f_S\) counts colors having incidence support \(S\). Each vertex has three allowed colors exactly when
\[
\sum_{S\ni v}f_S=3\quad(v\in V).
\]
The source checker enumerates all such vectors by iterating over the \(63\) nonempty masks \(S\) in increasing order and choosing \(f_S\) between zero and the least residual list capacity among vertices in \(S\). A branch is complete if and only if all six residual capacities vanish after the last mask. Consequently, every unrestricted-palette \(3\)-assignment occurs, up to renaming, **exactly once**. There are exactly \(2{,}406{,}208\) such vectors. The last integer is independently reproduced by the separate memoized recurrence in `verify_support_count.py`.

**3. Exhaustive, logically exact feasibility test.** Given an enumerated incidence vector, `verify_degree2_six.cpp` constructs a separate color identifier for every copy of each support \(S\), puts that identifier in the three lists of exactly the vertices in \(S\), and assigns its lower/upper permitted use counts
\[
\ell_c=\left\lfloor\frac{|S_c|}{3}\right\rfloor,
\qquad u_c=\left\lceil\frac{|S_c|}{3}\right\rceil.
\]
For each of the four maximal graphs, the verifier performs depth-first search over **all** choices of a color from the current vertex's list. It rejects a choice only when it repeats a color on an already colored neighbor, would exceed \(u_c\), or makes some \(\ell_c\) impossible because too few remaining vertices even have that color in their list. Each rejection is therefore a necessary-condition failure. The recursion returns success only after coloring all six vertices and checking that every use count is at least \(\ell_c\). Upper counts and properness have already been enforced at each extension. Thus success gives a valid proportional coloring, while no valid coloring can be erroneously pruned.

The complete checker terminates normally and prints `PASS` on **all \(2{,}406{,}208\)** incidence vectors for each of the four graphs: \(9{,}624{,}832\) checked graph–list combinations in total, followed by `VERIFY_OK`. Every \(3\)-assignment on each maximal graph is consequently feasible. By Step 1, the upper bound \(\chi_{\mathrm{pc}}(G)\le3\) follows for all graphs in the theorem. Because six vertices bound both the number of support types and the total palette size, this is a valid finite exhaustive proof of the stated finite-order theorem, rather than an extrapolation from samples.

**4. Exact choice numbers.** An edgeless nonempty graph has proportional choice number \(1\): assigning to every vertex its unique allowed color yields the required multiplicities, with no adjacency constraints. A graph with an edge is not proportionally \(1\)-choosable, since assigning the same singleton color to its two endpoints defeats any proper coloring. The complete characterization of proportionally \(2\)-choosable graphs by Kaul, Mudrock, Pelsmajer, and Reiniger (2018/2020) says that these are precisely the linear forests whose largest component has at most five vertices and every other component has at most two vertices. Combining that classification with the proved \(3\)-color upper bound gives the three cases stated above. In particular, the six-vertex path fails the \(2\)-color characterization and has choice number exactly three; the six-cycle is not a forest and also has choice number exactly three.

## Verification

The two standalone checkers in this package can be run using:

```sh
g++ -O3 -std=c++17 verify_degree2_six.cpp -o verify_degree2_six
./verify_degree2_six
python3 verify_support_count.py
```

Expected terminal lines (the graph names are labels, not additional hypotheses):

```text
PASS C6 canonical_color_list_types=2406208
PASS C3+C3 canonical_color_list_types=2406208
PASS C4+K2 canonical_color_list_types=2406208
PASS C5+K1 canonical_color_list_types=2406208
VERIFY_OK
INDEPENDENT_SUPPORT_COUNT_OK 2406208
```

The first checker verifies actual existence of proportional list-colorings for every canonical assignment; the second independently counts the canonical assignments by a different dynamic-programming implementation. The finite search has complete quantified coverage because of the support-multiplicity bijection above. This proof does not resolve the infinite path conjecture.

## Relationship to prior work

Mudrock, *Improved Bounds on Proportional Choice Numbers*, arXiv:2610.33914v1 (first posted 2026-10-24), proves \(\chi_{\mathrm{pc}}(G)\le2^{\chi'(G)}\), giving \(\chi_{\mathrm{pc}}(P_n)\le4\), and formulates as Conjecture 11 the stronger \(\chi_{\mathrm{pc}}(P_n)=3\) for all \(n\ge6\). This theorem confirms the first still-open path length and more generally all graphs on at most six vertices of maximum degree at most two; it does not claim Mudrock's general upper bound or the whole conjecture.

Kaul, Mudrock, Pelsmajer and Reiniger, *A Simple Characterization of Proportionally 2-choosable Graphs*, arXiv:1806.11265v1 (first posted 2018-06-29; later published 2020), supplies the \(2\)-choosability characterization used to derive exact choice numbers, but no corresponding \(3\)-choosability classification. Other exact results for prescribed ordinary color-class sizes in degree-two graphs do not impose the per-vertex color availability constraints present here. Searches in mathematical-result records and the relevant literature have not identified an earlier theorem with this unrestricted-palette six-vertex assertion; this is not a claim of exhaustive historical priority.

## Limitations

The result is an **exact finite-order** classification, established by a reproducible exhaustive checker with finite source code. It does not give a purely short pencil-and-paper proof of the main six-vertex upper bound. It does not establish \(\chi_{\mathrm{pc}}(P_n)=3\) for \(n\ge7\), does not prove \(\chi_{\mathrm{pc}}(G)\le3\) for every degree-two graph of larger order, and is consistent with Mudrock's 12-vertex example of a degree-two graph having proportional choice number four. Source comparison and independent mathematical validation may reveal additional priority or correctness issues not resolved by the supplied self-review.

## References

1. J. A. Mudrock, *Improved Bounds on Proportional Choice Numbers*, arXiv:2610.33914v1 (2026-10-24), https://arxiv.org/abs/2610.33914; esp. Propositions 2–3, Theorem 4, Theorem 10, Conjecture 11 and Theorem 12.
2. H. Kaul, J. A. Mudrock, M. J. Pelsmajer, and B. Reiniger, *A Simple Characterization of Proportionally 2-choosable Graphs*, arXiv:1806.11265v1 (2018-06-29), https://arxiv.org/abs/1806.11265.
