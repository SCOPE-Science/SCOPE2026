# The published trace–determinant source criterion overlaps the saddle region

## Finding

Consider the Ricker-type predator-prey map
\[
\begin{aligned}
H_{n+1}
&=
H_n\exp\!\left(
a-bH_n-\frac{\alpha}{\beta+H_n}
-\frac{cP_n}{e+H_n}
\right),\\
P_{n+1}
&=
P_n\exp\!\left(
\frac{fH_n}{e+H_n}-d
\right).
\end{aligned}
\]

At a positive coexistence equilibrium the source writes the characteristic polynomial
\[
\lambda^2-T\lambda+D=0.
\]
Its Lemma 3 contains an overlap: one of the printed alternatives for a source is
\[
|T|>D+1,
\]
while the same lemma's saddle condition is
\[
0<|T|+D+1<2|T|.
\]
The latter condition is equivalent to
\[
|T|>|D+1|.
\]

The overlap occurs for parameters that satisfy the model's positivity and coexistence assumptions. Take
\[
a=\frac{37}{2},\qquad
b=\frac{19}{2},\qquad
c=d=e=1,\qquad
f=2,\qquad
\alpha=2,\qquad
\beta=1.
\]
Then
\[
H^*=\frac{de}{f-d}=1
\]
and
\[
P^*=16.
\]
The Jacobian at this equilibrium is
\[
J^*
=
\begin{pmatrix}
-4&-\frac12\\
8&1
\end{pmatrix},
\]
so
\[
T=-3,
\qquad
D=0,
\]
and the multipliers are
\[
0,\quad -3.
\]
Hence the coexistence equilibrium is a hyperbolic saddle.

The source's printed source criterion nevertheless applies because
\[
|T|=3>D+1=1.
\]
Its saddle criterion also applies because
\[
0<3+0+1<6.
\]
Thus the same positive coexistence equilibrium is classified simultaneously as source and saddle by the printed lemma.

The correct disjoint hyperbolic classification is
\[
\text{sink}
\iff
D<1
\quad\text{and}\quad
|T|<D+1,
\]
\[
\text{source}
\iff
|D|>1
\quad\text{and}\quad
|T|<|D+1|,
\]
\[
\text{saddle}
\iff
|T|>|D+1|.
\]
The nonhyperbolic boundaries are
\[
|T|=|D+1|
\]
or
\[
D=1,\qquad |T|\le2.
\]

## Assumptions and scope

All model parameters are positive. The coexistence equilibrium is assumed to exist in the positive quadrant.

The exact witness also satisfies the source's weak-Allee inequality
\[
\alpha<a\beta
\]
and its displayed sufficient inequalities for existence of the positive coexistence equilibrium.

The result concerns only the local trace-determinant classification in Lemma 3. It does not claim that the source's later numerical bifurcation examples or control computations are incorrect.

## Proof

For a real \(2\times2\) Jacobian with characteristic polynomial
\[
p(\lambda)=\lambda^2-T\lambda+D,
\]
unit-circle crossings occur on three boundaries.

A multiplier
\[
\lambda=1
\]
gives
\[
D=T-1.
\]
A multiplier
\[
\lambda=-1
\]
gives
\[
D=-T-1.
\]
A nonreal conjugate pair on the unit circle has product
\[
D=1
\]
and
\[
|T|<2.
\]

The sink region is the triangle bounded by these three unit-circle loci:
\[
D<1,\qquad
D>T-1,\qquad
D>-T-1.
\]
Equivalently,
\[
D<1,\qquad |T|<D+1.
\]

Applying the same unit-disk criterion to the reciprocal multipliers gives the source region. When
\[
D>1,
\]
both multipliers are outside the unit disk exactly when
\[
|T|<D+1.
\]
When
\[
D<-1,
\]
both multipliers are outside exactly when
\[
|T|<-D-1.
\]
Together,
\[
\text{source}
\iff
|D|>1
\quad\text{and}\quad
|T|<|D+1|.
\]

The remaining hyperbolic region has one multiplier inside and one outside the unit disk and is therefore the saddle region:
\[
|T|>|D+1|.
\]

The saddle inequality printed by the source,
\[
0<|T|+D+1<2|T|,
\]
is equivalent to
\[
-|T|<D+1<|T|,
\]
which is precisely
\[
|D+1|<|T|.
\]

For the explicit model witness,
\[
H^*=1,\qquad P^*=16.
\]
The equilibrium exponents vanish exactly:
\[
\frac{37}{2}
-\frac{19}{2}
-\frac{2}{2}
-\frac{16}{2}
=0
\]
and
\[
\frac{2}{2}-1=0.
\]

The source's Jacobian formula gives
\[
1-\frac{19}{2}
+\frac{2}{4}
+\frac{16}{4}
=-4
\]
in its upper-left entry,
\[
-\frac{1}{2}
\]
in its upper-right entry, and
\[
\frac{1\cdot2\cdot16}{(1+1)^2}=8
\]
in its lower-left entry. The lower-right entry is \(1\). Hence
\[
J^*
=
\begin{pmatrix}
-4&-\frac12\\
8&1
\end{pmatrix},
\]
with characteristic polynomial
\[
\lambda(\lambda+3).
\]
This proves the claimed saddle classification and the simultaneous satisfaction of the two printed source conditions.

## Verification

The bundled `verify.py` uses exact rational arithmetic.

It verifies the positive coexistence equilibrium, the weak-Allee inequality, the source's displayed sufficient coexistence inequalities, the exact Jacobian, trace, determinant, and multipliers.

It then checks directly that the witness satisfies both the source condition
\[
|T|>D+1
\]
and the source's saddle inequality, while satisfying the corrected saddle criterion and not the corrected source criterion.

No numerical eigenvalue approximation is needed.

## Relationship to prior work

The motivating article uses a standard trace-determinant local classification to organize the stability of its coexistence equilibrium and then develops bifurcation analysis from that equilibrium.

The standard planar discrete-time trace-determinant partition is classical. An accessible derivation in Bosi's discrete-time dynamics notes the three unit-circle boundaries
\[
D=1,\qquad D=T-1,\qquad D=-T-1
\]
and partitions the plane into sink, source, and saddle regions. The correction above is therefore not a new stability theorem.

The new content is source-specific: the printed source criterion in Lemma 3 overlaps the saddle condition, and the overlap is realized by an explicit positive parameter vector within the paper's own predator-prey model and its coexistence assumptions.

Searches by the article DOI and title, trace-determinant terminology, source/saddle aliases, and the exact witness invariants did not locate a published correction of this lemma.

## Limitations

The repeated condition may be a typographical error rather than an error in the authors' intended dynamical reasoning.

The finding does not reassess every later parameter example in the article. Later calculations that use direct eigenvalues rather than the erroneous branch of Lemma 3 may remain unaffected.

The correction is local: it classifies the multipliers of a fixed point and does not by itself determine global dynamics.

## References

1. V. Seralan, R. Vadivel, D. Chalishajar, N. Gunasekaran, “Dynamical complexities and chaos control in a Ricker type predator-prey model with additive Allee effect,” AIMS Mathematics 8 (2023), 22896–22923. DOI: 10.3934/math.20231165.
2. S. Bosi, “Discrete Time Macroeconomic Dynamics,” EPEE Research Document 03-04, University of Evry, 2003.
