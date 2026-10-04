# An admissible saddle contradicts the source criterion in a Ricker predator–prey stability lemma

## Finding

Consider the Ricker-type predator-prey map
\[
H_{n+1}
=
H_n\exp\!\left(
a-bH_n-\frac{\alpha}{\beta+H_n}
-\frac{cP_n}{e+H_n}
\right),
\]
\[
P_{n+1}
=
P_n\exp\!\left(
\frac{fH_n}{e+H_n}-d
\right),
\]
with all parameters positive.

At a positive fixed point, the source writes the characteristic polynomial as
\[
p(\lambda)=\lambda^2-T\lambda+D.
\]
Its Lemma 3 correctly gives the sink condition
\[
D<1,\qquad |T|<D+1,
\]
and its stated saddle inequality
\[
0<|T|+D+1<2|T|
\]
is equivalent to
\[
|T|>|D+1|.
\]

The printed source condition is not correct. The source states that the fixed point is a source if
\[
D>1,\quad |T|<D+1,
\]
or if
\[
|T|>D+1.
\]
The second alternative overlaps the saddle region.

The complete disjoint classification for
\[
p(\lambda)=\lambda^2-T\lambda+D
\]
is
\[
\text{sink}
\iff
D<1
\ \text{and}\
|T|<D+1,
\]
\[
\text{source}
\iff
|D|>1
\ \text{and}\
|T|<|D+1|,
\]
\[
\text{saddle}
\iff
|T|>|D+1|,
\]
and
\[
\text{nonhyperbolic}
\iff
|T|=|D+1|
\quad\text{or}\quad
D=1,\ |T|\le2.
\]

The error is realized by an interior equilibrium satisfying the source's own sufficient existence conditions. Choose
\[
a=12,\quad
b=8,\quad
c=1,\quad
d=4,\quad
e=1,\quad
f=8,\quad
\alpha=\frac1{10},\quad
\beta=1.
\]
Then
\[
\alpha<a\beta,
\]
and
\[
H^*=\frac{de}{f-d}=1.
\]
The source's sufficient conditions read
\[
\alpha<(a-bH^*)(\beta+H^*)
\]
and
\[
\max\{\beta,H^*\}
<
\frac ab
<
\beta+H^*.
\]
Here they become
\[
\frac1{10}<8
\]
and
\[
1<\frac32<2.
\]
The corresponding positive predator coordinate is
\[
P^*=\frac{79}{10}.
\]

At this equilibrium the Jacobian is
\[
J^*
=
\begin{pmatrix}
-5&-\frac12\\[2mm]
\frac{79}{5}&1
\end{pmatrix}.
\]
Therefore
\[
T=-4,
\qquad
D=\frac{29}{10},
\]
and the eigenvalues are
\[
\lambda_{\pm}
=
-2\pm\sqrt{\frac{11}{10}}.
\]
Numerically,
\[
\lambda_+\approx-0.9511911518,
\qquad
\lambda_-\approx-3.0488088482.
\]
Thus exactly one multiplier lies inside the unit circle: the coexistence equilibrium is a saddle.

The source criterion simultaneously labels it a source, since
\[
D>1
\]
and
\[
|T|=4>D+1=\frac{39}{10},
\]
and labels it a saddle, since
\[
0<|T|+D+1
=
\frac{79}{10}
<
8=2|T|.
\]
Hence the local classification lemma is internally inconsistent on an admissible coexistence equilibrium.

## Assumptions and scope

The finding concerns the two-dimensional discrete map and the local fixed-point classification in Lemma 3 of the source.

The parameters in the explicit witness are all positive, the Allee effect is weak in the paper's sense because
\[
\alpha<a\beta,
\]
and the witness satisfies the paper's sufficient conditions for a unique interior equilibrium.

The corrected trace-determinant partition is a statement about the two multipliers of a real \(2\times2\) Jacobian. It does not claim that every later numerical bifurcation example in the paper is invalid; those examples can be checked directly from their own multipliers.

## Proof

Let
\[
p(\lambda)=\lambda^2-T\lambda+D
\]
have real coefficients and roots \(\lambda_1,\lambda_2\).

The unit-circle crossing at \(+1\) is
\[
p(1)=1-T+D=0,
\]
that is,
\[
T=D+1.
\]
The crossing at \(-1\) is
\[
p(-1)=1+T+D=0,
\]
that is,
\[
T=-(D+1).
\]
Complex conjugate roots lie on the unit circle precisely when
\[
D=1,\qquad |T|<2.
\]
Combining the real and complex boundary cases gives the stated nonhyperbolic set.

For both roots to lie strictly inside the unit circle, the second-order Schur conditions are
\[
1-T+D>0,\qquad
1+T+D>0,\qquad
1-D>0.
\]
These are exactly
\[
D<1,\qquad |T|<D+1.
\]

For a source, both reciprocal roots must lie strictly inside the unit circle. When \(D\ne0\), the reciprocal roots satisfy
\[
\mu^2-\frac{T}{D}\mu+\frac1D=0.
\]
Applying the same Schur conditions and separating the signs of \(D\) gives
\[
D>1,\qquad |T|<D+1,
\]
or
\[
D<-1,\qquad |T|<-D-1.
\]
Equivalently,
\[
|D|>1,\qquad |T|<|D+1|.
\]

The remaining hyperbolic region has one multiplier inside and one outside the unit circle. It is
\[
|T|>|D+1|.
\]
Equivalently,
\[
0<|T|+D+1<2|T|,
\]
which is the source's own saddle inequality.

For the explicit model parameters, the positive equilibrium formula gives
\[
H^*=\frac{4}{8-4}=1
\]
and
\[
P^*
=
\frac{(12-8)(2)(2)-(1/10)(2)}{2}
=
\frac{79}{10}.
\]
Substitution into the printed Jacobian formula yields
\[
J^*
=
\begin{pmatrix}
-5&-\frac12\\
\frac{79}{5}&1
\end{pmatrix}.
\]
The characteristic polynomial is
\[
\lambda^2+4\lambda+\frac{29}{10},
\]
so
\[
\lambda_{\pm}
=
-2\pm\sqrt{\frac{11}{10}}.
\]
Since
\[
-1<\lambda_+<0
\]
and
\[
\lambda_-<-1,
\]
the equilibrium is a saddle.

## Verification

The bundled script `verify.py` reconstructs the equilibrium from the source formulas using exact rational arithmetic, verifies all of the source's sufficient interior-existence inequalities, reconstructs the Jacobian, and checks
\[
T=-4,\qquad D=\frac{29}{10}.
\]

It then verifies both printed Lemma-3 predicates:
\[
D>1,\qquad |T|>D+1,
\]
and
\[
0<|T|+D+1<2|T|.
\]
Finally it computes the exact eigenvalues and confirms that precisely one has modulus below one.

The checker is used only for algebraic replay. The complete trace-determinant classification is proved analytically above.

## Relationship to prior work

Seralan, Vadivel, Chalishajar, and Gunasekaran (2023), DOI 10.3934/math.20231165, introduce the exact Ricker-type model studied here. Their full text gives the positive-equilibrium formula, its sufficient existence conditions, the Jacobian, the characteristic polynomial, and Lemma 3 with the overlapping source and saddle predicates.

Song (2023), DOI 10.1155/2023/5475999, studies a different nonlinear discrete predator-prey model with Allee effects. Its full text states the standard root-based sink/source/saddle definitions and, under \(F(1)>0\), distinguishes source and saddle through the signs of \(F(-1)\) and the determinant. For the witness above,
\[
p(1)=\frac{79}{10}>0,
\qquad
p(-1)=-\frac1{10}<0,
\]
so that independent criterion also classifies the witness as a saddle.

The trace-determinant partition itself is standard discrete dynamical-systems theory. The source-specific contribution here is the exact correction of the published Lemma 3 together with an admissible coexistence equilibrium satisfying the paper's own existence hypotheses for which the printed lemma gives incompatible classifications.

## Limitations

The finding corrects the local classification lemma. It does not rederive the paper's center-manifold coefficients, bifurcation directions, chaos-control calculations, or numerical diagrams.

The explicit witness is a mathematical parameter point in the model's stated positive parameter domain and satisfies the source's interior-existence assumptions; it is not asserted to be a calibrated ecological parameter set.

The corrected source condition is standard Schur/Jury theory. The new content is its source-specific application and the admissible contradiction to the printed lemma.

## References

1. V. Seralan, R. Vadivel, D. Chalishajar, N. Gunasekaran, “Dynamical complexities and chaos control in a Ricker type predator-prey model with additive Allee effect,” AIMS Mathematics 8 (2023), 22896–22923. DOI: 10.3934/math.20231165.
2. N. Song, “Bifurcation and Chaos of a Nonlinear Discrete-Time Predator-Prey Model Involving the Nonlinear Allee Effect,” Discrete Dynamics in Nature and Society (2023), Article 5475999. DOI: 10.1155/2023/5475999.
