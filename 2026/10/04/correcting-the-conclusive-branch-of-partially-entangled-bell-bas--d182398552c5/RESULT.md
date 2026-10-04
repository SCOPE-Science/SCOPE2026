# Correcting the conclusive branch of partially entangled Bell-basis teleportation

## Finding

Let
\[
x\in[1/\sqrt2,1],
\qquad
y=\sqrt{1-x^2},
\]
and consider the orthonormal partially entangled basis
\[
|\psi^-\rangle'=x|01\rangle-y|10\rangle,
\qquad
|\psi^+\rangle'=y|01\rangle+x|10\rangle,
\]
\[
|\phi^-\rangle'=x|00\rangle-y|11\rangle,
\qquad
|\phi^+\rangle'=y|00\rangle+x|11\rangle.
\]

Trump, Bruß, and Lewenstein use this basis in the final conclusive-teleportation construction of arXiv:quant-ph/0010113v1, with Alice and Bob sharing
\[
|\Psi\rangle_{23}
=
\frac{|01\rangle+|10\rangle}{\sqrt2}.
\]

The displayed state decomposition in Eq. (8) of that version is not an identity. The two matrices printed in Eq. (9) also cannot be interpreted simultaneously as Kraus operators of a valid two-outcome POVM for
\[
0<\frac yx<1,
\]
because their squared effects do not sum to the identity.

The corrected decomposition shows that each of Alice's four outcomes leaves Bob with a branch map whose two singular values are
\[
\frac{x}{\sqrt2}
\quad\text{and}\quad
\frac{y}{\sqrt2}.
\]
Therefore the largest input-independent probability with which Bob can reverse one branch perfectly is
\[
\frac{y^2}{2}.
\]
Summing over all four mutually exclusive outcomes gives the exact optimal conclusive-teleportation probability
\[
\boxed{
P_{\mathrm{succ}}^{\mathrm{opt}}
=
2y^2
=
2(1-x^2).
}
\]

For example, after the appropriate Pauli correction, one branch is represented by
\[
D
=
\frac1{\sqrt2}
\begin{pmatrix}
x&0\\
0&y
\end{pmatrix}.
\]
It is optimally reversed by the success Kraus operator
\[
K_{\mathrm{s}}
=
\begin{pmatrix}
y/x&0\\
0&1
\end{pmatrix},
\]
completed to a valid instrument by
\[
K_{\mathrm{f}}
=
\begin{pmatrix}
\sqrt{1-y^2/x^2}&0\\
0&0
\end{pmatrix}.
\]
The second branch type uses the transposed diagonal choice.

This correction has the required physical endpoints:
\[
P_{\mathrm{succ}}^{\mathrm{opt}}=1
\quad\text{at}\quad
x=\frac1{\sqrt2},
\]
when Alice measures a Bell basis, while
\[
P_{\mathrm{succ}}^{\mathrm{opt}}\to0
\quad\text{as}\quad
x\to1,
\]
when the measurement basis becomes a product basis.

By contrast, the probability printed at the end of arXiv v1,
\[
\frac1{2x^2},
\]
approaches \(1/2\) in the product-basis limit and is not the success probability of a valid branchwise reversing instrument for the stated construction.

## Assumptions and scope

The claim concerns the final probabilistic-teleportation section of arXiv:quant-ph/0010113v1 and the basis written there. It does not challenge the paper's preceding numerical results on information gain or average fidelity for imperfect Bell-state discrimination.

The shared teleportation resource is the maximally entangled two-qubit state written by the source. Alice's partially entangled measurement is assumed ideal in this final subsection, exactly as in the source.

The result concerns faithful, heralded teleportation of an arbitrary unknown qubit. Success probability is required to be independent of the unknown amplitudes.

The correction is a statement about the mathematical protocol. It does not optimize how efficiently the four partially entangled basis states can themselves be distinguished by a particular optical apparatus.

## Proof

Write the unknown input as
\[
|\tau\rangle_1=\alpha|0\rangle+\beta|1\rangle,
\qquad
|\alpha|^2+|\beta|^2=1.
\]
Direct inversion of the orthonormal measurement basis gives
\[
|01\rangle
=
x|\psi^-\rangle'
+
y|\psi^+\rangle',
\]
\[
|10\rangle
=
-y|\psi^-\rangle'
+
x|\psi^+\rangle',
\]
\[
|00\rangle
=
x|\phi^-\rangle'
+
y|\phi^+\rangle',
\]
\[
|11\rangle
=
-y|\phi^-\rangle'
+
x|\phi^+\rangle'.
\]

Hence
\[
|\tau\rangle_1|\Psi\rangle_{23}
=
\frac1{\sqrt2}
\Big[
|\psi^+\rangle'
(\alpha y|0\rangle+\beta x|1\rangle)
+
|\psi^-\rangle'
(\alpha x|0\rangle-\beta y|1\rangle)
\]
\[
+
|\phi^+\rangle'
(\beta x|0\rangle+\alpha y|1\rangle)
+
|\phi^-\rangle'
(-\beta y|0\rangle+\alpha x|1\rangle)
\Big].
\]
This identity is normalized for every \(x\), \(y\), \(\alpha\), and \(\beta\).

After outcome-dependent Pauli corrections, every branch map is unitarily equivalent to either
\[
D_1
=
\frac1{\sqrt2}
\operatorname{diag}(x,y)
\]
or
\[
D_2
=
\frac1{\sqrt2}
\operatorname{diag}(y,x).
\]
The two singular values of either map are therefore \(x/\sqrt2\) and \(y/\sqrt2\).

Consider \(D_1\). Faithful reversal on every unknown input requires a successful quantum operation \(K\) such that
\[
KD_1=cU
\]
for some scalar \(c\) and unitary \(U\). Since a physical Kraus operator satisfies
\[
K^\dagger K\le I,
\]
one has
\[
\|K\|\le1.
\]
Equivalently,
\[
K=cUD_1^{-1},
\]
so
\[
1\ge\|K\|
=
|c|\,\|D_1^{-1}\|
=
|c|\frac{\sqrt2}{y}.
\]
Thus
\[
|c|^2\le\frac{y^2}{2}.
\]
This is the joint success probability contributed by that branch because the branch map is kept unnormalized.

Equality is achieved by
\[
K_{\mathrm{s}}
=
\operatorname{diag}(y/x,1),
\]
for which
\[
K_{\mathrm{s}}D_1
=
\frac{y}{\sqrt2}I.
\]
A valid complementary Kraus operator is
\[
K_{\mathrm{f}}
=
\operatorname{diag}\!\left(\sqrt{1-y^2/x^2},0\right),
\]
and indeed
\[
K_{\mathrm{s}}^\dagger K_{\mathrm{s}}
+
K_{\mathrm{f}}^\dagger K_{\mathrm{f}}
=
I.
\]
The same argument applies to the other three outcomes. Since the four branches are mutually exclusive, the total optimal probability is
\[
4\frac{y^2}{2}=2y^2.
\]

For comparison with the printed construction, if the two matrices in Eq. (9) of arXiv v1 are read as Kraus operators, their squared effects sum on the first component to
\[
\left(\frac yx\right)^2
+
\left(1-\frac yx\right)^2,
\]
which differs from \(1\) whenever
\[
0<\frac yx<1.
\]
If they are instead read merely as POVM effects, their sum is \(I\), but the first effect is then not the state-transforming filter required to invert the distorted branch. The displayed pair therefore cannot perform the claimed role as written.

## Verification

`verify_partial_basis_teleportation.py` constructs the three-qubit state and the four projectors directly, checks the corrected basis decomposition on deterministic complex input states, verifies the singular values of every branch map, and checks the Kraus completeness relation.

It also verifies that the success branch returns the original unknown qubit up to the appropriate Pauli correction, with joint probability \(y^2/2\) for each Alice outcome and total probability \(2y^2\).

The checker separately confirms that the two matrices printed in the source's Eq. (9), when interpreted as Kraus operators, fail the completeness relation away from the endpoint cases.

The numerical replay is supplementary. The optimality bound follows analytically from the least singular value of the branch map.

## Relationship to prior work

Mor and Horodecki introduced conclusive teleportation and showed that faithful teleportation can be made probabilistic when the available entanglement is nonmaximal.

Trump, Bruß, and Lewenstein considered a different placement of the nonmaximal entanglement: the shared Alice--Bob resource is maximal, while Alice measures in a partially entangled orthonormal basis. Their final subsection proposes a receiver-side POVM and prints a success probability, but the displayed state decomposition and measurement operators are internally inconsistent as written.

Later work on optimal conclusive teleportation and on measurement reversal establishes the general principle used in the corrected proof: the success probability of perfectly reversing a branch is governed by its smallest singular value. In particular, this broader theory is consistent with the corrected \(2y^2\) law after the branch maps of the present measurement are identified.

Those general results therefore support the corrected probability rather than constitute a new claim here. The new point is the explicit diagnosis and repair of the final arXiv-v1 construction: the printed equations do not form the stated quantum instrument, whereas the corrected branch maps and Kraus completion do.

Targeted searches for the paper title and DOI together with “erratum,” “correction,” the printed \(1/(2x^2)\) probability, and the partially entangled measurement basis did not locate a published correction of these displayed equations.

## Limitations

The claim is restricted to the final probabilistic subsection of arXiv:quant-ph/0010113v1. The journal version was not independently available for line-by-line comparison, so no assertion is made about whether later typesetting or editorial processing changed those equations.

The corrected success probability assumes ideal projective discrimination of Alice's partially entangled basis. A realistic linear-optical implementation has an additional basis-discrimination efficiency, which must be multiplied or otherwise composed with the conclusive-reversal probability according to the actual detector model.

The formula \(2y^2\) is consistent with general conclusive-teleportation and quantum-measurement-reversal theory. Originality here is confined to identifying and repairing the specific internally inconsistent arXiv-v1 construction.

## References

1. C. Trump, D. Bruß, and M. Lewenstein, “Realistic teleportation with linear optical elements,” arXiv:quant-ph/0010113v1, first public 31 October 2000; *Physics Letters A* 279 (2001), 7–11, DOI: 10.1016/S0375-9601(00)00784-2.
2. T. Mor and P. Horodecki, “Teleportation via generalized measurements, and conclusive teleportation,” arXiv:quant-ph/9906039, first public 14 June 1999.
3. L. Roa, A. Delgado, and I. Fuentes-Guridi, “Optimal conclusive teleportation of quantum states,” *Physical Review A* 68 (2003), 022310, DOI: 10.1103/PhysRevA.68.022310.
4. S.-W. Lee, D.-G. Im, Y.-H. Kim, H. Nha, and M. S. Kim, “Quantum teleportation is a reversal of quantum measurement,” *Physical Review Research* 3 (2021), 033119, DOI: 10.1103/PhysRevResearch.3.033119.
