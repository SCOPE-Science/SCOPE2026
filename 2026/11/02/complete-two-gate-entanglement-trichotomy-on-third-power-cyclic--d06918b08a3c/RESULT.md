# Complete two-gate entanglement trichotomy on third-power cyclic graph states

## Finding
Let \(n\ge4\) be divisible by four. Prepare the standard qubit graph state associated with the third power of the cycle \(C_{2n}^{3}\): vertices \(0,1,\ldots,2n-1\), with an edge between vertices of cyclic distance one, two, or three. Use the checkerboard partition \(E=\{0,2,\ldots,2n-2\}\) and \(O=\{1,3,\ldots,2n-1\}\). Its initial bipartite entropy is \(n-3\) bits.

Omit exactly two distinct controlled-\(Z\) gates, from even vertex \(0\) to odd vertex \(2t+1\), and from even vertex \(2d\) to odd vertex \(2(d+u)+1\), where indices are modulo \(2n\), \(1\le d\le n-1\), and \(t,u\in\{-2,-1,0,1\}\). These are precisely all pairs of cross-cut edges having different even endpoints, up to cyclic translation by an even number.

The resulting graph state has bipartite von Neumann entropy \(S=n-3+\Delta\) bits, with the **complete trichotomy**

\[
\Delta=\begin{cases}
1,&d\not\equiv0\pmod4\ \text{and}\ d+u-t\equiv0\pmod4,\\
2,&d\not\equiv0\pmod4\ \text{and}\ d+u-t\not\equiv0\pmod4,\\
0,&d\equiv0\pmod4,\ t=u\in\{-1,0\},\\
1,&d\equiv0\pmod4\ \text{in all other cases}.
\end{cases}
\]

Every nonzero Schmidt coefficient is equal, so the same number \(S\) is also the entropy of every positive-order Rényi entropy. In particular, removing two near-neighbor edges at spacing divisible by four can leave this partition's entanglement **unchanged**, whereas other pairs of missing gates increase it by one or two bits.

## Assumptions and scope
The graph state is pure and ideal except for precisely two absent (rather than noisy or partially weighted) controlled-\(Z\) gates. It is defined by preparing \(\lvert+\rangle\) at each vertex and applying controlled-\(Z\) along all present graph edges. The cycle has \(2n\) vertices with \(4\mid n\), hence at least eight qubits. The checkerboard partition is the even-versus-odd vertex split. Edges between two even or two odd vertices are retained but do not affect Schmidt coefficients for this bipartition.

The two omitted edges have different even endpoints; they may or may not share an odd endpoint. The formula makes no assertion for two deleted edges incident on the *same* even vertex, for other system sizes, or for other bipartitions. All vector spaces and matrices in the proof are over \(\mathbb F_2\). The symbol \(e_j\) denotes the \(j\)-th standard column in \(\mathbb F_2^n\), with subscripts modulo \(n\).

## Proof
**Step 1: reduction to an explicit binary cut matrix.** The standard graph-state bipartition identity identifies entropy in bits with the \(\mathbb F_2\)-rank of the cross-cut adjacency matrix (Hein--Eisert--Briegel). Index even vertices by \(E_i=2i\) and odd vertices by \(O_j=2j+1\). A cross-cut edge appears when \(j-i\in\{-2,-1,0,1\}\) modulo \(n\). Thus the pristine cut matrix \(B\) acts by

\[
(Bz)_i=z_{i-2}+z_{i-1}+z_i+z_{i+1}.
\]

Let \(P\) be the cyclic shift \((Pz)_i=z_{i+1}\). In characteristic two,

\[
B=P^{-2}(I+P)^3,\qquad (I+P)^4=I+P^4.
\]

If \(Bz=0\), multiplication by \(I+P\) implies \(P^4z=z\). Conversely, a four-periodic \(z\) lies in the kernel exactly when its four components in one period sum to zero. Because \(4\mid n\), there are exactly three free components. Therefore \(\dim\ker B=3\) and \(\operatorname{rank}B=n-3\). The identical argument for the transpose shows \(\ker B^T\) is the same space of even-parity four-periodic sequences. In particular

\[
\operatorname{im}B=\operatorname{im}B^T=\left\{w:\sum_{j\equiv0\ (4)}w_j=\sum_{j\equiv1\ (4)}w_j=\sum_{j\equiv2\ (4)}w_j=\sum_{j\equiv3\ (4)}w_j\right\}.
\]

This is an equality of the four residue-class sums in \(\mathbb F_2\). The initial rank is also implied by the classical Smith-normal-form analysis of four-consecutive-ones circulants (Williams); the new statement here concerns the two missing gates.

**Step 2: general rank-two defect.** Removing the specified two gates toggles exactly two entries:

\[
B'=B+e_0e_t^T+e_de_{d+u}^T.
\]

The classes of two standard vectors \(e_a,e_b\) in \(\mathbb F_2^n/\operatorname{im}B\) are linearly independent if and only if \(a\not\equiv b\pmod4\); if their indices agree modulo four, their classes coincide and are nonzero. For a rank-two update \(B+UV^T\), if the two columns of \(U\) have linearly independent images in \(\operatorname{coker}B\), a vector \(z\) satisfies \((B+UV^T)z=0\) precisely when \(z\in\ker B\) and \(V^Tz=0\). Therefore

\[
\operatorname{rank}(B+UV^T)-\operatorname{rank}B
=\operatorname{rank}\left(V^T|_{\ker B}\right).
\]

By the description of \(\ker B\), evaluation at indices in distinct residue classes modulo four gives independent functionals, whereas two evaluations at indices in the same residue class are identical. Consequently, when \(d\not\equiv0\pmod4\), the two left defect columns are independent in the cokernel, and the entropy gain is two if \(t\not\equiv d+u\pmod4\) and one otherwise. When \(d\equiv0\pmod4\) but \(t\ne u\), the two right defect vectors have independent cokernel images instead. Apply the same argument to \((B')^T\) to obtain gain one.

**Step 3: the genuinely dependent case.** It remains to treat \(d\equiv0\pmod4\) and \(t=u\). Write \(d=4k\), with \(1\le k<n/4\), and introduce

\[
a=e_0,\quad c=e_d,\quad b=e_t,\quad f=e_{d+t},\quad r=a+c,\quad v=b+f.\]

Both \(r\in\operatorname{im}B\) and \(v\in\operatorname{im}B^T\) by the residue-class characterization, while \(a\notin\operatorname{im}B\). The original update may be rewritten

\[
B'=B+av^T+rf^T.
\]

Take the concrete preimage

\[
x=\sum_{j=0}^{k-1}(e_{4j+1}+e_{4j+2}),\qquad Bx=r.
\]

Indeed the length-four sliding sum of the two consecutive ones in each full internal block vanishes except at its two endpoints. Define \(s=v^Tx\in\mathbb F_2\). Direct evaluation of the four allowed offsets yields

\[
s=0\quad\text{for }t\in\{-1,0\},\qquad s=1\quad\text{for }t\in\{-2,1\}.
\]

Let \(z\in\ker B'\) and put \(\ell=f^Tz\). Projecting \(B'z=0\) to the cokernel and using \(a\notin\operatorname{im}B\) gives \(v^Tz=0\), and then \(Bz=r\ell\). Hence \(w=z+x\ell\in\ker B\). Since \(v\in\operatorname{im}B^T\), we have \(v^Tw=0\) and thus \(s\ell=0\). The definition of \(\ell\) gives the remaining scalar constraint

\[
(1+f^Tx)\ell=f^Tw.
\]

The functional \(w\mapsto f^Tw\) is nonzero on the three-dimensional \(\ker B\). If \(s=1\), the first constraint fixes \(\ell=0\), leaving the two-dimensional kernel \(\{w\in\ker B:f^Tw=0\}\); hence \(\operatorname{rank}B'=n-2\), a gain of one. If \(s=0\), the last scalar constraint yields a three-dimensional solution space regardless of whether its coefficient on \(\ell\) vanishes: either \(\ell\) is uniquely determined by every \(w\), or \(w\) satisfies one independent linear constraint and \(\ell\) is free. Thus \(\operatorname{rank}B'=n-3\), giving zero gain. The formulas cover every pair in scope.

**Step 4: complete Schmidt spectrum.** For a pure qubit graph state, the reduced density matrix across a bipartition is proportional to a projection with \(2^{\operatorname{rank}B'}\) equal nonzero eigenvalues. Its entropy for any positive Rényi order and at order one is therefore \(\operatorname{rank}B'\) bits, as claimed.

## Verification
Run `python3 verify.py`, using only the Python standard library. It builds each cross-cut matrix directly from the four physical cross-edge offsets, deletes every possible ordered pair with distinct even endpoints, and recomputes binary rank by independent bitwise Gaussian elimination. It exhaustively checks all \(8{,}448\) parameter triples for \(n\in\{4,8,\ldots,64\}\) against the piecewise formula and checks every pristine rank. The stored `verification_output.txt` includes the exact counted results. This finite census corroborates the symbolic proof but is not a proof for arbitrary \(n\).

## Relationship to prior work
Hein, Eisert and Briegel (arXiv:quant-ph/0307130, first public July 18, 2003) establish the graph-state cut-rank entanglement identity and stabilizer foundations; their Proposition 5 bounds changes of the multipartite Schmidt measure under a single edge operation, but does not classify the two-edge checkerboard entropy response here. Williams (2014), *Smith forms for adjacency matrices of circulant graphs*, Section 3.1, Theorem 3.1 and Corollary 3.3, treats the Smith normal form of matrices with a cyclic block of consecutive ones; the pristine \(n-3\) cut rank is already implied by those results and is not asserted as new. Campbell, Fitzsimons, Benjamin and Kok (arXiv:quant-ph/0606199, 2006) develop adaptive graph-state growth under monitored errors and weighted/partially fused edges, without a matching two-edge cyclic cut-rank classification in the inspected full text. The claimed contribution is the complete two-omitted-gate **placement-dependent trichotomy**, including exact cancellation, for this specific local ring family.

There is no claim that generic finite-rank perturbation bounds or the known undamaged circulant Smith forms are new. An unexamined specialized double-defect entanglement result or a broader arbitrary-two-entry circulant rank theorem remains a historical-priority risk; no independent priority certification is claimed.

## Limitations
The result does not quantify fidelity, robustness to coherent over/under-rotation, noise, or non-Clifford gates. It does not extend without proof to arbitrary numbers of missing bonds, pairs sharing the same even endpoint, other cyclic interaction ranges, other ring lengths, or other cuts. The binary rank algorithm is finite verification, not an infinite certificate. Independent external audit has not been performed.

## References
1. M. Hein, J. Eisert, H. J. Briegel, *Multi-party entanglement in graph states*, arXiv:quant-ph/0307130 (first posted July 18, 2003), https://arxiv.org/abs/quant-ph/0307130 ; full text https://arxiv.org/html/quant-ph/0307130v7 .
2. G. Williams, *Smith forms for adjacency matrices of circulant graphs*, Linear Algebra Appl. 443 (2014), 21–33, https://repository.essex.ac.uk/8578/1/SNRcirculantgraphs.pdf , especially Section 3.1 and Corollary 3.3.
3. E. T. Campbell, J. Fitzsimons, S. C. Benjamin, P. Kok, *Adaptive strategies for graph state growth in the presence of monitored errors*, arXiv:quant-ph/0606199 (June 23, 2006), https://arxiv.org/abs/quant-ph/0606199 .
