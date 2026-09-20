# Quartic endpoint stability and translation bifurcation for the Gaussian volume product

## Statement

Let \(n\ge 2\), let \(s=\sigma^2>0\), and write
\[
\mathcal G_s(K)=\gamma_{\sqrt s}^n(K)\,\gamma_{\sqrt s}^n(K^\circ).
\]
For the Euclidean unit ball \(B=B_2^n\), a unit vector \(e\), and \(|\varepsilon|<1\), set
\[
K_\varepsilon=B+\varepsilon e,
\qquad
\Phi_n(\varepsilon,s)=\frac{\mathcal G_s(K_\varepsilon)}{\mathcal G_s(B)}.
\]
By rotational invariance, the same function describes translation by any vector of length \(|\varepsilon|\).

Artstein-Avidan, Fradelizi and Wyczesany proved that the quadratic translation variation changes sign at
\[
s_c=\frac{2}{n+1},
\]
and used it to show that \(B\) is not a maximizer when \(s>s_c\). At the endpoint \(s=s_c\), that quadratic term vanishes. The endpoint is nevertheless strictly stable inside the translated-unit-ball family, with an explicit negative quartic term.

Define
\[
G_c=\gamma_{\sqrt{s_c}}^n(B),
\qquad
H_c=(2\pi s_c)^{-n/2}e^{-1/(2s_c)}|S^{n-1}|,
\qquad
R_n=\frac{H_c}{G_c},
\]
and
\[
D_n=\frac{2R_n(n+1)(n+2)}{n}-(n^2-17).
\]
Then \(D_n>0\), and
\[
\boxed{
\Phi_n(\varepsilon,s_c)
=1-\beta_n\varepsilon^4+O(\varepsilon^6),
\qquad
\beta_n=
\frac{R_n(n+1)}{32n(n+2)}D_n>0.
}
\]
Consequently the centered ball is a strict local maximizer against translations at the critical variance, despite having zero quadratic translation Hessian.

There is also a local symmetry-breaking branch immediately above the threshold. Put \(\delta=s-s_c\). For all sufficiently small \(\delta>0\), there is a unique small positive critical radius \(r_*(s)\) for translated unit balls, and the full critical orbit is \(|z|=r_*(s)\). It consists of local maxima within the translated-ball family and satisfies
\[
\boxed{
r_*(s)^2
=
\frac{4(n+1)(n+2)}{D_n}\,\delta+O(\delta^2),
}
\]
or equivalently
\[
\boxed{
r_*(s)
=2\sqrt{\frac{(n+1)(n+2)}{D_n}}\,\sqrt\delta
+O(\delta^{3/2}).
}
\]
Their gain over the centered unit ball is
\[
\boxed{
\Phi_n(r_*(s),s)-1
=
\frac{R_n(n+1)^3(n+2)}{2nD_n}\,\delta^2+O(\delta^3).
}
\]
For \(s<s_c\) sufficiently close to \(s_c\), the centered ball is a strict local maximum in translation directions; at \(s=s_c\) it is quartically stable; for \(s>s_c\) sufficiently close, it becomes a strict local minimum in translation directions and an \((n-1)\)-sphere of translated local maxima emerges.

The claims above concern only the finite-dimensional family of translated unit balls. They do not determine the full maximizer among arbitrary convex bodies.

## Proof

Let
\[
G(s)=\gamma_{\sqrt s}^n(B),
\qquad
H(s)=(2\pi s)^{-n/2}e^{-1/(2s)}|S^{n-1}|,
\qquad
R(s)=\frac{H(s)}{G(s)}.
\]
Write
\[
A(\varepsilon,s)=\gamma_{\sqrt s}^n(B+\varepsilon e),
\qquad
P(\varepsilon,s)=\gamma_{\sqrt s}^n((B+\varepsilon e)^\circ).
\]
Both are even analytic functions of \(\varepsilon\) for \(|\varepsilon|<1\).

### 1. The translated ball factor to fourth order

Let \(t=\langle u,e\rangle\). Differentiating under the integral over \(B\), followed by the divergence theorem, gives the second-order coefficient already used in the source paper:
\[
A(\varepsilon,s)
=G(s)-\frac{H(s)}{2ns}\varepsilon^2+a_4(s)\varepsilon^4+O(\varepsilon^6).
\]
For the fourth derivative,
\[
\int_B \partial_e^4 e^{-|x|^2/(2s)}dx
=
 e^{-1/(2s)}\int_{S^{n-1}}
\left(\frac{3t^2}{s^2}-\frac{t^4}{s^3}\right)d\omega(u).
\]
Using
\[
\frac1{|S^{n-1}|}\int t^2d\omega=\frac1n,
\qquad
\frac1{|S^{n-1}|}\int t^4d\omega=\frac{3}{n(n+2)},
\]
one obtains
\[
\boxed{
a_4(s)=\frac{H(s)}{8n}
\left(\frac1{s^2}-\frac1{(n+2)s^3}\right).}
\]

### 2. The polar factor to fourth order

The support function of \(B+\varepsilon e\) is \(1+\varepsilon t\), hence
\[
\rho_{(B+\varepsilon e)^\circ}(u)=\frac1{1+\varepsilon t}.
\]
Set
\[
F_s(r)=(2\pi s)^{-n/2}\int_0^r e^{-q^2/(2s)}q^{n-1}dq.
\]
Then
\[
P(\varepsilon,s)=\int_{S^{n-1}}
F_s\!\left((1+\varepsilon t)^{-1}\right)d\omega(u).
\]
If \(f_s=F_s'\), direct differentiation gives at \(r=1\)
\[
\frac{f_s'}{f_s}=n-1-\frac1s,
\]
\[
\frac{f_s''}{f_s}
=n^2-3n+2-\frac{2n-1}{s}+\frac1{s^2},
\]
and
\[
\frac{f_s'''}{f_s}
=
\frac{n^3s^3-6n^2s^3-3n^2s^2+11ns^3+6ns^2+3ns-6s^3-3s^2-1}{s^3}.
\]
Since
\[
(1+\varepsilon t)^{-1}-1
=-\varepsilon t+\varepsilon^2t^2-\varepsilon^3t^3+\varepsilon^4t^4+O(\varepsilon^5),
\]
the coefficient multiplying \(t^4\varepsilon^4\) in the Taylor expansion of \(F_s\) is
\[
F_s'(1)+\frac32F_s''(1)+\frac12F_s'''(1)+\frac1{24}F_s''''(1).
\]
At \(s=s_c=2/(n+1)\), dividing this quantity by \(F_s'(1)\) simplifies to
\[
\frac{(n+1)(n^2-4n-37)}{192}.
\]
Therefore
\[
P(\varepsilon,s_c)
=G_c+\frac{H_c(n+1)}{4n}\varepsilon^2
+\frac{H_c(n+1)(n^2-4n-37)}{64n(n+2)}\varepsilon^4
+O(\varepsilon^6).
\]
At the same critical value,
\[
A(\varepsilon,s_c)
=G_c-\frac{H_c(n+1)}{4n}\varepsilon^2
+\frac{H_c(n+1)^2(n+3)}{64n(n+2)}\varepsilon^4
+O(\varepsilon^6).
\]

Multiplication yields cancellation of the quadratic terms and gives
\[
\Phi_n(\varepsilon,s_c)
=1+c_{4,n}\varepsilon^4+O(\varepsilon^6),
\]
where
\[
c_{4,n}
=
\frac{R_n(n+1)(n^2-17)}{32n(n+2)}
-
\frac{R_n^2(n+1)^2}{16n^2}
=-\frac{R_n(n+1)}{32n(n+2)}D_n.
\]

### 3. The quartic coefficient is strictly negative

At \(s=s_c\), put \(x=1/(2s_c)=(n+1)/4\) and
\[
I=\int_0^1 e^{-xr^2}r^{n-1}dr,
\qquad
J=\int_0^1 e^{-xr^2}r^{n+1}dr.
\]
The common Gaussian constants cancel, so \(R_n=e^{-x}/I\). Integrating the derivative of \(r^n e^{-xr^2}\) gives
\[
e^{-x}=nI-2xJ.
\]
Since \(J<I\),
\[
R_n>n-2x=\frac{n-1}{2}.
\]
For \(2\le n\le4\), \(D_n>0\) is immediate because \(n^2-17<0\). For \(n\ge5\), the preceding bound gives
\[
D_n>
\frac{(n-1)(n+1)(n+2)}{n}-(n^2-17)
=
\frac{2n^2+16n-2}{n}>0.
\]
Thus \(c_{4,n}<0\), proving the endpoint quartic stability.

### 4. Emergence of translated local maxima

The quadratic coefficient for general \(s\), obtained by multiplying the second-order expansions, is
\[
p_2(s)=\frac{R(s)}{2n}\left(n+1-\frac2s\right).
\]
It vanishes at \(s_c\), and because the parenthesis vanishes there,
\[
p_2'(s_c)=\frac{R_n(n+1)^2}{4n}=:a_n>0.
\]
Analyticity and evenness give, locally uniformly near \((\varepsilon,s)=(0,s_c)\),
\[
\Phi_n(\varepsilon,s)
=1+a_n\delta\varepsilon^2-\beta_n\varepsilon^4
+O(\delta^2\varepsilon^2+|\delta|\varepsilon^4+\varepsilon^6).
\]
Writing \(q=\varepsilon^2\), the nonzero radial critical points solve \(\partial_q\Phi_n=0\). Since
\[
\partial_q^2\Phi_n(0,s_c)=-2\beta_n<0,
\]
the implicit-function theorem gives a unique small branch
\[
q_*(s)=\frac{a_n}{2\beta_n}\delta+O(\delta^2)
=
\frac{4(n+1)(n+2)}{D_n}\delta+O(\delta^2).
\]
For \(\delta>0\), this branch lies in \(q>0\), and its radial second derivative is negative. Rotational invariance turns it into the sphere \(|z|=r_*(s)=\sqrt{q_*(s)}\). Substitution back into the expansion gives
\[
\Phi_n(r_*(s),s)-1
=
\frac{a_n^2}{4\beta_n}\delta^2+O(\delta^3)
=
\frac{R_n(n+1)^3(n+2)}{2nD_n}\delta^2+O(\delta^3).
\]
This proves the claimed local bifurcation law.

## Context and originality boundary

Artstein-Avidan, Fradelizi and Wyczesany introduced the uncentered Gaussian volume-product problem and proved that translations of the ball have second variation proportional to
\[
n+1-\frac2{\sigma^2}.
\]
Their Proposition 5.1 establishes non-optimality of the ball for \(\sigma^2>2/(n+1)\) from this quadratic term. Their current v1 does not compute the fourth variation at equality, the strict sign of that fourth variation, or the nearby nonzero translation branch. The present contribution is precisely this endpoint and bifurcation refinement within the translated-unit-ball family.

Cordero-Erausquin's theorem that the centered ball maximizes the same Gaussian product among centrally symmetric convex bodies is prior work and is not claimed here. In dimension two, the source paper proves that the centered ball is globally optimal at and below \(s_c=2/3\); the quartic calculation here is consistent with and more local than that theorem. In dimensions \(n\ge3\), the global maximization problem near the endpoint remains open.

To the best of our knowledge, searches for higher-order translation variation, quartic endpoint stability, translated-ball bifurcation, and equivalent Gaussian Blaschke--Santaló formulations did not locate this refinement. The main residual originality risk is the recency of arXiv:2609.18472v1: a later revision or an unindexed parallel observation could contain the same calculation.

## Limitations

- The theorem concerns translations of the fixed unit ball only; it is not a full shape-Hessian or full convex-body stability theorem.
- At \(s=s_c\), strict quartic stability against translations does not imply global optimality in dimensions \(n\ge3\).
- The branch above \(s_c\) is a branch of local maxima inside the translated-ball family; no claim is made that those translated balls are local or global maximizers among arbitrary convex bodies.
- No claim is made that \(s_c\) is the first loss of stability for all nonsymmetric shape modes.
- The source preprint is very recent, so revision and parallel-work risk remains.

## References

1. S. Artstein-Avidan, M. Fradelizi, K. Wyczesany, *Uncentered Blaschke-Santaló inequalities for the Gaussian measure*, arXiv:2609.18472v1 (2026). https://arxiv.org/abs/2609.18472
2. D. Cordero-Erausquin, *Santaló's inequality on C^n by complex interpolation*, C. R. Math. Acad. Sci. Paris 334 (2002), 767--772. https://doi.org/10.1016/S1631-073X(02)02328-2
