# Endpoint-tail fingerprints in the rare-jump sub-gamma transition

## Finding

Fix \(a>0\), \(b>0\), \(C>0\), and \(\beta>0\). Let \(J\) be a nonnegative random variable supported on \([0,b]\), with essential supremum \(b\), satisfying the upper-endpoint tail law
\[
\Pr(J>b-h)\sim C h^{\beta}\qquad(h\downarrow0).
\]
For each \(\lambda>0\), take independent \(G\sim N(0,a)\), \(N_\lambda\sim\operatorname{Poisson}(\lambda)\), and iid copies \(J_i\) of \(J\). Define the centered Gaussian–compound-Poisson variable and its exact variance by
\[
X_\lambda=G+\sum_{i=1}^{N_\lambda}J_i-\lambda\mathbb EJ,
\qquad V_\lambda=a+\lambda\mathbb EJ^2.
\]
Let \(c_\lambda\) be the least \(c\ge0\) for which the **right-sided, variance-exact** sub-gamma inequality
\[
\log\mathbb E e^{tX_\lambda}\le\frac{V_\lambda t^2}{2(1-ct)}
\quad\text{for every }0\le t<1/c
\]
holds, with the usual unbounded domain when \(c=0\). Put
\[
L_\lambda=\log\frac{a}{\lambda b^2},\qquad
K=C\,\Gamma(\beta+1)b^\beta.
\]
As \(\lambda\downarrow0\), the sharp expansion is
\[
\boxed{\frac{b}{c_\lambda}
=L_\lambda+(\beta+3)\log L_\lambda+1-\log(2K)+o(1).}
\]
Moreover, every maximizing tilting argument \(t_\lambda\) in the exact variational formula satisfies
\[
\boxed{bt_\lambda=L_\lambda+(\beta+3)\log L_\lambda-\log(2K)+o(1).}
\]
Thus the **non-atomic jump endpoint exponent** changes the second-order logarithmic coefficient. For the uniform law on \([0,b]\), \(K=1\) and the coefficient is \(4\), not the atomic-endpoint coefficient \(3\). For \(J/b\sim\operatorname{Beta}(1,\beta)\), \(K=\Gamma(\beta+1)\).

## Assumptions and scope

The Gaussian variance \(a\), maximal jump size \(b\), endpoint exponent \(\beta>0\), and endpoint constant \(C>0\) are held fixed; only the Poisson intensity \(\lambda\) tends to zero. No density is assumed for \(J\); only the displayed survival asymptotic is required. No assertion of uniqueness of an optimizer at each finite intensity is needed. The result concerns the right tail with the variance proxy fixed at the **true variance**, not an arbitrary Bernstein proxy or an unoptimized tail bound. It does not claim uniformity when \(a\), \(b\), or the jump distribution varies with \(\lambda\).

## Proof

**1. Exact variational reduction.** Scale the jump to \(W=J/b\in[0,1]\), and write \(\mu=\mathbb EW\), \(\nu=\mathbb EW^2\), \(\delta=\lambda b^2/a=e^{-L_\lambda}\), and \(F(z)=\mathbb E e^{zW}\). For \(z>0\), the cumulant generating function is
\[
\log\mathbb E e^{(z/b)X_\lambda}
=\frac{a z^2}{2b^2}+\lambda(F(z)-1-\mu z).
\]
Define
\[
q_\delta(z)=\frac{2\delta}{z^2}(F(z)-1-\mu z),\qquad
M_\delta(z)=\frac{1+q_\delta(z)}{1+\delta\nu}.
\]
Then \(M_\delta(z)\) is exactly twice the cumulant generating function divided by \(V_\lambda(z/b)^2\). The inequality defining \(c_\lambda\), rearranged both inside and beyond its admissible moment range, yields the exact elementary variational identity
\[
\frac{c_\lambda}{b}=\sup_{z>0} f_\delta(z),\qquad
f_\delta(z)=\frac{1-M_\delta(z)^{-1}}{z}.
\]
This is the established optimal-scale principle, restated here in the present normalization.

**2. Endpoint Laplace lemma.** The assumed tail of \(J\) implies for \(Y=1-W\) that \(\Pr(Y\le y)\sim Cb^\beta y^\beta\). Integration by parts and the change of variable \(u=zy\), followed by dominated exponential-tail truncation, give
\[
\mathbb E e^{-zY}\sim Cb^\beta\Gamma(\beta+1)z^{-\beta}=Kz^{-\beta}.
\]
Therefore \(F(z)\sim K e^z z^{-\beta}\). Under the tilted probability with density proportional to \(e^{-zY}\), \(Y\to0\) in probability, so \(F'(z)/F(z)=1-\mathbb E_zY\to1\). Consequently, for \(z\to\infty\), independently of the choice of \(\delta>0\),
\[
q_\delta(z)\sim2\delta K e^z z^{-(\beta+2)},
\qquad \frac{q_\delta'(z)}{q_\delta(z)}\longrightarrow1.
\]
The uniformity relevant here follows because \(\delta\) factors out of the ratio, and the terms \(1+\mu z\) are negligible relative to \(F(z)\).

**3. Localization of global maximizers.** Since \(e^u-1-u-u^2/2\le u^3e^u/6\) for \(u\ge0\), we have
\[
0\le M_\delta(z)-1\le\frac{\delta z e^z}{3(1+\delta\nu)},
\qquad 0\le f_\delta(z)\le\frac{\delta e^z}{3}.
\]
Also \(f_\delta(z)\le1/z\). Thus \(f_\delta\) extends continuously to \(z=0\), tends to zero at infinity, and is positive somewhere, so a positive interior maximizer exists. Set \(z_0=L_\lambda+(\beta+3)\log L_\lambda\). From step 2,
\[
q_\delta(z_0)\sim2K L_\lambda,\qquad
f_\delta(z_0)=\frac{1-o(1)}{L_\lambda}.
\]
For each fixed \(\varepsilon\in(0,1)\), the exponential upper bound excludes \(z\le(1-\varepsilon)L_\lambda\); the \(1/z\) upper bound excludes \(z\ge(1+\varepsilon)L_\lambda\). Hence every maximizer \(z_\delta\) obeys \(z_\delta/L_\lambda\to1\). The trial bound then implies
\[
z_\delta f_\delta(z_\delta)\longrightarrow1,
\qquad M_\delta(z_\delta)\longrightarrow\infty,
\qquad q_\delta(z_\delta)\longrightarrow\infty.
\]

**4. Stationarity and second-order expansion.** Differentiating at an interior maximizer gives
\[
z_\delta M_\delta'(z_\delta)
=M_\delta(z_\delta)(M_\delta(z_\delta)-1).
\]
Substitution of the formula in step 1 yields the exact equation
\[
z_\delta(1+\delta\nu)q_\delta'(z_\delta)
=(1+q_\delta(z_\delta))(q_\delta(z_\delta)-\delta\nu).
\]
Divide by \(q_\delta(z_\delta)\), use step 2 and \(q_\delta(z_\delta)\to\infty\), obtaining \(q_\delta(z_\delta)/z_\delta\to1\). The logarithm of the Laplace asymptotic in step 2 now gives
\[
z_\delta=L_\lambda+(\beta+3)\log z_\delta-\log(2K)+o(1).
\]
As \(z_\delta/L_\lambda\to1\), this proves the asserted tilt asymptotic. Finally, using \(c_\lambda/b=f_\delta(z_\delta)\),
\[
\frac{b}{c_\lambda}
=\frac{z_\delta M_\delta(z_\delta)}{M_\delta(z_\delta)-1}
=z_\delta+\frac{z_\delta}{M_\delta(z_\delta)-1}
=z_\delta+1+o(1),
\]
since \(M_\delta\sim q_\delta\sim z_\delta\). The two expansions follow. \(\square\)

## Verification

The included `check.py` independently evaluates exact beta-family jump moment generating functions and their derivatives for integer endpoint exponents \(1,2,3\). It numerically solves the stationary optimality equation at three intensities per family, confirms local optimality on a multi-point grid and checks the shrinking difference from the proposed expansion. It passes 90 deterministic assertions using only the Python standard library. These tests are finite evidence for the calculations and do not substitute for the asymptotic proof.

## Relationship to prior work

Chen, *Optimal Sub-Gamma Scales for Spectrally Positive Infinitely Divisible Laws*, arXiv:2610.00032v1, proves the general exact optimal-scale variational identity and treats gamma and bounded two-point jump examples. Chen and Wang, *Directional Optimal Sub-Gamma Scales for Infinitely Divisible Laws*, arXiv:2609.02590v1, analyze other directional and atomic endpoint behaviors. Both the general variational formula and the atomic positive-jump logarithmic correction precede this result. The contribution claimed here is the explicit **non-atomic regularly varying jump-endpoint** expansion, including the \(\beta+3\) coefficient and the tail-amplitude constant \(-\log(2C\Gamma(\beta+1)b^\beta)\) in the Gaussian-dominated rare-intensity limit. A general leading logarithmic law alone cannot determine either of these terms.

## Limitations

The comparison with known literature is not a proof of historical priority; a broader unlocated saddle-point theorem might imply the formula. The theorem assumes fixed positive Gaussian variance, bounded nonnegative jumps with a power-law upper-endpoint survival function and intensity tending to zero. It does not cover unbounded jumps, vanishing Gaussian variance, logarithmic endpoint corrections beyond the assumed regular variation, the simultaneous variation of model parameters, or a rate for the \(o(1)\) term. Independent validation has not been performed.

## References

1. Y. Chen, *Optimal Sub-Gamma Scales for Spectrally Positive Infinitely Divisible Laws*, arXiv:2610.00032v1 (first public 2026-09-02), https://arxiv.org/abs/2610.00032.
2. Y. Chen and X. Wang, *Directional Optimal Sub-Gamma Scales for Infinitely Divisible Laws*, arXiv:2609.02590v1 (2026), https://arxiv.org/abs/2609.02590.
3. S. Boucheron, G. Lugosi and P. Massart, *Concentration Inequalities: A Nonasymptotic Theory of Independence*, Oxford University Press (2013), for standard sub-gamma terminology and bounds.
