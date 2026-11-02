# Exact fort-support polynomial and minimum obstructions for open ladders

## Finding

For the open ladder \(L_n=P_2\square P_n\) with \(n\ge1\), call a nonempty vertex subset a **fort** if no vertex outside it has exactly one neighbor inside it. Let \(F_n(z)\) count all forts by size, **including the empty subset with weight one**, and set \(F_0(z)=1\). Then the entire infinite collection of cardinality polynomials is given by

\[
\sum_{n\ge0} F_n(z)t^n=\frac{P(t,z)}{(1-t)Q(t,z)},
\]
where
\[
\begin{aligned}
P(t,z)={}&1-tz-t^2z^2+2t^2z^3-3t^3z^2-2t^3z^3-4t^4z^4+4t^5z^4,\\
Q(t,z)={}&1-tz-tz^2-2t^2z^2-t^2z^3-t^3z^2+t^3z^3-t^3z^4+t^5z^4.
\end{aligned}
\]

Moreover, if \(d_n\) is the minimum positive fort size and \(c_n\) is the number of vertex-labelled forts of that size, then
\[
d_n=\left\lceil\frac{2(n+1)}3\right\rceil,
\qquad
c_n=\begin{cases}
1,&n=1,\\
2k,&n=3k,\ k\ge1,\\
k(k+3),&n=3k+1,\ k\ge1,\\
2,&n=3k+2,\ k\ge0.
\end{cases}
\]
In particular, the maximum cardinality of a failed ordinary zero-forcing starting set is \(2n-d_n\); the formula does not assert that every failed starting set is the complement of a minimum fort.

## Assumptions and scope

All graphs are finite, simple, undirected, with two labelled rows and \(n\) labelled consecutive columns. Every exterior vertex of a fort must have either zero or at least two neighbors in it. A fort is by definition nonempty, while \(F_n\) adjoins the empty set for enumerative convenience. Distinct subsets of the labelled ladder count separately. The zero-forcing convention is the ordinary color-change rule (not the skew rule).

## Proof

**1. Local transfer and rational generating function.** Encode each column by its selected-row bitmask \(b\in\{0,1,2,3\}\): bit \(1\) is the top row and bit \(2\) the bottom row. Write \(w(b)\) for the number of set bits. For three consecutive masks \(a,b,c\), define \(A(a,b,c)\) to hold when, for each missing bit \(r\) of \(b\),
\[
\mathbf1_{r\in a}+\mathbf1_{r\in c}+\mathbf1_{3-r\in b}\ne1.
\]
Here bit-membership means selection of that row; \(3-r\) denotes the other bit. Give both virtual columns beyond the ladder mask \(0\). Then a column word is the empty set or a fort precisely when every consecutive triple satisfies \(A\), including both boundary triples. This is exactly the exterior-neighbor test, so it is both necessary and sufficient.

For ordered mask pairs \((a,b)\), let \(f_{a,b}(t,z)\) be the contribution of valid finite continuations to the right, with a terminal virtual zero column. Last-step termination is permitted precisely if \(A(a,b,0)\). Therefore
\[
f_{a,b}=\mathbf1_{A(a,b,0)}+t\sum_{\substack{c\in\{0,1,2,3\}\\A(a,b,c)}}z^{w(c)}f_{b,c},
\qquad
F(t,z)=1+t\sum_{b=0}^3 z^{w(b)}f_{0,b}.
\]
Simultaneously exchanging the two rows merges the 16 pair states into ten orbits, represented by
\[
(0,0),(0,1),(0,3),(1,0),(1,1),(1,2),(1,3),(3,0),(3,1),(3,3).
\]
The finite linear system \((I-tM)f=v\), whose entries are explicitly specified by the displayed recurrence, has the rational solution stated in the finding. The included verifier reconstructs this exact ten-state system over \(\mathbb Q(t,z)\) and checks the numerator–denominator identity algebraically, not by truncation.

**2. Sharp minimum.** Suppose \(S\) is a nonempty fort and let \(w_i\in\{0,1,2\}\) be its number of selected vertices in column \(i\). Two adjacent completely empty columns would force every neighboring column to be empty, because an exterior vertex in an empty column would otherwise have exactly one selected horizontal neighbor; propagation would make \(S\) empty. Also, any three consecutive columns with only one selected vertex violate the exterior-neighbor condition: with selection at an end, its adjoining empty column has a vertex with exactly one selected neighbor; with selection in the middle, the missing row in that middle column sees exactly its selected vertical neighbor. Hence, for every \(n\ge3\),
\[
 w_i+w_{i+1}+w_{i+2}\ge2\quad(1\le i\le n-2).
\]
Nonemptiness forces \(w_1,w_n\ge1\). Moreover the end-column neighborhood test gives \(w_1+w_2\ge2\) and \(w_{n-1}+w_n\ge2\). The exact weighted sum of all interior triple inequalities and three boundary inequalities is
\[
3|S|=\sum_{i=1}^{n-2}(w_i+w_{i+1}+w_{i+2})+(w_1+w_n)+(w_1+w_2)+(w_{n-1}+w_n)
\ge2(n+1).
\]
Thus \(|S|\ge\lceil2(n+1)/3\rceil\). For \(n=1,2\) the graph can be checked directly.

Equality is attained by mask words \(3\) at \(n=1\), \(12\) at \(n=2\), \(121\) at \(n=3\), and \(1212\) at \(n=4\). If a valid word ends with two different singleton masks \(\bar s,s\), appending \(0,s,\bar s\) adds three columns and two selected vertices while preserving all interior and boundary conditions; this is verified directly from \(A\). Iteration reaches all positive lengths with the asserted minimum.

**3. Exact multiplicity of minimum forts.** For \(n\ge1\) and any nonempty fort \(S\) define its nonnegative integer slack \(j=3|S|-2(n+1)\). The bivariate slack series is
\[
H(t,q)=\sum_{n\ge1}t^n\sum_{S\text{ fort of }L_n}q^{3|S|-2(n+1)}
=q^{-2}\left(F(tq^{-2},q^3)-\frac1{1-tq^{-2}}\right).
\]
Substituting the already established rational formula and cancelling gives
\[
H(t,q)=\frac{t(2t+q^2-3q^2t^3+3q^3t+q^4t^2)}{1-t^3-qt-2q^2t^2+q^2t^5+q^3t^3-q^4t-q^5t^2-q^6t^3}.
\]
The three lowest slack coefficients are, by exact coefficient extraction,
\[
[q^0]H=\frac{2t^2}{1-t^3},\qquad
[q^1]H=\frac{2t^3}{(1-t^3)^2},\qquad
[q^2]H=\frac{t(1+t^3+t^6-t^9)}{(1-t^3)^3}.
\]
For each \(n\), the least possible slack is the unique element of \(\{0,1,2\}\) congruent to \(-2(n+1)\) modulo three. Reading the corresponding coefficient of \(t^n\) in these three series gives exactly the displayed \(c_n\), including \(n=1\). Because no smaller fort exists, each counted minimum-size fort is inclusion-minimal. The equivalence of fort supports with complements of failed zero-forcing sets yields the stated maximum failed-set size.

## Verification

Run \(\texttt{python3 verify.py}\) with Python 3 and SymPy available. The script independently constructs the ten-orbit transfer matrix and symbolically verifies the full rational identity, the slack generating identity, and all three low-slack coefficients. A direct graph-neighbor enumeration of all \(4^n\) vertex subsets for every \(1\le n\le8\) agrees with the transfer polynomial in every coefficient; the total examined is 87,380 subsets. A separate integer dynamic program verifies the minimum-size and multiplicity formulas for every \(1\le n\le44\). Its successful output is \(\texttt{VERIFY_OK transfer_states=10 exact_rational_identities=5 direct_supports=87380 direct_lengths=1..8 minimum_profile_lengths=1..44}\). Symbolic identities and the local proof, rather than finite samples, support the infinite results.

Examples:
\[
\begin{aligned}
F_1(z)&=1+z^2,\\
F_2(z)&=1+2z^2+4z^3+z^4,\\
F_3(z)&=1+2z^3+9z^4+6z^5+z^6,\\
F_4(z)&=1+4z^4+20z^5+22z^6+8z^7+z^8.
\end{aligned}
\]

## Relationship to prior work

Forts are the standard obstructions dual to ordinary zero-forcing sets. Han and Liang (2026, arXiv:2610.31109v1) study exact support loci and a general support-signature composition algorithm; their statements do not provide this labelled open-ladder fort polynomial or minimum-fort multiplicity formula. Abiad and Ghasemi Nezhad (2026, arXiv:2609.11754v1) investigate general fort abundance. Becker, Cameron, Hanely, Ong and Previte (2024, arXiv:2404.05963v1) study inclusion-minimal forts and explicitly display one minimal fort on a four-rung ladder but do not enumerate all forts on ladders of arbitrary length. Cameron, Hogben, Kenter, Mojallal and Schuerger (2023, arXiv:2310.17904v1) study fort hypergraphs and Cartesian-product lower bounds rather than complete ladder support polynomials. Existing zero-forcing-set polynomials enumerate the complementary hitting sets, not this full fort-support distribution by a direct equivalence of their coefficients.

## Limitations

The classification concerns two-row **open** ladders, labelled vertices, ordinary forts and all fort cardinalities. It does not count only inclusion-minimal forts, does not handle circular ladders or larger widths, and does not prove a corresponding formula for other forcing rules. The algebraic verification requires SymPy. Although closely relevant open-access primary articles were read, a historical zero-forcing polynomial thesis for ladders was not available for full inspection; priority under alternative formulations remains a residual risk. No independent mathematical audit was performed.

## References

1. Z. Han and Y. Liang, *Zero Forcing, Support Varieties, and Boundary Complexes* (2026), arXiv:2610.31109v1, https://arxiv.org/abs/2610.31109.
2. A. Abiad and S. Ghasemi Nezhad, *Fort Abundance in Zero Forcing* (2026), arXiv:2609.11754v1, https://arxiv.org/abs/2609.11754.
3. P. Becker, T. R. Cameron, D. Hanely, B. Ong, and J. P. Previte, *On the Number of Minimal Forts of a Graph* (2024), arXiv:2404.05963v1, https://arxiv.org/abs/2404.05963.
4. T. R. Cameron, L. Hogben, F. H. J. Kenter, S. A. Mojallal, and H. Schuerger, *Forts, (fractional) zero forcing, and Cartesian products of graphs* (2023), arXiv:2310.17904v1, https://arxiv.org/abs/2310.17904.
