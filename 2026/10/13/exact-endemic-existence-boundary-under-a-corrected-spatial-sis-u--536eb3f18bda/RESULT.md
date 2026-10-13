# Exact endemic-existence boundary under a corrected spatial SIS uniqueness hypothesis

## Finding

Deng and Wu's corrigendum revises the endemic-equilibrium uniqueness result for their spatial susceptible–infected–susceptible reaction–diffusion model. In the case
\[
d_S<d_I,
\]
its Theorem 1.2 assumes
\[
\frac{N}{|\Omega|}\ge \frac{\gamma(x)}{\beta(x)}
\quad\text{for every }x\in\overline\Omega,
\]
and its proof states that this weak inequality implies
\[
\mathcal R_0>1
\]
and hence that an endemic equilibrium exists.

The weak inequality has a sharp boundary that must be separated. Let
\[
c=\frac{N}{|\Omega|},
\qquad
w(x)=c\beta(x)-\gamma(x).
\]
Under the corrigendum's hypothesis \(w\ge0\), exactly one of the following occurs:

1. If \(w\not\equiv0\), then \(\mathcal R_0>1\), and the model has exactly one endemic equilibrium.
2. If \(w\equiv0\), then \(\mathcal R_0=1\), and the model has no positive endemic equilibrium.

Thus the source's intended existence-and-uniqueness statement is correct under the strengthened condition
\[
\frac{N}{|\Omega|}\ge\frac{\gamma}{\beta}
\quad\text{and strict inequality somewhere},
\]
while the everywhere-equality case is the disease threshold rather than an endemic state.

The theorem's phrase “the endemic equilibrium is unique” can be read as an at-most-one statement and is then vacuously compatible with the equality case. The proof, however, explicitly asserts existence from the weak inequality; that inference fails at equality.

## Assumptions and scope

The model is the conserved-total-population SIS reaction–diffusion system of Deng and Wu on a bounded smooth domain \(\Omega\), with positive Hölder-continuous transmission and recovery functions \(\beta,\gamma\), positive diffusion rates \(d_S,d_I\), homogeneous Neumann boundary conditions, and fixed total population \(N\).

The result concerns the additional-hypothesis regime of the 2022 corrigendum,
\[
d_S<d_I,
\qquad
\frac{N}{|\Omega|}\ge\frac{\gamma}{\beta}.
\]
It does not address uniqueness when the pointwise ordering fails.

## Proof

Set
\[
c=\frac{N}{|\Omega|},
\qquad
D=\frac{d_I}{d_S}>1,
\qquad
d=D-1.
\]
The disease-free equilibrium has susceptible density \(c\). The infected linearization is governed by
\[
\mathcal L\phi=d_I\Delta\phi+(c\beta-\gamma)\phi
\]
with homogeneous Neumann boundary condition.

Assume first that
\[
w=c\beta-\gamma\ge0
\]
and \(w\not\equiv0\). The Rayleigh quotient of \(\mathcal L\) evaluated at the constant test function is strictly positive because
\[
\int_\Omega w(x)\,dx>0.
\]
Hence the principal growth eigenvalue is positive, equivalently
\[
\mathcal R_0>1
\]
in the threshold convention of the source. Theorem 1.1 of the corrigendum gives existence of an endemic equilibrium, and Theorem 1.2 gives uniqueness under the same pointwise ordering. Therefore there is exactly one endemic equilibrium.

Now assume the boundary case
\[
w\equiv0,
\qquad\text{that is},\qquad
c\beta\equiv\gamma.
\]
Then
\[
\mathcal L=d_I\Delta
\]
has principal Neumann eigenvalue zero, so
\[
\mathcal R_0=1.
\]
The reduced endemic equation displayed as equation (1.1) in the corrigendum becomes
\[
d_I\Delta I+\beta I\left(dM-DI\right)=0,
\qquad
\partial_n I=0,
\]
where
\[
M=\frac1{|\Omega|}\int_\Omega I(x)\,dx.
\]
Suppose for contradiction that \(I>0\) solves this equation. Define the constant
\[
q=\frac{dM}{D}.
\]
Then the equation is
\[
d_I\Delta I+D\beta I(q-I)=0.
\]
Multiply by \(I-q\) and integrate. The Neumann condition removes the boundary term, giving
\[
-d_I\int_\Omega |\nabla I|^2\,dx
-D\int_\Omega \beta I(I-q)^2\,dx=0.
\]
Both terms are nonpositive, while \(d_I,D,\beta,I\) are positive. Hence both integrals vanish and
\[
I\equiv q.
\]
Therefore \(M=q\). But the definition of \(q\) gives
\[
q=\frac dD q.
\]
Since
\[
D-d=1,
\]
we obtain \(q=0\), contradicting \(I>0\). Thus no positive endemic equilibrium exists at the everywhere-equality boundary.

This proves the exact dichotomy.

## Verification

The proof uses only the source's reduced endemic equation, the Neumann principal-eigenvalue threshold, and an exact energy identity.

The critical calculation can be checked directly: in the equality case, after setting \(q=dM/D\), multiplication of
\[
d_I\Delta I+D\beta I(q-I)=0
\]
by \(I-q\) produces a sum of two nonpositive terms. Equality forces both spatial constancy and \(I=q\), and the nonlocal definition of \(q\) then forces the zero solution.

No finite numerical experiment is used to infer the PDE result.

## Relationship to prior work

The 2022 corrigendum itself corrects the original 2016 claim that the endemic equilibrium is always unique when \(\mathcal R_0>1\). For \(d_S<d_I\), it proves uniqueness under the additional pointwise condition
\[
\frac{N}{|\Omega|}\ge\frac{\gamma}{\beta}.
\]
Its proof then states that this weak condition implies \(\mathcal R_0>1\) and therefore existence. The equality boundary isolated here shows that the existence implication needs strictness somewhere.

Later SIS literature found in the comparison search cites the original paper and its corrigendum, but the inspected records do not state this exact boundary dichotomy. General reaction–diffusion reproduction-number theory explains the principal-eigenvalue threshold, but does not supply the source-specific nonexistence identity for the corrected endemic equation.

## Limitations

The result does not solve the open uniqueness problem for \(d_S<d_I\) when the pointwise ordering \(N/|\Omega|\ge\gamma/\beta\) fails.

It does not claim that the main uniqueness argument of the corrigendum is wrong away from the equality boundary. It only separates the threshold case from the genuinely supercritical case and corrects the proof's existence inference.

An unindexed later note could contain the same boundary clarification.

## References

1. K. Deng and Y. Wu, “Corrigendum: Dynamics of a susceptible—infected—susceptible epidemic reaction—diffusion model,” Proceedings of the Royal Society of Edinburgh Section A: Mathematics 153 (2023), 718–720. DOI: 10.1017/prm.2022.13. Published online 30 March 2022.
2. K. Deng and Y. Wu, “Dynamics of a susceptible–infected–susceptible epidemic reaction–diffusion model,” Proceedings of the Royal Society of Edinburgh Section A: Mathematics 146 (2016), 929–946. DOI: 10.1017/S0308210515000864.
