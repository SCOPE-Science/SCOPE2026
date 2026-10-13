# Sharp one-mode two-copy fermionic Gaussian de Finetti constant
## Finding
For every integer \(n\ge 2\), consider an even fermionic Gaussian state \(\rho_{A_1A_2}\) with one fermionic mode in each copy. Assume that it is \(n\)-exchangeable under graded fermionic copy permutations, and let \(\rho_A\) be its one-copy marginal. Then
\[
\sup_{\rho_{A_1A_2}}\left\|\rho_{A_1A_2}-\rho_A^{\otimes 2}\right\|_1
=\frac{2}{n}\left(1+\frac{1}{n}\right).
\]
The supremum is attained. Equality holds exactly when the two one-copy covariance sectors of an \(n\)-copy Gaussian extension are opposite pure one-mode covariances. With
\[
J_f=\begin{pmatrix}0&1\\-1&0\end{pmatrix},
\]
this means
\[
\{M_A+(n-1)Y,\,M_A-Y\}=\{J_f,-J_f\}
\]
up to the simultaneous particle-hole sign convention.

The general finite Gaussian de Finetti theorem of Negari et al. gives \(4/n\) after setting one mode and two retained copies. The exact constant above is smaller for every finite \(n\) and is asymptotic to one half of that published upper bound.

## Assumptions and scope
All Gaussian states are even. The Schatten trace norm is denoted by \(\|\cdot\|_1\); no extra factor of \(1/2\) is included. Exchangeability is the graded-copy notion in which a two-copy Gaussian marginal admits an \(n\)-copy extension invariant under the fermionic copy-permutation unitaries.

For one mode, every real antisymmetric covariance matrix is a scalar multiple of \(J_f\). Write
\[
M_A=aJ_f,\qquad Y=yJ_f.
\]
The covariance criterion of Negari et al. says that an \(n\)-copy block-constant extension is admissible exactly when
\[
u:=a+(n-1)y\in[-1,1],\qquad v:=a-y\in[-1,1].
\]
Equivalently,
\[
a=\frac{u+(n-1)v}{n},\qquad y=\frac{u-v}{n}.
\]

## Proof
The two-copy covariance matrix has equal diagonal blocks \(aJ_f\) and equal off-diagonal blocks \(yJ_f\). An orthogonal rotation of the two copy labels diagonalizes the copy-space matrix. Its lift to the four Majorana coordinates has determinant one, so it is implemented by a parity-preserving Gaussian unitary. After this unitary,
\[
\rho_{A_1A_2}\sim \sigma_{a+y}\otimes\sigma_{a-y},
\qquad
\rho_A^{\otimes2}\sim \sigma_a\otimes\sigma_a,
\]
where \(\sigma_t\) is the one-mode Gaussian state with covariance \(tJ_f\). The product state is unchanged by the same copy rotation because its covariance is scalar in copy space.

A one-mode Gaussian state is diagonal in the occupation basis. With the convention
\[
q(t)=\frac{1+t}{2},
\]
its two probabilities are \(q(t)\) and \(1-q(t)\). Put
\[
p=q(a),\qquad h=\frac{y}{2}=\frac{u-v}{2n}.
\]
The four diagonal probabilities of the rotated correlated state are those of independent Bernoulli variables with parameters \(p+h\) and \(p-h\), whereas the product marginal has parameters \(p,p\). Their entrywise differences are
\[
-h^2,\qquad -h^2,\qquad h+h^2,\qquad -h+h^2.
\]
Since \(|u-v|\le2\), one has \(|h|\le 1/n\le1/2\). Therefore the Schatten trace norm is exactly
\[
2|h|+2h^2
=\frac{|u-v|}{n}+\frac{(u-v)^2}{2n^2}.
\]
This expression is strictly increasing in \(|u-v|\) on the permitted interval. Hence
\[
\left\|\rho_{A_1A_2}-\rho_A^{\otimes2}\right\|_1
\le \frac{2}{n}+\frac{2}{n^2},
\]
with equality exactly when \(|u-v|=2\). Because \(u,v\in[-1,1]\), equality is equivalent to \(\{u,v\}=\{-1,1\}\), namely to opposite pure sector covariances. The covariance family in Remark IV.5 of Negari et al. realizes one of the two signs, so the upper bound is attained.

## Verification
The proof is analytic and applies to every integer \(n\ge2\). The accompanying script `artifacts/verify.py` performs exact rational checks of the probability differences, the closed trace-norm formula, the bound, and the equality corners over a deterministic grid for \(2\le n\le64\). These finite checks are corroborative only; the all-\(n\) conclusion is established by the proof above.

The critical source-level premises were checked against the full text of arXiv:2610.01860v1: Proposition IV.3 gives the two-sector admissibility criterion, Lemma IV.4 bounds the common off-diagonal covariance block, Remark IV.5 exhibits the one-mode extremal covariance family, and Theorem IV.2 converts covariance control into the published state trace-norm bound. The mixed-state covariance-to-trace-norm inequality used there is Theorem 1 of arXiv:2409.17953v3.

## Relationship to prior work
Negari et al., arXiv:2610.01860v1, prove
\[
\left\|\rho_{A_1\cdots A_k}-\rho_A^{\otimes k}\right\|_1\le\frac{4m_A(k-1)}{n}
\]
and show that the covariance suppression constant is sharp already for one mode. They do not state a sharp state-level constant for the one-mode two-copy marginal. Their proof uses a general mixed-Gaussian Lipschitz inequality after the covariance estimate; the exact diagonal calculation above resolves the slack for this first nontrivial marginal.

Bittel et al., arXiv:2409.17953v3, prove the general mixed free-fermion perturbation inequality
\[
\|\rho-\sigma\|_1\le\frac12\|\Gamma(\rho)-\Gamma(\sigma)\|_1.
\]
That theorem is the broad conversion tool used by the anchor paper, but it does not optimize the exchangeability-constrained two-copy problem.

Negari and Salek, arXiv:2508.18532v2, study two-sided fermionic Gaussian extendibility and distance to the separable set; their two-mode bounds scale as \(1/\sqrt{k_1k_2}\) and concern a different extension geometry and target set. Burkat, Studziński, and Strelchuk, arXiv:2607.25779v1, study Gaussian-symmetric or Gaussian-invariant replicas and almost-i.i.d. approximants with exponential bounds, again a different symmetry class and approximation target. Krumnow, Zimborás, and Eisert, arXiv:1708.01266v1, give a finite Majorana de Finetti theorem for mode permutations rather than the graded identical-copy Gaussian setting used here.

## Limitations
This result is only for one fermionic mode per copy and the first nontrivial retained marginal \(k=2\). It does not determine the sharp constant for \(k>2\), for multiple modes per copy, for non-Gaussian retained states, or for other notions of fermionic exchangeability. It also does not improve the covariance suppression constant itself, which the anchor paper already shows to be sharp. The literature comparison cannot exclude an independently derived equivalent formula in very recent or differently indexed work.

## References
1. A.-R. Negari, F. Salek, Z. Zimborás, A. Harrow, P. Hayden, and J. Eisert, *Approximation theorems for fermionic Gaussian states*, arXiv:2610.01860v1 (first public 2026-10-01).
2. L. Bittel, A. A. Mele, J. Eisert, and L. Leone, *Optimal trace-distance bounds for free-fermionic states: Testing and improved tomography*, arXiv:2409.17953v3; PRX Quantum 6, 030341 (2025).
3. A.-R. Negari and F. Salek, *Extendibility of Fermionic Gaussian States*, arXiv:2508.18532v2; Phys. Rev. Lett. 137, 080201 (2026).
4. J. Burkat, M. Studziński, and S. Strelchuk, *Exponential de Finetti Theorems for Fermionic Gaussian States*, arXiv:2607.25779v1 (2026).
5. C. Krumnow, Z. Zimborás, and J. Eisert, *A fermionic de Finetti theorem*, arXiv:1708.01266v1; J. Math. Phys. 58, 122204 (2017).
