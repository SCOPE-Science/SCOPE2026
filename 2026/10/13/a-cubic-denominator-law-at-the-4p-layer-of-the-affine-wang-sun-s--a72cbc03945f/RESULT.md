# A cubic denominator law at the \(4p\) layer of the affine Wang–Sun sum
## Finding
Let \(S_n\) denote the affine Wang–Sun sum introduced by Agustín-Aquino. For every prime \(p\ge 7\),
\[
\operatorname{den}(S_{4p})=
\begin{cases}
p^2,&p=7,\\
p^3,&p\ge 11,
\end{cases}
\]
where \(\operatorname{den}\) means the positive denominator after reduction. Thus the next dyadic layer after the published \(2p\) denominator theorem has a generic cubic prime denominator, with the single exceptional drop \(p=7\).

The exception is explicit:
\[
C_{28}=-\frac{34695770811027473098809241186}{49},
\]
where \(C_n\) is the alternating cotangent block in the source. Its numerator is congruent to \(2\pmod 7\), so the denominator is exactly \(7^2\). Since \(S_{28}-C_{28}\) is an integer, the same denominator holds for \(S_{28}\).

## Assumptions and scope
For even \(n\), Agustín-Aquino defines
\[
S_n=\sum_{\pi}\operatorname{sign}(\pi)\prod_j\frac{1+\zeta^{j-\pi(j)}}{1-\zeta^{j-\pi(j)}},
\]
with the sum over affine derangements of \(\mathbb Z/n\mathbb Z\). The paper reduces \(S_n\) to divisor-indexed contributions and defines
\[
C_\sigma=\sum_{r=1}^{\sigma-1}(-1)^r\left(i\cot\frac{\pi r}{\sigma}\right)^\sigma.
\]
The present statement concerns only indices \(n=4p\) with \(p\) prime and \(p\ge7\). It does not assert a denominator formula for arbitrary composite \(n\), nor for higher dyadic multiples \(8p,16p,\ldots\).

Agustín-Aquino proves that for primes \(p>3\), \(S_{2p}\) has reduced denominator \(p\). The result here identifies the complete reduced-denominator law at the next dyadic layer \(4p\).

## Proof
For \(n=4p\), the even divisors are \(2,4,2p,4p\). In the source's divisor formula, the cotangent block occurs only when \(n/\sigma\) is odd. Thus the \(\sigma=4\) term is an integer multiple of \(C_4=-2\), the \(\sigma=4p\) term occurs with coefficient one, and the other two contributions are integral. Hence
\[
S_{4p}-C_{4p}\in\mathbb Z,
\]
so it suffices to determine the reduced denominator of \(C_{4p}\).

For even \(q\), put
\[
P_k(q)=\sum_{r=1}^{q-1}\cot^k\frac{\pi r}{q}.
\]
Section 6 of the source gives
\[
C_{2m}=(-1)^m\bigl(2P_{2m}(m)-P_{2m}(2m)\bigr).
\]
With \(m=2p\), this becomes
\[
C_{4p}=2P_{4p}(2p)-P_{4p}(4p). \tag{1}
\]

Let \(x_r=\cot(\pi r/q)\), and write
\[
E_q(t)=\prod_{r=1}^{q-1}(1+x_rt)=\sum_{j=0}^{q-1}e_j(q)t^j.
\]
The source gives
\[
e_j(q)=0\quad(j\text{ odd}),
\]
and, for even \(j\),
\[
e_j(q)=(-1)^{j/2}\frac1q\binom q{j+1}. \tag{2}
\]
For \(q=2p\) or \(4p\), formula (2) has no denominator prime other than \(p\): the power of two in \(q\) divides \(\binom q{j+1}\) because \(j+1\) is odd. Rewriting (2) as
\[
e_j(q)=(-1)^{j/2}\frac{\binom{q-1}{j}}{j+1}
\]
shows that a factor \(p\) in the denominator can occur only when \(p\mid j+1\).

Set \(d=p-1\). For \(q=2p\), the only possibly non-\(p\)-integral elementary symmetric coefficient is \(e_d\). For \(q=4p\), the only such even-index coefficients are \(e_d\) and \(e_{3p-1}\). Therefore, over the localization \(\mathbb Z_{(p)}\),
\[
E_{2p}(t)=B_{2p}(t)+\frac{u_{2p}}p t^d,
\]
\[
E_{4p}(t)=B_{4p}(t)+\frac{u_{4p}}p t^d+\frac{v_{4p}}p t^{3p-1},
\]
where each \(B_q(t)\) has \(p\)-integral coefficients and constant term one. Moreover
\[
u_{kp}=p e_{p-1}(kp)=(-1)^{(p-1)/2}\binom{kp-1}{p-1}\qquad(k=2,4),
\]
so
\[
u_{2p}\equiv u_{4p}\equiv(-1)^{(p-1)/2}\pmod p. \tag{3}
\]
In particular, \(u_{2p}^4\equiv u_{4p}^4\equiv1\pmod p\).

Use
\[
\log E_q(t)=\sum_{r\ge1}(-1)^{r-1}\frac{P_r(q)}r t^r. \tag{4}
\]
Assume first that \(p\ge11\). Since \(d=p-1\), a term contributing to degree \(4p\) can contain at most four factors from the nonintegral part of \(E_q\). In the expansion of the second logarithm after factoring out \(B_q\), every contribution with at most three such factors has \(p\)-adic valuation at least \(-3\) before the factor \(4p\) in (4), and hence contributes at valuation at least \(-2\) to \(P_{4p}(q)\). A term involving the coefficient at degree \(3p-1\) cannot occur with four nonintegral factors at total degree \(4p\). Thus the only contribution capable of producing valuation \(-3\) in \(P_{4p}(q)\) is the fourth power of \(u_q t^d/p\). Consequently
\[
p^3P_{4p}(q)\equiv u_q^4[t^4]B_q(t)^{-4}\pmod p. \tag{5}
\]

Because \(p\ge11\), the exceptional degree \(d\) exceeds four, so the coefficients of \(t^2\) and \(t^4\) in \(B_q\) are simply those of \(E_q\). Formula (2) gives, modulo \(p\),
\[
e_2(q)\equiv-\frac13,\qquad e_4(q)\equiv\frac15.
\]
Therefore
\[
[t^4]B_q(t)^{-4}
\equiv10e_2(q)^2-4e_4(q)
\equiv\frac{10}{9}-\frac45
=\frac{14}{45}\pmod p. \tag{6}
\]
Combining (3), (5), and (6) for \(q=2p\) and \(q=4p\), then using (1), yields
\[
p^3C_{4p}\equiv2\frac{14}{45}-\frac{14}{45}
=\frac{14}{45}\pmod p. \tag{7}
\]
For every prime \(p\ge11\), the residue in (7) is nonzero. All denominators in the Newton recurrence for the two power sums are powers of \(p\), so (7) proves that the reduced denominator of \(C_{4p}\), and therefore of \(S_{4p}\), is exactly \(p^3\).

The generic residue (7) vanishes at \(p=7\), so that prime must be evaluated one order deeper. Applying the same finite Newton recurrence from (2) exactly gives
\[
C_{28}=-\frac{34695770811027473098809241186}{49}.
\]
The numerator is \(2\pmod7\), proving that the denominator is exactly \(7^2\). This completes the classification for all primes \(p\ge7\).

## Verification
The accompanying `verify.py` implements (2), Newton's identities, and equation (1) with exact rational arithmetic. It verifies the displayed value of \(C_{28}\), confirms that its numerator is nonzero modulo \(7\), and checks the congruence
\[
p^3C_{4p}\equiv\frac{14}{45}\pmod p
\]
for a collection of primes \(p\ge11\). It also checks the source's listed denominator at \(n=20\) as a regression test. These finite computations are diagnostic; the uniform theorem for all \(p\ge11\) follows from the coefficient and valuation argument above.

## Relationship to prior work
Agustín-Aquino's 2026 paper is the same-object source. It gives the divisor reduction, the exact cotangent-power-sum machinery, a full formula for every even \(n\), and the theorem that \(S_{2p}\) has denominator \(p\) for primes \(p>3\). Its displayed table reaches \(n=24\). A search of the paper for a \(4p\) specialization found no uniform reduced-denominator theorem at this layer.

Liu and Xin give broad closed forms for root-of-unity weighted trigonometric power sums, including ordinary and alternating cotangent sums. Those formulas provide a general evaluation framework, but the located statement does not classify the reduced denominator of the affine Wang–Sun combination at \(4p\), nor the exceptional cancellation at \(p=7\).

Agustín-Aquino's 2023 paper treats the earlier affine Wang–Sun setting and the especially simple involutive subfamily. The 2026 paper is the direct source of the general divisor and cotangent reductions used here.

## Limitations
The proof is specific to the \(4p\) layer. It does not determine the denominator exponent at \(8p\) or higher dyadic layers, where more exceptional elementary-symmetric coefficients can interact. It also does not classify composite odd parts. The originality check cannot exclude unindexed or differently phrased literature, and broad trigonometric-sum formulas can in principle be specialized to individual cases even when they do not state this uniform denominator law.

## References
1. O. A. Agustín-Aquino, *The Wang–Sun Sum over Affine Derangements*, arXiv:2610.02806v1, 2 October 2026.
2. J. Liu and G. Xin, *Root-of-unity weighted trigonometric power sums: a constant term approach*, arXiv:2607.29130v1, 31 July 2026.
3. O. A. Agustín-Aquino, *Wang-Sun Formula in GL(Z/2kZ)*, INTEGERS 23 (2023), A37, DOI 10.5281/zenodo.7997988.
