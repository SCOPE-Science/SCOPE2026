# Sharp reciprocal two-cycle stability window for a variable-step three-step multistep formula

## Finding
For the BDFL2 variable-step method defined below, let successive step ratios alternate \(t,1/t\) for any \(t>0\). Put
\[
y_* = \frac{5+\sqrt{221}}4,\qquad t_* = \frac{y_*-\sqrt{y_*^2-4}}2.
\]
The exact homogeneous recurrence is zero-stable if and only if \(t_*\le t\le t_*^{-1}\). Its two parasitic Floquet multipliers are strictly inside the unit disk if and only if \(t_*<t<t_*^{-1}\). At the two boundary ratios one simple parasitic multiplier equals \(-1\); outside the closed interval one has modulus greater than one. For every \(t_*<t<1/4\), the periodic recurrence is stable despite one of its two frozen-coefficient recurrences being unstable. The same phenomenon holds for \(4<t<t_*^{-1}\).

## Assumptions and scope
The model is the homogeneous scalar test equation \(u'=0\) in exact arithmetic, using the BDFL2 coefficients in Jensen, Lóczi, and Ketcheson (2026). Set the positive step ratio \(w_n=h_n/h_{n-1}\) and previous ratio \(v_n=w_{n-1}\). For a sequence of three past solution values, the source's homogeneous companion map is
\[
C(w,v)=\begin{pmatrix}3/2&-a_1(w,v)&-a_0(w,v)\\1&0&0\\0&1&0\end{pmatrix},
\]
where
\[
a_0(w,v)=\frac{v^2(2w^2-2w-1)}{4v(w+1)+2},\qquad
 a_1(w,v)=\frac{v^2(-2w^2+2w+1)+2v(w+1)+1}{4v(w+1)+2}.
\]
Only the alternating two-cycle \(w_n=t,1/t,t,1/t,\ldots\) is claimed. Zero-stability means boundedness of all powers of the two-step monodromy matrix, equivalently the root condition with every unit-modulus eigenvalue semisimple. The constant-solution eigenvalue \(1\) is always present.

## Proof
Let \(M(t)=C(t,t^{-1})C(t^{-1},t)\). Since every companion map fixes the constant vector \((1,1,1)^{\mathsf T}\), the monodromy polynomial factors as
\[
\det(\lambda I-M(t))=(\lambda-1)(\lambda^2-S(t)\lambda+P(t)),
\]
where direct multiplication gives
\[
S(t)=-\frac{6t^4+2t^3-21t^2+2t+6}{4t(2t+3)(3t+2)},\qquad
P(t)=-\frac{(t^2+2t-2)(2t^2-2t-1)}{4t(2t+3)(3t+2)}.
\]
For a real monic quadratic \(\lambda^2-S\lambda+P\), both roots lie strictly inside the unit disk if and only if \(1-P>0\), \(1-S+P>0\), and \(1+S+P>0\). The first two expressions simplify to
\[
1-P(t)=\frac{2t^4+26t^3+43t^2+26t+2}{4t(2t+3)(3t+2)}>0,
\]
\[
1-S(t)+P(t)=\frac{(t+1)^2(t^2+4t+1)}{t(2t+3)(3t+2)}>0
\]
for every \(t>0\). The remaining inequality is
\[
1+S(t)+P(t)=-\frac{4t^4-10t^3-41t^2-10t+4}{2t(2t+3)(3t+2)}>0.
\]
Set \(y=t+t^{-1}\ge2\). After dividing the numerator by \(t^2\), the decisive inequality is
\[
4y^2-10y-49<0.
\]
Its only root in \([2,\infty)\) is \(y_*=(5+\sqrt{221})/4>2\). Consequently the strict disk condition is equivalent to \(t_*<t<t_*^{-1}\), with \(t_*=(y_*-\sqrt{y_*^2-4})/2\). At equality, exactly one parasitic root is \(-1\). The other parasitic root has modulus smaller than one because the other two strict Jury inequalities remain valid. Also \(1-S+P>0\) excludes a second root equal to \(1\). Thus all unit roots are simple at the two endpoints; the recurrence remains zero-stable there, and is unstable outside the closed interval.

Finally,
\[
a_0(t,t^{-1})=\frac{2t^2-2t-1}{2t(3t+2)}.
\]
When \(0<t<1/4\), one has \(-a_0(t,t^{-1})>1\), because \(1-2t-8t^2>0\). The frozen companion \(C(t,t^{-1})\) has the exact eigenvalue \(1\), and the product of the other two eigenvalues is its determinant \(-a_0(t,t^{-1})>1\). Hence at least one nonprincipal eigenvalue lies outside the unit disk. Intersecting \(t<1/4\) with the strict period-two stability region proves periodic stabilization on \((t_*,1/4)\). Reversing the two steps changes neither the monodromy nonzero spectrum nor zero-stability and replaces \(t\) by \(t^{-1}\), giving \((4,t_*^{-1})\).

## Verification
The checker `check.py` independently reconstructs both companion matrices from rational coefficients, computes the symbolic monodromy invariants, checks the polynomial identities, and tests representative ratios on either side of the sharp boundary. The proof above is algebraic and does not infer universal stability from numerical samples.

## Relationship to prior work
Jensen, Lóczi, and Ketcheson (2026) introduced BDFL2 and analyzed frozen-step-ratio characteristic-root regions, while observing that stability for varying ratios requires studying products of companion matrices. The present theorem supplies the exact complete reciprocal period-two product region, including a stabilization interval in which one frozen matrix is individually unstable. General multistep root conditions and quadratic Schur/Jury conditions are established techniques and are not claimed as original. Other specialized analyses of period-two variable-step multistep coefficients might contain equivalent formulas; that risk remains open.

## Limitations
The theorem is confined to the zero differential equation, BDFL2's stated exact coefficients, and strictly alternating reciprocal positive ratios. It is a sharp periodic zero-stability result, not a bound for arbitrary varying ratios or nonlinear stiff equations. Floating-point rounding and transient matrix norm amplification are not quantified.

## References
- Jensen, Lóczi, and Ketcheson, *Optimized linear multistep methods for stiff problems* (2026), arXiv:2610.22685, particularly the variable-step BDFL2 formulas and Section 6.3 on stability.
