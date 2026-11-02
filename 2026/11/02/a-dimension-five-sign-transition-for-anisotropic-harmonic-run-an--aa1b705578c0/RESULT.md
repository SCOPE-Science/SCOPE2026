# A dimension-five sign transition for anisotropic harmonic run-and-tumble energies

## Finding

Consider a stationary run-and-tumble particle in dimension \(d\ge2\), with constant propulsion speed \(v>0\), independently and uniformly redrawn orientations on \(S^{d-1}\) at Poisson rate \(\gamma>0\), and diagonal harmonic relaxation. For distinct axes \(i\ne j\), write their relaxation rates as \(a,b>0\). Independent thermal Brownian noises of arbitrary strengths may be present. Define \(s=a+b\), \(p=ab\) and

\[
\begin{aligned}
P_{d,a,b}(\gamma)={}&2(d-4)\gamma^4+(7d-34)s\gamma^3\\
&+\bigl[(6d-54)s^2+(8d+4)p\bigr]\gamma^2\\
&+\bigl(12dsp-36s^3\bigr)\gamma-4s^2(2s^2+p),\\
Q_{a,b}(\gamma)={}&(\gamma+a)(\gamma+2a)(\gamma+b)(\gamma+2b)\\
&\quad\cdot s(\gamma+s)(\gamma+a+2b)(\gamma+2a+b).
\end{aligned}
\]

**Theorem.** The unique stationary law satisfies the exact mixed energy-covariance identity

\[
\boxed{\operatorname{Cov}(X_i^2,X_j^2)=\frac{2v^4P_{d,a,b}(\gamma)}{d^2(d+2)Q_{a,b}(\gamma)}.}
\]

This covariance does not depend on the independent translational thermal diffusivities. For \(2\le d\le4\), it is strictly negative at every finite positive tumble rate. For every integer \(d\ge5\) and any positive pair \(a,b\), there is **exactly one** positive root \(\gamma_*(a,b,d)\): the covariance is negative below it, zero at it and positive above it. Moreover the sharp anisotropy bound is

\[
\boxed{\gamma_*(a,b,d)\ge\frac{3(a+b)}{d-4},}
\]

with equality if and only if \(a=b\). Thus unequal harmonic stiffnesses strictly delay the sign reversal at fixed sum of relaxation rates. For an isotropic pair, \(a=b=\mu\), the root is exactly \(\gamma_*=6\mu/(d-4)\); this isotropic specialization is also recoverable from existing isotropic stationary-moment theory and is not separately claimed as novel. The new classification holds for **arbitrary unequal** positive trap strengths, including all degrees of anisotropy.

As a concrete asymmetric example, for \(d=5\), \(a=1\), \(b=2\), the unique positive root is between \(9.32548\) and \(9.32549\), whereas the equal-stiffness lower bound is \(9\). The slow-tumbling boundary and fast-tumbling leading coefficient are, respectively,

\[
\lim_{\gamma\downarrow0}\operatorname{Cov}(X_i^2,X_j^2)
=-\frac{2v^4}{d^2(d+2)a^2b^2},
\]
\[
\operatorname{Cov}(X_i^2,X_j^2)
=\frac{4v^4(d-4)}{d^2(d+2)(a+b)\gamma^3}+O(\gamma^{-4})
\quad(d\ne4),
\]

while for \(d=4\) it is \(-v^4/(8\gamma^4)+O(\gamma^{-5})\). The fourth dimension therefore has an additional cancellation in the fast-tumbling asymptotic.

## Assumptions and scope

Let \(U_t\in S^{d-1}\) remain constant between the jumps of a rate-\(\gamma\) Poisson clock, with each jump replacing \(U_t\) by an independent uniform direction. Let \(B_1,\ldots,B_d\) be mutually independent standard Brownian motions, independent of \(U\). For fixed positive \(\mu_k\) and nonnegative \(D_k\), the model is

\[
dX_k(t)=\bigl(-\mu_kX_k(t)+vU_k(t)\bigr)dt+\sqrt{2D_k}\,dB_k(t),\qquad k=1,\ldots,d.
\]

The result concerns the stationary **equal-time covariance of the squared positions in two different principal axes**, not the covariance of the positions themselves. All parameters are finite and fixed. Positive diagonal drift ensures existence and uniqueness of the invariant law and all its polynomial moments. No assumption of a reversible orientation process beyond independent isotropic redraws is needed.

## Proof

**1. Stationary construction and elimination of thermal noise.** Use a two-sided stationary Poisson clock and Brownian motions. The unique stationary solution is the convergent causal convolution

\[
X_k(t)=v\int_{-\infty}^t e^{-\mu_k(t-r)}U_k(r)\,dr
+\sqrt{2D_k}\int_{-\infty}^t e^{-\mu_k(t-r)}\,dB_k(r).
\]

The active terms are bounded in absolute value by \(v/\mu_k\), and the thermal terms are independent centered Gaussians across axes. Conditional on the active history, the squared thermal-shifted coordinates have independent conditional second moments equal to active squared coordinate plus \(D_k/\mu_k\). The constants disappear from cross-covariance, proving exact thermal-diffusivity independence.

**2. Shared-clock decomposition.** Walk backward from the observation time. Its current age and successive earlier Poisson gaps \(T_0,T_1,\ldots\) are independent \(\operatorname{Exp}(\gamma)\) variables. Put \(S_k=T_0+\cdots+T_{k-1}\), with \(S_0=0\), and

\[
w_{c,k}=e^{-cS_k}\frac{1-e^{-cT_k}}{c},\qquad
Z_c=\sum_{k\ge0}w_{c,k}^2,\qquad
W=\sum_{k\ge0}w_{a,k}^2w_{b,k}^2.
\]

The active coordinate along axis \(i\), whose relaxation rate is \(c=\mu_i\), is \(v\sum_{k\ge0}w_{c,k}U_{k,i}\), where the orientations indexed by \(k\) are mutually independent uniform sphere vectors, but different coordinates within one such vector are dependent. For distinct axes, the exact sphere moments are

\[
\mathbb E U_{k,i}^2=\frac1d,\qquad
\mathbb E[U_{k,i}^2U_{k,j}^2]=\frac1{d(d+2)},\qquad
\mathbb E[U_{k,i}U_{k,j}]=0.
\]

Expanding fourth moments conditional on the gaps and then taking total covariance yields

\[
\operatorname{Cov}(X_i^2,X_j^2)
=\frac{v^4}{d^2}\left[\operatorname{Cov}(Z_a,Z_b)-\frac{2}{d+2}\mathbb EW\right].\tag{1}
\]

The first term is the *positive shared-clock contribution*, while the second is the *negative fixed-length-orientation contribution*. Their competition, rather than ordinary two-point position covariance, creates the dimension transition.

**3. Closed renewal moments.** Write \(A_c(t)=c^{-2}(1-e^{-ct})^2\) and \(L(q)=\gamma/(\gamma+q)\). Conditioning on the first backward gap \(T\sim\operatorname{Exp}(\gamma)\) and shifting the rest of the stationary Poisson sequence gives, in joint distribution,

\[
Z_c=A_c(T)+e^{-2cT}Z_c',\qquad
W=A_a(T)A_b(T)+e^{-2(a+b)T}W',
\]

where primed quantities come from a common independent copy of the remaining gaps. Therefore

\[
M_c:=\mathbb EZ_c=\frac{\mathbb EA_c(T)}{1-L(2c)}
=\frac1{c(\gamma+c)},
\]

and, with \(H=\mathbb E[A_a(T)A_b(T)]\) and \(J_{c,h}=\mathbb E[A_c(T)e^{-2hT}]\),

\[
\begin{aligned}
\mathbb EW&=\frac{H}{1-L(2a+2b)},\\
\mathbb E[Z_aZ_b]&=
\frac{H+J_{a,b}M_b+J_{b,a}M_a}{1-L(2a+2b)}.
\end{aligned}
\]

Here each expectation is an explicit finite combination of \(L(q)\):

\[
\begin{aligned}
J_{c,h}&=c^{-2}[L(2h)-2L(c+2h)+L(2c+2h)],\\
H&=(a^2b^2)^{-1}\sum_{r=0}^2\sum_{s=0}^2
\binom2r\binom2s(-1)^{r+s}L(ra+sb).
\end{aligned}
\]

In particular, direct cancellation gives the independent closed identity

\[
\boxed{\operatorname{Cov}(Z_a,Z_b)=
\frac{2\gamma(2\gamma+3a+3b)}{(\gamma+a)(\gamma+b)(a+b)
(\gamma+a+b)(\gamma+a+2b)(\gamma+2a+b)}>0.}\tag{2}
\]

Substitute these identities into (1), expand the finite nine-term sum for \(H\), combine positive denominators, and collect powers of \(\gamma\). The result is exactly the displayed rational covariance formula with numerator \(2v^4P_{d,a,b}\) and denominator \(d^2(d+2)Q_{a,b}\). The accompanying independent exact-rational checker evaluates both derivations without any approximate algebra.

**4. Complete sign classification.** Every factor in \(Q_{a,b}(\gamma)\) is positive. Because \(0<p\le s^2/4\), for \(2\le d\le4\) the leading coefficient of \(P\) is nonpositive, and its other coefficients are strictly negative: the coefficient of \(\gamma^2\) is at most \((8d-53)s^2<0\), and that of \(\gamma\) is at most \(3(d-12)s^3<0\). This proves strict negativity.

For \(d\ge5\), the coefficients of \(\gamma^4\) and \(\gamma^3\) are strictly positive and the constant coefficient is strictly negative. If \(5\le d\le8\), the linear coefficient is strictly negative; the quadratic coefficient can have either sign. If \(d\ge9\), the quadratic coefficient is strictly positive; the linear coefficient can have either sign. Consequently the ordered coefficients of \(P\), with zeros omitted, have exactly one sign change. Descartes' rule of signs, together with \(P(0)<0\) and \(P(\gamma)\to+\infty\), proves exactly one positive root and the strict sign ordering on either side.

**5. Sharp anisotropy penalty.** Fix \(s=a+b\) and define \(\gamma_0=3s/(d-4)\). In the equal-stiffness case \(p=s^2/4\), direct substitution into the isotropic specialization gives \(P(\gamma_0)=0\). At fixed \(s\), the polynomial is affine in \(p\), with coefficient

\[
\frac{\partial P}{\partial p}=(8d+4)\gamma^2+12ds\gamma-4s^2.
\]

This coefficient is strictly positive at \(\gamma_0\), since \(12ds\gamma_0>36s^2\). Thus for unequal rates, \(p<s^2/4\) gives \(P(\gamma_0)<0\). The unique positive root must strictly exceed \(\gamma_0\). Equality occurs only when \(p=s^2/4\), equivalently \(a=b\). Finally, the stated small- and large-tumble limits follow from the constant and leading nonzero coefficients and the positive denominator, completing the proof.

## Verification

The standalone standard-library program `check.py` performs **2,731 exact-rational assertions**. It independently evaluates the stationary mixed moment by (i) the above shared-Poisson-gap renewal calculation and (ii) a direct nine-moment Markov-generator closure, and matches both against the polynomial formula. It also checks symmetry under exchanging axes, the dimension-four sign boundary, the exact isotropic critical rate, the anisotropy lower bound, and the frozen-orientation limit for explicitly enumerated and seeded rational parameters. Run `python3 check.py` without additional dependencies. These finite checks do not prove the universal statements; the proof above does.

## Relationship to prior work

Guéneau, Majumdar and Schehr (2026) obtain the full stationary law and arbitrary-coordinate moments for the **isotropic** harmonic trap, including a Gaussian thermal convolution. Its already-known isotropic moments imply the equal-stiffness slice of the present calculation. The present theorem instead concerns **two independently selectable principal stiffnesses**, a parameter region not determined by rotational invariance, and proves a global anisotropic sign transition and sharp anisotropy penalty. The arbitrary-dimensional isotropic moment framework is not claimed as new.

Sun, Ye and Podgornik (2025) give a programmable moment recursion for a different finite-tumble-time process with scalar harmonic confinement. Sun, Ye and Chen (2026) derive conditional run/tumble distributions in one-dimensional harmonic confinement. Neither cited work supplies the anisotropic cross-axis covariance phase diagram above. Loewe, Kozhukhov and Shendruk (2024) study anisotropic *turning rules* without the same diagonally anisotropic confining-force model. General polynomial-generator and moment-recursion methods are established tools; the contribution here is the sharp parameter-dependent sign classification, not a new general moment-solving algorithm.

## Limitations

The formula assumes independent uniform full orientation redraws and diagonal positive harmonic stiffness in orthogonal axes; it does not address correlated Brownian driving, nonuniform tumbles, rotational diffusion between tumbles, off-diagonal confinement, nonlinear traps, interacting particles, or finite-duration tumble states. The result identifies a stationary squared-coordinate covariance, not a full stationary joint density or a time-dependent mixing theorem. The isotropic slice has stronger pre-existing moment coverage. Broad tensor-valued moment recursions not located in the literature could potentially subsume the anisotropic formulas; this is a publication-priority risk and is not resolved merely by unsuccessful searches.

## References

1. M. Guéneau, S. N. Majumdar and G. Schehr, *Exact Stationary State of a \(d\)-dimensional Run-and-Tumble Particle in a Harmonic Potential*, arXiv:2602.08436, first submitted 9 February 2026. https://arxiv.org/abs/2602.08436
2. A. Sun, F. Ye and J. Z. Y. Chen, *Run-and-tumble particles in a harmonic external field: constructing the solution of the Fokker-Planck equation from the equations of motion*, arXiv:2610.24961, first submitted 18 October 2026. https://arxiv.org/abs/2610.24961
3. A. Sun, F. Ye and R. Podgornik, *Exact moments for a run-and-tumble particle with a finite tumble time in a harmonic trap*, arXiv:2409.00578, first submitted 2024, later revised 2025. https://arxiv.org/abs/2409.00578
4. B. Loewe, T. Kozhukhov and T. N. Shendruk, *Anisotropic run-and-tumble-turn dynamics*, Soft Matter **20** (2024), 1133–1150. https://doi.org/10.1039/D3SM00589E
