# The exponential ridge window for a Gaussian-diagonal Hadamard least-squares sketch

## Finding

A Gaussian diagonal placed **before** Hadamard row subsampling produces a striking separation between high-probability behavior and squared-error risk. An explicit one-parameter least-squares instance has infinite unregularized mean-square error for every finite number of sampled rows when sampling is with replacement. Ridge regularization repairs the moments, but the regularization required to control the rare rank-one collisions has an exact exponential transition at scale \(4^{-m}\). The result below gives the finite distribution, its dependence on with- versus without-replacement sampling, and the sharp regularization constant.

**Theorem.** Let \(N\geq2\) be an order admitting a real Hadamard matrix \(H\in\{-1,1\}^{N\times N}\), normalized by \(H^{\mathsf T}H=NI\). Fix distinct columns \(a,b\) and put
\[
 u=(e_a+e_b)/\sqrt2,\qquad v=(e_a-e_b)/\sqrt2.
\]
The original least-squares problem \(\min_{x\in\mathbb R}\|ux-v\|_2^2\) has the unique solution \(x_*=0\). For each integer \(m\geq1\), let \(P\) select \(m\) Hadamard rows uniformly either **with replacement** (any \(m\)) or **without replacement** (\(m\leq N\)). Independently let \(D_\gamma\) be diagonal with independent \(N(0,1)\) entries, and set
\[
 S=m^{-1/2}PH D_\gamma,\quad
 \widehat x_{m,\eta}=\arg\min_{x\in\mathbb R}
 \left(\|Sux-Sv\|_2^2+\frac{\eta}{2}x^2\right),\qquad \eta\geq0.
\]
Almost surely the minimizer is unique even at \(\eta=0\). Denote \(X_m=\widehat x_{m,0}\), and set \(R_m=m^{-1}\sum_{k=1}^mH_{i_k,a}H_{i_k,b}\), where the \(i_k\) are the selected row indices.

**(1) Exact distribution.** Conditional on \(R_m=\rho\), the law of \(|X_m|\) is
\[
 F_\rho(t)=\Pr(|X_m|\leq t\mid R_m=\rho)
 =\frac2\pi\arctan\!\left(\frac{t}{\sqrt{1-(1-\rho^2)t^2}}\right)
\]
for \(0\leq t<(1-\rho^2)^{-1/2}\) when \(|\rho|<1\), and \(F_\rho(t)=1\) beyond that endpoint. For \(|\rho|=1\) the same expression with square root equal to one holds for every \(t\geq0\), giving the standard absolute-Cauchy law. In particular, conditional on \(|\rho|<1\), the signed density is
\[
 f_\rho(x)=\frac{\mathbf{1}_{\{|x|<(1-\rho^2)^{-1/2}\}}}
 {\pi(1+\rho^2x^2)\sqrt{1-(1-\rho^2)x^2}}.
\]
Write \(J_m\) for the number of selected rows with \(H_{i_k,a}H_{i_k,b}=+1\). Then \(R_m=(2J_m-m)/m\), and the full distribution is the finite mixture of these conditional laws with weights
\[
 \Pr(J_m=j)=
 \begin{cases}
 2^{-m}\binom mj,&\text{with replacement},\\[2pt]
 \displaystyle\frac{\binom{N/2}{j}\binom{N/2}{m-j}}{\binom Nm},&\text{without replacement},
 \end{cases}
\]
where binomial coefficients outside their admissible ranges are zero.

**(2) Exact moment and sampling cutoff.** Let \(w_m=\Pr(|R_m|=1)\). Then
\[
 w_m=\begin{cases}
 2^{1-m},&\text{with replacement},\\[2pt]
 \displaystyle\frac{2\binom{N/2}{m}}{\binom Nm},&\text{without replacement and }m\leq N/2,\\[5pt]
 0,&\text{without replacement and }m>N/2.
 \end{cases}
\]
For every real \(p>0\), \(\mathbb E|X_m|^p\) is infinite exactly when \(w_m>0\) and \(p\geq1\). In all other cases it is finite. Thus without-replacement sampling has the **exact threshold** \(m>N/2\) for existence of all positive moments on this instance, while with-replacement sampling retains infinite first absolute moment and infinite squared risk at *every* finite \(m\). For \(m\geq2\), all non-Cauchy mixture components are supported in
\[
 [-B_m,B_m],\qquad B_m=\frac{m}{2\sqrt{m-1}}.
\]
Consequently, for every \(t>B_m\), the unregularized two-sided tail is **exactly**
\[
 \Pr(|X_m|>t)=\frac{2w_m}{\pi}\arctan(1/t).
\]

**(3) Sharp fixed-size ridge blow-up.** For every fixed admissible \(N,m\), \(\mathbb E\widehat x_{m,\eta}^2<\infty\) at each \(\eta>0\). When \(w_m>0\),
\[
 \boxed{\displaystyle
 \mathbb E\widehat x_{m,\eta}^{\,2}
 =\frac{w_m\sqrt\pi}{2\sqrt\eta}+O_{N,m}(1)
 \qquad(\eta\downarrow0).}
\]
When \(w_m=0\), the second moment instead converges to the finite unregularized second moment as \(\eta\downarrow0\).

**(4) Exponential regularization window.** Under sampling with replacement, hold any Hadamard order \(N\geq2\) fixed, let \(m\to\infty\), and choose an arbitrary positive sequence \(\eta_m\to0\). Then
\[
 \boxed{\displaystyle
 \mathbb E\widehat x_{m,\eta_m}^{\,2}
 =\frac12+o(1)+\frac{\sqrt\pi}{2^m\sqrt{\eta_m}}\bigl(1+o(1)\bigr).}
\]
The \(o(1)\) terms in the two summands are independent of how rapidly the sequence \(\eta_m\) approaches zero. In particular, for any constant \(c>0\),
\[
 \eta_m=c\,4^{-m}\quad\Longrightarrow\quad
 \lim_{m\to\infty}\mathbb E\widehat x_{m,\eta_m}^{\,2}
 =\frac12+\sqrt{\frac\pi c}.
\]
If \(4^m\eta_m\to\infty\), the risk tends to \(1/2\); if \(4^m\eta_m\to0\), it diverges to infinity. In contrast, \(X_m\) itself converges almost surely under a natural common coupling to a bounded arcsine variable of second moment \(1/2\), although \(\mathbb E X_m^2=\infty\) for each finite \(m\).

## Assumptions and scope

The data are real and fixed, and the only randomness is independent Gaussian diagonal weighting and the specified row sampling. The Hadamard entries are unnormalized \(\pm1\); the overall sketch includes \(m^{-1/2}\). The ridge penalty is exactly \(\eta x^2/2\), so changing a conventional regularization normalization changes the numerical constants. The Gaussian diagonal is **before** row sampling and Hadamard mixing; it is not the balanced Gaussian-pooled transform introduced in the motivating source. Without-replacement statements require \(1\leq m\leq N\). All expectations are over both row selection and Gaussian weights. No floating-point stability or general-purpose multidimensional regression rate is asserted.

## Proof

**Step 1: exact scalar reduction.** Orthogonality of distinct Hadamard columns makes the original least-squares solution zero, and each of their rowwise products is \(+1\) at exactly \(N/2\) indices. Denote the two relevant Gaussian diagonal entries by \(g,h\). Direct multiplication gives
\[
 2\langle Su,Sv\rangle=g^2-h^2,\qquad
 2\|Su\|_2^2=g^2+h^2+2R_mgh.
\]
Thus for all \(\eta\geq0\), almost surely
\[
 \widehat x_{m,\eta}
 =\frac{g^2-h^2}{g^2+h^2+2R_mgh+\eta}.
 \tag{1}
\]
The denominator at \(\eta=0\) is zero only on a Gaussian null event, including when \(|R_m|=1\).

**Step 2: conditional angular law.** Write \((g,h)=r(\cos\theta,\sin\theta)\); for independent isotropic Gaussians, \(2\theta\) is uniform modulo \(2\pi\), independent of \(r\). Equation (1) at zero ridge becomes
\[
 X_m=\frac{\cos\phi}{1+\rho\sin\phi},\qquad
 \phi\sim\operatorname{Unif}[0,2\pi),
\]
conditional on \(R_m=\rho\). For \(|\rho|<1\), the denominator is positive and the extreme absolute value is \((1-\rho^2)^{-1/2}\), obtained by differentiating the angular ratio. Change of variables over the two inverse branches (or integration of their Jacobians) gives the displayed signed density. Its positive-half integral is
\[
 \frac2\pi\int_0^t\frac{dx}{(1+\rho^2x^2)\sqrt{1-(1-\rho^2)x^2}}
 =\frac2\pi\arctan\left(\frac{t}{\sqrt{1-(1-\rho^2)t^2}}\right).
\]
For \(|\rho|=1\), the orthogonal Gaussian variables \((g+h)/\sqrt2\) and \((g-h)/\sqrt2\) show that \(X_m\) is standard Cauchy, with either ordering. This proves the conditional laws.

**Step 3: mixture and moment boundary.** The row products give independent fair signs under sampling with replacement, and a hypergeometric count with \(N/2\) of each sign without replacement. This proves all finite mixing weights and \(w_m\). On \(0<|R_m|<1\) and \(R_m=0\), the conditional ratio has bounded support; on \(|R_m|=1\), its Cauchy component has finite absolute \(p\)-moment precisely when \(p<1\). For \(m\geq2\), any nonextreme count \(1\leq J_m\leq m-1\) satisfies \(|R_m|\leq1-2/m\), and the angular support bound becomes \(B_m\). This yields the exact final-tail identity.

**Step 4: ridge singularity.** Whenever \(|R_m|<1\), \(|\widehat x_{m,\eta}|\leq|X_m|\) pointwise, and hence its second moment remains bounded as ridge vanishes, for fixed \(m\). On \(|R_m|=1\), let \(U,V\) be independent standard normal variables formed by the orthogonal sums and differences of \(g,h\). Equation (1) becomes \(2UV/(2U^2+\eta)\), up to swapping \(U,V\). Therefore the singular-sector squared risk equals
\[
 Q(\eta)=\mathbb E\frac{U^2}{(U^2+\eta/2)^2}.
\]
With \(U=\sqrt{\eta/2}\,t\), the integral and the identity \(\int_{-\infty}^{\infty}t^2/(1+t^2)^2\,dt=\pi/2\) give
\[
 \lim_{\eta\downarrow0}\sqrt\eta\,Q(\eta)=\frac{\sqrt\pi}{2}.
\]
The error in \(Q(\eta)-\sqrt\pi/(2\sqrt\eta)\) is bounded: after scaling, apply \(1-e^{-z}\leq\min(1,z)\) to the Gaussian factor and split the integral at \(|t|=\eta^{-1/2}\), obtaining an \(O(\sqrt\eta)\) error before multiplying by \(\eta^{-1/2}\). Multiplication by \(w_m\) and addition of the bounded nonextreme contribution proves part (3).

**Step 5: simultaneous limit.** For with-replacement samples, couple all \(R_m\) as prefix averages of one infinite independent fair-sign sequence and keep \(g,h\) fixed. Then \(R_m\to0\) almost surely, so on \(|R_m|\leq1/2\) and with \(\eta_m\to0\), equation (1) tends to \((g^2-h^2)/(g^2+h^2)\). Its squared mean is \(1/2\), by uniform Gaussian angle. The nonextreme squared ratio is bounded by \(1/(1-R_m^2)\). On \(|R_m|\leq1/2\), this is at most \(4/3\); on \(1/2<|R_m|<1\), it is at most \(B_m^2=O(m)\), while Hoeffding's inequality makes that event exponentially rare. Therefore
\[
 \mathbb E\bigl[\widehat x_{m,\eta_m}^2\mathbf1_{\{|R_m|<1\}}\bigr]=\frac12+o(1).
\]
The extreme event has probability \(2^{1-m}\), and its exact contribution is \(2^{1-m}Q(\eta_m)\). Combining this with the expansion from Step 4 gives part (4) and the three regimes. The final almost-sure statement follows from the same coupling; the limiting arcsine law follows from the uniform angle.

## Verification

The standalone standard-library program `VERIFY.py` constructs Hadamard matrices directly, compares the sketched normal equations with equation (1), checks the exact binomial/hypergeometric mixing probabilities using rational arithmetic, compares conditional quantiles with independent angular enumeration, verifies the far-tail reduction, and numerically checks the scaled Gaussian ridge constant. Its finite tests support the algebra but are not a proof of any universal or asymptotic assertion. To reproduce: run `python3 VERIFY.py` from the directory containing this document and the program.

## Relationship to prior work

Song and Zhang (2026), Section 3 and equation (3), introduce the unregularized two-Gaussian Hadamard counterexample, explicitly give the basic ratio (1) at \(\eta=0\), and prove a nonvanishing-probability failure of a proposed Gaussian-diagonal shortcut. That representation and negative result **are prior work, not novel here**. The contribution assessed here is the new ridge-regularized risk calculation, the sharp \(4^{-m}\) simultaneous scaling and constant, and the sampling-without-replacement integrability classification, together with a closed-form conditional distribution useful for quantifying those statements. The original 2017 fast-regression analysis of Price, Song and Woodruff concerns high-probability directionwise guarantees for a different, signed SRHT sketch; Song, Ye, Yin and Zhang (2023) propose nearly-linear-row high-probability bounds. General sketched-pseudoinverse analyses discuss implicit ridge regularization, but do not furnish this two-column rare-collision ridge window. Thus the conclusion is specifically about Gaussian weights placed *before* the Hadamard transform, not about Gaussian-pooling sketches or standard SRHT algorithms.

## Limitations

The exact results concern a deliberately structured one-parameter regression test and do not imply divergence of risk for all inputs. Infinite moments are caused by low-probability singular row-sign patterns even though the scalar normal equation is nonsingular almost surely; numerical conditioning near those patterns is not analyzed. In the simultaneous limit, \(N\) is fixed and sampling is with replacement. The without-replacement all-moment cutoff \(m>N/2\) is particular to two Hadamard columns and is not asserted as a practical general-purpose sketch-size requirement. Any stronger literature equivalence not identified by the comparisons could affect originality.

## References

1. Z. Song and L. Zhang, *Hadamard Flattening and Gaussian Pooling Sketch for Least Squares with Coordinate-wise Guarantee*, arXiv:2608.26552v1 (first public version, 2026-08-27), especially Section 3 and equation (3). https://arxiv.org/abs/2608.26552
2. E. Price, Z. Song, and D. P. Woodruff, *Fast Regression with an \(\ell_\infty\) Guarantee*, arXiv:1705.10723 (2017), especially Sections 1 and 3. https://arxiv.org/abs/1705.10723
3. Z. Song, M. Ye, J. Yin, and L. Zhang, *A Nearly-Optimal Bound for Fast Regression with \(\ell_\infty\) Guarantee*, arXiv:2302.00248v1 (2023). https://arxiv.org/abs/2302.00248
4. *Asymptotics of the Sketched Pseudoinverse*, SIAM Journal on Mathematics of Data Science, DOI:10.1137/22M1530264 (background on sketching and ridge regularization). https://doi.org/10.1137/22M1530264
