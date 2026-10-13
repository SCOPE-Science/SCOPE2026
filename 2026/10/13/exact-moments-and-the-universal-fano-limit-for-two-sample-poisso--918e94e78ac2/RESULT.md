# Exact moments and the universal Fano limit for two-sample Poisson extremes
## Finding
Let \(X,Y\stackrel{\mathrm{iid}}{\sim}\operatorname{Pois}(\lambda)\) with \(\lambda>0\), and define the two order statistics
\[
M=\min(X,Y),\qquad A=\max(X,Y).
\]
Write \(I_\nu\) for the modified Bessel function of the first kind and put
\[
r_\lambda=e^{-2\lambda}I_0(2\lambda),\qquad
q_\lambda=e^{-2\lambda}\bigl(I_0(2\lambda)+I_1(2\lambda)\bigr).
\]
Then the first two moments are explicit:
\[
\mathbb EM=\lambda(1-q_\lambda),\qquad
\mathbb EA=\lambda(1+q_\lambda),
\]
\[
\operatorname{Var}(M)=\lambda\bigl(1-r_\lambda-\lambda q_\lambda^2\bigr),\qquad
\operatorname{Var}(A)=\lambda\bigl(1+r_\lambda-\lambda q_\lambda^2\bigr).
\]
In particular, the minimum and maximum have the same limiting index of dispersion,
\[
\frac{\operatorname{Var}(M)}{\mathbb EM},\ 
\frac{\operatorname{Var}(A)}{\mathbb EA}
\longrightarrow 1-\frac1\pi=0.6816901138162093\ldots .
\]
More sharply, with
\[
c=\frac{1/2-1/\pi}{\sqrt\pi}=0.1025076696487116\ldots>0,
\]
\[
\frac{\operatorname{Var}(M)}{\mathbb EM}
=1-\frac1\pi+c\lambda^{-1/2}+O(\lambda^{-1}),\qquad
\frac{\operatorname{Var}(A)}{\mathbb EA}
=1-\frac1\pi-c\lambda^{-1/2}+O(\lambda^{-1}).
\]
Thus the qualitative underdispersion of Poisson order statistics has a nontrivial universal large-intensity deficit \(1/\pi\), and the lower and upper extremes approach that common limit from opposite first-order directions.

## Assumptions and scope
The statement concerns exactly two independent Poisson variables with a common intensity \(\lambda>0\). It is an exact finite-\(\lambda\) identity plus a fixed-order large-\(\lambda\) expansion. It does not assert analogous constants for samples of size larger than two or for unequal Poisson means.

## Proof
Set
\[
S=X+Y,\qquad D=X-Y,
\]
so that
\[
M=\frac{S-|D|}2,\qquad A=\frac{S+|D|}2.
\]
For equal Poisson means, \(D\) has the symmetric Skellam mass function
\[
\Pr(D=k)=e^{-2\lambda}I_{|k|}(2\lambda),\qquad k\in\mathbb Z.
\]
Let \(d(\lambda)=\mathbb E|D|\). The Bessel recurrence
\[
kI_k(z)=\frac z2\bigl(I_{k-1}(z)-I_{k+1}(z)\bigr)
\]
telescopes to
\[
\sum_{k\ge1}kI_k(z)=\frac z2\bigl(I_0(z)+I_1(z)\bigr).
\]
Therefore
\[
d(\lambda)=2\lambda e^{-2\lambda}\bigl(I_0(2\lambda)+I_1(2\lambda)\bigr)=2\lambda q_\lambda.
\]
This immediately gives the two means.

To obtain the variances, differentiate an expectation with respect to the common Poisson intensity. For any integrable function \(f(D)\), termwise differentiation of the joint Poisson series gives
\[
\frac d{d\lambda}\mathbb Ef(D)=\mathbb E\!\left[f(D)\left(\frac S\lambda-2\right)\right],
\]
hence
\[
\operatorname{Cov}(S,f(D))=\lambda\frac d{d\lambda}\mathbb Ef(D).
\]
Taking \(f(D)=|D|\) yields
\[
\operatorname{Cov}(S,|D|)=\lambda d'(\lambda).
\]
The standard identities \(I_0'(z)=I_1(z)\) and \(I_1'(z)=I_0(z)-I_1(z)/z\) give the exact simplification
\[
d'(\lambda)=2e^{-2\lambda}I_0(2\lambda)=2r_\lambda.
\]
Also \(\operatorname{Var}(S)=2\lambda\) and, since \(|D|^2=D^2\) with \(\mathbb ED=0\),
\[
\operatorname{Var}(|D|)=\mathbb ED^2-d(\lambda)^2=2\lambda-d(\lambda)^2.
\]
Substitution into the variances of \((S\mp|D|)/2\) gives exactly
\[
\operatorname{Var}(M)=\lambda-\lambda r_\lambda-\lambda^2q_\lambda^2,
\qquad
\operatorname{Var}(A)=\lambda+\lambda r_\lambda-\lambda^2q_\lambda^2.
\]

For the asymptotics, the fixed-order large-argument expansion of \(I_\nu\) gives
\[
q_\lambda=\frac1{\sqrt{\pi\lambda}}\left(1-\frac1{16\lambda}+O(\lambda^{-2})\right),
\qquad
r_\lambda=\frac1{2\sqrt{\pi\lambda}}\left(1+\frac1{16\lambda}+O(\lambda^{-2})\right).
\]
Consequently \(\lambda q_\lambda^2=1/\pi+O(\lambda^{-1})\). Expanding the exact Fano ratios
\[
\frac{1-r_\lambda-\lambda q_\lambda^2}{1-q_\lambda},\qquad
\frac{1+r_\lambda-\lambda q_\lambda^2}{1+q_\lambda}
\]
through order \(\lambda^{-1/2}\) proves the two displayed expansions and the common limit.

## Verification
The accompanying checker evaluates the Bessel formulas and independently truncates the double Poisson sums for several intensities. It verifies the means and variances against the direct distribution to high precision and checks convergence of the two scaled Fano corrections to the predicted constants with opposite signs. These finite calculations are regression checks only; the proof above establishes the identities for every \(\lambda>0\) and the asymptotic limit analytically.

## Relationship to prior work
Gan and Kolaczyk give the Skellam law for the difference of two independent Poisson variables and develop approximation theory for Poisson-like differences. Their paper supplies the exact difference distribution used here but does not analyze minima, maxima, their moments, or Fano factors. Badiella, del Castillo and Puig prove that discrete order statistics preserve ultra log-concavity and deduce that Poisson order statistics are underdispersed; their result is qualitative with respect to the amount of underdispersion. The formulas above refine that statement in the first nontrivial sample size by identifying both exact finite-intensity moments and the universal limiting dispersion ratio.

A 2015 paper by Manca, D'Uggento and Girone studies the Gini mean difference for discrete models including Poisson. That literature can cover the intermediate quantity \(\mathbb E|X-Y|\), but it does not, from the publicly available abstract, cover the covariance identity, the extreme-order variances, or the opposite first-order Fano corrections. Targeted searches for the exact Bessel moment pair, the \(1-1/\pi\) Fano limit, and equivalent Skellam/order-statistic formulations found no statement dominating the present claim.

## Limitations
The originality search cannot exclude an unindexed elementary calculation of these moments. The full text of the 2015 Gini-mean-difference paper was not publicly available during the comparison, so overlap risk remains for the mean formula \(\mathbb E|X-Y|\); the variance identities and Fano asymptotics were compared separately and no covering source was found. The result is specific to two iid Poisson variables and does not classify larger-sample Poisson order statistics.

## References
1. H. L. Gan and E. D. Kolaczyk, *Approximation of the difference of two Poisson-like counts by Skellam*, arXiv:1708.04018, first posted 2017-08-14. Primary AMS 2010 classification 62E17.
2. L. Badiella, J. del Castillo and P. Puig, *Ultra log-concavity of discrete order statistics*, Statistics & Probability Letters 201 (2023), 109900, DOI: 10.1016/j.spl.2023.109900.
3. F. Manca, A. M. D'Uggento and G. Girone, *The mean difference of discrete distribution models* (2015), publicly indexed abstract describing Poisson Gini-mean-difference formulas.
4. NIST Digital Library of Mathematical Functions, §10.40, fixed-order large-argument expansions for modified Bessel functions.
