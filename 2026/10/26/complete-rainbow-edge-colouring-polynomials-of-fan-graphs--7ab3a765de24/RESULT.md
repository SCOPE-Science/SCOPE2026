# Complete rainbow-edge-colouring polynomials of fan graphs

## Finding

Let \(F_n=K_1\vee P_n\) be the simple fan graph with a hub \(h\), path vertices \(v_1,\ldots,v_n\), spokes \(s_i=hv_i\), and rim edges \(e_i=v_iv_{i+1}\). Let \(n\ge2\) be an integer. A \(B\)-edge-colouring is a proper edge-colouring in which every four-cycle is rainbow; a \(D\)-edge-colouring is a proper edge-colouring in which every (not necessarily induced) diamond, or \(K_4\) with one edge deleted, is rainbow. Colours are named from \(\{1,\ldots,q\}\), may go unused, and \(q\ge0\) is an integer. Let \(P_n(q)\) count these assignments.

**Theorem.** The two colouring notions agree on \(F_n\). For any integer \(q\ge0\),
\[
P_n(q)=(q)_n\sum_{\mathcal B\in\mathcal C_{n-1}}(-1)^{n-1-|\mathcal B|}\prod_{[a,b]\in\mathcal B}\bigl(q-w_n(a,b)\bigr),
\]
where \(\mathcal C_{n-1}\) is the family of all partitions of the interval \(\{1,\ldots,n-1\}\) into consecutive nonempty blocks, \(|\mathcal B|\) is the number of blocks, \((q)_n=q(q-1)\cdots(q-n+1)\), and
\[
w_n(a,b)=\min\{n,b+2\}-\max\{1,a-1\}+1.
\]
This formula counts all named \(B\)- and \(D\)-colourings, not only optimal ones. It can be evaluated in \(O(n^2)\) arithmetic operations by the recurrence
\[
R_{n,0}(q)=1,\qquad R_{n,j}(q)=\sum_{a=1}^j(-1)^{j-a}\bigl(q-w_n(a,j)\bigr)R_{n,a-1}(q),\quad1\le j<n,
\]
with \(P_n(q)=(q)_nR_{n,n-1}(q)\).

The minimum palette is
\[
\boxed{q_B(F_n)=\chi'_D(F_n)=\begin{cases}3,&n=2,\\5,&3\le n\le5,\\n,&n\ge6.\end{cases}}
\]
For \(n=2,3,4,5\), there is exactly one optimal colouring up to permutations of colour names. For every \(n\ge6\), there are at least two inequivalent optimal colourings. For \(n\ge5\), the exact number of optimal colourings up to permutations of colours is \(R_{n,n-1}(n)\), and the number with \(n\) named colours is \(n!R_{n,n-1}(n)\). The first normalised optimum counts at \(n=5,6,7,8,9\) are respectively \(1,16,333,7040,162150\).

## Assumptions and scope

All graphs are finite and simple. A proper colouring makes all edges sharing an endpoint differently coloured. Four-cycles and diamonds are subgraphs, not necessarily induced. The polynomial counts functions from the edge set to a fixed, named \(q\)-colour palette, allowing unused colours. A colouring modulo colour permutations is an equivalence class under permutations of the entire palette; at the minimum palette in every case here, all colours are used. The theorem concerns the fan on one path of length \(n-1\), not arbitrary cones, books, wheels, or outerplanar graphs.

## Proof

**1. Reduction to local lists.** Every four-cycle of \(F_n\) consists of \(h\) and three consecutive path vertices \(v_i,v_{i+1},v_{i+2}\): removing \(h\) leaves a two-edge path, and the rim contains no cycle. Its chord \(hv_{i+1}\) makes it a diamond. In any proper colouring this chord already differs from each of the four perimeter edges. Thus rainbow diamonds and rainbow four-cycles impose precisely the same conditions on \(F_n\). The general implication \(B\Rightarrow D\) is standard; the reverse follows here because all four-cycles are chorded.

All \(n\) spokes share the hub, so their colours are pairwise distinct. If \(q\ge n\), fix an injection of spoke colours and rename its images \(1,\ldots,n\) in path order. There are \((q)_n\) possible injections and the number of permissible rim assignments does not depend on the injection. The only extra conflicts are between successive rim edges and between a rim edge \(e_i\) and spokes \(s_j\) with
\[
\max\{1,i-1\}\le j\le\min\{n,i+2\}.
\]
Indeed, the two possible diamonds containing \(e_i\) have path triples centred at \(i\) and \(i+1\); incidence accounts for the middle two spokes, while opposite-edge constraints supply the outer spokes. No diamond contains two nonconsecutive rim edges. Consequently, for fixed spoke colours \(s_j=j\), the allowed list of \(e_i\) is
\[
L_i=\{1,\ldots,q\}\setminus\{j:\max(1,i-1)\le j\le\min(n,i+2)\},
\]
and successive rim edges must receive different colours. This description is necessary and sufficient.

**2. Exact all-palette count.** Apply inclusion-exclusion to the \(n-2\) forbidden equalities between successive rim edge colours. Any chosen subset of these equalities contracts the sequence \(e_1,\ldots,e_{n-1}\) into consecutive blocks \([a_1,b_1],\ldots,[a_r,b_r]\). Its sign is \((-1)^{(n-1)-r}\), since exactly \((n-1)-r\) adjacencies were imposed. All rim edges in a block must take one common colour, of which there are
\[
\left|\bigcap_{i=a}^b L_i\right|=q-\left|\bigcup_{i=a}^b\{j:\max(1,i-1)\le j\le\min(n,i+2)\}\right|=q-w_n(a,b).
\]
The forbidden intervals overlap consecutively, and their union is exactly \([\max(1,a-1),\min(n,b+2)]\). Different blocks are independent before inclusion-exclusion. Summing signs and products proves the stated formula. Grouping compositions by their last block yields the recurrence. If \(q<n\), no proper colouring exists because the hub has degree \(n\), and the polynomial expression vanishes since \((q)_n=0\) for integral \(0\le q<n\).

**3. Sharp palette and rigid boundary.** For \(n=2\), \(F_2\) is a triangle and requires three colours. For \(n=3\), \(F_3\) is a diamond and all five edges require distinct colours. For \(n=4\), the middle rim edge \(e_2\) conflicts with all four distinct spokes, so at least five colours are required. The recurrence gives the exact low-order normalised polynomials
\[
R_{2,1}(q)=q-2,\quad R_{3,2}(q)=(q-3)(q-4),\quad R_{4,3}(q)=(q-4)^3,
\]
\[
R_{5,4}(q)=(q-4)^2(q^2-9q+21),\qquad R_{6,5}(q)=(q-5)(q-4)^2(q^2-9q+22).
\]
These show that \(q=5\) suffices for \(n=3,4\) and that \(n=5\) is already colourable with five colours. More generally, for every \(n\ge5\) colour the spokes with \(s_i=i\), give \(e_i\) colour \(i+3\) for \(1\le i\le n-3\), and give \(e_{n-2}\) and \(e_{n-1}\) colours \(1\) and \(2\), respectively. All choices lie outside their forbidden spoke intervals and consecutive rim colours differ. This gives an \(n\)-colouring, and the hub gives the matching lower bound.

At each of \(n=2,3,4,5\) the displayed normalised polynomial evaluates to \(1\) at the minimum palette after fixing all spoke colours; for \(n=2\) the minimum palette is three, leaving one possible rim colour. Thus each has one optimal colouring modulo names. For \(n\ge6\), modify the displayed \(n\)-colour construction only at \(e_1\), changing its colour from \(4\) to \(6\). This remains permissible because \(e_1\) sees only spokes \(s_1,s_2,s_3\) and neighbouring rim edge \(e_2\), which has colour \(5\). The changed and unchanged colourings cannot be equivalent under a colour permutation because their spoke colours were fixed individually. For \(n\ge5\), the spoke colours exhaust the minimum palette, so the normalised count equals the number modulo all colour-name permutations. This proves every assertion.

## Verification

The companion self-contained Python program `fan_rainbow_verify.py` constructs graph edges directly. It computes the \(D\)-conflict relation from pairs of disjoint edges and three or four cross-edges, and separately constructs \(B\)-conflicts by enumerating actual four-cycles. It independently counts completions of fixed spoke colours using the full conflict graph, the inclusion-exclusion formula, and a separate explicit-state rim dynamic program. All three counting methods agree in 20 direct graph cases, while inclusion-exclusion and the state dynamic program agree in 42 additional cases (62 comparisons altogether). It additionally validates explicit colourings for 75 fan orders and checks the first five optimum counts. Execution: `python3 fan_rainbow_verify.py`; expected completion line is `VERIFY_OK independent_cases=62 explicit_constructions=75`.

## Relationship to prior work

Wang (arXiv:2606.06831v1, first submitted 2026-06-05) introduced rainbow-diamond \(D\)-edge-colouring and general degree bounds. Hu, Kong and Wang (arXiv:2607.14837, 2026-07-16) explicitly noted that on chordal graphs \(D\)- and \(B\)-colourings coincide; this equivalence is *not* claimed as new here. Gyárfás, Martin, Ruszinkó and Sárközy (arXiv:2408.09059v2, Theorem 1.6) already gave \(q_B(K_4-e)=5\) and used the four-path-vertex fan as a sharpness witness for their outerplanar \(\Delta+1\) bound; these small cases are prior work. The present contribution is the explicit palette-sensitive polynomial and complete optimum census for the infinite fan family, including the previously unidentified \(n\ge5\) sharp palette and rigidity boundary. These specialized conclusions are not consequences of the stated general bounds or chordality observation.

## Limitations

This exact polynomial is for the path-cone family; the recurrence does not directly count coloured wheels or arbitrary outerplanar graphs. Computational tests sample finite cases, whereas the proof covers every integer \(n\ge2\), every integer \(q\ge0\), and all named assignments. The originality comparison is bounded by accessible published literature and indexed records; independent mathematical review and a comprehensive historical-priority assessment have not been performed.

## References

1. R. Wang, *Proper edge coloring with rainbow diamonds*, arXiv:2606.06831v1 (2026-06-05), https://arxiv.org/abs/2606.06831.
2. X. Hu, J. Kong, Y. Wang, *D-coloring of planar graphs*, arXiv:2607.14837 (2026-07-16), https://arxiv.org/abs/2607.14837.
3. A. Gyárfás, R. R. Martin, M. Ruszinkó, G. N. Sárközy, *Proper edge colorings of planar graphs with rainbow \(C_4\)-s*, arXiv:2408.09059v2, *Journal of Graph Theory* 107 (2024), 833–846, https://arxiv.org/abs/2408.09059.
