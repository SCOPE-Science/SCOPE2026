# The claimed Bertrand stability boundary misses a second stable ray segment
## Finding
For the heterogeneous dynamic Bertrand price map of Guo and Song (2025), take
\[
a=1,\qquad b=\frac12,\qquad c_1=c_2=2,\qquad d_1=d_2=\frac13,\qquad \beta=\frac12.
\]
These values satisfy the model assumptions \(1>b>d_i\ge 0\), \(a>b\), and \(c_i>0\). The interior Nash equilibrium is
\[
(\bar p_1,\bar p_2)=(3,3),
\]
and both equilibrium demands equal \(1/2\).

Along the equal-adjustment ray \(\alpha_1=\alpha_2=t>0\), substitution into the paper's Jacobian gives
\[
J(t)=\begin{pmatrix}
1-3t & t\\
t\left(1-\frac32t\right) & 1-3t+\frac12t^2
\end{pmatrix}.
\]
Its trace and determinant are
\[
\operatorname{tr}J(t)=\frac{t^2-12t+4}{2},\qquad
\det J(t)=\frac{17t^2-12t+2}{2}.
\]
Therefore the three strict Jury inequalities factor exactly as
\[
1+\operatorname{tr}J+\det J=(3t-2)^2,
\]
\[
1-\operatorname{tr}J+\det J=8t^2,
\]
\[
1-\det J=\frac{t(12-17t)}2.
\]
Consequently the equilibrium is locally asymptotically stable on this ray exactly for
\[
0<t<\frac{12}{17},\qquad t\ne\frac23.
\]
At \(t=2/3\), one multiplier is exactly \(-1\), but stability returns immediately afterward and persists on the second interval
\[
\frac23<t<\frac{12}{17}.
\]

For the same parameters, the radial curve stated in Theorem 1 and Remark 2 gives \(t=2/3\) on the diagonal ray. Thus that curve is a sufficient small-adjustment boundary here, but it is not the full stability boundary claimed in Remark 2, the abstract, and the conclusions. The omitted second stable segment is genuine. For example, at \(t=7/10\),
\[
J=\begin{pmatrix}
-\frac{11}{10} & \frac7{10}\\
-\frac7{200} & -\frac{171}{200}
\end{pmatrix},
\]
with
\[
1+\operatorname{tr}J+\det J=\frac1{100},\qquad
1-\operatorname{tr}J+\det J=\frac{98}{25},\qquad
1-\det J=\frac7{200},
\]
so all multipliers lie strictly inside the unit disk although \(7/10>2/3\).

## Assumptions and scope
The claim concerns only local asymptotic stability of the interior Nash equilibrium of the discrete price-adjustment system, under the source paper's linear-demand and cost assumptions. The equality case \(t=2/3\) is nonhyperbolic and is not classified beyond the exact multiplier \(-1\). No claim is made about global convergence, nonlinear dynamics at the flip point, or the numerical parameter sets displayed in the source paper.

The paper itself distinguishes a merely sufficient radial bound from an if-and-only-if statement that requires an additional inequality in Corollary 1. For the parameters used here, that additional inequality fails at \(\beta=1/2\), so the counterexample does not contradict the sufficient part of Theorem 1. It instead shows that the later language identifying that radial curve as the exact stability boundary is too strong without the extra condition.

## Proof
The static first-order conditions are
\[
a+bc_1-2bp_1+d_1p_2=0,\qquad
a+bc_2-2bp_2+d_2p_1=0.
\]
With the stated symmetric parameters, \(p_1=p_2=3\) solves both equations because
\[
1+\frac12\cdot2-2\cdot\frac12\cdot3+\frac13\cdot3=0.
\]
The demand of either firm is
\[
1-\frac12\cdot3+\frac13\cdot3=\frac12>0.
\]

At the interior equilibrium the source paper gives the Jacobian
\[
\begin{pmatrix}
1-2\alpha_1b\bar p_1 & \alpha_1d_1\bar p_1\\
\alpha_2\bar p_2d_2\left(1-2(1-\beta)\alpha_1b\bar p_1\right) &
1+\alpha_2\bar p_2\left((1-\beta)\alpha_1d_1d_2\bar p_1-2b\right)
\end{pmatrix}.
\]
Putting \(\alpha_1=\alpha_2=t\), \(\beta=1/2\), \(b=1/2\), \(d_1=d_2=1/3\), and \(\bar p_1=\bar p_2=3\) yields the displayed \(J(t)\). Direct expansion gives the stated trace and determinant. For a real \(2\times2\) discrete-time Jacobian, strict Schur stability is equivalent to the three Jury inequalities
\[
1+\operatorname{tr}J+\det J>0,\qquad
1-\operatorname{tr}J+\det J>0,\qquad
1-\det J>0.
\]
Factoring them gives \((3t-2)^2\), \(8t^2\), and \(t(12-17t)/2\). For \(t>0\), the second is always positive; the third is positive exactly when \(t<12/17\); the first is positive except at \(t=2/3\). This proves the exact two-interval stability set.

On the diagonal ray, write \(\alpha_1=\alpha\cos(\pi/4)\), \(\alpha_2=\alpha\sin(\pi/4)\), so \(t=\alpha/\sqrt2\). At \(\beta=1/2\), the source radial formula has \(2\beta-1=0\). With \(\tilde p_1=\tilde p_2=3/\sqrt2\), its discriminant term is zero, and its stated radius is \(\alpha_L=2\sqrt2/3\), equivalent to \(t<2/3\). Hence it omits the stable segment \((2/3,12/17)\).

At \(t=7/10\), exact substitution gives the displayed Jacobian and positive Jury factors. The characteristic discriminant is
\[
\left(\operatorname{tr}J\right)^2-4\det J=-\frac{1519}{40000}<0,
\]
so the multipliers are a complex-conjugate pair with common modulus \(\sqrt{193/200}<1\), an independent check of strict local stability.

## Verification
The accompanying `verifier.py` uses only Python's standard-library `fractions.Fraction`. It reconstructs the equilibrium, demand, symbolic polynomial coefficients of the Jacobian entries, trace, determinant, all three Jury factors, the neutral point \(t=2/3\), and the exact witness \(t=7/10\). It prints `VERIFY_OK` only if every identity and strict inequality succeeds.

## Relationship to prior work
Guo and Song introduce the rationality-level parameter \(\beta\), state the standard two-dimensional Jury criterion, prove a sufficient small-radius stability region for \(1/2\le\beta\le1\), and give an if-and-only-if statement only under an additional condition in Corollary 1. Nevertheless, their abstract, Remark 2, and conclusions describe the radial curve as an exact characterization or boundary of the stable region. The exact diagonal calculation above identifies a parameter regime where the additional Corollary 1 condition does not hold and the stable set is not star-shaped along the ray: it is interrupted only by an isolated flip-neutral point and then becomes stable again.

Earlier heterogeneous-expectations Bertrand work by Fanti and Gori studies a vertically differentiated duopoly and reports flip bifurcations under a different model and expectation structure. It does not imply the exact two-interval stability law derived here for the 2025 rationality-level map.

## Limitations
This result is a local linear-stability correction. It does not determine the nonlinear normal form at \(t=2/3\), the attracting set for unstable parameters, or whether re-entrant stability persists away from the chosen symmetric slice. It also does not invalidate Theorem 1 as a sufficient condition; the correction applies to the paper's stronger claim that the Theorem 1 curve is the complete stability boundary without the extra Corollary 1 hypothesis.

## References
1. M. Guo and Q. Song, “Rationality Levels in a Heterogeneous Dynamic Price Game,” *Axioms* 14(3), 194 (2025), DOI: 10.3390/axioms14030194.
2. L. Fanti and L. Gori, “Stability Analysis in a Bertrand Duopoly with Different Product Quality and Heterogeneous Expectations,” *Journal of Industry, Competition and Trade* 13, 481–501 (2013), DOI: 10.1007/s10842-012-0134-9.
