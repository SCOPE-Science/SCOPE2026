# Same-model review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

PASS.

The proof was re-derived directly from the reciprocal coefficient expansion. For
\[
q_\sigma(z)=1+\sum_{n\ge1}\frac{b_n}{(n+1)^\sigma}z^n
\]
and \(F_\sigma=z/q_\sigma\), the identity
\[
U_{F_\sigma}=q_\sigma-zq_\sigma'-1
=-\sum_{n\ge2}\frac{(n-1)b_n}{(n+1)^\sigma}z^n
\]
was checked algebraically.

The two coefficient inputs are standard and exactly match the hypotheses:
\[
|b_1|\le2,\qquad
\sum_{n\ge2}(n-1)|b_n|^2\le1.
\]
Applying Cauchy--Schwarz to the unweighted reciprocal tail gives the
zero-free criterion
\[
|q_\sigma(z)-1|
<
2^{1-\sigma}
+
\sqrt{\sum_{m\ge1}\frac1{m(m+2)^{2\sigma}}}.
\]
At the defining root the inequality is still strict for every \(|z|<1\),
so no endpoint gap is present.

For the \(\mathcal U\) functional, a separate Cauchy--Schwarz estimate gives
\[
|U_{F_\sigma}(z)|^2
\le
\sum_{n\ge2}\frac{(n-1)|z|^{2n}}{(n+1)^{2\sigma}}.
\]
Because the root is larger than \(7/5\), this is bounded by
\(\sum_{n\ge2}n^{-9/5}<0.945\). Thus the proof does not confuse the
zero-free estimate with the \(\mathcal U\)-estimate.

The lower obstruction was checked independently. For
\(f_\alpha=z/(1-z)^\alpha\), \(0<\alpha<1\),
\[
\operatorname{Re}(zf_\alpha'/f_\alpha)>1-\alpha/2>0,
\]
so \(f_\alpha\in\mathcal S\). Its reciprocal coefficients are negative and
have the exact gamma form used in the record, with asymptotic
\(|b_n|\asymp n^{-\alpha-1}\). Hence the positive boundary series for
\(U_{F_\sigma}\) diverges whenever \(\alpha+\sigma<1\). This proves failure
of universal \(\mathcal U\)-membership for every \(\sigma<1\), regardless
of whether the smoothed reciprocal first develops a zero.

The numerical root bracket is not used as a black-box proof of the theorem.
The root is defined intrinsically, monotonicity is analytic, and the
verification artifact uses a finite sum plus the explicit tail bound
\[
\sum_{m>N}\frac1{m(m+2)^{2\sigma}}
<
\frac{N^{-2\sigma}}{2\sigma}.
\]

## Originality

PASS, to the best of our knowledge.

Ali--Obradović--Ponnusamy (2013) was inspected at the definition of
\(F_\sigma\), Theorem 1.6, Corollary 1.7, and the concluding open problem.
The paper proves the explicit universal bound \(\sigma\ge3/2\) and asks for
the smallest parameter yielding membership in \(\mathcal U\) or
\(\mathcal S\).

Searches covered the exact title and DOI, the concluding problem wording,
`F_sigma`, `Li_sigma`, reciprocal Hadamard convolution, polylogarithm
univalence operators, and later class-\(\mathcal U\) literature. No located
source gave the bound \(1.413520\), the series-root criterion, or the
starlike power-family obstruction below \(1\).

The 1996 Ponnusamy--Sabapathy paper is a material residual risk because it
develops polylogarithms in geometric function theory, but the full
theorem-by-theorem text was not available in the inspected sources. Its
available abstract concerns geometric mapping properties of generalized
polylogarithms. Since the 2013 paper, with Ponnusamy as coauthor, later poses
this specific reciprocal-smoothing threshold as open, direct prior coverage
there appears unlikely but cannot be excluded without full inspection.

The 2007 Obradović--Ponnusamy convolution-transform paper was checked at the
available abstract. Its hypotheses start with functions already in a
restricted class \(\mathcal U(\lambda)\) and a hypergeometric convolution,
rather than arbitrary \(f\in\mathcal S\), so it does not visibly imply the
universal theorem here. The 2019 polylogarithm-operator paper concerns a
different operator/subclass and does not state the 2013 threshold problem.

## Value

PASS.

The result advances a concrete open quantitative boundary from an explicit
published upper bound \(3/2\) to less than \(1.413520\), and at the same time
supplies the first simple universal obstruction \(1\) from below for the
stronger \(\mathcal U\) target. The upper and lower arguments use different
mechanisms: area-theorem control plus zero-free smoothing on one side, and
slow reciprocal coefficient decay in a starlike family on the other. The
remaining interval is therefore a substantially narrower and structurally
better-defined target.

## Limitations

- The exact \(\mathcal U\)-threshold remains unresolved in
  \([1,1.413520)\).
- The lower example only excludes \(\mathcal U\), not univalence itself.
- The upper proof uses uncoupled reciprocal coefficient information and may
  be improvable.
- Full theorem-level inspection of Ponnusamy--Sabapathy (1996) was not
  available; equivalent prior coverage remains a residual originality risk.
- Independent audit has not been performed.
