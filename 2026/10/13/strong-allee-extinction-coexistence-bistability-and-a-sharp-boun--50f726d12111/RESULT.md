# Strong-Allee extinction–coexistence bistability and a sharp boundary-type transition in a Ricker map

## Finding

The positive-parameter Ricker-type predator–prey map of Seralan, Vadivel, Chalishajar, and Gunasekaran is
\[
H_{n+1}=H_n\exp\!\left(a-bH_n-\frac{\alpha}{\beta+H_n}-\frac{cP_n}{e+H_n}\right),
\]
\[
P_{n+1}=P_n\exp\!\left(\frac{fH_n}{e+H_n}-d\right),
\qquad H_n,P_n\ge0.
\]
The source explicitly studies the **weak** Allee regime \(\alpha<a\beta\). Here we identify a sharp, structurally robust extinction–coexistence bistability window in its complementary **strong** regime \(\alpha>a\beta\), including the other fixed points and their spectral types.

For general positive parameters with \(\alpha>a\beta\), a positive coexistence fixed point exists if and only if
\[
f>d,\qquad \alpha<(a-b\eta)(\beta+\eta),
\qquad \eta=\frac{de}{f-d}.
\]
It is unique, with
\[
H^*=\eta,\qquad
P^*=\frac{e+\eta}{c}\left(a-b\eta-\frac{\alpha}{\beta+\eta}\right)>0.
\]
Under these conditions there are exactly two additional positive prey-only equilibria, \(H_-<\eta<H_+\), and the origin. Indeed, the prey-only equation is
\[
bH^2+(b\beta-a)H+\alpha-a\beta=0,
\]
which has one root on either side of \(\eta\) when the coexistence criterion holds. This general branch lemma is used to obtain a complete fixed-point diagram for the following parameter family.

Fix
\[
a=4,\quad b=\beta=c=d=e=1,\quad f=\frac32
\]
and allow
\[
4<\alpha<6.
\]
The four and only four nonnegative fixed points are
\[
E_0=(0,0),\quad
E_\pm=\left(\frac{3\pm\sqrt{25-4\alpha}}2,0\right),
\quad E_*=(2,6-\alpha).
\]
Both the extinction state \(E_0\) and positive coexistence state \(E_*\) are **hyperbolic sinks throughout the entire open interval**. Their attracting basins contain distinct open subsets of the nonnegative quadrant. Thus the same strong-Allee parameter values support either extinction or long-term coexistence, depending on initial populations.

The other equilibria have a sharp classification. Put
\[
\alpha_F=\frac{29+\sqrt{41}}8\approx4.4253905297.
\]
Then \(E_-\) is a saddle for every \(4<\alpha<6\). The upper boundary state \(E_+\) is a source for \(4<\alpha<\alpha_F\), has a multiplier \(-1\) at \(\alpha=\alpha_F\), and is a saddle for \(\alpha_F<\alpha<6\). The predator multiplier at \(E_+\) exceeds one for the whole interval; in particular, neither prey-only equilibrium is a full two-species sink.

## Assumptions and scope

All original rates and half-saturation parameters are strictly positive; populations \(H,P\) are nonnegative. The strong Allee effect is defined by \(\alpha>a\beta\), as in the source. The displayed exact classification concerns the particular one-parameter family above and every real \(\alpha\) in its stated open interval, not just sampled values.

The words “sink” and “source” refer to eigenvalues strictly inside or outside the unit circle, respectively, for the two-dimensional discrete map. Bistability means two distinct locally asymptotically stable equilibria with open local basins; it does not assert global partition into exactly two basins or exclude other invariant sets elsewhere.

The value \(\alpha_F\) identifies a boundary eigenvalue \(-1\); no nonlinear flip-bifurcation nondegeneracy or existence of a period-two orbit is claimed at that parameter.

## Proof

Write
\[
U(H,P)=a-bH-\frac\alpha{\beta+H}-\frac{cP}{e+H},
\qquad
W(H)=\frac{fH}{e+H}-d.
\]
At an interior fixed point, the exponential factors must both equal one, so \(W(H)=0\) and \(U(H,P)=0\). The first equation requires \(f>d\) and fixes \(H=\eta=de/(f-d)\). The second gives the unique \(P^*\) above. Its positivity is equivalent to \(\alpha<(a-b\eta)(\beta+\eta)\).

At a prey-only positive fixed point, \(U(H,0)=0\), equivalent to
\[
q(H)=bH^2+(b\beta-a)H+\alpha-a\beta=0.
\]
When \(\alpha>a\beta\), we have \(q(0)>0\) and \(q(H)\to+\infty\) at positive infinity. Positive coexistence yields \(q(\eta)=\alpha-(a-b\eta)(\beta+\eta)<0\); therefore exactly two simple positive roots straddle \(\eta\). This exhausts the fixed points: either \(P=0\), or \(W(H)=0\) with the unique positive solution above.

In the chosen family, \(\eta=2\), and
\[
q(H)=H^2-3H+\alpha-4.
\]
For \(4<\alpha<6\), its roots satisfy
\[
0<H_-<1<2<H_+<3.
\]
The interior predator value is \(P^*=6-\alpha>0\). The origin has diagonal Jacobian with eigenvalues
\[
\lambda_{0,H}=e^{4-\alpha},\qquad \lambda_{0,P}=e^{-1},
\]
which both lie strictly between zero and one.

At an interior fixed point of the general map, differentiation yields
\[
J=\begin{pmatrix}
1+H[-b+\alpha/(\beta+H)^2+cP/(e+H)^2]&-cH/(e+H)\\
feP/(e+H)^2&1
\end{pmatrix}.
\]
Substitution of \(H=2\) and \(P=6-\alpha\) gives exactly
\[
J_* = \begin{pmatrix}1/3&-2/3\\(6-\alpha)/6&1\end{pmatrix}.
\]
Thus
\[
T=\operatorname{tr}J_*=\frac43,\qquad
D=\det J_*=1-\frac\alpha9.
\]
The Schur–Jury criterion for the real quadratic \(z^2-Tz+D\) reads
\[
1-D>0,\qquad 1-T+D>0,\qquad1+T+D>0.
\]
Here those expressions are \(\alpha/9\), \((6-\alpha)/9\), and \((30-\alpha)/9\), all strictly positive for every \(4<\alpha<6\). Hence \(E_*\) is a hyperbolic sink, proving two simultaneous sinks and open local attracting basins.

At a prey-only fixed point \((H,0)\), the triangular Jacobian has prey and predator multipliers
\[
\lambda_H=1+H\left[-1+\frac\alpha{(1+H)^2}\right],\qquad
\lambda_P=\exp\!\left(\frac{3H}{2(1+H)}-1\right).
\]
The prey-only equilibrium equation gives \(\alpha=(4-H)(1+H)\). Therefore
\[
\lambda_H=1+\frac{H(3-2H)}{1+H},\qquad
\lambda_P=\exp\!\left(\frac{H-2}{2(1+H)}\right).
\]
For \(0<H_-<1\), we have \(\lambda_H>1\), but \(0<\lambda_P<1\). Thus \(E_-\) is always a saddle. For \(2<H_+<3\), \(\lambda_H<1\) and \(\lambda_P>1\). The prey multiplier equals \(-1\) precisely when
\[
2H_+^2-5H_+-2=0,
\quad H_+=\frac{5+\sqrt{41}}4.
\]
Since \(\alpha=(4-H_+)(1+H_+)\), this corresponds exactly to
\[
\alpha_F=\frac{29+\sqrt{41}}8.
\]
The function \(\lambda_H=1+H(3-2H)/(1+H)\) is strictly decreasing for \(H>2\), while \(H_+\) is strictly decreasing with \(\alpha\). Hence \(\lambda_H<-1\) for \(\alpha<\alpha_F\), \(\lambda_H=-1\) at \(\alpha_F\), and \(-1<\lambda_H<1\) for \(\alpha>\alpha_F\). Combined with \(\lambda_P>1\), this gives the stated source-to-nonhyperbolic-to-saddle classification.

## Verification

The included standalone `verify.py` reconstructs the fixed-point polynomial, the interior Jacobian, the Schur–Jury margins, and the exact upper-boundary multiplier crossing. Symbolic identities are verified with exact rational and algebraic arithmetic. Selected rational parameters are then replayed directly against the original exponential map and its Jacobian as supporting numerical checks; those samples are not the proof of the universal interval.

## Relationship to prior work

Seralan, Vadivel, Chalishajar, and Gunasekaran introduce exactly this exponential Ricker-type map and state that their main local-stability and bifurcation analysis concerns the **weak** Allee regime. Their Section 2 gives the basic equilibrium equations but does not give a strong-Allee bistability interval or classify both prey-only branches as \(\alpha\) varies across an entire strong regime.

Al Khabyah, Ahmed, Akram, and Akhtar analyze **strong Allee** effects in a different discrete predator–prey model obtained from a cubic-growth differential equation by forward Euler discretization. Its map has polynomial-increment, rather than exponential Ricker, form. Their fixed-point and stability classifications therefore do not imply the exact exponential-map Schur interval or the \(-1\) boundary crossing above.

Cai, Wang, and Wang study strong and weak additive Allee effects in a **continuous-time diffusive** predator–prey counterpart. That prior line of work motivates extinction–coexistence competition and may contain related equilibrium-existence conditions, so neither general strong-Allee bistability nor the equilibrium quadratic itself is claimed to be novel. A full-text comparison was limited by a publisher verification barrier; the available abstract does not determine the precise extent of its branch classification. In any event, differential-equation local stability does not supply the two discrete Jacobian multipliers, the complete Schur window, or the upper prey-only \(-1\) transition derived here.

A separate earlier analysis of the same Ricker article concerns the trace–determinant stability criterion in its weak-Allee setting. It does not discuss the present strong-Allee four-fixed-point family or its extinction–coexistence bistability window.

## Limitations

The theorem is source-specific and local-dynamical. It does not claim global basin partitions, absence of other attractors, nonlinear period-doubling at \(\alpha_F\), or practical optimal intervention thresholds. The prey-only roots are algebraic consequences shared by continuous and discrete analogues; the genuinely discrete conclusion comes from explicit eigenvalue and Jury analysis.

A relevant older continuous/diffusive paper could not be inspected beyond available bibliographic material because of a publisher access check; that is a residual literature-comparison risk, not evidence of independence or novelty by failed search.

## References

1. V. Seralan, R. Vadivel, D. Chalishajar, N. Gunasekaran, “Dynamical complexities and chaos control in a Ricker type predator-prey model with additive Allee effect,” *AIMS Mathematics* 8 (2023), 22896–22923. DOI: 10.3934/math.20231165. First public date: 19 July 2023.
2. A. Al Khabyah, R. Ahmed, M. S. Akram, S. Akhtar, “Stability, bifurcation, and chaos control in a discrete predator-prey model with strong Allee effect,” *AIMS Mathematics* 8 (2023), 8060–8081. DOI: 10.3934/math.2023408.
3. Y. Cai, W. Wang, J. Wang, “Dynamics of a diffusive predator–prey model with additive Allee effect,” *International Journal of Biomathematics* 5 (2012), 1250023. DOI: 10.1142/S1793524511001659.
