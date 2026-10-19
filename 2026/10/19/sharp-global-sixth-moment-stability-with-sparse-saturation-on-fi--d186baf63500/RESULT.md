# Sharp global sixth-moment stability with sparse saturation on finite-field moment curves

## Finding

Let \(q=p^n\) be a prime power with characteristic \(p>3\), and let \(\Gamma=\{(t,t^2,t^3):t\in\mathbb F_q\}\). Give \(\Gamma\) uniform probability measure \(\sigma\) and \(\mathbb F_q^3\) counting measure. For \(f:\mathbb F_q\to\mathbb C\) define the normalized Fourier extension
\[
E f(x)=\frac1q\sum_{t\in\mathbb F_q} f(t)\,\psi(x_1t+x_2t^2+x_3t^3),
\quad x\in\mathbb F_q^3,
\]
where \(\psi\) is a nontrivial additive character. For nonzero \(f\), put
\[
N=\|f\|_{L^2(\sigma)}^2,\qquad
\theta_t=\frac{|f(t)|^2}{qN},\qquad
\nu_t=\frac1q,
\qquad A_q=6-\frac9q+\frac4{q^2}.
\]
Thus \(\theta\) is a probability vector. Then the exact sixth-moment deficit admits the **nonnegative sum-of-squares decomposition**
\[
\boxed{\displaystyle
A_q-\frac{\|Ef\|_{\ell^6(\mathbb F_q^3)}^6}{N^3}
=\left(5-\frac4q\right)\sum_t(\theta_t-\nu_t)^2
+\frac4q\sum_{\{s,t\}\subset\mathbb F_q,\ s\ne t}
 (\theta_s-\theta_t)^2(1-\theta_s-\theta_t).}
\tag{1}
\]
Each unordered two-element subset appears exactly once in the second sum. Consequently,
\[
\boxed{\displaystyle
A_qN^3-\|Ef\|_{\ell^6}^6
\ge \frac{5-4/q}{q}\,N\,
\big\||f|^2-N\big\|_{L^2(\sigma)}^2.}
\tag{2}
\]
The coefficient \(5-4/q\) in the probability-vector form is the **largest possible global coefficient**. Equality in the inequality obtained by omitting the second summand in (1), equivalently in (2), holds exactly for constant-modulus signals (\(|f(t)|\) independent of \(t\)) and signals supported at a single point; the zero signal satisfies (2) trivially. In particular, among nonuniform probability vectors, the sharp global remainder is saturated only at vertices of the simplex.

At the uniform vector the deficit instead has the strictly larger local quadratic curvature \(9-12/q\): for \(\theta_t=1/q+h_t\) with \(\sum_t h_t=0\),
\[
A_q-F_3(\theta)=\left(9-\frac{12}{q}\right)\sum_t h_t^2-4\sum_t h_t^3,
\quad F_3(\theta)=6-9\sum_t\theta_t^2+4\sum_t\theta_t^3.
\tag{3}
\]
Thus sharp **global** stability is controlled by sparse boundary configurations rather than infinitesimal perturbations of the maximizer.

## Assumptions and scope

The restriction \(p>3\) ensures that the first three power sums determine the unordered triple via Newton identities, and is essential to the stated collision-count reduction. The definition of \(\ell^6\) uses counting measure on the entire physical vector space, not its uniform probability measure. All \(q\ge5\) with \(p>3\) are allowed, including nonprime fields. The only assumptions on the input are complex values and the displayed normalization. Phases of coefficients are unrestricted.

The coefficient \(A_q\) and constant-modulus maximizers were known; the contribution is the *sharp global quantitative deficit coefficient*, its exact nonnegative remainder, the complete equality alternatives, and the local/global stability separation.

## Proof

**1. Exact Fourier moment and collision polynomial.** For triples \(\mathbf s,\mathbf t\in\mathbb F_q^3\), character orthogonality shows that their terms in \(\|Ef\|_{\ell^6}^6\) interact precisely when
\(\sum_j s_j^r=\sum_j t_j^r\) for \(r=1,2,3\). Newton's identities, with \(2,3\) invertible, force equality of the monic cubics having the triples as roots. Hence \(\mathbf s\) and \(\mathbf t\) are permutations of one another. For any fixed ordered triple \(\mathbf t\), the number of distinct rearrangements is \(M(\mathbf t)=3!/\prod_a m_a!\), where \(m_a\) are the multiplicities. The Fourier phase factors cancel for each rearrangement, giving
\[
\|Ef\|_{\ell^6}^6
=q^{-3}\sum_{\mathbf t\in\mathbb F_q^3}M(\mathbf t)
\prod_{j=1}^{3}|f(t_j)|^2
=N^3\,\mathbb E_\theta M(T_1,T_2,T_3).
\tag{4}
\]
Here the \(T_j\) are independent with law \(\theta\). Put \(S_2=\sum_t\theta_t^2\) and \(S_3=\sum_t\theta_t^3\). The probabilities of, respectively, three equal entries, exactly two equal entries, and three distinct entries are \(S_3\), \(3(S_2-S_3)\), and \(1-3S_2+2S_3\). Their rearrangement counts are \(1,3,6\). Therefore
\[
F_3(\theta)=\mathbb E_\theta M
=S_3+9(S_2-S_3)+6(1-3S_2+2S_3)
=6-9S_2+4S_3.
\tag{5}
\]
In particular \(F_3(\nu)=A_q\) by substitution.

**2. Exact nonnegative decomposition.** The variance identity on the probability simplex is
\[
\sum_{s<t}(\theta_s-\theta_t)^2=qS_2-1,
\tag{6}
\]
and, expanding the factor \(\theta_s+\theta_t\),
\[
\sum_{s<t}(\theta_s-\theta_t)^2(\theta_s+\theta_t)=qS_3-S_2.
\tag{7}
\]
The notation \(s<t\) here refers to any temporary ordering of the index set. Subtracting (7) from (6) gives
\[
R(\theta):=\sum_{s<t}(\theta_s-\theta_t)^2(1-\theta_s-\theta_t)
=(q+1)S_2-qS_3-1.
\tag{8}
\]
Because \(\theta_s+\theta_t\le1\), every summand in \(R\) is nonnegative. Equations (5) and (8), together with \(\|\theta-\nu\|_2^2=S_2-1/q\), now give the identity
\[
A_q-F_3(\theta)
=\left(5-\frac4q\right)\left(S_2-\frac1q\right)+\frac4q R(\theta),
\]
which proves (1). Finally,
\[
\|\theta-\nu\|_2^2
=\frac1{qN^2}\big\||f|^2-N\big\|_{L^2(\sigma)}^2,
\]
which converts (1) into (2).

**3. Equality and sharpness.** The term \(R\) vanishes at \(\nu\) and every point mass. Conversely, suppose \(R=0\) and \(\theta\ne\nu\). There exist indices \(a,b\) with \(\theta_a\ne\theta_b\). Their nonzero squared difference forces \(\theta_a+\theta_b=1\), so every other coordinate is zero. If both \(\theta_a\) and \(\theta_b\) were positive, choosing a third index \(c\) would give the strictly positive summand \(\theta_a^2(1-\theta_a)\), a contradiction. Thus exactly one coordinate equals \(1\). A point mass satisfies \(\|\theta-\nu\|_2^2=1-1/q>0\), so any global coefficient larger than \(5-4/q\) fails already there. This proves optimality and the asserted equality alternatives. The expansion (3) follows by inserting \(\theta_t=1/q+h_t\) into (5).

## Verification

A separately implemented standalone checker, `verify_sharp_triple_stability.py`, uses exact rational arithmetic to compute \(F_3\) both by enumeration of all ordered triples and by the symmetric polynomial (5). It checks (1), the sharp vertex case, and strictness on sampled nontrivial vectors, including all \(210\) five-coordinate probability vectors with integer numerator summing to \(6\), together with \(18\) additional vectors for alphabet sizes \(5,7,11\). It separately constructs the finite-field Fourier extension sum from first principles for \(8\) complex-valued inputs at prime fields \(5\) and \(7\), and matches the normalized sixth moments to the collision polynomial. Running it prints `VERIFY_OK exact_prob_cases= 228 independent_fourier_cases= 8`.

The finite checks do not prove the all-prime-power statement; that follows from character orthogonality, the Newton identities, and the exact algebra above.

## Relationship to prior work

Biswas, Carneiro, Flock, Oliveira e Silva, Stovall, and Tautges (2025) already determine the sharp sixth-moment constant \(A_q\) and its extremizers at the cubic endpoint. The 2026 sequel (with Madrid) proves the general dimension-uniformity theorem using distinct-rearrangement expectations. Neither inspected source states the sharp global cubic deficit decomposition (1). Gonçalves (2026) establishes stronger qualitative majorization of permutation matches, which does not by itself supply the sharp numerical global remainder or its equality set.

The publicly available research record *Quadratic stability for endpoint finite-field moment-curve extension* proves the all-degree lower bound \(\tfrac{d(d-1)}2\|\theta-\nu\|_2^2\), which specializes to coefficient \(3\) in degree three and explicitly does not assert optimality when \(d>2\). Identity (1) improves \(3\) to the **best coefficient** \(5-4/q\), with exact residual and equality classification. The record *Isotropic quadratic stability at the uniform finite-field moment-curve extremizer* computes local Hessians but not the global optimum; the local cubic curvature in (3) is consistent with that work. These are statement-and-implication distinctions, not title distinctions.

## Limitations

This result concerns the degree-three endpoint in characteristic greater than three, not arbitrary moment-curve degrees, lower characteristic, other curves, or Euclidean restriction. The stability measures modulus-squared nonuniformity; the extension norm is phase-insensitive at this endpoint, so it cannot control phases. The already-known sharp endpoint constant is not claimed as a new discovery. The present claim's priority could be affected by an older unindexed strong-Schur-concavity identity for the same cubic rearrangement functional; accessible original and contemporary primary sources were checked, but exhaustive historical priority cannot be certified.

## References

1. C. Biswas, E. Carneiro, T. C. Flock, J. Madrid, D. Oliveira e Silva, B. Stovall, and J. Tautges, *Sharp endpoint extension inequalities for the moment curve on finite fields II: an extremal property of the uniform distribution*, arXiv:2609.29882v1, first posted 24 September 2026, https://arxiv.org/abs/2609.29882.
2. C. Biswas, E. Carneiro, T. C. Flock, D. Oliveira e Silva, B. Stovall, and J. Tautges, *Sharp endpoint extension inequalities for the moment curve on finite fields*, arXiv:2508.08377v1, first posted 11 August 2025, https://arxiv.org/abs/2508.08377.
3. F. Gonçalves, *A component-wise inequality for permutation matches*, arXiv:2609.31979v1, first posted 25 September 2026, https://arxiv.org/abs/2609.31979.
4. G. Peskir, *Best constants in Kahane--Khintchine inequalities for complex Steinhaus functions*, Proceedings of the American Mathematical Society 123 (1995), 3101--3111.
5. *Quadratic stability for endpoint finite-field moment-curve extension*, published published-finding corpus finding e3a60ec2aa94.
6. *Isotropic quadratic stability at the uniform finite-field moment-curve extremizer*, published published-finding corpus finding 49b4f93ca348.
