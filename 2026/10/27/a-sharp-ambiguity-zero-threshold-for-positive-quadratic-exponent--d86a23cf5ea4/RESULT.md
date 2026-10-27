# A sharp ambiguity-zero threshold for positive quadratic-exponential pulses

## Finding

Let \(d\geq 0\), define the real causal window
\[
g_d(t)=(1+d t^2)e^{-t}\mathbf 1_{[0,\infty)}(t),
\]
and use the angular-frequency self-ambiguity convention
\[
A_d(T,\omega)=\int_{\mathbb R}g_d(u+T/2)g_d(u-T/2)e^{-i\omega u}\,du.
\]
Put
\[
d_*=\frac45(1+\sqrt6),\qquad
\omega_*=\frac{2(1+\sqrt6)}{\sqrt5}.
\]
**Sharp dichotomy.** For \(0\leq d<d_*\), the ambiguity function is nonzero at every real delay and angular frequency. At \(d=d_*\), its only zeros are \((T,\omega)=(0,\pm\omega_*)\). For every \(d>d_*\), it has at least one conjugate-frequency pair of zeros at nonzero delays: there exist \(T_d>0\), \(\omega_d>0\) with \(A_d(\pm T_d,\pm\omega_d)=0\), independently choosing either sign.

The windows \(e^{-t}\mathbf 1_{t\ge0}\) and \(t^2e^{-t}\mathbf1_{t\ge0}\) each have zero-free self-ambiguity, whereas their strictly positive combination \(g_d\) has ambiguity zeros precisely when \(d\ge d_*\). In particular, the zero-free self-ambiguity property is not preserved by positive addition, even within the three-dimensional span of the first causal exponential moments.

## Assumptions and scope

All parameters and variables are real; \(d\geq0\), \(T,\omega\in\mathbb R\). Endpoint values of the indicator at zero are immaterial. The Fourier kernel is \(e^{-i\omega u}\), rather than the cycles-per-time convention \(e^{-2\pi i\xi u}\); thus \(\omega=2\pi\xi\) in the latter convention. Zeros mean simultaneous vanishing of real and imaginary parts. The claim is a global *existence/nonexistence* classification; no count or uniqueness of off-axis zeros for \(d>d_*\) is claimed.

## Proof

**1. Exact rational reduction.** The product in the ambiguity integral is even in \(T\). For \(T\geq0\), write \(u=v+T/2\), so \(v\geq0\) and
\[
A_d(T,\omega)=e^{-T-i\omega T/2}\int_0^\infty (1+d(v+T)^2)(1+dv^2)e^{-(2+i\omega)v}\,dv.
\]
With \(z=2+i\omega\), integration of the monomials gives
\[
A_d(T,\omega)=\frac{e^{-T-i\omega T/2}}{z^5}P_{d,T}(z),
\]
where
\[
P_{d,T}(z)=(1+dT^2)z^4+2dTz^3+(4d+2d^2T^2)z^2+12d^2Tz+24d^2.
\]
The prefactor and denominator never vanish on the physical line \(\operatorname{Re}z=2\). Moreover, \(A_d(-T,\omega)=A_d(T,\omega)\) and \(A_d(T,-\omega)=\overline{A_d(T,\omega)}\). Thus it suffices to locate intersections of the polynomial zero set with that vertical line for \(T\geq0\).

**2. The critical zero-delay pair.** At \(T=0\),
\[
P_{d,0}(z)=z^4+4dz^2+24d^2.
\]
For \(d>0\), its four roots have the form
\[
z=\pm\sqrt{d(\sqrt6-1)}\ \pm i\sqrt{d(\sqrt6+1)},
\]
with independent signs. A root lies on \(\operatorname{Re}z=2\) exactly when \(d=d_*\), and then its imaginary coordinate is \(\pm\omega_*\). The four roots are distinct for \(d>0\). At \(d=0\), the ambiguity integral is an elementary nonvanishing exponential transform.

**3. The entire zero-free range.** Fix \(0<d\le d_*<3\) and \(T>0\). Let \(Q_{d,T}(s)=P_{d,T}(s+2)\), with real coefficients \(a_4s^4+a_3s^3+a_2s^2+a_1s+a_0\). Each coefficient is strictly positive. The two nontrivial quartic Hurwitz determinants are
\[
\Delta_2=a_3a_2-a_4a_1,
\qquad
\Delta_3=a_3a_2a_1-a_4a_1^2-a_3^2a_0.
\]
Direct expansion gives
\[
\frac{\Delta_2}{4}=(2d^3+40d^2)T^4+d^2(30-2d)T^3+(12d^2+80d)T^2+d(30-d)T+4d+40.
\]
Every displayed coefficient is strictly positive when \(0<d<3\). Also
\[
\Delta_3=16\sum_{j=0}^6 b_j(d)T^j,
\]
where
\[
\begin{aligned}
b_0&=16(-5d^2+8d+16),\\
b_1&=-8d(5d^2-16d-48),\\
b_2&=-d(9d^3+104d^2-512d-768),\\
b_3&=-4d^2(7d^2-56d-192),\\
b_4&=-2d^2(3d^3+18d^2-224d-384),\\
b_5&=2d^3(d+8)(d+24),\\
b_6&=4d^3(d+8)^2.
\end{aligned}
\]
For \(0<d<3\), each \(b_j(d)\) with \(j\geq1\) is strictly positive. To check the three non-obvious negative brackets, use \(d^2<3d\) and \(d^3<9d\): respectively their positive terms are bounded by \(393d\), \(21d\), and \(81d\), which are smaller than the corresponding negative linear terms (the \(393d\) bound belongs to the bracket in \(b_2\)); the bracket in \(b_4\) has bound \(81d\). Explicitly, for \(b_2\), \(9d^3+104d^2\le393d<512d+768\); for \(b_3\), \(7d^2\le21d<56d+192\); and for \(b_4\), \(3d^3+18d^2\le81d<224d+384\). The bracket in \(b_1\) is negative because \(5d^2<15d<16d+48\). Finally \(b_0\ge0\) precisely for \(0<d\le d_*\), with equality only at \(d_*\). It follows that \(\Delta_3>0\) for every \(T>0\) in the stated range.

The strict quartic Routh–Hurwitz criterion (positive coefficients and \(\Delta_2,\Delta_3>0\)) therefore places **every** root of \(Q_{d,T}\) in \(\operatorname{Re}s<0\). Since \(z=s+2\), no root of \(P_{d,T}\) can have real part \(2\). Together with step 2 and the elementary \(d=0\) case, this proves the claimed zero-free range and identifies exactly two zeros at \(d=d_*\).

**4. Zeros beyond the threshold.** For \(d>d_*\), step 2 gives two roots of \(P_{d,0}\) whose real parts equal \(\sqrt{d(\sqrt6-1)}>2\). On the other hand, for fixed \(d>0\), coefficientwise
\[
\frac{P_{d,T}(z)}{dT^2}\longrightarrow z^2(z^2+2d)
\qquad(T\to\infty).
\]
The multisets of four polynomial roots converge, with multiplicity, to \(\{0,0,i\sqrt{2d},-i\sqrt{2d}\}\). Thus the maximum real part among the roots tends to zero as \(T\to\infty\). This maximum is continuous in \(T\geq0\) (continuity of polynomial roots as a multiset). Hence at some \(T_d>0\), a root has real part exactly \(2\). Since \(P_{d,T}(2)>0\), its imaginary part is nonzero; conjugation produces the opposite frequency. The even-delay symmetry produces the negative-delay counterparts. This completes the global dichotomy.

**5. The two endpoints of the positive mixture.** For \(g(t)=e^{-t}\mathbf1_{t\ge0}\), the reduced Laplace integral is \(1/z\), zero-free. For \(h(t)=t^2e^{-t}\mathbf1_{t\ge0}\), the corresponding reduced integral equals
\[
\frac{2T^2z^2+12Tz+24}{z^5}
\]
up to the same nonzero delay factor. For \(T>0\), the two roots of its numerator have negative real part; at \(T=0\) the numerator is the nonzero constant \(24\). Thus \(h\) is zero-free as well. Nevertheless \(g_d=g+dh\) has zeros for every \(d\geq d_*\), proving the claimed failure of positive-addition preservation.

## Verification

The standalone `checker.py` symbolically reconstructs the quartic, the two Hurwitz determinants and all seven \(\Delta_3\) coefficient identities; it confirms the exact critical pair. It also checks the integral formula against direct 60-digit numerical quadrature in four parameter cases and computes representative supercritical zeros at three weights. Execute with `python checker.py` after installing the libraries listed in `requirements.txt`. These finite calculations are not substitutes for the analytic all-parameter Hurwitz and continuity arguments above.

## Relationship to prior work

Gröchenig, Jaming and Malinnikova's work on zeros of the Wigner distribution and short-time Fourier transform proves zero-free ambiguity for one-sided exponentials, two-factor exponential convolutions, and each pure causal gamma moment \(t^n e^{-t}\mathbf1_{t>0}\), using Bessel and Hurwitz polynomials; those are known endpoints, not new here. It does **not** state the positive quadratic-exponential mixture threshold above, and the mixture is not a pure monomial, a two-factor convolution, or a metaplectic image of a cited endpoint. Kloos and Stöckler's work on totally positive Gabor windows concerns Zak-transform zero counts and frame sets, not this ambiguity-zero bifurcation. Earlier general results about radar ambiguity and positive-definite transforms do not by themselves imply the presented sharp parameter threshold. Publication-priority verification remains nonexhaustive, particularly for older radar-window literature.

## Limitations

The theorem concerns one particular natural positive two-moment family, with unit decay rate; scaling gives other common decay rates. It does not classify the number, simplicity, or exact locations of all supercritical off-axis ambiguity zeros, nor does it assert robustness to arbitrary window perturbations. No independent audit or formal verification has been carried out. Symbolic and numerical checker output complements but does not replace the full proof.

## References

1. Kloos, T., and Stöckler, J., *Zak transforms and Gabor frames of totally positive functions and exponential B-splines*, arXiv:1311.7359, first posted 2013-11-28, https://arxiv.org/abs/1311.7359.
2. Gröchenig, K., Jaming, P., and Malinnikova, E., *Zeros of the Wigner Distribution and the Short-Time Fourier Transform*, arXiv:1811.03937, first posted 2018-11-09, https://arxiv.org/abs/1811.03937; published as *Revista Matemática Complutense*, DOI:10.1007/s13163-019-00335-w, full-text Sections 3–4.
3. Routh, E. J., *A Treatise on the Stability of a Given State of Motion*, 1877; Hurwitz, A., *Über die Bedingungen, unter welchen eine Gleichung nur Wurzeln mit negativen reellen Theilen besitzt*, 1895 (classical stability criterion).
