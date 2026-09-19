# Critical Derrick scaling reverses at \(p=1\) in the SS+VV Dirac reduction

## Result

Consider the nonrelativistic modified-NLS Hamiltonian derived in Section IV of Khare--Cooper--Dawson--Saxena, *Two-Parameter Family of Nonlinear Dirac Equations With Scalar-Scalar plus Vector-Vector Interactions* (arXiv:2609.18170):
\[
H[\psi]=\int_{\mathbb R}\frac{dx}{2m}\left\{
|\psi_x|^2\left[1+\frac{\widehat g^2(1-1/p)}{2m}|\psi|^{2\kappa}\right]
-\frac{\widehat g^2(1+1/p)}{\kappa+1}|\psi|^{2\kappa+2}
\right\},\qquad p>0.
\]
Write
\[
H=H_1+H_2-H_3,
\]
where \(H_1>0\) is the quadratic gradient term, \(H_3>0\) is the focusing potential term, and
\[
H_2=\frac{\widehat g^2(1-1/p)}{4m^2}
\int_{\mathbb R}|\psi_x|^2|\psi|^{2\kappa}\,dx.
\]
Thus
\[
\operatorname{sgn}H_2=\operatorname{sgn}(p-1).
\]
This sign is essential: the source's subsequent Derrick discussion states that \(H_2\) is positive, although its own Hamiltonian allows every \(p>0\), including \(0<p<1\).

For the mass-preserving scale family
\[
\psi_\lambda(x)=\lambda^{1/2}\psi(\lambda x),\qquad \lambda>0,
\]
the Hamiltonian is exactly
\[
H(\lambda)=\lambda^2H_1+\lambda^{\kappa+2}H_2-\lambda^\kappa H_3.
\]
At a stationary solitary wave the scale virial identity is
\[
2H_1+(\kappa+2)H_2-\kappa H_3=0,
\]
and hence
\[
H''(1)=2(2-\kappa)H_1+2(\kappa+2)H_2.
\]

At the NLS-critical power \(\kappa=2\), the complete scale dependence collapses to the exact identity
\[
\boxed{
H(\lambda)-H(1)=H_2(\lambda^2-1)^2.
}
\]
Consequently the corrected nonrelativistic Hamiltonian has a sharp three-way Derrick classification:
\[
\boxed{
\begin{array}{ccl}
p>1 &:& \lambda=1\text{ is the unique global minimum along the mass-preserving scale orbit},\\
p=1 &:& H(\lambda)\text{ is scale-flat at this order},\\
0<p<1 &:& \lambda=1\text{ is a global maximum along the scale orbit}.
\end{array}}
\]
For \(0<p<1\), the truncated Hamiltonian even satisfies \(H(\lambda)\to-\infty\) as \(\lambda\to\infty\) along that formal scale family. This last statement is a property of the truncated modified-NLS functional, not a claim of blow-up for the full nonlinear Dirac equation; the nonrelativistic expansion itself ceases to be controlled under arbitrarily strong concentration.

The result corrects the blanket conclusion in the source's Derrick calculation that the \(\kappa=2\) waves are scale-stable because \(H_2\) is positive. The sign is stabilizing only for \(p>1\), vanishes at \(p=1\), and is destabilizing for the vector-dominated range \(0<p<1\).

## First nonrelativistic displacement of the critical exponent

The sign switch also moves the Derrick threshold away from \(\kappa=2\). Let
\[
\varepsilon_{\rm NR}=\frac{m-\omega}{2m}\ll1.
\]
Using the leading NLS profile from the source,
\[
\psi(x)=A\,\operatorname{sech}^{1/\kappa}(\kappa\beta x),
\qquad
A^{2\kappa}=\frac{p}{p+1}\frac{(\kappa+1)(m-\omega)}{g^2},
\]
one has the exact integral ratio
\[
\frac{\int |\psi_x|^2|\psi|^{2\kappa}\,dx}
{\int |\psi_x|^2\,dx}
=A^{2\kappa}\frac{2}{3\kappa+2}.
\]
Since \(\widehat g^2/g^2=1+O(\varepsilon_{\rm NR})\), this gives
\[
\frac{H_2}{H_1}
=
2\varepsilon_{\rm NR}\,
\frac{p-1}{p+1}\,
\frac{\kappa+1}{3\kappa+2}
+O(\varepsilon_{\rm NR}^2).
\]
Putting \(\kappa=2+O(\varepsilon_{\rm NR})\) into the exact Derrick curvature therefore yields the critical surface
\[
\boxed{
\kappa_D
=2+3\varepsilon_{\rm NR}\frac{p-1}{p+1}
+O(\varepsilon_{\rm NR}^2).
}
\]
Thus the first relativistic correction shifts the width-stability boundary upward from 2 for \(p>1\), downward from 2 for \(0<p<1\), and leaves it unshifted to first order at \(p=1\). The pure-SS and pure-VV limits correspond to the opposite endpoint shifts \(+3\varepsilon_{\rm NR}\) and \(-3\varepsilon_{\rm NR}\), respectively.

## Proof details

Under \(\psi_\lambda(x)=\lambda^{1/2}\psi(\lambda x)\), the three terms scale as \(\lambda^2\), \(\lambda^{\kappa+2}\), and \(\lambda^\kappa\). Differentiating at \(\lambda=1\) gives the virial identity and the displayed second derivative. At \(\kappa=2\), stationarity implies
\[
H_3=H_1+2H_2,
\]
so
\[
H(\lambda)=\lambda^2(H_1-H_3)+\lambda^4H_2
=H_2(\lambda^4-2\lambda^2),
\]
and subtracting \(H(1)=-H_2\) gives the square identity.

For the near-critical displacement, writing \(z=\kappa\beta x\) reduces the two relevant integrals to
\[
J(a)=\int_{-\infty}^{\infty}\operatorname{sech}^{a}z\,\tanh^2z\,dz
=B\!\left(\frac32,\frac a2\right).
\]
Hence
\[
\frac{J(a+2)}{J(a)}=\frac{a}{a+3},
\]
and setting \(a=2/\kappa\) gives \(2/(3\kappa+2)\). Substitution into \(H''(1)\), followed by expansion at \(\kappa=2\), gives the stated \(\kappa_D\).

## Relation to prior work and originality boundary

Cooper--Khare--Mihaila--Saxena (Phys. Rev. E 82, 036604, 2010) already derived opposite-sign next-order modified-NLS corrections for the pure scalar and pure vector nonlinear Dirac models and used Derrick-type arguments. Later work also established that Derrick and Vakhitov--Kolokolov diagnostics do not by themselves settle spectral stability of the full nonlinear Dirac equation. Those general facts are not claimed as new.

The source-specific contribution here is the exact \(p=1\) scale-energy trichotomy for the new SS\(+\)(1/\(p\))VV family, the identification that the source's positivity assumption fails on its advertised \(0<p<1\) parameter range, and the interpolating first-order critical surface
\[
\kappa_D=2+3\varepsilon_{\rm NR}(p-1)/(p+1)+O(\varepsilon_{\rm NR}^2).
\]
Searches by the source identifier, title, SS/VV terminology, Derrick scaling, and the \(p=1\) sign switch did not locate a public correction or an equivalent source-specific statement.

## Limitations

This is a statement about the modified-NLS Hamiltonian retained by the source's nonrelativistic expansion and about Derrick width variations. It is not a proof of spectral or orbital stability of the full nonlinear Dirac solitary waves. In particular, the large-\(\lambda\) behavior of the truncated functional lies outside the controlled asymptotic regime, so the unbounded-below scale direction for \(p<1\) must not be interpreted as a rigorous finite-time blow-up theorem for the parent Dirac PDE. The first-order formula for \(\kappa_D\) assumes \(\varepsilon_{\rm NR}\ll1\); only the \(\kappa=2\) sign trichotomy is exact within the displayed truncated Hamiltonian.

## Reproducibility

`artifacts/verify_derrick_scaling.py` symbolically checks the critical scale identity, the sign factor \((p-1)/p\), the hyperbolic-secant integral ratio, and the first-order displacement of the Derrick threshold. `artifacts/verification_output.txt` contains its output.

## References

1. A. Khare, F. Cooper, J. F. Dawson, A. Saxena, *Two-Parameter Family of Nonlinear Dirac Equations With Scalar-Scalar plus Vector-Vector Interactions*, arXiv:2609.18170 (2026). https://arxiv.org/abs/2609.18170
2. F. Cooper, A. Khare, B. Mihaila, A. Saxena, *Solitary waves in the nonlinear Dirac equation with arbitrary nonlinearity*, Phys. Rev. E 82, 036604 (2010). https://doi.org/10.1103/PhysRevE.82.036604
3. A. Comech, *On the meaning of the Vakhitov--Kolokolov stability criterion for the nonlinear Dirac equation*, arXiv:1107.1763 (2011). https://arxiv.org/abs/1107.1763
4. J. Cuevas-Maraver et al., *Stability of solitary waves in the nonlinear Dirac equation with arbitrary nonlinearity*, Phys. Rev. E 90, 032915 (2014). https://doi.org/10.1103/PhysRevE.90.032915
