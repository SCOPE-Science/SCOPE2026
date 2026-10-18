# Exact pole–branch transition for radial zeros of polynomial-power derivatives

## Finding
Let \(d\ge3\) be an integer and \(0<\alpha<d\). For integers \(0\le m_n<dn\) with \(m_n/n\to\alpha\), form the normalized zero-counting measure of \(\frac{\mathrm d^{m_n}}{\mathrm dz^{m_n}}(z^d-1)^n\) and push it forward by \(t=z^d\). These probability measures converge to a measure \(\nu_{d,\alpha}\) on \([0,1]\) having the complete sharp support and phase diagram described below.

Put
\[
T=\frac{\alpha(d-\alpha)^{d-1}}{(d-1)^{d-1}},\qquad
\kappa=\frac{\alpha(d-\alpha)^{d-1}}{d^d},\qquad
\beta=\frac{d-\alpha}{\alpha}.
\]
The absolutely continuous part has strictly positive density on \((0,T)\) and zero density outside \([0,T]\). When \(0<\alpha<1\) there is, in addition, exactly one atom, at \(t=1\), of mass \(d(1-\alpha)/(d-\alpha)\). For \(1\le\alpha<d\) there are no atoms. Thus the exact support is \([0,T]\cup\{1\}\) for \(\alpha<1\), and \([0,T]\) for \(\alpha\ge1\).

The complete limiting moment generating function is
\[
M(s)=\int\frac{\mathrm d\nu_{d,\alpha}(t)}{1-st}
=\frac{1+y(s)}{1-\beta y(s)},\qquad
 y=\kappa s(1+y)^d,\quad y(0)=0.
\]
Equivalently, for every integer \(k\ge1\),
\[
\int t^k\,\mathrm d\nu_{d,\alpha}(t)
=\frac{d\kappa^k}{\alpha k}
\sum_{j=0}^{k-1}(j+1)\beta^j\binom{dk}{k-1-j}.
\]
In particular the first moment is \(((d-\alpha)/d)^{d-1}\).

The three endpoint laws (for the continuous density \(f_{d,\alpha}\)) are
\[
f_{d,\alpha}(t)\sim\frac{\sin(\pi/d)}{\pi}
\left(\frac{\alpha}{d-\alpha}\right)^{1-1/d}t^{1/d-1}
\qquad(t\downarrow0),
\]
\[
f_{d,\alpha}(t)\sim\frac{\alpha\sqrt{2(d-1)/d}}
{\pi(\alpha-1)^2T^{3/2}}\sqrt{T-t}
\qquad(t\uparrow T,\ \alpha\ne1),
\]
and, at the collision parameter \(\alpha=1\), \(T=1\) and
\[
f_{d,1}(t)\sim\frac{1}{\pi}\sqrt{\frac{d}{2(d-1)}}(1-t)^{-1/2}
\qquad(t\uparrow1).
\]
In the original \(z\)-plane the limiting support comprises the \(d\) radial segments of length \(T^{1/d}\), with the \(d\) outer roots of unity additionally present when \(\alpha<1\).

## Assumptions and scope
The degree \(d\) is a fixed integer at least three; \(\alpha\) is fixed strictly between zero and \(d\); each derivative order \(m_n\) is an integer satisfying the stated asymptotic ratio. Zeros are counted with multiplicities and divided by the remaining degree \(dn-m_n\). The pushforward variable \(t=z^d\) is real and nonnegative on each radial zero ray. The endpoint asymptotics fix \(d,\alpha\) before taking the spatial limit; uniform claims near \(\alpha=0,1,d\) are not made.

## Proof
**Finite-level radial confinement.** Every derivative has the form \(z^r Q(z^d)\) with \(0\le r<d\), where \(Q\) has real zeros in \([0,1]\). Initially this follows from \((z^d-1)^n\). If \(r>0\), differentiation sends \(z^r Q(z^d)\) to \(z^{r-1}(rQ(t)+dtQ'(t))\). The positive zeros of the latter polynomial interlace those of \(Q\), by Rolle's theorem applied to \(t^{r/d}Q(t)\) on \((0,\infty)\), including endpoint multiplicities by continuity. If \(r=0\), differentiation instead gives \(dz^{d-1}Q'(t)\). Induction proves confinement. All nontrivial \(t\)-zeros therefore lie in \([0,1]\). The residual multiplicity at \(z=0\) never exceeds \(d-1\), so it cannot create a limiting atom.

**Limiting algebraic transform.** The fixed-ratio convergence theorem of Hägg and Shapiro [1, Theorem 1.1] applies also when \(P'\) has a repeated zero, as it does here. Its selected-saddle Cauchy-transform identity [1, Proposition 3.5] specializes, for \(P(w)=w^d-1\), to
\[
 z=F_\alpha(w)=\frac{d-\alpha}{d}w+\frac{\alpha}{d}w^{1-d},\qquad
 C_\mu(z)=\frac{dw^{d-1}}{(d-\alpha)(w^d-1)},
\]
where \(w(z)\sim dz/(d-\alpha)\) at infinity. Cyclic symmetry yields \(C_\mu(z)=z^{d-1}C_\nu(z^d)\). With \(t=z^d\) and \(v=z/w\), substitution gives
\[
 t(dv-(d-\alpha))=\alpha v^d,
 \qquad C_\nu(t)=\frac{\alpha v}{(d-\alpha)t(1-v)},
 \qquad v(\infty)=\frac{d-\alpha}{d}.
\]
The solution is the branch selected by analytic continuation from infinity in the upper half-plane. In particular, these identities determine the actual limiting probability measure, not a merely formal algebraic solution.

**Support, density, and atoms.** On the positive real axis the inverse relation is \(t(v)=\alpha v^d/(dv-(d-\alpha))\). On the real branch emerging from infinity, \(v\) increases from \((d-\alpha)/d\) to \(v_c=(d-\alpha)/(d-1)\); the inverse relation decreases from infinity to its unique positive critical value \(T=t(v_c)\), equal to the asserted expression. The only other potential real-axis singularity of the selected Cauchy transform is the pole at \(v=1\), which is attained at \(t=1\) on this branch precisely when \(\alpha<1\). Expanding implicitly there gives a Cauchy-transform residue \(d(1-\alpha)/(d-\alpha)\). When \(\alpha=1\), this pole meets the square-root branchpoint and has zero residue; for \(\alpha>1\), it lies beyond the selected branch.

There are no other nonzero finite critical values of the inverse algebraic relation: the derivative of \(t(v)\) vanishes, for \(v\ne0\), only at \(v_c\). Thus the selected branch continues analytically through every positive interval above \(T\), apart from the stated atom. Across \((0,T)\) it has distinct complex-conjugate boundary values, since a real continuation would require another critical value. The Möbius expression for \(C_\nu\) is nonreal whenever \(v\) is nonreal there; by Stieltjes inversion its density
\[
 f_{d,\alpha}(t)=-\frac1\pi\operatorname{Im}
 \frac{\alpha v(t+i0)}{(d-\alpha)t[1-v(t+i0)]}
\]
is strictly positive on the entire open interval. No singular continuous component occurs there, because the branch is analytic with nonzero finite boundary jump on compact subintervals. Near \(t=0\) its singularity is weaker than a simple pole, ruling out an atom. Analytic continuation and compact support therefore give exactly the claimed support and atom classification.

**Moments.** Write \(v=c(1+y)\), where \(c=(d-\alpha)/d\). The algebraic equation becomes \(y=\kappa s(1+y)^d\) with \(s=1/t\). Then the coefficient of \(t^{-1}\) in the Cauchy transform is \(M(s)=(1+y)/(1-\beta y)\). Lagrange inversion yields the displayed finite binomial-sum formula. Since the measures are supported in \([0,1]\), all coefficients are genuine moments and uniquely determine their law.

**Exact endpoint constants.** As \(t\downarrow0\) on the upper-bank boundary, \(v\sim[(d-\alpha)/\alpha]^{1/d}e^{-i\pi/d}t^{1/d}\). Stieltjes inversion gives the hard-edge constant. At \(v_c\), the exact second derivative is \(t''(v_c)=Td(d-1)/v_c^2\), so \(v=v_c-i v_c\sqrt{2(T-t)/(Td(d-1))}+O(T-t)\). If \(\alpha\ne1\), the Cauchy-transform denominator stays nonzero and the density vanishes with the displayed square-root coefficient. At \(\alpha=1\), \(v_c=1\) instead, and the same expansion in the reciprocal denominator gives the stated inverse-square-root law. All constants are therefore sharp equivalences, not upper or lower estimates.

## Verification
The coefficient polynomial of each finite descendant, after factoring its residual power of \(z\), is explicitly
\[
Q_{n,m}(t)=\sum_{\ell=\lceil m/d\rceil}^{n}
(-1)^{n-\ell}\binom n\ell\frac{(d\ell)!}{(d\ell-m)!}
 t^{\ell-\lceil m/d\rceil}.
\]
The accompanying checker uses exact integer/rational arithmetic to obtain the first two finite normalized moments from its leading coefficients for dimensions \(2,3,4\), parameters \(1/2,1,3/2\), and powers \(20,100,400\); these approach the first two coefficients of the proposed generating function. Additional algebraic spot checks of the branchpoint and edge constants are described in `VERIFICATION.md`. Numerical checks do not replace the analytic convergence theorem or the branch analysis in the proof.

## Relationship to prior work
Hägg and Shapiro [1] prove fixed-ratio convergence and the general Cauchy-transform/barrier characterization for all polynomials, including repeated critical points. Their Proposition 3.4 already implies the root-of-unity atomic mass and its vanishing at \(lpha=1\); those atomic facts alone are not claimed as new. Their results do not evaluate the complete continuous support profile, moment generating law, three sharp edge constants, or the pole–branch collision mechanism for this family. The older Bøgvad–Hägg–Shapiro treatment [2] gives general saddle equations under a simple-critical-point hypothesis, excluding \(z^d-1\) for \(d\ge3\); its explicit case study is quadratic. Leurs and Van Assche [3] analyze type-I Jacobi–Angelesco polynomials on a star with a distinct orthogonality construction; their displayed limiting Stieltjes equation and endpoint exponents are not those of the present derivative-ratio family. Jalowy, Kabluchko and Marynych [4,5] give broad exponential-profile techniques and detailed classical real-rooted examples; the inspected sections do not supply this complete ratio-dependent regular-polygon derivative law or its phase-critical edge constants. Martínez-Finkelshtein and Rakhmanov [6] give a general Cauchy-transform flow near infinity, rather than this solved physical-branch density. The present limiting measure can nevertheless be viewed as an algebraic Fuss–Catalan-type deformation; such terminology alone does not establish historical priority.

## Limitations
No finite-power rate of convergence, uniformity at the parameter endpoints, or perturbation robustness of the explicit formulas is claimed. The proof invokes the published fixed-ratio convergence and selected-branch result [1], and does not reprove its general contour theory. An exhaustive literature-priority claim is not made; multiple-orthogonal-polynomial and algebraic-distribution literature may contain equivalent representations.

## References
[1] C. Hägg and B. Shapiro, *The full shadow of a polynomial I. The limiting core and the transient set*, arXiv:2610.09602v1 (first public 2026-10-07), https://arxiv.org/html/2610.09602v1, Theorem 1.1 and Proposition 3.5.

[2] R. Bøgvad, C. Hägg and B. Shapiro, *Rodrigues' descendants of a polynomial and Boutroux curves*, Constructive Approximation 59 (2024), 737–798, https://doi.org/10.1007/s00365-023-09657-x (preprint arXiv:2107.05710).

[3] M. Leurs and W. Van Assche, *Jacobi–Angelesco multiple orthogonal polynomials on an r-star*, Constructive Approximation 51 (2020), 353–381, https://doi.org/10.1007/s00365-019-09457-2 (preprint arXiv:1804.07512).

[4] J. Jalowy, Z. Kabluchko and A. Marynych, *Zeros and Exponential Profiles of Polynomials I: Limit Distributions, Finite Free Convolutions and Repeated Differentiation*, Constructive Approximation (2026), https://doi.org/10.1007/s00365-026-09778-z.

[5] J. Jalowy, Z. Kabluchko and A. Marynych, *Zeros and Exponential Profiles of Polynomials II: Examples*, Constructive Approximation (2026), https://doi.org/10.1007/s00365-026-09775-2.

[6] A. Martínez-Finkelshtein and E. A. Rakhmanov, *Flow of the zeros of polynomials under iterated differentiation*, arXiv:2408.13851 (2024).
