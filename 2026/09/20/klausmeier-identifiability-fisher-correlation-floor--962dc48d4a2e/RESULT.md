# Exact identifiability dichotomy and Fisher-correlation floor in the non-spatial Klausmeier model

## Statement

Consider the non-spatial Klausmeier system studied in arXiv:2609.18231v1,
\[
\dot w=a-w-wn^2,\qquad
\dot n=wn^2-mn=n(wn-m),
\]
with \(a,m>0\).  The source paper studies joint inference of \((a,m)\) near the fold bifurcation and reports severe practical parameter correlation in the bistable regime.  For exact full-state data, however, the model admits a sharp structural identifiability dichotomy, and its steady vegetated branch has an explicit Fisher-correlation geometry.

### 1. Exact trajectory recovery

Let \((w(t),n(t))\) be an exact solution on \([0,T]\), \(T>0\).
If \(n(0)>0\), positivity of the scalar equation for \(n\) implies \(n(t)>0\) throughout the interval, and
\[
(\log n)'=wn-m.
\]
Integrating the two model equations gives the derivative-free reconstruction formulas
\[
\boxed{
 a=\frac{w(T)-w(0)+\int_0^T w(t)(1+n(t)^2)\,dt}{T},
}
\]
\[
\boxed{
 m=\frac{\int_0^T w(t)n(t)\,dt-\log\!\bigl(n(T)/n(0)\bigr)}{T}.
}
\]
Thus any exact continuous full-state trajectory with positive biomass globally identifies both parameters, independently of whether the parameters lie before or after the fold.

If \(n(0)=0\), then \(n(t)\equiv0\) and
\[
\dot w=a-w.
\]
The mortality parameter \(m\) disappears identically.  Hence the desert invariant set is structurally non-identifying for \(m\).  In particular, multistability by itself is not a structural obstruction here: the obstruction is exactly the invariant zero-biomass state.

### 2. One positive equilibrium already determines both parameters

At every positive equilibrium \((w_*,n_*)\),
\[
wn=m,\qquad a=w(1+n^2).
\]
Therefore
\[
\boxed{m=w_*n_*,\qquad a=w_*(1+n_*^2).}
\]
Define the equilibrium inverse map
\[
\Psi(w,n)=\bigl(w(1+n^2),wn\bigr).
\]
Its Jacobian is
\[
D\Psi=
\begin{pmatrix}
1+n^2&2wn\\
n&w
\end{pmatrix},
\qquad
\boxed{\det D\Psi=w(1-n^2).}
\]
Hence every positive equilibrium away from the fold \(n=1\) is locally structurally identifiable from an exact full-state steady-state observation.  At the fold, the inverse map becomes singular.

For the standard positive branch relation
\[
a=m\left(n+\frac1n\right),\qquad w=\frac mn,
\]
the high-biomass branch has \(n>1\).  Its state Jacobian has
\[
\det J_{\rm dyn}=m(n^2-1),\qquad
\operatorname{tr}J_{\rm dyn}=m-1-n^2,
\]
so for the source paper's \(m=0.45\) this entire high-biomass branch is asymptotically stable.

### 3. Exact equilibrium-only Fisher correlation

The source paper numerically observes a nearly one-dimensional joint \((a,m)\) likelihood/posterior in its stable vegetated regime.  This can be quantified exactly in the ideal steady-state limit.

Assume \(M\) independent full-state observations of one positive equilibrium,
\[
Y_k=(w_*,n_*)+\varepsilon_k,
\qquad
\varepsilon_k\sim N(0,\sigma^2I_2),
\]
with \(M\ge1\).  Let \(S=D_{(a,m)}(w_*,n_*)=(D\Psi)^{-1}\).  The expected local Fisher information is
\[
\mathcal I=\frac{M}{\sigma^2}S^TS,
\]
so the corresponding local Gaussian covariance is
\[
\mathcal C=\mathcal I^{-1}
=\frac{\sigma^2}{M}D\Psi\,D\Psi^T.
\]
Using \(w=m/n\), the common scale \(\sigma^2/M\) factors out and
\[
\mathcal C_{aa}\propto(1+n^2)^2+4m^2,
\]
\[
\mathcal C_{mm}\propto n^2+\frac{m^2}{n^2},
\]
\[
\mathcal C_{am}\propto n(1+n^2)+\frac{2m^2}{n}.
\]
Therefore the local parameter correlation is
\[
\boxed{
\rho(n,m)=
\frac{n^2(1+n^2)+2m^2}
{\sqrt{\bigl((1+n^2)^2+4m^2\bigr)(n^4+m^2)}}.
}
\]
Equivalently,
\[
\boxed{
1-\rho^2=
\frac{m^2(n^2-1)^2}
{\bigl((1+n^2)^2+4m^2\bigr)(n^4+m^2)}.
}
\]
Thus the covariance becomes exactly rank-one correlated at the fold \(n=1\), and the correlation also tends to one as \(n\to\infty\), even though the equilibrium inverse map remains full rank away from the fold.

### 4. Sharp correlation floor on the vegetated branch

Set \(x=n^2>1\).  Differentiating \(1-\rho^2\) gives a numerator proportional to
\[
-2m^2(x-1)(2m^2+x^2+x)(x^2-2x-1-2m^2).
\]
All factors except the last have fixed sign for \(x>1\).  Hence \(1-\rho^2\) has a unique maximum, and \(\rho\) a unique minimum, at
\[
\boxed{x_*=1+\sqrt{2(1+m^2)}}.
\]
At this point
\[
\boxed{
1-\rho_{\min}^2
=\frac{m^2}
{9m^2+12\sqrt2\sqrt{1+m^2}+17}.
}
\]
For the source paper's value \(m=0.45\),
\[
n_*=1.5971243664558757,\qquad
 a_*=1.0004623574887596,
\]
and
\[
\boxed{\rho_{\min}=0.9972914395948188.}
\]
Consequently, in this ideal equilibrium-only Gaussian geometry, every point on the high-biomass positive equilibrium branch at \(m=0.45\) has \((a,m)\) correlation at least \(0.99729144\).  Increasing the number of repeated steady-state observations or decreasing isotropic noise scales the covariance but does not change this correlation coefficient.

The Fisher determinant is also explicit:
\[
\boxed{
\det\mathcal I
=\left(\frac{M}{\sigma^2}\right)^2
\frac{1}{w^2(n^2-1)^2}.
}
\]
Thus a scalar Fisher-size diagnostic can become large near the fold at the same time that the inferred parameter directions become almost perfectly aligned.  This supplies an exact local explanation for why large information magnitude need not imply well-separated individual parameters.

## Equilibrium-indexing correction in arXiv:2609.18231v1

The source paper first derives \(w=m/n\), but its displayed Eqs. (5)--(6) attach the same sign to
\[
w_\pm=\frac{a\pm\Delta}{2},\qquad
n_\pm=\frac{a\pm\Delta}{2m},\qquad
\Delta=\sqrt{a^2-4m^2}.
\]
The same-sign pairs do not satisfy \(wn=m\) except at the fold.  The actual positive equilibria are cross-paired:
\[
\boxed{
\left(\frac{a-\Delta}{2},\frac{a+\Delta}{2m}\right),
\qquad
\left(\frac{a+\Delta}{2},\frac{a-\Delta}{2m}\right).
}
\]
This pairing is standard prior art for the Klausmeier model; for example, Köhnke and Malchow (2017) give equivalent equilibrium formulas and their stability classification.  The correction is therefore not claimed as a new equilibrium theorem.  It is recorded because the sign indexing in the 2026 source is internally inconsistent with its own relation \(w=m/n\), while later algebra in its appendix effectively uses the cross pairing.

## Interpretation relative to the source paper

The result does not contradict the source paper's numerical observation that joint Bayesian inference can be practically poor in the bistable vegetated regime.  Rather, it separates three effects:

- on the exact desert invariant set, \(m\) is structurally absent;
- on any positive exact trajectory or positive equilibrium away from the fold, \((a,m)\) are structurally identifiable from full-state data;
- on the stable vegetated equilibrium branch, the local noisy inverse geometry is nevertheless forced to be extremely correlated for the source value \(m=0.45\).

Accordingly, the source paper's broad statement that reliable joint inference is not possible in its bistable numerical regime should be read as a practical/statistical conclusion for its observation design and noise level, not as a structural non-identifiability theorem caused by bistability itself.

## Verification

`artifacts/verify_identifiability.py` symbolically checks the trajectory identities, the positive-equilibrium inverse Jacobian, the corrected equilibrium pairing, the Fisher covariance and determinant, the factorization locating the unique correlation minimum, and the closed form of the sharp floor.  Its recorded output is in `artifacts/verification.txt`.

## Limitations

The trajectory reconstruction formulas assume exact continuous observations of both \(w\) and \(n\) with positive biomass.  They are identifiability identities, not proposed noise-robust estimators.  The Fisher-correlation formula assumes repeated independent isotropic Gaussian observations of an exact positive equilibrium and is a local/asymptotic covariance statement; finite-time transients, anisotropic or correlated noise, unknown observation operators, priors, and nonlinear finite-sample posterior effects can change practical correlations.  The result does not analyze the spatial Klausmeier PDE or prove any claim about optimal experimental design.  It also does not imply that the source paper's numerical simulations used its displayed same-sign equilibrium indexing internally.

## Originality boundary

Structural versus practical identifiability, Fisher information, the inverse-function criterion, and the classical Klausmeier equilibrium branches are established methods or prior results.  To the best of our knowledge, the contribution here is restricted to the source-specific exact full-state identifiability dichotomy for arXiv:2609.18231v1 and the closed-form equilibrium-only Fisher correlation law with its sharp global correlation floor, which analytically explains the near-collinearity reported in that new study.  Searches also located generalized Klausmeier inverse-problem work, but no prior statement of these exact formulas for this non-spatial two-parameter problem.

## References

1. L. Beer, C. Kuehn, C. Piazzola, *The Role of Bifurcations in Parameter Estimation: A UQ Analysis of the Non-spatial Klausmeier Model*, arXiv:2609.18231v1 (2026). https://arxiv.org/abs/2609.18231v1
2. M. C. Köhnke, H. Malchow, *Impact of Parameter Variability and Environmental Noise on the Klausmeier Model of Vegetation Pattern Formation*, Mathematics 5(4), 69 (2017). https://doi.org/10.3390/math5040069
3. M. P. Cruz de la Cruz, D. A. Santiesteban, L. M. Martín Álvarez, R. Abreu Blaya, J. C. Hernández-Gómez, *On a generalized Klausmeier model*, Mathematical Biosciences and Engineering 20(9), 16447--16470 (2023). https://doi.org/10.3934/mbe.2023734
