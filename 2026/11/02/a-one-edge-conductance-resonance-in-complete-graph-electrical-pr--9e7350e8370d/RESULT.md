# A one-edge conductance resonance in complete-graph electrical projections

## Finding
Let \(n\ge3\) and equip the complete graph \(K_n\) with conductance \(c>0\) on the edge \(\{1,2\}\) and conductance one on all other edges. Orient its edges arbitrarily, let \(B\) be the edge-by-vertex incidence matrix, let \(C\) be the conductance diagonal, and let \(L=B^{\mathsf T}CB\). The symmetric electrical-gradient projection on edge signals is
\[
\Pi_c=C^{1/2}BL^+B^{\mathsf T}C^{1/2}.
\]
Set \(t=\sqrt c\) and \(D=n-2+2c\). There are three kinds of absolute row sum (the remote kind exists only for \(n\ge4\)):
\[
E_n(c)=\frac{2(c+(n-2)\sqrt c)}{D},
\qquad
R_n=\frac{2(n-1)}n,
\]
\[
A_n(c)=\begin{cases}
\dfrac{\sqrt c+2c+2n-5}{D},&0<c\le1,\\[4pt]
\dfrac{n\sqrt c+4cn-6c+2n^2-7n+6}{nD},&c\ge1.
\end{cases}
\]
Here \(E\) corresponds to the exceptional edge, \(A\) to an edge incident to exactly one endpoint of the exceptional edge, and \(R\) to an edge whose endpoints avoid both. Consequently
\[
\|\Pi_c\|_{\ell^\infty\to\ell^\infty}
=\max\{E_n(c),A_n(c),R_n\}\quad(n\ge4),
\]
with \(R_n\) omitted for \(n=3\). Every maximum is attained by an input edge-sign vector.

More strikingly, the sharp optimization over **all positive exceptional-edge conductances** is
\[
\boxed{\sup_{c>0}\|\Pi_c\|_{\ell^\infty\to\ell^\infty}
=\frac{1+\sqrt{2n-3}}2.}
\]
It is attained at \(c=c_*\), where
\[
\sqrt{c_*}=\frac{1+\sqrt{2n-3}}2.
\]
Thus the unweighted norm \(2(n-1)/n<2\) can grow to order \(\sqrt{n/2}\) by changing only one edge conductance. This concerns symmetrically conductance-rescaled edge coordinates, not unscaled physical currents.

## Assumptions and scope
All edges are present and have strictly positive conductance, and \(n\) is an integer at least three. Matrices act over the real field. The induced maximum norm is taken on the full edge-coordinate space, so the row-sum formula applies. The Moore--Penrose inverse is defined by the graph Laplacian. Orientation changes merely conjugate the projection by diagonal signs and leave the norm invariant.

## Proof
Let \(b_e\) denote the incidence row of edge \(e\), and write \(e_0=\{1,2\}\), \(b_0=b_{e_0}\), \(Q=I-\mathbf1\mathbf1^{\mathsf T}/n\). For the unit-weight clique, the Laplacian is \(nQ\), while in the present graph
\[
L=nQ+(c-1)b_0b_0^{\mathsf T}.
\]
Since \(b_0^{\mathsf T}b_0=2\) and \(b_0\perp\mathbf1\), inversion on the mean-zero subspace gives exactly
\[
L^+=\frac Qn-\frac{c-1}{n(n-2+2c)}b_0b_0^{\mathsf T}.
\]
Therefore every transfer-current entry is explicitly
\[
(\Pi_c)_{ef}=\sqrt{c_ec_f}\left[
\frac{b_e^{\mathsf T}b_f}n-
\frac{(c-1)(b_e^{\mathsf T}b_0)(b_f^{\mathsf T}b_0)}{nD}
\right].
\]
For the exceptional row, its diagonal entry is \(2c/D\), the absolute entry for each of the \(2(n-2)\) incident neighboring edges is \(\sqrt c/D\), and all other entries vanish. Its absolute row sum is \(E_n(c)\).

For an ordinary edge adjacent to exactly one exceptional endpoint, the absolute row sum is obtained by splitting edges into the exceptional edge, its own diagonal, edges sharing the same exceptional endpoint, edges sharing the other exceptional endpoint, the edge joining its two nonexceptional/exceptional endpoints, and edges sharing only its nonexceptional endpoint. Their contributions, respectively, are
\[
\frac{\sqrt c}D,\quad
\frac{2n-3+3c}{nD},\quad
\frac{(n-3)(n-2+c)}{nD},\quad
\frac{(n-3)|c-1|}{nD},\quad
\frac{n-3+3c}{nD},\quad
\frac{n-3}n.
\]
Summing and resolving \(|c-1|\) yields the two displayed expressions for \(A_n(c)\). For an edge disjoint from both exceptional endpoints, the correction term vanishes; its row has diagonal magnitude \(2/n\) and \(2(n-2)\) additional entries of magnitude \(1/n\), giving \(R_n\). For \(n=3\) no such remote edge exists. The maximum absolute row sum is the induced \(\ell^\infty\) norm, and for any maximizing row the signs of its entries supply a norm-one, norm-attaining input.

It remains to optimize over \(c\). In the variable \(t=\sqrt c\),
\[
E_n(t)=\frac{2(t^2+(n-2)t)}{n-2+2t^2}.
\]
Its derivative has the sign of \(n-2+2t-2t^2\). Hence its unique positive maximizer is
\[
t_*=(1+\sqrt{2n-3})/2,
\]
and the critical relation \(2t_*^2=2t_*+n-2\) simplifies its maximum to exactly \(E_n(t_*)=t_*\).

To prove that no other row exceeds \(t_*\), first take \(0<t\le1\). Direct subtraction yields
\[
A_n(t)=1+\frac{n-3+t}{n-2+2t^2}\le2.
\]
For \(n\ge6\), \(t_*\ge2\), so this suffices. For \(n=3\), the sharp bound is \(A_3(t)\le1+1/(2\sqrt2)<t_*\). For \(n=4\), elementary differentiation gives \(A_4(t)\le1+(1+\sqrt2)/4<t_*\). For \(n=5\), the elementary inequality \(8t^2-5t+2>0\) implies \(A_5(t)<9/5<t_*\). Also \(R_n<2\), and direct comparison gives \(R_n<t_*\) for \(3\le n\le5\).

For \(t\ge1\), direct subtraction gives
\[
A_n(t)-R_n
=\frac{(t-1)(n-2t-2)}{n(n-2+2t^2)},
\]
\[
E_n(t)-A_n(t)
=\frac{(t-1)\{2n^2-7n+6-(2n-6)t\}}{n(n-2+2t^2)}.
\]
If \(t\ge(n-2)/2\), then \(A_n(t)\le R_n<t_*\). If \(1\le t\le(n-2)/2\), a nonempty case only for \(n\ge4\), the bracket in the second displayed difference is at least \(n(n-2)>0\), so \(A_n(t)\le E_n(t)\le t_*\). Combining the ranges proves the sharp optimization and attainment.

## Verification
The standalone `verify.py` reconstructs the grounded weighted graph Laplacian for every \(3\le n\le9\) and nine positive rational values of \(\sqrt c\), inverts it exactly over the rationals, and computes the actual symmetric electrical projector without using the closed-form pseudoinverse. It compares all 1,071 edge row sums against the three closed formulas. It additionally performs 588 parameter-bound spot checks over \(3\le n\le100\). All passed. The analytical derivative, factorization and row counting, rather than the finite checks, prove the all-parameter theorem.

## Relationship to prior work
Kelner and Maymounkov (2009, arXiv:0909.2859v1) develop electrical routing operators and prove universal estimates for operator norms of electrical-flow projections; their Appendix A derives a general square-root-of-edge-count bound from orthogonal projection. Those bounds do not yield the sharp one-parameter formula or the optimized \(\sqrt n\) law for a fully connected weighted graph. Kassel and Wu (2013, arXiv:1312.2946) study transfer-current matrices in spanning-tree scaling limits; their subject provides a related matrix formulation, rather than the stated exact finite exceptional-edge norm. Standard weighted-network identities are described in Aldous and Fill's notes. The result here addresses the exact induced endpoint norm in symmetrically scaled edge coordinates; it is not a claim about oblivious-routing competitive ratios or random-edge average current lengths.

## Limitations
The classification assumes one exceptional edge and all other conductances equal. It does not determine analogous exact norms for multiple exceptional edges, arbitrary weighted graphs, or unscaled physical-current coordinates. The usual priority uncertainty applies to possible equivalent historical rank-one network calculations not located in the inspected sources; absence of a search match is not a proof of novelty.

## References
1. Jonathan Kelner and Petar Maymounkov, *Electric routing and concurrent flow cutting*, arXiv:0909.2859v1, 15 September 2009, https://arxiv.org/abs/0909.2859 ; original manuscript: https://math.mit.edu/~kelner/publications/Electricroutingandconcurrentflowcutting.pdf .
2. Adrien Kassel and Wei Wu, *Transfer current and pattern fields in spanning trees*, arXiv:1312.2946v1, 10 December 2013, https://arxiv.org/abs/1312.2946 .
3. David Aldous and James Allen Fill, *Reversible Markov Chains and Random Walks on Graphs*, chapter 3.3, 2002 version, https://stat-www.berkeley.edu/users/aldous/RWG/Book_Ralph/Ch3.S3.html .
