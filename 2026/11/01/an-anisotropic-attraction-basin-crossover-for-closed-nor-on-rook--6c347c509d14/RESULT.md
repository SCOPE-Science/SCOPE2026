# An anisotropic attraction-basin crossover for closed NOR on rook graphs

## Finding
For every pair of integers \(2\le a\le b\), consider synchronous, binary, **closed-neighborhood NOR** on the rook graph \(K_a\square K_b\). Every state becomes periodic after at most one update; there are no fixed states. The exact number of primitive two-cycle orbits is
\[
1+\frac{(2^a-2)(2^b-2)}2.
\]
All individual attraction basins are determined below. The unique largest basin belongs to the orbit alternating between the empty and full boards; its size is
\[
B_{a,b}=1+(2^b-1)^a+(2^a-1)^b-H(a,b),
\]
where \(H(r,c)\) counts \(r\)-by-\(c\) binary matrices with no zero rows or zero columns. In particular \(B_{a,b}>2^{ab-1}\) for all admitted dimensions.

Under uniformly independent initial bits, let \(\varepsilon_{a,b}=1-B_{a,b}/2^{ab}\) be the probability of reaching any *other* attractor. The sharp uniform estimate, as \(b\to\infty\) with \(2\le a\le b\), is
\[
\varepsilon_{a,b}\sim a2^{-b}\left[1-\left(1-2^{-(a-1)}\right)^b\right].
\]
Consequently, for fixed \(a\ge2\) the exceptional probability is asymptotic to \(a2^{-b}\); for square boards it is asymptotic to \(a^2 2^{-(2a-1)}\). When \(a\to\infty\) and \(b/2^{a-1}\to\lambda\in(0,\infty)\), the normalized ratio \(\varepsilon_{a,b}/(a2^{-b})\) tends to \(1-e^{-\lambda}\). The crossover occurs at the exponentially elongated aspect ratio \(b\asymp2^{a-1}\).

## Assumptions and scope
The rook graph has vertex set \([a]\times[b]\); distinct cells are adjacent when they share a row or column. A configuration is a subset \(S\subseteq[a]\times[b]\) of occupied cells. A cell is occupied after the next simultaneous update exactly when **all** cells in its closed neighborhood, including itself, are unoccupied. Denote the update by \(F\). A primitive two-cycle is an unordered pair of distinct configurations \(\{X,Y\}\) with \(F(X)=Y\) and \(F(Y)=X\). Its basin includes both cycle configurations and all transients ultimately entering the pair.

For \(S\), write \(R(S)\subseteq[a]\) and \(C(S)\subseteq[b]\) for its occupied row and column sets. For positive integers \(r,c\), define
\[
H(r,c)=\sum_{i=0}^r\sum_{j=0}^c (-1)^{i+j}\binom ri\binom cj 2^{(r-i)(c-j)}.
\]
The expression counts exactly the subsets of an \(r\)-by-\(c\) rectangle that visit every one of its rows and columns, by inclusion–exclusion.

## Proof
**Step 1: exact update.** The closed neighborhood of cell \((i,j)\) is its entire row and its entire column. It is empty of occupied cells precisely when \(i\notin R(S)\) and \(j\notin C(S)\). Thus, for every \(S\),
\[
F(S)=([a]\setminus R(S))\times([b]\setminus C(S)).\tag{1}
\]
If \(S\) is empty, (1) sends it to the full board and back. If \(R(S)=[a]\) or \(C(S)=[b]\), (1) sends \(S\) to the empty board and then to the full board. Otherwise, any nonempty \(S\) has nonempty, proper row and column projections \(A=R(S)\), \(B=C(S)\), and (1) gives
\[
S\longmapsto A^{\mathrm c}\times B^{\mathrm c}\longmapsto A\times B\longmapsto A^{\mathrm c}\times B^{\mathrm c}.
\]
Hence \(F^3=F\); all orbits enter a two-cycle by time one. The two rectangles of each cycle are disjoint and nonempty, so no fixed point exists. The sharpness of the one-update bound follows, for example, from an occupied full row with at least two rows in the board and at least two columns, which is not itself the full board.

**Step 2: cycles.** Apart from \(\{\varnothing,[a]\times[b]\}\), the recurrent states are precisely the rectangles \(A\times B\) with both \(A\) and \(B\) nonempty and proper. The involution \((A,B)\mapsto(A^{\mathrm c},B^{\mathrm c})\) has no fixed pair. There are therefore exactly \((2^a-2)(2^b-2)/2\) additional orbits. The total number of periodic configurations is \(2+(2^a-2)(2^b-2)\).

**Step 3: every basin.** A nonempty initial matrix with row and column projections exactly \(A,B\) enters the orbit \(\{A\times B,A^{\mathrm c}\times B^{\mathrm c}\}\). Its possible subsets number \(H(|A|,|B|)\). Interchanging \((A,B)\) and their complements gives another \(H(a-|A|,b-|B|)\) configurations, with disjoint projection classes. Thus that individual orbit has basin size
\[
H(|A|,|B|)+H(a-|A|,b-|B|).\tag{2}
\]
The distinguished orbit is reached exactly from the empty matrix or a nonempty matrix with all rows occupied or all columns occupied. Matrices with no empty rows number \((2^b-1)^a\), those with no empty columns number \((2^a-1)^b\), and the intersection has \(H(a,b)\) elements. This proves the formula for \(B_{a,b}\), including the otherwise exceptional empty matrix. Equations (1) and (2) partition all \(2^{ab}\) initial matrices into the stated basins. In the thin-board boundary case \(a=2\), every non-distinguished basin has size exactly two, giving the exact check \(B_{2,b}=2^{2b}-2^{b+1}+4\).

**Step 4: strict dominance.** Suppose \(a\le b\). A state outside the distinguished basin must have at least one entirely empty row. The probability of that event is at most \(a2^{-b}\le b2^{-b}\le1/2\). The first bound is strict for the exceptional event because the empty matrix has an empty row but belongs to the distinguished basin. Hence \(B_{a,b}>2^{ab-1}\). As all other basins together contain fewer than half the states, the distinguished orbit is uniquely largest.

**Step 5: anisotropic asymptotics.** Let \(E_i\) be the event that row \(i\) is all zero and *some* column is all zero under uniform independent initial bits. Non-distinguished behavior is exactly \(\bigcup_i E_i\) minus the empty matrix. Put \(q=2^{-(a-1)}\) and \(h=1-(1-q)^b\). Independence across columns gives
\[
\Pr(E_i)=2^{-b}h,
\quad\Pr(E_i\cap E_j)=2^{-2b}\{1-(1-2q)^b\}\quad(i\ne j).
\]
The function \(u\mapsto1-(1-u)^b\) is concave on \([0,1]\) and vanishes at zero, so \(1-(1-2q)^b\le2h\). First- and second-order Bonferroni bounds therefore yield
\[
a2^{-b}h-a(a-1)2^{-2b}h-2^{-ab}
\le\varepsilon_{a,b}\le a2^{-b}h-2^{-ab}.\tag{3}
\]
The relative Bonferroni error is at most \((a-1)2^{-b}\). Furthermore \(h\ge q\), so the relative empty-matrix correction is at most \(2^{-(a-1)(b-1)}/a\). Both tend uniformly to zero for \(2\le a\le b\) and \(b\to\infty\). This proves the uniform equivalent. With fixed \(a\), \(h\to1\). If \(a\to\infty\) with \(b/2^{a-1}\to0\), then \(h\sim b/2^{a-1}\), giving the square-board and more general balanced regime. If the ratio tends to a positive finite \(\lambda\), then \(h\to1-e^{-\lambda}\); if it diverges, \(h\to1\). This establishes the crossover statements.

## Verification
The proof applies to all \(2\le a\le b\); the finite tests below are corroboration, not a substitute. Running `python3 checks/check_direct.py` gives `DIRECT_OK total_states 169808`; it implements the closed-neighborhood rule cell by cell and enumerates nine labelled boards through \(4\times4\). Running `g++ -std=c++17 -O2 checks/check_projection.cpp -o check_projection && ./check_projection` gives `PROJECTION_OK total_states 1676112`; it independently updates via row/column projections and enumerates ten boards through \(4\times5\), checking every individual basin. Recorded outputs are in `checks/check_direct_output.txt` and `checks/check_projection_output.txt`. No external data are needed.

## Relationship to prior work
Aledo, Martínez and Valverde's 2015 survey describes general synchronous minterm/NOR periodicity, but not a rectangle-indexed attraction-basin classification or an aspect-ratio crossover. Aledo et al. (2020) give general periodic-point counting bounds and fixed-point formulas, not individual basins or asymptotic exceptional-basin probabilities. Aledo et al. (2012) directly study the general maxterm/minterm orbit structure; its full text was unavailable in the accessible sources, so exact historical overlap with that paper cannot be ruled out. The Smith and critical group results of Ducey, Gerhard and Watson (2016) address different rook-graph algebraic invariants, and do not imply the NOR basin law. The period-two restriction itself is established background and is not claimed as novel. The mathematical claims here concern the exact rook-graph orbit and basin census and the sharp anisotropic concentration crossover.

## Limitations
The statements apply only to **closed-neighborhood**, simultaneous, binary NOR on rook graphs with both dimensions at least two. The update rule is not interchangeable with open-neighborhood NOR. The exact distribution is over all \(2^{ab}\) binary configurations; the probability statements require independent fair initial bits. General network claims are not inferred from the finite enumerations. Possible unindexed earlier graph-specific or matrix-occupancy derivations remain a novelty risk. No independent review or independent validation is claimed.

## References
1. J. A. Aledo, S. Martínez and J. C. Valverde, *Parallel Dynamical Systems over Graphs and Related Topics: A Survey*, Journal of Applied Mathematics (2015), article 594294, first published 2015-03-24, DOI: 10.1155/2015/594294. Full HTML sections 2–3 consulted.
2. J. A. Aledo, S. Martínez, F. L. Pelayo and J. C. Valverde, *Parallel discrete dynamical systems on maxterm and minterm Boolean functions*, Mathematical and Computer Modelling 55 (2012), 666–671, DOI: 10.1016/j.mcm.2011.08.040. Bibliographic record and abstract consulted; full text not accessible.
3. J. A. Aledo, A. Barzanouni, G. Malekbala, L. Sharifan and J. C. Valverde, *Counting Periodic Points in Parallel Graph Dynamical Systems*, Complexity (2020), article 9708347, DOI: 10.1155/2020/9708347. Full HTML sections 1–4 consulted.
4. J. E. Ducey, J. Gerhard and N. Watson, *The Smith and Critical Groups of the Square Rook's Graph and its Complement*, Electronic Journal of Combinatorics 23 (2016), P4.9, DOI: 10.37236/5442. Published abstract consulted.
