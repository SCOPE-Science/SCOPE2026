# A sign inconsistency separates the printed and simulated gyrostat models
## Finding
The printed physical gyrostat equation and the normalized system used for the numerical analysis differ by the sign of one nonlinear inertial term. The paper prints
\[
I_y\dot y=h_zx+\mu_y y+(I_x-I_z)xz+L_y,
\]
but Table 1 defines the corresponding normalized coefficient by
\[
F_{2m}=\frac{I_z-I_x}{I_y}=-1.
\]
The same table gives \(F_{1m}=(I_y-I_z)/I_x=1/3\) and \(F_{3m}=(I_x-I_y)/I_z=1\). These two equalities force the inertia ratio \(I_x:I_y:I_z=3:2:1\). Hence literal normalization of the printed second physical equation gives
\[
\frac{I_x-I_z}{I_y}=+1,
\]
not the tabulated value \(-1\).

This difference has a structural consequence. For
\[
H=\frac12(3x_1^2+2x_2^2+x_3^2),
\]
the cubic inertial contribution to \(\dot H\) is
\[
(3F_{1m}+2F_{2m}+F_{3m})x_1x_2x_3.
\]
With Table 1, this coefficient is \(1-2+1=0\). With the literal sign from the printed Equation (1), it is \(1+2+1=4\). Thus the table sign has the rigid-body energy cancellation, whereas the printed sign adds \(4x_1x_2x_3\).

Accordingly, the basin, Lyapunov-exponent, Poincaré-section, and synchronization computations explicitly performed for System (2) with Table 1 parameters concern the energy-consistent sign-modified vector field rather than Equation (1) literally as printed.

## Assumptions and scope
The claim concerns the equations and parameter definitions in Marwan, Dos Santos, Abidin, and Xiong (2022), with the symbols interpreted exactly as printed. It does not assume that the paper's numerical basin or synchronization computations are themselves numerically incorrect. It distinguishes which of two nonlinear vector fields those computations represent.

The inference \(I_x:I_y:I_z=3:2:1\) uses only the exact dimensionless entries \(F_{1m}=1/3\) and \(F_{3m}=1\) from Table 1. The decimal linear coefficients are not used to infer the inertia ratio. Their rounding is discussed only as a secondary consistency check.

## Proof
Set \(I_z=s>0\). From \(F_{3m}=(I_x-I_y)/I_z=1\),
\[
I_x-I_y=s.
\]
From \(F_{1m}=(I_y-I_z)/I_x=1/3\),
\[
3(I_y-s)=I_x.
\]
Substituting \(I_x=I_y+s\) gives \(3I_y-3s=I_y+s\), so \(I_y=2s\) and \(I_x=3s\). Hence
\[
I_x:I_y:I_z=3:2:1.
\]

Literal division of the printed middle equation by \(I_y\) therefore produces
\[
F_{2m}^{\mathrm{printed}}=\frac{I_x-I_z}{I_y}=\frac{3s-s}{2s}=1.
\]
Table 1 instead defines
\[
F_{2m}^{\mathrm{table}}=\frac{I_z-I_x}{I_y}=\frac{s-3s}{2s}=-1.
\]
Thus Equation (1) and System (2)/Table 1 cannot be related by the stated normalization without changing that sign.

For the quadratic form \(H=(3x_1^2+2x_2^2+x_3^2)/2\), the three quadratic inertial terms in System (2) contribute
\[
3F_{1m}x_1x_2x_3+2F_{2m}x_1x_2x_3+F_{3m}x_1x_2x_3.
\]
Table 1 gives zero exactly. The literal printed sign gives \(4x_1x_2x_3\). This proves that the sign difference changes the mechanical energy balance, rather than merely changing notation.

The tabulated linear gyroscopic coefficients provide an independent rounding-level check. Ideally the common \(h_z\) coefficient implies \(3b_{12}=2b_{21}\), while the common \(h_y\) coefficient implies \(3b_{13}=b_{31}\). The printed decimals give \(3(0.7933)-2(1.19)=-10^{-4}\) and \(3(0.1914)-0.5742=0\), consistent with rounding of a single physical parameter in each pair.

## Verification
The accompanying `verify.py` uses exact rational arithmetic to check the inertia ratio, the two competing values of \(F_{2m}\), the cubic energy coefficients \(0\) and \(4\), and the decimal gyroscopic consistency residuals. It prints `VERIFY_OK` only if every check passes.

## Relationship to prior work
Marwan et al. explicitly state that their changed parameters are taken from the earlier gyrostat model of Qi and Yang, and their numerical analysis is carried out for System (2) with Table 1. The 2019 Qi–Yang paper studies the gyrostat through force and energy and treats the inertial terms as internal mechanical torques. That background makes the exact cancellation of the inertia-only contribution to kinetic energy a substantive consistency condition.

Searches for the paper title together with the disputed coefficient, its numerical parameter values, and gyrostat energy identities did not locate a published correction or a prior statement of this equation-to-table mismatch. The closest located published records concern balance laws in different dynamical systems and do not imply this source-specific sign comparison.

## Limitations
This result is an equation-consistency and energy-structure statement. It does not recompute the paper's basins, Lyapunov exponents, Poincaré sections, or synchronization experiments, and it does not assert that those computations fail for System (2). It also does not establish which sign was intended by the authors beyond the structural evidence that the table sign has the standard inertial energy cancellation. No independent audit has been performed.

## References
1. M. Marwan, V. Dos Santos, M. Z. Abidin, A. Xiong, “Coexisting Attractor in a Gyrostat Chaotic System via Basin of Attraction and Synchronization of Two Nonidentical Mechanical Systems,” *Mathematics* 10 (2022), 1914. DOI: 10.3390/math10111914. Published 2022-06-02.
2. G. Qi, X. Yang, “Modeling of a Chaotic Gyrostat System and Mechanism Analysis of Dynamics Using Force and Energy,” *Complexity* (2019), Article 5439596. DOI: 10.1155/2019/5439596.
