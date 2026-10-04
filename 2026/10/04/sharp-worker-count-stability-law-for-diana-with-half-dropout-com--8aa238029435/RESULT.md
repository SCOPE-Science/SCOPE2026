# Sharp worker-count stability law for DIANA with half-dropout compression
## Finding

Consider \(n\ge1\) workers with scalar local objectives
\[
f_i(x)=\frac{\mu}{2}x^2+b_i x,
\qquad
\mu>0,
\qquad
\sum_{i=1}^n b_i=0.
\]
The global objective is therefore
\[
f(x)=\frac{\mu}{2}x^2,
\]
with minimizer \(x^\star=0\).

Use DIANA without momentum or a regularizer. Each worker has a shift \(h_i\), forms
\[
\Delta_i=\nabla f_i(x)-h_i,
\]
and applies the independent unbiased half-dropout compressor
\[
\mathcal C_i(u)=2\xi_i u,
\qquad
\xi_i\sim\operatorname{Bernoulli}\!\left(\frac12\right).
\]
This compressor has variance parameter \(1\). Use the standard DIANA shift learning rate
\[
\lambda=\frac12.
\]
Thus
\[
h_i^+=h_i+\frac12\mathcal C_i(\Delta_i),
\]
the server estimator is
\[
\widehat g
=
\frac1n\sum_{i=1}^n
\left[h_i+\mathcal C_i(\Delta_i)\right],
\]
and
\[
x^+=x-\gamma\widehat g.
\]
Put
\[
s=\gamma\mu.
\]

Then DIANA is exponentially stable in mean square exactly when
\[
0<s<s_n,
\]
where
\[
s_n
=
\frac{n-4+\sqrt{9n^2+8n+16}}{2(n+2)}.
\]

At \(s=s_n\), the exact second-moment recursion has eigenvalue \(1\). For every \(s>s_n\), a necessary Schur condition fails, so the method is not mean-square stable.

The threshold is strictly increasing in the number of workers. In particular,
\[
s_1=\frac{\sqrt{33}-3}{6}\approx0.457427,
\]
\[
s_2=\frac{\sqrt{17}-1}{4}\approx0.780776,
\]
\[
s_3=1,
\]
and
\[
\lim_{n\to\infty}s_n=2.
\]
More precisely,
\[
s_n
=
2-\frac{16}{3n}
+\frac{320}{27n^2}
+O\!\left(n^{-3}\right).
\]

Hence independent worker averaging has an exact stability meaning on this benchmark: with one worker, unbiased half-dropout plus DIANA memory permits less than one quarter of the uncompressed positive-quadratic ceiling \(2/\mu\), while increasing the worker count continuously restores that ceiling.

The offsets \(b_i\) do not affect the threshold. DIANA's shift mechanism absorbs them exactly after centering.

## Assumptions and scope

The result uses deterministic local gradients, equal scalar curvature \(\mu\), arbitrary affine offsets summing to zero, independent compressor coins across workers and iterations, no momentum, no regularizer, a constant model stepsize \(\gamma\), and the usual DIANA shift learning rate \(\lambda=1/(1+\omega)=1/2\) for an unbiased compressor with variance parameter \(\omega=1\).

The half-dropout compressor is the simplest nontrivial scalar unbiased sparsifier:
\[
\mathbb E[\mathcal C_i(u)]=u,
\qquad
\mathbb E\!\left[(\mathcal C_i(u)-u)^2\right]=u^2.
\]

Mean-square stability means geometric decay of
\[
\mathbb E\!\left[
x_k^2+\frac1n\sum_{i=1}^n e_{i,k}^2
\right]
\]
for every square-integrable initial state independent of future compressor randomness, where
\[
e_i=\frac{h_i-b_i}{\mu}.
\]

The theorem does not cover unequal local curvatures, correlated compressors, stochastic gradient noise, other dropout probabilities, momentum, or adaptive shift learning rates.

## Proof

Center the worker shifts by defining
\[
e_i=\frac{h_i-b_i}{\mu},
\qquad
\bar e=\frac1n\sum_{i=1}^n e_i.
\]
Since
\[
\nabla f_i(x)=\mu x+b_i,
\]
the gradient difference becomes
\[
\Delta_i=\mu(x-e_i).
\]
Therefore the affine offsets disappear completely from the dynamics.

With \(\xi_i\in\{0,1\}\),
\[
e_i^+
=
e_i+\xi_i(x-e_i).
\]
Also,
\[
\frac{\widehat g}{\mu}
=
\bar e
+
\frac2n
\sum_{i=1}^n
\xi_i(x-e_i).
\]
Write
\[
z=
\frac{\widehat g}{\mu}.
\]
Conditioned on the current state,
\[
\mathbb E[z]=x.
\]
Independence and
\[
\operatorname{Var}(\xi_i)=\frac14
\]
give
\[
\mathbb E[z^2]
=
x^2
+
\frac1n
\left(
x^2-2x\bar e+\frac1n\sum_{i=1}^n e_i^2
\right).
\]

Now define
\[
X_k=\mathbb E[x_k^2],
\qquad
Y_k=\mathbb E[x_k\bar e_k],
\qquad
W_k=
\mathbb E\!\left[
\frac1n\sum_{i=1}^n e_{i,k}^2
\right].
\]
Because
\[
x^+=x-sz,
\]
one obtains
\[
X^+
=
\left[(1-s)^2+\frac{s^2}{n}\right]X
-\frac{2s^2}{n}Y
+\frac{s^2}{n}W.
\]

The shift average satisfies the exact identity
\[
\bar e^+=\frac{z+\bar e}{2}.
\]
Hence
\[
Y^+
=
\frac{n(1-s)-s}{2n}X
+
\left[
\frac{1-s}{2}+\frac{s}{n}
\right]Y
-\frac{s}{2n}W.
\]

Finally,
\[
\mathbb E[(e_i^+)^2\mid x,e_i]
=
\frac12x^2+\frac12e_i^2,
\]
so
\[
W^+=\frac12X+\frac12W.
\]

Thus
\[
\begin{bmatrix}
X^+\\
Y^+\\
W^+
\end{bmatrix}
=
M_n(s)
\begin{bmatrix}
X\\
Y\\
W
\end{bmatrix},
\]
where
\[
M_n(s)=
\begin{bmatrix}
(1-s)^2+s^2/n & -2s^2/n & s^2/n\\
[n(1-s)-s]/(2n) & (1-s)/2+s/n & -s/(2n)\\
1/2 & 0 & 1/2
\end{bmatrix}.
\]

Let
\[
P(z)=\det(zI-M_n(s))
=
z^3+a_1z^2+a_2z+a_3.
\]
Direct expansion gives
\[
a_1
=
-\frac{
2(n+1)s^2+(2-5n)s+4n
}{2n},
\]
\[
a_2
=
-\frac{
2(n+1)s^3+(2-8n)s^2+(11n-6)s-5n
}{4n},
\]
and
\[
a_3
=
\frac{
(s-1)\left[n(s-1)^2+2s\right]
}{4n}.
\]

For a real monic cubic, the Jury conditions are
\[
1+a_1+a_2+a_3>0,
\]
\[
1-a_1+a_2-a_3>0,
\]
\[
1-a_3>0,
\qquad
1+a_3>0,
\]
and
\[
1-a_2+a_1a_3-a_3^2>0.
\]

The first condition factors as
\[
1+a_1+a_2+a_3
=
\frac{s}{4n}
\left[
n(2+s-s^2)-2s(s+2)
\right].
\]
For \(0<s<2\), define
\[
N(s)
=
\frac{2s(s+2)}{(2-s)(s+1)}.
\]
Then the first Jury condition is exactly
\[
n>N(s).
\]
Since
\[
N'(s)
=
\frac{
2(3s^2+4s+4)
}{
(2-s)^2(s+1)^2
}>0,
\]
there is a unique positive boundary. Solving \(n=N(s)\) gives
\[
s=s_n
=
\frac{
n-4+\sqrt{9n^2+8n+16}
}{
2(n+2)
}.
\]

It remains to show that the other Jury inequalities cannot fail earlier.

For the second condition,
\[
1-a_1+a_2-a_3
=
-\frac{
3n(s-3)(s^2-2s+2)+2s(s^2-6)
}{4n}.
\]
Both terms in the numerator are negative for \(0<s<2\), so this quantity is positive.

For \(1+a_3\),
\[
1+a_3
=
\frac{
n[(s-1)^3+4]+2s(s-1)
}{4n}>0
\]
throughout \(0<s<2\). If \(s\le1\), then \(1-a_3>0\) is immediate. If \(1<s<s_n\), then necessarily \(n\ge4\), and
\[
n[4-(s-1)^3]>12>2s(s-1),
\]
so \(1-a_3>0\).

For the final Jury quantity, write
\[
1-a_2+a_1a_3-a_3^2
=
-\frac{G_n(s)}{16n^2},
\]
where
\[
G_n(s)=n^2A(s)+nB(s)+C(s),
\]
with
\[
A(s)
=
(s+3)(s^2-2s-1)\bigl[(s-1)^3+2\bigr],
\]
\[
B(s)
=
4s(s-2)(s+1)(2s^2-2s-1),
\]
\[
C(s)
=
4s^2(s-1)(3s+1).
\]
For \(0<s<2\),
\[
A(s)<0.
\]
At \(n=N(s)\),
\[
G_{N(s)}(s)
=
\frac{
4s^3(s^3-3s-8)
(s^4-2s^3-s^2+10s+4)
}{
(2-s)^2(s+1)^2
}<0.
\]
Indeed, \(s^3-3s-8<0\) on \((0,2)\), while
\[
s^4-2s^3-s^2+10s+4>0.
\]
For \(0<s\le1\), the latter is at least \(7s+4\). For \(1\le s<2\), it is at least \(2\).

Moreover,
\[
\left.
\frac{\partial G_n(s)}{\partial n}
\right|_{n=N(s)}
=
\frac{
4sH(s)
}{
(2-s)(s+1)
},
\]
where
\[
H(s)
=
s^7-2s^6-5s^5+11s^4+17s^3-41s^2-23s-2.
\]
Write
\[
H(s)
=
s^6(s-2)
+
s^2(-5s^3+11s^2+17s-41)
-23s-2.
\]
The cubic in parentheses is increasing on \((0,2)\) and equals \(-3\) at \(s=2\), so it is negative throughout. Hence
\[
H(s)<0.
\]
Because \(A(s)<0\), the derivative of \(G_n(s)\) decreases with \(n\). Therefore
\[
n>N(s)
\quad\Longrightarrow\quad
G_n(s)<G_{N(s)}(s)<0.
\]
The final Jury inequality is thus positive everywhere before the first condition becomes tight.

All five Jury conditions therefore hold exactly for
\[
0<s<s_n.
\]
At \(s=s_n\),
\[
P(1)=0,
\]
so \(1\) is an eigenvalue of the second-moment operator. For \(s>s_n\), the necessary condition \(P(1)>0\) fails. This proves the sharp mean-square stability frontier.

The monotonicity of \(s_n\) follows from the strict monotonicity of \(N(s)\). Expanding the closed form at large \(n\) gives
\[
s_n
=
2-\frac{16}{3n}
+\frac{320}{27n^2}
+O(n^{-3}).
\]

## Verification

The accompanying `verify.py` reconstructs the moment recursion from explicit Bernoulli branch averaging for several worker counts using exact rational arithmetic. It separately checks the characteristic-polynomial coefficients, all five cubic Jury expressions, the boundary identity \(P(1)=0\), and numerical eigenvalue crossing immediately below and above the analytic threshold.

The finite tests are algebra and transcription guards. The exact frontier is established by the analytic Jury proof above.

## Relationship to prior work

Mishchenko, Gorbunov, Takáč, and Richtárik introduced DIANA as a distributed method that compresses gradient differences while maintaining worker-specific shifts that learn the gradients at the optimum. The defining algorithm updates the shifts from compressed differences and forms the server direction from the old shifts plus compressed differences. Their strongly convex analysis gives sufficient convergence conditions, but the inspected full text does not derive an exact quadratic mean-square stability boundary as a function of worker count.

Condat, Yi, and Richtárik later placed DIANA in a framework for arbitrary unbiased compressors. They explicitly identify DIANA as the case using unbiased compressors with bounded variance and state the usual shift scaling
\[
\lambda=\frac{1}{1+\omega}.
\]
For the half-dropout compressor used here,
\[
\omega=1,
\]
so the canonical choice is exactly \(\lambda=1/2\). Their analysis also emphasizes that independent compressor randomness improves behavior as the number of workers grows, but it does not give the exact interpolation
\[
s_n
=
\frac{
n-4+\sqrt{9n^2+8n+16}
}{
2(n+2)
}
\]
or its sharp approach to the gradient-descent ceiling.

Targeted searches for DIANA, unbiased Bernoulli compression, scalar quadratics, mean-square stability, Schur boundaries, and worker-count scaling did not identify a source stating or implying this exact law.

## Limitations

The theorem fixes half-dropout probability and the corresponding canonical shift learning rate. Other dropout probabilities produce a different cubic moment operator.

All local Hessians are equal. The affine offsets may be arbitrary subject to zero average, but unequal curvatures introduce additional coupled modes.

Compressor coins are independent across workers and time. Shared or correlated compression can change the worker-count scaling.

The result concerns mean-square asymptotic stability, not transient monotonicity of every sample path or communication-optimal tuning.

The formula is an exact benchmark for the DIANA memory mechanism, not a claim that practical distributed objectives are one-dimensional or curvature-homogeneous.

## References

1. Konstantin Mishchenko, Eduard Gorbunov, Martin Takáč, and Peter Richtárik, “Distributed Learning with Compressed Gradient Differences,” arXiv:1901.09269v1, 2019.
2. Laurent Condat, Kai Yi, and Peter Richtárik, “EF-BV: A Unified Theory of Error Feedback and Variance Reduction Mechanisms for Biased and Unbiased Compression in Distributed Optimization,” arXiv:2205.04180v1, 2022.
