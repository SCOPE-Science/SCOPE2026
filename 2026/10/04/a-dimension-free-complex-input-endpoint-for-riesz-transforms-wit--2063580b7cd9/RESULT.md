# A dimension-free complex-input endpoint for Riesz transforms with constant drift

## Finding

Let
\[
L_v=-\Delta-2v\cdot\nabla
\]
on
\[
L^2(\mathbb R^n,\mu_v),
\qquad
d\mu_v(x)=e^{2v\cdot x}\,dx,
\qquad
v\in\mathbb R^n\setminus\{0\},
\]
and let
\[
R_v=\nabla L_v^{-1/2}.
\]
Complexify the real weak-\(L^1\) extension componentwise:
\[
R_v^{\mathbb C}(a+ib)=R_va+iR_vb
\]
for real-valued \(a,b\).

Then every
\[
f\in L^1(\mu_v;\mathbb C)
\]
satisfies
\[
\|R_v^{\mathbb C}f\|_{L^{1,\infty}(\mu_v;\mathbb C^n)}
\le
C_{\mathbb C}\|f\|_{L^1(\mu_v)},
\]
uniformly in the dimension and in the magnitude and direction of the drift, where
\[
C_{\mathbb C}
=
\frac{2}{c_*\arccos c_*}
=
3.564450280406266\ldots .
\]
Here
\[
c_*=\cos\theta_*
=
0.652184623909186\ldots
\]
and
\[
\theta_*\in(\pi/4,\pi/2)
\]
is the unique solution of
\[
\theta_*\tan\theta_*=1.
\]

This improves the elementary separate-real-and-imaginary transfer, which gives constant \(4\), while retaining complete dimension and drift independence. No claim is made that \(C_{\mathbb C}\) is the optimal complex weak-\(L^1\) constant.

## Assumptions and scope

The target norm on
\[
\mathbb C^n
\]
is the Euclidean norm
\[
|z|^2=\sum_{j=1}^n|z_j|^2.
\]
The weak norm is
\[
\|F\|_{L^{1,\infty}(\mu_v)}
=
\sup_{t>0}
t\,\mu_v(\{|F|>t\}).
\]

The motivating theorem gives, for real-valued data,
\[
\|R_v f\|_{L^{1,\infty}(\mu_v;\mathbb R^n)}
\le
2\|f\|_{L^1(\mu_v)}.
\]
Its construction is explicitly real: the obstacle decomposition is performed for nonnegative data and signed data are treated through positive and negative parts. The underlying \(L^2\) realization is nevertheless compatible with complex functions, and the paper records the complex weighted Sobolev identity.

The result here concerns the natural complexification of that real operator. It does not improve the source constant \(2\) for real data and does not assert the best possible constant for complex data.

## Proof

We first prove a geometric rotation lemma.

Let
\[
z=a+ib\in\mathbb C^n,
\qquad
a,b\in\mathbb R^n,
\]
and normalize
\[
|z|=1.
\]
For
\[
\theta\in[0,2\pi]
\]
set
\[
q_z(\theta)
=
|\operatorname{Re}(e^{-i\theta}z)|^2
=
|a\cos\theta+b\sin\theta|^2.
\]

The real symmetric Gram matrix of \(a\) and \(b\) has trace one. After translating the angular variable, there is
\[
\lambda\in[1/2,1]
\]
such that
\[
q_z(\theta)
=
\lambda\cos^2\theta+(1-\lambda)\sin^2\theta.
\]
Fix
\[
0<c\le2^{-1/2}.
\]
If
\[
c^2\le1-\lambda,
\]
then
\[
q_z(\theta)\ge c^2
\]
for every angle. Otherwise,
\[
q_z(\theta)>c^2
\]
is equivalent to
\[
|\cos\theta|>t_\lambda,
\]
where
\[
t_\lambda^2
=
\frac{c^2-(1-\lambda)}{2\lambda-1}.
\]
Since
\[
c^2\le\frac12,
\]
one has
\[
t_\lambda^2\le c^2,
\]
because this inequality is equivalent to
\[
(1-\lambda)(1-2c^2)\ge0.
\]
Hence
\[
\left|
\left\{
\theta:
|\operatorname{Re}(e^{-i\theta}z)|>c|z|
\right\}
\right|
\ge
4\arccos c.
\]
This is sharp for the geometric lemma when the real and imaginary parts of \(z\) are collinear.

Now let
\[
f\in L^1(\mu_v;\mathbb C)
\]
and define
\[
f_\theta
=
\operatorname{Re}(e^{-i\theta}f).
\]
It is real-valued, and by complex linearity of the complexified transform,
\[
R_v f_\theta
=
\operatorname{Re}(e^{-i\theta}R_v^{\mathbb C}f).
\]

If
\[
|R_v^{\mathbb C}f(x)|>s,
\]
the rotation lemma implies
\[
\left|
\left\{
\theta:
|R_v f_\theta(x)|>cs
\right\}
\right|
\ge
4\arccos c.
\]
Therefore
\[
\mathbf 1_{\{|R_v^{\mathbb C}f|>s\}}(x)
\le
\frac1{4\arccos c}
\int_0^{2\pi}
\mathbf 1_{\{|R_vf_\theta|>cs\}}(x)\,d\theta.
\]
Integrating in \(x\) and using the real weak-\(L^1\) theorem gives
\[
\mu_v(\{|R_v^{\mathbb C}f|>s\})
\le
\frac1{4\arccos c}
\int_0^{2\pi}
\frac{2}{cs}\|f_\theta\|_{L^1(\mu_v)}
\,d\theta.
\]

For every scalar \(w\in\mathbb C\),
\[
\int_0^{2\pi}
|\operatorname{Re}(e^{-i\theta}w)|\,d\theta
=
4|w|.
\]
Tonelli's theorem therefore yields
\[
\int_0^{2\pi}
\|f_\theta\|_{L^1(\mu_v)}
\,d\theta
=
4\|f\|_{L^1(\mu_v)}.
\]
Thus
\[
s\,\mu_v(\{|R_v^{\mathbb C}f|>s\})
\le
\frac{2}{c\arccos c}
\|f\|_{L^1(\mu_v)}.
\]

It remains to optimize the one-variable factor. Writing
\[
c=\cos\theta,
\qquad
\theta\in[\pi/4,\pi/2),
\]
amounts to maximizing
\[
\theta\cos\theta.
\]
Its derivative vanishes precisely when
\[
\cos\theta-\theta\sin\theta=0,
\]
or
\[
\theta\tan\theta=1.
\]
There is a unique solution in the interval, and it gives the displayed values of
\[
\theta_*,
\qquad
c_*,
\qquad
C_{\mathbb C}.
\]
Taking the supremum over \(s>0\) completes the proof.

## Verification

The source theorem was checked in the full primary text: it assumes real-valued \(L^1\) data, gives the full-vector constant \(2\), and is uniform in both dimension and drift. The same text explicitly notes that its exact weighted \(L^2\) identity remains valid for complex functions.

The rotation lemma was reconstructed from the two-by-two Gram matrix of the real and imaginary parts of a vector in
\[
\mathbb C^n.
\]
Its only restriction,
\[
c\le2^{-1/2},
\]
contains the optimizer
\[
c_*=0.652184623909186\ldots .
\]
The optimization equation was solved from the exact derivative condition
\[
\theta\tan\theta=1;
\]
the decimal values are only evaluations of this exact characterization.

The proof does not use dimension-dependent coordinate estimates, finite-dimensional enumeration, or an unproved complex obstacle decomposition.

## Relationship to prior work

Mukherjee's 2026 theorem establishes the constant-\(2\) dimension-free endpoint for real-valued functions and explicitly formulates its main theorem in that real setting. Its proof uses positivity and a positive/negative decomposition, so a complex-input theorem is not a literal instance of the stated obstacle argument.

Ouyang, Spector, and Stockdale prove the corresponding dimension-free Euclidean vector-Riesz estimate and likewise derive it from a positive obstacle decomposition followed by positive and negative parts. Their theorem is a zero-drift predecessor and does not imply the constant-drift statement through translation or scaling, because the exponentially weighted measure and drift operator are different.

Earlier work of Li, Sjögren, and Wu proves weak type \((1,1)\) for the constant-drift Riesz transform uniformly in the drift vector, but the 2026 source records that the earlier statement does not give a dimension-independent constant. Thus it cannot supply the present dimension-free complex estimate.

The present argument is instead a Hilbert-target rotation transfer: it uses every real phase
\[
\operatorname{Re}(e^{-i\theta}f)
\]
simultaneously and exploits the exact angular measure of large real projections. Candidate-specific searches for complex-valued input, complexification, rotational realification, constant drift, and dimension-free weak type did not locate a published statement of this quantitative extension.

## Limitations

The constant
\[
C_{\mathbb C}=3.564450280406266\ldots
\]
is an explicit upper bound, not a claimed optimum for complex-valued data.

The proof uses the Euclidean Hilbert norm on the vector target. Different target norms would require a different angular projection lemma.

No complex-valued obstacle decomposition is constructed. The method deliberately transfers the verified real theorem by rotation instead.

## References

1. S. Mukherjee, *Dimension-free weak \((1,1)\) estimates for Riesz transforms with constant drift*, arXiv:2609.21458v2, 2026.
2. Y. Ouyang, D. Spector, and C. B. Stockdale, *A dimension-free weak-type \((1,1)\) bound for the vector Riesz transform on \(\mathbb R^n\)*, arXiv:2608.18068v1, 2026.
3. H.-Q. Li, P. Sjögren, and Y. Wu, *Weak type \((1,1)\) of some operators for the Laplacian with drift*, Mathematische Zeitschrift 282 (2016), 623--633.
