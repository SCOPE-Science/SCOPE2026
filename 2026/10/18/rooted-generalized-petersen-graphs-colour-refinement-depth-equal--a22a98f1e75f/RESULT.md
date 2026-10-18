# Rooted generalized Petersen graphs: colour-refinement depth equals eccentricity

## Finding
For every integer \(n\ge14\), let \(P_n\) be the cubic generalized Petersen graph \(G(n,2)\), defined below, and distinguish just one outer vertex \(u_0\) by a unique initial colour. Run synchronous, counting one-dimensional colour refinement, retaining old colours in every signature. The first stable partition occurs after exactly
\[
R(n)=2+\left\lceil\frac{\lfloor n/2\rfloor}{2}\right\rceil
=\left\lfloor\frac{n+10}{4}\right\rfloor
\]
strict refinement rounds. It consists of the separate reflection orbits
\[
U_j=\{u_j,u_{-j}\},\qquad V_j=\{v_j,v_{-j}\},\qquad
0\le j\le \lfloor n/2\rfloor,
\]
with repeated elements counted once. Consequently it is exactly the orbit partition of the full automorphism group fixing \(u_0\), and has \(2\lfloor n/2\rfloor+2\) cells. Moreover \(R(n)\) equals the graph eccentricity of \(u_0\).

There is an explicit wavefront description. Put \(h=\lfloor n/2\rfloor\). For \(n\ge26\) and each integer \(r\) with \(6\le r\le R(n)-2\), let \(a=2r-4\). The round-\(r\) cells are precisely the individual orbits \(U_0,\ldots,U_{a-1}\), the individual orbits \(V_0,\ldots,V_a\), and two remaining cells
\[
C_r=U_a\cup V_{a+1}\cup V_{a+2},\qquad
T_r=\bigcup_{j=a+1}^{h} U_j\ \cup\!\bigcup_{j=a+3}^{h}V_j.
\]
Empty index ranges contribute nothing. In particular, each interior round advances the fully resolved outer frontier by two indices while retaining a three-orbit leading collision. A four-case description of the last nonstable round is proved below.

## Assumptions and scope
The graph has vertices \(u_i,v_i\), where \(i\in\mathbb Z/n\mathbb Z\), and edges \(u_i u_{i+1}\), \(u_i v_i\), and \(v_i v_{i+2}\). For \(n\ge14\) these define a simple cubic graph. Initially \(u_0\) alone has one colour; every other vertex shares another colour. Round zero is the initial colouring. The next colour is the ordered pair of the current colour and the multiset of all three neighbour colours. The depth counts strict partition changes, not the final comparison that detects stabilization. No markings on inner vertices and no other generalized-Petersen parameter are considered.

Reflection \(i\mapsto-i\) simultaneously on both vertex layers is an automorphism fixing \(u_0\). Thus every colouring cell must be a union of the displayed \(U_j,V_j\). Write \(\phi_n(t)=\min(t\bmod n,(-t)\bmod n)\), taking representatives in \(\{0,\ldots,n-1\}\). Neighbour multisets on the reflection-orbit quotient, with multiplicities, are exactly
\[
\begin{aligned}
N(U_j)&=\{U_{\phi_n(j-1)},U_{\phi_n(j+1)},V_j\},\\
N(V_j)&=\{V_{\phi_n(j-2)},V_{\phi_n(j+2)},U_j\}.
\end{aligned}
\tag{1}
\]
These formulas remain valid at endpoints: if two neighbours lie in the same orbit, that orbit occurs twice in the multiset. They give a finite, weighted, pathlike quotient on \(2h+2\) orbit names and are used for every computation below.

## Proof
**Six-round initialization.** Applying equation (1) to the two initial colours gives the following successive proper cells away from the unresolved tail; commas separate classes, and braces within a class indicate a union of reflection orbits. These formulas are valid for every \(n\ge26\), because every orbit index touched by these six updates is at most ten, whereas the folded boundary is at least thirteen:

* Round 0: \(U_0\); all others together.
* Round 1: \(U_0\), \(\{U_1,V_0\}\); the tail.
* Round 2: the preceding non-tail cells and \(\{U_2,V_1,V_2\}\); the tail.
* Round 3: the preceding non-tail cells and \(\{U_3,V_3,V_4\}\); the tail.
* Round 4: \(U_0\), \(\{U_1,V_0\}\), \(\{U_2,V_1,V_2\}\), \(\{U_3,V_3\}\), \(U_4\), \(V_4\), \(\{V_5,V_6\}\); the tail.
* Round 5: \(U_0\), \(\{U_1,V_0\}\), \(\{U_2,V_1\}\), the separate \(U_3,U_4,U_5\), the separate \(V_2,V_3,V_4,V_5,V_6\), \(\{U_6,V_7,V_8\}\); the tail.
* Round 6: the separate \(U_0,\ldots,U_7\) and \(V_0,\ldots,V_8\), the class \(\{U_8,V_9,V_{10}\}\), and the tail formed by all \(U_j\) with \(j\ge9\) and all \(V_j\) with \(j\ge11\).

Each line is obtained by taking, for every displayed orbit, its old cell label and the three labels from (1); no degree-normalization or unweighted quotient approximation is used. In the first four lines every not-yet-listed orbit shares a single tail colour. The sixth-round line is precisely the wavefront formula with \(a=8\).

**Interior induction.** Assume the wavefront formula at round \(r\), where \(6\le r\le R(n)-3\), and put \(a=2r-4\). Previously resolved individual orbits cannot merge because each new signature retains its old colour. Within the old class \(C_r\), the three constituents have distinct neighbours among already individual orbits:
\[
U_a:\ U_{a-1}\text{ and }V_a;\quad
V_{a+1}:\ V_{a-1};\quad
V_{a+2}:\ V_a.
\]
Thus they split into three separate cells. Within the old tail \(T_r\), the respective numbers of neighbours belonging to \(C_r\) are
\[
\begin{array}{c|cccc|c}
\text{orbit}&U_{a+1}&U_{a+2}&V_{a+3}&V_{a+4}&\text{every other tail orbit}\\\hline
\#\,N(\cdot)\cap C_r&2&1&1&1&0.
\end{array}
\tag{2}
\]
The three orbits with count one have identical new signatures (one neighbour in \(C_r\), two in \(T_r\)); the orbit with count two is distinguished, and the remaining tail stays homogeneous. The folded-neighbour formula (1) proves (2) also at the right-hand boundary: in the allowed range \(r\le R(n)-3\), reflected edges cannot enter \(C_r\) from any other tail orbit. For the tightest two residue classes \(n\equiv2,3\pmod4\), the near-antipodal orbit \(V_{a+4}\) is indeed one of the three listed count-one orbits, not an extra exception. The resulting cells are exactly \(C_{r+1},T_{r+1}\) and the individually resolved \(U_0,\ldots,U_{a+1}\) and \(V_0,\ldots,V_{a+2}\). This proves the asserted wavefront formula by induction through round \(R(n)-2\).

**The antipodal seam and sharpness.** Set \(r=R(n)-1\). From the wavefront at \(r-1\), substitute the folded indices from (1). Every cell at round \(r\) is one orbit except for the following *complete* list of merged cells, where \(h=\lfloor n/2\rfloor\):
\[
\begin{array}{c|l}
n\bmod4&\text{unresolved cells at round }R(n)-1\\\hline
0& U_{h-3}\cup V_h;\ U_{h-2}\cup V_{h-1};\ U_{h-1}\cup U_h\\
1& U_{h-2}\cup V_{h-1}\cup V_h;\ U_{h-1}\cup U_h\\
2& U_{h-2}\cup V_h\\
3& U_{h-2}\cup V_h.
\end{array}
\tag{3}
\]
For instance, in residue zero the two neighbours of \(V_h\) on its own layer both belong to \(V_{h-2}\), while \(U_{h-3}\) has two neighbours in the former front class; hence their old counting signatures coincide. The other entries follow by the same two-step index folding, with all unlisted orbits identified separately. Formula (3) is an explicit local check on the at-most-six orbit names adjacent to \(h\); it is independent of the length of the already resolved prefix.

In the next round all displayed collisions split. For residue zero, the members of the first pair have different neighbours in the singleton cells \(U_{h-4}\) and \(V_{h-2}\); the second pair has different singleton neighbours \(V_{h-2}\) and \(V_{h-3}\); and the third pair has different numbers of neighbours in its own old cell. For residue one, the three members of the first collision have respectively distinguishable singleton neighbours \(U_{h-3}\), \(V_{h-3}\), and \(V_{h-2}\), while the final pair has different counts into its own old cell. For residues two and three, \(U_{h-2}\) is adjacent to singleton \(U_{h-3}\), whereas \(V_h\) is not. Thus round \(R(n)\) resolves every \(U_j,V_j\), and at least one nontrivial collision at round \(R(n)-1\) proves sharpness.

The above induction starts at round six when \(n\ge26\). For the twelve remaining integers \(14\le n\le25\), exhaustive application of (1) (or direct application on the cubic graph) gives depth six for \(14\le n\le17\), seven for \(18\le n\le21\), and eight for \(22\le n\le25\); in each case the final classes are exactly the \(U_j,V_j\) and the preceding round contains a collision. The complete executable finite calculation is included as `verify_graph.py` and independently as `verify_quotient.py`, with no untested isomorphism assumptions.

**Orbits and eccentricity.** The reflection automorphism makes each \(U_j,V_j\) a subset of some marked-graph automorphism orbit. Conversely all colour classes are invariant under any colour-preserving automorphism, so the final orbit-sized cells force equality with the full pointwise-stabilizer orbit partition, without needing an external automorphism classification.

Shortest-path analysis gives, for \(0\le j\le h\),
\[
\operatorname{dist}(u_0,u_j)=\min\{j,\ 2+\lceil j/2\rceil\},\qquad
\operatorname{dist}(u_0,v_j)=1+\lceil j/2\rceil.
\]
Indeed outer edges change cyclic coordinate by one, inner edges by two, and spokes switch layers; the displayed costs are realized by paths with zero, one, or two spokes. Extra layer switches cannot improve them. Taking the maximum at \(j=h\), and using \(h\ge7\), gives eccentricity \(2+\lceil h/2\rceil\), exactly \(R(n)\).

## Verification
The included `verify_graph.py` constructs every cubic graph directly from its edges, runs colour refinement from the single marked vertex, checks orbit classes and root distances, and performs an exact all-case check for each \(14\le n\le300\). The separately implemented `verify_quotient.py` iterates the multiplicity-weighted reflected quotient (1), checks the interior wavefront, checks all four seam patterns, and confirms the asserted depth for \(14\le n\le500\). Both reproduce the accompanying plain-text outputs. These independent finite tests are corroboration; the induction and seam argument above establish the unbounded theorem.

## Relationship to prior work
Frucht, Graver and Watkins classified automorphism groups of generalized Petersen graphs, and Conder, Pisanski and Žitnik extended this framework to GI-graphs. Their results supply graph-family and symmetry context, not refinement-depth formulas. Arvind, Köbler, Rattan and Verbitsky analyze colour refinement, orbit refinability, compactness and Johnson graphs; their inspected results do not specialize to the present rooted generalized-Petersen wavefront. Kiefer and McKay study worst-case refinement iteration numbers but do not give this family's exact rooted depth. Kluge's circulant-graph work studies a different graph class and primarily a different (two-dimensional) refinement process. The present contribution is the exact one-dimensional, one-mark, all-parameter wavefront and its equality with eccentricity.

## Limitations
The theorem does not show that unmarked graphs are identified up to isomorphism, does not cover arbitrary choices or numbers of marked vertices, and does not extend to \(G(n,k)\) for \(k\ne2\). The claim of literature originality is a bounded comparison, not proof of publication priority; an unlocated specialized treatment of rooted generalized Petersen graphs could subsume it. The accompanying finite programs do not establish the infinite statement without the proof above.

## References
1. M. D. E. Conder, T. Pisanski and A. Žitnik, *GI-graphs and their groups*, arXiv:1207.2752, first posted 11 July 2012, https://arxiv.org/abs/1207.2752.
2. V. Arvind, J. Köbler, G. Rattan and O. Verbitsky, *Graph Isomorphism, Color Refinement, and Compactness*, arXiv:1502.01255, first posted 4 February 2015, https://arxiv.org/abs/1502.01255.
3. S. Kiefer and B. D. McKay, *The Iteration Number of Colour Refinement*, arXiv:2005.10182, first posted 20 May 2020, https://arxiv.org/abs/2005.10182.
4. L. Kluge, *Combinatorial refinement on circulant graphs*, arXiv:2204.01054, first posted 3 April 2022, https://arxiv.org/abs/2204.01054.
