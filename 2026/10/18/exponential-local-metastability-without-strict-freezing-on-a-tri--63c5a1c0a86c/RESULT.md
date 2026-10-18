# Exponential local metastability without strict freezing on a triangular Ising ladder

## Finding

For each integer \(n\ge4\), put Ising spins \(\sigma_{i,r}\in\{-1,+1\}\) on the two-row, \(n\)-column triangular ladder described below, with identical antiferromagnetic coupling \(J>0\). A configuration is **weakly one-spin stable** when no individual spin flip decreases energy; it is **strictly frozen** when every individual spin flip increases energy. These are different concepts when zero-energy spin flips are permitted.

There are exactly **four** strictly frozen configurations if \(n\) is even and **none** if \(n\) is odd. The ground-state multiplicity is exactly four for even \(n\), but exactly \(2n^2\) for odd \(n\). In contrast, the number \(Z_n\) of weakly one-spin-stable configurations grows exponentially:

\[
\lim_{n\to\infty}\frac{\log Z_n}{2n}=\frac12\log\alpha=0.510606762205\ldots,
\]

where \(\alpha=2.7765621462928\ldots\) is the unique positive root of

\[
P(x,1)=x^5-2x^4-x^3-2x^2-3x-1.
\]

Under the uniform distribution on weakly stable configurations, the number \(F_n\) of parallel (antiferromagnetically frustrated) edges satisfies

\[
\frac{F_n}{n}\xrightarrow{\mathbb P}\mu
=\frac{2(\alpha^4+2\alpha^3+6\alpha^2+10\alpha+4)}
{\alpha(5\alpha^4-8\alpha^3-3\alpha^2-4\alpha-3)}
=1.464073732677\ldots.
\]

Thus uniform weak local minima typically have an **extensive energy excess** \(J(\mu-1)>0\) per spin over the ground-state energy density, even though strict absorbing configurations number at most four.

## Assumptions and scope

Vertex positions are \((i,r)\) with \(i\in\mathbb Z/n\mathbb Z\) and row \(r\in\{0,1\}\). Edges consist exactly of the two horizontal edges \((i,0)(i+1,0)\) and \((i,1)(i+1,1)\), the rung \((i,0)(i,1)\), and the diagonal \((i,0)(i+1,1)\), for every \(i\). There are \(2n\) distinct vertices, \(4n\) edges, \(2n\) elementary triangular faces, and each vertex has degree four. This defines an open-transverse, periodic-longitudinal strip; it is not a fully periodic width-two quotient of the bulk triangular lattice.

The Hamiltonian is \(H(\sigma)=J\sum_{\{v,w\}\in E}\sigma_v\sigma_w=J(2F_n-4n)\), where \(F_n\) counts equal-spin edges. Weakly stable means \(H(\sigma^v)\ge H(\sigma)\) for every vertex \(v\), while strictly frozen means all these inequalities are strict. Under ordinary zero-temperature Glauber dynamics in which a zero-energy flip has positive rate, only the strictly frozen configurations are absorbing; the weakly stable configurations need not be absorbing. Statements about uniform ensembles are **not** dynamical hitting probabilities.

## Proof

**1. Local conditions.** If a vertex has \(k\) neighbors with the opposite spin, flipping it changes energy by \(4J(k-2)\). Consequently weak one-spin stability is equivalent to \(k\ge2\) at every vertex, and strict freezing to \(k\ge3\) at every vertex. In particular, a strictly frozen state has at most one equal-spin incident edge per vertex.

**2. Strictly frozen states.** Every elementary triangular face has at least one equal-spin edge. Let \(h\) count equal-spin horizontal edges. Each equal-spin rung or diagonal belongs to two elementary triangles, while a horizontal edge belongs to only one. Counting face–equal-edge incidences therefore yields

\[
2n\le 2F_n-h.
\]

Strict freezing gives \(2F_n\le2n\), so necessarily \(F_n=n\) and \(h=0\). Both rows must alternate. This is impossible for odd \(n\); for even \(n\), there are exactly four choices of the two alternating row phases. Conversely, in each such state the two horizontal neighbors of every vertex have opposite spins, and exactly one of its two inter-row neighbors agrees with it, giving three opposing neighbors. All four states are strictly frozen.

**3. Exact ground-state multiplicities.** Every configuration obeys \(F_n\ge n\); for odd \(n\), each horizontal row has at least one equal-spin edge, whence \(h\ge2\) and \(F_n\ge n+1\). Label a column by one of \(00,01,10,11\), interpreting \(0,1\) as the two spins. For columns \(b,c\), let \(w(b,c)\) be the number of equal-spin edges among the rung of \(b\), the top and bottom horizontal edges from \(b\) to \(c\), and the diagonal from top \(b\) to bottom \(c\). Then the full energy polynomial is \(\mathrm{tr}\,W(u)^n\), with

\[
W(u)=\begin{pmatrix}
u^4&u^2&u^3&u\\
u^2&u^2&u&u\\
u&u&u^2&u^2\\
u&u^3&u^2&u^4
\end{pmatrix}.
\]

Write \(W(u)=uA+u^2B+O(u^3)\), where

\[
A=\begin{pmatrix}0&0&0&1\\0&0&1&1\\1&1&0&0\\1&0&0&0\end{pmatrix},\qquad
B=\begin{pmatrix}0&1&0&0\\1&1&0&0\\0&0&1&1\\0&0&1&0\end{pmatrix}.
\]

A direct multiplication gives \(A^2=I+N\), \(N^2=0\), \(\mathrm{tr}(A^{2m})=4\), \(\mathrm{tr}(A^{2m+1})=0\), \(\mathrm{tr}(B)=2\), and \(\mathrm{tr}(NB)=4\). The coefficient of \(u^n\) in \(\mathrm{tr}\,W(u)^n\) is therefore four for even \(n\) and zero for odd \(n\). For odd \(n\), the next coefficient is

\[
[u^{n+1}]\mathrm{tr}\,W(u)^n
=n\,\mathrm{tr}(A^{n-1}B)=n\bigl(2+2(n-1)\bigr)=2n^2.
\]

These positive leading coefficients prove both ground-state multiplicities and the claimed minimum frustrated-edge counts.

**4. All weak one-spin local minima.** Let \(R=\{00,01,10,11\}\). States of a 16-state transfer matrix are ordered pairs \((a,b)\in R^2\), with the order induced by \(R\). Write \(b=(b_0,b_1)\) and similarly for \(a,c\). Define \(L(a,b,c)=1\) precisely when both conditions hold:

\[
\begin{aligned}
&\#\{t\in\{a_0,c_0,b_1,c_1\}:t\ne b_0\}\ge2,\\
&\#\{t\in\{a_1,c_1,b_0,a_0\}:t\ne b_1\}\ge2.
\end{aligned}
\]

For \(u>0\), set

\[
M(u)_{(a,b),(b',c)}=\mathbf1\{b=b'\}\,L(a,b,c)\,u^{w(b,c)}.
\]

The middle column's two local inequalities use exactly its four physical neighbors. Consequently the marked weak-local-minimum polynomial is, for every \(n\ge4\),

\[
Z_n(u)=\sum_{\sigma\text{ weakly stable}}u^{F_n(\sigma)}=\mathrm{tr}\,M(u)^n.
\]

The determinant of this explicitly defined matrix factors over \(\mathbb Z[x,u]\) as

\[
\det(xI-M(u))=x^4(x-u^2)^2P(x,u)Q(x,u),
\]

with

\[
\begin{aligned}
P(x,u)={}&x^5-2ux^4-(2u^3-u^2)x^3\\
&-(u^6+2u^5-u^4)x^2-(2u^7+u^6)x-u^8,\\
Q(x,u)={}&x^5+2ux^4+(2u^3+u^2)x^3\\
&-(u^6-2u^5-u^4)x^2+(2u^7-u^6)x-u^8.
\end{aligned}
\]

An exact determinant calculation and all matrix-entry rules are included in the verification program. At \(u=1\), the only nontrivial strongly connected component comprises the 14 states other than \((00,00)\) and \((11,11)\), and the fifth power of its 14-by-14 adjacency matrix is strictly positive. Perron–Frobenius theory therefore gives a simple positive dominant eigenvalue. Descartes' sign rule applied to \(P(x,1)\) and \(Q(x,1)\) identifies it as the unique positive root of \(P(x,1)\), lying between \(2\) and \(3\), since the sole positive root of \(Q(x,1)\) is below \(1\). Thus \(Z_n(1)=\alpha^n(1+O(\vartheta^n))\) for some \(0<\vartheta<1\), and the entropy formula follows.

**5. Energy-density law.** Positivity of the same fifth power holds for the marked matrix near \(u=1\), so its Perron root \(\lambda(u)\) is analytic. It obeys \(P(\lambda(u),u)=0\). Hence the limiting logarithmic moment-generating function per column of \(F_n\) is \(\log\lambda(e^t)-\log\lambda(1)\). Differentiation gives

\[
\mu=-\frac{P_u(\alpha,1)}{\alpha P_x(\alpha,1)},
\]

which simplifies to the expression in the Finding. Analyticity gives \(\mathrm{Var}(F_n)=O(n)\); Chebyshev's inequality establishes convergence in probability. Moreover, using \(P(\alpha,1)=0\),

\[
\mu-1=\frac{2\alpha^3+6\alpha^2+8\alpha+3}
{\alpha(5\alpha^4-8\alpha^3-3\alpha^2-4\alpha-3)}>0.
\]

The denominator is positive because the unique positive root of \(P(x,1)\) is crossed with positive derivative. Thus the energy-density separation is strict.

## Verification

The attached `verify.py` independently constructs the physical graph and exhaustively enumerates all \(2^{2n}\) labeled spin configurations for \(4\le n\le8\). It compares their local flip conditions, energy gradings, strict counts, and ground-state counts with a separately constructed transfer-state recurrence. The weak counts for consecutive lengths \(4\) through \(11\) are respectively \(62,172,450,1276,3550,9782,27256,75616\). It also checks the exact weighted characteristic-polynomial identity, the positive fifth power of the primitive core, the nilpotent ground-state expansion, and the dominant-root formulas. The program was actually executed and returned `ALL CHECKS PASS`. These finite checks support, but do not replace, the infinite proofs above.

## Relationship to prior work

Triangular antiferromagnetic ground-state degeneracy and its dimer-covering representation are classical subjects. Dhar, Chaudhuri and Dasgupta analyze the full triangular antiferromagnet's ground-state strings and dynamics under a staggered field; their full-text treatment concerns a different geometry and does not give this strip's weak-local-minimum polynomial or strict-freezing parity law. Spirin, Krapivsky and Redner count frozen ferromagnetic states on the square lattice and tree geometries, not the present frustrated strip. Newman and Stein analyze blocking on the degree-three square ladder, where zero-energy ties are absent, unlike the degree-four triangular ladder here. Pagnani, Parisi and Ratiéville treat metastable entropy on locally tree-like random regular graphs rather than this deterministic family of triangles. Previously recorded square-ladder Ising and multicolor Potts statements also concern ferromagnetic couplings and different edge sets; they do not imply this antiferromagnetic three-way separation.

## Limitations

Weak one-spin stability is not absorbing under a Glauber rule that permits zero-energy moves. The analysis concerns uniform counting over weak local minima, not the trajectory-dependent distribution reached by quenches. Finite transverse width means no assertion is made about the full two-dimensional triangular-lattice bulk limit. The literature comparisons do not rule out unindexed or differently worded transfer-matrix enumerations of exactly this strip. Independent scientific validation has not been performed.

## References

- C. M. Newman and D. L. Stein, *Blocking and Persistence in the Zero-Temperature Dynamics of Homogeneous and Disordered Ising Models*, arXiv:cond-mat/9904208 (public 1999-04-14), https://arxiv.org/abs/cond-mat/9904208.
- A. Dhar, P. Chaudhuri and C. Dasgupta, *The triangular Ising antiferromagnet in a staggered field*, arXiv:cond-mat/9910472 (public 1999-10-28), https://arxiv.org/abs/cond-mat/9910472.
- V. Spirin, P. L. Krapivsky and S. Redner, *Freezing in Ising Ferromagnets*, arXiv:cond-mat/0105037 (public 2001-05-02), https://arxiv.org/abs/cond-mat/0105037.
- A. Pagnani, G. Parisi and M. Ratiéville, *Metastable configurations on the Bethe lattice*, arXiv:cond-mat/0210305 (public 2002-10-14), https://arxiv.org/abs/cond-mat/0210305.
