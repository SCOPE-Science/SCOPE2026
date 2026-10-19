# Sharp zero-exclusion radius for symmetric multiaffine bidisk approximants

## Finding
Fix a real exponent \(\alpha\ge0\) and put \(v=2^\alpha\), \(w=3^\alpha\),
\[
\eta_\alpha=\left(\frac{w+v^2}{w(w/v+2v)}\right)^{1/2},\qquad R_\alpha=\eta_\alpha^{-1}.
\]
For every nonzero symmetric multiaffine polynomial \(f(z_1,z_2)=u+a(z_1+z_2)+bz_1z_2\), \(u\ne0\), let \(p_f=A+B(z_1+z_2)\) be the unique best affine polynomial for \(\|1-pf\|_\alpha\), with the norm defined below. Then \(A\ne0\) and
\[
\boxed{\quad 2|B/A|\le\eta_\alpha<1,\qquad
\inf_{p_f(z_1,z_2)=0}\max(|z_1|,|z_2|)\ge R_\alpha>1.\quad}
\]
The bound is sharp for every \(\alpha\ge0\). For each fixed exponent, all equality generators, up to multiplication by a nonzero complex scalar, are exactly
\[
 f_{\alpha,\theta}(z_1,z_2)=1+\eta_\alpha e^{i\theta}(z_1+z_2)
   +\frac vw e^{2i\theta}z_1z_2,\qquad\theta\in\mathbb R/(2\pi\mathbb Z).
\]
For every \(\alpha>0\), these extremizing generators themselves have no zeros on the **closed** unit bidisk. Hence \(R_\alpha\) is the exact universal zero-exclusion radius even within the zero-free symmetric multiaffine generators. Moreover \(R_0=\sqrt{3/2}\), \(R_\alpha\) increases strictly with \(\alpha\ge0\), and \(R_\alpha\sim\sqrt2(3/2)^{\alpha/2}\) as \(\alpha\to\infty\).

## Assumptions and scope
In the complex bidisk Dirichlet-type Hilbert space, the monomials are mutually orthogonal and
\[
 \left\|\sum_{j,k\ge0}c_{jk}z_1^jz_2^k\right\|_\alpha^2
 =\sum_{j,k\ge0}|c_{jk}|^2(j+1)^\alpha(k+1)^\alpha.
\]
An *affine* approximant means \(A_0+A_1z_1+A_2z_2\), not an arbitrary multiaffine approximant. Strict convexity and invariance under coordinate swap force the unique minimizer to satisfy \(A_1=A_2=B\). The theorem concerns only symmetric generators of bidegree at most \((1,1)\), with a nonzero constant coefficient; no claim is made for arbitrary polynomial generators, nonsymmetric generators, or higher-degree approximants. The norm and coefficients are fixed exactly as displayed (with no extra factor of one half multiplying \(z_1+z_2\)).

## Proof
Write \(M=z_1+z_2\). The normal equation for the coefficient of \(Mf\) gives
\[
\frac BA=-\frac{\langle Mf,f\rangle_\alpha}{\|Mf\|_\alpha^2}
\]
(up to the harmless inner-product conjugation convention); the other equation ensures \(A\ne0\) because \(u\ne0\). Direct orthogonality of monomials yields
\[
\begin{aligned}
\|Mf\|_\alpha^2&=2v|u|^2+(2w+4v^2)|a|^2+2vw|b|^2,\\
|\langle Mf,f\rangle_\alpha|&=2v|\overline a u+v\overline b a|\le2v|a|(|u|+v|b|).
\end{aligned}
\]
Let \(x=|u|\), \(y=|a|\), \(z=|b|\), and \(c=w/v+2v\). Consequently
\[
 2|B/A|\le\frac{2y(x+vz)}{x^2+cy^2+wz^2}.
\]
The last quotient is the generalized Rayleigh quotient of
\[
 Q=\begin{pmatrix}0&1&0\\1&0&v\\0&v&0\end{pmatrix},
 \qquad D=\operatorname{diag}(1,c,w).
\]
The characteristic polynomial of \(D^{-1/2}QD^{-1/2}\) is \(\lambda(\lambda^2-\eta_\alpha^2)\). Its largest eigenvalue is \(\eta_\alpha\), and its positive top eigenvector is proportional to \((1,\eta_\alpha,v/w)\). Every maximizing nonnegative vector is proportional to this eigenvector, since that eigenvalue is simple. Equality in the triangle inequality requires the two complex summands \(\overline a u\) and \(\overline b a\) to have the same argument. Upon dividing \(f\) by \(u\), this gives exactly \(a=\eta_\alpha e^{i\theta}\), \(b=(v/w)e^{2i\theta}\), proving the equality classification.

A zero of \(p_f=A+B(z_1+z_2)\) obeys \(2\max(|z_1|,|z_2|)\ge|A/B|\), whenever \(B\ne0\), and the diagonal choice \(z_1=z_2=-A/(2B)\) achieves equality. If \(B=0\), there are no zeros. In particular the minimal polydisk radius containing any zero is bounded below by \(1/\eta_\alpha\) and equals it precisely for the preceding extremizers.

To verify the extremal generators are zero-free on the closed unit bidisk when \(\alpha>0\), rotate both coordinates to take \(\theta=0\), and write \(h=v/w=(2/3)^\alpha\) and \(\eta=\eta_\alpha\). For \(|z_1|=1\), a hypothetical zero would require \(z_2=-(1+\eta z_1)/(\eta+h z_1)\). But
\[
 |1+\eta z_1|^2-|\eta+h z_1|^2=(1-h)(1+h+2\eta\Re z_1)>0.
\]
Indeed \(0<h<1\), \(\eta^2=h(1+(4/3)^\alpha)/(1+2(4/3)^\alpha)<2h/3\), and \((1+h)^2>8h/3\), so \(2\eta<1+h\). The Möbius quotient \((\eta+h z_1)/(1+\eta z_1)\) is analytic on the closed disk since \(\eta<1\), and its boundary modulus is strictly less than one. By the maximum-modulus principle, any zero would have \(|z_2|>1\); hence none lies in the closed bidisk.

Finally set \(h_\alpha=(2/3)^\alpha\), \(t_\alpha=(4/3)^\alpha\). The exact identity
\[
\eta_\alpha^2=h_\alpha\frac{1+t_\alpha}{1+2t_\alpha}
\]
shows strict decrease in \(\alpha\), since \(h_\alpha\) strictly decreases and \((1+t)/(1+2t)\) strictly decreases for positive \(t\). Its value at zero is \(2/3\), while its high-exponent equivalent is \(h_\alpha/2\). Taking reciprocal square roots gives the radius claims.

## Verification
The independent standard-library script `check.py` recomputes eleven exact rational characteristic-polynomial/equality identities at integer exponents, tests 12,008 random and extremal cases, tests 100 complex-phase extremizers, and verifies 2,400 coefficient expansions computed independently from the norm definition. Execute `python3 check.py` from the extracted package. The Rayleigh-eigenvalue proof, rather than the finite tests, establishes the theorem for all \(\alpha\ge0\) and all admissible coefficients.

## Relationship to prior work
The Hilbert-space optimal polynomial approximant and zero-location questions are part of the framework developed by Bénéteau, Cheng, Felder, Khavinson, Manolaki and Maronikolakis (arXiv:2511.08000, first version 2025-11-11), whose paper treats metric projections and one-variable Hardy-space zeros. Navío and Seco (arXiv:2609.37180, first version 2026-09-29) produce closed-bidisk-zero-free **higher-degree** symmetric generators whose affine optimal approximants have zeros *inside* the bidisk for positive Dirichlet parameters. These statements do not give the present sharp multiaffine radius: the bidegree restriction is essential and avoids the higher-degree counterexamples. Earlier work of Sargent and Sola (arXiv:2002.08790) studies weak Shanks-type questions in bidisk settings but does not state the present bidegree-specific sharp radius or optimizer family in the portions inspected. No assertion of global novelty is an independent certification.

## Limitations
There is no quantitative claim here for nonsymmetric generators, unrestricted approximation degrees, or other weighted norms. Sharpness is proved only in the specified bidegree-one-in-each-variable class. The proof is analytic; checking a finite numerical collection would not suffice to establish the all-exponent result. Earlier unindexed work could contain an equivalent finite-degree optimization, so the historical-priority assessment remains provisional. Independent mathematical review has not been performed.

## References
1. C. Bénéteau, R. Cheng, C. Felder, D. Khavinson, M. Manolaki, and K. Maronikolakis, *Metric projections, zeros of optimal polynomial approximants, and some extremal problems in Hardy spaces*, arXiv:2511.08000v1 (2025-11-11), https://arxiv.org/abs/2511.08000.
2. O. Navío and D. Seco, *Polynomial Counterexamples to Shanks' Conjecture in Dirichlet-Type Spaces over the Bidisc*, arXiv:2609.37180v1 (2026-09-29), https://arxiv.org/abs/2609.37180.
3. M. Sargent and A. Sola, work on polynomial approximants and weak Shanks-type conjectures on the bidisk, arXiv:2002.08790 (2020), https://arxiv.org/abs/2002.08790.
