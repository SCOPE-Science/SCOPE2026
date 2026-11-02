# Rank-one coupled Sylvester forcing with flat-rank solutions and vanishing normalized residual

## Finding
For every integer \(n\ge2\) and real \(0<\tau\le1\), a pair of real coupled generalized Sylvester equations has **two nonzero rank-one right-hand sides**, uniquely determined solutions \(X=I_n\) and \(Y=-I_n\), and matrix coefficients with \(2\)-norm condition numbers at most \(2\). The standard generalized spectral-separation condition holds. Nonetheless neither solution admits a relatively accurate low-rank approximation: all its singular values equal \(1\). Moreover, the normalized residual used for these coupled equations can converge to zero along explicit low-rank trial pairs even while both relative forward errors converge to one.

For \(1\le k<n\), let \(K_k=\operatorname{diag}(\underbrace{1,\ldots,1}_{k},0,\ldots,0)\). For the trial pair \((\widetilde X,\widetilde Y)=(K_k,-K_k)\), the two equation residuals and the maximal normalized relative residual \(\mathcal R\), defined below, obey
\[
\|R_1\|_F=\sqrt2,\qquad R_2=0,\qquad
\mathcal R(K_k,-K_k)=\frac{\sqrt2}{2\sqrt k+2},
\qquad
\frac{\|I_n-K_k\|_F}{\|I_n\|_F}=\sqrt{\frac{n-k}{n}}.
\]
In particular \(n=m^2\) and \(k=m\) give residual tending to \(0\), while both relative forward errors tend to \(1\) as \(m\to\infty\).

## Assumptions and scope
All computations are over the real field and in exact arithmetic. Write the standard basis of \(\mathbb R^n\) as \(e_0,\ldots,e_{n-1}\). Define the cyclic and anticyclic signed permutation matrices \(P,Q\) by
\[
Pe_j=Qe_j=e_{j+1}\quad(0\le j<n-1),\qquad
Pe_{n-1}=e_0,\quad Qe_{n-1}=-e_0.
\]
Let \(E=I_n+\tau e_0e_0^\mathsf{T}\). Take the coefficient and forcing matrices
\[
 A_1=P,\quad A_2=Q,\quad E_1=I_n,\quad E_2=E,
 \qquad F_1=-(P-Q)=-2e_0e_{n-1}^\mathsf{T},
 \quad F_2=E-I_n=\tau e_0e_0^\mathsf{T}.
\]
Each \(F_i\) is nonzero and rank one. Consider the coupled system
\[
 A_1X+YA_2=-F_1,\qquad E_1X+YE_2=-F_2.\tag{1}
\]
Define the residuals for an arbitrary trial pair \((U,V)\) by
\[
 R_1(U,V)=A_1U+VA_2+F_1,\qquad
 R_2(U,V)=E_1U+VE_2+F_2.
\]
The relative residual in the cited motivating scheme is the maximum of the two termwise-normalized Frobenius residuals,
\[
\mathcal R(U,V)=\max_{i=1,2}
 \frac{\|R_i(U,V)\|_F}{\|G_{i1}U\|_F+\|VG_{i2}\|_F+\|F_i\|_F},
\]
where \((G_{11},G_{12})=(A_1,A_2)\) and \((G_{21},G_{22})=(E_1,E_2)\). Denominators are positive for the trial matrices considered here. The spectral separation criterion is
\(\sigma(E_1^{-1}A_1)\cap\sigma(E_2^{-1}A_2)=\varnothing\).

## Proof
**Existence and uniqueness.** Direct multiplication yields \(A_1I_n-I_nA_2=P-Q=-F_1\) and \(E_1I_n-I_nE_2=I_n-E=-F_2\); hence \((I_n,-I_n)\) solves (1). From the homogeneous second equation \(U+VE=0\), obtain \(V=-UE^{-1}\). Inserting this into the first yields \(PU-U(E^{-1}Q)=0\). Since \(P^n=I_n\), the eigenvalues of \(P\) are the \(n\)-th roots of \(1\). The weighted anticyclic shift \(W=E^{-1}Q\) satisfies
\[
 W^n=-\frac1{1+\tau}I_n,
\qquad
\sigma(W)=\left\{r\exp\left(\frac{(2j+1)\pi\mathrm i}n\right):0\le j<n\right\},
\quad r=(1+\tau)^{-1/n}<1.
\]
Thus the two spectra lie on concentric circles of radii \(1\) and \(r<1\) and are disjoint. The standard elementary Sylvester uniqueness argument (diagonalization of \(P\) and \(W\) over \(\mathbb C\), or vectorization) forces \(U=0\), then \(V=0\). This proves unique solvability over \(\mathbb R\).

**Coefficient conditioning and near-resonance.** Both \(P\) and \(Q\) are orthogonal, so their \(2\)-norm condition numbers equal \(1\). The matrix \(E\) has singular values \(1+\tau\) once and \(1\) otherwise; hence \(\kappa_2(E)=1+\tau\le2\). Also \(W=D(rQ)D^{-1}\) for \(D=\operatorname{diag}(1,r^{-1},\ldots,r^{-(n-1)})\); therefore \(\kappa_2(D)=r^{-(n-1)}\le1+\tau\le2\). The exact minimum distance between the two coefficient spectra is
\[
\delta_n=\sqrt{1+r^2-2r\cos(\pi/n)}.
\]
For fixed \(\tau>0\), \(n\delta_n\to\sqrt{\pi^2+[\log(1+\tau)]^2}\). Hence spectral separation is nonzero at each finite \(n\) but **not uniform in dimension**; there is no contradiction with singular-value decay results that demand effective spectral separation.

**Flat singular values and optimal approximation.** Both exact solutions are signed identity matrices, so each has \(n\) singular values equal to \(1\). By the elementary Eckart–Young bound, every matrix of rank at most \(k<n\) approximating either exact solution has squared Frobenius error at least \(n-k\), and spectral-norm error at least \(1\). The diagonal projector \(K_k\) attains the Frobenius bound for \(X\), and \(-K_k\) does so for \(Y\).

**Normalized-residual separation.** Using the definitions of the two shifts,
\[
 PK_k-K_kQ=e_ke_{k-1}^\mathsf{T}+e_0e_{n-1}^\mathsf{T},
\]
so
\[
R_1(K_k,-K_k)
=e_ke_{k-1}^\mathsf{T}-e_0e_{n-1}^\mathsf{T},
\qquad R_2(K_k,-K_k)=K_k-K_kE+(E-I_n)=0.
\]
The two displayed rank-one pieces in \(R_1\) have distinct supports for \(1\le k<n\), hence \(\|R_1\|_F=\sqrt2\). Moreover, orthogonality of \(P,Q\) gives \(\|PK_k\|_F=\|K_kQ\|_F=\sqrt k\), and \(\|F_1\|_F=2\). The stated exact formula for \(\mathcal R\) follows. With \(n=m^2,k=m\), the forward-error ratio tends to one and the residual tends to zero.

## Verification
Run the self-contained Python 3 script `verify_coupled_sylvester.py` in the same directory. It uses only the Python standard library and exact rational arithmetic for all matrix identities and residual-squared comparisons. The recorded execution returned `EXACT_CHECKS_OK 1035` over dimensions \(2\) through \(11\), rational \(\tau\in\{1/8,1/2,1\}\), and all ranks \(1\le k<n\). These finite checks illustrate the theorem; its all-dimensional conclusion is proved above, not inferred from enumeration.

## Relationship to prior work
Zulfiqar's 2026 analysis of coupled generalized Sylvester equations motivates low-rank Krylov projection when the **solution itself** is low rank and uses termwise-normalized equation residuals. The present result is a concrete boundary outside that low-rank-solution hypothesis. It does not claim failure of those algorithms under their published assumptions. Clouâtre, Klippenstein, and Slevinsky (2023) explicitly discuss why low-rank Sylvester forcing alone does not imply solution low rank, including identity-matrix examples; that general observation and the elementary cyclic displacement are prior art, **not** claimed as discoveries. The distinguishable claim here is the simultaneously nonzero rank-one coupled forcing, uniformly conditioned coefficients, disjoint generalized spectra, exact flat solution singular values, and explicit low-rank pairs with vanishing termwise-normalized residual but nearly maximal relative solution error. Beckermann and Townsend's Zolotarev-type decay bounds under stronger effective separation do not yield a uniform low-rank conclusion in this near-resonant family.

## Limitations
The family is deliberately near-resonant: its spectral gap is of order \(1/n\), even though each input matrix has condition number at most \(2\). The result does **not** concern systems with a dimension-independent resolvent separation or guaranteed low-rank solutions. The low-rank trial matrices are explicit candidates; they are not asserted to be actual iterates of any specific Krylov method. Small normalized residual cannot, by itself, certify small forward error in this family. Numerical conditioning of the coupled **operator** is not bounded by the individual coefficient condition numbers. All statements use exact arithmetic and square real systems.

## References
1. U. Zulfiqar, *Numerical Solution of Large-Scale Low-Rank Coupled Generalized Sylvester Equations*, arXiv:2610.30804v1, first public October 22, 2026, https://arxiv.org/abs/2610.30804.
2. R. Clouâtre, C. Klippenstein, R. M. Slevinsky, *Lifting Sylvester Equations: Singular Value Decay for Non-Normal Coefficients*, arXiv:2308.11533, https://arxiv.org/abs/2308.11533.
3. B. Beckermann, A. Townsend, *On the Singular Values of Matrices with Displacement Structure*, arXiv:1609.09494, https://arxiv.org/abs/1609.09494.
