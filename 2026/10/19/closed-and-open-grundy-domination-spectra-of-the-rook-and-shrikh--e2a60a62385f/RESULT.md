# Closed and open Grundy domination spectra of the rook and Shrikhande graphs

## Finding
Let \(R=K_4\square K_4\) and let \(S\) be the Shrikhande graph, the nonisomorphic strongly regular graphs with parameters \((16,6,2,2)\). Define the completed legal-sequence polynomial \(F_G^{\tau}(z)=\sum_{k\ge0}a_{G,k}^{\tau}z^k\), where \(a_{G,k}^{\tau}\) is the number of **ordered, distinct-vertex sequences** of length \(k\) that cover all vertices by closed neighborhoods when \(\tau=c\), or open neighborhoods when \(\tau=o\), with each newly selected vertex covering at least one vertex not previously covered.

The exact polynomials are
\[
\begin{aligned}
F_R^{c}(z)&=11712z^4+114048z^5+266112z^6,\\
F_S^{c}(z)&=192z^3+10176z^4+127296z^5+492480z^6+48384z^7,\\
F_R^{o}(z)&=F_S^{o}(z)=1920z^4+103680z^5+1658880z^6.
\end{aligned}
\]
In particular, \(\gamma_{\mathrm{gr}}(R)=6\), \(\gamma_{\mathrm{gr}}(S)=7\), while \(\gamma_{\mathrm{gr}}^t(R)=\gamma_{\mathrm{gr}}^t(S)=6\). Thus the two graphs have different closed-neighborhood sequence spectra but exactly the same *entire* open-neighborhood sequence spectra.

## Assumptions and scope
Vertices in both graphs are \((r,c)\in\mathbb Z_4^2\), encoded as the integer \(4r+c\). In \(R\), two distinct vertices are adjacent exactly when their first or second coordinates agree. In \(S\), adjacency means the difference belongs to \(\{(1,0),(-1,0),(0,1),(0,-1),(1,1),(-1,-1)\}\) modulo four. Both have sixteen vertices, degree six, and precisely two common neighbors for every pair of distinct vertices. There are eight four-cliques in \(R\), but none in \(S\), so the graphs are nonisomorphic.

For a vertex \(v\), write \(B_v=N[v]\) in the closed case and \(B_v=N(v)\) in the open case. A sequence \((v_1,\ldots,v_k)\) is legal when \(B_{v_i}\setminus\bigcup_{j<i}B_{v_j}\ne\varnothing\) for each \(i\), and completed when \(\bigcup_{i=1}^k B_{v_i}=V\). Every such legal sequence automatically has pairwise distinct vertices. Counts use labeled vertices, not automorphism orbits. No claim is made for other parameters or graph orders.

## Proof
The finite classification follows from an exhaustive acyclic recurrence on the **covered vertex subset**, independently corroborated by an exhaustive recurrence on the **chosen-vertex subset**. Identify any subset with its sixteen-bit characteristic mask and put \(U=2^{16}-1\). For each neighborhood convention and graph, define the polynomial \(P_A(z)\) to enumerate all legal completed continuations from covered set \(A\). Then
\[
P_U(z)=1,\qquad P_A(z)=z\sum_{v:B_v\not\subseteq A}P_{A\cup B_v}(z)\quad(A\ne U).
\]
Each term corresponds bijectively to a legal next vertex and the remaining continuation. Since every term strictly increases the covered set, the recurrence terminates and exhaustively enumerates every legal completed sequence *exactly once*. In particular, a previously selected vertex cannot be reselected: its neighborhood is already covered. The four initial values \(P_{\varnothing}\) are exactly the displayed polynomials.

The file `coverage_certificate.json` contains, for all four graph/convention combinations, **every reachable covered set** and its complete continuation polynomial, together with full graph edge lists, a maximum-length legal witness, and terminal length distributions. The `check_certificate.py` checker independently verifies every recurrence equality, all edges, the strongly regular parameters, the four-clique distinction, each spectrum, and each longest witness. The numbers of reachable covered states are respectively \(198,654,398,654\), in the order rook-closed, rook-open, Shrikhande-closed, Shrikhande-open.

As an independent finite enumeration, `verify_selected_sets.cpp` uses the states \(T\subseteq V\) of already **selected** vertices, their neighborhood unions \(C(T)=\bigcup_{v\in T} B_v\), and integer continuation counts. Starting at the empty selected set, it adds an unused vertex precisely when this strictly enlarges \(C(T)\), and accumulates counts whenever \(C(T)=V\). This second algorithm has up to \(2^{16}\) possible states, differs substantively from the covered-set recurrence, and agrees coefficient-by-coefficient on all four polynomials. Its actually reached selected-state counts are \(11169,10137,17129,10137\), respectively. These complete enumerations establish both the polynomial coefficients and the absence of any longer or shorter completed legal sequences.

## Verification
Run `python3 verify_coverage.py`, `python3 check_certificate.py`, and `c++ -O2 -std=c++17 verify_selected_sets.cpp -o checker && ./checker` from the directory containing these files. The complete observed textual results are in `coverage_output.txt`, `certificate_output.txt`, and `selected_output.txt`. The source and certificate are self-contained; they require only a standard Python 3 interpreter and a C++17 compiler. All certificate states and arithmetic are exact integers, not probabilistic or approximate outputs. The checker does not import the certificate producer.

## Relationship to prior work
Brešar, Henning and Rall introduced and systematically investigated open-neighborhood total dominating sequences, including general bounds for regular graphs [1]. Brešar and collaborators studied Grundy domination on Cartesian graph products [2]; in Section 3 they give a length-\(m+n-2\) construction for \(K_m\square K_n\), which supplies an existing lower bound of six in the rook case. Neither inspected paper supplies the four completed-sequence polynomials, the Shrikhande comparison, or equality of the two *open* polynomials. Lin's general zero-forcing duality [3] distinguishes loop zero forcing, which corresponds to ordinary Grundy domination, from ordinary zero forcing, so results about ordinary zero forcing of this graph pair do not imply these counts. The present contribution is the exact **comparative spectrum**, not the previously available rook-graph lower bound or the general definitions.

## Limitations
The result is a finite exact classification for these two labeled sixteen-vertex graphs, not an infinite-family theorem. Novelty comparisons cover the inspected full texts and searched mathematical records, but unindexed publications or supplementary tables could contain overlapping computations. Two separate finite enumerations and a complete reproducible certificate support correctness; these do not constitute an independent external scientific audit.

## References
[1] B. Brešar, M. A. Henning, and D. F. Rall, *Total Dominating Sequences in Graphs*, first posted 2016-01-27, https://arxiv.org/abs/1601.07525.

[2] B. Brešar et al., *Dominating sequences in grid-like and toroidal graphs*, first posted 2016-07-01, https://arxiv.org/abs/1607.00248.

[3] J. C.-H. Lin, *Zero forcing number, Grundy domination number, and their variants*, https://arxiv.org/abs/1706.00798.
