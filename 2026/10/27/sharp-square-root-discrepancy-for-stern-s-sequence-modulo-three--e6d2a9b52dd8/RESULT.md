# Sharp square-root discrepancy for Stern’s sequence modulo three

## Finding

Define Stern's diatomic sequence by \(s(0)=0\), \(s(1)=1\), and \(s(2n)=s(n)\), \(s(2n+1)=s(n)+s(n+1)\) for \(n\ge1\). For each integer \(k\ge0\), put
\[
H_k=\#\{n:2^k\le n<2^{k+1},\ 3\mid s(n)\},\qquad d_k=4H_k-2^k.
\]

**Theorem.** The exact dyadic discrepancy satisfies
\[
d_0=-1,\quad d_1=-2,\quad d_{k+2}=-d_{k+1}-2d_k\qquad(k\ge0).
\]
Writing \(A(N)=\#\{0\le n<N:3\mid s(n)\}\), we have for every positive integer \(N\)
\[
A(N)=\frac N4+O(\sqrt N),\qquad
\limsup_{N\to\infty}\frac{|A(N)-N/4|}{\sqrt N}>0.
\]
Thus the exponent \(1/2\) in the global discrepancy estimate is sharp. The generating function of the dyadic discrepancies is exactly
\[
\sum_{k\ge0}d_k z^k=\frac{-1-3z}{1+z+2z^2}.
\]
The limiting density \(1/4\) was previously established; the contribution here is the exact fluctuation recurrence and the optimal quantitative convergence rate.

## Assumptions and scope

All counts concern nonnegative indices and the ordinary integer Stern sequence, reduced modulo \(3\). The statement holds for *all* positive integer cutoffs \(N\), not merely powers of two. The implicit upper-bound constant is absolute. It makes no claim about higher moduli or about a limiting constant in the normalized global discrepancy.

## Proof

**Finite-state description.** Consecutive Stern terms are coprime, by induction from \((s(0),s(1))=(0,1)\) under the elementary unimodular updates
\[
L(a,b)=(a,a+b),\qquad R(a,b)=(a+b,b).
\]
Thus modulo three each ordered pair \((s(n),s(n+1))\) belongs to the eight nonzero pairs in \(\mathbb F_3^2\). Number these states in the order
\[
(0,1),(0,2),(1,0),(1,1),(1,2),(2,0),(2,1),(2,2).
\]
Define \(M_{ij}\) as the number of the two transitions from state \(i\) to state \(j\). Direct substitution gives
\[
M=\begin{pmatrix}
1&0&0&1&0&0&0&0\\
0&1&0&0&0&0&0&1\\
0&0&1&1&0&0&0&0\\
0&0&0&0&1&0&1&0\\
0&1&1&0&0&0&0&0\\
0&0&0&0&0&1&0&1\\
1&0&0&0&0&1&0&0\\
0&0&0&0&1&0&1&0
\end{pmatrix}.
\]
Each row and column sums to two. Exact determinant expansion gives
\[
\det(tI-M)=t^2(t-2)(t-1)^3(t^2+t+2).
\]
Moreover, direct matrix multiplication gives the stronger squarefree annihilator
\[
M(M-I)(M-2I)(M^2+M+2I)=0.
\]
The attached exact-arithmetic checker reconstructs and checks the matrix, characteristic polynomial, and annihilator independently from the transition formulas. These identities imply that \(M\) is diagonalizable over \(\mathbb C\). The eigenvalue \(2\) is simple, with spectral projector \(J/8\), where \(J\) is the all-ones matrix, because the left and right eigenvectors are both uniform. Every other eigenvalue has absolute value at most \(\sqrt2\), since the two nonreal roots of \(t^2+t+2\) have modulus \(\sqrt2\).

**Arbitrary-prefix upper bound.** Consider any aligned binary block of indices \([a2^r,(a+1)2^r)\), where \(a,r\ge0\). Its states are exactly the \(2^r\) length-\(r\) descendants of the state attached to index \(a\). With \(f\) the column indicator of the two states having first coordinate zero, the number of admissible indices in this block equals \(e_aM^rf\), where \(e_a\) selects the initial state. The spectral decomposition proves, uniformly over all eight possible \(a\)-states,
\[
e_aM^rf=2^r/4+O(2^{r/2}).
\]
For every integer \(N\ge1\), decompose \([0,N)\) into the disjoint aligned binary blocks represented by the set bits of \(N\). There is at most one such block of each length \(2^r\). Summing the displayed bound over their sizes gives
\[
|A(N)-N/4|\le C\sum_{0\le r\le\lfloor\log_2N\rfloor}2^{r/2}=O(\sqrt N).
\]
This argument includes the initial state at \(a=0\) and is not restricted to dyadic endpoints.

**Exact level recurrence.** At level \(k=2\), the indices \(4,5,6,7\) realize once each the four axis states \((0,1),(0,2),(1,0),(2,0)\), and no other states. The transition formulas preserve equality of counts inside each of the following three classes: the four axis states, the two equal-coordinate states \((1,1),(2,2)\), and the two remaining states \((1,2),(2,1)\). Let \(U_k,V_k,W_k\) be the per-state counts in these classes. For \(k\ge2\),
\[
(U_2,V_2,W_2)=(1,0,0),\qquad
(U_{k+1},V_{k+1},W_{k+1})=(U_k+W_k,2U_k,2V_k).
\]
In particular \(H_k=2U_k\) and \(4U_k+2V_k+2W_k=2^k\). Eliminating \(V_k,W_k\) gives \(U_{k+3}=U_{k+2}+4U_k\) with characteristic polynomial \((t-2)(t^2+t+2)\). Removing the geometric \(2^k\)-component gives \(d_{k+2}=-d_{k+1}-2d_k\) for \(k\ge2\). Direct enumeration gives \((d_0,d_1,d_2,d_3)=(-1,-2,4,0)\), which verifies the same recurrence for \(k=0,1\). The displayed rational generating function follows immediately.

**Sharpness.** The roots \(\lambda_{\pm}=(-1\pm i\sqrt7)/2\) are distinct, nonreal, and have modulus \(\sqrt2\). The companion matrix for \((d_k,d_{k+1})\) is therefore similar over \(\mathbb R\) to a rotation followed by dilation by \(\sqrt2\). Because \((d_0,d_1)=(-1,-2)\ne(0,0)\), there exists an absolute \(c>0\) with
\[
\max(|d_k|,|d_{k+1}|)\ge c\,2^{k/2}\quad(k\ge0).
\]
Consequently \(|d_k|\ge c'2^{k/2}\) for infinitely many \(k\). Put \(D(N)=A(N)-N/4\). By the definition of \(d_k\),
\[
D(2^{k+1})-D(2^k)=d_k/4.
\]
At least one of these two endpoint discrepancies has absolute value at least \(|d_k|/8\). Since \(\sqrt{2^{k+1}}\le\sqrt2\,2^{k/2}\), infinitely many dyadic endpoints have discrepancy bounded below by a fixed positive multiple of their square root. This proves the claimed strict positive limsup.

## Verification

Run `python3 verify.py` using standard Python only; it creates the eight states from the two maps, checks the full characteristic polynomial by exact integer Newton identities, multiplies the squarefree annihilator, enumerates all Stern terms below \(2^{17}\), checks every available dyadic level recurrence and the three state classes, and compares every initial-prefix count with a generous uniform square-root envelope. A finite calculation alone would not establish the asymptotic theorem; the spectral and recurrence arguments above do so.

## Relationship to prior work

Deshouillers and Schinzel, *The modular distribution of Stern's sequence* (2019), Theorem 1.1 and Corollary 1.3, prove the density \(1/4\) of indices at which Stern's sequence vanishes modulo \(3\) and construct the general invertible finite-state automaton. Their Theorem 2.2 gives the qualitative frequency through Perron–Frobenius theory. The inspected eight-page primary paper does not calculate the second spectral radius or state an error term, a sharp global discrepancy exponent, or this three-term dyadic recurrence. Its automaton forms the starting point for the present explicit analysis. Bettin, Drappeau and Spiegelhofer (2017) study the statistical distribution of the *logarithms of the values* of Stern's sequence, a different distributional observable. OEIS A002487 records the sequence and related references, not a proof of the sharp modular discrepancy estimate. These comparisons do not exclude an unindexed independent derivation.

## Limitations

The main modulus is exactly \(3\). The proof provides absolute constants but does not identify an exact global limsup constant or characterize the full set of sharp cutoffs. The recurrence and eigenanalysis are elementary finite-state computations, not a claimed new general theorem about arbitrary automata. The literature comparison may miss prior equivalent explicit calculations.

## References

1. J.-M. Deshouillers and A. Schinzel, *The modular distribution of Stern's sequence*, Banach Center Publications **118** (2019), 37–44, DOI `10.4064/bc118-3`, https://www.impan.pl/shop/publication/transaction/download/product/113097 .
2. S. Bettin, S. Drappeau and L. Spiegelhofer, *Statistical distribution of the Stern sequence*, arXiv:1704.05253 (first posted 2017-04-18), https://arxiv.org/abs/1704.05253 .
3. OEIS A002487, *Stern's diatomic series*, https://oeis.org/A002487 .
