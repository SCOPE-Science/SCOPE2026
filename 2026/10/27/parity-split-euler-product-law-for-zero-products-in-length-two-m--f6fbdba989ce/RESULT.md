# Parity-split Euler-product law for zero products in length-two matrix rings

## Finding
Let \(R\) be any finite commutative chain ring with maximal ideal \((\pi)\), \(\pi^2=0\ne\pi\), and residue field \(\mathbb F_q\), where \(q\) is a prime power. For \(n\geq0\), choose an ordered pair \((X,Y)\) uniformly from
\[
\mathcal Z_n(R)=\{(X,Y)\in M_n(R)^2:XY=0\}.
\]
Write the Smith form of \(X\) as \(\operatorname{diag}(I_a,\pi I_b,0_c)\), so \(a,b,c\geq0\) and \(a+b+c=n\). Set \(h=a-c\). Both the exact finite distribution and the following limits are independent of the isomorphism type of \(R\), depending only on \(q\).

For \(0\leq k\leq m\), write
\[
G_q(m,k)={m\brack k}_q^2\prod_{i=0}^{k-1}(q^k-q^i),
\]
where \({m\brack k}_q\) is the Gaussian binomial coefficient, and the empty product is \(1\). **Exact formula:** the number of pairs in \(\mathcal Z_n(R)\) with Smith multiplicities \((a,b,c)\) for \(X\) is
\[
Q_{n,q}(a,b,c)=G_q(n,a)\,q^{2na-a^2}\,G_q(n-a,b)\,q^{n(b+2c)}.
\tag{1}
\]
All infeasible triples have count zero. In particular, \(Z_{n,q}=|\mathcal Z_n(R)|=\sum_{a+b+c=n}Q_{n,q}(a,b,c)\) is the exact number of ordered zero-product pairs in \(M_n(R)\).

Put
\[
\Phi_j(q)=\prod_{i=1}^{j}(1-q^{-i}),\quad
\Phi_\infty(q)=\prod_{i=1}^{\infty}(1-q^{-i}),\quad
P_\pm(q)=\prod_{j=1}^{\infty}(1\pm q^{-(j-1/2)}).
\]
For \(\sigma\in\{0,1\}\) define the strictly positive constants
\[
C_\sigma(q)=\frac{P_+(q)^3+(-1)^\sigma P_-(q)^3}{2}.
\tag{2}
\]
**Parity-split counting law:** for each fixed \(q\), along either parity subsequence \(n\equiv\sigma\pmod2\),
\[
Z_{n,q}=q^{5n^2/2}\bigl(C_\sigma(q)+o_q(1)\bigr),
\qquad
\frac{Z_{n,q}}{|M_n(R)|^2}=q^{-3n^2/2}\bigl(C_\sigma(q)+o_q(1)\bigr).
\tag{3}
\]
These are genuinely distinct parity constants since \(C_0(q)-C_1(q)=P_-(q)^3>0\).

**Limiting Smith law:** for each integer \(h\) and \(b\geq0\), the distribution of \((a-c,b)\) in a uniform zero-product pair converges in total variation, along \(n\equiv\sigma\pmod2\), to
\[
\Pr_\sigma(h,b)=
\begin{cases}
\displaystyle\frac{q^{-(h^2+b^2)/2}}{\Phi_\infty(q)\,\Phi_b(q)\,C_\sigma(q)},&h+b\equiv\sigma\pmod2,\\
0,&\text{otherwise}.
\end{cases}
\tag{4}
\]
Thus \(a\) and \(c\) are both \(n/2+O_{\Pr}(1)\), while the \(\pi\)-Smith multiplicity \(b\) remains a nondegenerate, tight random variable. For \(q=2\), the limiting probability that \(b>0\) along even \(n\) is approximately \(0.6898119281\). Equations (2)–(4), rather than the standard finite-field matrix-rank count, are the principal asymptotic contributions.

## Assumptions and scope
The ring is finite, commutative, unital, and has exactly the ideals \(0\subsetneq(\pi)\subsetneq R\), with \(\pi^2=0\). This includes \(\mathbb F_q[\varepsilon]/(\varepsilon^2)\) and the mixed-characteristic example \(\mathbb Z/p^2\mathbb Z\) when \(q=p\). No splitting of the coefficient field is assumed. The pair \((X,Y)\) is sampled **uniformly among all solutions** to \(XY=0\), not by first sampling \(X\) uniformly and then sampling a compatible \(Y\). Matrix ranks mean Smith multiplicities over \(R\), not just rank over the residue field. The case \(n=0\) is interpreted as one empty pair; the asymptotic claims concern \(n\to\infty\) with \(q\) fixed.

## Proof
**Step 1 (classification and exact count).** Every matrix over a finite principal ideal ring of length two has Smith form \(\operatorname{diag}(I_a,\pi I_b,0_c)\). Reduction modulo \(\pi\) has rank \(a\). There are \(G_q(n,a)\) residue matrices of rank \(a\). Fix one and lift invertible row/column transformations to \(R\), putting a chosen lift of the matrix into block form with an invertible \(a\)-square corner. Elementary block elimination leaves a lower-right \((n-a)\)-square block divisible by \(\pi\); its quotient modulo \((\pi)\) is an arbitrary matrix over \(\mathbb F_q\). Its rank is exactly \(b\), while the remaining \(n^2-(n-a)^2=2na-a^2\) lift parameters are free over \(\mathbb F_q\). The number of matrices with Smith type \((a,b,c)\) is therefore
\[
G_q(n,a)q^{2na-a^2}G_q(n-a,b).
\tag{5}
\]
This argument uses only that \((\pi)\) is one-dimensional over the residue field and square-zero, so it covers nonsplit chain rings.

For a fixed \(X\) of this Smith type, \(XY=0\) forces each column of \(Y\) into \(\ker X\), which has \(q^{b+2c}\) elements: a unit diagonal coordinate forces zero, a \(\pi\) coordinate permits the \(q\) annihilator elements, and a zero coordinate permits all \(q^2\) ring elements. The \(n\) columns can be chosen independently, giving \(q^{n(b+2c)}\) choices of \(Y\). Multiplication with (5) establishes (1).

**Step 2 (exact quadratic weight).** Write \(\Phi_j=\Phi_j(q)\). The standard finite-field rank formula gives
\[
G_q(m,k)=q^{k(2m-k)}\frac{\Phi_m^2}{\Phi_k\Phi_{m-k}^2}.
\]
Substitution into (1), with \(h=a-c=2a+b-n\), simplifies *exactly* to
\[
Q_{n,q}(a,b,c)=q^{5n^2/2-(h^2+b^2)/2}
\frac{\Phi_n^2}{\Phi_a\Phi_b\Phi_c^2}.
\tag{6}
\]
The integer-feasibility conditions are \(b\geq0\), \(h\in\mathbb Z\), \(h+b\equiv n\pmod2\), and \(a=(n+h-b)/2\), \(c=(n-h-b)/2\) both nonnegative.

**Step 3 (total-variation convergence).** Let \(t=q^{-1}\). For every fixed feasible pair \((h,b)\), both \(a,c\to\infty\) as \(n\to\infty\) through one parity, and the finite-product factor in (6) converges to \(1/(\Phi_\infty\Phi_b)\). Since \(0<\Phi_\infty\leq\Phi_j\leq1\), the same factor is bounded above uniformly by \(\Phi_\infty^{-4}\). The series \(\sum_{h\in\mathbb Z}\sum_{b\geq0}t^{(h^2+b^2)/2}\) converges. Dominated convergence on this countable state space therefore yields, for \(\sigma=n\bmod2\),
\[
\frac{Z_{n,q}}{q^{5n^2/2}}\longrightarrow
\frac{1}{\Phi_\infty}
\sum_{\substack{h\in\mathbb Z,\ b\geq0\\h+b\equiv\sigma\ (2)}}
\frac{t^{(h^2+b^2)/2}}{\Phi_b},
\tag{7}
\]
and convergence in \(\ell^1\) of the unnormalized weights. Normalizing proves total-variation convergence to (4) once the sum in (7) is evaluated.

**Step 4 (Euler-product evaluation).** The finite \(q\)-binomial theorem, followed by a limit of finite products, yields Euler's identity
\[
\sum_{b\geq0}\frac{(\pm1)^b t^{b^2/2}}{\Phi_b}
=\prod_{j\geq1}(1\pm t^{j-1/2})=P_\pm.
\tag{8}
\]
The classical Jacobi triple-product identity at signs \(\pm1\) yields
\[
\sum_{h\in\mathbb Z}(\pm1)^h t^{h^2/2}=
\Phi_\infty P_\pm^2.
\tag{9}
\]
Apply the parity projector \((1+(-1)^{h+b+\sigma})/2\) to the double series in (7). Using (8)–(9), the sum equals \(\Phi_\infty(P_+^3+(-1)^\sigma P_-^3)/2\). The prefactor \(1/\Phi_\infty\) in (7) cancels, yielding (2)–(3). As every factor of \(P_-\) lies strictly between zero and one and its infinite product is positive, the parity constants are unequal. This completes the proof.

## Verification
The standalone program `artifacts/verify.py` uses only the Python standard library. Run `python3 artifacts/verify.py` from the extracted result directory. It directly enumerates matrix kernels and Smith-type strata over both \(\mathbb Z/4\mathbb Z\) and dual numbers over \(\mathbb F_2\), and over both \(\mathbb Z/9\mathbb Z\) and dual numbers over \(\mathbb F_3\), including complete \(2\times2\) matrix enumerations. The zero-product pair totals are \(2464\) for \(q=2,n=2\) and \(123201\) for \(q=3,n=2\), for both ring types. Independent direct pair multiplication is also checked for the two \(q=2,n=2\) rings. Larger sampling and arithmetic normalization checks cover additional cases and the limiting products. The output ends in `VERIFY_OK`.

## Relationship to prior work
Dolžan studies zero-product probability for finite rings and gives exact semisimple results and general bounds. The present ring is nonsemisimple, and the main issue is the parity-dependent large-matrix asymptotic and its conditional two-parameter Smith law. Catanzaro–Zabka study random chain complexes over finite fields, with a sampling construction different from the uniform distribution over all ordered zero-product pairs. Byrne–Horlemann–Khathuria–Weger provide the standard background count of individual matrix module types over finite chain rings; the one-matrix enumeration (5) is not claimed as independently new. Their results do not state (2)–(4) for zero-product pairs. Shumyatsky–Vannacci give structural ideal bounds from zero-product probability, not this exact distribution. Earlier matrix square-zero and finite-chain-ring intersection laws concern different equations or invariants and do not imply the parity-split Euler-product constants without additional analysis.

## Limitations
The asymptotic is for fixed \(q\) with \(n\to\infty\), not simultaneous growing \(q\), and the ring must have length two; no claim is made for arbitrary local rings or longer chains. Formula (1) tracks the Smith invariants of the first matrix, not the complete joint Smith type of both matrices or the homology module of the two-term complex. Publication priority is assessed against inspected literature, not exhaustively established. The full text of Dolžan's directly relevant 2022 paper was not accessible in this review; its abstract and stated scope were checked, and an exact earlier derivation under different terminology remains a residual originality risk. Finite program checks corroborate, but are not the proof of, the unbounded-dimensional claims.

## References
1. D. Dolžan, “The Probability of Zero Multiplication in Finite Rings,” *Bulletin of the Australian Mathematical Society* 106 (2022), 83–88, published online January 24, 2022. DOI: 10.1017/S0004972721001246.
2. M. J. Catanzaro and M. J. Zabka, “A Model for Random Chain Complexes,” arXiv:1901.00964v1, January 4, 2019; in particular its definitions and Theorems A–B for finite fields.
3. E. Byrne, A.-L. Horlemann, K. Khathuria and V. Weger, “Density of Free Modules over Finite Chain Rings,” arXiv:2106.09403, first posted June 17, 2021; especially Proposition 15 on matrix type counts.
4. P. Shumyatsky and M. Vannacci, “Commuting and Product-Zero Probability in Finite Rings,” arXiv:2307.12633v1, July 24, 2023, especially Theorem 1.3.
5. Classical finite \(q\)-binomial theorem and Jacobi triple-product identity; both are applied in (8)–(9) with \(0<t<1\).
