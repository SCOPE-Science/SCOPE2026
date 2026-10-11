# Exact stability skeleton of the coefficient-one normalized PMSG flow
## Finding
Consider the printed zero-input normalized PMSG system
\[
\dot x=a(y-x)+zy,\qquad
\dot y=-y-xz+bx,\qquad
\dot z=-z+xy.
\]
At the source value \(a=109/20\), the origin is globally asymptotically stable for every \(0<b\le 1\). For every \(b>1\), there are exactly two nonzero equilibria. Writing their common third coordinate as \(s>0\), they are
\[
E_{\pm}(s)=\left(\pm\sqrt{\frac{s(a+s)}{a}},\ \pm\sqrt{\frac{as}{a+s}},\ s\right),
\qquad
b=s+\frac{a}{a+s}.
\]
The map \(s\mapsto b\) is strictly increasing for \(s\ge0\), so this parameterization is unique. The pair \(E_{\pm}\) is locally asymptotically stable exactly for \(1<b<b_H\), where
\[
b_H=s_H+\frac{109/20}{109/20+s_H}
 =5.5859037407683744217621939969\ldots
\]
and \(s_H\) is the unique positive root of
\[
552000s^3+6016800s^2+394580s-228364701=0.
\]
At \(b=b_H\), each nonzero equilibrium has eigenvalues
\[
-\frac{149}{20},\qquad \pm i\,3.6883664158283907473\ldots,
\]
and for \(b>b_H\) each has exactly two eigenvalues in the open right half-plane. Thus the source's numerically reported transition near \(b=5.2\) occurs while the nonzero equilibrium pair is still locally asymptotically stable; the exact local spectral stability boundary is \(b_H\).

## Assumptions and scope
The claim concerns exactly the coefficient-one vector field printed as system (4) in the cited 2022 source, with \(a=5.45=109/20\) and \(b>0\). It does not assert that a trajectory from the source's chosen initial condition converges to an equilibrium whenever that equilibrium is locally stable. It does not classify all periodic or chaotic invariant sets, and it does not assert a nonlinear Hopf bifurcation, its criticality, or the basin boundary at \(b=b_H\).

## Proof
For \(0<b<1\), define
\[
V=\frac12\left(x^2+\frac{a}{b}y^2+\left(\frac{a}{b}-1\right)z^2\right).
\]
Since \(a=109/20>1\), this is positive definite and radially unbounded. Direct substitution gives the exact cancellation
\[
\dot V
=-a(x-y)^2-a\left(\frac1b-1\right)y^2-
\left(\frac ab-1\right)z^2,
\]
which is negative definite. Hence the origin is globally asymptotically stable and all forward solutions are bounded and complete. At \(b=1\), use
\[
V=\frac12\left(x^2+ay^2+(a-1)z^2\right),
\qquad
\dot V=-a(x-y)^2-(a-1)z^2.
\]
The largest invariant subset of \(\{\dot V=0\}\) is the origin: invariance would require \(x=y\) and \(z=0\), while \(\dot z=x^2\) then forces \(x=y=0\). LaSalle's invariance principle therefore gives global asymptotic stability also at \(b=1\).

For an equilibrium with \(b>0\), set \(s=z=xy\). If it is nonzero then \(y(a+s)=ax\), so
\[
\frac yx=\frac a{a+s},\qquad
x^2=\frac{s(a+s)}a,
\qquad
b=s+\frac a{a+s}.
\]
For positive \(b\), real nonzero equilibria require \(s>0\); the alternative \(s<-a\) makes \(b<0\). Because \(a>1\),
\[
\frac{db}{ds}=1-\frac{a}{(a+s)^2}>0\qquad(s\ge0),
\]
and \(b(0)=1\), proving the stated existence and uniqueness of the two symmetric equilibria for every \(b>1\).

At either nonzero equilibrium, the characteristic polynomial is
\[
q(\lambda)=\lambda^3+A_1\lambda^2+A_2\lambda+A_3,
\]
where
\[
A_1=a+2,
\]
\[
A_2=\frac{a^3+a^2s+a^2+2as^2+as+s^3}{a(a+s)},
\]
\[
A_3=\frac{2s\big((a+s)^2-a\big)}{a+s}.
\]
For \(a=109/20\) and \(s>0\), all three coefficients are positive. The cubic Routh-Hurwitz criterion therefore reduces local asymptotic stability to \(A_1A_2-A_3>0\). Exact simplification gives
\[
A_1A_2-A_3
=-\frac{552000s^3+6016800s^2+394580s-228364701}
{43600(20s+109)}.
\]
The numerator polynomial on the right has derivative
\[
1656000s^2+12033600s+394580>0\qquad(s\ge0),
\]
is negative at \(s=0\), and tends to \(+\infty\). It therefore has exactly one positive root \(s_H\), and the Routh determinant changes from positive to negative there. At equality, \(A_3=A_1A_2\), hence
\[
q(\lambda)=(\lambda+A_1)(\lambda^2+A_2),
\]
which gives the stated imaginary pair and the real eigenvalue \(-149/20\). For \(s>s_H\), the first column of the cubic Routh array has signs \(+,+,-,+\), so exactly two roots lie in the open right half-plane.

Finally, the origin has characteristic factor
\[
(\lambda+1)\left(\lambda^2+(a+1)\lambda+a(1-b)\right).
\]
Thus it is locally asymptotically stable for \(0<b<1\), nonhyperbolic at \(b=1\), and unstable for \(b>1\), consistent with the global result and the birth of the nonzero pair.

## Verification
The accompanying `verify.py` uses only the Python standard library. It reconstructs the exact specialized Routh numerator from rational arithmetic, proves its derivative coefficients are positive on \(s\ge0\), isolates the unique positive root by bisection, computes \(b_H\) and the imaginary frequency to high precision, and checks the quoted decimal values. The analytic Lyapunov and Routh-Hurwitz arguments above are the proof; the script verifies the algebraic specialization and numerical rendering.

## Relationship to prior work
The 2022 AIMS Mathematics article prints this coefficient-one system, fixes \(a=5.45\), and reports a numerical Lyapunov/bifurcation sweep in \(b\), describing stable behavior on \([0,5.2]\) and chaotic behavior beginning at \(5.2\). It does not give the equilibrium parameterization, a global Lyapunov proof for the origin, or the exact local spectral threshold above.

Borah and Roy (2017) analyze a related fractional-order PMSG model, including equilibria, a Jacobian characteristic equation, and a fractional-order Hopf discussion. Their displayed model retains a separate coefficient multiplying the quadratic term in the first equation and their displayed nonzero equilibria are parameterized differently. Their accessible analysis does not state the coefficient-one branch above, the global Lyapunov factorization, or the algebraic threshold \(b_H\).

Messadi et al. (2015) is the earlier PMSG source cited by the 2022 article for its model and is therefore a relevant comparison. Its public abstract and bibliographic page describe predictive chaos control; a full article text was not recovered through the available lawful-access routes during this review. This remains a residual originality risk, but no accessible evidence located there or in the later related literature states or implies the combined global/local stability skeleton proved here.

## Limitations
The result is a theorem about the printed autonomous ODE, not a validation of the physical parameter reduction. Local stability of \(E_{\pm}\) does not imply global attraction, and coexistence with other invariant sets is not excluded. The statement at \(b=b_H\) is spectral only: no first Lyapunov coefficient or nonlinear Hopf theorem is claimed. The originality assessment is limited by incomplete access to the full 2015 Messadi et al. article.

## References
1. A. Sambas et al., “Investigation of chaotic behavior and adaptive type-2 fuzzy controller approach for Permanent Magnet Synchronous Generator (PMSG) wind turbine system,” *AIMS Mathematics* 8 (2023), 5670–5686. DOI: 10.3934/math.2023285. Published 22 December 2022.
2. M. Borah and B. K. Roy, “Dynamics of the fractional-order chaotic PMSG, its stabilisation using predictive control and circuit validation,” *IET Electric Power Applications* 11 (2017), 707–716. DOI: 10.1049/iet-epa.2016.0506.
3. M. Messadi, A. Mellit, K. Kemih, M. Ghanes, “Predictive control of a chaotic permanent magnet synchronous generator in a wind turbine system,” *Chinese Physics B* 24 (2015), 010502. DOI: 10.1088/1674-1056/24/1/010502.
