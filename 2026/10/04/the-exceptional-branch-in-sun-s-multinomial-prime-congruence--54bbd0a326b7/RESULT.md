# The exceptional branch in Sun’s multinomial prime congruence

## Finding
For a prime \(p\), an integer \(l\ge 1\), and an integer \(m\ge 0\), set
\[
S_l^{(m)}(n)=\sum_{k_1+\cdots+k_l=n}\binom{n}{k_1,\ldots,k_l}^m
\]
and
\[
T_{l,m}(p)=\sum_{n=1}^{p-1}\frac{(-1)^{mn}}{n^{m-1}}S_l^{(m)}(n).
\]
Then
\[
T_{l,m}(p)\equiv
\begin{cases}
0\pmod p,&p\nmid l+1,\\
-1\pmod p,&p\mid l+1.
\end{cases}
\]
The first branch is Theorem 1.1 of Sun’s recent paper; the second branch completes the missing case and is independent of both \(m\) and the quotient \((l+1)/p\).

## Assumptions and scope
The sum defining \(S_l^{(m)}(n)\) is over \(l\)-tuples of nonnegative integers with total \(n\). When \(m=0\), the factor \(n^{m-1}\) is interpreted in the displayed quotient in the evident field sense, so \(1/n^{-1}=n\). All congruences are in \(\mathbb F_p\). The statement is only a modulo-\(p\) result; it does not assert a uniform lift modulo \(p^2\) or a corresponding exceptional formula for the \(q\)-analogue.

## Proof
Let
\[
F(x)=\sum_{k=0}^{p-1}\frac{x^k}{(k!)^m}.
\]
For \(0\le n<p\), coefficient extraction gives
\[
[x^n]F(x)^l=\frac{S_l^{(m)}(n)}{(n!)^m}.
\]
Exactly as in the coefficient calculation used in the source paper,
\[
B:=[x^{p-1}]F(x)^lF'(x)
=\frac1{((p-1)!)^m}\sum_{n=1}^{p-1}\binom{p-1}{n}^m\frac{S_l^{(m)}(n)}{(p-n)^{m-1}}.
\]
Wilson’s theorem and \(\binom{p-1}{n}\equiv(-1)^n\pmod p\) therefore give
\[
B\equiv -T_{l,m}(p)\pmod p.
\]

If \(p\nmid l+1\), then
\[
(F(x)^{l+1})'=(l+1)F(x)^lF'(x),
\]
so the coefficient of \(x^{p-1}\) on the right is \(p[x^p]F(x)^{l+1}\). Since \(l+1\) is invertible modulo \(p\), this gives \(B\equiv0\pmod p\), hence \(T_{l,m}(p)\equiv0\pmod p\).

Now suppose \(p\mid l+1\), and write \(l+1=ap\). Reduce \(F\) modulo \(p\). In the truncated power-series ring \(\mathbb F_p[[x]]/(x^p)\), the Frobenius identity gives
\[
F(x)^p=F(x^p)\equiv1\pmod{x^p}.
\]
Consequently
\[
F(x)^l=F(x)^{ap-1}\equiv F(x)^{-1}\pmod{x^p},
\]
and hence
\[
B=[x^{p-1}]\frac{F'(x)}{F(x)}.
\]

Over an algebraic closure of \(\mathbb F_p\), write
\[
F(x)=\prod_{i=1}^{p-1}(1-\alpha_i x),
\]
counting multiplicity. This is legitimate because the leading coefficient of \(F\) is nonzero modulo \(p\). Then
\[
\frac{F'(x)}{F(x)}=-\sum_{i=1}^{p-1}\frac{\alpha_i}{1-\alpha_i x},
\]
so
\[
[x^{p-1}]\frac{F'(x)}{F(x)}=-\sum_i\alpha_i^p.
\]
The coefficient of \(x\) in \(F\) is \(1\), hence \(-\sum_i\alpha_i=1\). In characteristic \(p\), Frobenius gives
\[
\sum_i\alpha_i^p=\left(\sum_i\alpha_i\right)^p=(-1)^p=-1,
\]
with the same identity in characteristic \(2\). Therefore \(B=1\) in \(\mathbb F_p\). Since \(B\equiv-T_{l,m}(p)\), the exceptional branch is
\[
T_{l,m}(p)\equiv-1\pmod p.
\]
This proves the dichotomy.

## Verification
The proof is symbolic and does not depend on finite computation. The accompanying verifier independently constructs the truncated polynomial \(F\) over \(\mathbb F_p\), recovers \(S_l^{(m)}(n)\) from coefficients, and checks the stated dichotomy for every prime \(p\le19\), every \(1\le l\le3p+2\), and every \(0\le m\le6\). It also checks the logarithmic-derivative coefficient in the exceptional branch. Finite checks are only sanity tests and are not used as an infinite proof.

## Relationship to prior work
Sun’s arXiv:2607.07638v3 introduces \(S_l^{(m)}(n)\), proves \(T_{l,m}(p)\equiv0\pmod p\) under the explicit condition \(p\nmid l+1\), and derives it from the same coefficient \([x^{p-1}]F^lF'\). The published proof stops precisely where division by \(l+1\) is required. The paper’s separate Domb-number theorem covers the special instance \(l=4\), \(m=2\), \(p=5\) through a stronger modulo-\(p^2\) statement, so that specialization is not claimed as new. The present result is the general exceptional branch for arbitrary \(l\) and \(m\).

Targeted indexed-literature searches for the source, the exceptional condition, the exact residue \(-1\), multinomial-power-sum aliases, and logarithmic-derivative formulations returned no equivalent or stronger published finding. Independent web searches likewise surfaced the source theorem and summaries that retain the condition \(p\nmid l+1\), not a general treatment of the omitted branch.

## Limitations
The novelty comparison is necessarily bounded by the literature and indexed databases actually checked; an unindexed or differently phrased prior derivation could exist. The result is only modulo \(p\). No claim is made about a uniform modulo-\(p^2\) refinement, about the source paper’s \(q\)-analogue in the exceptional regime, or about new information in the already-covered Domb specialization at \(p=5\).

## References
1. Z.-W. Sun, “A new kind of numbers and related congruences,” arXiv:2607.07638v3, first submitted 2026-07-08. Theorem 1.1 and its proof give the nonexceptional branch; Theorem 1.3 separately treats Domb sums modulo \(p^2\).
