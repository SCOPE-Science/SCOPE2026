# Sharp all-degree asymptotics for binomial-polynomial numerical semigroups

## Finding
For each fixed integer \(d\ge 2\), let \(a\ge2\) and \(b\ge1\) be coprime integers. Define the numerical semigroup
\[
S_d(a,b)=\left\langle ai+b\binom{i}{d}:i=1,2,3,\ldots\right\rangle,
\qquad c_d=(d!)^{1/d},\qquad \eta_d=\frac{d-1}{d^2}.
\]
Its Frobenius number \(F_d(a,b)\) and genus \(g_d(a,b)\) obey
\[
\boxed{F_d(a,b)=(a-1)b+c_da^{1+1/d}+O_d\bigl(a^{1+\eta_d}\bigr)}
\]
and
\[
\boxed{g_d(a,b)=\frac{(a-1)(b-1)}2+
\frac{d}{d+1}c_da^{1+1/d}+O_d\bigl(a^{1+\eta_d}\bigr).}
\]
Both error bounds have constants depending only on \(d\), uniformly for all \(b\ge1\) coprime to \(a\). Equivalently, after subtracting the indicated elementary \(b\)-terms, the normalized limits as \(a\to\infty\) are \(c_d\) and \(dc_d/(d+1)\), uniformly in those choices of \(b\). For \(d=2\), this refines the previously established order-of-growth estimates to constants \(\sqrt2\) and \(2\sqrt2/3\); the formulas additionally treat every fixed degree \(d\ge3\).

## Assumptions and scope
The notation \(\binom{i}{d}=0\) for \(i<d\) is used. A numerical semigroup is an additive submonoid of the nonnegative integers with finite complement. The Frobenius number is the largest omitted nonnegative integer, and the genus is the cardinality of the complement. The generator at \(i=1\) is \(a\); the generator at \(i=d\) is \(da+b\). These are coprime, so \(S_d(a,b)\) has finite complement and multiplicity \(a\). The exponent \(\eta_d\) is positive and strictly smaller than \(1/d\) for \(d\ge2\). All constants implicit in the asymptotic errors are independent of \(b\).

## Proof
**Step 1: the binomial-weight coin function.** For each nonnegative integer \(n\), put
\[
\mu_d(n)=\min\left\{\sum_{i\ge d}i x_i:
   \sum_{i\ge d}\binom{i}{d}x_i=n,
   \ x_i\in\mathbb Z_{\ge0},\ \text{finitely many nonzero}\right\}.
\]
In particular \(\mu_d(0)=0\), and every \(n\) is feasible because \(\binom d d=1\). The following uniform estimate is the key new quantitative lemma:
\[
(d!n)^{1/d}\ \le\ \mu_d(n)\ \le\ (d!n)^{1/d}
 +C_d(n+1)^{(d-1)/d^2}. \tag{1}
\]
For the lower bound, the nonnegative Vandermonde convolution implies
\(\binom{u+v}{d}\ge\binom u d+\binom v d\) for all nonnegative integers \(u,v\). Repeatedly applying this to any representation with total index cost \(M=\sum_i i x_i\) gives
\(n=\sum_i x_i\binom i d\le\binom M d\le M^d/d!\), proving the lower estimate.

For the upper estimate, write \(q=(d-1)/d\) and perform a greedy binomial decomposition. For a positive remainder \(m\), choose the largest integer \(k\ge d\) with \(\binom{k}{d}\le m\); subtract that binomial coin, at index cost \(k\). As \(\binom{k}{d}=k^d/d!+O_d(k^{d-1})\), the initial index is
\(k=(d!m)^{1/d}+O_d(1)\). The resulting remainder is strictly less than
\(\binom{k+1}{d}-\binom k d=\binom k{d-1}=O_d((m+1)^q)\). Upon repeating \(L\) times, the residual value is at most \(O_{d,L}((n+1)^{q^L})\). Choose a fixed \(L=L(d)\) so that \(q^L\le q/d\). The index costs after the first greedy coin are each \(O_d((n+1)^{q/d})\), while the final remainder may be paid for with copies of the unit binomial coin \(\binom d d=1\), costing \(d\) times that remainder. Thus the total is at most \((d!n)^{1/d}+O_d((n+1)^{q/d})\), establishing (1), since \(q/d=(d-1)/d^2\). This also handles bounded \(n\) after enlarging \(C_d\).

**Step 2: exact residue envelopes.** Each element of \(S_d(a,b)\) is of the form \(aM+bK\), where \(K\ge0\) is a sum of \(d\)-th binomial coefficients and \(M\) is the corresponding sum of indices. For any fixed \(K\), the smallest such \(M\) is \(\mu_d(K)\); the generators with \(i<d\) contribute only positive multiples of \(a\), so cannot lower this minimum. Because \(b\) is a unit modulo \(a\), for each \(r\in\{0,\ldots,a-1\}\) the least semigroup element in residue \(br\pmod a\) is
\[
w_r=br+a\lambda_r,\qquad
\lambda_r=\min_{j\ge0}\{\mu_d(r+ja)+bj\}. \tag{2}
\]
Every term in this minimum obeys \(\mu_d(r+ja)+bj\ge c_d(r+ja)^{1/d}+bj\ge c_dr^{1/d}\); the admissible choice \(j=0\), followed by (1), yields
\[
c_dr^{1/d}\le\lambda_r\le c_dr^{1/d}+C_d(r+1)^{\eta_d}. \tag{3}
\]
These bounds do not involve \(b\). The \(a\) values \(w_r\) form the Apéry set relative to multiplicity \(a\).

**Step 3: Frobenius number.** The standard Apéry identity gives \(F_d(a,b)=\max_{0\le r<a}w_r-a\). From (3), and using the \(r=a-1\) term for the lower bound,
\[
(a-1)b+ac_d(a-1)^{1/d}-a\le F_d(a,b)
\le(a-1)b+ac_d(a-1)^{1/d}+C_da^{1+\eta_d}-a.\tag{4}
\]
The upper bound uses monotonicity of both \(r^{1/d}\) and \((r+1)^{\eta_d}\) on this range. Since \(a(a-1)^{1/d}=a^{1+1/d}+O_d(a^{1/d})\), equation (4) proves the first asserted expansion.

**Step 4: genus.** The Apéry genus identity gives
\[
 g_d(a,b)=\frac1a\sum_{r=0}^{a-1}w_r-\frac{a-1}{2}
=\frac{(a-1)(b-1)}2+\sum_{r=0}^{a-1}\lambda_r. \tag{5}
\]
By (3), \(\sum_{r<a}\lambda_r=c_d\sum_{r<a}r^{1/d}+O_d(\sum_{r<a}(r+1)^{\eta_d})\). Integral comparison shows
\(\sum_{r<a}r^{1/d}=\frac{d}{d+1}a^{1+1/d}+O_d(a^{1/d})\), while the error sum is \(O_d(a^{1+\eta_d})\). Inserting these estimates into (5) proves the second expansion and completes the theorem.

## Verification
The included standalone `verify.py` uses only the Python standard library. It independently computes the Apéry set using shortest paths in the residue graph generated by sufficiently many actual polynomial generators, and also constructs the exact envelope (2) by unbounded-change dynamic programming for the binomial index costs. For all coprime pairs \(2\le a\le50\), \(b\in\{1,2,3,5,7,11\}\), and \(d\in\{2,3,4,5\}\), the two independently implemented computations agreed in all \(928\) finite cases. The generator cutoff in the residue-graph computation is rigorous: the two coprime generators \(a\) and \(da+b\) bound each Apéry representative above by \((a-1)(da+b)\), and every omitted generator is already larger than that bound. Computation checks finite instances of (2); the claims for every exponent and unbounded \(a,b\) are proved in Steps 1–4, not inferred from experiments.

## Relationship to prior work
Hashuga, Herbine and Jensen, *Numerical Semigroups Generated by Quadratic Sequences* (first public arXiv version dated 2020-09-04, arXiv:2009.01981), introduced the identical degree-two generator family. In their full text, Theorems 8.2–8.4 and Corollaries 8.3/8.5 give explicit nonmatching bounds and \(\Theta(a^{3/2}+ab)\) growth for the Frobenius number and genus. Their genus identity and the standard Apéry method are acknowledged. The present theorem sharpens the two quadratic asymptotics to explicit leading constants after removing their exact linear-in-\(b\) parts, establishes a uniform power-saving error, and treats every higher fixed degree. Their concluding discussion identifies higher-degree polynomial generators as a natural direction.

Liu, Xin, Ye and Yin, *On the Frobenius Number and Genus of a Collection of Semigroups Generalizing Repunit Numerical Semigroups* (arXiv:2306.03459), give Apéry methods for ordered repunit-type recurrence systems with substantially different coefficient constraints, not a theorem for the family above. Hwang and Song, *The Frobenius Problem for Numerical Semigroups Generated by Binomial Coefficients* (arXiv:2412.17882), determine invariants for finite sets of pure coefficients \(\binom n k\) with a fixed upper index; this does not cover the mixed generators \(ai+b\binom i d\) with variable upper index. No priority claim is made beyond the material inspected.

## Limitations
The result gives asymptotic expansions with explicit leading coefficients but not exact finite-parameter formulas, second-order constants, or a uniform estimate when the polynomial degree itself grows with \(a\). The power-saving exponent in the error may not be optimal. The novelty comparison is conditional on accessible and inspected literature: an earlier unindexed result or an indirect implication from uninspected stronger work remains possible. Independent mathematical audit has not been performed.

## References
1. M. Hashuga, M. Herbine and A. Jensen, *Numerical Semigroups Generated by Quadratic Sequences*, arXiv:2009.01981, 2020, https://arxiv.org/abs/2009.01981.
2. F. Liu, G. Xin, S. Ye and J. Yin, *On the Frobenius Number and Genus of a Collection of Semigroups Generalizing Repunit Numerical Semigroups*, arXiv:2306.03459, 2023, https://arxiv.org/abs/2306.03459.
3. W. Hwang and K. Song, *The Frobenius Problem for Numerical Semigroups Generated by Binomial Coefficients*, arXiv:2412.17882, first public 2024, https://arxiv.org/abs/2412.17882.
