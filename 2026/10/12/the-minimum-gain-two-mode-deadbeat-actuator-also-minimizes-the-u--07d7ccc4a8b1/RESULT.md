# The minimum-gain two-mode deadbeat actuator also minimizes the unavoidable transient

## Finding
Consider the stable discrete-time system
\[
x_{j+1}=Ax_j+b u_j,
\qquad
A=\operatorname{diag}(a,d),
\qquad
0<d<a<1,
\]
with one scalar input, a freely oriented unit actuator
\[
b=(b_1,b_2)^{\mathsf T},
\qquad
b_1^2+b_2^2=1,
\qquad
b_1b_2\ne0,
\]
and state feedback
\[
u_j=-k^{\mathsf T}x_j.
\]
Require minimum-time deadbeat regulation: the two closed-loop poles are both at zero.

There is one actuator direction, unique in squared components, that simultaneously minimizes two natural quantities: the feedback gain and the worst one-step Euclidean transient of the nilpotent closed loop. Its squared components are
\[
\boxed{
 b_1^2=\frac{a^2}{a^2+d^2},
 \qquad
 b_2^2=\frac{d^2}{a^2+d^2}.
}
\]
At this direction,
\[
\boxed{
\min_b\|k\|_2
=
\frac{a^2+d^2}{a-d}
}
\]
and
\[
\boxed{
\min_b\|A-bk^{\mathsf T}\|_2
=
\frac{2ad}{a-d}.
}
\]

For the positive representative
\[
b_*=\frac{1}{\sqrt{a^2+d^2}}(a,d)^{\mathsf T},
\]
the optimum feedback is
\[
k_*=\frac{\sqrt{a^2+d^2}}{a-d}(a,-d)^{\mathsf T},
\]
and the deadbeat closed loop is
\[
A_{c,*}
=
\frac{ad}{a-d}
\begin{pmatrix}
-1&1\\
-1&1
\end{pmatrix},
\qquad
A_{c,*}^2=0.
\]

Thus gain minimization and transient minimization agree exactly in this first nontrivial actuator-co-design problem. They also expose an unavoidable speed-versus-robustness cost: as the two stable modes coalesce, both optimal quantities diverge like the reciprocal modal gap.

An exact example is
\[
a=\frac45,
\qquad
d=\frac35,
\qquad
b_*=\left(\frac45,\frac35\right)^{\mathsf T},
\qquad
k_*=(4,-3)^{\mathsf T}.
\]
Then the open-loop spectral radius is only \(4/5\), while
\[
A_{c,*}
=
\frac{12}{5}
\begin{pmatrix}
-1&1\\
-1&1
\end{pmatrix},
\qquad
\|A_{c,*}\|_2=\frac{24}{5}.
\]
Some state is therefore amplified by a factor \(24/5\) in the first step, even though every state is exactly zero after the second step.

## Assumptions and scope
The plant is real, diagonal, two-dimensional, discrete-time, and open-loop stable, with distinct positive eigenvalues. The input is scalar. Its direction is a design variable but its Euclidean norm is fixed to one, because otherwise feedback-gain minimization is ill-posed under reciprocal rescaling of actuator and gain.

The feedback convention is
\[
u_j=-k^{\mathsf T}x_j,
\]
so the closed-loop matrix is
\[
A_c=A-bk^{\mathsf T}.
\]
Deadbeat means that both closed-loop poles are at the origin. Since the system is two-dimensional, scalar-input, and controllable whenever \(b_1b_2\ne0\), this is the minimum-time two-step deadbeat requirement. The nonzero closed-loop matrix is nilpotent of index two.

The transient objective is the spectral norm \(\|A_c\|_2\), which is exactly the largest possible one-step Euclidean state amplification. No claim is made about input saturation, measurement noise, finite precision, nonnormal open-loop matrices, multiple inputs, or dimensions above two.

## Proof
Put
\[
\Delta=a-d>0.
\]
For fixed \(b\), the scalar-input controllable pair has a unique feedback assigning the characteristic polynomial \(\lambda^2\). The trace condition gives
\[
b_1k_1+b_2k_2=a+d,
\]
while the determinant condition gives
\[
db_1k_1+ab_2k_2=ad.
\]
Solving these two equations yields
\[
b_1k_1=\frac{a^2}{\Delta},
\qquad
b_2k_2=-\frac{d^2}{\Delta}.
\]
Therefore
\[
\|k\|_2^2
=
\frac1{\Delta^2}
\left(
\frac{a^4}{b_1^2}+
\frac{d^4}{b_2^2}
\right).
\]
Let
\[
x=b_1^2,
\qquad
1-x=b_2^2.
\]
Then Cauchy--Schwarz gives
\[
\frac{a^4}{x}+\frac{d^4}{1-x}
\ge
(a^2+d^2)^2,
\]
with equality exactly when
\[
x=\frac{a^2}{a^2+d^2}.
\]
This proves the sharp gain formula.

Substituting the feedback products into the closed-loop matrix gives
\[
A_c
=
\frac1\Delta
\begin{pmatrix}
-ad & d^2 b_1/b_2\\
-a^2 b_2/b_1 & ad
\end{pmatrix}.
\]
Its trace and determinant are zero, so
\[
A_c^2=0.
\]
Because \(A_c\ne0\), it has rank one. A rank-one matrix has a single nonzero singular value, and therefore
\[
\|A_c\|_2=\|A_c\|_{\mathrm F}.
\]
Directly,
\[
\|A_c\|_2^2
=
\frac{
\left(a^2b_2^2+d^2b_1^2\right)^2
}{
 b_1^2b_2^2\Delta^2
}.
\]
Now
\[
a^2(1-x)+d^2x
\ge
2ad\sqrt{x(1-x)},
\]
because it is equivalent to
\[
\left(a\sqrt{1-x}-d\sqrt{x}\right)^2\ge0.
\]
Hence
\[
\|A_c\|_2\ge\frac{2ad}{\Delta},
\]
with equality exactly when
\[
a\sqrt{1-x}=d\sqrt{x},
\]
that is, at the same squared actuator weights as the gain optimum.

For the positive representative of this direction,
\[
b_*=\frac1{\sqrt{a^2+d^2}}(a,d)^{\mathsf T},
\]
substitution gives the displayed \(k_*\) and \(A_{c,*}\).

Finally, if \(a,d\to s\in(0,1)\) with \(a>d\), then
\[
a^2+d^2\to2s^2,
\qquad
2ad\to2s^2,
\]
so both minima are asymptotic to
\[
\frac{2s^2}{a-d}.
\]

## Verification
The embedded `verify.py` checks the exact rational witness
\[
a=\frac45,
\qquad
d=\frac35,
\qquad
b=\left(\frac45,\frac35\right)^{\mathsf T},
\qquad
k=(4,-3)^{\mathsf T}.
\]
It verifies exactly that
\[
A-bk^{\mathsf T}
=
\frac{12}{5}
\begin{pmatrix}
-1&1\\
-1&1
\end{pmatrix}
\]
and that its square is zero. It also verifies the exact gain norm \(5\), the exact spectral norm \(24/5\) through the rank-one Frobenius identity, and the equality conditions for both optimization bounds.

The checker additionally tests the symbolic algebra behind the trace/determinant equations and the closed-loop norm formula on several rational parameter choices. Finite checks corroborate the proof but do not establish the all-parameter theorem.

## Relationship to prior work
Minimum-time deadbeat control and minimum-gain deadbeat feedback are classical. Amin and Elabdalla explicitly studied minimum-gain minimum-time deadbeat controllers. Lam, Tso, and Tsing later emphasized that deadbeat closed-loop matrices are nilpotent and can have nontrivial Jordan structure, making transient robustness a separate issue from pole placement alone.

Minimum-gain exact pole placement is also classical. Schmid, Ntogramatzidis, Nguyen, and Pandey treat arbitrary repeated pole placement and optimize the feedback-matrix norm for a fixed plant input matrix. Datta and Chakraborty study feedback-norm minimization under exact or regional pole constraints. These works supply the gain-minimization context.

The actuator itself is fixed in the classical minimum-gain pole-placement formulation. Later work has considered joint input-assignment and feedback-gain design in other settings, such as shifting one dominant mode of an undirected network, but that problem preserves the remaining eigenstructure rather than imposing a nilpotent deadbeat closed loop.

The result here isolates the smallest continuous actuator-co-design problem and solves it in closed form. The new point is the joint statement that, among all unit scalar actuator directions for a two-mode diagonal plant, the minimum-gain deadbeat actuator is exactly also the minimum-transient deadbeat actuator, together with the sharp formulas and the reciprocal modal-gap obstruction. Targeted searches for actuator-direction, input-assignment, minimum-gain deadbeat, nilpotent-transient, and two-mode equivalents did not locate an implication-equivalent statement.

## Limitations
The two-mode diagonal model is deliberately minimal. Higher-dimensional actuator co-design can have competing gain and transient objectives and is not covered.

The actuator magnitude is normalized. Without such a normalization, gain norm can be reduced arbitrarily by scaling the actuator and inversely scaling the feedback.

The state norm and feedback norm are Euclidean. Similarity transformations that are not orthogonal change these quantities, so the statement belongs to the given orthonormal modal coordinates.

The theorem concerns exact state feedback. It does not include observer dynamics, input constraints, modeling error, or noise. The large transient near modal coalescence indicates why those effects may matter, but no robustness theorem for them is claimed.

## References
1. M. H. Amin and A. M. Elabdalla, “Minimum-gain minimum-time deadbeat controllers,” Systems & Control Letters 11 (1988), 213–219. DOI 10.1016/0167-6911(88)90061-8.
2. J. Lam, H. K. Tso, and N. K. Tsing, “On the Design of Robust Deadbeat Regulators,” Proceedings of the 35th IEEE Conference on Decision and Control (1996), 3080–3085. DOI 10.1109/CDC.1996.573597.
3. S. Datta and D. Chakraborty, “Feedback norm minimisation with regional pole placement,” International Journal of Control 87 (2014), 2239–2251. DOI 10.1080/00207179.2014.908476.
4. R. Schmid, L. Ntogramatzidis, T. Nguyen, and A. Pandey, “A unified method for optimal arbitrary pole placement,” Automatica 50 (2014), 2150–2154. arXiv:1405.1516.
5. H. Yasukata, X. Shen, H. Sasahara, J.-i. Imura, and M. Oku, “Design of input assignment and feedback gain for re-stabilizing undirected networks with High-Dimension Low-Sample-Size data,” International Journal of Robust and Nonlinear Control 33 (2023), 8382–8398. DOI 10.1002/rnc.6720.
