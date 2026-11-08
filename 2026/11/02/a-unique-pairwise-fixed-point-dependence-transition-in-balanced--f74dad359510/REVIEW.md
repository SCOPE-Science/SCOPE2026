# Independent mathematical audit

## correctness

PASS

Conditional on K=k intra-A images, there are (m!)^2 C(m,k)^2 permutations and B has exactly k within-block matched rows. Each tagged B label is fixed with conditional probability k/m^2, and two distinct tagged B labels with probability k(k-1)/[m^2(m-1)^2], yielding exact covariance theta^2 H_m/[m^4(m-1)^2 Z_m^2]. Z_m=sum C(m,k)^2 theta^k is the Legendre transformed polynomial with m distinct negative real roots -rho_i. Setting S_j=sum(theta+rho_i)^(-j) gives H_m/Z_m^2=(2m-1)S_1^2-m^2 S_2; the derivative of S_1^2/S_2 is strictly positive by strict Cauchy–Schwarz because rho_i are distinct. H(0)<0 and the uniform permutation theta=1 covariance =1/[4m^2(2m-1)]>0 give one unique switch theta_m in (0,1). Differentiating the saddle-point/elementary integral representation of Z_m gives E K=mx+O(1), Var K=(m/2)x(1-x)+O(1), x=sqrt(theta)/(1+sqrt(theta)); substituting into exact covariance gives m^3 Cov -> x(3x-1)/2 and theta_m ->1/4 by sign bracketing. Completely enumerated permutations for m=2,3, checked conditional probabilities and covariance for four rational theta values, exact Legendre denominator. These finite instances corroborate, not prove, the general root and asymptotic results.

## originality

PASS

Ottolini–Starr (arXiv:2605.25274) already derive the SAME binomial-square normalizer and its Legendre representation for balanced two-block permanent/permutation weights, including large-block asymptotics. Duan–Lyu–Powell (arXiv:2610.14616) provide more general Gibbs permutation/block contingency couplings and macroscopic fluctuations. The assessed increment is microscopic pairwise tagged diagonal fixed-point covariance, a single finite-m sign reversal, and the universal limiting threshold 1/4. General CLT statements for block statistics do not directly impose the exact finite-size sign uniqueness. Fisher noncentral hypergeometric theory also covers K but not event covariance sign geometry. Prior normalization is fully credited.

## value

PASS

The covariance sign distinguishes competition among diagonal slots from common latent block-preservation fluctuations, a natural question for Gibbs random matching. An exact phase diagram at every m and a fixed nontrivial limiting critical bias 1/4 identify a microscopic dependence transition not visible from partition-function normalization alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
