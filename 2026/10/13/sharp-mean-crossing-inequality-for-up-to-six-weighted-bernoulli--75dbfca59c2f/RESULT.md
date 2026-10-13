# Sharp mean-crossing inequality for up to six weighted Bernoulli trials

## Finding
Let \(1\le m\le6\), let \(0<p\le1/3\), and let \(w_1,\ldots,w_m\) be nonnegative real numbers with \(\sum_iw_i=1\). For independent Bernoulli\((p)\) variables \(B_i\), put \(X=\sum_iw_iB_i\). Then
\[
\Pr\{X\ge\mathbb EX\}=\Pr\{X\ge p\}\ge p.
\]
Equality holds **if and only if** \(\max_iw_i>1-p\). In particular, whenever every weight is less than \(p\), the inequality is strict, with explicit strictly positive lower bounds given in the proof. For \(p=0\) the inequality holds trivially, since the event has probability one. The upper restriction \(p\le1/3\) is the sharp conjectured universal parameter range, although the theorem here concerns only at most six summands.

## Assumptions and scope
Weights are real, nonnegative, and normalized to sum to one; Bernoulli trials are independent and identically distributed with common success probability \(p\). The event uses a **non-strict** threshold. There is no lattice or rationality hypothesis on the weights or on \(p\). Zero weights may be appended, reducing the proof to exactly six weights. No hypothesis of exchangeability beyond independence and the common Bernoulli parameter is needed.

For the proof, write \(q=1-p\) and suppose first that \(w_i<p\) for every one of the six weights. A subset \(S\subseteq\{1,\ldots,6\}\) is *winning* if \(\sum_{i\in S}w_i\ge p\). The probability that a particular subset of size \(j\) is precisely the set of successful trials is \(p^jq^{6-j}\). Every subset of at least four indices is winning: its complement has at most two weights, each below \(p\), so its own weight exceeds \(1-2p\ge p\).

## Proof
**1. A dominant coordinate.** If some \(w_i\ge p\), then the event \(B_i=1\) implies \(X\ge p\), giving probability at least \(p\). If \(w_i\le1-p\), the complementary weights have total at least \(p\), so the disjoint event \(B_i=0\) and \(B_j=1\) for all other positive-weight coordinates also wins and has positive probability. Hence equality in this case requires \(w_i>1-p\). Conversely, if \(w_i>1-p\), then \(w_i>p\) and the complementary weights sum to less than \(p\); consequently \(X\ge p\) holds exactly when \(B_i=1\), proving equality.

It remains to prove strict inequality when all six weights satisfy \(w_i<p\). Necessarily \(p>1/6\), since their sum is one.

**2. Region \(1/6<p\le1/5\).** Every pair is winning: if \(S\) consists of two indices, the sum of the four other weights is below \(4p\), so \(\sum_{i\in S}w_i>1-4p\ge p\). Thus
\[
\Pr\{X\ge p\}\ge1-q^6-6pq^5.
\]
The difference \(1-q^6-6pq^5-p\) is strictly positive on \([1/6,1/5]\): it equals \(4505/46656\) at \(p=1/6\), and its derivative is \(30pq^4-1>0\) throughout this interval (indeed \(30pq^4\ge5(4/5)^4>1\)).

**3. Region \(1/5\le p\le1/4\).** Consider the graph of *losing pairs*: an edge \(\{i,j\}\) occurs when \(w_i+w_j<p\). Two edges cannot be disjoint: their four weights sum to less than \(2p\), and the remaining two weights to less than \(2p\), contradicting \(1\le4p\). A graph in which every two edges intersect is a star or is contained in a triangle; it therefore has at most five edges on six vertices. Hence at least ten pairs win. Every triple also wins, since the complementary three weights sum to less than \(3p\) and the triple weight is more than \(1-3p\ge p\). It follows that
\[
\Pr\{X\ge p\}\ge10p^2q^4+20p^3q^3+15p^4q^2+6p^5q+p^6.
\]
Subtracting \(p\) factors the lower bound as
\[
p(1-p)\left(4p^3-11p^2+9p-1\right).
\]
The parenthetical polynomial equals \(49/125>0\) at \(p=1/5\); its derivative \(12p^2-22p+9\) is at least \(7/2\) for \(p\le1/4\). Therefore the lower bound is strictly above \(p\).

**4. Region \(1/4\le p\le1/3\).** Let \(H\) be the simple graph on six vertices whose edges are the winning pairs, and write \(k=|E(H)|\) and \(t(H)\) for its number of triangles. Every perfect matching of the complete six-vertex graph includes a winning edge: three disjoint losing edges would have total weight below \(3p\le1\), a contradiction. There are exactly fifteen perfect matchings, each edge belonging to exactly three, so \(k\ge5\).

If a triple \(T\) is losing, its complementary triple \(S\) has total weight above \(1-p\ge2p\). Because each individual weight is below \(p\), every pair inside \(S\) has weight above \(p\). Thus \(S\) forms a triangle of \(H\). Complementation injects the losing triples into the triangles of \(H\), and there are at least \(20-t(H)\) winning triples.

We use the finite six-vertex graph inequality
\[
t(H)\le2k-8\quad\text{whenever }5\le k\le15.
\]
This is a finite clique-counting fact. It follows, for example, from the graph form of the Kruskal–Katona bound: writing \(k=\binom r2+s\) with \(0\le s<r\), the number of triangles is at most \(\binom r3+\binom s2\). Checking the eleven integers \(5\le k\le15\) gives respective maxima \(2,4,4,5,7,10,10,11,13,16,20\), each no greater than \(2k-8\). An independently specified exhaustive enumeration of all \(2^{15}=32768\) labeled simple graphs on six vertices checks the finite inequality without invoking Kruskal–Katona; its complete executable certificate is supplied as `checker.py`.

Consequently,
\[
\begin{aligned}
\Pr\{X\ge p\}&\ge kp^2q^4+(20-t(H))p^3q^3+15p^4q^2+6p^5q+p^6\\
&\ge5p^2q^4+18p^3q^3+15p^4q^2+6p^5q+p^6.
\end{aligned}
\]
Indeed, the second difference is at least \((k-5)p^2q^3(q-2p)=(k-5)p^2q^3(1-3p)\ge0\). Subtracting \(p\) from the final expression factors as
\[
p(1-p)\left(3p^4-7p^3+2p^2+4p-1\right).
\]
The parenthetical polynomial equals \(7/256>0\) at \(p=1/4\), and has derivative \(12p^3-21p^2+4p+4\ge4-21/9>0\) on \([1/4,1/3]\). This proves strict positivity in the final region and completes the proof for six weights. Appending zero weights proves the statement for every \(1\le m\le6\).

**5. Equality.** The three regions prove strict inequality if every \(w_i<p\). The dominant-coordinate argument proves that otherwise equality occurs exactly when some \(w_i>1-p\). This also covers the one-summand boundary.

## Verification
Run `python3 checker.py` using Python 3.8 or later; no third-party packages are needed. The checker exhausts all \(32768\) labeled six-vertex graphs, verifies the complete triangle maxima, checks \(t\le2k-8\), and verifies by rational Bernstein coefficients that all three explicit lower-bound polynomials exceed \(p\) on their prescribed closed intervals. Its expected terminal marker is `EXACT_CHECK_OK`. The polynomial derivatives in the proof independently establish positivity without computer reliance. All universal assertions follow analytically from graph counting and polynomial inequalities; a finite numerical grid alone would not suffice.

## Relationship to prior work
Milojević and Sudakov (2026, arXiv:2606.30287) formulated the weighted-Bernoulli mean-crossing inequality for every number of summands and the full range \(p\le1/3\). Their paper proves a very-small-\(p\) range for arbitrary summand count through a restricted Manickam–Miklós–Singhi question and credits the known \(p=1/r\) cases. This finding addresses the complementary restriction of **at most six weights**, with no restriction within the conjectured parameter range, and determines all equality cases. It does not supply a general unrestricted proof. Earlier work on optimal **upper** tails of weighted Bernoulli bets by Fokkink, Meester, and Pelekis (2020/2023) treats a different extremal direction, and general small-deviation/MMS estimates do not directly give this finite six-weight sharp lower bound.

## Limitations
The result assumes common Bernoulli success probability and independent trials. It does not establish the conjecture for seven or more positive weights, for heterogeneous Bernoulli success probabilities, or for general nonnegative summands. The explicit positive lower bounds in the all-small-weights case are **not** claimed individually optimal. Priority remains subject to additional sources not indexed by the inspected literature searches; no independent external audit has occurred.

## References
1. A. Milojević and B. Sudakov, *On the Probability a Weighted Bernoulli Sum Exceeds Its Mean*, arXiv:2606.30287 (first public version 2026-06-29), https://arxiv.org/abs/2606.30287.
2. R. Fokkink, L. Meester and C. Pelekis, *Optimizing stakes in simultaneous bets*, ALEA 20 (2023), 153–165; original arXiv:2002.06804, https://arxiv.org/abs/2002.06804.
3. N. Alon, H. Huang and B. Sudakov, *Nonnegative \(k\)-sums, fractional covers, and probability of small deviations*, J. Combin. Theory B 102 (2012), 784–796; arXiv:1104.1753.
4. Kruskal–Katona clique-shadow theorem (standard graph clique-counting form); the particular six-vertex inequality used here is additionally verified exhaustively by the included checker.
