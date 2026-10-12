# Two-client SCAFFOLD can stabilize a locally divergent client
## Finding

Consider deterministic, full-participation SCAFFOLD with two clients, Option II for the client control variates, server step
\[
\eta_g=1,
\]
and
\[
K\ge 1
\]
local steps of size
\[
\eta>0.
\]

Let the client objectives be the scalar strongly convex quadratics
\[
f_i(x)=\frac{a_i}{2}x^2,
\qquad
a_i>0,
\qquad
i\in\{1,2\}.
\]
Write the server control as the exact client average
\[
c=\frac{c_1+c_2}{2},
\]
which is the invariant maintained by the source algorithm under full participation, and define the control difference
\[
d=\frac{c_1-c_2}{2}.
\]

For
\[
z_i=1-\eta a_i,
\qquad
p_i=z_i^K,
\qquad
s_i=\frac{1}{K}\sum_{j=0}^{K-1}z_i^j,
\]
one complete SCAFFOLD communication round is exactly
\[
\begin{bmatrix}
x^+\\
d^+
\end{bmatrix}
=
A
\begin{bmatrix}
x\\
d
\end{bmatrix},
\]
with
\[
\boxed{
A=
\begin{bmatrix}
\dfrac{p_1+p_2}{2}
&
\dfrac{K\eta(s_1-s_2)}{2}
\\[6pt]
\dfrac{p_2-p_1}{2K\eta}
&
1-\dfrac{s_1+s_2}{2}
\end{bmatrix}.
}
\]

This exact reduction yields two stability facts.

First, if each client's local gradient step is individually contractive,
\[
|z_1|<1,
\qquad
|z_2|<1,
\]
then the SCAFFOLD round matrix is Schur stable for every
\[
K\ge1.
\]
Thus, on this two-client scalar family, increasing the number of local steps imposes no additional round-level stability restriction once both local gradient maps are themselves stable.

Second, that local condition is not necessary. Take
\[
\eta=1,
\qquad
K=3,
\qquad
a_1=\frac{11}{5},
\qquad
a_2=\frac{1}{10}.
\]
Then
\[
z_1=-\frac65,
\qquad
z_2=\frac9{10}.
\]
The first client's isolated local gradient iteration is unstable, and after three local steps its homogeneous endpoint factor is
\[
p_1=
\left(-\frac65\right)^3
=
-\frac{216}{125},
\]
whose magnitude exceeds one.

Nevertheless the exact SCAFFOLD round matrix is
\[
\boxed{
A=
\begin{bmatrix}
-\dfrac{999}{2000} & -\dfrac{147}{200}\\[6pt]
\dfrac{819}{2000} & \dfrac{41}{120}
\end{bmatrix}.
}
\]
Its trace and determinant are
\[
\operatorname{tr}(A)=-\frac{947}{6000},
\qquad
\det(A)=\frac{1629}{12500}.
\]
The discriminant is
\[
\operatorname{tr}(A)^2-4\det(A)
=
-\frac{17869271}{36000000}<0.
\]
Hence the eigenvalues are a complex-conjugate pair with common modulus
\[
\boxed{
\rho(A)
=
\sqrt{\frac{1629}{12500}}
\approx 0.360999<1.
}
\]

So SCAFFOLD can stabilize a communication-round dynamics even though one participating client's local solver is linearly divergent in isolation.

## Assumptions and scope

The result uses the source SCAFFOLD update with Option II,
\[
c_i^+
=
c_i-c+\frac{x-y_i}{K\eta},
\]
full participation, deterministic exact gradients, and
\[
\eta_g=1.
\]

The objectives are two scalar quadratics sharing the minimizer
\[
x^\star=0
\]
but having different positive curvatures. This isolates Hessian heterogeneity from gradient noise, client sampling, and shifted local optima.

The theorem is a linear stability statement for the exact round map. It does not claim that arbitrarily unstable local solvers are globally stabilized, nor does it extend the witness automatically to more than two clients, vector-valued coupled Hessians, stochastic gradients, partial participation, or other SCAFFOLD control updates.

## Proof

The source client update is
\[
y_i\leftarrow
y_i-\eta\bigl(\nabla f_i(y_i)+c-c_i\bigr).
\]
Because
\[
\nabla f_i(y)=a_i y,
\]
and
\[
c-c_1=-d,
\qquad
c-c_2=d,
\]
the local recurrences are
\[
y_{1,k+1}=z_1 y_{1,k}+\eta d,
\]
and
\[
y_{2,k+1}=z_2 y_{2,k}-\eta d,
\]
with
\[
y_{1,0}=y_{2,0}=x.
\]

Summing the geometric series gives
\[
y_1=p_1x+K\eta s_1d,
\]
and
\[
y_2=p_2x-K\eta s_2d.
\]
Since
\[
\eta_g=1
\]
and both clients participate,
\[
x^+=\frac{y_1+y_2}{2},
\]
which is the first row of the displayed matrix.

For Option II,
\[
c_i^+
=
c_i-c+\frac{x-y_i}{K\eta}.
\]
Therefore
\[
d^+
=
\frac{c_1^+-c_2^+}{2}
=
d+\frac{y_2-y_1}{2K\eta},
\]
which gives the second row.

Now assume
\[
|z_1|<1,
\qquad
|z_2|<1.
\]
Then
\[
-1<p_i<1
\]
and
\[
0<s_i<1.
\]
For a real \(2\times2\) matrix with characteristic polynomial
\[
\lambda^2-T\lambda+D,
\]
Schur stability is equivalent to the three Jury inequalities
\[
1-T+D>0,
\qquad
1+T+D>0,
\qquad
1-D>0.
\]

Direct substitution gives
\[
1-T+D
=
\frac{
s_1(1-p_2)+s_2(1-p_1)
}{2}
>0.
\]

Also
\[
1+T+D
=
2+p_1+p_2
-
\frac{
s_2(1+p_1)+s_1(1+p_2)
}{2}.
\]
Since
\[
0<s_i<1
\]
and
\[
1+p_i>0,
\]
the right-hand side is strictly larger than
\[
1+\frac{p_1+p_2}{2}>0.
\]

Finally,
\[
1-D
=
1-\frac{p_1+p_2}{2}
+\frac{p_1s_2+p_2s_1}{2}.
\]
If both \(p_i\) are nonnegative, this is positive because
\[
p_1+p_2<2.
\]
If exactly one is negative, say
\[
p_2<0\le p_1,
\]
then
\[
p_2s_1>p_2
\]
and
\[
p_1s_2\ge0,
\]
so
\[
1-D
>
1-\frac{p_1}{2}>0.
\]
If both are negative, then
\[
p_1s_2>p_1,
\qquad
p_2s_1>p_2,
\]
and therefore
\[
1-D>1.
\]
All three Jury inequalities hold.

For the explicit witness,
\[
z_1=-\frac65,
\qquad
z_2=\frac9{10},
\]
so
\[
p_1=-\frac{216}{125},
\qquad
p_2=\frac{729}{1000},
\]
and
\[
s_1=\frac{31}{75},
\qquad
s_2=\frac{271}{300}.
\]
Substitution yields the stated rational matrix. Its negative discriminant and determinant less than one prove the exact spectral-radius formula and strict linear stability.

## Verification

The accompanying `verify.py` reconstructs the source Option-II round directly from local iterations and independently from the closed matrix formula.

It tests random locally contractive pairs for many values of
\[
K,
\]
checks all three Jury inequalities, verifies that direct client-level simulation agrees with the reduced \(2\times2\) map, and checks the exact rational unstable-client witness.

Finite computation is used only as a transcription guard. The stability implication and the explicit counterexample to necessity are proved analytically above.

## Relationship to prior work

Karimireddy and coauthors introduced SCAFFOLD to correct client drift with control variates. Their Algorithm 1 gives the exact local update and Option-II control update used here. Their quadratic theory shows that local steps become more useful as client Hessians become more similar, and their simulated study explicitly uses two quadratic clients.

That source gives convergence-rate bounds and a similarity-dependent sufficient analysis. The inspected paper does not state the exact two-state round matrix above, prove the all-\(K\) Jury region
\[
|1-\eta a_i|<1,
\]
or exhibit a stable SCAFFOLD round containing a locally divergent client step.

Zhang and coauthors later place SCAFFOLD inside a stochastic multi-rate control framework. Their inspected classification and full-text searches model SCAFFOLD generically as a multi-rate distributed algorithm but do not give the two-client scalar spectral classification or the unstable-local-client witness above.

Luo and coauthors later revisit LocalSGD and SCAFFOLD convergence under similarity and smoothness assumptions, broadening rate theory beyond the original quadratic setting. Their published abstract and summary emphasize convergence-rate improvements rather than a sharp two-client Option-II round spectrum.

Focused indexed-record searches for SCAFFOLD, its source identifier, Option-II spectral radius, sharp local-step stability, and stabilization of an unstable local client did not identify an implication-equivalent result.

## Limitations

The guarantee
\[
|z_i|<1
\]
is sufficient rather than necessary. The explicit
\[
K=3
\]
example proves that the true stable region extends beyond it but does not classify that entire larger region.

The proof is specific to two scalar clients and exact full participation.

The result concerns linear stability of the deterministic round map. It does not by itself quantify stochastic stationary error, communication complexity, or finite-time optimization error for general federated objectives.

## References

1. Sai Praneeth Karimireddy, Satyen Kale, Mehryar Mohri, Sashank J. Reddi, Sebastian U. Stich, and Ananda Theertha Suresh, “SCAFFOLD: Stochastic Controlled Averaging for Federated Learning,” arXiv:1910.06378v1, first submitted 2019-10-14; PMLR 119, 2020.
2. Xinwei Zhang, Mingyi Hong, Sairaj Dhople, and Nicola Elia, “A Stochastic Multi-Rate Control Framework For Modeling Distributed Optimization Algorithms,” PMLR 162, 2022.
3. Ruichen Luo, Sebastian U. Stich, Samuel Horváth, and Martin Takáč, “Revisiting LocalSGD and SCAFFOLD: Improved Rates and Missing Analysis,” PMLR 258, 2025.
