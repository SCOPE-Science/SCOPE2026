# Two rare-displacement crossover scales for an interpolating quantum walk

## Finding

The fixed-parameter diffusive limit law for the Yoshino–Shiratori–Yamagami–Horisaki–Segawa interpolating quantum walk has **two distinct rare-displacement scales** near its persistent-classical limit. The first has displacement \(|x|\asymp\sqrt{r/q}\) and an exact modified-Bessel enhancement profile; the second has \(|x|\asymp\sqrt r/q\) and a further exponential correction. This statement concerns the density of the fixed-\(q\), infinite-time weak limit and does not infer a joint finite-time limit.

Let \(f_q\) be the limit-law density and \(\phi_r(x)=(2\pi r)^{-1/2}\exp[-x^2/(2r)]\). Put \(\eta=qx^2/r\), and \(I_0(\eta)=\pi^{-1}\int_0^\pi\exp(\eta\cos\theta)\,d\theta\). For every \(r>0\), \(0<q\le1/4\), and \(x\in\mathbb R\),
\[
 e^{-8q(1+\eta)} I_0(\eta)
 \le \frac{f_q(x)}{\phi_r(x)}
 \le e^{8q(1+\eta)} I_0(\eta).
\]
Consequently, for any sequence \(q\downarrow0\) with \(qx^2/r\to z<\infty\), the density ratio converges to \(I_0(z)\). This exhibits a nontrivial crossover at the first scale despite the ordinary weak Gaussian limit as \(q\downarrow0\).

There is also a **uniform far-tail asymptotic**, valid as \(\eta\to\infty\) simultaneously with arbitrary \(0<q\le1/4\):
\[
 \frac{f_q(x)}{\phi_r(x)}
 = \frac{1+q}{\sqrt{2\pi\eta}}
   \exp\!\left(\frac{\eta}{1+q}\right)
   \bigl(1+O(\eta^{-1})\bigr).
\]
The constant implicit in \(O(\eta^{-1})\) is absolute, independent of \(r,q,x\) over this range. In the double scaling \(q\downarrow0\), \(\eta\to\infty\), and \(q\eta\to z\in[0,\infty)\), this implies the **second crossover law**
\[
\frac{f_q(x)}{\phi_r(x) I_0(\eta)}\longrightarrow e^{-z}.
\]
Since \(q\eta=q^2x^2/r\), its displacement scale is \(|x|\asymp\sqrt r/q\), parametrically beyond the initial Bessel crossover.

For each fixed \(q\in(0,1)\), define \(U_q=r(1+q)/(1-q)\). The corresponding sharp far-tail density and two-sided survival laws are
\[
 f_q(x)\sim\frac{1+q}{2\pi\sqrt q\,|x|}\,e^{-x^2/(2U_q)},
 \qquad
 \Pr(|Y_q|>x)\sim\frac{U_q(1+q)}{\pi\sqrt q\,x^2}\,e^{-x^2/(2U_q)}
 \quad (x\to\infty).
\]

## Assumptions and scope

Consider the one-dimensional discrete-time interpolating model of Yoshino et al. A classical persistent-walk update is chosen independently with probability \(p=1-q\), and a quantum-walk update with probability \(q\). The unitary two-state coin has nonzero diagonal and off-diagonal magnitudes, written \(r=|a|^2/|b|^2\in(0,\infty)\). The initial walker is at the origin with maximally mixed coin state. The existing weak-limit theorem, for each fixed \(0<q<1\), identifies the diffusive scaled position \(Y_q\) as \(\sqrt{V_q}Z\), with \(Z\sim N(0,1)\) independent of \(V_q\) and
\[
 V_q=\frac{r(1+q^2+2q\cos\Theta)}{1-q^2},
 \qquad \Theta\sim\operatorname{Uniform}[0,\pi].
\]
Equivalently \(V_q\) has the arcsine law between \(L_q=r(1-q)/(1+q)\) and \(U_q=r(1+q)/(1-q)\). These fixed-parameter distributional facts are **prior work**, not a new conclusion. The new conclusions are the global comparison inequality, uniform large-\(\eta\) estimate, two scaling profiles and their sharp tail prefactors. They are statements about the already-taken time limit; they make no assertion that finite-time and small-\(q\) limits commute.

## Proof

**1. Exact ratio.** Write \(c=\cos\theta\), \(s_q(c)=V_q/r=(1+2qc+q^2)/(1-q^2)\), and condition on \(\Theta\). The normal density gives
\[
 \frac{f_q(x)}{\phi_r(x)}
 =\frac1\pi\int_0^\pi A_q(\cos\theta)
       \exp\bigl(\eta B_q(\cos\theta)\bigr)\,d\theta,
\]
where
\[
 A_q(c)=\sqrt{\frac{1-q^2}{1+2qc+q^2}},\qquad
 B_q(c)=\frac{c+q}{1+2qc+q^2}.
\]
All denominators are strictly positive for \(0<q<1\). The exponent follows from \((x^2/(2r))(1-s_q(c)^{-1})=\eta B_q(c)\).

**2. Explicit all-displacement bound.** For \(-1\le c\le1\), \(0<q\le1/4\),
\[
 |\log A_q(c)|\le\operatorname{arctanh}(q)
 \le\frac q{1-q}\le\frac43q.
\]
An exact subtraction yields
\[
 B_q(c)-c=\frac{q(1-2c^2-qc)}{1+2qc+q^2},
 \qquad |B_q(c)-c|\le \frac{q(3+q)}{(1-q)^2}\le\frac{52}{9}q.
\]
Thus \(|\log A_q(c)+\eta[B_q(c)-c]|\le8q(1+\eta)\). Comparing the integrands pointwise with \(\exp(\eta c)\), then integrating, gives the stated global two-sided comparison. For bounded \(\eta\) its relative error is \(O(q)\), uniformly over bounded \(\eta\)-intervals.

**3. Uniform large-\(\eta\) Laplace expansion.** For \(q\in[0,1/4]\), the function \(B_q(c)\) is strictly increasing since
\[
 \frac{dB_q}{dc}(c)=\frac{1-q^2}{(1+2qc+q^2)^2}>0.
\]
Its unique maximum on \([-1,1]\) is at \(c=1\), where
\[
 B_q(1)=\frac1{1+q},\quad
 b_q:=\frac{dB_q}{dc}(1)=\frac{1-q}{(1+q)^3},\quad
 A_q(1)=\sqrt{\frac{1-q}{1+q}}.
\]
The derivatives of \(A_q,B_q\) are bounded uniformly for \(q\in[0,1/4]\), and \(b_q\) is uniformly bounded away from zero. Substituting \(y=1-\cos\theta\) transforms the integral into a Laplace endpoint integral with weight \([y(2-y)]^{-1/2}\). Near \(y=0\), uniformly in \(q\),
\[
 B_q(1-y)=B_q(1)-b_qy+O(y^2),\quad
 A_q(1-y)=A_q(1)(1+O(y)),\quad
 [y(2-y)]^{-1/2}=(2y)^{-1/2}(1+O(y)).
\]
For \(y\ge\epsilon>0\), strict monotonicity and compactness give an exponential suppression uniform in \(q\). For \(y\le\epsilon\), the substitution \(t=\eta b_qy\), dominated convergence with the displayed Taylor remainders (or a standard split at \(y=\eta^{-2/3}\)) yields a **uniform relative error** \(O(\eta^{-1})\). Using \(\int_0^\infty t^{-1/2}e^{-t}\,dt=\sqrt\pi\), the leading term is
\[
 \frac{A_q(1)}{\sqrt{2\pi\eta b_q}}
  e^{\eta/(1+q)}
 =\frac{1+q}{\sqrt{2\pi\eta}}e^{\eta/(1+q)}.
\]
This proves the uniform far-tail statement, including the endpoint \(q\to0\) of the parameter domain.

**4. Two scales and fixed-parameter tails.** The global bound gives \(f_q/\phi_r\to I_0(z)\) when \(q\to0\) and \(\eta\to z\). For \(\eta\to\infty\), the classical asymptotic \(I_0(\eta)=e^\eta/\sqrt{2\pi\eta}\,(1+O(\eta^{-1}))\), combined with Step 3, gives
\[
 \frac{f_q(x)}{\phi_r(x)I_0(\eta)}
 =(1+q)\exp\!\left(-\frac{q\eta}{1+q}\right)
  (1+O(\eta^{-1})),
\]
with a uniform remainder, hence the stated \(e^{-z}\) profile for \(q\eta\to z\). For fixed \(0<q\le1/4\), rewrite the Step 3 density using \(\eta=qx^2/r\), obtaining the claimed fixed-\(q\) prefactor. The same endpoint Laplace argument applies to every fixed \(0<q<1\), since its positive curvature remains nonzero. Finally, integrate the density using \(\int_x^\infty t^{-1}e^{-t^2/(2U)}dt\sim (U/x^2)e^{-x^2/(2U)}\), and double by symmetry, proving the survival asymptotic for all fixed \(0<q<1\).

## Verification

The standalone script `mix_crossover_checker.py` numerically integrates the exact angular density, compares its logarithm with the stated global \(8q(1+\eta)\) envelope, tests the Bessel and second crossover, and checks the endpoint prefactors for representative parameters. Run `python mix_crossover_checker.py` after installing the dependencies in `requirements.txt`. A successful execution reports **149 checks**. The script does not prove the global bounds or infinite limits; all quantified claims are derived analytically above.

## Relationship to prior work

Yoshino, Shiratori, Yamagami, Horisaki and Segawa (2025) supply the discrete-time interpolation, the weak-limit theorem, and its exact arcsine normal-variance mixture. The construction, mixture representation, and ordinary \(q\downarrow0\) weak Gaussian limit are not claimed as new. Classical normal-variance mixture theory supplies the Gaussian mixture integral; the usual Laplace method and modified-Bessel asymptotic are established tools. The additional result is a uniform two-parameter comparison with an explicit error, revealing two distinct rare-displacement scales and a sharp second scaling profile. The primary paper's theorem, density, model, and discussion were compared; no corresponding displacement-tail theorem was identified there in the accessible full-text sections. This does **not** exclude implicit coverage in general normal-mixture asymptotic theory or in uninspected appendices.

## Limitations

All results concern the **density of the fixed-parameter infinite-time weak limit**; they are not large-deviation estimates for the walk at finite time, nor a joint theorem for simultaneously changing time and \(q\). The uniform bounds are proved for \(q\le1/4\), although the separate fixed-\(q\) tail law holds for all \(0<q<1\). The use of exact source mixture formulas means that the principal originality risk is implicit coverage by a more general Gaussian-mixture saddle-point analysis. Independent expert verification has not been conducted.

## References

1. S. Yoshino, H. Shiratori, T. Yamagami, R. Horisaki and E. Segawa, *Normal Variance Mixture with Arcsine Law of an Interpolating Walk Between Persistent Random Walk and Quantum Walk*, arXiv:2503.03021v1 (first posted 2025-03-04); *Entropy* **27** (2025), 670. DOI: 10.3390/e27070670. https://arxiv.org/abs/2503.03021 ; https://www.mdpi.com/1099-4300/27/7/670
2. O. E. Barndorff-Nielsen, J. Kent, and M. Sørensen, *Normal variance-mean mixtures and z distributions*, *International Statistical Review* **50** (1982), 145–159. General background on normal variance mixtures; not a source of the two-scale quantum-walk claim.
