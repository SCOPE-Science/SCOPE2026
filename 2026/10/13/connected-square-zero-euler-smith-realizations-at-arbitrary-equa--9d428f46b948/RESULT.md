# Connected square-zero Euler–Smith realizations at arbitrary equal depth
## Finding
For every field \(\Bbbk\) and every pair of integers \(k,m\ge1\), there is a finite-dimensional connected positively graded elementary algebra with square-zero radical and signed Euler–Smith profile
\[
(\underbrace{-m,\ldots,-m}_{k\text{ times}},0).
\]
Thus arbitrary negative depth and arbitrary multiplicity can occur simultaneously in a connected square-zero realization.

An explicit construction uses \(r=k+1\) vertices. Put
\[
f_m(x)=(1-x^2)^m
\]
and decompose its nonconstant part coefficientwise as
\[
f_m(x)-1=p_+(x)-p_-(x),
\]
where \(p_+(x),p_-(x)\in\mathbb Z_{\ge0}[x]\) have disjoint supports. Let \(J_r\) denote the \(r\times r\) all-ones matrix and set
\[
N_{k,m}(x)=p_+(x)I_r+p_-(x)(J_r-I_r).
\]
Take the elementary square-zero algebra \(A_{k,m}=E\oplus V\), with \(E\cong\Bbbk^r\), \(V^2=0\), and graded \(E\)-bimodule multiplicities encoded by \(N_{k,m}(x)\).

## Assumptions and scope
The construction works over an arbitrary base field; no characteristic restriction is imposed. The Euler–Smith calculation is performed, as in the defining framework, over \(\mathbb Q\llbracket x-1\rrbracket\), because graded dimensions are integers. The algebra is finite dimensional because \(N_{k,m}(x)\) is polynomial, positively graded because \(N_{k,m}(0)=0\), and elementary with degree-zero part \(E\cong\Bbbk^r\).

The result concerns the special but structurally natural class of radical-square-zero algebras. It does not classify all connected realizations of signed profiles, nor does it assert uniqueness or minimality of the construction.

## Proof
The binomial expansion gives
\[
f_m(x)-1=\sum_{j=1}^{m}(-1)^j\binom mj x^{2j}.
\]
Hence one may take
\[
p_-(x)=\sum_{\substack{1\le j\le m\\ j\text{ odd}}}\binom mj x^{2j},
\qquad
p_+(x)=\sum_{\substack{1\le j\le m\\ j\text{ even}}}\binom mj x^{2j}.
\]
Both have nonnegative integer coefficients and zero constant term. In particular, the coefficient of \(x^2\) in \(p_-(x)\) is \(m>0\). Every ordered pair of distinct vertices therefore has positive degree-two radical multiplicity, so the underlying vertex graph is complete and the square-zero algebra is connected.

For a square-zero algebra of this form, the matrix Hilbert series is
\[
C_A(x)=I_r+N_{k,m}(x),
\]
and the rational Euler matrix is \(\mathcal E_A(x)=C_A(x)^{-1}\). By construction,
\[
\begin{aligned}
I_r+N_{k,m}(x)
&=(1+p_+(x)-p_-(x))I_r+p_-(x)J_r\\
&=f_m(x)I_r+p_-(x)J_r.
\end{aligned}
\]
Over \(\mathbb Q\), the space \(\mathbb Q^r\) is the direct sum of the all-ones line and the sum-zero hyperplane. Relative to any constant basis adapted to that decomposition, multiplication by \(J_r\) has eigenvalue \(r\) on the first summand and eigenvalue \(0\) on the second. Therefore \(I_r+N_{k,m}(x)\) is equivalent over \(\mathbb Q[x]\), and hence over \(\mathbb Q\llbracket t\rrbracket\) after \(x=1+t\), to
\[
\operatorname{diag}\bigl(f_m(1+t)+r p_-(1+t),f_m(1+t),\ldots,f_m(1+t)\bigr).
\]
Now
\[
f_m(1+t)=\bigl(1-(1+t)^2\bigr)^m=(-t(2+t))^m,
\]
so its \(t\)-adic valuation is exactly \(m\). Also
\[
p_-(1)=\sum_{j\text{ odd}}\binom mj=2^{m-1},
\]
which implies
\[
\bigl(f_m(1+t)+r p_-(1+t)\bigr)\big|_{t=0}=r2^{m-1}\ne0
\]
in \(\mathbb Q\). Thus that diagonal entry is a unit in \(\mathbb Q\llbracket t\rrbracket\), while the other \(k=r-1\) entries have valuation \(m\). The local Smith exponents of the Cartan matrix are therefore
\[
(0,\underbrace{m,\ldots,m}_{k\text{ times}}).
\]
Inverting the matrix reverses signs and order, giving the signed Euler–Smith profile
\[
(\underbrace{-m,\ldots,-m}_{k\text{ times}},0).
\]
This completes the construction.

## Verification
Every step is symbolic. The only local invariant needed is the \(t\)-adic valuation of two explicit scalar factors after a constant decomposition of \(\mathbb Q^r\). The first factor is a unit because its constant term is the positive integer \(r2^{m-1}\); the remaining factor is \((-t(2+t))^m\), which has exact valuation \(m\). No finite experiment is used as an infinite proof.

The standing hypotheses of the signed Euler–Smith framework are satisfied: the algebra is finite dimensional and hence noetherian, its vertex simples are of graded type \(\mathrm{FP}_\infty\), and its matrix Hilbert series is polynomial. The calculation uses the local DVR \(\mathbb Q\llbracket t\rrbracket\), exactly the coefficient ring prescribed for graded-dimension Smith data.

## Relationship to prior work
Kaygun's 2026 paper introduces signed Euler–Smith profiles and explicitly identifies connected realization modulo common shifts as the nontrivial realization problem. Its square-zero constructions separately realize arbitrary depth in the two-vertex profile \((-m,0)\), arbitrary multiplicity at depth one in profiles \((-1,\ldots,-1,0)\), and a displayed depth-two three-vertex example \((-2,-2,0)\). The formula above unifies these directions: every grid point with arbitrary equal negative depth \(m\) and arbitrary multiplicity \(k\) is realized by one connected square-zero family.

The earlier local-Smith paper treats the nonnegative twisted Calabi–Yau setting and supplies the local Smith framework, but it does not cover this negative connected square-zero realization problem.

Targeted statement-level searches for the exact profile family, its local Smith exponent form, and the complete-graph square-zero construction found no published finding that implies this two-parameter realization. The closest indexed records concern unrelated Smith-type or matrix-invariant problems.

## Limitations
The theorem realizes only profiles whose negative entries are all equal and with one terminal zero. It does not solve the general connected-realization problem for arbitrary mixed signed tuples. It also does not determine whether the number of vertices, radical dimension, or highest grading degree is minimal for the prescribed profile.

Because the motivating preprint is very recent, there remains a residual bibliographic risk that an unindexed contemporaneous note contains an equivalent complete-graph construction. No such statement was found in the inspected primary text or targeted literature/database searches.

## References
1. A. Kaygun, *Signed Euler–Smith Profiles of Graded Algebras*, arXiv:2609.35248v1, first public 2026-09-28.
2. A. Kaygun, *Local Smith Profiles of Twisted Calabi–Yau Algebras*, arXiv:2608.14057v1, first public 2026-08-14.
