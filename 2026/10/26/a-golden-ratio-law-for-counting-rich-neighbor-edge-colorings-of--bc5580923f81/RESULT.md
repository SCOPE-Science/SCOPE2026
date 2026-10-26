# A golden-ratio law for counting rich-neighbor edge-colorings of cycles

## Finding

For each integer \(n\ge3\), let \(N_n\) count proper rich-neighbor edge-colorings of the simple cycle \(C_n\) by the **named palette** \(\{0,1,2\}\), with vertices and edges distinguished by their cyclic indices. A proper edge-coloring is *rich-neighbor* when every edge has an adjacent edge whose two adjacent edges have different colors. Unused palette colors are allowed in the definition of \(N_n\).

Define a \(24\)-by-\(24\) zero-one matrix \(M\) with states \((a,b,c,r)\in\{-1,+1\}^3\times\mathbb Z/3\mathbb Z\). There is a directed transition from \((a,b,c,r)\) to \((b,c,d,r+d)\) of weight one exactly when \(d\in\{-1,+1\}\) and \(a=b\) or \(c=d\); the fourth coordinate is reduced modulo three. All other entries are zero. Then, for every \(n\ge3\),

\[
N_n=\operatorname{tr}(M^n).
\]

Writing \(X\) for a polynomial indeterminate, the characteristic polynomial is **exactly**

\[
\det(XI-M)=(X-1)(X+1)(X^2+1)(X^2-X-1)(X^2-X+1)P(X)^2,
\]

\[
P(X)=X^8+X^7+X^6+X^4-X^3-X^2+1.
\]

Let \(\varphi=(1+\sqrt5)/2\). The full sequence consequently satisfies

\[
\boxed{N_n\sim\varphi^n\quad(n\to\infty)}.
\]

In particular, the fraction of proper colorings by this named three-color palette which are rich-neighbor is asymptotic to \((\varphi/2)^n\); it tends to zero exponentially. Initial values are \(N_3=6\), \(N_4=0\), \(N_5=30\), \(N_6=24\), \(N_7=0\), \(N_8=72\), \(N_9=60\), \(N_{10}=120\), \(N_{11}=264\), and \(N_{12}=228\).

## Assumptions and scope

All graphs are finite and simple. Cycles have length at least three. A coloring of a fixed labeled cycle is distinguished from its rotations, reflections and palette permutations. A rich edge is an edge whose adjacent edges all receive distinct colors; the rich-neighbor condition requires an *adjacent rich edge*, not that each edge itself be rich. As each cycle edge has two adjacent edges, the condition given above is equivalent. The asymptotic is for the precise number \(N_n\), not the number of palette-permutation or graph-automorphism orbits. It does not enumerate all colorings when more than three colors are available.

## Proof

Index the edges as \(e_i\) for \(i\in\mathbb Z/n\mathbb Z\), and identify their three permitted colors with \(\mathbb Z/3\mathbb Z\). A coloring \(c_i\) is proper if and only if its consecutive increments satisfy
\[
s_i=c_{i+1}-c_i\in\{-1,+1\}\pmod3.
\]
The cyclic closure condition is \(\sum_i s_i\equiv0\pmod3\). Conversely, such a cyclic sign sequence determines exactly three proper edge-colorings, by choosing \(c_0\).

The two edges adjacent to \(e_i\) have different colors precisely when \(s_{i-1}=s_i\). Therefore \(e_i\) has a rich neighbor precisely when
\[
(s_{i-2}=s_{i-1})\quad\text{or}\quad(s_i=s_{i+1}).
\]
The matrix transition records this local disjunction using consecutive triples of signs. Its fourth state coordinate accumulates the sign sum modulo three. A closed walk of length \(n\) therefore encodes a cyclic sign word satisfying every local rule and the modular closure, together with one arbitrary initial residue. Each sign word produces three closed walks, exactly the number of proper colorings it determines. This establishes \(N_n=\operatorname{tr}(M^n)\).

The asserted characteristic polynomial follows by exact integer matrix arithmetic. It may be verified without a symbolic algebra package using Newton identities: if \(t_j=\operatorname{tr}(M^j)\) and \(q_0=1\), then the coefficient of \(X^{24-k}\) is
\[
q_k=-\frac1k\sum_{j=1}^{k}q_{k-j}t_j\qquad(1\le k\le24).
\]
The accompanying standard-library verifier constructs \(M\), computes all \(q_k\), and compares the resulting polynomial coefficient-by-coefficient with the displayed factorization; it independently compares the transfer counts with a direct enumeration of every named three-color edge assignment at lengths three through ten.

For the asymptotic, the directed graph of \(M\) is strongly connected. This is a finite claim that can be established by inspecting its eight possible sign triples: from any triple, repeatedly appending the final sign reaches a constant triple; changing signs from a constant triple reaches the other constant triple, and both constants reach every one of the eight triples. At a positive constant triple, the four-step return with appended signs \((-1,+1,+1,+1)\) alters the residue by \(+2\) modulo three. Thus one can adjust the residue arbitrarily before following a path to any desired final triple. The verifier also checks reachability from every one of the 24 states. The positive constant triple has closed walks of lengths three and five with appended signs \((+1,+1,+1)\) and \((+1,-1,+1,+1,+1)\), respectively, both having sum divisible by three. Since three and five are coprime, the matrix is primitive.

By Perron–Frobenius, \(M\) has a unique simple positive dominant eigenvalue \(\rho\), strictly larger in absolute value than all other eigenvalues. The displayed factorization shows that \(\varphi\) is an eigenvalue. Moreover, the degree-eight factor has no positive real root \(X\ge\varphi\), because there
\[
P(X)=X^6(X^2+X+1)+X^2(X^2-X-1)+1>0.
\]
None of the other factors has a positive root above \(\varphi\). Consequently \(\rho=\varphi\). Since a matrix-power trace is the sum of the eigenvalues raised to the corresponding power, counted with algebraic multiplicity, and \(\varphi\) has multiplicity one, \(N_n=\varphi^n+O(\theta^n)\) for some \(0<\theta<\varphi\). This proves the stated asymptotic.

The total number of proper edge-colorings of \(C_n\) from three named colors is its chromatic polynomial evaluated at three, namely \(2^n+2(-1)^n\). Dividing gives the fraction claimed above.

## Verification

Run `python3 verify.py` in a directory containing the accompanying file. It uses only the Python standard library, constructs the 24-state matrix from its definition, independently checks strong connectivity, verifies the exact characteristic polynomial by Newton identities over integers, and compares transfer-matrix counts against exhaustive direct three-color assignment checks for every cycle length from three to ten. `verification_output.txt` records one actual execution and the counts through 24. Neither the finite count checks nor the software are substituted for the proved trace bijection and Perron–Frobenius argument.

## Relationship to prior work

Rich-neighbor edge-coloring was introduced by Petruševski and Škrekovski (2024). Kashima, Petruševski, Sedlar and Škrekovski (2026, Proposition 2) already construct three-color rich-neighbor colorings of cycles except at lengths four and seven, and give a four-color bound at those lengths. Kong (2026) gives general linear bounds and exact values for complete and complete bipartite graphs, including \(C_4\). These existence and chromatic-index results are **not** claimed as new here. The present statement enumerates *all* named three-color rich-neighbor colorings of every cycle and establishes the exact golden-ratio asymptotic. Neither follows from a mere existence bound or the usual count of proper colorings. No covering formula was identified in the accessible primary results and targeted record searches.

## Limitations

The 2024 foundational article was not available for a full-text priority comparison; an earlier equivalent enumeration under other terminology cannot be excluded. This theorem counts named three-color assignments only, not unrestricted palettes or equivalence classes under the dihedral group. The transfer matrix and finite integer factorization are reproducible; independent mathematical audit has not been performed.

## References

1. M. Kashima, M. Petruševski, J. Sedlar and R. Škrekovski, *The rich-neighbor chromatic index is linear in the maximum degree*, arXiv:2610.16446v1, first posted 2026-10-12. https://arxiv.org/abs/2610.16446
2. J. Kong, *Linear bounds for rich-neighbor edge-colorings*, arXiv:2610.21036v1, first posted 2026-10-15. https://arxiv.org/abs/2610.21036
3. M. Petruševski and R. Škrekovski, *Proper edge-colorings with a rich neighbor requirement*, Discrete Mathematics 347 (2024), 113803, DOI:10.1016/j.disc.2023.113803.
4. L. Chen, Y. Tan and X. Zhou, *On the Rich-Neighbor Edge-Colorings of Subcubic Graphs*, Graphs and Combinatorics 41 (2025), 89, DOI:10.1007/s00373-025-02949-y.
