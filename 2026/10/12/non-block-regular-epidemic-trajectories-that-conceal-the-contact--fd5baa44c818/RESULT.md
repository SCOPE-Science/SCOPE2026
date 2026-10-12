# Non-block-regular epidemic trajectories that conceal the contact network

## Finding

**Theorem (failure of block-regular reconstruction criterion, all finite dimensions).** In the deterministic symmetric-weight susceptible--infected--susceptible (SIS) metapopulation model
\[
\dot z_i=(1-z_i)\sum_{j=1}^{n}w_{ij}\pi_j z_j-\gamma_i z_i,
\qquad i=1,\ldots,n,
\]
for every integer \(n\ge2\), there are two distinct, entrywise strictly positive symmetric contact matrices with the **same** strictly positive population fractions, nonnegative recovery rates and pairwise distinct interior initial prevalences that generate **exactly the same nonconstant trajectories for all times**. Both parameter sets are admissible in the sense of the bounded-weight model of Keliger and Horváth [1], and neither is block regular under their Definition 3.2. Thus their proposed implication "not block regular \(\Rightarrow\) contact matrix reconstructible" (Conjecture 3.3) is false, including its asserted two-community case.

An explicit construction, valid for every \(n\ge2\), is
\[
\begin{gathered}
\pi_i=\frac1n,\qquad
k_i=1+\frac{i-1}{n-1},\qquad
z_i(0)=\frac{k_i}{5},\qquad
\gamma_i=\frac3{k_i}-1,\\
W_{ij}=2,\qquad u=(k_2,-k_1,0,\ldots,0)^\mathsf T,\qquad
\widetilde W=W+\tfrac14 uu^\mathsf T.
\end{gathered}
\]
The common solution is
\[
 z_i(t)=k_i\,\frac{e^t}{2+3e^t}\qquad(t\ge0).
\]
Both matrices have entries within \([1/10,4]\), and the solution is genuinely time-varying. With this same fixed initial condition and known demographic data, they remain observationally indistinguishable even under perfect observations over arbitrary time intervals.

**Companion exact two-community observability classification.** For any two-community SIS model with positive initial prevalences, define the weighted contact matrix
\[
 A=W\operatorname{diag}(\pi_1,\pi_2)
  =\begin{pmatrix}a&b\\c&d\end{pmatrix},
 \quad z(0)=(x_0,kx_0),\quad 0<x_0<1,\quad 0<kx_0<1,
\]
and set
\[
\begin{gathered}
 \alpha=a+bk,\quad \beta=c/k+d,\quad
 P=\alpha-\gamma_1-\beta+\gamma_2,\quad
 Q=\alpha-k\beta,\quad \delta=P-Qx_0,\\
 G(T)=\int_0^Tz(t)z(t)^\mathsf T\,dt .
\end{gathered}
\]
Then \(\det G(T)=0\) for one (equivalently every) \(T>0\) if and only if either \(z(0)\) is an equilibrium or \(P=Q=0\). At any nonstationary initial state with \(\delta\ne0\),
\[
\det G(T)=\frac{k^2x_0^4\delta^2}{12}T^4+O(T^5)
\quad (T\downarrow0).
\]
At any nonstationary initial state with \(\delta=0\) and \(Q\ne0\), writing \(v=\dot z_1(0)\ne0\),
\[
\det G(T)=\frac{k^2x_0^4Q^2v^2}{45}T^6+O(T^7)
\quad (T\downarrow0).
\]
Thus all observable nonstationary two-community cases have exactly one of the two stated sharp short-window determinant orders; the nonstationary singular cases are precisely invariant infection-ratio rays. This classification uses the source's Gram matrix, not an alternative loss functional.

## Assumptions and scope

All trajectories are solutions of the continuous-time deterministic SIS equations above, with known strictly positive \(\pi_i\), known \(\gamma_i\ge0\), symmetric \(W\), and \(0<z_i(0)<1\). Contact weights in the explicit construction are strictly positive; no sparsity or zero diagonal is assumed, consistently with [1, eq. (8)]. For this construction take the admissible bounds \(m=1/10\) and \(M=4\). Its \(\pi_i=1/n\) are strictly positive for every \(n\); [1, eq. (7)] requires their sum to be one, not a fixed lower bound on each \(\pi_i\). The companion two-community classification does not require the explicit construction and applies to any weighted contact matrix of the stated model, including the symmetric-weight subclass.

The source defines *block regularity* as the existence of a partition of the \(n\) communities into strictly fewer than \(n\) nonempty blocks such that all communities in the same block have identical initial prevalence and identical recovery rates, together with the prescribed matching blockwise weighted contact sums [1, Definition 3.2]. It defines *reconstructibility at fixed demographic data* through injectivity of the parameter-to-trajectory map on every positive observation interval [1, Definition 2.3]. Both definitions are used literally here.

## Proof

**Construction and admissibility.** The numbers \(k_i\) are pairwise distinct and lie in \([1,2]\). Their mean equals \(3/2\). Consequently
\[
 \sum_{j=1}^n W_{ij}\pi_j k_j
 =2\,\frac1n\sum_{j=1}^n k_j=3.
\]
The vector \(u\) obeys \(u^\mathsf T\operatorname{diag}(\pi)k=(k_2k_1-k_1k_2)/n=0\), so exactly the same identity holds for \(\widetilde W\). The perturbation is nonzero and symmetric. Its only nonzero entries are in the first two rows and columns; since \(k_1=1\), \(1<k_2\le2\), and \(|u_i|\le2\), all entries of \(\widetilde W\) belong to \([3/2,3]\), and all entries of \(W\) equal two. The specified initial conditions lie in \([1/5,2/5]\) and the recovery rates satisfy \(1/2\le\gamma_i\le2\). The same \(m=1/10,M=4\) therefore apply to both matrices for every \(n\ge2\).

On the candidate ray \(z_i=k_i x\), the infection pressure is \(\sum_j w_{ij}\pi_jz_j=3x\), under either contact matrix. Therefore
\[
 \dot z_i=(1-k_ix)3x-(3/k_i-1)k_ix
 =k_ix(1-3x).
\]
The scalar initial-value problem \(\dot x=x(1-3x),\ x(0)=1/5\) has exactly the asserted solution \(x(t)=e^t/(2+3e^t)\); its derivative is initially \(2/25>0\), and \(1/5\le x(t)<1/3\). This is a global solution in the biologically admissible cube since \(k_i x(t)<2/3\). Uniqueness of the polynomial ODE proves that the solution is identical for both contact matrices for every \(t\ge0\).

Because all \(z_i(0)=k_i/5\) are different, no block can contain two indices and hence there is no block-regular partition with fewer than \(n\) blocks, regardless of its contact-sum requirement. Distinct \(W\) and \(\widetilde W\) nevertheless give identical measured trajectories with the same known \(\pi,\gamma,z(0)\). This directly violates injectivity. Moreover the source Gram matrix satisfies
\[
 G(T)=kk^\mathsf T\int_0^T x(t)^2\,dt,
\]
so its rank is one for every positive \(T\). In the simplest case \(n=2\), the matrices, recovery rates and initial prevalences are
\[
 W=\begin{pmatrix}2&2\\2&2\end{pmatrix},\quad
 \widetilde W=\begin{pmatrix}3&3/2\\3/2&9/4\end{pmatrix},\quad
 \pi=(1/2,1/2),\quad\gamma=(2,1/2),\quad z(0)=(1/5,2/5).
\]
This completes the counterfamily.

**Exact two-community classification.** In the notation of the finding, restriction to the ray \(z=(x,kx)\) gives
\[
 \dot z_1/x=\alpha(1-x)-\gamma_1,
 \qquad \dot z_2/(kx)=\beta(1-kx)-\gamma_2.
\]
These normalized velocities agree exactly when \(P-Qx=0\). Since \(z_i(t)>0\) for finite times, the Gram determinant vanishes on an observation interval precisely when the trajectory spans at most one dimension. To see the forward implication rigorously, for any nonzero \(v\) with \(v^\mathsf TG(T)v=0\), continuity gives \(v\cdot z(t)=0\) throughout the interval. Positivity implies that \(z_2(t)=kz_1(t)\) there, with \(k=z_2(0)/z_1(0)\). If this trajectory is not stationary, \(x(t)\) ranges over a nondegenerate interval, so the affine function \(P-Qx(t)\) vanishes on that interval only when \(P=Q=0\). Conversely, \(P=Q=0\) makes the vector field tangent to the ray at every point, hence by uniqueness the trajectory remains on the ray; an initial equilibrium produces a constant trajectory. These give the complete equivalence for all \(T>0\); if a trajectory is not on the ray at any time, its continuous Gram determinant is positive for every positive interval by the same analytic-ODE/uniqueness argument.

For the short-window rates write \(z_0=z(0)\), \(z_1=z'(0)\), \(z_2=z''(0)\). The exact two-dimensional identity
\[
 \det G(T)=\frac12\int_0^T\int_0^T
   \det(z(t),z(s))^2\,dt\,ds
\]
results by expanding the determinant of the Gram matrix. On the initial ray,
\[
 \det(z_0,z_1)=-kx_0^2\delta.
\]
If \(\delta\ne0\), the Taylor expansion \(\det(z(t),z(s))=(s-t)\det(z_0,z_1)+O(T^2)\), uniformly on the square, and \(\frac12\int_0^T\int_0^T(s-t)^2\,dt\,ds=T^4/12\) prove the first asymptotic formula.

If \(\delta=0\), the initial velocity is tangent to the ray, with \(z_1=(v,kv)\). Let \(h(t)=z_2(t)-kz_1(t)\), where here the subscripts index *communities*, not derivatives. Since \(h'(0)=0\), differentiation of the ray-restricted normal component \(F_2(x,kx)-kF_1(x,kx)=-kx(P-Qx)\) along the initially tangent velocity yields \(h''(0)=kx_0Qv\), hence
\[
 \det(z_0,z''(0))=kx_0^2Qv.
\]
For a nonstationary state \(v\ne0\). Taylor expansion now gives
\[
 \det(z(t),z(s))=	frac12(s^2-t^2)\det(z_0,z''(0))+O(T^3).
\]
Using \(\frac18\int_0^T\int_0^T(s^2-t^2)^2\,dt\,ds=T^6/45\) proves the second formula. If also \(Q=0\), then \(P=0\) and the exact invariant-ray singular case applies. The classification and asymptotic orders follow.

## Verification

A standalone standard-library script, `verify.py`, uses exact rational arithmetic. It verifies feasibility, non-block-regular initial data, rank-one contact-matrix perturbations and equality of the polynomial vector fields on the invariant ray for \(n=2,3,4,7,11,25\). It also checks exact first- and second-transverse-jet examples with leading coefficients \(1/7500\) for the \(T^4\) case and \(4/703125\) for the \(T^6\) case. Running `python3 verify.py` prints `VERIFY_OK` after the assertions pass. The code checks finitely many instances; the proof above, not the finite tests, establishes the statements for every \(n\) and all admissible two-community parameters.

## Relationship to prior work

Keliger and Horváth [1, §§2.2 and 3.1] already establish the Gram-matrix reconstruction equivalence and propose block regularity as an equivalent parameter-side obstruction (Definition 3.2 and Conjecture 3.3). They specifically report the two-community direction as settled with proof omitted. We do not claim originality for the general Gram criterion, the rank-deficiency principle or low-dimensional prediction surrogates. The newly specified strict-positive symmetric counterfamily directly contradicts the proposed sufficiency direction *inside its published model class*, including its smallest nontrivial dimension. Its nonstationary, unequal-prevalence realization and the precise two-community ray/short-window classification are the new claims.

Prasse and Van Mieghem [2] previously explain that multiple networks can reproduce SIS trajectories when the dynamics occupy a low-dimensional subspace. That general principle motivates but does not provide the present all-dimension admissible construction or the counterexample to the *specific block-regularity equivalence* subsequently proposed in [1]. Beaufort, Massé, Reboulet and Oudre [3, §4.3] classify symmetry-related nonidentifiability for a different epidemic reaction--diffusion model, in which infections occur locally and network edges govern population diffusion; their permutation-fixed-subspace criterion neither enforces nor implies the present asymmetric-prevalence proportional SIS invariant ray. The exact nonstationary ratio obstruction is a different mechanism from a partition with equal infection curves.

## Limitations

This is a mathematical nonidentifiability construction, not an inference about observed epidemics, real demographic measurements or stochastic individual-based transmission. It assumes the source's strictly positive *weighted* interaction model, which allows positive diagonal weights; it need not apply to simple unweighted loopless networks or to models with uniform known recovery rates. The original Gram equivalence, generic reconstruction observations and prior low-rank-surrogate theory remain valid. The accompanying two-community classification concerns perfect continuous-time observation and the specified Gram determinant; finite sampled/noisy estimators have additional issues. No claim is made that the construction exhausts all nonreconstructible \(n\)-community models for \(n>2\), nor that numerical near-rank-deficiency has the same sharp powers outside two communities.

## References

[1] D. Keliger and I. Horváth, *Why is it easier to predict the epidemic curve than to reconstruct the underlying contact network?* arXiv:2506.00059 (first public version 2025-05-29); *Journal of Mathematical Biology* 92 (2026), article 82, doi:10.1007/s00285-026-02401-6. Open-access full text: https://link.springer.com/article/10.1007/s00285-026-02401-6.

[2] B. Prasse and P. Van Mieghem, *Predicting network dynamics without requiring the knowledge of the interaction graph*, *Proceedings of the National Academy of Sciences* 119 (2022), e2205517119, doi:10.1073/pnas.2205517119; full text https://pmc.ncbi.nlm.nih.gov/articles/PMC9636954/.

[3] L.-B. Beaufort, P.-Y. Massé, A. Reboulet and L. Oudre, *Network Reconstruction Problem for an Epidemic Reaction-Diffusion System*, 2022; author-hosted full manuscript https://www.laurentoudre.fr/publis/ComplexNetworks2022.pdf.
