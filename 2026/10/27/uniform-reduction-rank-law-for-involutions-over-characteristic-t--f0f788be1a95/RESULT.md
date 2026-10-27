# Uniform reduction-rank law for involutions over characteristic-two finite dual numbers

## Finding
Let \(q=2^f\) with integer \(f\ge1\), and put \(R=\mathbb F_q[\varepsilon]/(\varepsilon^2)\). For \(n\ge1\), set
\[
\Phi_k(q)=\prod_{i=1}^{k}(1-q^{-i}),\quad \Phi_0(q)=1,\qquad
\Phi_\infty(q)=\prod_{i=1}^\infty(1-q^{-i}).
\]
An **involution** here means a matrix \(U\in\operatorname{GL}_n(R)\) with \(U^2=I\), including the identity. Write \(\overline U\) for reduction modulo \(\varepsilon\) and \(r(U)=\operatorname{rank}_{\mathbb F_q}(\overline U-I)\). Then for each integer \(0\le r\le\lfloor n/2\rfloor\),
\[
\#\{U:U^2=I,\ r(U)=r\}
=\frac{|\operatorname{GL}_n(\mathbb F_q)|}
{\Phi_r(q)\Phi_{n-2r}(q)}.\tag{1}
\]
Consequently, with \(m=\lfloor n/2\rfloor\) and \(U\) uniform among these solutions,
\[
\Pr(r(U)=r)=\frac{[\Phi_r(q)\Phi_{n-2r}(q)]^{-1}}
{\sum_{j=0}^{m}[\Phi_j(q)\Phi_{n-2j}(q)]^{-1}}.\tag{2}
\]
More sharply, if \(\mathrm{Unif}_m\) denotes discrete uniform measure on \(\{0,\ldots,m\}\), then
\[
\left\|\mathcal L(r(U))-\mathrm{Unif}_m\right\|_{\mathrm{TV}}
\le \frac{C_q}{m+1},\qquad
C_q=\frac{q/(q-1)+1/(1-q^{-2})}{q-1}.\tag{3}
\]
For each fixed \(q\), as \(n\to\infty\),
\[
\frac{2r(U)}{n}\Longrightarrow\operatorname{Unif}[0,1],\qquad
\#\{U\in\operatorname{GL}_n(R):U^2=I\}
\sim\frac{n|\operatorname{GL}_n(\mathbb F_q)|}{2\Phi_\infty(q)^2}.\tag{4}
\]
This contrasts with the strong concentration of reduction ranks among involutions over the residue field alone.

## Assumptions and scope
The coefficient field has characteristic exactly two, the local ring is the **split** length-two dual-number ring, and matrices have arbitrary positive size \(n\). No assertion is made for \(\mathbb Z/4\mathbb Z\), rings of length three, or odd characteristic. The rank is a rank **after reduction**, not the rank of the endomorphism over the ring. All finite formulas include \(U=I\); subtract one from the total when counting elements of order exactly two. The asymptotic assertion keeps \(q\) fixed.

## Proof
**Step 1: reduction of the involution equation.** Every matrix over the dual-number ring is uniquely \(U=A+\varepsilon B\) with \(A,B\in M_n(\mathbb F_q)\). Since \(\operatorname{char}(\mathbb F_q)=2\) and \(\varepsilon^2=0\),
\[
U^2=I\quad\Longleftrightarrow\quad
A^2=I,\quad AB+BA=0.
\]
The first equation implies \(A=I+N\) for a unique square-zero matrix \(N^2=0\). Conversely every such \(N\) gives invertible \(A\). The second equation becomes \(NB+BN=0\), which in characteristic two means \(NB=BN\). Since \(U\) reduces to the invertible matrix \(A\), it is automatically invertible over \(R\). Thus, for each rank \(r\), solutions correspond bijectively to pairs \((N,B)\) with \(N^2=0\), \(\operatorname{rank}(N)=r\), and \(B\) in the full matrix centralizer of \(N\).

**Step 2: a direct centralizer calculation.** A square-zero \(N\) of rank \(r\) necessarily has \(2r\le n\). Put \(s=n-2r\). Choose vector-space decompositions with basis ordered so that \(N\) has only the \((1,3)\) block \(I_r\) for block sizes \((r,s,r)\). An elementary block multiplication shows that all and only matrices commuting with \(N\) have the form
\[
B=\begin{pmatrix}
P&X&Y\\0&Q&Z\\0&0&P
\end{pmatrix},
\]
where \(P\in M_r(\mathbb F_q)\), \(Q\in M_s(\mathbb F_q)\), \(X\in M_{r\times s}(\mathbb F_q)\), \(Y\in M_r(\mathbb F_q)\), and \(Z\in M_{s\times r}(\mathbb F_q)\). The centralizer algebra therefore has dimension
\[
d_r=2r^2+2rs+s^2.
\]
Hence there are exactly \(q^{d_r}\) choices of \(B\), and its invertible members number
\[
q^{d_r-r^2-s^2}|\operatorname{GL}_r(\mathbb F_q)||\operatorname{GL}_s(\mathbb F_q)|
=q^{d_r}\Phi_r(q)\Phi_s(q).
\]
The formulas remain valid at \(r=0\) and \(s=0\), taking \(\operatorname{GL}_0\) as a singleton.

**Step 3: orbit-stabilizer and exact count.** All rank-\(r\) square-zero matrices are conjugate over \(\mathbb F_q\), because their Jordan blocks have only sizes one and two, and the multiplicities are fixed by \(r\). The \(\operatorname{GL}_n(\mathbb F_q)\)-orbit of \(N\) therefore has size
\[
\frac{|\operatorname{GL}_n(\mathbb F_q)|}
{q^{d_r}\Phi_r(q)\Phi_s(q)}.
\]
Each such \(N\) admits \(q^{d_r}\) commuting matrices \(B\). The two factors cancel, proving (1) for every admissible \(r\); the above bijection excludes all other ranks. Normalization gives (2).

**Step 4: quantitative uniformity.** Write \(a_k=\Phi_\infty(q)/\Phi_k(q)=\prod_{i>k}(1-q^{-i})\). Then \(0<a_k\le1\) and, by the elementary product inequality,
\[
0\le1-a_k\le\sum_{i>k}q^{-i}=\frac{q^{-k}}{q-1}.
\]
Put \(b=\Phi_\infty(q)^{-2}\), \(w_r=[\Phi_r(q)\Phi_{n-2r}(q)]^{-1}=b a_r a_{n-2r}\), and \(W=\sum_{r=0}^m w_r\). Thus
\[
0\le (m+1)b-W
\le \frac b{q-1}\left(\sum_{r=0}^{m}q^{-r}
+\sum_{r=0}^{m}q^{-(n-2r)}\right)
\le b C_q.
\]
(The second geometric sum has exponents of one parity, descending from \(n\) to zero or one.) By the triangle inequality,
\[
\frac12\sum_{r=0}^m\left|\frac{w_r}{W}-\frac1{m+1}\right|
\le\frac{(m+1)b-W}{(m+1)b}\le\frac{C_q}{m+1},
\]
which proves (3). As \(n\to\infty\), \(m\to\infty\); rescaling discrete uniform measure by \(2/n\) gives the continuous uniform limit. Also \(W=(m+1)b+O_q(1)\) by the bound above, so (1) summed over all ranks gives the asymptotic (4). No finite-size experiment is used in these deductions.

## Verification
A standalone standard-library Python checker, `verification/check_involutions.py`, exhaustively enumerates both coefficients of every matrix over \(\mathbb F_2[\varepsilon]/(\varepsilon^2)\) in sizes one to three and over \(\mathbb F_4[\varepsilon]/(\varepsilon^2)\) in sizes one and two. It tests the multiplication equation and residue rank directly; it does not use formula (1) to construct the counted matrices. It checks all rank strata against the independently evaluated closed formula and checks integrality for \(q=2\) and \(1\le n\le11\). Across five finite configurations, \(327956\) matrices over the dual-number ring are examined; an independent program output is embedded as `verification/check_output.txt`. Reproduce with `python verification/check_involutions.py` from the package root. These finite checks corroborate but do not prove the all-rank and asymptotic assertions.

## Relationship to prior work
Fulman–Guralnick–Stanton, Proposition 3.1, gives exact ranks for involutions in \(\operatorname{GL}_n(\mathbb F_q)\) over the **field**; its rank multiplicities have a different (concentrated) shape. Stasinski investigates representation theory of special linear groups over length-two local rings and describes the reduction-kernel structure and centralizers; the enumerative cancellation and uniform-rank asymptotic of (1)–(4) are not established in the inspected material. Earlier work by Brawley–Gamble studies similarity classification of involutory matrices over finite commutative rings and counts the case of integer residue rings modulo powers of two; this is the closest broad structural priority risk, because a fully accessible text was not obtained. Gazaryan studies similarity of involutory matrices over local rings of characteristic a power of two; only abstract-level material was accessible. The exact rank-refined formula and quantitative uniformity for split characteristic-two dual numbers were not found in the examined accessible literature, and no exhaustive uniqueness claim is made.

## Limitations
The counting proof is self-contained, but assessment of historical precedence is limited by incomplete access to some original similarity-classification papers and possible equivalents written in module-theoretic language. The uniformity constant depends on the fixed field order, and the result does not apply to characteristic-four Witt-vector rings. The finite checker does not exhaust general \(n\) or prove asymptotics. No independent mathematical audit has been performed.

## References
1. A. Stasinski, *Representations of \(\mathrm{SL}_n\) over finite local rings of length two*, arXiv:1907.09878 (first submitted 2019-07-23), https://arxiv.org/abs/1907.09878. The original 2019 source for the length-two ring setting.
2. J. Fulman, R. Guralnick, D. Stanton, *Asymptotics of the number of involutions in finite classical groups*, arXiv:1602.03611, Proposition 3.1, https://arxiv.org/abs/1602.03611. Field involution counts and asymptotics.
3. J. V. Brawley and R. O. Gamble, *Involutory matrices over finite commutative rings*, Linear Algebra and its Applications 21 (1978), 175–188, DOI:10.1016/0024-3795(78)90041-1. Abstract accessed; full text not accessed.
4. T. G. Gazaryan, *Similarity of involutive matrices over a local ring of characteristic \(2^k\)*, Discrete Mathematics and Applications 5 (1995), 587–601, https://www.mathnet.ru/eng/dm600. Abstract accessed; full text not accessed.
