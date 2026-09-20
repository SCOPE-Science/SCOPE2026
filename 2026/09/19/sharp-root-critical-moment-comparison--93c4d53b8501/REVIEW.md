# Same-model review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

**PASS.**

The proof was checked directly at the matrix level.

Let \(D=\operatorname{diag}(\lambda_i)\), \(Q=J_n/n\), \(P=I-Q\), and
\(A=PDP\). The Komarova--Rivin differentiator identity gives
\(\operatorname{spec}(A)=\{0,\xi_1,\dots,\xi_{n-1}\}\), hence traces of powers of
\(A\) are the critical-point power sums. The algebraic decomposition
\[
D-A=QD+PDQ
\]
is exact. Moreover \(AQ=QA=0\), and \(D,A,P,Q\) all have operator norm at most
one when the zeros lie in the unit disk.

Expanding \(D^m-A^m\) telescopically produces two families of rank-one trace
terms. All \(PDQ\,A^k\) terms with \(k\ge1\) vanish after cyclically moving
\(Q A^k\) to the front. The first \(QD\) term is exactly the normalized zero
moment, and its final term vanishes for \(m\ge2\) because \(A^{m-1}Q=0\).
Exactly \(m-1\) remaining rank-one terms need to be bounded, each by one via
\(|\operatorname{tr}B|\le\operatorname{rank}(B)\|B\|\). This proves
\[
\left|T_m-\frac1n\operatorname{tr}D^m\right|\le m-1.
\]
The normalization identity
\[
T_m-\frac1n\operatorname{tr}D^m
=(n-1)\left(
\frac1n\operatorname{tr}D^m-\frac1{n-1}\operatorname{tr}A^m
\right)
\]
then gives the theorem. The case \(m=1\) was checked separately and is exact.

Translation and scaling preserve the critical-point relation and introduce the
factor \(R^m\). Repeated roots cause no difficulty because all spectra and power
sums are counted with algebraic multiplicity.

The stated equality family was checked explicitly. For
\(f(z)=((z-c)^m-R^m)^{n/m}\), \(m\mid n\), the root moment equals \(R^m\);
the derivative has each of the \(m\) boundary roots with multiplicity
\(n/m-1\), and \(c\) with multiplicity \(m-1\). Its normalized critical moment
is \((n-m)R^m/(n-1)\), producing equality.

The analytic-test corollary follows from absolute summation of the monomial
bounds. The constant and linear coefficients cancel, and the larger-disk form
uses the standard Cauchy estimate and the exact geometric-series identity
\(\sum_{m\ge2}(m-1)q^m=q^2/(1-q)^2\).

No computer-assisted argument is needed for the proof.

## Originality

**PASS, to the best of our knowledge.**

The closest source located is Teng Zhang, arXiv:2609.20256v1. Its Lemma 2.5
proves
\[
|\mathbb E\lambda^m-\mathbb E\xi^m|\le 5m/n
\]
for every integer \(m\ge1\). The paper explicitly presents this as an explicit
improvement of Tao's earlier \(O(m\log m/n)\) comparison. Its proof uses the
Komarova--Rivin differentiator matrix, bounds \(D-PDP\) globally as a rank-two
perturbation of norm at most two, and then handles the normalization separately.
It does not state the \((m-1)/(n-1)\) coefficient, the equality family, or the
analytic-test consequence recorded here.

The Komarova--Rivin paper supplies the differentiator identity but was not found
to state this normalized moment inequality. Schmeisser's majorization theorem
controls ordered moduli of zeros and critical points and its convex transforms;
that is not a bound for complex normalized power-sum differences. Random
polynomial results on convergence or pairing of zero and critical-point
empirical measures impose probabilistic hypotheses and do not provide this
deterministic coefficientwise estimate.

Searches included exact and synonymous formulations involving power sums,
normalized moments, empirical zero/critical-point measures, derivative zeros,
rank-one compressions, differentiator matrices, analytic test functions, and
trace powers. No earlier statement equivalent to the theorem was located.
The current SCOPE archive was also checked by source identifier, mathematical
object, claim family, and synonymous terminology, with no accepted overlap
found.

Residual risk remains from older operator-theoretic, matrix-compression, or
geometric-function-theoretic coefficient inequalities under substantially
different terminology. The proof ingredients are elementary once the
differentiator representation is known, so an unindexed prior observation is
plausible. No inaccessible source was identified whose available title,
abstract, or theorem description gave concrete evidence of coverage.

## Value

**PASS.**

The result replaces a recent explicit \(5m/n\) moment estimate used in an
effective Sendov argument by a substantially sharper normalized coefficient
\((m-1)/(n-1)\), identifies an infinite equality family, and converts the
coefficientwise estimate into an \(O(n^{-1})\) deterministic discrepancy theorem
for analytic observables. The cancellation responsible for the improvement is
structural: it comes from separating the two rank-one pieces of the
differentiator perturbation and retaining the normalization identity rather than
from numerical optimization.

The theorem does not claim an exact extremal value for every fixed pair
\((n,m)\), nor an optimal analytic-test constant, and these limits are stated
explicitly.
