# Exact Floquet transition for a weakly singular two-step periodic oscillator

## Finding
Consider a strictly positive periodic solution of the two-step equation
\[
 x''(t)=\begin{cases}
 a/\sqrt{x(t)},&0<t<T/2,\\
 -b/\sqrt{x(t)},&T/2<t<T,
 \end{cases}
\]
with \(a,b,T>0\), continued with forcing period \(T\). Set \(\beta=b/a\) and \(\beta_*= (3+\sqrt{17})/2\). Such a solution exists uniquely exactly when \(1<\beta<\beta_*\). Along this unique solution, the determinant-one monodromy matrix of the variational equation has exact trace
\[
 \boxed{\operatorname{tr}M(\beta)=-\frac{2(17\beta^4-38\beta^2+17)}{(1+\beta^2)^2}.}
\]
Consequently its two Floquet multipliers are distinct and lie on the unit circle when \(1<\beta<\sqrt{2}\); at \(\beta=\sqrt{2}\) they form a defective double multiplier \(-1\); and for \(\sqrt{2}<\beta<\beta_*\) they are distinct real negative reciprocals, one of modulus greater than one. The spectral threshold is independent of the forcing period and the common forcing-amplitude scale. This is a statement about the **linearized forcing-period map**, not nonlinear Lyapunov stability or creation of a doubled-period orbit.

## Assumptions and scope
The solution is in \(C^1(\mathbb R)\), twice continuously differentiable between switches, bounded strictly away from zero, and satisfies the differential equation almost everywhere (Carathéodory sense). The forcing jumps at integer half-periods; global \(C^2\) regularity at jumps is neither required nor claimed. At a switch the state and first derivative, and also variations of initial data, are continuous. The monodromy \(M\) is the derivative of the time-\(T\) state map on \((x,x')\), evaluated at the periodic state, and does not include a saltation matrix because switch times are prescribed rather than state-dependent.

The first public source for this research direction is Godoy and Zamora (arXiv:1707.04513, first submitted July 14, 2017), whose Example 1 treats precisely the weakly singular two-step forcing. The later uniqueness and existence classification of Cagnetta (arXiv:2610.06068, first submitted October 5, 2026) is used for comparison, not as a claim of novelty for existence or uniqueness.

## Proof
### 1. The positive periodic state and its domain
Write \(s_0=x(0)\), \(s_1=x(T/2)\), and the corresponding velocities \(w_0,w_1\). On the first and second autonomous segments respectively, the conserved energies are
\[
 \tfrac12(x')^2-2a\sqrt{x},\qquad
 \tfrac12(x')^2+2b\sqrt{x}.
\]
Evaluating both at the switches and using periodicity gives \(s_0=s_1=:s\) and \(w_1^2=w_0^2\). Strict positivity makes the acceleration strictly positive during the first segment, so \(w_1>w_0\); hence \(w_0=-v\) and \(w_1=v\) for some \(v>0\). The derivative reverses from \(-v\) to \(v\) in the first segment and from \(v\) to \(-v\) in the second. Energy conservation and time reversal locate the unique minimum at \(T/4\) and maximum at \(3T/4\).

For a velocity coordinate \(z\in[-v,v]\), integration of the autonomous energies yields
\[
 \sqrt{x_+(z)}=\sqrt{s}-\frac{v^2-z^2}{4a},\qquad
 \sqrt{x_-(z)}=\sqrt{s}+\frac{v^2-z^2}{4b}.
\]
These are positive square roots, not signed algebraic branches. Integrating \(dt=\sqrt{x_+(z)}\,dz/a\) on the first segment and \(dt=-\sqrt{x_-(z)}\,dz/b\) in the reverse velocity direction on the second gives
\[
 \frac T4=\frac{v\sqrt{s}}a-\frac{v^3}{6a^2}
 =\frac{v\sqrt{s}}b+\frac{v^3}{6b^2}.
\]
Define \(\xi=v^2/(a\sqrt{s})\) and \(\beta=b/a\). Equating the two half-period expressions determines
\[
 \xi=\frac{6\beta(\beta-1)}{1+\beta^2},\qquad
 s=\left(\frac{T\sqrt a}{4\sqrt\xi(1-\xi/6)}\right)^{4/3},
 \qquad v^2=a\sqrt{s}\,\xi.
\]
The minimum has value \(m=s(1-\xi/4)^2\), provided the **positive-root** requirement \(1-\xi/4>0\) holds, and the maximum equals \(s(1+\xi/(4\beta))^2\). Thus \(\xi>0\) requires \(\beta>1\), and \(\xi<4\) is equivalent to \(\beta^2-3\beta-2<0\), namely \(\beta<\beta_*\). Conversely, for every \(1<\beta<\beta_*\), the displayed \(s,v,m\) yield positive velocity-to-time quadratures; inverting them on each segment, reflecting about the midpoints, and joining the values and velocities constructs a unique positive \(T\)-periodic solution. No strictly positive state exists at either endpoint or outside this open interval. This existence argument is included to identify the domain of the new spectral claim; the general two-step existence and uniqueness problem is also covered by Cagnetta's cited classification.

### 2. Reduction and a fundamental matrix on each forcing step
Rescale \(x=sX\) and time by \(t=s^{3/4}\theta/\sqrt a\). The equation becomes \(X''=hX^{-1/2}\) with first-step \(h=1\), second-step \(h=-\beta\); derivatives in this paragraph are with respect to \(\theta\). At the switches, \(X=1\), and the velocities alternate \(-q,q,-q\), where
\[
 q^2=\xi=\frac{6\beta(\beta-1)}{1+\beta^2},\qquad
 \tau=2q\left(1-\frac{q^2}{6}\right)
\]
is the duration of each normalized forcing step. Constant state-time scaling conjugates the original and normalized linear return matrices, so it leaves the multipliers and trace unchanged.

On a step with constant \(h\), the scalar variational equation is
\[
 y''=-\frac{h}{2X^{3/2}}y.
\]
Two solutions are \(y_1=X'\) (time translation of the autonomous segment) and \(y_2=X-3\theta X'/4\) (differentiate the exact scaling family \(cX(\theta/c^{3/4})\) at \(c=1\)). If the incoming velocity is \(\sigma q\), where \(\sigma\in\{-1,1\}\), the outgoing velocity is \(-\sigma q\). In the coordinate order \((y,y')\), their fundamental matrices at the start and finish of the step are
\[
 Y_{h,\sigma}(0)=\begin{pmatrix}\sigma q&1\\h&\sigma q/4\end{pmatrix},\qquad
 Y_{h,\sigma}(\tau)=\begin{pmatrix}
 -\sigma q&1+3\sigma q\tau/4\\
 h&-\sigma q/4-3h\tau/4
 \end{pmatrix}.
\]
Both have determinant \(q^2/4-h\). These are nonzero for \((h,\sigma)=(1,-1)\) since \(0<q^2<4\), and for \((h,\sigma)=(-\beta,1)\) since \(\beta>0\). Consequently each step derivative equals
\[
 A_{h,\sigma}=Y_{h,\sigma}(\tau)Y_{h,\sigma}(0)^{-1},
 \qquad M=A_{-\beta,1}A_{1,-1}.
\]
No parameter-derivative or discontinuity impulse is omitted: the forcing-switch times are fixed and both state variations are continuous there.

### 3. Trace algebra and the sharp change of spectral type
Substitute the above \(q^2\) and \(\tau\) into the product of the two explicit matrices. Direct rational simplification (also performed exactly by the accompanying `verification/check.py`) gives
\[
 \det M=1,\quad
 \operatorname{tr}M=-\frac{2(17\beta^4-38\beta^2+17)}{(1+\beta^2)^2},\quad
 M_{21}=-\frac{6q(\beta^2-1)}{1+\beta^2}.
\]
Moreover,
\[
 \operatorname{tr}M-2=-\frac{36(\beta^2-1)^2}{(1+\beta^2)^2}<0,
 \qquad
 \operatorname{tr}M+2=-\frac{16(\beta^2-2)(2\beta^2-1)}{(1+\beta^2)^2}.
\]
Since \(\beta>1\), the second expression is positive before \(\beta=\sqrt2\), zero at that value, and negative afterward. For real determinant-one matrices this gives the three spectral alternatives in the Finding. At the threshold the eigenvalue is \(-1\) with algebraic multiplicity two, but \(M_{21}\ne0\), so \(M\ne-I\) and its \(-1\) Jordan block is nontrivial. In particular, the linearized return iterates grow linearly at that parabolic threshold, while they are bounded in the strictly elliptic interval. In the hyperbolic interval one multiplier has modulus greater than one.

## Verification
The standalone `verification/check.py` symbolically reconstructs the two step matrices, reduces the resulting rational identities modulo the relation for \(q^2\), and asserts the trace, determinant, off-diagonal entry, and both sharp trace factorizations. It uses SymPy and no numerical extrapolation. Running `python verification/check.py` from the package root prints the two factorizations and `All exact algebraic checks passed.`

An independent high-accuracy integration of the base and variational equations was also run for forcing ratios \(1.1\), \(1.2\), \(2\), \(3\), and \(3.5\), and agreed with the analytical trace to approximately \(10^{-10}\) (or better). In particular, at \(\beta=2\) the exact trace is \(-274/25\). The symbolic identity and proof, rather than these finite numerical checks, establish the theorem for every admissible ratio.

## Relationship to prior work
Godoy and Zamora, arXiv:1707.04513, Corollary 1 and Example 1, provide a sufficient **existence** bound for weakly singular, two-step periodic forcing, including the inverse-square-root case. Boscaggin, Feltrin and Zanolin, arXiv:2009.00854, Section 4.1 and Proposition 4.2, analyze the weak negative-power regime; they state only a sufficient existence criterion there and explicitly note the absence of a general uniqueness result at the time. Cagnetta, arXiv:2610.06068, reports a subsequent complete **existence/uniqueness** classification for all power exponents and two-step weights. Accordingly, neither uniqueness nor the mere sharp existence interval is presented as new here. The new assertion is the closed Floquet discriminant and its independent sharp threshold inside that existence interval, including the nonsemisimple resonance; this is not implied by knowing the number of periodic solutions.

## Limitations
This result treats the exact equal-duration, two-valued forcing and exponent \(-1/2\). It does not determine nonlinear stability of elliptic solutions, existence of solutions with twice the forcing period, behavior under smoothing of the step discontinuities, or a Floquet classification for other exponents or unequal step durations. The 2026 Cagnetta source was accessible in abstract only during the scientific comparison; the full text could contain an unobserved related stability calculation, so full-text comparison remains a specific residual originality risk. It was not treated as evidence of coverage or noncoverage from snippets alone. At \(\beta=\beta_*\) the positive solution ceases to exist; no monodromy claim is made there.

## References
1. J. Godoy and M. Zamora, *Periodic solutions for indefinite singular equations with applications to the weak case*, arXiv:1707.04513v1 (July 14, 2017), especially Corollary 1 and Example 1. https://arxiv.org/abs/1707.04513
2. A. Boscaggin, G. Feltrin, and F. Zanolin, *Uniqueness of positive solutions for boundary value problems associated with indefinite \(\phi\)-Laplacian type equations*, arXiv:2009.00854v1 (September 2, 2020), especially Section 4.1, Proposition 4.2. https://arxiv.org/abs/2009.00854
3. A. Cagnetta, *A uniqueness result for two-step indefinite \(p\)-Laplacian equations*, arXiv:2610.06068v1 (October 5, 2026), abstract available; full-text comparison outstanding. https://arxiv.org/abs/2610.06068
