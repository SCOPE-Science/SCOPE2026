# Same-model review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

PASS.

For the D=infinity slow-limit system of arXiv:2609.20609v1, the source's variables

\[
\varphi=(\alpha-\alpha_*)g_{\max},\qquad h=(g_{\max}-g)/g_{\max}
\]

turn its representation formula into the exact identity

\[
u(x,t)=\big[u_0(x)+A(t)-(t+A(t))h(x)\big]_+,
\qquad A(t)=\int_0^t\varphi(s)\,ds.
\]

Setting \(\tau=t+A\) and \(q=A/\tau\) gives \(u=\tau[q-h+u_0/\tau]_+\). The source proves \(\alpha\downarrow\alpha_*\), hence \(\varphi\to0\), \(A=o(t)\), and \(q\to0\).

For finitely many nondegenerate minima of normalized \(h\), the Morse expansion gives

\[
G(s):=\int(s-h)_+=Cs^2+o(s^2),\qquad
C=\pi\sum_j(\det H_j)^{-1/2}.
\]

Mass conservation yields the two-sided squeeze

\[
G(q)\le\tau^{-1}\le G(q+\|u_0\|_\infty/\tau).
\]

This first implies \(q\asymp\tau^{-1/2}\), so the initial-data correction is \(o(q)\); a second application then gives \(C\tau q^2\to1\). The resulting asymptotics for \(q,A\), peak height, and support width follow algebraically.

The multiplier asymptotic was checked separately rather than inferred by differentiating an asymptotic equivalence. The active set is sandwiched between the sublevel sets \(\{h<q\}\) and \(\{h<q+o(q)\}\). For Morse minima,

\[
|\{h<s\}|=2Cs+o(s),\qquad
\int_{\{h<s\}}h=C s^2+o(s^2),
\]

so the exact source formula \(\varphi=\int_Sh/\int_S(1-h)\) gives \(\varphi\sim q/2\). This avoids any unjustified differentiation of \(A(t)\sim\sqrt{t/C}\).

In Hessian coordinates \(z=\sqrt q\,H_j^{-1/2}y\), the Taylor expansion gives \(h=q(|y|^2/2+o(1))\), while \(u_0/(\tau q)\to0\). Together with \(d\sigma=q(\det H_j)^{-1/2}(1+o(1))dy\) and \(\tau q^2\to1/C\), this proves both the parabolic-cap profile and its local mass coefficient.

The verification artifact was executed on the exactly quadratic radial reduction. It checks \(C\tau q^2=1\), \(\tau=t+A\), and the exact identity \(A'=\varphi=q/(2-q)\), and confirms the normalized ratios approach one.

## Adversarial checks

The result is restricted to the source's D=infinity slow-limit system. The corresponding finite-D limit has a spatially dependent auxiliary field, so the scalar reduction through \(A(t)\) is not available in the same form; no finite-D rate is claimed.

The coefficient \(C\) is written for the normalized gap \(h=(g_{\max}-g)/g_{\max}\), not for the unnormalized gap used in part of Section 4 of the source. This normalization is essential for the stated constants. The determinant mass weights are invariant under the common rescaling and agree with the source.

Continuous nonnegative \(u_0\) need not be positive near a maximum. This does not alter the leading law because \(u_0/\tau=o(q)\), and \(\{h<q\}\subset\{u>0\}\) holds from \(u_0\ge0\). The support statement is local near each maximum and does not assume a pre-existing positive component there.

The \(t^{-1/4}\) exponent is not presented as a generic free-boundary novelty. It is the source-specific temporal scale forced by the two-dimensional quadratic Morse geometry and fixed mass in this slow-limit dynamics.

## Originality

PASS, to the best of our knowledge.

The full arXiv:2609.20609v1 text was inspected, including its slow-limit system, representation formula, monotonicity and concentration theorem, distribution-of-limit-measures theorem, and the nondegenerate-minimum computation in Section 4. The source gives determinant weights for limiting mass but does not state a temporal localization rate, a t^{-1/4} shrinking law, a t^{1/2} peak law, a t^{-1/2} multiplier gap, or a rescaled parabolic-cap dynamical profile.

Searches using the exact title and arXiv identifier together with `localization rate`, `t^{-1/4}`, `parabolic cap`, `profile`, `nondegenerate maxima`, and equivalent cell-polarization/free-boundary terminology did not locate a public correction, follow-up, or prior source-specific derivation of these asymptotics.

The closest prior work is arXiv:2605.03553v1 by Flores Sepulveda--Niethammer--Velazquez. It studies the small-mass stationary elliptic obstacle problem. For Morse maxima it proves an elliptic free-boundary limit and an explicit obstacle profile; in the radial quadratic case the profile is quartic inside the support. Elliptic support geometry near Morse maxima is therefore excluded from the originality claim. The present claim is the temporal rate and parabolic-cap profile for the different zero-diffusion slow-time limit introduced in arXiv:2609.20609v1.

The 2021 SIAM paper establishes the obstacle-type model, well-posedness, contraction and stability of steady states. The 2023 CPDE paper studies support continuity and jumps, and the 2025 interface paper studies interface regularity and short-time oscillation phenomena. These are also excluded from the originality claim.

The source preprint is very recent, so an unindexed author revision, note, or discussion is the main residual originality risk. No inaccessible paper emerged from the search as a particularly plausible source of the same slow-limit rate/profile theorem.

## Value

PASS.

The source's main long-time conclusion for the slow-limit system is qualitative concentration plus a characterization of limit measures. Under the generic Morse hypothesis, the present result converts that description into a complete leading-order dynamical scaling: an explicit support width, peak height, multiplier relaxation rate, and local shape with constants determined by the Hessians. The profile also explains dynamically why the determinant weights appear.

The distinction from the stationary small-mass obstacle profile is scientifically useful: the same signal Hessian produces an elliptic support geometry in both settings, but the local density profile and scaling exponents are different because one problem is a time-dependent zero-diffusion mass-constrained flow and the other is an elliptic obstacle problem.

## Scope and limitations

The theorem assumes a smooth closed two-dimensional membrane, a time-independent signal with finitely many isolated nondegenerate maxima, and bounded continuous nonnegative unit-mass initial data. It applies to the D=infinity slow-limit system only. Degenerate maxima, moving signal maxima, finite-D slow-limit dynamics, and quantitative error bounds for the original positive-mass parabolic PDE are not covered.
