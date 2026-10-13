# Sharp lower bound for a quartic–quadratic mixed-sign Gaussian moment

## Finding
Let \((X,Y,Z)\) be any centered jointly Gaussian triple with \(\mathbb E X^2=\mathbb E Y^2=\mathbb E Z^2=1\); singular covariance matrices are permitted. For every real \(0<u<1\),
\[
\boxed{\mathbb E[|X|^{-u}Y^4Z^2]\ \ge\ (1-u)(3-u)\,\mathbb E|X|^{-u}.}
\]
The constant is optimal, and equality holds **exactly** when \(Y=X\) or \(Y=-X\) almost surely and \(Z\) is independent of \(X\). In terms of the product of the three marginal moments, the best universal factor is \((1-u)(3-u)/3\), because \(\mathbb E Y^4=3\) and \(\mathbb E Z^2=1\).

## Assumptions and scope
The three variables are real, zero-mean jointly Gaussian, each with unit variance. No restrictions are imposed on their correlations apart from positive semidefiniteness. A possibly singular covariance is included; for positive definite covariance the inequality is strict but the constant is still the infimum by approximation. The negative exponent satisfies \(0<u<1\), ensuring \(\mathbb E|X|^{-u}<\infty\). This is a bound for the **specific exponent pattern** negative \(u\), positive \(4\), positive \(2\); no statement for other powers or non-Gaussian laws is asserted.

## Proof
Write \(t=1-u\in(0,1)\), \(a=\mathbb E[XY]\), \(v=\sqrt{1-a^2}\), and \(r=a^2\). Extend the probability space, if necessary, to independent standard Gaussians \(X,W,V\), so that
\[
Y=aX+vW,\qquad Z=kX+\ell W+mV,\qquad k^2+\ell^2+m^2=1.
\]
Set \(M=\mathbb E|X|^{-u}=2^{-u/2}\Gamma((1-u)/2)/\sqrt\pi\). Gamma recurrence gives, for nonnegative integers \(j\),
\[
\frac{\mathbb E[|X|^{-u}X^{2j}]}M=\prod_{h=0}^{j-1}(t+2h).
\]
Consequently, by expanding \(Y^4\) and using the independent even Gaussian moments,
\[
\frac{\mathbb E[|X|^{-u}Y^4Z^2]}M
 =k^2A+2k\ell B+\ell^2C+m^2D,
\]
where
\[
\begin{aligned}
A&=r^2t(t+2)(t+4)+6r(1-r)t(t+2)+3(1-r)^2t,\\
B&=4a^3vt(t+2)+12av^3t,\\
C&=r^2t(t+2)+18r(1-r)t+15(1-r)^2,\\
D&=r^2t(t+2)+6r(1-r)t+3(1-r)^2.
\end{aligned}
\]
We show this quadratic form is at least \(T=t(t+2)\) on every unit vector \((k,\ell,m)\). First,
\[
D-T=(1-r)(1-t)\bigl(3+t-r(3-t)\bigr)\ge0.
\]
Also,
\[
A-T=t\bigl(1-t+6r(t+1)+r^2(t^2-1)\bigr)
\ge t\bigl(1-t+r(t^2+6t+5)\bigr)>0.
\]
For the upper-left \(2\times2\) block, direct polynomial expansion yields
\[
(A-T)(C-T)-B^2=t(1-r)(1-t)(t+5)K(r,t),
\]
where the **Bernstein-positive polynomial**
\[
\begin{aligned}
K(r,t)={}&(3-t)(1-r)^3+2(t+12)r(1-r)^2\\
&+(t+2)(t+9)r^2(1-r)+2t(t+2)r^3
\end{aligned}
\]
is positive for every \(r\in[0,1]\) and \(t\in(0,1)\). Hence the \(2\times2\) block minus \(TI_2\) is positive semidefinite; it is positive definite if \(r<1\). Together with \(D\ge T\), this proves the bound.

If \(r<1\), the \(2\times2\) block is positive definite and \(D>T\), so equality is impossible. If \(r=1\), then \(v=0\), \(Y=\pm X\), \(B=0\), \(C=D=T\), and \(A=t(t+2)(t+4)>T\). Thus equality holds precisely if \(k=0\), namely \(Z\) is independent of \(X\). Choosing independent standard normal \(X,Z\) and \(Y=X\) realizes equality, proving sharpness. Positive-definite examples approaching that singular triple yield the same infimum.

## Verification
The accompanying standalone `VERIFY.py` requires Python 3 and no third-party packages. Run `python3 VERIFY.py`. It checks 207 independent exact-rational algebraic identities, Gaussian moment expansions, inequality cases, and equality boundary configurations. Its moment expansion uses independent Gaussian even moments directly, separately from the quadratic-form formula. The algebraic factorization and its sign on the full parameter ranges are proved above; the finite checks are not used as a substitute for that proof.

## Relationship to prior work
Russell and Sun (2022) prove the **bivariate** opposite Gaussian product inequality for one negative and one positive power. Zhou, Zhao, Hu and Song (2023 preprint, Proposition 1.6) prove, among other inequalities, a three-dimensional covariance-dependent lower bound for negative \(u\) and arbitrary two positive powers, including \((4,2)\). That lower bound specializes to \(3M(1-a^2)^2(1-b^2)\), with \(b=\mathbb E[XZ]\), and becomes zero at the very configuration where the present strictly positive optimal constant is attained. Their upper comparison is not claimed as new here. Lan, Ouimet and Sun (2025 preprint, Theorem 1) extend analogous Schur-complement lower bounds but do not give this sharp covariance-independent endpoint for \((4,2)\). This result therefore answers a **different extremal question**: the exact correlation-free infimum and its equality cases for the first unequal even-power three-factor pattern. Previously studied \((2,2)\) formulas do not state this \((4,2)\) optimization.

## Limitations
Only this explicit exponent pattern and real Gaussian triples are covered; the result does not assert general mixed-sign Gaussian product inequalities or all higher even exponents. Equality lies at a singular covariance, so it is an infimum rather than an attained minimum if positive definiteness is required. The literature comparison cannot exclude every unpublished or differently named earlier inequality, and independent scientific assessment has not been performed.

## References
1. O. Russell and W. Sun, *An Opposite Gaussian Product Inequality*, arXiv:2205.10231v1 (first posted 2022-05-20), https://arxiv.org/abs/2205.10231; doi:10.1016/j.spl.2022.109656.
2. Q.-Q. Zhou, H. Zhao, Z.-C. Hu and R. Song, *Some New Results on Gaussian Product Inequalities*, arXiv:2308.13740v1 (first posted 2023-08-26), https://arxiv.org/abs/2308.13740; doi:10.1016/j.jmaa.2023.127907. Relevant statements: Theorem 1.1, Proposition 1.6 and its proof.
3. G. Lan, F. Ouimet and W. Sun, *Results related to the Gaussian product inequality conjecture for mixed-sign exponents in arbitrary dimension*, arXiv:2505.09976v3 (first posted 2025-05-15), https://arxiv.org/abs/2505.09976. Relevant statement: Theorem 1.
