# Exact boundary obstruction for Liu’s 2014 one-parameter triangle conjecture
## Finding
For a nondegenerate Euclidean triangle \(ABC\), write \(a=BC\), \(b=CA\), and \(c=AB\). For an interior point \(P\), let \(R_1,R_2,R_3\) be its distances to \(A,B,C\), and let \(r_1,r_2,r_3\) be its distances to the opposite sidelines. Define
\[
F_\lambda(P,ABC)=\frac{{R_2+R_3-\lambda r_1}}{{a}}+\frac{{R_3+R_1-\lambda r_2}}{{b}}+\frac{{R_1+R_2-\lambda r_3}}{{c}}-\frac{{(4-\lambda)\sqrt3}}{{2}}.
\]
Jian Liu conjectured \(F_\lambda(P,ABC)\ge0\) for every interior \(P\) whenever \(3/5\le\lambda\le2\).

Set
\[
t_* = \frac{{1+2\sqrt{{-3+2\sqrt3}}}}{{3\sqrt3-2}}
\]
and
\[
\lambda_* = \frac{{8\sqrt3\,t_*-8t_*-2(1+t_*^2)}}{{t_*^2+2\sqrt3\,t_*-1}}
=0.586699153797909426\ldots.
\]
A necessary condition for the inequality to hold for every nondegenerate triangle and every interior point is
\[
\lambda_*\le\lambda\le2.
\]
For every \(\lambda<\lambda_*\), genuine interior counterexamples occur arbitrarily close to one apex of a fixed isosceles triangle. For every \(\lambda>2\), genuine interior counterexamples occur in a collapsing right-triangle family. The statement is deliberately one-sided: no validity is asserted for any parameter inside \([\lambda_*,2]\).

## Assumptions and scope
All distances are ordinary unsigned Euclidean distances. The triangle is nondegenerate and \(P\) is strictly interior in the final counterexamples. Boundary points are used only to compute limiting defects; strict negativity at a boundary configuration is transferred to nearby interior points by continuity.

The lower obstruction concerns the same first-power inequality and the same parameter \(\lambda\) as Liu's Conjecture 1. It does not address Liu's separate power inequality (Conjecture 2).

## Proof
Consider first an isosceles triangle with \(b=c=1\), and write its apex angle as \(2\theta\), where \(0<\theta<\pi/2\). Then
\[
a=2\sin\theta.
\]
Put the boundary point \(P=A\). At this point,
\[
R_1=0,\qquad R_2=R_3=1,\qquad r_1=\cos\theta,\qquad r_2=r_3=0.
\]
Hence
\[
F_\lambda(A,ABC)=2+\csc\theta-2\sqrt3+\frac{\lambda}{2}(\sqrt3-\cot\theta).
\]
Whenever \(\sqrt3-\cot\theta>0\), this vanishes at
\[
L(\theta)=\frac{2(2\sqrt3-2-\csc\theta)}{\sqrt3-\cot\theta}.
\]
Let \(t=\tan(\theta/2)\). On the relevant interval \(2-\sqrt3<t<1\),
\[
L(t)=\frac{8\sqrt3\,t-8t-2(1+t^2)}{t^2+2\sqrt3\,t-1}.
\]
Differentiation gives
\[
L'(t)=\frac{-4\big((3\sqrt3-2)t^2-2t+\sqrt3-2\big)}{(t^2+2\sqrt3\,t-1)^2}.
\]
The quadratic in the numerator has negative constant term and positive leading coefficient, so it has exactly one positive zero. Moreover it is negative at \(t=2-\sqrt3\) and positive at \(t=1\). Therefore \(L\) has a unique maximum on this interval, attained at
\[
t_*=\frac{1+2\sqrt{-3+2\sqrt3}}{3\sqrt3-2},
\]
with maximum \(\lambda_*=L(t_*)\).

At the fixed isosceles triangle determined by \(t_*\), the coefficient
\[
B_* = \frac{\sqrt3-\cot\theta_*}{2}
\]
is positive and
\[
F_\lambda(A,ABC)=B_*(\lambda-\lambda_*).
\]
Thus \(F_\lambda(A,ABC)<0\) for every \(\lambda<\lambda_*\). Since the displayed defect is continuous in \(P\), points strictly inside the triangle and arbitrarily close to \(A\) also have negative defect. Universal validity therefore forces \(\lambda\ge\lambda_*\).

For the upper obstruction, take
\[
A=(0,0),\qquad B=(1,0),\qquad C=(1,\varepsilon),
\]
with \(\varepsilon>0\), and use the boundary point \(P=(q,0)\) with fixed \(0<q<1\). Here \(a=\varepsilon\), \(R_2=1-q\), \(R_3=\sqrt{(1-q)^2+\varepsilon^2}\), and \(r_1=1-q\). All terms of \(F_\lambda\) except the \(a^{-1}\) term remain bounded as \(\varepsilon\to0^+\), while
\[
\varepsilon F_\lambda(P,ABC)\longrightarrow (2-\lambda)(1-q).
\]
For every \(\lambda>2\), the boundary defect is therefore negative for all sufficiently small positive \(\varepsilon\). Continuity again moves the point slightly into the triangle while preserving strict negativity. Universal validity forces \(\lambda\le2\).

Combining the two families gives the necessary outer window \(\lambda_*\le\lambda\le2\).

## Verification
The accompanying `verify.py` independently evaluates the exact radical formulas at high precision, checks the stationary quadratic, checks the derivative sign on both sides of \(t_*\), and numerically evaluates explicit interior representatives for \(\lambda=0.58\) and \(\lambda=2.01\). It also verifies the predicted upper-family scaled limit. These computations are diagnostic checks of the algebra; the infinite statements follow from the analytic limiting and continuity arguments above.

## Relationship to prior work
Liu's 2014 paper states Conjecture 1 precisely for \(3/5\le\lambda\le2\), after computer checking, and gives no proof of that conjecture. The present result does not prove the conjecture; it identifies a sharp obstruction within a natural isosceles apex-limit family and independently confirms that \(2\) is an unavoidable universal upper endpoint.

Two later full texts with very similar titles were inspected because they are plausible sources of coverage. Yang, Chen, Huang, Wang, and Lin (2017) prove a different parameterized inequality whose summands involve \((R_i^2-r_i^2)/(\cdots)\). Huang and Li (2018) prove four parameterized inequalities originating from Liu's different 2014 paper in volume 8, issue 3; their displayed propositions have squared-distance numerators and parameterized quadratic denominators. Neither inspected statement implies the first-power boundary obstruction proved here.

## Limitations
This result gives only necessary parameter conditions. It does not establish \(F_\lambda\ge0\) anywhere in \([\lambda_*,2]\), and in particular does not resolve Liu's stated conjecture on \([3/5,2]\). The lower number \(\lambda_*\) is the exact maximum obstruction produced by the specific isosceles-apex boundary family; a different family could in principle force a larger lower endpoint. Searches did not locate such a statement, but absence from the searched literature is not a proof of absolute novelty.

## References
1. Jian Liu, “A geometric inequality with one parameter for a point in the plane of a triangle,” *Journal of Mathematical Inequalities* 8 (2014), 91–106, doi:10.7153/jmi-08-05.
2. Yong Yang, Shengli Chen, Dong Huang, Xiang Wang, and Xiaoguang Lin, “Proof of an inequality conjecture for a point in the plane of a triangle,” *Journal of Mathematical Inequalities* 11 (2017), 399–411, doi:10.7153/jmi-11-34.
3. Fangjian Huang and Yi Li, “Parameterized inequalities about a point in the plane of a triangle,” *Journal of Mathematical Inequalities* 12 (2018), 953–960, doi:10.7153/jmi-2018-12-72.
