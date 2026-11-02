# Exact environmental sensitivity from a finite Perron block system

## Finding

Let \(A_1,\ldots,A_h\) be strictly positive \(d\times d\) population projection matrices with a **common positive left Perron vector** \(\ell\), so that
\[
\ell^{\mathsf T}A_k=\rho_k\ell^{\mathsf T},\qquad \rho_k>0.
\]
Let the environment \(E_t\) be a stationary finite-state Markov chain with strictly positive column-stochastic transition matrix \(P\), with the convention \(P_{jk}=\Pr(E_{t+1}=j\mid E_t=k)\). Define \(B_k=A_k/\rho_k\), and form the strictly positive block matrix
\[
\mathcal M_{jk}=P_{jk}B_k,\qquad 1\le j,k\le h.
\]
There is a unique strictly positive block vector \(\mu=(\mu_1,\ldots,\mu_h)\) satisfying
\[
\mu_j=\sum_{k=1}^hP_{jk}B_k\mu_k,\qquad
\sum_k\ell^{\mathsf T}\mu_k=1.
\]
For the stationary environmental probabilities \(\pi\), its block masses are \(\ell^{\mathsf T}\mu_k=\pi_k\). The almost-sure long-run stochastic logarithmic growth exponent is exactly
\[
\gamma=\sum_{k=1}^h\pi_k\log\rho_k.
\]
For **every** collection of real perturbation matrices \(H_k\), the directional derivative under \(A_k(\delta)=A_k+\delta H_k\) is
\[
\boxed{\left.\frac{d\gamma(\delta)}{d\delta}\right|_{\delta=0}
=\sum_{k=1}^h\frac{\ell^{\mathsf T}H_k\mu_k}{\rho_k}.}
\]
In particular, adding the same small amount to entry \((i,j)\) in just the environmental states \(U\) has exact sensitivity
\[
\boxed{b_{ij}(U)=\ell_i\sum_{k\in U}\frac{\mu_{k,j}}{\rho_k}.}
\]
If each targeted entry is instead multiplied by \(1+\delta\), the elasticity is
\[
 e_{ij}(U)=\ell_i\sum_{k\in U}\frac{(A_k)_{ij}\mu_{k,j}}{\rho_k},
 \qquad \sum_{i,j}e_{ij}(U)=\pi_U.
\]
Thus a finite \(hd\)-dimensional Perron eigenvector provides the **exact** sensitivity, rather than a random-product simulation, even for Markov-correlated environments and noncommuting demographic matrices.

For independent and identically distributed (iid) environments, \(P_{jk}=\pi_j\), let \(r>0\), \(\ell^{\mathsf T}r=1\), be the stationary right eigenvector of \(\overline B=\sum_k\pi_k B_k\). Then \(\mu_k=\pi_k r\) and
\[
 b_{ij}(U)=\ell_i r_j\sum_{k\in U}\frac{\pi_k}{\rho_k}.
\]
Consequently the proposed frequency-proportionality relation \(b_{ij}(\{k\})=\pi_k b_{ij}(\{1,\ldots,h\})\) holds **for all states** precisely when all \(\rho_k\) agree. For any specific nonempty subset \(U\), it holds precisely when the \(\pi\)-conditional mean of \(1/\rho_k\) on \(U\) equals its unconditional mean. In both characterizations, \(\pi_U>0\) and every coordinate of \(\ell,r\) is positive.

## Assumptions and scope

All statements hold for any integers \(d,h\ge2\). Matrices \(A_k\) and \(P\) are strictly entrywise positive, and \(P\) is column-stochastic. The vector \(\ell>0\) is common to every left eigenrelation; it is not assumed that the \(A_k\) commute or share a right eigenvector. Perturbations \(H_k\) are arbitrary fixed real matrices, with \(\delta\) restricted to a sufficiently small real neighborhood of zero so that every \(A_k(\delta)\) remains strictly positive. The environmental transition law is held fixed under differentiation. Growth is measured by any norm of the population vector (the finite-dimensional norm choice does not change the exponent), and the initial population vector is nonzero and nonnegative. The stationary Markov law is unique because \(P>0\).

The sensitivities concern **additive perturbations of the entries of the original matrices** \(A_k\), not perturbations constrained to preserve the common-left-vector identity. This distinction is essential: the perturbed matrices need not share any Perron vector. The exact formula is a *first derivative at the specified unperturbed family*, not a formula for arbitrary finite changes.

## Proof

**1. Normalized matrix products and growth.** Normalize \(\ell>0\) arbitrarily and consider the compact positive simplex \(\Sigma=\{x\ge0:\ell^{\mathsf T}x=1\}\). For each environmental state define
\[
F_k^\delta(x)=\frac{(A_k+\delta H_k)x}{\ell^{\mathsf T}(A_k+\delta H_k)x}.
\]
At \(\delta=0\), the common-left-vector hypothesis implies \(F_k^0(x)=B_kx\), and \(\ell^{\mathsf T}B_kx=1\). Because there are finitely many strictly positive matrices, for all sufficiently small \(\delta\) each normalized map sends the nonnegative simplex uniformly into its positive interior and is a contraction in Hilbert's projective metric with one common coefficient strictly less than one. This is the elementary strict-positive-matrix projective-contraction theorem; alternatively its coefficient is bounded via the maximal ratio of pairs of positive entries across the finite family. Applying these contractions to a bi-infinite stationary environmental sequence yields a unique stationary, past-measurable positive state \(x_t^\delta\in\Sigma\), and their uniform contraction implies \(x_t^\delta\to x_t^0\) almost surely as \(\delta\to0\).

The unnormalized population mass satisfies a multiplicative cocycle. The ergodic theorem and norm equivalence give its almost-sure growth exponent as
\[
\gamma(\delta)=\mathbb E\left[\log\left(\ell^{\mathsf T}
  (A_{E_t}+\delta H_{E_t})x_t^\delta\right)\right].
\]
At \(\delta=0\) the quantity inside the logarithm equals \(\rho_{E_t}\), independent of \(x_t^0\); hence \(\gamma(0)=\sum_k\pi_k\log\rho_k\).

**2. Differentiating without differentiating the random state.** Exactly, for each \(\delta\) near zero,
\[
\ell^{\mathsf T}(A_{E_t}+\delta H_{E_t})x_t^\delta
=\rho_{E_t}+\delta\ell^{\mathsf T}H_{E_t}x_t^\delta.
\]
Every \(\ell^{\mathsf T}H_kx\) is uniformly bounded on \(\Sigma\), and all \(\rho_k\) are strictly positive. Taking difference quotients of the logarithms, continuity of \(x_t^\delta\) and dominated convergence therefore yield
\[
\gamma'(0)=\mathbb E\left[
\frac{\ell^{\mathsf T}H_{E_t}x_t^0}{\rho_{E_t}}\right].
\]
No derivative of \(x_t^\delta\) is needed: its contribution vanishes because the zeroth-order multiplier \(\rho_{E_t}\) is independent of the state.

**3. A finite closed system for the stationary population composition.** Define the nonnormalized block moments
\[
\mu_k=\mathbb E[x_t^0\mathbf1_{\{E_t=k\}}].
\]
The unperturbed recursion is \(x_{t+1}^0=B_{E_t}x_t^0\). Conditioning on \(E_t=k\) and using the Markov property gives
\[
\mu_j=\sum_kP_{jk}B_k\mu_k.
\]
Since each \(\ell^{\mathsf T}x_t^0=1\), summing block masses gives \(\sum_k\ell^{\mathsf T}\mu_k=1\). Conversely, \(\mathcal M=(P_{jk}B_k)_{j,k}\) is strictly positive and has left eigenvector \((\ell^{\mathsf T},\ldots,\ell^{\mathsf T})\) for eigenvalue one. Perron–Frobenius uniqueness gives the stated normalized positive solution. Applying \(\ell^{\mathsf T}\) to the block equations yields \(\ell^{\mathsf T}\mu=P(\ell^{\mathsf T}\mu)\), so \(\ell^{\mathsf T}\mu_k=\pi_k\). Substitution into Step 2 proves the directional derivative formula and entry sensitivities.

For the elasticity identity, use \(\ell^{\mathsf T}A_k=\rho_k\ell^{\mathsf T}\):
\[
\sum_{i,j}e_{ij}(U)=\sum_{k\in U}\rho_k^{-1}\ell^{\mathsf T}A_k\mu_k
=\sum_{k\in U}\pi_k.
\]

**4. Iid characterization.** When \(P_{jk}=\pi_j\), the present environmental state is independent of the past-dependent normalized state \(x_t^0\). Therefore \(\mu_k=\pi_k r\), where \(r=\mathbb E[x_t^0]\). Its stationary equation is \(r=\overline B r\), and strict positivity of \(\overline B\) gives a unique positive normalized solution. Thus the stated iid sensitivity formula holds. For any entry, \(\ell_i r_j>0\), and the equation
\[
\ell_i r_j\frac{\pi_k}{\rho_k}
=\pi_k\ell_i r_j\sum_l\frac{\pi_l}{\rho_l}
\]
for every \(k\) is equivalent, since \(\pi_k>0\), to \(1/\rho_k\) being constant across \(k\). The subset result follows by summing over \(U\) and dividing by \(\pi_U\).

**5. Exact noncommuting counterexample and correlation effect.** Let \(\ell=(1,1)^{\mathsf T}\), \(\rho_1=2\), \(\rho_2=4\), and
\[
B_1=\begin{pmatrix}9/10&2/5\\1/10&3/5\end{pmatrix},\quad
B_2=\begin{pmatrix}1/5&4/5\\4/5&1/5\end{pmatrix},\quad
P=\begin{pmatrix}3/4&1/3\\1/4&2/3\end{pmatrix}.
\]
Take \(A_k=\rho_kB_k\). Direct multiplication gives
\[
B_1B_2-B_2B_1=\frac6{25}
\begin{pmatrix}1&1\\-1&-1\end{pmatrix}\ne0.
\]
The unique environment law and block Perron moments are exactly
\[
\pi=(4/7,3/7)^{\mathsf T},\quad
\mu_1=(8/21,4/21)^{\mathsf T},\quad
\mu_2=(5/21,4/21)^{\mathsf T}.
\]
Consequently \(\gamma=(10/7)\log2\), and the environment-specific sensitivities of entry \((1,1)\) are \(4/21\) and \(5/84\), respectively, with common-entry sensitivity \(1/4\). But \(\pi_1/4=1/7\ne4/21\); frequency-proportionality fails. If the environmental process is replaced by iid draws with the **same** \(\pi\), the stationary right composition becomes \(r=(10/17,7/17)^{\mathsf T}\), and the two corresponding sensitivities change to \(20/119\) and \(15/238\). Thus temporal correlation can change intervention sensitivities although it leaves this family's stochastic growth exponent unchanged.

## Verification

The self-contained Python 3 standard-library script `verify.py` reconstructs stationary block equations over exact rational arithmetic, checks the noncommuting example and conditional moments, verifies finite-horizon derivative identities for arbitrary environmental words, and compares the derived stationary derivatives with exact enumerations of Markov environmental sequences. It also performs numerical finite-difference checks based on long Markov trajectories. The finite computations are diagnostic checks; the proof above establishes all dimensions, admissible matrices, and parameter boundaries.

Run `python3 verify.py` from the directory containing this document and the script. Its reported successful execution is separately detailed in `VERIFICATION.md`.

## Relationship to prior work

Caswell (2005) introduced environment-specific stochastic-growth sensitivities and proposed a frequency-proportionality conjecture for iid environments. Caswell (2010) gives general random-product response formulas, evaluated asymptotically. Giaimo (2023), Theorems and Section 4, disproves the conjecture using a small-demographic-variation approximation and comparisons with simulation; Section 5 proves the corresponding total-elasticity identity. The exact identity \(\sum_{i,j}e_{ij}(U)=\pi_U\) here is **previously known**, is included only for consistency, and is not claimed as new.

The presently established finite block-Perron formula uses the additional common-left-reproductive-value hypothesis and supplies exact sensitivities for arbitrary magnitude differences, arbitrary positive Markov transitions, and noncommuting \(A_k\). Unlike the general asymptotic response formula, it requires no long random trajectory. The exact iid necessary-and-sufficient proportionality characterization and explicit correlated-versus-iid comparison follow within this restricted family. No claim is made that the general conjecture's disproof, random-product response formula, or universal elasticity sum is novel.

## Limitations

The common positive left eigenvector and strict positivity hypotheses are strong structural restrictions, not generic properties of age- or stage-structured demographic matrices. Projection matrices with structural zeros, reducible Markov environments, changing environmental transition probabilities, or perturbations of the environmental law are outside the proved assumptions. This analysis concerns derivatives at the common-left-vector family, not finite perturbed growth rates or full nonlinear population dynamics. The priority comparison is limited by inaccessible full text of Caswell (2005) and some related specialized literature; an independently formulated equivalent special-case formula may exist. No independent validation or external priority certification has been performed.

## References

1. S. Giaimo (2023), *On two conjectures about perturbations of the stochastic growth rate*, Australian & New Zealand Journal of Statistics **65**, 1–13. First published 15 February 2023. https://doi.org/10.1111/anzs.12382 ; full open access: https://onlinelibrary.wiley.com/doi/full/10.1111/anzs.12382 .
2. H. Caswell (2005), *Sensitivity analysis of the stochastic growth rate: three extensions*, Australian & New Zealand Journal of Statistics. https://doi.org/10.1111/j.1467-842X.2005.00373.x . Full text was not accessible in this review.
3. H. Caswell (2010), *Life table response experiment analysis of the stochastic growth rate*, Journal of Ecology. https://doi.org/10.1111/j.1365-2745.2009.01627.x ; full text: https://besjournals.onlinelibrary.wiley.com/doi/10.1111/j.1365-2745.2009.01627.x .
4. J. Åberg et al. (2009), *Environment-specific elasticity and sensitivity analysis of the stochastic growth rate*, Ecological Modelling **220**, 605–610. https://ideas.repec.org/a/eee/ecomod/v220y2009i5p605-610.html . Abstract inspected; full text unavailable.
