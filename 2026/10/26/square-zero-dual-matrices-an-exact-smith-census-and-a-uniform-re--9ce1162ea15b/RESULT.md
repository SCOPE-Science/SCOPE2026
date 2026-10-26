# Square-zero dual matrices: an exact Smith census and a uniform residue-rank law

## Finding
Let \(q\) be any prime power, let \(R=\mathbb F_q[\varepsilon]/(\varepsilon^2)\), and let \(n\ge1\). For \(X\in M_n(R)\) satisfying \(X^2=0\), define \(r=\operatorname{rank}_{\mathbb F_q}(X\bmod\varepsilon)\). The Smith diagonal of \(X\) over \(R\) consists of \(r\) unit entries, \(t\) entries associated to \(\varepsilon\), and \(n-r-t\) zeros. Write \(s=n-2r\). The number \(C_{n,q}(r,t)\) of such matrices with prescribed \((r,t)\) is
\[
\boxed{C_{n,q}(r,t)={n\brack r}_q{n-r\brack r}_q\,|\operatorname{GL}_r(\mathbb F_q)|\,q^{2r(n-r)}{s\brack t}_q^2\,|\operatorname{GL}_t(\mathbb F_q)|,}
\]
for \(0\le r\le\lfloor n/2\rfloor\) and \(0\le t\le s\); it is zero otherwise. Empty products and \(\operatorname{GL}_0\) have value one. Here \({a\brack b}_q\) is the Gaussian binomial coefficient.

Let \(X_n\) be uniform among all square-zero matrices in \(M_n(R)\) and put \(R_n=\operatorname{rank}(X_n\bmod\varepsilon)\) and \(D_n=n-2R_n-t(X_n)\). Set
\[
\Phi_j(q)=\prod_{i=1}^{j}(1-q^{-i}),\qquad \Phi_\infty(q)=\prod_{i=1}^{\infty}(1-q^{-i}).
\]
Then, for each fixed \(q\),
\[
\#\{X\in M_n(R):X^2=0\}=q^{n^2}\left(\frac{n}{2\Phi_\infty(q)}+O_q(1)\right).
\]
Moreover \(R_n/n\) converges in distribution to the uniform distribution on \([0,1/2]\), and jointly \((R_n/n,D_n)\) converges to the independent pair \((U,D)\), where \(U\) is uniform on \([0,1/2]\) and
\[
\Pr(D=d)=\frac{q^{-d^2}\Phi_\infty(q)}{\Phi_d(q)^2}\quad(d=0,1,2,\ldots).
\]
Thus the mod-\(\varepsilon\) rank does *not* concentrate near half the dimension, unlike the familiar field-level square-zero rank census.

## Assumptions and scope
The finite field may have any characteristic, including two. The result counts actual matrices, not similarity classes; Smith diagonal means equivalence under independent invertible left and right multipliers over the principal ideal ring \(R\). The invariants \(r,t\) are uniquely determined. The convention \({a\brack b}_q=0\) outside \(0\le b\le a\) is used, and \(n\) tends to infinity through all positive integers with \(q\) fixed in the limit theorems.

## Proof
**Residue rank and lifts.** Write \(X=A+\varepsilon B\), where \(A,B\in M_n(\mathbb F_q)\). Because \(\varepsilon^2=0\), the necessary and sufficient equations are
\[
A^2=0,\qquad AB+BA=0.
\]
If \(\operatorname{rank}A=r\), the inclusion \(\operatorname{im}A\subseteq\ker A\) forces \(0\le r\le\lfloor n/2\rfloor\). Choose a basis ordered as \(U,V,W\), with \(\dim U=\dim V=r\), \(\dim W=s=n-2r\), in which
\[
A=\begin{pmatrix}0&I_r&0\\0&0&0\\0&0&0\end{pmatrix}.
\]
Block multiplication gives the following *full* solution of the anticommutator equation, with independently arbitrary blocks of the stated sizes:
\[
B=\begin{pmatrix}P&Q&L\\0&-P&0\\0&M&T\end{pmatrix},
\]
where \(P,Q\) have size \(r\times r\), \(L\) has size \(r\times s\), \(M\) has size \(s\times r\), and \(T\) has size \(s\times s\). There are precisely
\[
q^{2r^2+2rs+s^2}=q^{n^2-2r(n-r)}
\]
choices of \(B\). The formula is valid without dividing by two, so also in characteristic two.

**Smith invariant.** Use the \(r\) unit pivots in the \(U\)-row, \(V\)-column of \(X\) to eliminate their rows and columns by invertible operations over \(R\). The remaining block is \(\varepsilon T\), together with zero rows and columns. In particular, the number \(t\) of \(\varepsilon\)-invariant factors equals \(\operatorname{rank}_{\mathbb F_q}T\). This also follows from the independent identity that the \(\mathbb F_q\)-linear matrix of multiplication by \(X\) on \(R^n\) has rank \(2r+t\). Since \(T\) ranges independently over all \(s\times s\) matrices, the number of eligible lifts with \(t\) fixed is
\[
q^{2r(n-r)}{s\brack t}_q^2|\operatorname{GL}_t(\mathbb F_q)|.
\]

**Counting residue matrices.** The number of \(A\in M_n(\mathbb F_q)\) satisfying \(A^2=0\) and \(\operatorname{rank}A=r\) is
\[
{n\brack r}_q{n-r\brack r}_q|\operatorname{GL}_r(\mathbb F_q)|.
\]
Indeed choose the image \(U\), choose a kernel containing it, and then choose the induced isomorphism from the quotient by the kernel to \(U\). Multiplying this count by the preceding lift count proves the boxed formula. Summing over \(t\) uses the standard count of all \(s\times s\) matrices, \(\sum_t{s\brack t}_q^2|\operatorname{GL}_t|=q^{s^2}\), and yields the exact residue-rank marginal
\[
\#\{X:X^2=0,\ \operatorname{rank}(X\bmod\varepsilon)=r\}
=q^{n^2}\frac{\prod_{j=n-2r+1}^{n}(1-q^{-j})}{\Phi_r(q)}.
\]

**Asymptotic flatness.** Uniformly over \(0\le r\le\lfloor n/2\rfloor\), the factor multiplying \(q^{n^2}\) in the last display differs from \(\Phi_\infty(q)^{-1}\) by at most \(O_q(q^{-r}+q^{-(n-2r)})\). The sum of this error over all permissible \(r\) is \(O_q(1)\). Thus the total is \(q^{n^2}(n/(2\Phi_\infty(q))+O_q(1))\), and the cumulative distribution satisfies, uniformly for \(0\le x\le1/2\),
\[
\Pr(R_n/n\le x)=2x+O_q(n^{-1}).
\]
This proves convergence of \(R_n/n\) to the stated continuous uniform law.

**Corank law and independence.** Conditional on \(R_n=r\), the \(s\times s\) block \(T\) is uniform. Its corank \(D_n=s-\operatorname{rank}T\) therefore satisfies
\[
\Pr(D_n=d\mid R_n=r)=q^{-d^2}\frac{\bigl(\Phi_s(q)/\Phi_d(q)\bigr)^2}{\Phi_{s-d}(q)},\quad 0\le d\le s.
\]
For fixed \(d\), this tends to \(q^{-d^2}\Phi_\infty(q)/\Phi_d(q)^2\) as \(s\to\infty\). The limiting masses sum to one: the union bound over \(d\)-dimensional subspaces of the kernel gives a uniform tail bound \(\Pr(D_n\ge d\mid s)\le{s\brack d}_q q^{-sd}=O_q(q^{-d^2})\). Except for a set of residue ranks of probability tending to zero, \(s=n-2R_n\to\infty\). Conditioning on the residue rank and using the uniform law then gives joint convergence and asymptotic independence.

## Verification
Run `python3 verify.py` with the standalone accompanying script. It directly enumerates matrices \(A,B\) over the prime fields \(\mathbb F_2,\mathbb F_3,\mathbb F_5\), tests \(A^2=AB+BA=0\), computes \(r\) by elimination, and obtains \(t\) from the rank of the induced \(2n\times2n\) \(\mathbb F_q\)-linear operator, without using the proof's block form. All joint strata match for \((q,n)=(2,1),(2,2),(2,3),(3,1),(3,2),(5,1),(5,2)\). In particular, the total counts are respectively \(2,28,1184,3,153,5,1225\). Separate exact integer identities confirm all \(t\)-sums for \(q\in\{2,3,4,5,7,8\}\) and \(1\le n\le34\). The finite checks do not constitute the general or asymptotic proofs.

## Relationship to prior work
Cheong, Liang, and Strand (first publicly posted 2022-09-08) study solutions of polynomial matrix equations over finite prime-power rings and cokernel distributions. Their Theorem 1.1 requires a polynomial square-free modulo the prime, and their main Theorem 1.3 requires irreducibility modulo the prime. They explicitly identify non-square-free reductions as outside their method. The equation \(X^2=0\) has repeated-root polynomial \(z^2\), so neither theorem implies this census; moreover, the coefficient ring here is the equal-characteristic dual-number ring.

The public note *Exact nilpotency-index distribution for Jordan lifts over finite dual numbers* determines nilpotency indices in the fixed fiber over one long Jordan block. It covers neither the simultaneous residue-rank and Smith distribution of *square-zero* matrices nor the uniform-rank limit. The public note *Exact strongly nil-clean census over finite dual numbers* counts a much larger locus containing the square-zero matrices and has no square-zero or Smith-rank refinement. Classical finite-field nilpotent enumerations count residue matrices but not their anticommuting dual lifts or limiting flat law. Bollman--Ramírez and Brawley treat nilpotent and Drazin-index enumerations over different finite rings; a stronger implicit consequence of their formulas is an unresolved historical coverage risk.

## Limitations
The theorem concerns square-zero matrices over the length-two equal-characteristic principal local ring only. It does not classify similarity classes, count higher nilpotency indices, or extend directly to \(\mathbb Z/p^2\mathbb Z\) or longer chain rings. It is a self-contained derivation with self-review, not independently audited, and publication priority remains subject to further historical literature comparison (particularly older finite-ring matrix enumerations).

## References
1. G. Cheong, Y. Liang, and M. Strand, *Polynomial equations for matrices over integers modulo a prime power and the cokernel of a random matrix*, arXiv:2209.03626v1 (first posted 2022-09-08), https://arxiv.org/abs/2209.03626; especially the introduction, Theorems 1.1 and 1.3, and Remark 1.2 of v3.
2. *Exact nilpotency-index distribution for Jordan lifts over finite dual numbers*, public research note (2026), https://github.com/Resultary/2026/tree/main/2026/10/4/SCOPE-exact-nilpotency-index-distribution-for-jordan-lifts-over-finite--a669645ca0b7.
3. *Exact strongly nil-clean census over finite dual numbers*, public research note (2026), https://github.com/Resultary/2026/tree/main/2026/10/4/SCOPE-exact-strongly-nil-clean-census-over-mathbb-f-q-varepsilon-varep--0c1ad928a72e.
4. D. Bollman and H. Ramírez, *On the number of nilpotent matrices over* \(\mathbb Z_m\), *J. Reine Angew. Math.* 238 (1969). Historical context; original full text was not obtained.
5. J. V. Brawley, *Counting matrices by Drazin index*, *SIAM J. Algebraic Discrete Methods* 3 (1982), 30--34, https://doi.org/10.1137/0603003. Abstract and references inspected; full text unavailable.
