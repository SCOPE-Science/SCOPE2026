# Distance-three packing polynomials and exact three-capacities of Möbius ladders

## Finding

Let \(m\ge5\). The labelled Möbius ladder \(M_{2m}\) has vertex set \(\mathbb Z/(2m)\mathbb Z\) and edges joining \(i\) to \(i-1\), \(i+1\), and \(i+m\). A **distance-three packing** is a set \(S\) in which any two distinct vertices have graph distance at least three. Let \(p_{m,t}\) count the labelled distance-three packings of cardinality \(t\).

The **complete packing polynomial** \(P_m(z)=\sum_{t\ge0}p_{m,t}z^t\) has \(p_{m,0}=1\), and for every integer \(t\ge1\):

\[
p_{m,t}=\begin{cases}
0,&2t>m,\\
4,&2t=m\text{ and }t\text{ odd},\\
0,&2t=m\text{ and }t\text{ even},\\
\displaystyle\frac mt\sum_{r=1}^{\min(t,m-2t)}
\binom tr\binom{m-2t-1}{r-1}2^r,&2t<m.
\end{cases}
\]

In particular, the maximum packing cardinality and the number \(B_m\) of labelled maximum packings are

\[
\rho_2(M_{2m})=\begin{cases}
m/2-1,&m\equiv0\pmod4,\\
\lfloor m/2\rfloor,&m\not\equiv0\pmod4,
\end{cases}
\qquad
B_m=\begin{cases}
m(m-2),&m\equiv0\pmod4,\\
4,&m\equiv2\pmod4,\\
2m,&m\text{ odd}.
\end{cases}
\]

For the direct and strong distance-three capacities of Grašič–Mouron–Šubašić–Taranenko–Vojković (defined using traversing tours of all vertices),

\[
\operatorname{cap}_{\times,3}(M_{2m})=
\operatorname{cap}_{\boxtimes,3}(M_{2m})=
\rho_2(M_{2m}).
\]

Every labelled maximum packing is an initial configuration of an optimal direct tour in which all participants rotate one step clockwise at every time. The minimum interparticipant distance on such a tour is exactly three, not merely at least three.

## Assumptions and scope

All graphs are finite, simple, and undirected. Vertices are labelled by residues modulo \(2m\); two packings that differ by a graph automorphism still count separately unless they are the same labelled vertex subset. The parameter \(\rho_2\) uses the standard convention that pairwise distances in a 2-packing are strictly greater than two. A direct tour consists of synchronous adjacent-vertex moves, one per participant per time step; a strong tour also permits stays. Each participant's finite walk must visit all vertices. The distance-three capacity is the maximum participant count for which the minimum pairwise distance across the tour is exactly three. Our statement assumes \(m\ge5\), so no exceptional small-ladder conventions are needed.

## Proof

**1. Rung reduction and local constraints.** Partition the vertices into the \(m\) antipodal rung classes \(R_i=\{i,i+m\}\), indexed by \(i\in\mathbb Z/m\mathbb Z\). Two selected vertices cannot belong to the same rung (distance one), and two selected rung classes cannot be adjacent on the quotient cycle: for either choice of lifts, the two vertices have graph distance at most two, using at most one rung and one cycle edge. Thus the selected rung classes are a \(t\)-subset of the quotient cycle with each cyclic spacing at least two; necessarily \(2t\le m\).

For two selected rung classes at cyclic spacing exactly two, the selected lifted vertices must use **opposite sides of the two-step arc**: using the same side gives a length-two path along the outer cycle, whereas opposite sides have distance exactly three (one rung and two outer edges). When the spacing exceeds two, it causes no distance-below-three obstruction. These are all restrictions: any two selected classes not consecutive in the cyclic order of chosen classes lie at cyclic quotient distance at least four along either arc of chosen classes, so they cannot have a graph path of at most two edges. This is valid for \(m\ge5\); when only two classes are selected, both complementary spacings are among the displayed cyclic gaps, and the same conclusion holds. In particular, the full packing problem is exactly the binary-lift assignment problem with one required reversal across each spacing-two gap.

**2. Cyclic gap count.** Fix a nonempty selected rung set and mark one selected class. Read the cyclic spacings \(g_1,\ldots,g_t\ge2\) clockwise, with \(\sum_i g_i=m\). Write \(L=m-2t\). If \(L>0\), let \(r\) be the number of spacings \(g_i>2\). There are \(\binom tr\) choices of their positions and \(\binom{L-1}{r-1}\) ways to distribute the \(L\) positive excess units. Every spacing-two constraint forces a reversal of the two possible lifts. The \(r\) wider spacings break the cyclic constraint system into exactly \(r\) chains, leaving \(2^r\) independent binary choices for their starting lifts. This remains true across the Möbius twist because at least one constraint edge is absent. A marked initial rung class has \(m\) choices, while each actual packing has exactly \(t\) possible marked selected classes. Hence its count is the displayed factor \(m/t\) times the sum over \(r\).

If \(L=0\), all cyclic gaps are two, so the selected classes are exactly one of the two alternating subsets of the \(m\)-cycle. Traversing one complete circuit of quotient rung classes changes the lifted side once due to the Möbius twist. The \(t\) spacing-two constraints also change side \(t\) times. They are consistent precisely when \(t\) is odd, and then the first selected lift has two choices. Consequently there are \(2\cdot2=4\) packings if \(t\) is odd and none otherwise. This completes the polynomial formula, including the empty set separately.

**3. Maximum size and extremal multiplicity.** No size greater than \(\lfloor m/2\rfloor\) is possible. If \(m\) is odd, the top value \(t=(m-1)/2\) has \(L=1\), so exactly one wide gap and \(p_{m,t}=2m\). If \(m\equiv2\pmod4\), the top value \(t=m/2\) is odd, giving exactly four packings. If \(m\equiv0\pmod4\), the putative top value has \(t=m/2\) even and is impossible; the next value \(t=m/2-1\) has \(L=2\) and, since \(m\ge8\), \(t\ge3\). The cases of one spacing-four gap or two spacing-three gaps give respectively \(2m\) and \(m(m-4)\) packings, summing to \(m(m-2)\). All stated top coefficients are positive, so the bounds are attained.

**4. Tour capacity.** At every moment of any distance-three tour, occupied vertices form a distance-three packing, so either capacity is at most \(\rho_2\). Conversely, start with any maximum packing \(S=\{s_1,\ldots,s_k\}\) and move each participant by the explicit walk \(f_j(u)=s_j+u\pmod{2m}\) for \(u=0,\ldots,2m-1\). These are legal synchronous moves on cycle edges; every walk visits every vertex, and rotating all positions is a graph automorphism, so all pairwise distances are preserved. Every maximum packing in the three residue classes above includes at least one cyclic spacing-two gap: the gap surplus is respectively \(1\), \(0\), or \(2\), and the number of selected classes is at least two (at least three in the last case). Across a spacing-two gap, the selected lifts are at distance exactly three by Step 1. The resulting tour therefore has minimum separation **exactly** three, satisfying the original equality-based capacity definition. Thus a direct tour with \(k=\rho_2\) participants exists, and it also qualifies as a strong tour. Both capacities attain the packing bound. QED.

## Verification

Run `python3 mobius_pack_verify.py` with Python 3 and its standard library. The verifier constructs \(M_{2m}\) independently from its edge definition, builds every closed graph-radius-two neighborhood, and recursively counts independent sets in the resulting squared-graph conflict system by deletion and branching. It compares **all coefficients** with the closed formula, as well as both the maximum size and its exact multiplicity, for each integer \(5\le m\le24\). The replay completed with the marker `VERIFY_OK m=5..24 all polynomial coefficients, exact maxima, labelled optimum counts`. These finite tests corroborate but do not replace the four-step proof for all \(m\ge5\).

## Relationship to prior work

Grašič, Mouron, Šubašić, Taranenko, and Vojković [1] introduced the strong and direct distance-\(d\) capacities, analyzed paths and cycles, and bounded capacities for bipartite graphs. Their full text does not give the Möbius-ladder family or the distance-three packing polynomial. Goddard and Henning [2] give general cubic-graph packing bounds; such a bound does not count packings or imply the exact residue-class formulas here. MathWorld [3] records the **ordinary** independence polynomial of the Möbius ladder and identifies its square as a circulant graph; the ordinary polynomial is not the distance-three packing polynomial (the latter is the independence polynomial of the **square**). McSorley's earlier work [4] discusses exact enumeration of many Möbius-ladder structures; its full manuscript was not accessible for a decisive theorem-by-theorem comparison, so historical priority for all coefficients is not independently certified.

## Limitations

The theorem does not address the small ladders with \(m<5\), distance parameters other than three, Cartesian/patient-tour capacity, unlabelled orbit counts, or general twisted ladder graphs. As with any mathematical priority claim, undiscovered equivalent enumerations of the square-graph independence polynomial remain possible. The proof and verifier establish the stated combinatorial equalities, not priority relative to inaccessible literature.

## References

1. M. Grašič, C. Mouron, A. Šubašić, A. Taranenko, and T. Vojković, *Span capacities of graphs*, arXiv:2605.16852v1, publicly posted 2026-05-16. https://arxiv.org/abs/2605.16852 .
2. W. Goddard and M. A. Henning, *The packing number of cubic graphs*, Discrete Optimization 53 (2024), 100850. https://doi.org/10.1016/j.disopt.2024.100850 .
3. E. W. Weisstein, *Möbius Ladder*, MathWorld. https://mathworld.wolfram.com/MoebiusLadder.html .
4. J. P. McSorley, *Counting Structures in the Möbius Ladder*, Discrete Mathematics 184 (1998), 137–164. https://doi.org/10.1016/S0012-365X(97)00086-1 .
