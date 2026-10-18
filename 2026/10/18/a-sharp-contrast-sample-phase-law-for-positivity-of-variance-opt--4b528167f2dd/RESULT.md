# A sharp contrast–sample phase law for positivity of variance-optimal Bernoulli Galerkin control variates

## Finding

An entrywise variance-optimal control variate for a symmetric Galerkin matrix can reduce its Frobenius mean-square error while destroying positive definiteness. For the four-row, two-column leverage-uniform model defined below, the exact loss-of-positivity probability is a binomial tail, with a sharp coefficient-contrast threshold of \(3\). When the coefficient contrast \(\kappa\) grows at the same order as the square root of the number \(\nu\) of independent sketches, this failure probability has a nontrivial Gaussian transition. The inverse-fusion matrix \(2Y_B+\theta\bar Y\) has an exact all-samples positivity threshold \(\theta>(\kappa-3)/2\); the natural variance-ratio choice of \(\theta\) does not meet it for sufficiently large contrast.

Here and below, positive definite means strictly positive definite. The event of failure includes singular matrices.

## Assumptions and scope

Fix an integer \(\nu\ge1\) and positive real numbers \(h>\ell>0\), with contrast \(\kappa=h/\ell>1\). Define
\[
 U=\frac12\begin{pmatrix}1&1\\-1&-1\\1&-1\\-1&1\end{pmatrix},\qquad
 P=\operatorname{diag}(h,h,\ell,\ell),\qquad T=I_4.
\]
The two columns of \(U\) are orthonormal; all four row leverage scores equal \(1/2\). For each \(1\le j\le\nu\), independently sample four fair Bernoulli variables \(\gamma_{ij}\), put \(S_j=\operatorname{diag}(\sqrt{2}\gamma_{1j},\ldots,\sqrt{2}\gamma_{4j})\), and form the coupled Bernoulli sketches
\[
 \bar Y=\frac1\nu\sum_{j=1}^\nu U^{\mathsf T}S_jPS_jU,
 \qquad \bar T=\frac1\nu\sum_{j=1}^\nu U^{\mathsf T}S_jTS_jU.
\]
The deterministic targets are \(Y=U^{\mathsf T}PU\) and \(U^{\mathsf T}TU=I_2\). For each entry \((a,b)\), set the *population-optimal* scalar control weight
\[
 B_{ab}=\frac{\operatorname{Cov}(\bar Y_{ab},\bar T_{ab})}
 {\operatorname{Var}(\bar T_{ab})},
 \qquad (a,b)\in\{1,2\}^2,
\]
and define the symmetric entrywise corrected estimator \(Y_B=\bar Y-B\circ(\bar T-I_2)\), where \(\circ\) denotes the Hadamard product. All four denominators above are positive. These are oracle covariance weights, not estimated regression coefficients.

Write \(v_\pm=(1,\pm1)^{\mathsf T}/\sqrt2\), \(E_\pm=v_\pm v_\pm^{\mathsf T}\), and let \(K_+\) and \(K_-\) denote the total selections of rows \(\{1,2\}\) and \(\{3,4\}\), respectively, across all \(\nu\) sketches. They are independent \(\operatorname{Bin}(2\nu,1/2)\) variables.

## Proof

**Exact simultaneous eigenvalues.** Since the squared product of any two entries within the same row of \(U\) is \(1/16\), independent Bernoulli sampling gives
\[
 B_{ab}=\frac{h+h+\ell+\ell}{4}=\beta:=\frac{h+\ell}{2}
 \quad\text{for every }a,b.
\]
The two rows in each sign pair have outer products \(E_+/2\) or \(E_-/2\). Consequently,
\[
 \begin{aligned}
 Y&=hE_++\ell E_-,\\
 \bar Y&=\frac{hK_+}{\nu}E_++\frac{\ell K_-}{\nu}E_-,\\
 Y_B&=\left(\beta+\frac{h-\ell}{2}\frac{K_+}{\nu}\right)E_+
     +\left(\beta-\frac{h-\ell}{2}\frac{K_-}{\nu}\right)E_-.
 \end{aligned}
\]
Both estimators are unbiased. The plus eigenvalue of \(Y_B\) is always positive. Its minus eigenvalue is nonpositive precisely when
\[
 K_-\ge\nu\frac{\kappa+1}{\kappa-1}.
\]
In particular, \(Y_B\) is strictly positive definite for *every* sketch realization if and only if \(1<\kappa<3\). At \(\kappa=3\) the all-selected minus block gives a zero eigenvalue, and above \(3\) it gives a negative one.

**Exact probability law and nonsingular-original conditioning.** Define
\[
 q_\nu(\kappa)=4^{-\nu}\sum_{k=0}^{2\nu}\binom{2\nu}{k}
 \mathbf 1\!\left\{k\ge\nu\frac{\kappa+1}{\kappa-1}\right\}.
\]
The above eigendecomposition proves \(\Pr(Y_B\not\succ0)=q_\nu(\kappa)\). Moreover, \(\bar Y\succ0\) is exactly the event \(K_+>0,K_->0\), with probability \((1-4^{-\nu})^2\). Because a nonpositive minus eigenvalue requires \(K_->0\), independence gives
\[
 \Pr(Y_B\not\succ0,\ \bar Y\succ0)
 =(1-4^{-\nu})q_\nu(\kappa),\qquad
 \Pr(Y_B\not\succ0\mid\bar Y\succ0)
 =\frac{q_\nu(\kappa)}{1-4^{-\nu}}.
\]
At \(\nu=1\) and \(\kappa>3\), \(q_1(\kappa)=1/4\): a corrected sketch is indefinite with probability \(1/4\), and the probability of an indefinite corrected sketch *and* positive-definite uncorrected sketch is \(3/16\) (conditional failure probability \(1/3\)).

**Sharp fusion threshold.** For any \(\theta>0\), define \(F_\theta=2Y_B+\theta\bar Y\). Its plus eigenvalue is strictly positive. Its minus eigenvalue, divided by \(\ell\), is
\[
 (\kappa+1)+\bigl[\theta-(\kappa-1)\bigr]\frac{K_-}{\nu}.
\]
Taking the minimum over \(K_-\in\{0,\ldots,2\nu\}\) proves the exact equivalence
\[
 F_\theta\succ0\text{ for every sketch realization}
 \quad\Longleftrightarrow\quad \theta>\frac{\kappa-3}{2}.
\]
For each fixed \(\theta\), the unconditional failure probability is the exact binomial tail
\[
 r_\nu(\kappa,\theta)=4^{-\nu}\sum_{k=0}^{2\nu}\binom{2\nu}{k}
 \mathbf1\!\left\{(\kappa+1)+[\theta-(\kappa-1)]k/\nu\le0\right\}.
\]
Here the event \(F_\theta\not\succ0\) includes singularity; if \(\kappa\le1+\theta\), the sum is empty. The joint probability of fusion failure and \(\bar Y\succ0\) is \((1-4^{-\nu})r_\nu(\kappa,\theta)\). In particular, for \(\nu=1\) and \(\kappa\ge3+2\theta\), it is exactly \(3/16\). On realizations with \(F_\theta\succ0\), the formal inverse fusion \((2+\theta)F_\theta^{-1}\) is positive definite. This algebra does *not* make a Stein-loss expression that separately requires \(Y_B\succ0\) meaningful when \(Y_B\) is indefinite.

**Variance reduction and a bounded ridge rule.** The independent binomial variances \(\operatorname{Var}(K_\pm/\nu)=1/(2\nu)\) give
\[
 V_0:=\mathbb E\|\bar Y-Y\|_F^2=\frac{h^2+\ell^2}{2\nu},\qquad
 V_B:=\mathbb E\|Y_B-Y\|_F^2=\frac{(h-\ell)^2}{4\nu}<\frac{V_0}{2}.
\]
Consider the explicitly defined variance-ratio rule \(\theta_{\rm var}=2\sqrt{V_B/V_0}\). It equals
\[
 \theta_{\rm var}=\frac{\sqrt2(\kappa-1)}{\sqrt{\kappa^2+1}}<\sqrt2,
\]
whereas unconditional fused positivity requires a parameter exceeding \((\kappa-3)/2\). The two are equal exactly at one \(\kappa_0>3\), characterized by
\[
 (\kappa_0-3)^2(\kappa_0^2+1)=8(\kappa_0-1)^2,
 \qquad \kappa_0=5.249140538129574\ldots .
\]
Uniqueness follows because \((\kappa-3)/2-\theta_{\rm var}\) is strictly increasing on \(\kappa\ge3\): the derivative of the first term is \(1/2\), while the derivative of the second is \(\sqrt2(\kappa+1)/(\kappa^2+1)^{3/2}<1/2\) in that range. For \(\kappa\ge\kappa_0\), this ridge rule fails to guarantee positive-definite fusion; at \(\nu=1\) the joint failure probability with \(\bar Y\succ0\) equals \(3/16\).

**Contrast versus number of sketches.** For any contrast sequence \(\kappa_\nu>1\), the exact tail law and the binomial central limit theorem imply
\[
 \Pr(Y_B\not\succ0)\longrightarrow
 \begin{cases}
 0,&\kappa_\nu/\sqrt\nu\to0,\\
 1-\Phi(2\sqrt2/c),&\kappa_\nu/\sqrt\nu\to c\in(0,\infty),\\
 1/2,&\kappa_\nu/\sqrt\nu\to\infty,
 \end{cases}
\]
where \(\Phi\) is the standard Gaussian distribution function. Indeed, the threshold is \(\nu+2\nu/(\kappa_\nu-1)\), while the binomial standard deviation is \(\sqrt{\nu/2}\); the first case follows also from a binomial concentration inequality. Conditioning on \(\bar Y\succ0\) does not alter any of these limits. For each fixed \(\kappa>3\), the separate large-deviation exponent is
\[
 -\lim_{\nu\to\infty}\frac1\nu\log q_\nu(\kappa)
 =2D\!\left(\frac{\kappa+1}{2(\kappa-1)}\bigg\|\frac12\right),
\]
with binary relative entropy \(D(p\|q)=p\log(p/q)+(1-p)\log((1-p)/(1-q))\).

## Verification

The companion file `verify.py` uses exact rational arithmetic and independently assembles every Bernoulli sketch outcome in five finite parameter configurations. It compares exact spectra, conditional and unconditional failure probabilities, the optimal control weights, and Frobenius variance formulas. Further numerical calculations check the central-limit profile at two large finite sketch counts. Running `python3 verify.py` completed 18,761 assertions/checks successfully. The finite tests do not replace the analytical proof of the all-\(\nu\) or asymptotic statements.

## Relationship to prior work

Polydorides, Noori, Vandierendonck, and Woods (2025) introduced parameter-oblivious Bernoulli sketching with entrywise control variates. Their equations (13)–(18) give the underlying sketch and variance-optimal weight formulas, and their Section III.A explicitly **warns** that the correction can damage positive definiteness, recommending damping. This qualitative warning and the general optimal-weight rule are prior work and are not claimed here. The present result supplies an exact four-row *spectral and probabilistic* phase classification, a nonvanishing contrast–sample transition, and the sharp ridge threshold of the indicated forward/inverse fusion combination.

Polydorides and collaborators (2026) further motivate low-variance Galerkin sketching and regularized inverse fusion. Their public abstract and an independently prepared mathematical summary were accessible, but the full preprint was not accessible during comparison. Accordingly no assertion is made that the new formulas contradict any guarantee in that work. Choi, Lim, Roy, and Park (2016) address positivity restoration for a different class of covariance estimators; those generic repairs do not provide the present Bernoulli Galerkin binomial law.

## Limitations

This is a sharp theorem for a deliberately transparent real \(4\times2\) orthonormal-column design with two coefficient levels and fair independent row selection. It does not establish a general necessary and sufficient threshold for arbitrary finite-element bases, sampling probabilities, row contrasts, or dimensions. The control weights are exact population quantities; empirical weight estimation, threshold-based weight suppression, post-correction damping, and clipping are different procedures. The matrix \(F_\theta\) is a specified algebraic combination; if the separate corrected matrix is not positive definite, a Stein loss formulated only on positive-definite inputs may remain undefined regardless of the fused matrix's sign. None of the statements concerns floating-point behavior or a downstream finite-element solution error. The strongest bibliographic risk is uninspected material in the 2026 motivating preprint.

## References

1. N. Polydorides, H. Noori, H. Vandierendonck, R. Woods, *Randomised sketching of parametric linear systems*, IEEE Statistical Signal Processing Workshop (2025), DOI: 10.1109/SSP64130.2025.11073388. Open accepted manuscript: https://www.pure.ed.ac.uk/ws/files/516680657/IEEE_ssp_5_pager-19.pdf. Particularly Section III.A, equations (13)–(18) and discussion of positivity.
2. N. Polydorides, Y. Wu, H. Noori, H. Vandierendonck, R. Woods, *Low-Variance Randomised Numerical Linear Algebra for Finite Element Simulation*, arXiv:2606.08817v1, first public June 7, 2026. https://arxiv.org/abs/2606.08817. Full text not inspected; method description cross-checked against https://www.themoonlight.io/en/review/low-variance-randomised-numerical-linear-algebra-for-finite-element-simulation.
3. Y.-G. Choi, J. Lim, A. Roy, J. Park, *Fixed support positive-definite modification of covariance matrix estimators via linear shrinkage*, arXiv:1606.03814 (2016). https://arxiv.org/abs/1606.03814.
