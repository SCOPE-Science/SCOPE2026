# Exact mean-square ridge stabilization of rank-one indefinite Nyström

## Finding

**Theorem (complete scalar-core risk frontier for a balanced indefinite pair).** Let \(\lambda>0\), let \(Q\) be any real orthogonal \(2\times2\) matrix, and set
\[
 A=\lambda Q\operatorname{diag}(1,-1)Q^{\mathsf T}.
\]
Draw \(g\sim N(0,I_2)\), let \(u=g/\|g\|_2\), and put \(v=Au\) and \(d=u^{\mathsf T}Au\). For each \(\tau>0\), form the rank-at-most-one *scalar-core Tikhonov Nyström approximation*
\[
 \widehat A_\tau=v\frac{d}{d^2+\tau^2}v^{\mathsf T}.
\]
The expected squared Frobenius error has the exact value
\[
 \mathcal R_\lambda(\tau):=\mathbb E\|A-\widehat A_\tau\|_{\mathrm F}^2
 =\lambda^2\left(\frac{2x}{\sqrt{1+x^2}}+
 \frac{1}{2x(1+x^2)^{3/2}}\right),\qquad x=\tau/\lambda.
\]
Its **unique** minimizer among all positive ridge parameters is
\[
 \tau_*=\lambda/\sqrt2,\qquad
 \mathcal R_\lambda(\tau_*)=\frac{8\sqrt3}{9}\lambda^2.
\]

For comparison, define the hard spectral cutoff of the *same scalar core* by
\[
 \widehat A^{\mathrm{cut}}_\delta
 =v\frac{\mathbf1_{\{|d|\ge\delta\}}}{d}v^{\mathsf T},
 \qquad \delta>0,
\]
where the scalar is set to zero when the cutoff excludes the core. Its unique risk-minimizing threshold is \(\delta_*=\lambda/\sqrt2\), with
\[
 \inf_{\delta>0}\mathbb E\|A-\widehat A^{\mathrm{cut}}_\delta\|_{\mathrm F}^2
 =\left(1+\frac2\pi\right)\lambda^2
 >\frac{8\sqrt3}{9}\lambda^2.
\]
Thus optimally tuned scalar-core ridge has strictly smaller **expected squared Frobenius error** than even the best scalar hard cutoff for this same direction distribution. The gap is approximately \(0.0970191\lambda^2\).

The unregularized scalar-core Nyström approximation \(\widehat A_0=vv^{\mathsf T}/d\), defined almost surely, instead satisfies, for every \(t\ge\lambda\),
\[
 \mathbb P\big(\|A-\widehat A_0\|_{\mathrm F}>t\big)
 =\frac2\pi\arcsin(\lambda/t),
\]
and \(\mathbb E\|A-\widehat A_0\|_{\mathrm F}^{p}<\infty\) exactly for \(0<p<1\). In particular its expected squared error is infinite. The qualitative possibility of unbounded error and an equivalent deterministic two-dimensional witness were already known; they are stated here to motivate, not to claim priority for, the ridge-risk optimization.

Finally, among **all** finite-risk measurable scalar coefficients \(\psi(d)\) in approximants \(v\psi(d)v^{\mathsf T}\), the unique optimal coefficient (up to null sets) is \(\psi_{\mathrm{or}}(d)=d/\lambda^2\), with minimal mean-square error \(3\lambda^2/2\). Hence the optimized ridge is within a factor \(16\sqrt3/27\) of the best scalar coefficient risk on this model. This oracle may use the known spectral scale \(\lambda\); it is a comparison benchmark, not a general-purpose data-driven prescription.

## Assumptions and scope

The ambient space is real and exactly two-dimensional. The indefinite matrix has two eigenvalues of **equal magnitude and opposite sign**. Its orientation is arbitrary, but the eigenvalue magnitude \(\lambda\) is fixed and positive. The Gaussian probe is explicitly normalized to unit length *before* sketching; it is a Haar-uniform unit direction. The ridge parameter \(\tau\) has the same units as a matrix eigenvalue. Both methods use the same single sketched column \(v=Au\) and differ only in how the scalar core \(d=u^{\mathsf T}Au\) is inverted. The expectation concerns the randomness in \(u\), not additive data noise or roundoff. All identities use exact arithmetic. Denominators in the unregularized approximation are nonzero with probability one; setting an arbitrary value on the measure-zero null cone does not change its laws.

The comparison is about **squared Frobenius matrix approximation loss** for this specific signature-balanced model, not about spectral norm, nuclear norm, condition number, or asymptotic error of general large matrices. It does not assert that ridge improves every individual realization: the strict improvement is in expectation at each family's best tuning.

## Proof

**1. Distribution of the core.** Rotational invariance reduces to \(Q=I_2\). Write \(u=(\cos\theta,\sin\theta)^{\mathsf T}\), with \(\theta\) uniform on \([0,2\pi)\). Then
\[
 \|v\|_2^2=\lambda^2,\qquad
 d=\lambda\cos(2\theta),\qquad z:=d/\lambda=\cos(2\theta).
\]
The scalar \(z\) has arcsine density \(f(z)=1/(\pi\sqrt{1-z^2})\) on \((-1,1)\). Consequently \(\mathbb E z^2=1/2\). This also makes clear why the normalization of the Gaussian probe matters for the regularizer.

**2. Pointwise matrix loss.** Since \(A^2=\lambda^2I_2\), \(A^3=\lambda^2A\), and \(v=Au\), for any real scalar \(\psi\) we have
\[
 \begin{split}
 \|A-\psi vv^{\mathsf T}\|_{\mathrm F}^2
 &=\operatorname{tr}(A^2)-2\psi v^{\mathsf T}Av
      +\psi^2\|vv^{\mathsf T}\|_{\mathrm F}^2\\
 &=2\lambda^2-2\psi\lambda^2d+\psi^2\lambda^4.\tag{1}
 \end{split}
\]
Putting \(w=\lambda\psi\) gives the useful completed square
\[
 \lambda^{-2}\|A-\psi vv^{\mathsf T}\|_{\mathrm F}^2
 =2-2wz+w^2=2-z^2+(w-z)^2.\tag{2}
\]
This identity proves that \(w=z\), hence \(\psi(d)=d/\lambda^2\), minimizes the error for every direction individually, with minimum \(\lambda^2(2-z^2)\). The equality coefficient is unique for every direction and therefore almost surely unique in the measurable-scalar class. Averaging gives the oracle risk \(3\lambda^2/2\).

**3. Tikhonov risk integral.** For \(x=\tau/\lambda>0\), its normalized coefficient is \(w=z/(z^2+x^2)\). The arcsine identity
\[
 J(x)=\mathbb E\frac1{z^2+x^2}
 =\frac2\pi\int_0^{\pi/2}\frac{d\theta}{\cos^2\theta+x^2}
 =\frac1{x\sqrt{1+x^2}}
\]
follows from the substitution \(t=\tan\theta\). Differentiation under the integral is justified for each \(x>0\). Hence
\[
 \mathbb E\frac{z^2}{z^2+x^2}
 =1-x^2J(x)=1-\frac{x}{\sqrt{1+x^2}},
\]
and
\[
 \begin{split}
 \mathbb E\frac{z^2}{(z^2+x^2)^2}
 &=J(x)+\frac x2J'(x)
 =\frac1{2x(1+x^2)^{3/2}}.
 \end{split}
\]
Insert these expectations into \((1)\), using \(\psi(d)=\lambda^{-1}z/(z^2+x^2)\), to obtain the stated formula for \(\mathcal R_\lambda(\tau)\).

Set \(F(x)=\mathcal R_\lambda(\lambda x)/\lambda^2\). Direct differentiation yields
\[
 F'(x)=\frac{(2x^2-1)(2x^2+1)}{2x^2(1+x^2)^{5/2}}.
\]
The denominator and second numerator factor are positive for every \(x>0\). Thus \(F\) decreases strictly up to \(x=1/\sqrt2\) and increases strictly thereafter. Its limits are \(+\infty\) as \(x\downarrow0\) and \(2\) as \(x\to\infty\). Substitution proves the unique optimum and its value.

**4. Hard cutoff and its optimality.** For a realized \(z\), the cutoff rule returns the plain inverse when \(|z|\ge c\), where \(c=\delta/\lambda\), and the zero matrix otherwise. By \((1)\), the corresponding normalized loss is \(z^{-2}\) upon retention and \(2\) upon rejection. For \(0<c\le1\), the arcsine density gives
\[
 H(c):=\lambda^{-2}\mathbb E\|A-\widehat A^{\mathrm{cut}}_{\lambda c}\|_{\mathrm F}^2
 =\frac4\pi\arcsin c+\frac2\pi\frac{\sqrt{1-c^2}}c.
\]
Its derivative on \((0,1)\) is
\[
 H'(c)=\frac{2(2c^2-1)}{\pi c^2\sqrt{1-c^2}}.
\]
It follows that the unique minimum occurs at \(c=1/\sqrt2\), with value \(H(c)=1+2/\pi\). For \(c\ge1\), the approximation vanishes almost surely, giving loss \(2\lambda^2\). Strict comparison with ridge can be proved without decimals from the elementary inequalities \(\pi<22/7\) and \(\sqrt3<7/4\):
\[
 1+\frac2\pi>\frac{18}{11}>\frac{14}{9}>\frac{8\sqrt3}{9}.
\]
(The middle inequality follows by cross multiplication.)

**5. Unregularized heavy tail and moments.** Setting \(\psi=1/d\) in \((1)\) produces the identity
\[
 \|A-\widehat A_0\|_{\mathrm F}=\lambda/|z|
\]
almost surely. Since \(\mathbb P(|z|<s)=2\arcsin(s)/\pi\) for \(0\le s\le1\), the exact survival function follows. The arcsine density is bounded above and below by positive constants near \(z=0\); thus the integral of \(|z|^{-p}\) is finite exactly when \(p<1\). This confirms the stated moment boundary. The basic deterministic blow-up mechanism here is the same as the published indefinite Nyström counterexample, and is not independently claimed as new.

## Verification

The standalone script `verify.py` reconstructs the symbolic risk identity, its critical derivatives and optimal constants, the hard-cutoff derivative, and the completed-square identity. It also checks a rational \(2\times2\) example by direct matrix arithmetic, independently integrates the original angle-dependent squared matrix error for twelve positive ridge and matrix-scale pairs, and compares hard-cutoff angle quadrature with its analytic formula at four thresholds. Run `python -m pip install -r requirements.txt` if SymPy is missing, then `python verify.py`. The script contains deterministic checks; the theorem's continuum statements and moment divergence are proved above, not inferred from finite numerical tests.

## Relationship to prior work

Park and Nakatsukasa [1] explicitly identify the potential unbounded error of indefinite Nyström approximations, give a deterministic \(2\times2\) example equivalent under orthogonal conjugation to the unregularized witness here, and develop an oversampled rank-truncated core method with nuclear-norm guarantees. The present quantitative contribution is **not** discovery of indefinite-core singularity; it is the exact mean-square risk curve, uniquely optimal parameter and strict comparison of scalar-core *ridge* with the best scalar-core *hard cutoff* under a normalized random direction.

Cai, Nagy and Xi [2] study deterministic landmark selection for indefinite kernel matrices, rather than this one-vector Gaussian core shrinkage law. Bucci, Nakatsukasa and Park [3] analyze numerical stability of pseudoinverse implementations for mainly positive-semidefinite column-selection Nyström approximations; their core truncation addresses roundoff rather than the distributional squared-risk optimization here. Chen, Nakatsukasa, Narendran and Park [4] propose a **different** two-sided sketched least-squares choice of the Nyström core with oversampling. Only its public abstract was accessible for this comparison, so an overlapping special-case statement in its complete text has not been ruled out. General literature on distributions of ratios of quadratic forms [5] can already supply the underlying ratio-density machinery, and is not excluded from covering the elementary tail calculation. These comparisons do not amount to independent publication-priority certification.

## Limitations

This is an exact two-dimensional, equal-magnitude opposite-sign, isotropic normalized-direction **benchmark**. It proves neither that \(\tau=\lambda/\sqrt2\) is optimal for arbitrary indefinite matrices nor that ridge uniformly outperforms hard truncation per sample or in other losses. The oracle coefficient assumes knowledge of \(\lambda\). At fixed \(\lambda\), an even more general estimator outside the sketched one-column class need not obey the scalar-oracle bound; the globally optimal rank-one truncated SVD of \(A\) has squared Frobenius error \(\lambda^2\). No claims are made about roundoff stability, unnormalized Gaussian sketches, oversampling, adaptively selected sketches, or probabilistic confidence guarantees beyond the displayed distribution. A specialized exact risk analysis under another name could precede this derivation, particularly in the less-accessible current literature; independent validation and priority review remain outstanding.

## References

[1] T. Park and Y. Nakatsukasa, *Randomized low-rank approximation for symmetric indefinite matrices*, arXiv:2212.01127 (first posted 2022-12-02), https://arxiv.org/abs/2212.01127. See introduction (indefinite counterexample), Section 2.2 (truncated core), Section 3 (error guarantees), and Section 4 (numerical experiments).

[2] D. Cai, J. Nagy and Y. Xi, *Fast deterministic approximation of symmetric indefinite kernel matrices with high dimensional datasets*, SIAM Journal on Matrix Analysis and Applications 43 (2022), https://doi.org/10.1137/21M1424627.

[3] A. Bucci, Y. Nakatsukasa and T. Park, *Numerical stability of the Nyström method*, arXiv:2511.15583 (2025), https://arxiv.org/abs/2511.15583. See Sections 1–3 (column sampling, truncated pseudoinverse and positive-semidefinite assumptions).

[4] Y. Chen, Y. Nakatsukasa, A. Narendran and T. Park, *Nyström method for symmetric indefinite matrices*, arXiv:2608.20531 (2026), https://arxiv.org/abs/2608.20531. Only accessible abstract used for the comparison.

[5] H. P. Mulholland, *On singularities of sampling distributions, in particular for ratios of quadratic forms*, Biometrika (1970), cited as general classical ratio-distribution background.
