# Third-order temporal moments identify heterogeneous patch turnover from aggregate occupancy

## Finding

**Finite-moment identifiability and sharpness theorem.** Fix any integer \(n\ge1\) and sampling interval \(h>0\). Suppose \(n\) independent habitat patches evolve in stationarity, each as a continuous-time occupied/unoccupied Markov chain with strictly positive colonization rate \(\alpha_i\) (empty to occupied) and extinction rate \(\beta_i\) (occupied to empty). Assume their turnover rates \(r_i=\alpha_i+\beta_i\) are pairwise distinct. Only the aggregate number of occupied patches \(N(t)\), not their identities, is observed.

The stationary mean, the \(2n\) autocovariances at lags \(0,h,\ldots,(2n-1)h\), and the \(n\) third centered joint moments at triples \((0,jh,2jh)\), \(0\le j<n\), uniquely determine every pair \((\alpha_i,\beta_i)\), up to permutation of the patches. A constructive exact inversion is given below. The mean and **the entire autocovariance function**, even when known at every nonnegative real lag, do not in general determine these rates as soon as \(n\ge2\). For \(n=1\), the mean and autocovariance suffice. Thus third order is the minimum universally sufficient temporal moment order in this identifiable class for \(n\ge2\).

The result concerns structural identification from exact stationary moments, not inference from a finite noisy trajectory.

## Assumptions and scope

Write \(X_i(t)\in\{0,1\}\) for patch occupancy and \(N(t)=\sum_{i=1}^n X_i(t)\). The independent component processes start in their unique stationary distributions. Put
\[
\pi_i=\frac{\alpha_i}{\alpha_i+\beta_i},\quad
r_i=\alpha_i+\beta_i,\quad
z_i=e^{-r_i h},\quad c_i=\pi_i(1-\pi_i),\quad d_i=c_i(1-2\pi_i).
\]
Every \(\pi_i\) and \(z_i\) is strictly between zero and one. Distinct turnover rates mean that the \(z_i\) are distinct. The observed population mean is \(m=\mathbb E[N(t)]\). Define
\[
C_j=\mathbb E[(N(0)-m)(N(jh)-m)],\quad 0\le j\le2n-1,
\]
\[
T_j=\mathbb E[(N(0)-m)(N(jh)-m)(N(2jh)-m)],\quad0\le j\le n-1.
\]
The case \(j=0\) is allowed: \(C_0\) is the variance and \(T_0\) is the ordinary centered third moment. All expectations refer to the stationary, perfectly observed continuous-time model. No rates are fixed or normalized other than the known time unit \(h\). An unknown common change of the time unit would of course rescale every rate.

## Proof

**Step 1: exact covariance and third-order identities.** For one patch, the Markov transition probabilities give
\[
\mathbb E[X_i(t+s)-\pi_i\mid X_i(t)]=e^{-r_i s}(X_i(t)-\pi_i),\qquad s\ge0.
\]
Consequently \(\operatorname{Cov}(X_i(0),X_i(t))=c_i e^{-r_i t}\). Independence makes all cross-patch centered covariances zero, so
\[
\boxed{C_j=\sum_{i=1}^n c_i z_i^j.}
\]
For a Bernoulli variable \(X\) of mean \(\pi\), the algebraic identity
\[
(X-\pi)^2=\pi(1-\pi)+(1-2\pi)(X-\pi)
\]
holds at both possible values of \(X\). Applying the Markov conditional expectation successively at \(2jh\) and \(jh\), and then using stationarity, gives
\[
\mathbb E[(X_i(0)-\pi_i)(X_i(jh)-\pi_i)(X_i(2jh)-\pi_i)]
=c_i(1-2\pi_i)z_i^{2j}.
\]
In the aggregate centered triple product, independence and zero means kill all terms in which at least one component index appears only once. Thus
\[
\boxed{T_j=\sum_{i=1}^n d_i z_i^{2j}.}
\]
Both identities remain valid when \(j=0\).

**Step 2: the covariance sequence determines decay factors and amplitudes.** Construct two \(n\times n\) Hankel matrices, with indices \(0\le a,b<n\):
\[
H_0=(C_{a+b})_{a,b},\qquad H_1=(C_{a+b+1})_{a,b}.
\]
Let \(V_{ai}=z_i^a\). The preceding identity gives
\[
H_0=V\operatorname{diag}(c_i)V^{\mathsf T},\qquad
H_1=V\operatorname{diag}(c_i z_i)V^{\mathsf T}.
\]
The Vandermonde matrix \(V\) is invertible because the \(z_i\) are pairwise distinct. Every \(c_i>0\), so \(H_0\) is positive definite. Hence the generalized eigenvalues of \((H_1,H_0)\), equivalently the eigenvalues of \(H_0^{-1}H_1\), are precisely the \(n\) positive, distinct numbers \(z_i\). The solution of
\[
(C_0,\ldots,C_{n-1})^{\mathsf T}=V(c_1,\ldots,c_n)^{\mathsf T}
\]
then recovers each positive coefficient \(c_i\) associated with its recovered \(z_i\). No alternative list of \(n\) distinct decays with positive weights can reproduce the \(2n\) covariance observations.

**Step 3: the third-order moments resolve the occupancy-direction ambiguity.** The \(z_i^2\) remain positive and pairwise distinct. Therefore the Vandermonde system
\[
(T_0,\ldots,T_{n-1})^{\mathsf T}
=(z_i^{2j})_{0\le j<n,1\le i\le n}(d_1,\ldots,d_n)^{\mathsf T}
\]
uniquely recovers every \(d_i\). Since \(c_i>0\), reconstruct
\[
\boxed{\pi_i=\frac{1-d_i/c_i}{2},\quad
\alpha_i=-\frac{\pi_i\log z_i}{h},\quad
\beta_i=-\frac{(1-\pi_i)\log z_i}{h}.}
\]
These are exactly the original positive rates, after ordering components by their recovered decay factors. This proves the finite-moment identification assertion.

**Step 4: sharp failure at second order.** With two patches, take the distinct relaxation factors \(z_1=1/2\), \(z_2=1/3\) (equivalently \(r_1=(\log2)/h\), \(r_2=(\log3)/h\)). Compare stationary occupancies \((\pi_1,\pi_2)=(1/4,3/4)\) and \((3/4,1/4)\), with each pair translated to colonization/extinction rates by \(\alpha_i=\pi_i r_i\), \(\beta_i=(1-\pi_i)r_i\). Both models have mean \(m=1\) and
\[
C(t)=\frac3{16}(e^{-r_1t}+e^{-r_2t})\quad\text{for every }t\ge0.
\]
They are genuinely different unordered rate-pair collections, because the distinct \(r_i\) couple to opposite \(\pi_i\) in the two models. Their third centered moments at times \((0,h,2h)\) are respectively
\[
T_1=\frac5{384}\qquad\text{and}\qquad T_1=-\frac5{384}.
\]
The example survives adding any number of identical further independent patches with new distinct turnover rates to both models. Thus mean and full autocovariance are insufficient for every \(n\ge2\). For \(n=1\), the mean gives \(\pi_1\), and \(C_1/C_0=z_1\) gives \(r_1\), so moment order two already suffices. The assertions follow. \(\square\)

## Verification

The attached standalone standard-library script `verify.py` independently constructs finite-state transition probabilities at integer multiples of the sampling interval, enumerates all state triples for two rational two-/three-patch examples, and compares exact rational covariances and third centered moments with the exponential identities. It also builds and solves the covariance Hankel linear system, checks the characteristic roots, and reconstructs occupancy probabilities from third-order data using exact rational arithmetic. It verifies the two-patch ambiguity and the unequal signed third moments. Run `python3 verify.py` and compare its one-line JSON output byte for byte with `certificate.json`. The script provides finite consistency checks, not a substitute for the all-parameter argument in the proof.

## Relationship to prior work

Royle and Kéry (2007) develop state-space dynamic occupancy models for colonization, extinction and heterogeneous sites; Fukaya and Royle (2013) develop a community transition model that explicitly uses point-resolved observations and observation errors. The present idealized inverse problem instead has **only an aggregate occupied-site count**, assumes independent stationary continuous-time patches, and seeks exact structural identification from a specified finite list of temporal moments.

Classical Prony/Hankel exponential inversion supplies the known linear-algebra step that recovers \((z_i,c_i)\) from covariances; that step is not claimed as new. The distinction is the model-specific loss of colonization/extinction orientation in all second-order data and its exact finite third-cumulant resolution. Work on identifiability of superposed renewal point processes concerns event-time superpositions, not this aggregate occupancy count. More general hidden-state identifiability results may entail related statements under additional hypotheses; an equivalence under another terminology has not been ruled out.

## Limitations

The claim fails without the stated independent homogeneous-in-time two-state patch structure; it does not address interactions, common environmental shocks, nonstationary initial conditions, finite observational noise, or irregular unknown time scales. The distinct-turnover assumption is used critically in both Vandermonde inversions. The theorem proves identifiability with exact moments, not numerical stability of Prony inversion when two decay rates are close. No finite-trajectory estimator, variance bound or robustness guarantee is asserted. The lowest order required is a worst-case identification statement, not a claim that every individual instance needs a nonzero third cumulant. No independent review has been performed.

## References

1. Royle, J. A. and Kéry, M., *A Bayesian state-space formulation of dynamic occupancy models*, Ecology 88 (2007), 1813–1823. DOI: 10.1890/06-0669.1. First published 2007-07-01.
2. Fukaya, K. and Royle, J. A., *Markov models for community dynamics allowing for observation error*, Ecology 94 (2013), 2670–2677. DOI: 10.1890/12-1540.1. Full accessible article: https://esajournals.onlinelibrary.wiley.com/doi/10.1890/12-1540.1.
3. O'Cinneide, C. A., *Identifiability in superpositions of renewal processes*, Communications in Statistics: Stochastic Models 7 (1991), 603–614. DOI: 10.1080/15326349108807208. Comparison restricted to accessible abstract.
4. Classical Prony exponential-sum reconstruction; historical method attributed to G. R. de Prony (1795). Used here as prior linear-algebra machinery.
