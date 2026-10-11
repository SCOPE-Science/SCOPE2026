# Complete prime-period-two spectrum and the sharp sink boundary of the Duffing map

## Finding

For the classical planar Duffing (Holmes) map
\[
F_{a,b}(x,y)=(y,ay-y^3-bx),\qquad a\ge0,\quad 0<b<1,
\]
write \(B=1+b\) and
\[
a_*(b)=\sqrt{\frac{9(1+b)^2+(1-b)^2}{2}}.
\]
There is one antipodal prime-period-two orbit for every \(a\ge0\). It is always a hyperbolic saddle. There are exactly two further prime-period-two orbits if and only if \(a>2B\). These are exchanged by simultaneous coordinate negation, and each is a hyperbolic sink precisely when
\[
2(1+b)<a<a_*(b).
\]
At the upper endpoint the two return multipliers are exactly \(-1\) and \(-b^2\). Above it, the two cycles are hyperbolic saddles. In particular at \(b=1/5\) the upper endpoint is \(\sqrt{34/5}=2.607680962\ldots\), which separates the continued existence of attracting period-two cycles from their first linear flip instability; it is not a claim about global attractor basins or other periods.

## Assumptions and scope

All dynamics occur on the real plane. The parameter domain is \(a\ge0\) and \(0<b<1\). A prime-period-two orbit means a pair of distinct points \(P,Q\) satisfying \(F(P)=Q\) and \(F(Q)=P\); cyclic relabeling does not create a second orbit. A sink has both eigenvalues of the return matrix \(DF^2\) strictly inside the unit circle; a hyperbolic saddle has one inside and one outside. No claims are made outside the given parameter domain or about period-four and higher orbits. The stability statement at the neutral endpoint is only spectral.

## Proof

Write \(F(u,v)=(v,\,av-v^3-bu)\). An orbit of prime period two can be represented by \((u,v)\leftrightarrow(v,u)\), so its defining equations are
\[
(1+b)u=av-v^3,\qquad(1+b)v=au-u^3.
\]
Factoring their sum and difference gives, exactly,
\[
(u+v)[u^2-uv+v^2-(a-B)]=0,
\]
\[
(u-v)[u^2+uv+v^2-(a+B)]=0.
\]
The case \(u=v\) is a fixed point, so it is excluded. If \(u=-v\ne0\), the second equation becomes \(u^2=a+B\). Because \(a+B>0\), this gives exactly one antipodal prime-period-two orbit (modulo cyclic relabeling). For every remaining orbit, both factors \(u+v\) and \(u-v\) are nonzero; hence subtraction and addition of the bracket equations yield
\[
uv=B,\qquad u^2+v^2=a.
\]
As \(B>0\), both coordinates have the same sign. The real solutions exist with \(u\ne v\) if and only if \(a>2B\), since \((u-v)^2=a-2B\). The two positive coordinates (ordered with \(u>v\)) are
\[
u=\frac{\sqrt{a+2B}+\sqrt{a-2B}}{2},\qquad
v=\frac{\sqrt{a+2B}-\sqrt{a-2B}}{2}.
\]
Their sign reversal yields one other cycle. Swapping \(u\) and \(v\) merely advances the phase. This exhausts every prime-period-two orbit, including parameter boundaries. At \(a=2B\), the positive and negative solutions coalesce respectively with fixed points; there are no additional prime-period-two orbits at equality.

The derivative matrix is
\[
DF(x,y)=\begin{pmatrix}0&1\\-b&a-3y^2\end{pmatrix},\qquad \det DF=b.
\]
The derivative of a two-step return always has determinant \(b^2\), and along the pair \((u,v),(v,u)\) its trace equals
\[
\tau=(a-3u^2)(a-3v^2)-2b.
\]
For either non-antipodal cycle, substituting \(u^2+v^2=a\) and \(u^2v^2=B^2\) gives
\[
\tau=-2a^2+9B^2-2b.
\]
Since \(0<b<1\), the quadratic characteristic polynomial \(\lambda^2-\tau\lambda+b^2\) has both roots strictly inside the unit circle if and only if \(-1-b^2<\tau<1+b^2\). This follows equivalently from the elementary quadratic Schur/Jury test: \(1-b^2>0\), \(1-\tau+b^2>0\), and \(1+\tau+b^2>0\). At \(a=2B\), the trace is \(1+b^2\); it decreases strictly as \(a\) increases. Its first crossing of \(-1-b^2\) is at
\[
a=a_*(b)=\sqrt{[9B^2+(1-b)^2]/2}.
\]
Indeed \(a_*(b)^2-4B^2=1+b^2>0\), so this upper endpoint always lies strictly above the orbit-creation threshold. For \(2B<a<a_*\), both non-antipodal cycles are sinks. At \(a=a_*\), the characteristic polynomial factors as \((\lambda+1)(\lambda+b^2)\). For \(a>a_*\), its trace is less than \(-1-b^2\), so one eigenvalue is below \(-1\) and the other lies in \((-1,0)\): a hyperbolic saddle.

For the antipodal cycle, \(u^2=v^2=a+B\), so
\[
\tau_{\mathrm{anti}}=(-2a-3B)^2-2b.
\]
For \(a\ge0\), \(\tau_{\mathrm{anti}}\ge9B^2-2b>1+b^2\). The return polynomial has one real root greater than \(1\), and its other root is in \((0,1)\), so the antipodal orbit is always a hyperbolic saddle. There can be no fourth prime-period-two orbit by the exhaustive factorization above.

## Verification

The accompanying independent finite-precision checker `check_duffing.py` evaluates the explicit orbit formulas against two map iterates, checks return traces and determinant, and probes both sides of the sharp stability threshold for multiple parameter values. It supplies reproducible numerical stress tests; the exhaustive result for all real parameters follows from the algebraic factorization and exact inequalities in the proof, not from finite experiments. The exact specialization at \(b=1/5\) gives \(a_*^2=34/5\).

## Relationship to prior work

Kraut and Grebogi (2004, first public arXiv submission on 2004-11-30) use the classical Holmes map to compare noise robustness of chaotic attractors. The later open-access treatment by Coomes, Koçak, and Palmer (2026), Example 3.2, discusses precisely the same planar cubic map, its reflection symmetry, pitchfork at \(a=1+b\), and the period-two branch born at \(a=2(1+b)\). It reports parameter windows and coexistence near \(b=0.2\) numerically, but does not supply the exact complete prime-period-two orbit count or the upper stability boundary as a closed two-parameter formula. The 2017 analysis by Chen, Wang, and Li reports local fixed-point bifurcation conditions and Marotto chaos, but its complete text could not be materially compared, leaving a literature-overlap risk. A separately studied recurrence \((x,y)\mapsto(y,ax-x^3-by)\) has a different second-order update and state-dependent Jacobian determinant; it is not the same formula as the present map and its invariant-measure statements do not imply the two-cycle classification.

## Limitations

The upper boundary refers to linear stability of the two non-antipodal prime-period-two cycles; it does not certify a period-four orbit at equality or exclude other coexisting attractors. Nonlinear behavior exactly at the flip endpoint, basin geometry, and periods exceeding two are outside scope. Earlier historical material may contain an equivalent stability formula under a different parameter normalization; the survey here does not prove global uniqueness of the statement. Full text of the 2004 Kraut–Grebogi preprint and the 2017 Chen–Wang–Li paper was not successfully retrieved for line-by-line comparison. The explicit parameter date is that of the earliest day-verified preprint examined; older historical descriptions exist without independently resolved first-public calendar days.

## References

1. S. Kraut and C. Grebogi, *Stability Properties of Nonhyperbolic Chaotic Attractors under Noise*, arXiv:nlin/0411064, initially posted 2004-11-30, https://arxiv.org/abs/nlin/0411064.
2. B. Coomes, H. Koçak, and K. J. Palmer, *A Computable Criterion for the Existence of Homoclinic Tangencies*, Journal of Dynamics and Differential Equations (2026), DOI:10.1007/s10884-026-10533-y, https://link.springer.com/article/10.1007/s10884-026-10533-y, Example 3.2.
3. Z. Chen, J. Wang, and Y. Li, *Analysis on Bifurcation and Chaos of Two-Dimensional Discrete Duffing-Holmes System*, Journal of Dynamics and Control 15 (2017), 324–329, DOI:10.6052/1672-6553-2017-011.
4. M. Cross, *Two Dimensional Maps – Equations*, Caltech course page, https://www.its.caltech.edu/~mcc/Chaos_Course/Map2D_docs/Equations.html.
