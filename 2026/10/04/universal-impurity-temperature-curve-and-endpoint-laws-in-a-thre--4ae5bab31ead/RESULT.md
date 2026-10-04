# Universal impurity-temperature curve and endpoint laws in a three-spin XXX ring

## Finding

Consider the three-qubit Heisenberg \(XXX\) ring with one exchange impurity,
\[
H=J_1(\boldsymbol\sigma_1\!\cdot\!\boldsymbol\sigma_2+\boldsymbol\sigma_3\!\cdot\!\boldsymbol\sigma_1)+J\,\boldsymbol\sigma_2\!\cdot\!\boldsymbol\sigma_3.
\]
Assume
\[
J_1>0
\]
and restrict to the regime in which the impurity-neighbor pair is entangled at zero temperature. In the source this is
\[
J_1>J\quad\text{when }J>0,
\]
and
\[
J_1>0\quad\text{when }J<0.
\]
Equivalently, with
\[
r=\frac{J}{J_1},
\]
the full regime is
\[
r<1.
\]

For every \(r<1\), there is a unique positive critical temperature \(T_c\) above which the impurity-neighbor concurrence vanishes. Set
\[
u=\frac{J_1}{T_c}.
\]
Then the entire two-parameter critical-temperature diagram collapses to the single equation
\[
\boxed{e^{6u}=e^{(2+4r)u}+4.}
\]
Consequently
\[
\boxed{\frac{T_c}{J_1}=t(r)=\frac1{u(r)}}
\]
is a universal one-variable curve. The root \(u(r)\) is strictly increasing on \(( -\infty,1)\), so \(t(r)\) is strictly decreasing.

The two endpoints of this curve have different structures.

For the antiferromagnetic activation boundary, write
\[
\delta=1-r.
\]
As \(\delta\downarrow0\),
\[
\boxed{
\frac{T_c}{J_1}
\sim
\frac{6}{W\!\left(6/\delta\right)}
}
\]
with \(W\) the principal Lambert function. Thus, for fixed \(J>0\),
\[
\boxed{
T_c
\sim
\frac{6J_1}{W\!\left(6J_1/(J_1-J)\right)}
}
\qquad(J_1\downarrow J).
\]
The thermal-entanglement window therefore collapses only inverse-logarithmically at the zero-temperature activation boundary.

At the strong-impurity endpoint, let \(z_0>1\) be the unique real root of
\[
z^3-z-4=0.
\]
Then
\[
z_0=1.7963219032594415\ldots
\]
and
\[
\alpha=\frac{2}{\log z_0}=3.414477321211954\ldots.
\]
The source's numerical asymptotic \(T_c\approx3.41448J_1\) is therefore the leading term of the sharper expansion
\[
\boxed{
T_c
=
\alpha J_1-\beta J+O\!\left(\frac{J^2}{J_1}\right)
}
\]
where
\[
\beta
=
\alpha\frac{z_0}{z_0+6}
=
0.786717182330735\ldots.
\]

## Assumptions and scope

The result concerns the periodic three-spin isotropic Heisenberg model and the impurity-neighbor concurrence treated in the source. Boltzmann's constant is set to one.

The critical temperature exists in the zero-temperature-entangled region \(J_1>0\), \(J/J_1<1\). The endpoint law involving the Lambert function concerns the antiferromagnetic side \(J>0\) with \(J_1\downarrow J\). The strong-impurity expansion keeps \(J\) fixed while \(J_1\to\infty\).

The result does not concern the concurrence between the two normal sites, the anisotropic \(XX\) model, spin-one impurities, magnetic fields, or multipartite negativity.

## Proof

The Hamiltonian is diagonalized most transparently by first coupling spins \(2\) and \(3\). There are three energy sectors:
\[
E_s=-3J
\]
with degeneracy two,
\[
E_d=J-4J_1
\]
with degeneracy two, and
\[
E_q=J+2J_1
\]
with degeneracy four.

Put
\[
A=e^{(4J_1-J)/T},\qquad
B=e^{3J/T},\qquad
C=e^{-(2J_1+J)/T}.
\]
Then
\[
Z=2A+2B+4C.
\]
The source's impurity-neighbor concurrence for \(J_1>0\) is
\[
C_{12}(T)
=
\max\!\left\{0,\frac{A-B-4C}{Z}\right\}.
\]
This also follows directly from \(SU(2)\) invariance: the impurity-neighbor correlator is
\[
\langle\boldsymbol\sigma_1\!\cdot\!\boldsymbol\sigma_2\rangle
=
\frac{-4A+4C}{Z},
\]
and the concurrence of the corresponding two-qubit Werner form is
\[
\max\!\left\{0,-\frac{1+\langle\boldsymbol\sigma_1\!\cdot\!\boldsymbol\sigma_2\rangle}{2}\right\}.
\]

The positive-temperature boundary therefore satisfies
\[
A-B-4C=0.
\]
Multiplying by \(e^{(2J_1+J)/T}\) gives
\[
e^{6J_1/T}=e^{(2J_1+4J)/T}+4.
\]
With \(u=J_1/T_c\) and \(r=J/J_1\), this is the universal equation
\[
F(u,r)=e^{6u}-e^{(2+4r)u}-4=0.
\]

For every \(r<1\),
\[
F(0,r)=-4
\]
and
\[
F(u,r)\to+\infty
\]
as \(u\to\infty\). Moreover \(F_u>0\) for all \(u>0\): when \(2+4r\ge0\), the exponent \(6\) is larger than \(2+4r\), and when \(2+4r<0\) the second derivative contribution has the favorable sign. Hence the positive root is unique.

At the root,
\[
F_r=-4u e^{(2+4r)u}<0,
\]
while \(F_u>0\). Thus implicit differentiation gives
\[
\frac{du}{dr}=-\frac{F_r}{F_u}>0,
\]
which proves that \(t(r)=1/u(r)\) is strictly decreasing.

For the activation endpoint write \(r=1-\delta\). The threshold equation becomes
\[
e^{6u}\left(1-e^{-4\delta u}\right)=4.
\]
As \(\delta\downarrow0\), necessarily \(u\to\infty\). The same equation then forces \(\delta u\to0\), so
\[
1-e^{-4\delta u}\sim4\delta u.
\]
Therefore
\[
\delta u e^{6u}\sim1.
\]
Writing \(w=6u\) gives
\[
w e^w\sim\frac6\delta,
\]
hence
\[
u\sim\frac16W\!\left(\frac6\delta\right),
\]
which proves the inverse-logarithmic endpoint law.

For the strong-impurity endpoint let \(r\to0\). At \(r=0\), setting \(z=e^{2u}\) gives
\[
z^3-z-4=0.
\]
The positive root \(z_0\) is unique and gives
\[
u_0=\frac12\log z_0,
\qquad
\alpha=\frac1{u_0}=\frac2{\log z_0}.
\]
Differentiate \(F(u(r),r)=0\) at \(r=0\). Using \(z_0^3=z_0+4\) yields
\[
u'(0)=u_0\frac{z_0}{z_0+6}.
\]
Thus
\[
\frac1{u(r)}
=
\alpha-\beta r+O(r^2),
\]
where
\[
\beta=\alpha\frac{z_0}{z_0+6}.
\]
Multiplication by \(J_1\) proves the stated finite-\(J\) correction.

## Verification

`verify_impurity_xxx_threshold.py` reconstructs the full \(8\times8\) Hamiltonian from Pauli matrices, forms the Gibbs state by spectral decomposition, traces out the third spin, and evaluates Wootters concurrence directly.

The direct matrix concurrence is compared with
\[
\max\!\left\{0,\frac{A-B-4C}{2A+2B+4C}\right\}
\]
on deterministic ferromagnetic and antiferromagnetic parameter grids.

The checker also solves the universal threshold equation by bisection, verifies its unique sign change, confirms monotonicity of \(u(r)\), checks the exact algebraic strong-impurity constant and first correction, and tests convergence to the Lambert-function activation law.

The finite numerical replay supplements, rather than replaces, the analytic proof.

## Relationship to prior work

Hu and Tian derive the impurity-neighbor concurrence, prove the zero-temperature activation conditions, show numerically that the critical temperature increases with impurity strength, and state that for \(J_1\gg|J|\) the critical temperature approaches
\[
T_c=3.41448J_1.
\]
They also display the limiting nonlinear equation from which that decimal is obtained.

The result here retains those premises but identifies the complete dimensionless critical curve, proves uniqueness and monotonicity of its root, replaces the strong-impurity decimal by an exact cubic constant with its first finite-\(J\) correction, and resolves the opposite endpoint \(J_1\downarrow J\) by a Lambert-function law.

An earlier paper treats impurity concurrence in a three-qubit Heisenberg \(XX\) chain, not the isotropic \(XXX\) Hamiltonian used here. A later paper by the same research group studies global bipartite negativities in the impurity \(XXX\) chain rather than this pairwise concurrence threshold. Targeted searches for the exact universal equation, the cubic constant together with the first correction, and the Lambert-function activation asymptotic did not locate a covering result.

## Limitations

The source itself already contains the concurrence formula, the existence of a critical temperature, its monotone increase with \(J_1\), and the leading numerical slope \(3.41448\) at strong impurity. Those facts are not claimed as new.

The new strong-impurity correction is an asymptotic expansion for fixed \(J\). The activation law is asymptotic as \(J_1\downarrow J\) with \(J>0\); it is not a uniform approximation over the whole phase diagram.

The full text of the closely related 2002 \(XX\)-chain paper was not publicly accessible in the inspected sources. Its abstract establishes a different anisotropic Hamiltonian, so it does not imply the isotropic threshold equation, but it remains a residual literature risk for related impurity asymptotics.

The exact bibliographic record used here supplies an exact public date of 30 July 2007, while the journal issue is labeled April 2007 without a day in the inspected full text. No received or accepted date is used as a publication date.

## References

1. M.-L. Hu and D.-P. Tian, “Effects of impurity on the entanglement of the three-qubit Heisenberg \(XXX\) spin chain,” *Science in China Series G: Physics, Mechanics & Astronomy* 50 (2007), 208–214, DOI: 10.1007/s11433-007-0019-9.
2. X.-Q. Xi, S.-R. Hao, W.-X. Chen, and R. Yue, “Impurity entanglement in three-qubit Heisenberg \(XX\) chain,” *Physics Letters A* 297 (2002), 291–299, DOI: 10.1016/S0375-9601(01)00843-X.
3. W. K. Wootters, “Entanglement of Formation of an Arbitrary State of Two Qubits,” *Physical Review Letters* 80 (1998), 2245–2248, DOI: 10.1103/PhysRevLett.80.2245.
