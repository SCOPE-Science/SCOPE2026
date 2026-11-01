# Sharp quasi-Schatten threshold for the second Cesàro–Mellin defect

## Finding

On \(\ell^2(\mathbb N)\), index rows and columns by positive integers and define
\[
C_{jk}=\frac{\mathbf 1_{\{k\le j\}}}{j},\qquad
W_{jk}=\frac{\mathbf 1_{\{k\le j\}}}{j}\log\frac jk,
\qquad D=C^2-W.
\]
Then \(D\) belongs to the Schatten quasi-ideal \(\mathcal S_p\) **if and only if** \(p>1/2\). More precisely, there is an absolute constant \(K<\infty\) such that
\[
s_n(D)\le Kn^{-2}\quad(n\ge1),\qquad D\in\mathcal S_{1/2,\infty}\setminus\mathcal S_{1/2}.
\]
The Fredholm determinant and the nonzero eigenvalues, with algebraic multiplicity, are
\[
\det(I-zD)=\prod_{j=1}^{\infty}\left(1-\frac z{j^2}\right)
=\frac{\sin(\pi\sqrt z)}{\pi\sqrt z},
\qquad \lambda_j(D)=j^{-2}\quad(j\ge1).
\]
The quotient at \(z=0\) is interpreted by continuity; its power series is entire. For each integer \(r\ge1\), \(\operatorname{Tr}(D^r)=\zeta(2r)\). The new statement is the sharp quasi-Schatten membership and weak critical bound; the first-power trace is known from earlier work.

## Assumptions and scope

\(C\) is the classical one-based Cesàro operator; \(W\) is the sampled Mellin kernel for the second multiplicative power of \(\mathbf1_{(0,1]}\). Both are bounded on \(\ell^2\), and the displayed difference defines a bounded operator. Let \(H_j=\sum_{h=1}^j1/h\) and \(H_0=0\). Direct multiplication gives the exact lower-triangular matrix
\[
D_{jk}=\frac{\mathbf1_{\{k\le j\}}}{j}
\left(H_j-H_{k-1}-\log\frac jk\right).
\]
The singular values \(s_n(D)\) are numbered in decreasing order with multiplicity. For \(0<p<1\), \(\mathcal S_p\) is the usual Schatten quasi-ideal; \(\mathcal S_{1/2,\infty}\) means \(\sup_{n\ge1}n^2s_n(D)<\infty\). No optimal leading coefficient for \(s_n(D)\) is asserted.

## Proof

**Step 1: a two-term exact decomposition.** Write \(\gamma\) for Euler's constant and put
\[
R_j=H_j-\log j-\gamma,\qquad
S_k=H_{k-1}-\log k-\gamma.
\]
Standard integral comparison of harmonic sums gives \(|R_j|\le c/j\) and \(|S_k|\le c/k\), for one absolute \(c\) and all positive indices. Thus
\[
D_{jk}=\mathbf1_{\{k\le j\}}\left(\frac{R_j}{j}-\frac{S_k}{j}\right).
\tag{1}
\]
These bounds and the decomposition are exact, not finite-section approximations.

**Step 2: dyadic diagonal blocks.** Partition \(\mathbb N\) into \(I_m=\{2^m,\ldots,2^{m+1}-1\}\) for \(m\ge0\), and write \(N_m=2^m\). Let \(B\) be the direct sum of the \(I_m\)-diagonal compressions of \(D\), and put \(F=D-B\). Let \(L_N\) be the \(N\)-by-\(N\) lower triangular all-ones matrix. On \(I_m\), (1) becomes
\[
B_m=\operatorname{diag}(R_j/j)L_{N_m}
-\operatorname{diag}(1/j)L_{N_m}\operatorname{diag}(S_k),
\]
where the diagonals are restricted to the same block. Each diagonal coefficient in either product is bounded by a constant times \(N_m^{-1}\) on both sides, so the ideal inequality yields
\[
s_r(B_m)\le c_1N_m^{-2}s_{\lceil r/2\rceil}(L_{N_m}).
\tag{2}
\]
For every \(N\) and \(1\le r\le N\),
\[
s_r(L_N)\le c_2\frac Nr.
\tag{3}
\]
Indeed, for \(r\ge2\) partition \(\{1,\ldots,N\}\) into \(r-1\) consecutive nearly equal intervals; delete the within-interval lower-triangular pieces of \(L_N\). The remaining matrix is constant on each interval of rows and has rank at most \(r-1\). The discarded direct-sum operator has norm at most \(\lceil N/(r-1)\rceil\); the approximation-number characterization of \(s_r\) gives (3), with \(r=1\) following from \(\|L_N\|\le N\). Consequently,
\[
s_r(B_m)\le \frac{c_3}{N_mr}\quad(1\le r\le N_m).
\tag{4}
\]
Counting singular values above \(t>0\) in the orthogonal direct sum and using (4) gives
\[
\begin{split}
N_B(t)&:=\#\{r:s_r(B)>t\}\\
&\le \sum_{m\ge0}\min\left(N_m,\frac{c_3}{N_mt}\right)
\le c_4t^{-1/2}.
\end{split}
\tag{5}
\]
For the last inequality sum the geometric series separately over \(N_m\le t^{-1/2}\) and \(N_m>t^{-1/2}\). Enlarging the constant handles all \(t>0\). Thus \(s_r(B)=O(r^{-2})\).

**Step 3: off-diagonal blocks are in every Schatten quasi-ideal.** For \(m>\ell\), all entries in the rectangle \(I_m\times I_\ell\) satisfy \(k<j\), so (1) yields the sum of exactly two rank-one matrices:
\[
F_{m\ell}=(R_j/j)_{j\in I_m}(1)_{k\in I_\ell}^{*}
-(1/j)_{j\in I_m}(\overline{S_k})_{k\in I_\ell}^{*}.
\]
For these two rank-one terms, their sole nonzero singular values are respectively bounded by
\[
c_5N_\ell^{1/2}N_m^{-3/2},\qquad
c_5N_\ell^{-1/2}N_m^{-1/2}.
\tag{6}
\]
Since \(N_m=2^m\), the sum of the \(p\)-th powers of both quantities over \(m>\ell\ge0\) is finite for every fixed \(p>0\); their ordinary first powers also have finite sum. Partial sums of these rank-one operators therefore converge to \(F\) in \(\mathcal S_p\) for \(0<p\le1\), using the \(p\)-triangle inequality, and in trace norm for \(p>1\). In particular \(F\in\mathcal S_{1/4}\), whence \(s_r(F)=O(r^{-4})\).

**Step 4: upper bound and sharp threshold.** The singular-value sum inequality
\[
s_{2r-1}(B+F)\le s_r(B)+s_r(F)
\]
combined with (5) and Step 3 gives \(s_r(D)=O(r^{-2})\). Hence \(D\in\mathcal S_p\) whenever \(p>1/2\), and it belongs to the weak endpoint \(\mathcal S_{1/2,\infty}\). In particular it is trace class.

On the other hand, the diagonal of \(D\) is exactly \(D_{jj}=j^{-2}\). Every power \(D^r\) is lower triangular with diagonal \(j^{-2r}\). As the powers are trace class,
\[
\operatorname{Tr}(D^r)=\sum_{j\ge1}j^{-2r}=\zeta(2r)
\qquad(r=1,2,\ldots).
\]
The trace-class Fredholm determinant identity for sufficiently small \(|z|\) gives
\[
\begin{split}
\log\det(I-zD)&=-\sum_{r\ge1}\frac{z^r}{r}\operatorname{Tr}(D^r)\\
&=\sum_{j\ge1}\log(1-z/j^2).
\end{split}
\]
By analyticity this proves the determinant product for all complex \(z\); Euler's sine product gives the displayed closed form. Its zeros are exactly the distinct positive squares, hence the nonzero eigenvalues of \(D\) are the simple numbers \(j^{-2}\). Weyl's inequality for eigenvalue and singular-value \(p\)-sums implies
\[
\sum_{j\ge1}|\lambda_j(D)|^p\le\sum_{j\ge1}s_j(D)^p.
\]
For \(p\le1/2\), the left side is \(\sum_{j\ge1}j^{-2p}=\infty\), excluding \(\mathcal S_p\) and completing the proof.

## Verification

The accompanying `checker.py` tests exact rational identities for finite Cesàro squares, independent matrix formation, dyadic diagonal-block decompositions, rank-two off-block structure and sampled singular values. It uses Python 3 and NumPy; execute `python3 checker.py`. A recorded check performed 174,080 finite assertions. The estimates (2)–(6), the ideal argument, and the determinant proof are analytic and do not follow from finite computation. There is no claim to an exact constant in the singular-value asymptotic.

## Relationship to prior work

Bellavita–Stylogiannis introduced sampled-ratio Mellin matrices and proved that their general multiplicativity defect belongs to \(\mathcal S_2\). The particular classical Cesàro defect \(C^2-W\) was subsequently shown in a separate 2026 mathematical note to be trace class with trace \(\zeta(2)\). **Neither the general \(\mathcal S_2\) theorem nor that trace-class result determines the sharp \(\mathcal S_p\) cutoff for \(p<1\)**. The present result sharpens membership for this canonical defect to the exact threshold \(p>1/2\), including the critical weak bound, and computes its complete Fredholm determinant. Bellavita–Dellepiane–Stylogiannis study Schatten membership of Rhaly matrices themselves, a distinct class of operators from the difference \(D\).

## Limitations

Only the second Cesàro–Mellin multiplicativity defect is treated. The proof does not establish an optimal coefficient or limit for \(n^2s_n(D)\), nor a universal Schatten refinement for arbitrary Mellin kernels. The determinant follows from the trace-class property and triangular diagonal; this elementary spectral consequence is not offered as a separate priority claim. Broader preexisting trace-ideal estimates or dyadic approximation results might imply the threshold indirectly and remain a residual priority risk. All review here is self-review; independent verification and definitive priority assessment have not been conducted.

## References

1. C. Bellavita and G. Stylogiannis, *A discrete Mellin calculus in the Toeplitz algebra*, arXiv:2609.09453v1, initially submitted 8 September 2026. https://arxiv.org/abs/2609.09453
2. *Trace-class Mellin semigroup defects and zeta traces for Cesàro powers*, public mathematical note, 19 September 2026. https://github.com/Resultary/2026/tree/main/2026/9/19/SCOPE-zeta-trace-cesaro-mellin-defects--b8e60639c683
3. C. Bellavita, E. Dellepiane and G. Stylogiannis, *Boundedness, compactness and Schatten class for Rhaly matrices*, arXiv:2503.21930v1, initially submitted 27 March 2025. https://arxiv.org/abs/2503.21930
