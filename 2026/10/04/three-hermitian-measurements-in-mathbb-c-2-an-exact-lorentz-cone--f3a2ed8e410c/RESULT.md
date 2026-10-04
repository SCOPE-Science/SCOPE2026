# Three Hermitian measurements in \(\mathbb C^2\): an exact Lorentz-cone trichotomy
## Finding
Let \(A_1,A_2,A_3\in\mathbf H_2(\mathbb C)\). Define the real-linear measurement operator
\[
L:\mathbf H_2(\mathbb C)\longrightarrow\mathbb R^3,
\qquad
L(Q)=\bigl(\operatorname{tr}(A_1Q),\operatorname{tr}(A_2Q),\operatorname{tr}(A_3Q)\bigr),
\]
and the quadratic signal map
\[
M(x)=L(xx^*).
\]
Signals are identified up to multiplication by a scalar of modulus one.

If \(\operatorname{rank}L<3\), then \((A_1,A_2,A_3)\) is not phase retrievable almost everywhere. Suppose now that \(\operatorname{rank}L=3\). Then \(\ker L=\mathbb RH\) for a nonzero Hermitian matrix \(H\), unique up to nonzero real scaling, so the sign of \(\det H\) is well defined. The classification is
\[
\boxed{\text{PR-ae}\iff \det H\ge0},
\qquad
\boxed{\text{PR}\iff \det H>0}.
\]
More precisely:

- If \(\det H>0\), every measurement fiber contains exactly one signal class.
- If \(\det H=0\), let \(P\) be the unique rank-one positive semidefinite ray contained in \(\mathbb RH\). Every nonzero signal outside \(\operatorname{ran}P\) is uniquely determined, while all amplitudes on the complex line \(\operatorname{ran}P\) have the same measurements as the zero signal. Hence full phase retrieval fails, but the exceptional signal set is null.
- If \(\det H<0\), then outside a real-algebraic null set every nonzero signal class has exactly one distinct partner with identical measurements. Hence phase retrieval almost everywhere fails, and the generic fiber has exactly two signal classes.

Thus the determinant sign of the one-dimensional Hermitian kernel gives the complete trichotomy for the minimal three-measurement problem in \(\mathbb C^2\).

## Assumptions and scope
The matrices \(A_j\) are arbitrary Hermitian \(2\times2\) matrices; positivity, rank-one structure, or a POVM normalization is not assumed. Phase retrieval means injectivity of \(M\) modulo global complex phase, including recovery of the signal norm. Phase retrieval almost everywhere means that the noninjective signal classes form a Lebesgue-null subset in the standard three-real-dimensional quotient chart, equivalently a null subset after lifting back to \(\mathbb C^2\).

The rank condition is essential. If \(\operatorname{rank}L<3\), the three displayed measurements have at most two independent real components. The sharp lower bound of Huang--Rong--Wang--Xu gives three measurements as necessary for complex almost-everywhere generalized phase retrieval in dimension two; equivalently, their rank-theorem argument applies after discarding linearly dependent measurements.

## Proof
Use the Pauli-coordinate identification of \(\mathbf H_2(\mathbb C)\) with real Minkowski space. Every Hermitian matrix has a unique representation
\[
Q=\frac12\bigl(tI+r_1\sigma_1+r_2\sigma_2+r_3\sigma_3\bigr),
\qquad t\in\mathbb R,\quad r\in\mathbb R^3,
\]
for which
\[
\det Q=\frac14\bigl(t^2-\|r\|^2\bigr).
\]
The nonzero matrices \(xx^*\) are exactly the future null cone
\[
\mathcal C_+=\{(t,r):t>0,\ t^2=\|r\|^2\}.
\]
Measurement equality is equivalent to
\[
xx^*-yy^*\in\ker L.
\]
When \(\operatorname{rank}L=3\), write the kernel generator as
\[
H=\frac12\bigl(\tau I+w\cdot\sigma\bigr),
\qquad
q:=\tau^2-\|w\|^2=4\det H.
\]
Fix a nonzero signal point \((t,tn)\in\mathcal C_+\), where \(t>0\) and \(\|n\|=1\). The affine measurement fiber is the line
\[
(t,tn)+s(\tau,w),\qquad s\in\mathbb R.
\]
Its intersections with the null cone are determined by
\[
0=(t+s\tau)^2-\|tn+sw\|^2
=s\Bigl(2t(\tau-n\cdot w)+sq\Bigr).
\]
The root \(s=0\) is the original signal. If \(q\ne0\), the only other algebraic root is
\[
s_*=-\frac{2t(\tau-n\cdot w)}q,
\]
and its time coordinate is
\[
t_*=t+s_*\tau
=-\frac{t\,\|\tau n-w\|^2}{q}.
\]

If \(q>0\), then \(t_*<0\). The second intersection lies on the past null cone and cannot equal \(yy^*\) for a signal \(y\). Thus every future-cone point is unique. This also recovers, in this two-dimensional one-kernel setting, the full phase-retrieval criterion of Wang--Xu: a nonzero kernel element of rank at most two must have its two nonzero eigenvalues of the same sign.

If \(q<0\), then \(t_*>0\) whenever \(s_*\ne0\), because \(\|\tau n-w\|^2>0\) for a spacelike kernel direction. Hence the second algebraic intersection is another future-cone point and gives a distinct signal class. The only points where the two roots coincide satisfy
\[
\tau-n\cdot w=0.
\]
This is a proper real-algebraic subset of the sphere of directions, and after adjoining the positive radial variable it remains null in the three-dimensional signal quotient. Therefore the generic fiber contains exactly two classes, so PR-ae fails.

If \(q=0\), the nonzero Hermitian matrix \(H\) has rank one and is semidefinite up to sign. The cone equation reduces to
\[
s\,2t(\tau-n\cdot w)=0.
\]
Because \(\|w\|=|\tau|\ne0\), the factor \(\tau-n\cdot w\) vanishes at exactly one projective direction, namely the rank-one positive semidefinite ray contained in \(\mathbb RH\). Away from that direction, \(s=0\) is the only cone intersection. On that direction, the entire positive ray is collapsed by \(L\), since its rank-one projector belongs to \(\ker L\). The exceptional complex line is null, proving PR-ae but not PR.

These three cases exhaust \(\operatorname{rank}L=3\), and the lower-rank case was excluded above.

## Verification
The proof is analytic and covers every Hermitian triple in the stated domain. The accompanying checker uses exact rational arithmetic to verify the line--cone intersection formulas on rational Bloch directions and checks canonical representatives of the three determinant-sign regimes: a timelike kernel generated by \(I\), a null kernel generated by a rank-one projector, and a spacelike kernel generated by a Pauli matrix. It also checks the expected uniqueness, null-boundary, and two-point-fiber signs. These finite checks are supplementary and are not used as a proof of the universal statement.

## Relationship to prior work
Huang, Rong, Wang, and Xu introduced almost-everywhere generalized phase retrieval and asked both for the minimal measurement number and for conditions under which a Hermitian measurement family is PR-ae. They proved that at least \(2d-1\) Hermitian measurements are necessary over \(\mathbb C^d\), constructed families attaining that number, and established generic results at \(2d\) measurements. In dimension two, their sharp lower bound is three measurements, but the inspected paper does not classify all Hermitian triples by their one-dimensional kernel geometry.

Wang and Xu earlier characterized full generalized phase retrieval by the absence of an indefinite nonzero Hermitian matrix of rank at most two in the measurement kernel. Therefore the \(\det H>0\) branch of the present trichotomy is a two-dimensional specialization of a known global criterion. The additional content here is the exact almost-everywhere boundary at \(\det H=0\), the failure regime at \(\det H<0\), and the generic fiber multiplicity in each kernel-sign class.

Balan and Dock give global Lipschitz and injectivity criteria for generalized phase-retrievable matrix frames. Their inspected results concern global generalized phase retrieval and stability, not this almost-everywhere classification of all three Hermitian measurements in \(\mathbb C^2\).

## Limitations
The theorem is specific to complex dimension two and exactly three Hermitian measurements. It does not classify higher-dimensional minimal families, where the kernel has a more complicated intersection with the rank-two Hermitian difference variety. The matrices are not required to be positive semidefinite or to form a POVM; imposing such constraints can change the feasible kernel geometry. The originality comparison found no covering statement under the searched generalized-phase-retrieval, qubit-tomography, and Hermitian-kernel formulations, but an unindexed low-dimensional observation using different terminology remains a residual priority risk.

## References
1. M. Huang, Y. Rong, Y. Wang, and Z. Xu, *Almost Everywhere Generalized Phase Retrieval*, arXiv:1909.08874; Applied and Computational Harmonic Analysis 50 (2021), DOI:10.1016/j.acha.2020.08.002.
2. Y. Wang and Z. Xu, *Generalized phase retrieval: measurement number, matrix recovery and beyond*, arXiv:1605.08034; Applied and Computational Harmonic Analysis 47 (2019), DOI:10.1016/j.acha.2017.09.003.
3. R. Balan and C. B. Dock, *Lipschitz Analysis of Generalized Phase Retrievable Matrix Frames*, arXiv:2109.14522; SIAM Journal on Matrix Analysis and Applications 43 (2022), DOI:10.1137/21M1435446.
