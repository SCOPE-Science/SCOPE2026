# A strict cardinality-by-cardinality subset-sum bias in reduced residue systems

## Finding

For an integer \(N\ge 2\), let \(U_N=(\mathbb Z/N\mathbb Z)^\times\), and let \(q=\varphi(N)\). For every integer \(0\le r\le q\), let \(F_{N,r}(b)\) count the \(r\)-element subsets \(A\subseteq U_N\) whose sum is congruent to \(b\pmod N\). No one of these fixed-cardinality distributions is uniform modulo \(N\).

The stronger exact statement applies to every prime \(p\mid N\). Put \(m=\varphi(N)/(p-1)\), and let \(C_{N,r,p}(b)\) count those \(r\)-subsets whose sums reduce to \(b\pmod p\), for \(b\in\mathbb F_p\). Define the strictly positive integer

\[
B_{p,m}(r)=[z^r](1+z+\cdots+z^{p-1})^m.
\]

Then for all \(0\le r\le\varphi(N)\),

\[
C_{N,r,p}(b)=\begin{cases}
\displaystyle\frac{\binom{\varphi(N)}r+(p-1)(-1)^rB_{p,m}(r)}p,&b=0,\\[5pt]
\displaystyle\frac{\binom{\varphi(N)}r-(-1)^rB_{p,m}(r)}p,&b\ne0.
\end{cases}
\]

In particular, for every nonzero \(b\),

\[
C_{N,r,p}(0)-C_{N,r,p}(b)=(-1)^rB_{p,m}(r)\ne0.
\]

Thus zero is strictly more common than each nonzero residue modulo \(p\) for even \(r\), and strictly less common for odd \(r\). The alternating biases cancel after summing over all nonempty cardinalities when \(p\) is odd.

## Assumptions and scope

All subsets contain distinct residue classes modulo \(N\) (no repeated selections). The sum is taken additively modulo \(N\), and then, when indicated, reduced modulo \(p\). The prime \(p\) is any prime divisor of \(N\), and the theorem covers the endpoints \(r=0\) and \(r=\varphi(N)\), the prime \(p=2\), and all composite moduli. Uniformity means that every residue class has the same subset count. No asymptotic or squarefreeness assumption is used.

## Proof

**Uniform reduction fibers.** Reduction modulo \(p\) is a surjective multiplicative homomorphism \(U_N\to\mathbb F_p^\times\). Indeed, for each \(v\in\mathbb F_p^\times\), the Chinese remainder theorem supplies an integer congruent to \(v\pmod p\) and to \(1\) modulo every other prime divisor of \(N\); it is coprime to \(N\). Each fiber therefore has cardinality \(m=q/(p-1)\).

**Nontrivial Fourier coefficient.** Let \(\zeta\) be a primitive \(p\)-th root of unity. For any \(t\in\{1,\ldots,p-1\}\), the size-and-sum enumerator at the additive character \(b\mapsto\zeta^{tb}\) is

\[
\begin{aligned}
\sum_{A\subseteq U_N}z^{|A|}\zeta^{t\sum_{a\in A}a}
&=\prod_{a\in U_N}(1+z\zeta^{t a})\\
&=\left(\prod_{v=1}^{p-1}(1+z\zeta^{tv})\right)^m\\
&=\left(\frac{1-(-z)^p}{1+z}\right)^m\\
&=(1-z+z^2-\cdots+(-z)^{p-1})^m.
\end{aligned}
\]

The polynomial identity follows because \(\{\zeta^{tv}:1\le v<p\}\) consists of all the nonidentity \(p\)-th roots of unity; it holds also at \(p=2\). Extracting the coefficient of \(z^r\), every nontrivial additive Fourier coefficient of the size-\(r\) subset-sum distribution equals \((-1)^r B_{p,m}(r)\). Its trivial coefficient is \(\binom qr\).

**Fourier inversion.** Orthogonality of characters gives

\[
C_{N,r,p}(b)=\frac1p\left(\binom qr+(-1)^rB_{p,m}(r)\sum_{t=1}^{p-1}\zeta^{-tb}\right).
\]

The last character sum equals \(p-1\) for \(b=0\) and \(-1\) otherwise, giving the claimed exact formulas. They yield integers because their left sides are subset counts.

**Strict positivity and nonuniformity.** Every coefficient of \((1+z+\cdots+z^{p-1})^m\) from degree \(0\) through \((p-1)m=q\) is positive: any such degree can be written as a sum of \(m\) integers between \(0\) and \(p-1\), by filling the coordinates in sequence. Hence the two types of prime-residue counts are unequal for every \(r\). If the counts \(F_{N,r}(b)\) were uniform over \(\mathbb Z/N\mathbb Z\), the aggregate over the \(N/p\) residue classes reducing to any fixed \(b\pmod p\) would also be uniform; this contradicts the exact difference. This proves the theorem for all \(N,r\).

**Cancellation across cardinalities.** For odd \(p\), the nontrivial Fourier contribution of all nonempty subsets is

\[
\sum_{r=1}^{q}(-1)^r B_{p,m}(r)=(1-1+1-\cdots+1)^m-1=0.
\]

Thus the nonuniformities of individual layers can cancel in their union. This is consistent with the known unrestricted, nonempty subset-sum equidistribution for odd \(N\); it does not infer that stronger modulus-\(N\) assertion from this prime-level calculation.

## Verification

The standalone \`verify.py\` enumerates the cardinality-by-residue distributions using a dynamic-programming recurrence independently of the Fourier proof. For every \(2\le N\le96\), every prime \(p\mid N\), every \(0\le r\le\varphi(N)\), and every \(b\pmod p\), it confirms the exact count and strict signed difference. It also independently checks nonempty all-cardinality equidistribution modulo \(N\) for odd \(N\) in that finite range. The program prints \`VERIFY_OK\` on completion.

For example, \(N=21\) has \(q=12\). At \(r=6\), the number of subsets is \(\binom{12}{6}=924\), divisible by \(21\); nevertheless the subset sums modulo \(3\) occur \(402\) times at zero and \(261\) times at each nonzero residue. Therefore even the usual necessary divisibility condition for uniformity is insufficient in this natural family.

## Relationship to prior work

Wagon and Wilf (1994) classified equidistribution of fixed-size subset sums when the underlying set is the initial interval \(\{1,\ldots,n\}\), by a Gaussian-binomial criterion, and described Fourier/generating-function methods. Their full paper does not state the fixed-size distribution for the unit system \(U_N\), nor the universal signed bias for every \(p\mid N\). In particular, for prime \(N\) their interval theorem already implies the nonuniformity part, but it does not directly apply to the reduced-residue set at composite \(N\).

Gaitanas (2023), Theorem 1.1, establishes uniformity of **nonempty subset sums with cardinalities pooled** for odd moduli. That theorem does not assert uniformity for each fixed cardinality, and its main classification concerns sets with pooled-subset equidistribution. The exact alternating prime-residue bias here explains how pooled uniformity can coexist with nonuniformity at every individual cardinality.

A Fourier expression for subset-sum counts is standard, so the novelty claimed here is limited to the simultaneous exact, strictly nonzero two-level prime-projection law and its all-moduli/all-cardinalities consequence for the full reduced residue system. The possibility of an implicit or unlocated specialization in existing general character-enumerator literature remains.

## Limitations

The theorem does not provide a full formula for each residue count modulo composite \(N\); it provides an exact formula after reduction modulo each prime divisor, which suffices to exclude uniformity modulo \(N\). It does not classify proper subsets of the unit system. The proof is self-contained but independent mathematical and bibliographic audits have not been performed.

## References

1. S. Wagon and H. S. Wilf, *When are subset sums equidistributed modulo m?*, Electronic Journal of Combinatorics 1 (1994), #R3; published 1994-04-13. DOI: https://doi.org/10.37236/1183 .
2. K. Gaitanas, *On subset sums of the units modulo n which are equally distributed modulo n* (2023), arXiv:2304.14141, https://arxiv.org/abs/2304.14141 . A published correction to an unrelated structural theorem appears as DOI: https://doi.org/10.1007/s00013-023-01864-z .
