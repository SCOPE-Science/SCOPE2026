# Two absorption-time moments identify contrast and switching in a confined two-mobility diffusion

## Finding

For a two-state diffusivity-switching Brownian particle in a reflecting–absorbing interval, a prescribed quasi-stationary spatial preparation turns its absorption-time law into an exact two-phase survival mixture. With known interval length and arithmetic-mean diffusivity, its dimensionless mean \(m\) and squared coefficient of variation \(c\) uniquely determine the positive diffusivity contrast and symmetric switching rate, up to interchange of the two mobility labels. **The precise realizability region is**
\[
 m>1,\qquad 1+2(1-m^{-1})^2<c<1+2(1-m^{-1}).
\]
Every pair in this open region is attained exactly once (up to labels). Neither boundary is attained by strictly positive unequal diffusivities and a strictly positive finite switching rate. This is a complete inverse and model-compatibility classification from two scalar first-passage observables.

## Assumptions and scope

Let \(L>0\) and \(\bar D>0\) be known. A particle moves in \([0,L]\), reflects at \(0\), and is absorbed when it first reaches \(L\). Its generator in hidden state \(i\in\{+,-\}\) is \(D_i\partial_{xx}\). Its hidden state \(J_t\) jumps symmetrically between the two states at rate \(q>0\), independently of the spatial Brownian noise. The diffusivities are \(D_\pm=\bar D(1\pm\delta)\), where \(0<\delta<1\) is unknown. The initial hidden state is uniform and independent of the spatial initial condition, which has density
\[
 f(x)=\frac{\pi}{2L}\cos\!\left(\frac{\pi x}{2L}\right),\qquad 0<x<L.
\]
This is the normalized ground-state quasi-stationary density of diffusion with the same reflecting–absorbing boundary conditions at fixed diffusivity. Define the eigenvalue \(\lambda=\pi^2/(4L^2)\), dimensionless switching rate \(s=q/(\lambda\bar D)\), absorption time \(T\), scaled time \(Y=\lambda\bar D T\), mean \(m=\mathbb E[Y]\), and squared coefficient of variation \(c=\operatorname{Var}(Y)/m^2\).

The theorem concerns the exact initial ensemble specified above; it does not assert identifiability from two moments under an arbitrary initial-position law, unknown \(\bar D\), asymmetric switching, or observation noise.

## Proof

**1. Exact reduction to two transient phases.** The density \(f\) is nonnegative, normalized to one, satisfies \(f'(0)=f(L)=0\), and solves \(f''=-\lambda f\). For ordinary reflected Brownian diffusion absorbed at \(L\), the forward killed heat semigroup therefore sends \(f\) to \(e^{-\lambda u}f\) after operational time \(u\). Conditioned on a complete hidden-state trajectory, the operational time equals \(U_t=\int_0^t D_{J_v}\,dv\); scalar diffusivity multiplies one common spatial generator. Thus the physical survival probability is \(\mathbb P(T>t)=\mathbb E[e^{-\lambda U_t}]\).

For row initial distribution \(p=(1/2,1/2)\), the two-state Feynman–Kac formula gives
\[
\mathbb P(Y>y)=p\,e^{-Ky}{\bf1},\qquad
K=\begin{pmatrix}1+s+\delta&-s\\-s&1+s-\delta\end{pmatrix},\qquad {\bf1}=\begin{pmatrix}1\\1\end{pmatrix}.
\]
The determinant \(\det K=1+2s-\delta^2\) is strictly positive, and both eigenvalues are positive. Consequently the first two moments exist and are
\[
 m=pK^{-1}{\bf1}=\frac{1+2s}{1+2s-\delta^2},\qquad
\mathbb E[Y^2]=2pK^{-2}{\bf1}
 =\frac{2[(1+2s)^2+\delta^2]}{(1+2s-\delta^2)^2}.
\]
Subtracting \(m^2\) yields
\[
 c=1+\frac{2\delta^2}{(1+2s)^2}.
\]
In particular \(m>1\) and \(c>1\).

**2. Constructive inverse.** Put \(a=1-m^{-1}\) and \(e=c-1\). The moment identities imply
\[
 a=\frac{\delta^2}{1+2s},\qquad
 e=\frac{2\delta^2}{(1+2s)^2}.
\]
Since \(a,e>0\), division determines \(1+2s=2a/e\). Substitution then determines the contrast and the dimensional switching rate:
\[
 \delta=\frac{\sqrt2\,a}{\sqrt e},\qquad
 q=\lambda\bar D\left(\frac{a}{e}-\frac12\right).
\]
These quantities are single-valued once the convention \(D_+>D_-\) is imposed; without a label convention, swapping \(+\) and \(-\) is the only ambiguity.

**3. Necessary and sufficient exact range.** The positivity condition \(q>0\) is exactly \(e<2a\). The physical positivity of the slower diffusivity, \(\delta<1\), is exactly \(e>2a^2\). The condition \(m>1\) means \(0<a<1\), and the interval \(2a^2<e<2a\) is nonempty for precisely those \(a\). Conversely any \(m,c\) in the displayed region defines positive \(q\) and two positive unequal diffusivities through the inverse above, and substituting into the forward moment identities returns the prescribed data. Thus the conditions are both necessary and sufficient, with uniqueness. At fixed \(m\), approaching the upper boundary drives \(q\downarrow0\), whereas approaching the lower boundary drives \(D_-\downarrow0\). Both are excluded by the strict model assumptions; these limits establish sharpness.

**4. Independent spectral representation.** With \(w=\sqrt{s^2+\delta^2}\), the two decay rates are \(r_\pm=1+s\pm w\) and the exact survival law also equals
\[
 \mathbb P(Y>y)=\frac{1+s/w}{2}e^{-r_-y}
 +\frac{1-s/w}{2}e^{-r_+y}.
\]
All rates and both mixture weights are strictly positive, which independently confirms positivity, finiteness of moments, and their phase-mixture interpretation.

## Verification

Run `python3 verify.py` in the same directory (Python standard library only). The checker verifies the exact two-phase formulas by an independent spectral diagonalization, exercises the forward–inverse reconstruction throughout a reproducible parameter grid, and tests that sampled data in the exact admissibility region reconstruct valid physical parameters. This computational corroboration is finite; the statements for all real parameter values follow from the algebraic proof above, not from enumeration.

## Relationship to prior work

Chen and coauthors (2015) study confinement-aware inverse recovery of interconverting Brownian mobility states from displacement distributions and establish direct physical motivation for unknown mobility states in confined cells. Their published recovery observable is a displacement distribution, not the two absorption-time moments and exact realizability region here. Grebenkov (2019) supplies a broad forward first-passage framework for switching diffusivity through the integrated-diffusivity generating function; its general framework plausibly implies the forward survival representation used in step 1. The result asserted here is the separately proved **global inverse range and uniqueness theorem** under a single principal-mode preparation, not novelty of the forward Feynman–Kac machinery or the two-state diffusion model. A complete full-text priority exclusion of the Grebenkov article could not be made, so historical originality remains subject to that important qualification.

## Limitations

The initial position must have the specified quasi-stationary density, the initial environment must be independent and equally likely in both states, and the arithmetic-mean diffusivity and interval length must be calibrated. No robustness, statistical efficiency, finite-sample error bound, or analogous inverse theorem for arbitrary initial conditions, asymmetric switching, additional mobility states, or non-Markov diffusivity is claimed. The approach of a realizability boundary produces physically singular parameters and may be ill-conditioned for noisy observations. The forward formula is a specialization of known first-passage machinery; no assertion is made that its forward representation is new.

## References

1. T.-Y. Chen, W. Jung, A. G. Santiago, F. Yang, Ł. Krzemiński, and P. Chen, “Quantifying Multistate Cytoplasmic Molecular Diffusion in Bacterial Cells via Inverse Transform of Confined Displacement Distribution,” *J. Phys. Chem. B* **119** (2015), 14451–14459. DOI: 10.1021/acs.jpcb.5b08654. Publisher records first online availability on 2015-11-02.
2. D. S. Grebenkov, “A unifying approach to first-passage time distributions in diffusing diffusivity and switching diffusion models,” *J. Phys. A: Math. Theor.* **52** (2019), 174001. arXiv:1812.07249; DOI: 10.1088/1751-8121/ab0dae. Its first preprint appeared 2018-12-18 (supporting later literature, not the archive anchor).
