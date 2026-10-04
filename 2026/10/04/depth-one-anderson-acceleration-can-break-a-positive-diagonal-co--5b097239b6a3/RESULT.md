# Depth-one Anderson acceleration can break a positive diagonal contraction in two dimensions
## Finding
Consider the depth-one Anderson acceleration method with unit mixing applied to a fixed-point map \(g:\mathbb R^d\to\mathbb R^d\). Starting from \(x^{(0)}\), set
\[
x^{(1)}=g(x^{(0)}).
\]
For \(k\ge1\), write
\[
f_k=g(x^{(k)})-x^{(k)}.
\]
When \(f_k\ne f_{k-1}\), choose the scalar \(s_k\) that minimizes
\[
\left\|(1-s)f_{k-1}+sf_k\right\|_2
\]
and set
\[
x^{(k+1)}=(1-s_k)g(x^{(k-1)})+s_k g(x^{(k)}).
\]
This is the standard depth-one specialization of Anderson acceleration with unit mixing.

For every sufficiently small \(\varepsilon>0\), consider the diagonal affine contraction
\[
g_\varepsilon(x_1,x_2)
=
\left(
(1-\varepsilon)x_1+1,
\frac45x_2+2\varepsilon
\right),
\qquad
x^{(0)}=(0,0).
\]
The map sends the nonnegative orthant into its strict interior and has contraction factor \(1-\varepsilon\) when \(0<\varepsilon<1/5\). Its unique fixed point is
\[
x^*_\varepsilon
=
\left(
\frac1\varepsilon,
10\varepsilon
\right)>0.
\]
Ordinary Picard iteration from the origin is componentwise strictly increasing and positive:
\[
x^{(k)}_{\mathrm{Picard},1}
=
\frac{1-(1-\varepsilon)^k}{\varepsilon},
\qquad
x^{(k)}_{\mathrm{Picard},2}
=
10\varepsilon\left(1-\left(\frac45\right)^k\right).
\]

Depth-one Anderson acceleration has a qualitatively different behavior. For all sufficiently small \(\varepsilon>0\), its first five nonzero iterates are strictly positive,
\[
x^{(1)},x^{(2)},x^{(3)},x^{(4)},x^{(5)}>0,
\]
but the second coordinate of the next iterate is negative:
\[
\bigl(x^{(6)}\bigr)_2<0.
\]
Thus a strictly positive diagonal contraction can lose orthant invariance solely through the affine residual-minimizing extrapolation.

The phenomenon has an exact rational witness. At
\[
\varepsilon=\frac1{200},
\]
the first five nonzero iterates are strictly positive, while
\[
\bigl(x^{(6)}\bigr)_2
=
-\frac{4801559852330482770906299820259}
{349417867959904066964567555052100}
<-rac1{100}.
\]
The corresponding first coordinate is positive, so \(x^{(6)}\) crosses exactly one coordinate hyperplane in this witness.

Dimension two is minimal for this failure among positive scalar affine contractions. In one dimension, for
\[
g(x)=ax+c,
\qquad
0\le a<1,
\qquad
c>0,
\qquad
x^{(0)}=0,
\]
depth-one Anderson acceleration reaches the positive fixed point exactly at its first accelerated step:
\[
x^{(2)}=\frac{c}{1-a}.
\]
Hence no one-dimensional member of this class can produce a negative Anderson iterate before convergence.

## Assumptions and scope
The Anderson convention is the affine-combination formulation with unit mixing and Euclidean residual least squares. The memory depth is exactly one, so only the two latest residuals are used.

The family is linear-affine, diagonal, and strictly contractive. No cross-coordinate coupling, nonlinearity, or indefinite Jacobian is used. The map itself preserves the positive orthant strictly; the sign failure is introduced only by the extrapolation coefficients.

The result establishes an open small-\(\varepsilon\) family and a concrete rational witness. It does not determine the largest contraction factor for which every positive diagonal affine map is orthant-safe under depth-one Anderson acceleration, nor does it classify other memory depths or safeguarding rules.

## Proof
For two residuals, the least-squares coefficient is explicit. Put
\[
d_k=f_k-f_{k-1}.
\]
Whenever \(d_k\ne0\),
\[
s_k
=
-\frac{f_{k-1}^{\mathsf T}d_k}{d_k^{\mathsf T}d_k}.
\]
This formula makes every finite Anderson iterate a rational function of \(\varepsilon\) as long as the denominators remain nonzero.

To expose the small-\(\varepsilon\) mechanism, scale only the slow coordinate:
\[
U=\varepsilon x_1,
\qquad
V=x_2.
\]
In these coordinates the fixed-point residual and map are
\[
F_\varepsilon(U,V)
=
\left(1-U,2\varepsilon-\frac15V\right),
\]
\[
G_\varepsilon(U,V)
=
\left((1-\varepsilon)U+\varepsilon,\frac45V+2\varepsilon\right).
\]
The first Picard point is
\[
S_1=(\varepsilon,2\varepsilon).
\]
At the first accelerated step the minimizing coefficient is exactly
\[
s_1
=
\frac{25+20\varepsilon}{29\varepsilon},
\]
so
\[
\varepsilon s_1\longrightarrow\frac{25}{29}.
\]
Consequently the scaled second Anderson iterate has the finite limit
\[
S_2
\longrightarrow
\left(\frac{25}{29},\frac{40}{29}\right).
\]

For the subsequent limiting recurrence set
\[
F_0(U,V)=\left(1-U,-\frac15V\right),
\qquad
G_0(U,V)=\left(U,\frac45V\right).
\]
Starting with
\[
S_1^{(0)}=(0,0),
\qquad
S_2^{(0)}=\left(\frac{25}{29},\frac{40}{29}\right),
\]
apply the same depth-one residual least-squares rule using \(F_0\) and \(G_0\). Exact rational arithmetic gives
\[
S_3^{(0)}
=
\left(\frac{625}{689},\frac{800}{689}\right),
\]
\[
S_4^{(0)}
=
\left(\frac{105125}{98149},\frac{28800}{98149}\right),
\]
\[
S_5^{(0)}
=
\left(\frac{14982925}{14044109},\frac{3548160}{14044109}\right),
\]
and
\[
S_6^{(0)}
=
\left(
\frac{2235098625}{2165688769},
-\frac{143897600}{2165688769}
\right).
\]
All residual-difference denominators in these limiting steps are nonzero. Therefore the actual scaled Anderson iterates depend continuously on \(\varepsilon\) for all sufficiently small positive \(\varepsilon\). The displayed limiting first coordinates are positive; the second coordinates through \(S_5^{(0)}\) are positive; and the second coordinate of \(S_6^{(0)}\) is strictly negative. Together with the explicit positive first Picard point, continuity proves the claimed open family.

For the one-dimensional minimality statement, let
\[
g(x)=ax+c,
\qquad
0\le a<1.
\]
Then
\[
f_0=c,
\qquad
f_1=ac.
\]
The depth-one least-squares residual can be made exactly zero with
\[
s_1=\frac1{1-a}.
\]
Hence
\[
x^{(2)}
=(1-s_1)c+s_1(1+a)c
=
\frac{c}{1-a},
\]
which is the fixed point and is positive. This excludes a one-dimensional sign failure.

## Verification
The accompanying `verify.py` implements the depth-one Anderson recurrence using exact rational arithmetic only.

For \(\varepsilon=1/200\), it reconstructs every residual, every least-squares coefficient, and the iterates through \(x^{(6)}\). It verifies strict positivity of \(x^{(1)},\ldots,x^{(5)}\), strict negativity of the second coordinate of \(x^{(6)}\), and the displayed exact fraction.

The checker separately reconstructs the scaled limiting recurrence from \(S_2^{(0)}\) through \(S_6^{(0)}\) and verifies every displayed rational state and the nonvanishing residual-difference denominators. It also verifies the scalar one-dimensional exact-convergence identity over several rational contraction factors.

The open-family conclusion is analytic: it follows from rational dependence and strict signs in the nondegenerate limiting recurrence, not from finite numerical sampling.

## Relationship to prior work
Anderson acceleration itself is classical. Walker and Ni give the standard affine-combination algorithm, develop its relation to GMRES on linear problems, and discuss practical truncated implementations. In their nonnegative-matrix-factorization experiment they explicitly note that Anderson acceleration can in general produce matrices with negative entries. That qualitative possibility is prior work and is not claimed here.

Potra and Engler give a characterization of Anderson acceleration on linear problems and establish its relation to GMRES up to stagnation for the untruncated linear setting. Toth and Kelley prove convergence results for Anderson acceleration on contractive maps, including Anderson depth one without a coefficient-boundedness assumption. Those convergence results concern residual or error convergence and do not imply preservation of a coordinate cone.

The present result isolates a minimal, exactly solvable positivity obstruction. The underlying fixed-point map is diagonal, strictly positive, and contractive; ordinary Picard iteration remains strictly positive and monotone; one dimension is impossible; and an open two-dimensional family has a certified sign crossing after five positive Anderson iterates. The claim is this exact cone-invariance failure and minimal-dimension mechanism, not the general possibility of negative Anderson coefficients or negative entries.

## Limitations
The family approaches contraction factor one as \(\varepsilon\to0\). No sharp contraction-factor threshold for positivity preservation is claimed.

The result uses depth one with unit mixing and no safeguard. Constrained, damped, restarted, or positivity-projected Anderson variants can behave differently.

The sign crossing occurs at the sixth iterate in this family, but no global earliest-iteration theorem is claimed for all two-dimensional positive contractions.

Anderson acceleration has a large literature across nonlinear equations, electronic structure, and optimization. A specialized source may contain a comparable positive-map counterexample under different terminology. The strongest checked primary sources already acknowledge possible negative entries qualitatively, so originality is claimed only for the minimal-dimensional diagonal contraction theorem and its explicit open family.

## References
1. Homer F. Walker and Peng Ni, *Anderson Acceleration for Fixed-Point Iterations*, SIAM Journal on Numerical Analysis 49 (2011), 1715--1735, DOI: 10.1137/10078356X.
2. Florian A. Potra and Hans Engler, *A Characterization of the Behavior of the Anderson Acceleration on Linear Problems*, arXiv:1102.0796v1, February 3, 2011; Linear Algebra and its Applications 438 (2013), 1002--1011.
3. Alex Toth and C. T. Kelley, *Convergence Analysis for Anderson Acceleration*, SIAM Journal on Numerical Analysis 53 (2015), 805--819, DOI: 10.1137/130919398.
