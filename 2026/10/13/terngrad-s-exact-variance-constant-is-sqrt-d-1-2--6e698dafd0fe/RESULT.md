# TernGrad's exact variance constant is \((\sqrt d-1)/2\)
## Finding

TernGrad replaces a vector by an unbiased ternary random vector using its largest coordinate magnitude as a shared scale. For a nonzero
\[
g\in\mathbb R^d,
\]
write
\[
M=\|g\|_\infty.
\]
The source quantizer has coordinates
\[
Q(g)_i
=
M\,\operatorname{sign}(g_i)B_i,
\]
where the \(B_i\) are independent Bernoulli variables satisfying
\[
\mathbb P(B_i=1)
=
\frac{|g_i|}{M}.
\]

The exact first two moments are
\[
\mathbb E[Q(g)]=g
\]
and
\[
\mathbb E\|Q(g)\|_2^2
=
M\|g\|_1.
\]
Therefore
\[
\mathbb E\|Q(g)-g\|_2^2
=
M\|g\|_1-\|g\|_2^2.
\]

The sharp dimension-only ratio is
\[
\boxed{
\sup_{g\ne0}
\frac{\|g\|_\infty\|g\|_1}{\|g\|_2^2}
=
\frac{\sqrt d+1}{2}.
}
\]
Consequently the **smallest** constant for which source-form TernGrad belongs to the standard class of unbiased compressors with relative variance at most \(\omega\) is
\[
\boxed{
\omega_\star
=
\frac{\sqrt d-1}{2}.
}
\]

For
\[
d\ge2,
\]
equality holds exactly, up to permutation, independent signs, and nonzero common scale, when one coordinate has maximal magnitude and all other coordinates have magnitude
\[
\frac{1}{\sqrt d+1}
\]
times that maximum. For
\[
d=1,
\]
the variance is identically zero.

A widely used compression summary lists ternary quantization with the valid sufficient variance parameter
\[
\sqrt d-1.
\]
The sharp constant above is exactly half of that value for every
\[
d>1.
\]
Thus the improvement is not merely asymptotic.

There is also an exact optimization consequence. Consider the isotropic strongly convex quadratic
\[
f(x)
=
\frac L2\|x\|_2^2,
\qquad
L>0,
\]
and the deterministic compressed-gradient update
\[
x^+
=
x-\eta Q(Lx).
\]
Let
\[
h=\eta L.
\]
Then, conditional on every nonzero \(x\),
\[
\frac{\mathbb E[f(x^+)\mid x]}{f(x)}
=
1-2h
+
h^2
\frac{\|x\|_\infty\|x\|_1}{\|x\|_2^2}.
\]
Hence
\[
\boxed{
\sup_{x\ne0}
\frac{\mathbb E[f(x^+)\mid x]}{f(x)}
=
1-2h+\frac{\sqrt d+1}{2}h^2.
}
\]

Uniform strict expected objective descent holds exactly for
\[
\boxed{
0<h<\frac{4}{\sqrt d+1}.
}
\]
The unique minimax normalized step is
\[
\boxed{
h_\star
=
\frac{2}{\sqrt d+1},
}
\]
and its exact worst factor is
\[
\boxed{
\rho_\star
=
\frac{\sqrt d-1}{\sqrt d+1}.
}
\]

The uncompressed exact-solve step
\[
h=1
\]
has sharp TernGrad factor
\[
\frac{\sqrt d-1}{2}.
\]
It is neutral at
\[
d=9
\]
and strictly increases the expected objective on a sharp direction for every
\[
d\ge10.
\]

## Assumptions and scope

The variance theorem concerns one source-form TernGrad quantization bucket. It applies to any deterministic input vector in
\[
\mathbb R^d.
\]

The optimization corollary uses one deterministic compressed gradient on the isotropic quadratic. The only randomness is TernGrad's independent coordinatewise Bernoulli rounding.

No gradient clipping, multiple workers, shared cross-worker scaling, error feedback, momentum, or stochastic-gradient sampling is used.

The result identifies the minimal uniform variance parameter for this quantizer. It does not claim that every convergence theorem using a looser compressor parameter automatically becomes sharp after substituting the new constant.

## Proof

Unbiasedness follows immediately from the source Bernoulli probabilities:
\[
\mathbb E[Q(g)_i]
=
M\operatorname{sign}(g_i)
\frac{|g_i|}{M}
=
g_i.
\]
Likewise,
\[
\mathbb E[Q(g)_i^2]
=
M^2\frac{|g_i|}{M}
=
M|g_i|.
\]
Summing gives
\[
\mathbb E\|Q(g)\|_2^2
=
M\|g\|_1.
\]
Because \(Q(g)\) is unbiased,
\[
\mathbb E\|Q(g)-g\|_2^2
=
\mathbb E\|Q(g)\|_2^2-\|g\|_2^2.
\]

It remains to optimize the deterministic norm ratio. Normalize
\[
M=\|g\|_\infty=1
\]
and put
\[
y_i=|g_i|\in[0,1].
\]
Choose an index with
\[
y_1=1.
\]
Set
\[
S=\sum_{i=2}^d y_i,
\qquad
R=\sum_{i=2}^d y_i^2.
\]
Cauchy--Schwarz gives
\[
R\ge\frac{S^2}{d-1}.
\]
Therefore
\[
\frac{\|g\|_\infty\|g\|_1}{\|g\|_2^2}
=
\frac{1+S}{1+R}
\le
\frac{1+S}{1+S^2/(d-1)}.
\]
For
\[
0\le S\le d-1,
\]
the scalar function on the right has its unique maximum at
\[
S=\sqrt d-1.
\]
Substitution yields
\[
\frac{\sqrt d+1}{2}.
\]

Equality in Cauchy--Schwarz requires
\[
y_2=\cdots=y_d,
\]
and the maximizing sum forces
\[
y_2=\cdots=y_d
=
\frac{\sqrt d-1}{d-1}
=
\frac{1}{\sqrt d+1}.
\]
This proves both sharpness and the equality family.

For the quadratic consequence, let
\[
g=Lx.
\]
Expanding the objective gives
\[
f(x-\eta Q(g))
=
f(x)
-\eta g^\top Q(g)
+
\frac{\eta^2L}{2}\|Q(g)\|_2^2.
\]
Conditional expectation and unbiasedness yield
\[
\mathbb E[f(x^+)\mid x]
=
f(x)
-\eta\|g\|_2^2
+
\frac{\eta^2L}{2}
\|g\|_\infty\|g\|_1.
\]
Dividing by
\[
f(x)=\frac L2\|x\|_2^2
\]
and writing
\[
h=\eta L
\]
gives the displayed factor. The sharp norm ratio then gives the exact worst case.

The quadratic
\[
1-2h+\frac{\sqrt d+1}{2}h^2
\]
is below one exactly for
\[
0<h<\frac4{\sqrt d+1}.
\]
Its unique minimum occurs at
\[
h=\frac2{\sqrt d+1},
\]
where the value is
\[
\frac{\sqrt d-1}{\sqrt d+1}.
\]

## Verification

The accompanying `verify.py` reconstructs TernGrad's complete finite Bernoulli distribution in dimensions up to eight.

For random vectors it enumerates every mask and checks the exact first moment, second moment, and variance identity. It checks the equality family in many dimensions, samples random vectors against the sharp constant, and verifies the exact isotropic-quadratic objective factor by direct distribution enumeration.

It also evaluates steps immediately below, at, and above the sharp expected-descent boundary on equality vectors.

These computations are transcription guards only. The all-dimensional variance and optimization constants are proved analytically above.

## Relationship to prior work

Wen, Xu, Yan, Wu, Wang, Chen, and Li introduced TernGrad. Their quantizer uses the infinity norm of the gradient as its scale and independently activates each ternary coordinate with probability proportional to its magnitude. Their convergence analysis naturally produces the quantity
\[
\|g\|_\infty\|g\|_1
\]
in its gradient-bound assumption and observes that it dominates
\[
\|g\|_2^2.
\]
The inspected source does not optimize the ratio of these two quantities over gradient directions or state the sharp relative-variance constant.

Safaryan, Shulgin, and Richtárik later place TernGrad's ternary quantization in the standard unbiased-compressor class
\[
\mathbb U(\omega)
\]
and tabulate the sufficient parameter
\[
\omega=\sqrt d-1.
\]
They also emphasize that compressed-gradient iteration complexities depend explicitly on the compressor variance parameter. Their table does not claim that the displayed TernGrad parameter is minimal.

The present result determines that minimal parameter exactly:
\[
\omega_\star=\frac{\sqrt d-1}{2}.
\]
It also identifies every sharp direction and turns the same constant into an exact expected-objective stability frontier on isotropic quadratics.

Focused searches for TernGrad together with the half-size variance constant, sharp infinity--one--two norm ratio, and exact isotropic-quadratic step boundary did not identify an implication-equivalent published statement.

## Limitations

The optimization corollary is for an isotropic quadratic and one compression bucket.

The exact compressor-variance result is broader than that corollary, but it does not by itself establish sharp end-to-end iteration complexity for a particular distributed training protocol.

The equality directions are mathematically natural worst cases for the quantizer; no claim is made that typical neural-network gradients concentrate near them.

Layer-wise ternarization changes the relevant dimension from the whole model to each bucket. The sharp formula applies separately to each chosen bucket.

## References

1. Wei Wen, Cong Xu, Feng Yan, Chunpeng Wu, Yandan Wang, Yiran Chen, and Hai Li, “TernGrad: Ternary Gradients to Reduce Communication in Distributed Deep Learning,” arXiv:1705.07878v1, first submitted 2017-05-22; NeurIPS 2017.
2. Mher Safaryan, Egor Shulgin, and Peter Richtárik, “Uncertainty Principle for Communication Compression in Distributed and Federated Learning and the Search for an Optimal Compressor,” arXiv:2002.08958v1, first submitted 2020-02-20; Information and Inference 11(2), 2022, DOI:10.1093/imaiai/iaab006.
