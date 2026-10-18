# A sharp temporal mode exchange in fourth-order correlations of a switching harmonic Brownian gas

## Finding
Let \(N\geq2\) noninteracting particles obey
\[
 dX_j(t)=-(k+hS_t)X_j(t)\,dt+\sqrt{2D}\,dW_j(t),\qquad j=1,\ldots,N,
\]
where \(k>h>0\), \(D>0\), the \(W_j\) are mutually independent two-sided Brownian motions, and the independent stationary symmetric Markov chain \(S_t\in\{-1,1\}\) changes sign at rate \(r>0\). All expectations below refer to the unique joint stationary law. For distinct particles \(i\ne j\), define the time-resolved connected fourth-order observable
\[
 C(t)=\operatorname{Cov}\bigl(X_i(t)^2,X_j(0)^2\bigr),\qquad t\in\mathbb R.
\]
Put
\[
 A=k(k+r)-h^2,\qquad B=2(k^2-h^2)+kr,\qquad
 g=2(k^2-h^2)+3kr+r^2,
\]
all strictly positive. Set
\[
 C_0=\frac{D^2h^2g}{BA^2},\qquad
 C_2=-\frac{4D^2h^2r(2k+r)}{BA},\qquad
 C_3=\frac{8D^2h^2r[2(k^2+h^2)+3kr+r^2]}{BA}.
\]
Then \(C\) is even, \(C(0)=C_0>0\), \(C'(0)=0\), \(C''(0)=C_2<0\), and its positive-lag third derivative satisfies \(C'''(0^+)=C_3>0\). In particular, the symmetric-time correlation has a genuine nonanalytic cubic cusp:
\[
 C(t)=C_0+\tfrac12 C_2t^2+\tfrac16 C_3|t|^3+O(t^4),\qquad t\to0.
\]
For \(\Re z>0\), its exact Laplace transform on nonnegative time is
\[
 \widehat C(z)=\frac{C_0\{z^2+4(k+r)z+4(k^2+3kr+r^2-h^2)\}+C_2}{(z+2r)\{z^2+(4k+2r)z+4(k^2+kr-h^2)\}}.
\]
Let \(\lambda_-=2k+r-\sqrt{r^2+4h^2}\), \(\lambda_+=2k+r+\sqrt{r^2+4h^2}\), and \(r_*=k-h^2/k\). The slowest nonvanishing relaxation undergoes a *sharp mode exchange*:
\[
 \begin{array}{ll}
 0<r<r_*:&C(t)\sim\displaystyle\frac{D^2h^2}{A(k^2-h^2-kr)}e^{-2rt},\\[2mm]
 r=r_*:&C(t)\sim\displaystyle\frac{D^2h^2k}{k^4-h^4}\,t\,e^{-2rt},\\[2mm]
 r>r_*:&C(t)\sim a_-e^{-\lambda_-t},\quad a_->0.
 \end{array}
\]
The explicit positive amplitude in the last line is
\[
 a_-=\frac{2D^2h^2r[\lambda_+g-2(2k+r)A]}{BA^2(2r-\lambda_-)(\lambda_+-\lambda_-)}.
\]
Thus the crossover has a nonzero double-pole amplitude, rather than a cancellation. Finally, the experimentally definable short-lag ratio
\[
 J=-\frac{C'''(0^+)}{C''(0^+)}=2(r+k)+\frac{4h^2}{r+2k}
\]
is strictly increasing in \(r>0\). If the two trap stiffnesses \(k+h\) and \(k-h\) are known, the switching rate is uniquely reconstructed without knowing \(D\):
\[
 r=\frac{J+2k+\sqrt{(J+2k)^2-32h^2}}4-2k.
\]
All statements concern the full continuum of admissible positive parameters and all distinct particle pairs, not a finite parameter sample.

## Assumptions and scope
The trap is confining in both environmental states: \(k>h>0\). Environmental switches are stationary, symmetric and memoryless, with rate \(r>0\) *per state*. Independent Brownian noises have diffusivity \(D>0\); the environment is shared and Brownian noises are not. The observable is a cross-particle covariance of squared positions at a stationary time lag. It is not the ordinary position cross-covariance, which is zero for distinct particles. The expansion is about \(t=0\) with the even stationary extension.

## Proof
**Stationary conditional-variance reduction.** Given the entire switching trajectory, the stationary particle coordinates are independent centered Gaussians with the same variance \(V_t\), which solves the bounded, continuous, piecewise deterministic equation
\[
 \dot V_t=f_{S_t}(V_t),\qquad f_s(v)=2D-2(k+hs)v.
\]
The strictly positive stiffness implies a unique stationary solution obtained by integrating from time \(-\infty\), with \(D/(k+h)\le V_t\le D/(k-h)\). Conditional independence gives \(C(t)=\operatorname{Cov}(V_t,V_0)\) for \(t\ge0\). Exchangeability of particle labels and stationarity make \(C\) even.

**Moments.** With \(Q=\left(\begin{smallmatrix}-r&r\\r&-r\end{smallmatrix}\right)\), \(K=\operatorname{diag}(k+h,k-h)\), and \(m_n=(\mathbb E[V^n\mathbf1_{S=+1}],\mathbb E[V^n\mathbf1_{S=-1}])^{\mathsf T}\), stationarity gives \(m_0=(1/2,1/2)^{\mathsf T}\) and
\[
 (2nK-Q^{\mathsf T})m_n=2nD m_{n-1},\qquad n=1,2.
\]
Solving these invertible systems yields
\[
 \mathbb EV=\frac{D(k+r)}A,\qquad
 \mathbb EV^2=\frac{D^2[2(k^2+h^2)+3kr+r^2]}{BA},
\]
and \(\operatorname{Var}(V)=C_0\) after subtraction.

**Independent lag dynamics and rational transform.** Starting from environment state \(s\) and conditional variance \(v\), the backward expectation \(\mathbb E[V_t\mid V_0=v,S_0=s]\) is affine, \(a_s(t)v+b_s(t)\). The column vectors satisfy
\[
 a'=(Q-2K)a,\quad a(0)=(1,1)^{\mathsf T},\qquad
 b'=Qb+2Da,\quad b(0)=0.
\]
Writing \(a\) and \(b\) as matrix exponentials, multiplying by the stationary \(m_2\) and \(m_1\), and subtracting \((\mathbb EV)^2\) gives the displayed rational transform. Its only possible nonzero relaxation exponents are \(2r\) and \(\lambda_\pm\), with repeated poles interpreted by continuity.

**Cusp without hidden differentiability assumptions.** Let \(\mathcal L\) be the generator of \((V,S)\). Since \(V\) remains continuous at switches, the generator product rule has no jump correction when one factor is \(V\). Stationarity yields \(\mathbb E[Vf_S(V)]=0\), hence \(C'(0^+)=0\), and applying stationarity to \(V f_S(V)\) yields \(C''(0^+)=-\mathbb E[f_S(V)^2]\). Applying stationarity to \(f_S(V)^2\), now including its jump carré-du-champ term, yields
\[
 C'''(0^+)=\tfrac12\mathbb E\bigl[r(f_{-S}(V)-f_S(V))^2\bigr]
 =8rh^2\mathbb E V^2.
\]
Substituting the two stationary moments gives \(C_2,C_3\). Analyticity at strictly positive lag follows from the finite-dimensional linear ODE. Evenness then produces the stated \(|t|^3\) singularity.

**Mode exchange and positivity of the leading residues.** The denominator factors as \((z+2r)(z+\lambda_-)(z+\lambda_+)\). The eigenvalue ordering changes exactly at \(2r=\lambda_-\), equivalent to \(r=r_*\). The numerator at \(z=-2r\) equals \(4D^2h^2/A>0\); for \(r<r_*\) the residue is the first displayed positive amplitude. At the collision \(r=r_*\) the second-order pole has coefficient \(D^2h^2k/(k^4-h^4)>0\), proving the critical \(t e^{-2rt}\) law. For \(r>r_*\) the \(-\lambda_-\) residue is \(a_-\). Its denominator is positive, while its numerator is positive because \(\lambda_+>2k+r\) and \(g-2A=r(k+r)>0\). No slower mode has zero coefficient.

**Exact inverse.** Division of \(-C_3\) by \(C_2\) gives \(J\) as displayed. The derivative \(dJ/dr=2-4h^2/(r+2k)^2>0\) since \(h<k\). Solving its quadratic for \(r+2k>2k\) gives the specified plus-root inversion. The estimator identity itself is mathematical; no sampling-distribution or stability claim is made.

## Verification
Run `python verify.py` with Python, SymPy, NumPy and SciPy. The script independently obtains stationary conditional moments from two-state generator equations, constructs the finite-time affine semigroup, and checks the exact Laplace identity, derivatives, residues, repeated-pole coefficient and inverse ratio using symbolic identities. Numerical matrix exponentials at multiple rational and decimal parameter samples corroborate the finite-lag representation; they are not used to prove the all-parameter results.

## Relationship to prior work
Biroli, Kulkarni, Majumdar and Schehr (arXiv:2312.02570, publicly posted 2023-12-05), including their supplementary material, derived the stationary joint Gaussian variance mixture and the *equal-time* pairwise squared-position covariance for this switching-trap model. Those equal-time structural facts are prior work, not claimed here. Their 2025 experimental preprint (arXiv:2508.07199) compares static collective observables and studies ordinary two-time linear position cross-correlations, which vanish in the ideal noninteracting model; it does not give the delayed squared-position spectral threshold or cubic cusp. Behme, Di Tella and Sideris (arXiv:2207.11093, publicly posted 2022-07-22), Theorems 4.4–4.5, provide general moment/autocovariance machinery for Markov-modulated generalized Ornstein–Uhlenbeck processes. Consequently, the unclassified finite-lag covariance can also be obtained by specializing that general framework. The evaluated sharp non-cancellation threshold, repeated-pole amplitude and diffusion-free short-lag inverse formula are the specific claims assessed here, not a claim to originate the Markov-modulated covariance method.

## Limitations
The result applies only to independent particles in a common *symmetric two-state* switching harmonic trap, with positive stiffnesses. An asymmetric switching clock, hydrodynamic coupling, nonlinear confinement or inferred stiffness parameters is outside scope. The short-lag formula assumes access to exact derivatives of an ideal stationary fourth-order correlation; practical finite-sample inference can be ill-conditioned and is not analyzed. Broad Markov-modulated covariance theory already supplies general representations, so priority for a sufficiently close previously evaluated specialization remains a residual risk.

## References
1. M. Biroli, M. Kulkarni, S. N. Majumdar and G. Schehr, *Dynamically emergent correlations between particles in a switching harmonic trap*, arXiv:2312.02570 (2023-12-05), https://arxiv.org/abs/2312.02570; full paper and Supplement, especially Eqs. (12)–(14), (S26), (S69)–(S73).
2. A. Behme, P. Di Tella and A. Sideris, *On moments of integrals with respect to Markov additive processes and of Markov modulated generalized Ornstein–Uhlenbeck processes*, arXiv:2207.11093 (first posted 2022-07-22), https://arxiv.org/abs/2207.11093, especially Theorems 4.4–4.5 and 4.8.
3. M. Biroli, S. Ciliberto, M. Kulkarni, S. N. Majumdar, A. Petrosyan and G. Schehr, *Experimental evidence for strong emergent correlations between particles in a switching trap*, arXiv:2508.07199 (first posted 2025-08-10), https://arxiv.org/abs/2508.07199; Supplement, two-time position cross-correlation discussion.
