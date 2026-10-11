# Exact length-six polyphase base-energy minimum
## Finding
Let
\[
P(z)=\sum_{j=0}^{5}a_jz^j,\qquad |a_j|=1,
\]
and define the aperiodic autocorrelations and base energy by
\[
C_k=\sum_{j=0}^{5-k}a_{j+k}\overline{a_j},\qquad
E=\sum_{k=1}^{5}|C_k|^2.
\]
Then
\[
E\ge 5.
\]
Consequently, for normalized Haar measure on \(\mathbb T\),
\[
\|P\|_{L^4(\mathbb T)}^4=36+2E\ge46,
\]
and the usual merit factor satisfies
\[
\operatorname{MF}(P)=\frac{36}{2E}\le\frac{18}{5}.
\]
The bound is attained. If \(\zeta=e^{i\pi/3}\), then
\[
(a_0,a_1,a_2,a_3,a_4,a_5)=(1,1,\zeta,-1,1,-\zeta)
\]
has \(|C_k|=1\) for every \(1\le k\le5\), hence \(E=5\).

## Assumptions and scope
Only the six coefficient constraints \(|a_j|=1\) are assumed; phases are otherwise arbitrary and need not belong to a finite alphabet. Multiplication of all coefficients by a common unimodular scalar and multiplication of \(a_j\) by \(e^{ij\phi}\) preserve every \(|C_k|\). We therefore normalize \(a_0=a_5=1\).

Write
\[
a_1=e^{i(s+p)},\quad a_4=e^{i(s-p)},\quad
a_2=e^{i(t+q)},\quad a_3=e^{i(t-q)}.
\]
Put
\[
A=\cos s,\qquad B=\cos(t-s),\qquad C=\cos t,
\]
\[
K=\frac{3+8ABC}{2},\qquad U=A+2BC,\qquad V=C+2AB,
\]
and
\[
X=p+2q,\qquad Y=2p-q.
\]
A direct expansion of the five autocorrelations gives
\[
E=5+4F,
\]
where
\[
F=K+U\cos X+B\cos(X-Y)+V\cos Y.
\]
Thus it remains to prove \(F\ge0\) for all real \(s,t,X,Y\).

## Proof
Define the four corner values
\[
\begin{aligned}
p_1&=K+V+U+B, & p_2&=K+V-U-B,\\
p_3&=K-V+U-B, & p_4&=K-V-U+B.
\end{aligned}
\]
First we prove that all four are nonnegative and, more strongly, establish a relation among them. For finite
\[
u=\tan(s/2),\qquad v=\tan(t/2),\qquad
D=(1+u^2)^2(1+v^2)^2,
\]
define two-dimensional real vectors
\[
\begin{aligned}
z_1={}&(u^2v^2-3u^2+4uv-3v^2+5,\ 4(u+v)),\\
z_2={}&(-3u^2v^2+5u^2-4uv+v^2-3,\ 4u(uv-1)),\\
z_3={}&(-3u^2v^2+u^2-4uv+5v^2-3,\ 4v(uv-1)),\\
z_4={}&(5u^2v^2-3u^2+4uv-3v^2+1,\ -4uv(u+v)).
\end{aligned}
\]
Substitution of the tangent half-angle formulas gives the exact identities
\[
2Dp_i=\|z_i\|_2^2\qquad(1\le i\le4)
\]
and
\[
z_1\cdot z_4-z_2\cdot z_3=-4DB.
\]
Hence \(p_i\ge0\), and Cauchy--Schwarz followed by the triangle inequality yields
\[
\begin{aligned}
\sqrt{p_1p_4}+\sqrt{p_2p_3}
&=\frac{\|z_1\|\|z_4\|+\|z_2\|\|z_3\|}{2D}\\
&\ge\frac{|z_1\cdot z_4|+|z_2\cdot z_3|}{2D}\\
&\ge 2|B|.
\end{aligned}
\]
The cases in which \(u\) or \(v\) is infinite follow by continuity.

Now put
\[
r=\cos(X/2),\quad s_1=\sin(X/2),\quad
t_1=\cos(Y/2),\quad w=\sin(Y/2).
\]
Using \(\cos(X-Y)=\cos X\cos Y+\sin X\sin Y\), one obtains
\[
F=p_1r^2t_1^2+p_2s_1^2t_1^2+p_3r^2w^2+p_4s_1^2w^2+4Brs_1t_1w.
\]
Applying the arithmetic--geometric mean inequality to the first and fourth terms and to the second and third terms gives
\[
F\ge2|rs_1t_1w|\left(\sqrt{p_1p_4}+\sqrt{p_2p_3}-2|B|\right)\ge0.
\]
Therefore \(E\ge5\). The displayed sixth-root sequence has five sidelobes of unit modulus, so equality is attained.

## Verification
The accompanying `verify.py` checks with exact integer arithmetic the four tangent-half-angle polynomial identities, the dot-product identity that drives the Cauchy--Schwarz step, and the exact sixth-root witness correlations. These computations only replay algebraic identities already used in the proof; the universal inequality is proved analytically above.

## Relationship to prior work
Golomb and Scholtz exhibited the sixth-root sequence \((1,1,\zeta,-1,1,-\zeta)\) as a generalized Barker sequence of length six. That supplies a sharpness witness but does not lower-bound total squared autocorrelation over arbitrary continuous phases.

Borwein and Ferguson later tabulated base energy \(5.000\) at length six. Their paper explicitly describes the table as output of stochastic/local optimization and treats global optimality through statistical evidence. The present statement proves that tabulated value globally over the full continuous phase torus.

Borwein and Mossinghoff record the standard Parseval identity connecting fourth norm, autocorrelation energy, and merit factor, and classify this circle of extremal questions under MSC 42A05. Their treatment does not imply the length-six polyphase lower bound above.

## Limitations
No classification of all equality cases is claimed. In particular, the proof establishes the exact minimum value and one classical attaining sequence; it does not assert that every minimizer is Barker-equivalent to that sequence. The literature comparison cannot exclude an older result hidden under different radar/polyphase terminology, although the directly relevant primary texts and several equivalent-formulation searches were checked.

## References
1. S. W. Golomb and R. A. Scholtz, “Generalized Barker Sequences,” 1965. NASA Technical Reports Server records `19650022866` and `19650013726`; public record date 1965-09-30.
2. P. Borwein and R. Ferguson, “Polyphase sequences with low autocorrelation,” IEEE Transactions on Information Theory 51 (2005), DOI `10.1109/TIT.2004.842778`.
3. P. Borwein and M. J. Mossinghoff, “Barker sequences and flat polynomials,” manuscript/public copy `CECM:P213`; see the Parseval identity relating \(L^4\), aperiodic autocorrelations, and merit factor.
