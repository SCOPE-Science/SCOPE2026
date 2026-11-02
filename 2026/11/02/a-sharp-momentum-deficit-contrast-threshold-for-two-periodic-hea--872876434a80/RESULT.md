# A sharp momentum-deficit contrast threshold for two-periodic heavy-ball instability

## Finding

**Theorem (complete two-periodic scalar heavy-ball stability and sharp contrast).** Let \(a>0\), \(\eta>0\), and let \(0\le b,c<1\). Apply the deterministic heavy-ball recurrence to the same strongly convex quadratic \(f(x)=a x^2/2\) at every iteration, using alternating momentum \(\beta_{2j}=b\) and \(\beta_{2j+1}=c\):
\[
 x_{k+1}=x_k-\eta a x_k+\beta_k(x_k-x_{k-1}).
\]
Set \(z=\eta a\). All initial pairs \((x_{-1},x_0)\) converge to zero if and only if
\[
 0<z<2+b+c,\qquad F_{b,c}(z):=z^2-(2+b+c)z+2(1+bc)>0.
\]
The full two-step characteristic polynomial is
\[
 \lambda^2-\bigl(1+bc-(2+b+c)z+z^2\bigr)\lambda+bc.
\]
For \(0<z<2+b+c\), write \(u=1-\min\{b,c\}\), \(v=1-\max\{b,c\}\) and \(q=u/v\ge1\). Then:

- When \(q<3+2\sqrt2\), the recurrence is strictly asymptotically stable for *every* \(z\) in that interval.
- When \(q=3+2\sqrt2\), strict stability fails only at \(z=(2+b+c)/2\), where a simple two-step Floquet multiplier is \(-1\).
- When \(q>3+2\sqrt2\), strict stability fails on the *closed* instability band \([z_-,z_+]\), with
\[
 z_\pm=\frac{2+b+c\pm\sqrt{(1-b)^2-6(1-b)(1-c)+(1-c)^2}}2.
\]
At both endpoints the Floquet multipliers are \(-1\) and \(-bc\); in the open band one multiplier is strictly less than \(-1\). The roots satisfy \(0<z_-<z_+<2\), so the open band lies inside a range in which **each momentum value used constantly would be stable**.

The contrast threshold is sharp. For \(b=0\), \(c=9/10\), \(z=3/2\), the prescribed zero-velocity initialization \(x_{-1}=x_0\ne0\) gives
\[
 x_{2j}=(-11/10)^j x_0,
\]
while both of the corresponding constant-momentum algorithms converge. Furthermore, for every \(0<\delta<1/7\), the momentum pair \(b=1-7\delta\), \(c=1-\delta\), with \(z=2-4\delta\), lies strictly inside the unstable band: the absolute contrast \(|b-c|=6\delta\) can tend to zero.

## Assumptions and scope

All numbers are real and all calculations are in exact arithmetic. The objective is fixed, unconstrained, one-dimensional and \(a\)-strongly convex; \(\eta\) is fixed, positive and does not vary with iteration. The only alternating coefficient is momentum. The two-step state is \((x_k,x_{k-1})\). "Strict stability" means convergence of every initial state to the unique minimizer zero, equivalently spectral radius strictly below one for the two-step matrix. The special diverging trajectory uses the usual initial rest convention \(x_{-1}=x_0\). No stochastic gradient is required or considered.

## Proof

For a momentum value \(t\), the state transition is
\[
 T_t(z)=\begin{pmatrix}1+t-z&-t\\1&0\end{pmatrix}.
\]
Over two steps the monodromy is \(M=T_c(z)T_b(z)\). Direct multiplication gives
\[
 \operatorname{tr}M=1+bc-(2+b+c)z+z^2,\qquad \det M=bc.
\]
The characteristic polynomial is \(\lambda^2-(\operatorname{tr}M)\lambda+bc\). Because \(0\le bc<1\), the elementary quadratic Schur criterion states that both roots have modulus strictly less than one exactly when
\[
 1-bc>0,\quad 1-\operatorname{tr}M+bc>0,\quad 1+\operatorname{tr}M+bc>0.
\]
(The criterion follows from mapping the open unit disk to the right half-plane, or from the real quadratic Jury inequalities.) Substitution reduces the last two expressions to
\[
 z(2+b+c-z)>0,\qquad F_{b,c}(z)>0,
\]
proving the first necessary-and-sufficient characterization, including all positive step sizes.

The discriminant of \(F\) is
\[
 \Delta=(2+b+c)^2-8(1+bc)=(1-b)^2-6(1-b)(1-c)+(1-c)^2.
\]
With \(u=1-\min\{b,c\}\ge v=1-\max\{b,c\}>0\), it becomes \(\Delta=v^2(q^2-6q+1)\). The roots of \(q^2-6q+1\) are \(3\pm2\sqrt2\). Since \(q\ge1>3-2\sqrt2\), \(\Delta<0\), \(=0\), or \(>0\) precisely in the three stated contrast regimes. If \(\Delta>0\), the quadratic has minimum below zero at \(z_0=(2+b+c)/2\in(0,2)\), while
\[
 F(0)=2(1+bc)>0,\qquad F(2)=2(1-b)(1-c)>0.
\]
Therefore both distinct roots are strictly between zero and two. At a root \(F(z)=0\), the characteristic polynomial at \(\lambda=-1\) vanishes; its other root is \(-bc\) because their product is \(bc\). That second root has modulus less than one. Inside the root interval \(F(z)<0\); the polynomial at \(-1\) is negative and its value tends to positive infinity at \(-\infty\), forcing one real multiplier below \(-1\). Outside the interval and inside \(0<z<2+b+c\), the three Schur inequalities all hold. At \(\Delta=0\), the same argument gives an isolated simple \(-1\) multiplier at \(z_0\). This proves the global classification and sharpness.

For comparison, a constant momentum \(t\in[0,1)\) has step polynomial \(\lambda^2-(1+t-z)\lambda+t\); the same Schur test gives strict stability exactly when \(0<z<2(1+t)\). Therefore every \(0<z<2\) is stable for either constant momentum \(b\) or \(c\), even though the alternating scheme has the above unstable band.

For the rational witness, set \(b=0\), \(c=9/10\), \(z=3/2\). The zero momentum every even step makes the even subsequence satisfy the exact scalar one-epoch rule
\[
 x_{2(j+1)}=\bigl[(1+c-z)(1-z)-c\bigr]x_{2j}=(-11/10)x_{2j}.
\]
This starts at \(x_0\), so \(x_{2j}=(-11/10)^jx_0\), establishing genuine divergence with zero initial velocity despite individually stable fixed choices.

Finally set \(b=1-7\delta\), \(c=1-\delta\) and \(z=2-4\delta\). For \(0<\delta<1/7\) both momentum values are in \([0,1)\) and \(0<z<2\). Direct substitution gives
\[
 \Delta=8\delta^2>0,\qquad F_{b,c}(z)=-2\delta^2<0.
\]
Thus the alternating method has a multiplier below \(-1\), whereas each constant-coefficient method is stable. Moreover \(|b-c|=6\delta\to0\). This completes the proof.

## Verification

The accompanying `check_periodic_momentum.py` is a self-contained Python standard-library verifier using exact rational arithmetic. Execute `python check_periodic_momentum.py` in the directory containing this document. It checks the two-step matrix trace/determinant, the Schur expressions, the discriminant identity on 6,400 rational triples, the exact zero-velocity divergent trajectory over 36 updates, and the near-equal-momentum construction at five exact rational values. These finite checks support but do not replace the preceding general proof.

## Relationship to prior work

Andreyev, Ananthkumar, Walden, Poggio, and Beneventano (arXiv:2604.14108v1, first public 2026-04-15) analyze momentum-dependent stability of stochastic gradient methods, including exact scalar bounds for **constant** momentum in Section 4.1 and Appendix B. Setting gradient noise to zero yields the familiar constant-coefficient stability interval, but it does not determine products of distinct per-step momentum matrices.

Pasechnyuk-Vilensky (arXiv:2610.09912v1) analyzes the heavy-ball method for arbitrary **fixed** tunings and nonlinear strongly convex functions. Its constant-momentum polynomial and quadratic stability condition agree with the fixed-parameter comparison above, but do not imply the alternating-coefficient Floquet region or the universal deficit-ratio threshold. Jin and Huang (arXiv:2404.03218v1) define an adaptive-momentum heavy-ball method for inverse problems with particular parameter-selection conditions; those conditions do not establish stability under arbitrary prescribed period-two coefficients. Elementary Floquet and Jury theory provide tools used here, but are not claimed as new.

## Limitations

The classification is exact for two-periodic scalar *deterministic* momentum, with \(0\le b,c<1\), positive fixed step and a fixed positive quadratic Hessian. It neither claims a universal failure of well-designed adaptive momentum schemes nor a high-dimensional nonquadratic/stochastic convergence theorem. The instability example is a worst-case choice of momentum scheduling and step size. The algebraic tools are classical, and an equivalent special-case formula could occur in older switched-system or discrete-Hill literature; exhaustive priority confirmation is not claimed. Independent mathematical audit has not been performed.

## References

1. Arseniy Andreyev, Advikar Ananthkumar, Marc Walden, Tomaso Poggio, and Pierfrancesco Beneventano, *Momentum Further Constrains Sharpness at the Edge of Stochastic Stability*, arXiv:2604.14108v1 (2026), https://arxiv.org/html/2604.14108v1 .
2. Dmitry Pasechnyuk-Vilensky, *Two Answers on Heavy-Ball Dynamics*, arXiv:2610.09912v1 (2026), https://arxiv.org/abs/2610.09912 .
3. Qinian Jin and Qin Huang, *An Adaptive Heavy Ball Method for Ill-Posed Inverse Problems*, arXiv:2404.03218v1 (2024), https://arxiv.org/html/2404.03218v1 .
4. Classical Schur/Jury criterion for quadratic polynomials and Floquet analysis of linear periodic recurrences (standard tools, not new results).
