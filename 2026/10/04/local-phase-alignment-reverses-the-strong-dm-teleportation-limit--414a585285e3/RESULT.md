# Local phase alignment reverses the strong-DM teleportation limit

## Finding
For the thermal two-qubit Heisenberg resource with a Dzyaloshinskii--Moriya interaction along the \(z\)-axis, define
\[
x=\frac JT,\qquad s=\sqrt{{1+D^2}},\qquad y=xs,\qquad \theta_D=\arctan D.
\]
Guo-Feng Zhang's resource eigenvectors in the odd-parity sector are
\[
|\pm\rangle=\frac{|01\rangle\pm e^{{i\theta_D}}|10\rangle}{\sqrt2}.
\]
Apply
\[
U_D=\operatorname{{diag}}(1,e^{{-i\theta_D}})
\]
to the first spin of each resource pair before using Zhang's standard Bell-measurement and Pauli-correction teleportation protocol. This converts the two odd-parity eigenvectors into the ordinary Bell states while leaving their thermal eigenvalues unchanged.

For the same pure input ensemble used in the source,
\[
|\psi(\vartheta,\varphi)\rangle=\cos(\vartheta/2)|10\rangle+e^{{i\varphi}}\sin(\vartheta/2)|01\rangle,
\]
with uniform Bloch-sphere averaging, the phase-aligned two-copy protocol has exact average fidelity
\[
F_{{\rm align}}=
\frac{{1+e^{{2x}}\left(3\cosh^2 y-1\right)}}
{{3\left(1+e^x\cosh y\right)^2}}.
\]
If \(F_Z\) denotes Zhang's published Eq. (11), then
\[
F_{{\rm align}}-F_Z=
\frac{{e^{{2x}}\sinh^2 y\,D^2}}
{{3(1+D^2)\left(1+e^x\cosh y\right)^2}}.
\]
Therefore \(F_{{\rm align}}>F_Z\) whenever \(JD\neq0\). In particular, Eq. (11) is not a maximal achievable average fidelity once a known local phase compensation on the shared pair is permitted. For every fixed \(J\neq0\) and \(T>0\),
\[
\lim_{{|D|\to\infty}}F_{{\rm align}}=1,
\qquad
\lim_{{|D|\to\infty}}F_Z=\frac23.
\]
The strong-DM classical-limit behavior in the published fixed-basis formula is therefore caused by a Bell-basis phase mismatch, not by loss of the underlying thermal entanglement resource.

## Assumptions and scope
The statement concerns exactly the two-copy teleportation construction and pure odd-parity input ensemble used in Zhang's 2007 paper. Temperature satisfies \(T>0\); \(J\) and \(D\) are real. The phase gate depends on the known Hamiltonian parameter \(D\) and is applied independently to the first spin of each shared thermal pair before the otherwise unchanged standard Bell protocol. No claim is made here about unknown \(D\), calibration error, arbitrary two-qubit inputs outside the source ensemble, or the globally optimal LOCC protocol.

The subject classification is anchored independently by Gürkan and Pashaev's mathematical treatment of the same two-qubit DM family, whose bibliographic record lists primary MSC \(81P40\). Zhang's teleportation paper is the earlier public problem source.

## Proof
Write
\[
r=e^x\cosh y,
\qquad
a=\frac1{{2(1+r)}},
\qquad
b=\frac{{e^x\cosh y}}{{2(1+r)}},
\qquad
u=\frac{{e^x\sinh y}}{{2(1+r)}}.
\]
The local phase gate sends \(|\pm\rangle\) to \((|01\rangle\pm|10\rangle)/\sqrt2\). Hence the four Bell overlaps of one aligned thermal pair, in the labeling used by the standard teleportation channel, are
\[
q_0=b+\nu,\qquad q_1=a,\qquad q_2=a,\qquad q_3=b-\nu.
\]
Using two independent resource copies gives the product Pauli channel
\[
\Lambda\otimes\Lambda(\rho)=
\sum_{{i,j=0}}^3q_iq_j(\sigma_i\otimes\sigma_j)\rho(\sigma_i\otimes\sigma_j).
\]
For the odd-parity logical-qubit ensemble, parity-changing Pauli products have zero overlap with the input. The two products acting as logical identity have Bloch-sphere average fidelity \(1\), while each nontrivial logical Pauli has average squared expectation \(1/3\). Therefore
\[
\overline F
=(b+\nu)^2+(b-\nu)^2+
\frac23(b+\nu)(b-\nu)+\frac43a^2.
\]
Substitution gives
\[
\overline F=F_{{\rm align}}=
\frac{{1+e^{{2x}}(3\cosh^2y-1)}}{{3(1+e^x\cosh y)^2}}.
\]

Without phase alignment, the standard Bell projectors see only the real part of the odd-sector coherence. Since \(\cos\theta_D=1/s\), the same calculation replaces \(\nu\) by \(\nu/s\). This produces
\[
F_Z=
\frac{{2s^2+e^{{2x}}\left[(2s^2-1)+(2s^2+1)\cosh(2y)\right]}}
{{6s^2(1+e^x\cosh y)^2}},
\]
which is algebraically identical to Zhang's Eq. (11). Subtracting yields the stated nonnegative gain, which is strictly positive exactly when \(JD\neq0\).

Finally, for fixed \(J\neq0\) and \(T>0\), \(|y|=|J|s/T\to\infty\) as \(|D|\to\infty\). Dividing numerator and denominator by \(e^{{2|y|}}\) in the two closed forms gives \(F_{{\rm align}}\to1\) and \(F_Z\to2/3\).

## Verification
The bundled script `artifacts/verify.py` independently evaluates the Bell-overlap formulas on a deterministic parameter grid, checks Zhang's printed Eq. (11) against the unaligned Bell-overlap expression, checks the closed-form gain identity, performs deterministic Bloch-sphere quadrature against the aligned product-Pauli channel, and checks the large-\(|D|\) limits numerically. Its recorded run for this package prints `VERIFY_OK source_formula=20 gain_identity=20 quadrature=4 limits=2`.

These finite checks support, but do not replace, the analytic proof above.

## Relationship to prior work
Zhang derives the thermal state, its DM-dependent phase \(\theta_D=\arctan D\), the two-copy Pauli-channel teleportation construction, and Eq. (11), then describes that equation as the maximal fidelity achievable from the thermal resource and notes its approach to \(2/3\) for strong DM coupling. The present result keeps the same resource copies and the same teleportation construction but aligns the known local DM phase before the Bell measurements; the positive gain shows that the maximality statement does not survive this allowed local-unitary preprocessing.

Gürkan and Pashaev analyze the same DM-induced complex odd-parity eigenvectors and the associated entanglement structure, but do not derive this phase-aligned two-copy teleportation fidelity. Horodecki, Horodecki, and Horodecki give the general relation between optimal teleportation fidelity and maximal singlet fraction; that broader theorem makes local-basis optimization conceptually natural but does not state the present source-specific two-copy input-ensemble formula or its exact gain over Zhang's Eq. (11).

A closely related 2010 paper by Chen and collaborators studies different DM orientations in two-qubit Heisenberg teleportation. Its accessible publisher preview reports fixed-protocol fidelity comparisons between DM components, but the full body was not available in the inspected corpus. It remains a residual coverage risk; no claim is made that every later paper using this model was exhaustively inspected.

## Limitations
The result is a correction to a maximality/asymptotic interpretation, not a claim that \(F_{{\rm align}}\) is globally optimal over all LOCC schemes. It assumes the DM phase is known well enough to implement \(U_D\). The strong-DM limit is mathematical; material-specific models may leave the regime in which the effective Hamiltonian is accurate before that limit is reached. The inaccessible full body of the closely related Chen et al. paper is an originality risk recorded explicitly rather than treated as negative evidence.

## References
1. G.-F. Zhang, “Thermal entanglement and teleportation in a two-qubit Heisenberg chain with Dzyaloshinski-Moriya anisotropic antisymmetric interaction,” arXiv:quant-ph/0703019; Phys. Rev. A 75, 034304 (2007), DOI: 10.1103/PhysRevA.75.034304.
2. Z. N. Gürkan and O. K. Pashaev, “Two Qubit Entanglement in Magnetic Chains with DM Antisymmetric Anisotropic Exchange Interaction,” arXiv:0804.0710; Int. J. Mod. Phys. B 24, 943–965 (2010), DOI: 10.1142/S0217979210054579.
3. M. Horodecki, P. Horodecki, and R. Horodecki, “General teleportation channel, singlet fraction, and quasidistillation,” Phys. Rev. A 60, 1888–1898 (1999), DOI: 10.1103/PhysRevA.60.1888.
4. T. Chen, C.-J. Shan, Y.-X. Huang, T.-K. Liu, and J.-X. Li, “The effect of different Dzyaloshinskii–Moriya interactions on teleportation via a two-qubit Heisenberg chain,” Mod. Phys. Lett. B 24, 461–473 (2010), DOI: 10.1142/S0217984910022536.
