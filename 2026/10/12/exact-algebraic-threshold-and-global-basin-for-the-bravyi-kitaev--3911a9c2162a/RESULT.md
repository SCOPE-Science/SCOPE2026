# Exact algebraic threshold and global basin for the Bravyi–Kitaev H-state 15-to-1 map

## Finding

For the twirled one-parameter H-type input family
\[
\rho_\epsilon=(1-\epsilon)|H\rangle\langle H|+\epsilon|-H\rangle\langle-H|,
\qquad 0\le \epsilon\le \frac12,
\]
Bravyi and Kitaev's H-type 15-to-1 protocol has conditional output error
\[
f(\epsilon)=
\frac{1-15(1-2\epsilon)^7+15(1-2\epsilon)^8-(1-2\epsilon)^{15}}
{2\left(1+15(1-2\epsilon)^8\right)}.
\]
Their Eq. (37) reports the nontrivial fixed point only numerically as \(\epsilon_0\approx0.141\). It has the exact algebraic form
\[
\epsilon_*=
\frac12\left(1-\sqrt{\frac{z_*-\sqrt{z_*^2-4}}{2}}\right)
=0.141480292656167238344579330466\ldots,
\]
where \(z_*\) is the unique real root in \((2,3)\) of
\[
z^3+z^2-2z-16=0.
\]
The only fixed points of \(f\) on \([0,1/2]\) are \(0\), \(\epsilon_*\), and \(1/2\). If \(0<\epsilon<\epsilon_*\), iteration is strictly decreasing and converges to \(0\). If \(\epsilon_*<\epsilon<1/2\), iteration is strictly increasing and converges to \(1/2\).

## Assumptions and scope

The inputs are independent copies of the H-twirled state above, and Clifford operations, syndrome measurement, and postselection are ideal as in the source. The map describes error conditional on a successful round.

The threshold is protocol-specific. It is not the best possible H-state distillation threshold: later routines enlarge the H-state distillable region. Correlated input noise, imperfect Clifford operations, and finite-sample success fluctuations are outside the statement.

## Proof

Set
\[
r=1-2\epsilon\in[0,1].
\]
Then
\[
f(\epsilon)=\frac{1-15r^7+15r^8-r^{15}}{2(1+15r^8)}.
\]
Exact subtraction and factorization give
\[
f(\epsilon)-\epsilon
=
\frac{r(1-r^2)}{2(1+15r^8)}
\left(r^{12}+r^{10}+r^8-14r^6+r^4+r^2+1\right).
\]
For \(0<r<1\), put \(y=r^2\) and
\[
Q(y)=y^6+y^5+y^4-14y^3+y^2+y+1.
\]
Before the endpoint \(y=1\) is cancelled, the fixed-point polynomial is
\[
y^7-15y^4+15y^3-1=(y-1)Q(y).
\]
Because \(Q\) is reciprocal,
\[
\frac{Q(y)}{y^3}=q\!\left(y+y^{-1}\right),
\qquad
q(z)=z^3+z^2-2z-16.
\]
On \(0<y\le1\), \(z=y+y^{-1}\ge2\). Moreover,
\[
q(2)=-8,\qquad q(3)=14,\qquad
q'(z)=3z^2+2z-2>0\quad(z\ge2).
\]
Hence there is exactly one \(z_*\in(2,3)\) with \(q(z_*)=0\). Since \(y\mapsto y+y^{-1}\) is strictly decreasing on \((0,1]\), the corresponding physical root is unique and equals
\[
y_*=\frac{z_*-\sqrt{z_*^2-4}}{2}.
\]
Thus \(r_*=\sqrt{y_*}\) and \(\epsilon_*=(1-r_*)/2\).

The factorization also gives the global sign. For \(0<\epsilon<\epsilon_*\), one has \(y>y_*\), hence \(Q(y)<0\) and \(f(\epsilon)<\epsilon\). For \(\epsilon_*<\epsilon<1/2\), \(y<y_*\), hence \(Q(y)>0\) and \(f(\epsilon)>\epsilon\).

Finally, \(f\) maps \([0,1/2]\) to itself. The upper bound \(f(\epsilon)\le1/2\) is immediate. For nonnegativity, the numerator is
\[
1-r^{15}-15r^7(1-r)
=(1-r)\left(\sum_{k=0}^{14}r^k-15r^7\right)\ge0,
\]
because the arithmetic mean of \(1,r,\ldots,r^{14}\) is at least their geometric mean \(r^7\). Therefore the iteration below threshold is decreasing and bounded below, while the iteration above threshold is increasing and bounded above. By continuity every limit is a fixed point, and the complete fixed-point classification forces convergence to \(0\) and \(1/2\), respectively.

## Verification

The bundled `artifacts/verify.py` was run from its packaged directory. It symbolically checks the fixed-point factorization and reciprocal reduction, computes the unique physical root at high precision, and performs supplementary sign checks on both sides. The recorded output begins with `VERIFY_OK` and gives
\[
z_*=2.459120158366609003241401765418\ldots,
\]
\[
y_*=0.514145522215629964198501899175\ldots,
\]
and
\[
\epsilon_*=0.141480292656167238344579330466\ldots.
\]
The finite numerical checks are supplementary only; uniqueness and the basin theorem are analytic.

## Relationship to prior work

Bravyi and Kitaev derive the exact rational map and state that solving its H-type fixed-point equation numerically gives \(\epsilon_0\approx0.141\). In the same paper their different T-type protocol receives an exact threshold expression.

Reichardt later enlarges the known H-state distillable region with other routines. Meier, Eastin, and Knill explicitly call the Bravyi–Kitaev H-state Reed–Muller routine the 15-to-1 protocol, continue to quote its threshold as \(0.141\), and contrast it with a 7-to-1 H-state routine reaching about \(0.146\). Those broader results do not imply the exact fixed point or global basin of this particular recurrence.

Focused scientific searches using the source identifier, protocol/code aliases, the high-precision value, the fixed-point polynomial, and basin terminology did not identify an implication-equivalent published statement. This is evidence against overlap, not a proof of universal novelty.

## Limitations

The result calibrates one canonical protocol and one twirled one-dimensional noise family. It does not establish nondistillability above \(\epsilon_*\), since other protocols can work there, and it does not model faulty Clifford operations or correlated inputs.

The cubic characterization is an exact structural result; no claim is made that it is numerically preferable to direct root finding in engineering calculations.

## References

1. S. Bravyi and A. Kitaev, *Universal quantum computation with ideal Clifford gates and noisy ancillas*, arXiv:quant-ph/0403025, Phys. Rev. A 71, 022316 (2005), especially Eqs. (34)–(38).
2. B. W. Reichardt, *Quantum universality by state distillation*, arXiv:quant-ph/0608085.
3. A. M. Meier, B. Eastin, and E. Knill, *Magic-state distillation with the four-qubit code*, arXiv:1204.4221.
4. MaRDI publication record Q3102456.
