# Isotropic quadratic stability at the uniform finite-field moment-curve extremizer

## Finding

Let \(d\ge2\), let \(q=p^n\) with prime \(p>d\), and let
\[
\Gamma=\{\gamma(t)=(t,t^2,\ldots,t^d):t\in\mathbb F_q\}
\]
carry normalized counting measure \(\sigma\). Let \(A=A_{d,q}\) denote the sharp endpoint constant in
\[
\|(f\sigma)^\vee\|_{L^{2d}(\mathbb F_q^d,dx)}
\le
A^{1/(2d)}\|f\|_{L^2(\Gamma,d\sigma)}.
\]

For a normalized function
\[
\|f\|_{L^2(\Gamma,d\sigma)}=1,
\]
write
\[
v_\xi=|f(\gamma(\xi))|^2-1.
\]
Then
\[
\sum_{\xi\in\mathbb F_q}v_\xi=0.
\]
As \(\max_\xi|v_\xi|\to0\),
\[
A-\|(f\sigma)^\vee\|_{L^{2d}}^{2d}
=
\gamma_{d,q}\sum_\xi v_\xi^2
+
O_{d,q}\!\left(
\left(\sum_\xi v_\xi^2\right)^{3/2}
\right),
\]
where
\[
\gamma_{d,q}
=
\frac{q^{-d}}4
\sum_{s=2}^{d}
\binom ds^2
B_{d-s,q-2}
\frac{s(s-1)}{2s-1}
\binom{2s}{s}
>0,
\]
and
\[
B_{r,Q}
=
\sum_{\substack{n_1+\cdots+n_Q=r\\n_j\ge0}}
\binom{r}{n_1,\ldots,n_Q}^{\!2},
\qquad
B_{0,Q}=1.
\]

Equivalently, if
\[
F_{d,q}(\theta)=\mathbb E_\theta[M(T)]
\]
is the expected number of distinct rearrangements of a \(d\)-sample with law \(\theta\), and
\[
\theta_0=(1/q,\ldots,1/q),
\]
then for \(\sum_\xi h_\xi=0\),
\[
F_{d,q}(\theta_0)-F_{d,q}(\theta_0+h)
=
C_{d,q}\|h\|_2^2+O_{d,q}(\|h\|_2^3),
\]
where
\[
C_{d,q}=q^2\gamma_{d,q}.
\]
Thus the Hessian of \(F_{d,q}\), restricted to the tangent space of the simplex, is exactly
\[
-2C_{d,q}I.
\]
The local curvature at the uniform extremizer is therefore isotropic.

For \(d=2\),
\[
\gamma_{2,q}=q^{-2},
\]
and the deficit is exactly quadratic.

## Assumptions and scope

The field size is a prime power \(q=p^n\) whose characteristic satisfies \(p>d\), exactly as in the sharp endpoint theorem. The physical-space measure \(dx\) and the curve measure \(d\sigma\) use the normalizations of the cited finite-field extension theorem.

The statement controls only modulus perturbations because the endpoint norm depends on \(f\) only through \(|f|\). It is a local stability expansion near the constant-modulus extremizer set; it is not a global stability inequality.

For fixed \(d\) and \(q\), the remainder is taken as the Euclidean tangent perturbation tends to zero. No uniformity in growing \(d\) or \(q\) is asserted.

## Proof

Define
\[
x_\xi=|f(\gamma(\xi))|^2.
\]
The normalization \(\|f\|_2=1\) gives
\[
\sum_\xi x_\xi=q.
\]
The exact probabilistic reformulation in the source identifies
\[
\theta_\xi=\frac{x_\xi}{q}
\]
and, for normalized \(f\),
\[
\|(f\sigma)^\vee\|_{2d}^{2d}=F_{d,q}(\theta),
\qquad
A=F_{d,q}(\theta_0).
\]
Hence it is enough to compute the Hessian of \(F_{d,q}\) at \(\theta_0\).

The polynomial \(F_{d,q}\) is invariant under every permutation of the \(q\) coordinates. Therefore its Hessian at \(\theta_0\) commutes with the full permutation representation. On the tangent hyperplane
\[
\left\{h:\sum_\xi h_\xi=0\right\},
\]
that representation is irreducible over the reals for \(q\ge3\), so the restricted Hessian is a scalar multiple of the identity. It suffices to compute the second variation in one direction.

Choose two distinct symbols \(a,b\) and set
\[
\theta(t)=\theta_0+t(e_a-e_b).
\]
The total mass of the pair is fixed:
\[
m=\theta_a(t)+\theta_b(t)=\frac2q.
\]
Writing
\[
\rho(t)=\frac{\theta_a(t)}m=\frac12+\frac q2t,
\]
the pair-merging identity from the source gives
\[
F_{d,q}(\theta(t))
=
\mathbb E_{\widetilde\theta}
\bigl[M(\widetilde T)H_S(\rho(t))\bigr],
\]
where \(S\) is the number of merged symbols in the projected sample and the merged law \(\widetilde\theta\) is independent of \(t\).

The source writes
\[
H_s(\rho)=P_s(c),
\qquad
c=\rho(1-\rho),
\]
with
\[
P_s(c)
=
\sum_{j=0}^{\lfloor s/2\rfloor}
\binom{s}{2j}\binom{2j}{j}c^j.
\]
At \(\rho=1/2\),
\[
H_s(1/2)
=
2^{-s}\binom{2s}{s}.
\]
A binomial differentiation identity gives
\[
P_s'(1/4)
=
2s\bigl(H_s(1/2)-H_{s-1}(1/2)\bigr)
=
\frac{2s(s-1)}{2s-1}
\,2^{-s}\binom{2s}{s}.
\]
Also,
\[
c(t)=\frac14-\frac{q^2t^2}{4}.
\]
Therefore
\[
F_{d,q}(\theta_0)-F_{d,q}(\theta(t))
=
\frac{q^2t^2}{4}
\mathbb E_{\widetilde\theta}
\bigl[M(\widetilde T)P_S'(1/4)\bigr]
+
O_{d,q}(t^4).
\]

Under the uniform merged law, the merged symbol has probability \(2/q\), while each of the remaining \(q-2\) symbols has probability \(1/q\). Conditioning on \(S=s\), summing over the remaining multiplicities, and using
\[
B_{r,Q}
=
\sum_{n_1+\cdots+n_Q=r}
\binom{r}{n_1,\ldots,n_Q}^{\!2}
\]
gives
\[
\mathbb E_{\widetilde\theta}
\bigl[M(\widetilde T)P_S'(1/4)\bigr]
=
q^{-d}
\sum_{s=2}^{d}
\binom ds^2
B_{d-s,q-2}
\frac{2s(s-1)}{2s-1}
\binom{2s}{s}.
\]
Because
\[
\|\theta(t)-\theta_0\|_2^2=2t^2,
\]
the tangent quadratic coefficient is
\[
C_{d,q}
=
\frac{q^{2-d}}4
\sum_{s=2}^{d}
\binom ds^2
B_{d-s,q-2}
\frac{s(s-1)}{2s-1}
\binom{2s}{s}.
\]
Permutation symmetry now gives the same coefficient in every tangent direction. Since \(F_{d,q}\) is a degree-\(d\) polynomial, Taylor's theorem supplies the stated cubic remainder for general tangent perturbations.

Finally,
\[
h_\xi=\theta_\xi-\frac1q=\frac{v_\xi}{q},
\]
so
\[
\gamma_{d,q}=\frac{C_{d,q}}{q^2}.
\]
Every summand in the formula for \(\gamma_{d,q}\) is nonnegative and the \(s=2\) term is positive, proving strict local curvature.

When \(d=2\), the source gives
\[
F_{2,q}(\theta)=2-\sum_\xi\theta_\xi^2,
\]
so the quadratic expansion is exact and \(\gamma_{2,q}=q^{-2}\).

## Verification

The accompanying verifier uses exact rational arithmetic. For several admissible pairs \((d,q)\), it computes the Hessian of
\[
F_{d,q}(\theta)
=
\sum_{t\in\{1,\ldots,q\}^d}
M(t)\prod_{j=1}^d\theta_{t_j}
\]
at the uniform distribution by direct finite enumeration. It compares the tangent Hessian coefficient with the closed formula for \(C_{d,q}\) and checks exact equality.

This finite computation is only an algebraic sanity check for the coefficient formula. The theorem itself is proved for all admissible \(d,q\) by the analytic permutation-symmetry and pair-merging argument above.

## Relationship to prior work

The 2026 endpoint paper proves the sharp finite-field moment-curve extension inequality, characterizes all maximizers by constant modulus, and gives the probabilistic reformulation in which the uniform distribution uniquely maximizes the expected number of distinct rearrangements. Its pair-merging proof supplies the exact one-variable polynomial \(H_s\), but it does not state the Hessian or a quantitative local deficit at the uniform distribution.

A follow-up paper proves a stronger component-wise permutation-match inequality by majorization and recovers the same uniform maximizer. Its full text does not state a quadratic stability expansion, Hessian, or local curvature constant.

The authors' earlier endpoint paper establishes sharp constants and maximizers in complementary finite-field regimes but does not contain the present local stability calculation.

The source also notes that Schur-concavity of the probabilistic functional is a special case of an earlier theorem of Rinott. Accessible bibliographic material for that paper does not state the quantitative Hessian formula above; the full 1973 text was not accessible during this review, so this remains a literature-comparison risk.

## Limitations

The result is local. It does not give a best global lower bound for the deficit in terms of distance to the constant-modulus extremizer set.

The curvature coefficient controls only modulus perturbations, which are exactly the perturbations visible to the endpoint norm. Phases remain flat directions.

No asymptotic simplification of \(C_{d,q}\) as \(q\) or \(d\) grows is claimed. The full text of the 1973 Schur-concavity antecedent was not accessible during the literature comparison, so an equivalent older differential formula cannot be completely excluded.

## References

1. C. Biswas, E. Carneiro, T. C. Flock, J. Madrid, D. Oliveira e Silva, B. Stovall, and J. Tautges, *Sharp endpoint extension inequalities for the moment curve on finite fields II: an extremal property of the uniform distribution*, arXiv:2609.29882v1, 2026.
2. F. Gonçalves, *A component-wise inequality for permutation matches*, arXiv:2609.31979v1, 2026.
3. C. Biswas, E. Carneiro, T. C. Flock, D. Oliveira e Silva, B. Stovall, and J. Tautges, *Sharp endpoint extension inequalities for the moment curve on finite fields*, arXiv:2508.08377v1, 2025.
4. Y. Rinott, *Multivariate majorization and rearrangement inequalities with some applications to probability and statistics*, Israel J. Math. 15 (1973), 60--77.
