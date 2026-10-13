# LAMB has a sharp dimension-dependent first-step descent threshold
## Finding

LAMB normalizes an Adam-style update to unit Euclidean norm within each layer and then scales that direction by a function of the layer norm. For the source's instructive choice
\[
\phi(z)=z,
\]
the resulting first-step geometry already has a sharp dimension dependence on the simplest isotropic quadratic.

Consider one layer
\[
x\in\mathbb R^d,
\qquad d\ge1,
\]
and
\[
F(x)=\frac12\kappa\lVert x\rVert_2^2,
\qquad \kappa>0.
\]
Start LAMB from zero first and second moments, set weight decay to zero, take
\[
\varepsilon>0,
\qquad
\eta>0,
\]
and use
\[
\phi(z)=z.
\]

At the first step, the Adam-style pre-trust vector has the coordinate form
\[
r_i=\frac{A x_i}{B|x_i|+\varepsilon},
\qquad A,B>0.
\]
The positive constants depend on the precise first-step moment scaling convention, but cancel from the geometric statement below. In particular,
\[
\operatorname{sign}(r_i)=\operatorname{sign}(x_i)
\]
and
\[
|r_i|
\]
is increasing in
\[
|x_i|.
\]

The LAMB layer update is therefore
\[
\boxed{
x^+=x-\eta\lVert x\rVert_2\frac{r}{\lVert r\rVert_2}.
}
\]
Define the alignment
\[
C(x)=
\frac{\langle x,r\rangle}
{\lVert x\rVert_2\lVert r\rVert_2}.
\]
Then
\[
\boxed{
\frac{F(x^+)}{F(x)}
=
1-2\eta C(x)+\eta^2.
}
\]

For every nonzero state,
\[
\boxed{
C(x)\ge\frac1{\sqrt d}.
}
\]
This bound is sharp. For example, with
\[
x^{(M)}=(M^2,M,\ldots,M),
\]
one has
\[
\frac{x^{(M)}}{\lVert x^{(M)}\rVert_2}\longrightarrow e_1,
\]
while saturation of the coordinatewise ratio gives
\[
\frac{r(x^{(M)})}{\lVert r(x^{(M)})\rVert_2}
\longrightarrow
\frac{1}{\sqrt d}(1,\ldots,1).
\]
Hence
\[
C(x^{(M)})\longrightarrow\frac1{\sqrt d}.
\]

Therefore the exact worst first-step objective factor is
\[
\boxed{
\sup_{x\ne0}\frac{F(x^+)}{F(x)}
=
1-\frac{2\eta}{\sqrt d}+\eta^2.
}
\]

Consequently,
\[
\boxed{
F(x^+)\le F(x)\ \text{for every nonzero }x
\iff
0<\eta\le\frac2{\sqrt d}.
}
\]
Moreover, there is a dimension-uniform strict contraction factor below one exactly when
\[
\boxed{
0<\eta<\frac2{\sqrt d}.
}
\]
At
\[
\eta=\frac2{\sqrt d},
\]
the supremum of the objective ratio equals one, so no strict uniform margin remains.

The threshold is independent of
\[
\kappa,
\qquad
\beta_1,
\qquad
\beta_2,
\qquad
\varepsilon
\]
at the first step. It is a geometric effect of the two normalizations rather than curvature conditioning.

## Assumptions and scope

The theorem concerns one deterministic LAMB layer on an isotropic positive quadratic at the first step from zero moment states.

Weight decay is zero. The source scaling choice
\[
\phi(z)=z
\]
is used; the defining paper presents this case as an instructive interpretation of layerwise adaptation. Bounded or clipped scaling functions alter the step-length calculation.

The additive denominator regularizer satisfies
\[
\varepsilon>0.
\]
The result also has a natural zero-regularizer limit, but the theorem is stated for the positive regularizer used in the source algorithm.

The statement is a first-step objective-descent theorem, not a long-run convergence theorem. Later moment history changes the pre-trust direction.

## Proof

Because
\[
\nabla F(x)=\kappa x,
\]
zero first and second moments imply that the first Adam-style pre-trust coordinate can be written
\[
r_i=\frac{A x_i}{B|x_i|+\varepsilon}
\]
for positive constants
\[
A,B.
\]
Thus the signs of
\[
r_i
\]
match those of
\[
x_i,
\]
and the magnitudes of the two vectors have the same coordinate ordering.

Set
\[
a_i=|x_i|,
\qquad
b_i=|r_i|,
\]
and relabel coordinates so that
\[
a_1\ge a_2\ge\cdots\ge a_d\ge0.
\]
Then also
\[
b_1\ge b_2\ge\cdots\ge b_d\ge0.
\]

For
\[
k=1,\ldots,d,
\]
let
\[
e^{(k)}=(\underbrace{1,\ldots,1}_{k},0,\ldots,0).
\]
Every nonnegative nonincreasing vector has the decomposition
\[
b=\sum_{k=1}^d c_k e^{(k)},
\qquad
c_k=b_k-b_{k+1}\ge0,
\]
with
\[
b_{d+1}=0.
\]

Because the first
\[
k
\]
coordinates of
\[
a
\]
contain at least a fraction
\[
k/d
\]
of its squared Euclidean mass,
\[
\sum_{i=1}^k a_i^2
\ge
\frac{k}{d}\lVert a\rVert_2^2.
\]
Therefore
\[
\langle a,e^{(k)}\rangle
=
\sum_{i=1}^k a_i
\ge
\sqrt{\sum_{i=1}^k a_i^2}
\ge
\frac{\lVert a\rVert_2\lVert e^{(k)}\rVert_2}{\sqrt d}.
\]
Multiplying by
\[
c_k
\]
and summing gives
\[
\langle a,b\rangle
\ge
\frac{\lVert a\rVert_2}{\sqrt d}
\sum_k c_k\lVert e^{(k)}\rVert_2.
\]
The triangle inequality gives
\[
\lVert b\rVert_2
=
\left\lVert\sum_k c_k e^{(k)}\right\rVert_2
\le
\sum_k c_k\lVert e^{(k)}\rVert_2.
\]
Hence
\[
\langle a,b\rangle
\ge
\frac{\lVert a\rVert_2\lVert b\rVert_2}{\sqrt d}.
\]
Restoring signs proves
\[
C(x)\ge1/\sqrt d.
\]

Now use the source layerwise normalization with
\[
\phi(\lVert x\rVert_2)=\lVert x\rVert_2.
\]
Expanding the squared norm after one step gives
\[
\begin{aligned}
\lVert x^+\rVert_2^2
&=
\left\lVert
x-\eta\lVert x\rVert_2\frac{r}{\lVert r\rVert_2}
\right\rVert_2^2\\
&=
\lVert x\rVert_2^2
\left(1-2\eta C(x)+\eta^2\right).
\end{aligned}
\]
Since the quadratic objective is proportional to
\[
\lVert x\rVert_2^2,
\]
the objective-ratio formula follows.

The sharp family above proves that the lower bound on
\[
C(x)
\]
cannot be improved. Taking its limit gives the exact supremum objective factor. Solving
\[
1-\frac{2\eta}{\sqrt d}+\eta^2\le1
\]
yields
\[
0<\eta\le2/\sqrt d.
\]
Strict inequality gives the uniform contraction condition.

## Verification

The accompanying `verify.py` reconstructs the first-step pre-trust vector for arbitrary positive source constants and regularizers.

It checks the exact objective-ratio identity, the co-monotone cosine lower bound on randomized vectors, convergence of the sharp family to
\[
1/\sqrt d,
\]
and the sharp descent threshold on dimensions from one through several hundred.

The computations are transcription guards. The universal cosine inequality and the exact supremum are proved analytically above.

## Relationship to prior work

You and coauthors introduce LAMB by combining an Adam-style coordinatewise normalization with a second layerwise normalization. They explain that the layerwise normalization makes the update norm comparable to the parameter norm and specifically identify
\[
\phi(z)=z
\]
as an instructive case. They also note a connection to sign-based updates in a limiting parameter regime.

The defining full text proves general nonconvex convergence under its assumptions but does not state a sharp first-step objective-descent threshold on an isotropic quadratic, nor a dimension-only lower bound on the angle between the parameter and the first pre-trust direction.

Fong, Chen, and Chen later observe that LAMB can experience unstable or extreme trust ratios and introduce clipping. Their full text restates the practical LAMB moment, preconditioning, and trust-ratio updates. It does not state the co-monotone angle bound or the exact
\[
2/\sqrt d
\]
first-step descent threshold.

SignSGD theory already emphasizes dimension-dependent Euclidean versus coordinate-sign geometry. That broader fact is prior work. The finding here is the sharp way that this geometry interacts with LAMB's *second* layerwise norm normalization: even on an isotropic quadratic, the worst first-step alignment is exactly
\[
1/\sqrt d,
\]
which converts directly into the exact universal LAMB descent ceiling.

Focused published-record searches for LAMB first-step quadratic descent, dimension-dependent trust-ratio thresholds, and layerwise-normalized sign geometry did not identify an implication-equivalent result.

## Limitations

The theorem concerns only the first LAMB step from zero moments.

It uses an isotropic quadratic, zero weight decay, and the source choice
\[
\phi(z)=z.
\]

Trust-ratio clipping, bounded scaling functions, or later moment history can change the threshold.

The result is a worst-case layer-state statement and does not claim that typical neural-network layers attain the sharp family.

## References

1. Yang You, Jing Li, Sashank Reddi, Jonathan Hseu, Sanjiv Kumar, Srinadh Bhojanapalli, Xiaodan Song, James Demmel, Kurt Keutzer, and Cho-Jui Hsieh, “Large Batch Optimization for Deep Learning: Training BERT in 76 minutes,” arXiv:1904.00962v1, first submitted 2019-04-01; ICLR 2020.
2. Jeffrey Fong, Siwei Chen, and Kaiqi Chen, “Improving Layer-wise Adaptive Rate Methods using Trust Ratio Clipping,” arXiv:2011.13584v1, 2020.
3. Jeremy Bernstein, Yu-Xiang Wang, Kamyar Azizzadenesheli, and Anima Anandkumar, “signSGD: Compressed Optimisation for Non-Convex Problems,” arXiv:1802.04434v1, 2018.
