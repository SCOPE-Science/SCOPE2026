# Exact finite-temperature field phase diagram for alternate-site entanglement in the four-qubit XX ring

## Finding

Consider the periodic four-qubit Heisenberg \(XX\) ring
\[
H
=
J\sum_{n=1}^{4}
\left(
\sigma_n^+\sigma_{n+1}^-
+
\sigma_n^-\sigma_{n+1}^+
\right)
+
B\sum_{n=1}^{4}\sigma_n^z
\]
with nonzero \(J\), uniform field \(B\), periodic boundary conditions, and temperature \(T>0\). Let \(C_{13}\) denote the Wootters concurrence of the alternate sites \(1\) and \(3\).

Set
\[
x=\frac{|J|}{T},
\qquad
h=\frac{|B|}{T},
\qquad
a=\cosh(2x),
\qquad
k=\cosh(2\sqrt2\,x),
\qquad
c=\cosh(2h).
\]
Then the sign of the concurrence is governed by a single quadratic:
\[
C_{13}>0
\quad\Longleftrightarrow\quad
F_x(c)>0,
\]
where
\[
F_x(c)=L(x)c^2-Q(x)c-R(x),
\]
with
\[
L(x)
=
4\left(
\sinh^4x-\cosh^2(\sqrt2\,x)
\right),
\]
\[
Q(x)
=
4\cosh(2x)
+
2\cosh(2\sqrt2\,x)
+
2,
\]
and
\[
R(x)
=
\left(\cosh(2x)+1\right)^2.
\]

There is a unique number
\[
x_*=1.4195389207530749\ldots
\]
satisfying
\[
\sinh^2x_*=\cosh(\sqrt2\,x_*).
\]
Consequently the exact maximal temperature at which any finite magnetic field can entangle alternate sites is
\[
\boxed{
T_*=\frac{|J|}{x_*}
=
0.7044540909589808\ldots\,|J|.
}
\]

If
\[
T\ge T_*,
\]
then
\[
C_{13}(T,B)=0
\]
for every finite \(B\).

If
\[
0<T<T_*,
\]
then \(L(x)>0\). Define
\[
c_*(x)
=
\frac{
Q(x)+\sqrt{Q(x)^2+4L(x)R(x)}
}{
2L(x)
}
\]
and
\[
B_*(T)
=
\frac{T}{2}
\operatorname{arcosh}c_*(|J|/T).
\]
Then
\[
\boxed{
C_{13}(T,B)>0
\quad\Longleftrightarrow\quad
|B|>B_*(T).
}
\]

Thus the positive-temperature phase diagram has exactly one field boundary below \(T_*\): a lower activation threshold. There is no finite upper-field cutoff.

The lower threshold becomes exponentially small as \(T\downarrow0\):
\[
\boxed{
B_*(T)
\sim
\sqrt2\,T
e^{-(2-\sqrt2)|J|/T}.
}
\]
Hence
\[
\inf_{0<T<T_*} B_*(T)=0.
\]
In particular, no positive field magnitude can be a global lower floor for finite-temperature alternate-site entanglement.

At the opposite field extreme, for fixed \(0<T<T_*\),
\[
\boxed{
C_{13}(T,B)
\sim
A(T)e^{-2|B|/T},
}
\]
where
\[
A(T)
=
\cosh(2|J|/T)
-
1
-
2\cosh(\sqrt2\,|J|/T)
>0.
\]
The alternate-site concurrence therefore approaches zero from the positive side at high field rather than vanishing at a finite upper field.

For \(J=1\), the exact threshold values include approximately
\[
B_*(0.1)=0.0004041963,
\qquad
B_*(0.2)=0.01543208,
\qquad
B_*(0.5)=0.32694377.
\]
The concurrence is correspondingly extremely small in regions that coarse numerical plots can visually classify as zero.

## Assumptions and scope

The calculation uses the exact reduced Gibbs state printed by Cao and Zhu for alternate sites of the four-site periodic \(XX\) chain.

Boltzmann's constant is set to one. The result is even in \(J\) and \(B\), so the phase diagram depends on \(|J|\) and \(|B|\).

The theorem concerns strictly positive temperature. At exactly \(T=0\), the source's ground-state level crossings produce a finite entangled field window. The \(T\downarrow0\) and fixed-\(B\) limits are therefore singular at portions of the zero-temperature phase diagram.

No claim is made for longer chains, nonuniform fields, \(XXZ\) anisotropy, or Dzyaloshinskii--Moriya coupling.

## Proof

The source writes the alternate-site reduced state as
\[
\rho_{13}
=
\frac1Z
\begin{pmatrix}
u&0&0&0\\
0&w&y&0\\
0&y&w&0\\
0&0&0&v
\end{pmatrix},
\]
so
\[
C_{13}
=
\frac{2}{Z}
\max\left\{
|y|-\sqrt{uv},
0
\right\}.
\]

Using the source expressions and writing
\[
x=\frac{|J|}{T},
\qquad
h=\frac{|B|}{T},
\]
one obtains
\[
y
=
\cosh(2x)\cosh(2h)
+
\frac12\cosh(2\sqrt2\,x)
-
\cosh(2h)
-
\frac12.
\]
For \(x>0\) and \(h\ge0\), this is nonnegative.

The exact source formulas for \(u\) and \(v\) can then be expanded without approximation. A direct simplification gives
\[
y^2-uv
=
L(x)c^2-Q(x)c-R(x),
\qquad
c=\cosh(2h),
\]
with \(L,Q,R\) as stated in the finding. Since
\[
y+\sqrt{uv}>0,
\]
the sign of
\[
y-\sqrt{uv}
\]
is exactly the sign of \(F_x(c)\).

Now
\[
Q(x)>0,
\qquad
R(x)>0.
\]
At zero field, \(c=1\), and direct simplification gives
\[
F_x(1)
=
-8\left(
2\sinh^2x+\sinh^2(\sqrt2\,x)+2
\right)<0.
\]

The leading coefficient satisfies
\[
L(x)>0
\quad\Longleftrightarrow\quad
\sinh^2x>\cosh(\sqrt2\,x).
\]
Define
\[
g(x)=\sinh^2x-\cosh(\sqrt2\,x).
\]
Then
\[
g(0)=-1
\]
and \(g(x)\to\infty\). Moreover
\[
g'(x)
=
\sinh(2x)-\sqrt2\,\sinh(\sqrt2\,x)>0
\]
for \(x>0\). The last inequality follows because
\[
\frac{\sinh(\alpha x)}{\alpha}
\]
is strictly increasing in \(\alpha>0\) for fixed \(x>0\). Hence \(g\) has exactly one positive zero \(x_*\).

When \(x\le x_*\), one has \(L\le0\), so for every \(c\ge1\),
\[
F_x(c)<0
\]
because every term is nonpositive and the constant term is strictly negative. This proves complete separability above the universal temperature ceiling.

When \(x>x_*\), the quadratic has positive leading coefficient and
\[
\frac{-R}{L}<0,
\]
so its two real roots have opposite signs. Since \(F_x(1)<0\), the positive root satisfies \(c_*>1\). Therefore
\[
F_x(c)>0
\quad\Longleftrightarrow\quad
c>c_*,
\]
which gives the exact single-threshold condition
\[
|B|>B_*(T).
\]

For the low-temperature threshold, put \(x=|J|/T\) and write
\[
c_*(x)=1+\delta(x).
\]
Expanding the exact quadratic coefficients at large \(x\) gives
\[
\delta(x)
\sim
4e^{-2(2-\sqrt2)x}.
\]
Since
\[
\operatorname{arcosh}(1+\delta)
\sim
\sqrt{2\delta},
\]
it follows that
\[
B_*(T)
\sim
\sqrt2\,T
e^{-(2-\sqrt2)|J|/T}.
\]

Finally, use
\[
C_{13}
=
\frac{2}{Z}
\frac{F_x(c)}{y+\sqrt{uv}}
\]
in the entangled region. Keeping the leading powers of
\[
c=\cosh(2|B|/T)
\]
as \(|B|\to\infty\) yields
\[
C_{13}
\sim
\left[
\cosh(2x)-1-2\cosh(\sqrt2\,x)
\right]e^{-2|B|/T}.
\]
The coefficient is positive precisely when \(x>x_*\), completing the phase and tail classification.

## Verification

`verify_xx4_field_phase.py` checks the exact quadratic identity against the source \(u,v,y\) expressions across deterministic parameter grids.

It independently verifies the concurrence-sign classification from the quadratic, computes the unique root \(x_*\) by bisection, checks convergence to the low-temperature threshold asymptotic, and checks the high-field concurrence tail.

The checker also evaluates explicit finite-field points below the source's visually reported low-field floor and above its visually reported high-field window. These points have strictly positive concurrence.

The finite replay is supplementary. The all-parameter phase classification is supplied by the analytic proof above.

## Relationship to prior work

Cao and Zhu derive the exact four-qubit Gibbs state and alternate-site concurrence, and they emphasize a magnetic-field entanglement switch. Their abstract says that a magnetic field induces entanglement in a certain range, while their finite-resolution contour and low-temperature plots display apparently field-bounded entangled regions.

The exact reduction above shows that the positive-temperature phase boundary is simpler: below one universal temperature ceiling, there is only a lower field threshold. The apparent small-field floor tends exponentially to zero with temperature, and the apparent high-field cutoff is an exponentially small positive tail rather than an exact finite boundary.

Earlier work on \(n\le5\) \(XX\) chains studies pairwise thermal entanglement without this exact field phase classification. A later study by Zhou treats three- and four-qubit \(XX\) models with both magnetic field and Dzyaloshinskii--Moriya interaction. Its available abstract describes field- and coupling-dependent critical temperatures, but the inspected material does not state the zero-D quadratic reduction, the one-threshold theorem, or the two asymptotic laws above.

Targeted searches for the source title and DOI together with field-cutoff corrections, the numerical ceiling \(0.704454\ldots |J|\), the exact quadratic discriminant, and the high-field exponential tail did not locate an equivalent published statement.

## Limitations

The theorem is specific to the four-site periodic \(XX\) ring and alternate sites.

The positive high-field tail can be exponentially tiny and is therefore numerically delicate. The proof uses exact inequalities rather than treating floating-point underflow as physical zero.

The positive-temperature result does not erase the source's distinct \(T=0\) ground-state level crossings; rather, it shows a nonuniform zero-temperature limit.

A residual originality risk remains because a later field-plus-DM study covers the same four-site family more broadly, and only abstract-level material was available for that paper during the comparison.

## References

1. M. Cao and S. Zhu, “Thermal Entanglement between Alternate Qubits of a Four-qubit Heisenberg \(XX\) Chain in a Magnetic Field,” arXiv:quant-ph/0501029, first public 6 January 2005; *Physical Review A* 71 (2005), 034311, DOI: 10.1103/PhysRevA.71.034311.
2. G.-F. Zhang and S.-S. Li, “Thermal entanglement in a two-qubit Heisenberg \(XXZ\) spin chain under an inhomogeneous magnetic field,” *Physical Review A* 72 (2005), 034302.
3. B. Zhou, “Pairwise entanglement in the \(N\)-qubit \(XX\) model with Dzyaloshinski--Moriya interaction and magnetic field,” *International Journal of Modern Physics B* 25 (2011), DOI: 10.1142/S021797921110117X.
4. X. Wang, H. Fu, and A. I. Solomon, “Thermal entanglement in three-qubit Heisenberg models,” *Journal of Physics A* 34 (2001), 11307–11320.
