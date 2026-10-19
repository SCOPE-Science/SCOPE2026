# A sharp sixth-cumulant chirality window for a harmonically trapped circle swimmer

## Finding

For a stationary two-dimensional circle swimmer under a linear harmonic restoring force and deterministic angular torque, the sixth connected cumulant of either Cartesian coordinate has a **complete sharp sign classification**. Write \(b=\kappa/D_r>0\) for trap-to-rotational-diffusion ratio and \(x=(\omega/D_r)^2\geq0\) for squared chirality. There is exactly one \(b_*\in(11/25,9/20)\) at which a pair of chirality-driven sign changes annihilates, with
\[
b_*=0.4475510940308399394\ldots,\qquad x_*=6.835392739927954179\ldots.
\]
For every \(0<b<b_*\) there are precisely two positive numbers \(x_-(b)<x_+(b)\), with the sixth cumulant positive outside the interval and negative strictly inside it. At \(b=b_*\) it is nonnegative, vanishing only at the double root \(x_*\), and for every \(b>b_*\) it is strictly positive for all chirality values. The sign classification remains valid after adding independent translational Brownian forcing of any nonnegative strength.

Define the dimensionless active contribution \(Z=D_r X/v\), where \(X\) is one stationary Cartesian position coordinate and \(v>0\) is self-propulsion speed. The exact cumulant is
\[
\operatorname{cum}_6(Z)=\frac{5Q(b,x)}{4b\big((b+1)^2+x\big)^3\big((b+2)^2+x\big)\big((b+3)^2+x\big)\big((3b+1)^2+x\big)\big((5b+1)^2+x\big)},
\]
with the explicitly determined polynomial
\[
\begin{aligned}
Q(b,x)={}&b x^{4}
 +(36b^{3}+29b^{2}+b)x^{3}\\
&+(294b^{5}+727b^{4}+533b^{3}+153b^{2}+285b+216)x^{2}\\
&+(484b^{7}+3863b^{6}+10439b^{5}+8958b^{4}-6038b^{3}-14997b^{2}-8453b-1392)x\\
&+225b^{9}+3165b^{8}+18739b^{7}+60773b^{6}+117845b^{5}+140183b^{4}\\
&\hspace{2em}+100985b^{3}+41711b^{2}+8734b+696.
\end{aligned}
\]
The critical point is **defined exactly** as the unique solution to \(Q(b,x)=\partial_xQ(b,x)=0\) in \((11/25,9/20)\times(6,8)\). In the weak-confinement limit the two squared-chirality endpoints approach
\[
x_-(b)\longrightarrow\frac{29-2\sqrt{145}}9,\qquad
x_+(b)\longrightarrow\frac{29+2\sqrt{145}}9.
\]

## Assumptions and scope

Let \(v,\kappa,D_r>0\), \(\omega\in\mathbb R\), and \(D\ge0\). The overdamped process satisfies
\[
 d\mathbf R_t=(-\kappa\mathbf R_t+v(\cos\Theta_t,\sin\Theta_t))\,dt+\sqrt{2D}\,d\mathbf W_t,
 \qquad d\Theta_t=\omega\,dt+\sqrt{2D_r}\,dB_t\pmod{2\pi}.
\]
The two Brownian drivers are independent, and the orientation marginal is uniform at stationarity. The stable linear dynamics has a unique stationary distribution. The univariate sixth cumulant means \(\operatorname{cum}_6(X)=\mathbb E[X^6]-15\mathbb E[X^4]\mathbb E[X^2]+30(\mathbb E[X^2])^3\); reflection and rotational invariance ensure centering. Coordinates are arbitrary orthogonal projections of the stationary vector; no claim is made about radial sixth cumulants or finite-time cumulants.

## Proof

Scale time by \(D_r\) and position by \(D_r/v\). The activity-only coordinate obeys \(dZ_t=(-bZ_t+\cos\Theta_t)dt\) with angular drift \(u=\omega/D_r\) and angular diffusivity one. Its unique stationary realization is the absolutely convergent integral \(Z_t=\int_{-\infty}^{t}e^{-b(t-s)}\cos\Theta_s\,ds\). It is bounded by \(1/b\), justifying all stationary generator identities.

For integer \(n\ge0\) and \(j\in\mathbb Z\), put \(m_{n,j}=\mathbb E[Z^ne^{ij\Theta}]\). Uniform stationary orientation gives \(m_{0,0}=1\), \(m_{0,j}=0\) for nonzero \(j\). Applying the generator to \(Z^ne^{ij\Theta}\) and using \(\cos\Theta=(e^{i\Theta}+e^{-i\Theta})/2\), for every \(n\ge1\) gives
\[
(nb+j^2-iju)m_{n,j}=\frac n2\big(m_{n-1,j+1}+m_{n-1,j-1}\big).
\]
For each fixed \(n\), only \(|j|\le n\) of matching parity are needed. Since \(nb+j^2>0\) the recursion is nonsingular. Repeated substitution for \(n=2,4,6\), together with \(m_{n,-j}=\overline{m_{n,j}}\), gives \(\mathbb E[Z^2]=(b+1)/(2b((b+1)^2+x))\) and, after the connected-cumulant subtraction, the displayed rational expression for \(\operatorname{cum}_6(Z)\). The included independent symbolic executable constructs these finite recursions rather than presupposing the final rational expression, and proves algebraic equality by exact cancellation. Every denominator factor is strictly positive on the stated domain, so the sign is the sign of \(Q\).

Write \(Q=\sum_{j=0}^4q_j(b)x^j\). The constant coefficient \(q_0\) and coefficients \(q_2,q_3,q_4\) are strictly positive for \(b>0\). Consequently \(\partial_x^2Q>0\) for all \(b,x>0\). The boundary polynomial is \(Q(0,x)=24(9x^2-58x+29)\), giving exactly two simple positive roots. Since \(Q(b,0)>0\), \(Q(b,x)\to+\infty\) as \(x\to\infty\), and strict convexity permits at most two positive roots, their count can change only at a positive double root.

To locate all possible collisions exactly, form \(R(b)=\operatorname{Res}_x(Q,\partial_xQ)\). The finite algebraic calculation yields
\[
R(b)=-49152 b^2(b+1)^4 F(b),
\]
where the primitive factor \(F\) is an explicit integer polynomial of degree 23, deterministically constructed from the displayed \(Q\). Sturm's exact sign-variation algorithm gives **one** real zero of \(F\) on \((0,1/2)\), and exactly one on \((11/25,9/20)\); the included executable independently recomputes and counts these zeros over the rational numbers. To rule out any additional positive-root transitions at higher confinement, let \(q_1\) denote the linear coefficient of \(Q\). Exact expansion gives \(4q_0q_2-q_1^2=(b+1)^3S(b)\), where every coefficient of the shifted polynomial \(S(t+1/2)\) is strictly positive. Thus \(q_0+q_1x+q_2x^2>0\) for every \(x\ge0\) and \(b\ge1/2\), and the remaining \(q_3x^3+q_4x^4\) terms are nonnegative. An exact Sturm count finds two positive roots at \(b=1/10\) and none at \(b=1/2\). Continuity and the unique possible collision in \((0,1/2)\) force the claimed two-root, double-root, and zero-root regimes. Strict convexity forces the double root to be unique. The defining rational isolating rectangle and the printed approximate values can be checked by exact sign tests and arbitrary-precision root refinement.

The two weak-trap endpoint limits follow by continuity of simple roots of \(Q(0,x)\). Moreover,
\[
\lim_{b\downarrow0}b\operatorname{cum}_6(Z)=\frac{30(9x^2-58x+29)}{(x+1)^5(x+4)(x+9)}.
\]
Finally, translational Brownian forcing contributes a stationary independent centered Gaussian Ornstein–Uhlenbeck coordinate. Gaussian independent summands have identically zero cumulants of order at least three, so the sixth cumulant is unchanged. Rotational invariance transfers the one-coordinate result to every Cartesian direction.

## Verification

Execute `python verify_sixth.py` with Python 3 and SymPy. It reconstructs the exact Fourier-generator recursion through degree six; independently simplifies the sixth and fourth cumulant identities; checks the strict-convexity coefficient conditions, degree-23 resultant factorization and exact Sturm counts; certifies the positive shifted-polynomial coefficients for the \(b\ge1/2\) exclusion; checks sample positive-root counts and the weak-trap limits; and computes the numerical critical coordinates. Every assertion passed in the packaged execution. Exact polynomial operations certify the all-parameter claims; the numerical approximations alone do not.

## Relationship to prior work

Caraglio and Franosch (2022) developed an exact spectral solution for an active Brownian particle in a harmonic well without deterministic chirality. Frydel (2023) gave recurrence methods for an active oscillator. Pattanayak and coauthors (2025) analyzed **this same torque-driven confined circle-swimmer model**, developed arbitrary-moment machinery and explicit steady-state **fourth** cumulants, including a reentrant non-Gaussianity phenomenon. Pattanayak and coauthors (2026) analyzed time-dependent moments up to fourth order of the same model. Those models, recurrence methods, and fourth-cumulant transitions are prior art. The present claim is **only** the closed rational sixth coordinate cumulant and the sharp, single-cusp all-parameter classification of its pair of sign changes, including the weak-trap endpoint constants. Higher-moment generating machinery in those articles can in principle recover this expression; the contribution is a new evaluated invariant and rigorous global phase classification, not a new general solution method or discovery of reentrance itself.

## Limitations

The result is restricted to planar, linearly trapped active Brownian particles with constant angular drift and uniform rotational diffusion, at stationarity. It does not imply that a vanishing sixth cumulant makes the distribution Gaussian. It does not establish higher-dimensional, nonlinear-trap, interacting-particle, finite-time, or experimentally estimated phase diagrams. Published general moment frameworks may implicitly subsume algebraic ingredients, and an independent mathematical-priority audit has not been performed. In particular, the separate 2024 torque paper was checked at the abstract level but not its full technical appendix, and any unavailable supplementary materials of closely related work remain a priority risk.

## References

1. M. Caraglio and T. Franosch, *Analytic Solution of an Active Brownian Particle in a Harmonic Well*, Physical Review Letters 129, 158001 (first public 2022-10-07), DOI 10.1103/PhysRevLett.129.158001; arXiv:2210.04205.
2. D. Frydel, *Active oscillator: recurrence relation approach* (2023), arXiv:2312.05406.
3. A. Pattanayak et al., *Chirality, confinement and dimensionality govern re-entrant transitions in active matter* (2025), arXiv:2509.03448.
4. A. Pattanayak et al., *Exact dynamics and dimensional effects in torque-driven trapped active Brownian particles* (2026), arXiv:2603.26967.
5. A. Pattanayak et al., *Impact of chirality on active Brownian particle: exact moments in two and three dimensions* (2024), arXiv:2404.09650 (abstract-level comparison only).
