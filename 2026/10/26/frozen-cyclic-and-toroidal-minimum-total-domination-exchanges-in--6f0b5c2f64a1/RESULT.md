# Frozen, cyclic, and toroidal minimum-total-domination exchanges in circular prisms

## Finding
Let \(P_n=C_n\square K_2\), with \(n\ge3\), and let \(\mathcal T_n\) be the **minimum-total-domination exchange graph**. Its vertices are all minimum total dominating sets of \(P_n\); two such sets are adjacent exactly when their symmetric difference has two vertices (one token replacement). For every \(n\not\equiv5\pmod6\), the complete classification is
\[
\begin{array}{c|c|c|c}
 n\bmod6 & \gamma_t(P_n)&|V(\mathcal T_n)| &\mathcal T_n\\ \hline
 0&2n/3&9&9K_1\\
 1&(2n+1)/3&2n&C_{2n}\\
 2&2(n+1)/3&n^2&C_n\square C_n\\
 3&2n/3&3&3K_1\\
 4&2(n+2)/3&[n(n+5)/6]^2&H_n\square H_n
\end{array}
\]
Here \(n\ge6\) in row zero; \(n\ge7\) in row one; \(n\ge8\) in row two; \(n\ge3\) in row three; and \(n\ge4\) in row four. The graph \(H_n\) is the minimum ordinary-domination exchange graph of the single cycle \(C_n\). It has \(n(n+5)/6\) vertices, is connected and 4-regular, and is defined intrinsically in the proof below. Therefore the last row is connected and 8-regular. In row two the exchange graph has diameter \(2\lfloor n/2\rfloor=n\); in row one it is a cycle with diameter \(n\). The frozen rows have no exchange edges.

## Assumptions and scope
All graphs are finite, simple and undirected. The prism has vertices \(a_i,b_i\), \(i\in\mathbb Z_n\), and edges \(a_i a_{i+1}\), \(b_i b_{i+1}\), \(a_i b_i\). A total dominating set \(S\) meets the **open** neighborhood of every vertex. Its minimum cardinality is \(\gamma_t\); a one-token exchange replaces exactly one member of a minimum set with one outside it, and the result must remain a minimum total dominating set. The residue \(n\equiv5\pmod6\) is deliberately **not** claimed. All congruence statements refer to integer \(n\) in the specified ranges.

## Proof
**1. Coverage accounting.** Every vertex of \(P_n\) has degree three. For \(c_S(v)=|N(v)\cap S|\), total domination requires \(c_S(v)\ge1\), and
\[
\sum_{v\in V(P_n)}(c_S(v)-1)=3|S|-2n.
\]
Consequently \(|S|\ge\lceil2n/3\rceil\), and equality at \(3\mid n\) means every vertex is dominated by **exactly one** chosen neighbor.

**2. Efficient cases \(3\mid n\).** Encode column \(i\) by \(x_i=1\) when \(a_i\in S\), \(y_i=1\) when \(b_i\in S\), and put \(s_i=x_i+y_i\). The two exact-coverage equations are
\[
x_{i-1}+x_{i+1}+y_i=1,\qquad y_{i-1}+y_{i+1}+x_i=1.
\]
Their sum is \(s_{i-1}+s_i+s_{i+1}=2\), so \(s_{i+3}=s_i\). The three nonnegative column counts sum to two, and thus form, up to phase, either \((2,0,0)\) or \((1,1,0)\). In the first case every third column contains both chosen rim vertices, giving exactly three configurations for all \(3\mid n\). In the second case, the two occupied columns in a triple necessarily use the *same* rim (substitution into either exact-coverage equation); successive triples must alternate rims. This closes around the prism precisely when \(n/3\) is even. Then there are three phases and two rim orientations, hence six additional configurations. Thus there are exactly nine for \(n\equiv0\pmod6\), and exactly three for \(n\equiv3\pmod6\). These all have \(2n/3\) chosen vertices and attain the lower bound. If two such perfect open-neighborhood coverings differed by replacing \(p\) with \(q\), then the 0-1 coverage vector would force \(N(p)=N(q)\). Distinct vertices of \(P_n\), \(n\ge3\), have distinct open neighborhoods. Thus no exchange exists.

**3. Every even prism splits into two cycle domination problems.** For even \(n\), define its bipartition classes \(A_i=a_i\) for even \(i\), \(A_i=b_i\) for odd \(i\), and \(B_i=b_i\) for even \(i\), \(B_i=a_i\) for odd \(i\). Then
\[
N(B_i)=\{A_{i-1},A_i,A_{i+1}\},\qquad N(A_i)=\{B_{i-1},B_i,B_{i+1}\}.
\]
Hence \(S\) totally dominates the prism **if and only if** its selected \(A\)-indices and selected \(B\)-indices are two independent ordinary dominating sets of \(C_n\). Since \(\gamma(C_n)=\lceil n/3\rceil\), minimum sets are exactly ordered pairs of minimum cycle dominating sets. Every one-token exchange changes just one factor, proving the graph identity
\[
\mathcal T_n\cong D_n\square D_n,
\]
where \(D_n\) denotes the exchange graph of minimum ordinary dominating sets of \(C_n\).

Write the selected indices of one minimum cycle dominating set in cyclic order and record positive clockwise gaps. Domination is **equivalent** to all gaps lying in \(\{1,2,3\}\), and the number of gaps is \(\lceil n/3\rceil\). This completely characterizes \(D_n\): exchanging a selected index only changes the two neighboring gaps, from \((r,s)\) to \((r+t,s-t)\), provided both resulting gaps remain between one and three.

If \(n=3q\), every gap is three, giving three mutually exchange-isolated sets. If \(n=3q+2\), exactly one gap is two and all others three. The exceptional gap has \(n\) possible positions; its two moves shift its absolute location by \(\pm3\) modulo \(n\). Since \(\gcd(n,3)=1\), \(D_n\cong C_n\). If \(n=3q+1\), the gap deficit from all-threes equals two: either one gap is one (type I), or two gaps are two (type II). There are \(n\) type-I sets and \(nq/2\) type-II sets. Every type-I set has two type-I neighbors from swapping \((1,3)\leftrightarrow(3,1)\), and two type-II neighbors from splitting its unique defect \((1,3)\leftrightarrow(2,2)\) on either side. Every type-II set has four neighbors by transporting each length-two gap across a neighboring length-three gap or, once adjacent, coalescing the two defects; counting admissible local moves at the boundaries gives exactly four also for \(q=1\). Any type-II set can move one defect toward the other and then coalesce, reaching type I. Type-I configurations connect cyclically by steps of three, and \(\gcd(3,3q+1)=1\), so \(D_n\) is connected, 4-regular and has \(n(q+2)/2=n(n+5)/6\) vertices. The even-prism rows now follow by graph Cartesian products.

**4. The one-excess odd prisms \(n=6k+1\).** Here \(k\ge1\). The coverage inequality forces \(|S|\ge(2n+1)/3\). Interpret digits \(0,1,2,3\) as respectively empty, top-only, bottom-only, both vertices selected in a column. The cyclic word
\[
(011022)^k2
\]
(the block has length six and is repeated exactly \(k\) times) is a total dominating set containing \(4k+1\) vertices; direct substitution into the open-neighborhood conditions shows that exactly the bottom vertex \(b_{n-2}\) has two selected neighbors, and all other vertices have one. Thus the lower bound is exact and every optimum has one and only one **doubled vertex** \(v\) with \(c_S(v)=2\).

The linear map from a selected-set indicator to its open-neighborhood coverage vector is the adjacency matrix of \(P_n\). Its eigenvalues are \(2\cos(2\pi j/n)\pm1\), with \(0\le j<n\); none vanish when \(n\equiv1\pmod6\). Therefore the unique doubled vertex determines the entire selected indicator vector (no two different minima share the same doubled vertex). The explicit cyclic word and all its rotations, together with exchanging the two rims, realize *every* possible doubled vertex exactly once. Thus there are exactly \(2n\) minima.

For an exchange replacing \(p\) with \(q\), the coverage vectors of the two minima differ by \(\boldsymbol 1_{N(q)}-\boldsymbol 1_{N(p)}\), which must also be the difference of two singleton doubled-vertex indicators. Since every open neighborhood has three vertices, \(|N(p)\cap N(q)|=2\). For \(n\ge7\), these overlapping neighborhood pairs are exactly the pairs at opposite rims in adjacent columns. Substitution gives that changing a doubled vertex \(a_i\) can only send it to \(b_{i-3}\) or \(b_{i+3}\), and conversely from \(b_i\) to \(a_{i\pm3}\). Both exchanges occur: in the displayed seed word they are respectively a replacement of a chosen bottom vertex in one adjacent column by an unchosen top vertex in the other; the row/rotation symmetries cover all vertices. Hence the exchange graph has precisely the edges
\[
a_i\sim b_{i-3},\qquad a_i\sim b_{i+3}
\]
on doubled-vertex labels. It is 2-regular and connected, since following two such steps moves the rim index by six, coprime to \(n=6k+1\). Thus it is \(C_{2n}\). This completes every asserted case.

## Verification
The accompanying `verify.py` is standalone Python 3 using only the standard library. Running `python3 verify.py` verifies all exact cyclic-word optimal configurations by dynamic programming for \(3\le n\le26\), compares against a separate direct subset enumeration for \(3\le n\le10\), explicitly reconstructs even prism factor configurations and exchange degrees, and for odd \(n\equiv1\pmod6\) checks the full doubled-vertex labeling and all actual exchanges. It terminates with `ALL_VERIFY_OK`. Finite checks are corroboration, not the proof of the unbounded claims.

## Relationship to prior work
The numerical equality \(\gamma_t(G\square K_2)=2\gamma(G)\) for bipartite \(G\) was proved by Azarija, Henning and Klavžar (arXiv:1606.08143; *The Electronic Journal of Combinatorics*, DOI 10.37236/6288). The minimum values and several minimum-set **counts** for prisms also appear in published enumerations, including OEIS A303053; they are not claimed as new here. Wongsriya and Trakultraipruk studied reconfiguration of minimum total dominating sets in *ordinary* paths and cycles, not prism graphs. Rakhimol and Bhatt classified counts and degree in the minimum **ordinary** domination exchange graph of cycles of order congruent to one modulo three, which describes one factor above but not the prism product or the odd-prism cycle theorem. Suzuki, Mouawad and Nishimura studied domination reconfiguration with add/delete moves and an allowed size threshold; those moves and constraints differ from the minimum-total-domination token-exchange graph. The proposed new result is the **complete exchange-graph isomorphism classification of the stated prism families**, notably the frozen-versus-cycle-versus-torus transition and the odd-prism doubled-vertex invariant; existing published numerical bounds or counts do not imply these edge structures.

## Limitations
The theorem makes no assertion for \(n\equiv5\pmod6\), nor for other domination variants or other exchange rules. Existing results about cycle gamma graphs cover part of the even-factor structure; this component is not presented as independently novel. Although direct relevant primary sources were read and mathematical record comparisons made, an equivalent exchange classification in unindexed literature cannot be excluded. The computations cover only finite orders. An independent scientific audit has not been performed.

## References
1. Suzuki, Mouawad and Nishimura, *Reconfiguration of Dominating Sets*, arXiv:1401.5714 (first public 2014-01-22).
2. Azarija, Henning and Klavžar, *(Total) Domination in Prisms*, arXiv:1606.08143 (2016); *Electronic Journal of Combinatorics*, DOI 10.37236/6288.
3. Wongsriya and Trakultraipruk, *γ-total dominating graphs of paths and cycles*, *ScienceAsia* 43 (2017), 326–333, DOI 10.2306/scienceasia1513-1874.2017.43.326.
4. Rakhimol and Bhatt, *A Study on The Gamma Graph of Cycle C3K+1*, *Journal of Computational Mathematica* 7(2) (2023), DOI 10.26524/cm178.
5. OEIS A303053 (previously published counts of minimum total dominating sets of prisms).
