# Finite-support strong monotonicity characterizes translated Poisson-binomial laws

## Finding
For an arbitrary finitely supported integer-valued random variable \(X\), the strong monotonicity condition on every exponentially tilted characteristic-function modulus is equivalent to a finite algebraic condition: the shifted probability-generating polynomial has only strictly negative real zeros. Equivalently, \(X\) is a deterministic integer translate of a sum of independent, possibly nonidentical Bernoulli variables. This includes deterministic variables as the empty sum.

In particular, for \(k=\min\operatorname{supp}(X)\), \(d=\max\operatorname{supp}(X)-k\), and
\[
P(z)=\mathbb E[z^{X-k}]=\sum_{j=0}^{d}p_jz^j,\qquad p_0>0,\ p_d>0,\quad \sum_{j=0}^{d}p_j=1,
\]
the following conditions are equivalent:

1. For every real \(\theta\), the function \(t\mapsto |\mathbb E_\theta e^{itX}|\) is nonincreasing on \([0,\pi]\), where \(\mathbb P_\theta\{X=x\}=e^{\theta x}\mathbb P\{X=x\}/\mathbb E[e^{\theta X}]\).
2. Every complex root of \(P\) is strictly negative and real.
3. There exist independent Bernoulli variables \(B_1,\ldots,B_d\) with success parameters \(q_i\in(0,1)\) such that \(X\overset{\mathrm d}=k+\sum_{i=1}^d B_i\).

For a nonreal root \(\zeta\) of \(P\) in the upper half-plane, the explicit tilt \(\theta=\log|\zeta|\) violates (1): the tilted characteristic modulus vanishes at the interior angle \(\arg\zeta\), but is nonzero again at some larger angle. Thus even a single nonreal zero is a concrete obstruction.

## Assumptions and scope
The support of \(X\) is any nonempty *finite* subset of \(\mathbb Z\); gaps and point masses are allowed initially. In the cited probability-theoretic definition, a variable is monotone if the modulus of its characteristic function is nonincreasing on \([0,\pi]\), and strongly monotone if every exponential tilt is monotone and the moment-generating domain has more than one point. Finite support makes that domain all of \(\mathbb R\), so condition (1) is exactly strong monotonicity. No moments, positivity of intermediate coefficients, or regularity of a density are assumed.

When \(d=0\), \(P=1\), the root condition is vacuous and the characteristic modulus is identically one for every tilt. The Bernoulli sum is then empty. For \(d\geq1\), the Bernoulli parameters are uniquely determined up to permutation by the roots, and all intermediate coefficients of \(P\) are in fact strictly positive.

## Proof
First, integer translation multiplies any tilted characteristic function by a phase of modulus one. Writing \(r=e^\theta>0\), we therefore have the exact identity
\[
\big|\mathbb E_\theta e^{itX}\big|=\frac{|P(re^{it})|}{P(r)},\qquad 0\le t\le\pi,
\]
where \(P(r)>0\) follows from the nonnegative coefficients and \(p_0>0\).

Suppose (1) holds but \(P\) has a nonreal zero \(\zeta\). By reality of the coefficients, a conjugate root also exists, so choose \(\zeta\) with \(\operatorname{Im}\zeta>0\), and write \(\zeta=re^{it_0}\) with \(r>0\), \(0<t_0<\pi\). For the tilt \(\theta=\log r\), the nonnegative function \(t\mapsto |P(re^{it})|/P(r)\) equals zero at \(t_0\). Since this function is nonincreasing by (1), it must equal zero for every \(t\in[t_0,\pi]\). A nonzero polynomial cannot vanish at infinitely many distinct points on that circle. This contradiction excludes nonreal zeros. Because \(P\) has no nonnegative real root (all coefficients are nonnegative and \(p_0>0\)), all its roots are strictly negative. Hence (1) implies (2).

Conversely, suppose (2). When \(d\geq1\), write the roots, with multiplicities, as \(-\lambda_1,\ldots,-\lambda_d\) where every \(\lambda_i>0\). The normalization \(P(1)=1\) forces the factorization
\[
P(z)=\prod_{i=1}^{d}\frac{z+\lambda_i}{1+\lambda_i}
=\prod_{i=1}^{d}\big[(1-q_i)+q_i z\big],\qquad
q_i=\frac1{1+\lambda_i}\in(0,1).
\]
This is exactly the probability-generating function of a sum of independent Bernoulli variables, establishing (3). The empty product handles \(d=0\).

Finally, suppose (3). Under a tilt by \(\theta\), each independent Bernoulli component remains independent and Bernoulli, with success probability
\[
q_i(\theta)=\frac{q_i e^{\theta}}{1-q_i+q_i e^{\theta}}\in(0,1).
\]
For each component,
\[
\big|1-q_i(\theta)+q_i(\theta)e^{it}\big|^2
=1-2q_i(\theta)(1-q_i(\theta))(1-\cos t).
\]
The right side is nonincreasing on \([0,\pi]\); its nonnegative square root is therefore nonincreasing. The modulus of the characteristic function of the sum is a product of such nonnegative, nonincreasing functions, hence is nonincreasing. The deterministic shift contributes only a phase. Thus (3) implies (1), completing the equivalence.

**Strictness of the weaker condition.** Ordinary monotonicity alone does not imply strong monotonicity, even on three consecutive support values. Let the probabilities at \(0,1,2\) be \((90,9,1)/100\); then \(P(z)=(90+9z+z^2)/100\). For a quadratic with nonnegative coefficients \(a,b,c\), the identity
\[
\frac{d}{dt}|a+be^{it}+ce^{2it}|^2
=-2\sin t\,[b(a+c)+4ac\cos t]
\]
shows that ordinary monotonicity holds precisely when \(b(a+c)\geq4ac\). Here this criterion is strict, but the discriminant \(b^2-4ac\) is negative. The roots are \((-9\pm i\sqrt{279})/2\), so at the tilt \(\theta=\tfrac12\log90\), the modulus is zero at the interior argument of the upper root and equals \((20-\sqrt{90})/(20+\sqrt{90})>0\) at \(t=\pi\). The weaker and stronger conditions are genuinely distinct.

## Verification
The proof above uses a polynomial-zero argument and elementary Bernoulli factorization, not a finite computation. An independent, standard-library-only supplementary script `verify.py` checks exact rational factorization of a four-Bernoulli polynomial; enumerates \(10{,}648\) strictly positive integer-coefficient quadratics, including \(608\) with ordinary but not strong monotonicity; and checks the explicit three-point counterexample. Execute `python3 verify.py` in the directory containing the files.

The exhaustive coefficient grid is *not* an exhaustive test of arbitrary-degree polynomials or a replacement for the proof. The displayed witness has an exact root and positive-endpoint certificate; the script's floating-point values merely illustrate their locations.

## Relationship to prior work
Aamand, Alon, Houen, and Thorup introduced the strong-monotonicity condition in their 2021 preprint and used it for sharp tail point-probability estimates. Their later journal manuscript states that Bernoulli, geometric, and Poisson laws are strongly monotone and that independent sums preserve monotonicity. Its relevant eight-page text establishes the forward example for Bernoulli sums but does not provide the converse finite-support classification or the nonreal-zero obstruction above. The deterministic integer shift and zero-root criterion are not claims about the infinitely supported geometric or Poisson examples.

Aissen, Edrei, Schoenberg, and Whitney studied the classical connection between negative-real-root generating polynomials and total positivity. Bernoulli factorization is also standard. The present result claims neither those classical ingredients nor the already-established forward inclusion as new: it identifies the **equivalence** of finite-support strong Fourier monotonicity with that algebraic class.

## Limitations
The characterization is only for finite-support integer distributions. Infinite-support laws, including geometric and Poisson examples, need not have polynomial generating functions; no classification is asserted for them. Ordinary monotonicity without tilting is demonstrably weaker. The result supplies a theoretical root criterion and an explicit failure certificate, not a numerically robust root-finding algorithm for poorly conditioned probability vectors.

## References
1. Aamand, A., Alon, N., Houen, J. B. T., and Thorup, M. *On Sums of Monotone Random Integer Variables*. First arXiv submission 8 April 2021, arXiv:2104.03721; *Electronic Communications in Probability* 27 (2022), article 64, DOI:10.1214/22-ECP500. The 2021 preprint and accessible later author manuscript were inspected.
2. Aissen, M., Edrei, A., Schoenberg, I. J., and Whitney, A. *On the Generating Functions of Totally Positive Sequences*. *Proceedings of the National Academy of Sciences* 37 (1951), 303–307, DOI:10.1073/pnas.37.5.303. Historical context for negative-real-root generating functions; not used as a proof dependency.
3. Weisstein, E. W. *Poisson Binomial Distribution*. Wolfram MathWorld, https://mathworld.wolfram.com/PoissonBinomialDistribution.html. Standard Bernoulli-product probability-generating function.
