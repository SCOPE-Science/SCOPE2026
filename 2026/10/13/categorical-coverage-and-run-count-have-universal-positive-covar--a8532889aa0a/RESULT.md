# Categorical coverage and run count have universal positive covariance
## Finding
Let \(X_1,\ldots,X_n\), \(n\ge2\), be iid on a finite alphabet
\[
\{1,\ldots,m\},
\qquad m\ge2,
\]
with strictly positive symbol probabilities \(p_1,\ldots,p_m\). Define
\[
K_n=\#\{X_1,\ldots,X_n\}
\]
and
\[
T_n=\sum_{j=1}^{n-1}\mathbf 1\{X_j\ne X_{j+1}\}.
\]
Thus \(K_n\) is categorical coverage, while the number of runs is
\[
R_n=T_n+1.
\]

Writing
\[
s_2=\sum_{i=1}^m p_i^2,
\]
the exact covariance is
\[
\boxed{
\operatorname{Cov}(K_n,T_n)
=
(n-1)\sum_{i=1}^m
p_i(1-p_i)^{n-2}
\left[
2s_2-(1+s_2)p_i
\right].
}
\]
For every nondegenerate probability vector this quantity is strictly positive:
\[
\boxed{
\operatorname{Cov}(K_n,T_n)>0.
}
\]
The same statement holds with \(T_n\) replaced by \(R_n\).

There is an equivalent local interpretation. Put
\[
I=\mathbf 1\{X_1\ne X_2\}.
\]
Then
\[
\operatorname{Cov}(K_n,T_n)
=
(n-1)\operatorname{Cov}(K_n,I),
\]
so the strict positivity says that forcing one adjacent pair to be a switch rather than a repeat raises expected global coverage:
\[
\boxed{
\mathbb E[K_n\mid X_1\ne X_2]
>
\mathbb E[K_n\mid X_1=X_2].
}
\]

For the uniform law \(p_i=1/m\),
\[
\boxed{
\operatorname{Cov}(K_n,T_n)
=
\frac{(n-1)(m-1)}{m^2}
\left(1-\frac1m\right)^{n-2},
}
\]
and the conditional gap simplifies to
\[
\boxed{
\mathbb E[K_n\mid X_1\ne X_2]
-
\mathbb E[K_n\mid X_1=X_2]
=
\left(1-\frac1m\right)^{n-2}.
}
\]

## Assumptions and scope
The observations are iid and the alphabet is finite. All listed symbol probabilities are positive; zero-probability symbols can simply be removed from the alphabet.

Coverage counts symbols appearing at least once. Runs are maximal consecutive blocks of equal symbols, so \(R_n=1+T_n\).

The theorem allows arbitrary unequal categorical probabilities. It does not assert the same sign for Markov-dependent sequences, sampling without replacement, or fixed-composition random words.

## Proof
For each symbol \(a\), let
\[
A_a=\mathbf 1\{\text{symbol }a\text{ appears among }X_1,\ldots,X_n\}.
\]
Then
\[
K_n=\sum_{a=1}^mA_a.
\]
For \(1\le j<n\), write
\[
I_j=\mathbf 1\{X_j\ne X_{j+1}\}.
\]
By iid symmetry, \(\operatorname{Cov}(K_n,I_j)\) does not depend on \(j\). Hence
\[
\operatorname{Cov}(K_n,T_n)
=
(n-1)\sum_{a=1}^m\operatorname{Cov}(A_a,I_1).
\]

Fix \(a\), write \(p=p_a\), and retain
\[
s_2=\sum_{i=1}^m p_i^2.
\]
Since
\[
\mathbb P(I_1=1)=1-s_2
\]
and
\[
\mathbb P(A_a=0)=(1-p)^n,
\]
we only need the probability that the distinguished adjacent pair is unequal while symbol \(a\) never appears. The first two positions must then be distinct symbols different from \(a\), while the remaining positions merely avoid \(a\). Thus
\[
\mathbb P(A_a=0,I_1=1)
=
(1-p)^{n-2}
\left[
(1-p)^2-(s_2-p^2)
\right].
\]
Subtracting the product of marginals gives
\[
\operatorname{Cov}(A_a,I_1)
=
p(1-p)^{n-2}
\left[
2s_2-(1+s_2)p
\right].
\]
Summing over \(a\) proves the exact covariance formula.

It remains to prove that the sum is always positive, even though an individual symbol contribution can be negative for a sufficiently heterogeneous probability vector. Put
\[
t=n-2
\]
and define
\[
U_t=\sum_i p_i(1-p_i)^t,
\qquad
V_t=\sum_i p_i^2(1-p_i)^t,
\qquad
W_t=\sum_i p_i^3(1-p_i)^t.
\]
Then
\[
U_{t+1}=U_t-V_t,
\qquad
V_{t+1}=V_t-W_t.
\]
With
\[
\rho_t=\frac{V_t}{U_t},
\]
we obtain
\[
\rho_{t+1}-\rho_t
=
\frac{V_t^2-U_tW_t}{U_t(U_t-V_t)}
\le0,
\]
because Cauchy--Schwarz gives
\[
V_t^2\le U_tW_t.
\]
Since
\[
\rho_0=s_2,
\]
it follows that
\[
\rho_t\le s_2.
\]
The exact covariance can therefore be rewritten as
\[
\operatorname{Cov}(K_n,T_n)
=
(n-1)U_t
\left[
2s_2-(1+s_2)\rho_t
\right],
\]
and hence
\[
\operatorname{Cov}(K_n,T_n)
\ge
(n-1)U_t\,s_2(1-s_2)>0.
\]
The last inequality uses nondegeneracy: \(0<s_2<1\) and \(U_t>0\).

For the uniform distribution, \(s_2=1/m\) and every summand is equal, giving the displayed closed form. Finally,
\[
\operatorname{Cov}(K_n,I)
=
\mathbb P(I=1)\mathbb P(I=0)
\left(
\mathbb E[K_n\mid I=1]-\mathbb E[K_n\mid I=0]
\right).
\]
Under uniform sampling,
\[
\mathbb P(I=1)=\frac{m-1}{m},
\qquad
\mathbb P(I=0)=\frac1m,
\]
and dividing the one-pair covariance yields the stated conditional gap.

## Verification
The accompanying `checker.py` independently enumerates finite iid words under several rational nonuniform probability vectors. It computes the exact weighted expectations of \(K_n\), \(T_n\), and their product, and checks the covariance identity with rational arithmetic.

The checker separately verifies the uniform specialization, the conditional switch-versus-repeat gap, and the monotonicity argument for \(\rho_t\) over a broad finite family of rational probability vectors. These finite checks supplement, rather than replace, the all-\(n\) proof.

## Relationship to prior work
Classical runs literature studies distributions of runs and more general patterns in iid multi-state trials. Johnson and Fu give an exact and approximate framework for run and pattern counts in multi-state sequences.

Classical occupancy literature studies the number of distinct observed symbols and the full occupancy-frequency vector. Ben-Hamou, Boucheron, and Ohannessian treat these coverage statistics for iid sampling from discrete distributions.

The present identity couples the order-sensitive run statistic to the order-insensitive coverage statistic. The inspected run source does not study coverage, and the inspected occupancy source does not study adjacent-run statistics. The proof also identifies a structural positivity mechanism that is not supplied by either marginal theory alone.

## Limitations
The iid assumption is essential to the proof. Conditioning on a fixed composition generally changes adjacent-transition dependence, while Markov dependence destroys the simple two-position factorization.

The result is a covariance and conditional-mean statement. It does not imply positive association for all increasing functions of coverage and run count, nor does it determine their complete joint distribution.

Older run-distribution or occupancy literature may encode this mixed moment through a multivariate generating function under different notation. Targeted searches did not locate such a formula, but this remains the main originality risk.

## References
1. B. C. Johnson and J. C. Fu, “Approximating the distributions of runs and patterns,” *Journal of Statistical Distributions and Applications* 1, 5 (2014). DOI: 10.1186/2195-5832-1-5.
2. A. Ben-Hamou, S. Boucheron, and M. I. Ohannessian, “Concentration inequalities in the infinite urn scheme for occupancy counts and the missing mass, with applications,” arXiv:1412.8652.
