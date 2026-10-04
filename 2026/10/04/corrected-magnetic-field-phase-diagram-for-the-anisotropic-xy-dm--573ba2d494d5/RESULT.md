# Corrected magnetic-field phase diagram for the anisotropic XY–DM thermal concurrence

## Finding

Consider the two-qubit model of Qin, Xu, Tao, and Tian with exchange constant \(J\), in-plane anisotropy \(\gamma\), a \(z\)-directed Dzyaloshinskii--Moriya coupling \(D\), and a uniform \(z\)-field \(B\). Put
\[
K=\sqrt{J^2+D^2},
\qquad
G=|J\gamma|,
\qquad
\Delta_B=\sqrt{B^2+G^2},
\]
and assume
\[
0<G<K,\qquad B\ge0,\qquad T>0,\qquad \beta=\frac1T.
\]

Define
\[
q_B(\beta)
=
\cosh^2(K\beta)
-
\frac{G^2}{\Delta_B^2}
\sinh^2(\Delta_B\beta).
\]
Then the concurrence is positive exactly when
\[
\boxed{q_B(\beta)>2\quad\text{or}\quad q_B(\beta)<0},
\]
and therefore the thermal state is separable exactly when
\[
\boxed{0\le q_B(\beta)\le2}.
\]

This scalar reduction gives the complete field--temperature topology. Let
\[
B_0=\sqrt{K^2-G^2}.
\]

For
\[
0\le B\le B_0,
\]
the function \(q_B\) is strictly increasing on \((0,\infty)\). There is exactly one inverse-temperature threshold \(\beta_c\), determined by
\[
q_B(\beta_c)=2,
\]
and the state is entangled exactly for
\[
\beta>\beta_c.
\]

For
\[
B>B_0,
\]
the function \(q_B\) first increases and then decreases to \(-\infty\), with a unique strict maximum. There is a unique field
\[
\boxed{B_*>B_0}
\]
at which that maximum is exactly \(2\).

If
\[
B_0<B<B_*,
\]
there are unique values
\[
0<\beta_1<\beta_2<\beta_3
\]
such that
\[
q_B(\beta_1)=q_B(\beta_2)=2,
\qquad
q_B(\beta_3)=0.
\]
The concurrence is positive precisely on
\[
\boxed{(\beta_1,\beta_2)\cup(\beta_3,\infty)}.
\]
Thus an intermediate-temperature entanglement island is separated from the low-temperature entangled branch by a genuine separable interval.

At
\[
B=B_*,
\]
the maximum merely touches \(q=2\), so the intermediate island has collapsed to one zero-concurrence point. For
\[
B>B_*,
\]
only the low-temperature entangled branch remains, beginning at the unique root of
\[
q_B(\beta)=0.
\]

In the high-field regime,
\[
\beta_c(B)
=
\frac{\log(2\Delta_B/G)+o(1)}{\Delta_B},
\]
hence
\[
\boxed{
T_c(B)
\sim
\frac{\Delta_B}{\log(2\Delta_B/G)}
\sim
\frac{B}{\log(2B/G)}
\longrightarrow\infty.
}
\]
Therefore the critical temperature cannot be independent of \(B\) when \(G>0\).

For the parameters used in the source's field-independence statement,
\[
J=1,\qquad
\gamma=0.6,\qquad
D=0.5,
\]
one obtains
\[
B_0=0.9433981132056605\ldots
\]
and
\[
\boxed{B_*=1.7495575301980955\ldots}.
\]
At the tangency,
\[
\beta_*=1.1916319802569633\ldots,
\qquad
T_*=0.8391852657263866\ldots.
\]

For comparison, in the special case
\[
G=0,
\]
the magnetic field drops out identically:
\[
q_B(\beta)=\cosh^2(K\beta),
\]
and the unique threshold is
\[
\boxed{
T_c=\frac{K}{\log(1+\sqrt2)}.
}
\]
Thus field-independent critical temperature is the isotropic-in-plane special case, not the anisotropic example stated in the source.

## Assumptions and scope

The result uses the Hamiltonian convention and concurrence formula of the 2008 two-qubit XY--DM paper. Units are chosen so that \(k_B=1\). The nondegenerate theorem assumes
\[
0<G<K.
\]
This includes the source example \(J=1,\gamma=0.6,D=0.5\). The case \(G=0\) is treated separately because it is exactly field independent.

The theorem classifies the zero versus positive concurrence of the two-qubit Gibbs state as a function of \(B\) and \(T\). It does not concern many-spin thermodynamic phase transitions, other orientations of the DM vector, inhomogeneous fields, or entanglement measures other than concurrence.

## Proof

The source diagonalizes the Hamiltonian into two two-dimensional sectors with energy scales
\[
K=\sqrt{J^2+D^2}
\]
and
\[
\Delta_B=\sqrt{B^2+G^2}.
\]
Its Gibbs state is an \(X\)-state. After removing the common positive partition-function factor, the two concurrence candidates are
\[
f_1
=
\sinh(K\beta)
-
\sqrt{
1+
\frac{G^2}{\Delta_B^2}
\sinh^2(\Delta_B\beta)
},
\]
and
\[
f_2
=
\frac{G}{\Delta_B}
\sinh(\Delta_B\beta)
-
\cosh(K\beta).
\]
All quantities being squared are nonnegative. Therefore
\[
f_1>0
\]
is equivalent to
\[
\sinh^2(K\beta)
>
1+
\frac{G^2}{\Delta_B^2}
\sinh^2(\Delta_B\beta),
\]
which is exactly
\[
q_B(\beta)>2.
\]
Likewise,
\[
f_2>0
\]
is equivalent to
\[
q_B(\beta)<0.
\]
This proves the scalar concurrence criterion.

Differentiate:
\[
q_B'(\beta)
=
K\sinh(2K\beta)
-
\frac{G^2}{\Delta_B}
\sinh(2\Delta_B\beta).
\]

If
\[
\Delta_B\le K,
\]
then the strict increase of
\[
\frac{\sinh x}{x}
\]
on \(x>0\) gives
\[
K\sinh(2K\beta)
\ge
\frac{K^2}{\Delta_B}
\sinh(2\Delta_B\beta)
>
\frac{G^2}{\Delta_B}
\sinh(2\Delta_B\beta).
\]
Hence
\[
q_B'(\beta)>0.
\]
Because \(q_B(0)=1\) and \(q_B(\beta)\to\infty\), there is one and only one crossing of \(q=2\). The condition
\[
\Delta_B\le K
\]
is exactly
\[
B\le B_0=\sqrt{K^2-G^2}.
\]

Now assume
\[
\Delta_B>K.
\]
The equation \(q_B'(\beta)=0\) can be written as
\[
\frac{\sinh(2K\beta)}{\sinh(2\Delta_B\beta)}
=
\frac{G^2}{K\Delta_B}.
\]
The left side is strictly decreasing on \((0,\infty)\). Indeed, the logarithmic derivative has the sign of
\[
K\coth(2K\beta)-\Delta_B\coth(2\Delta_B\beta),
\]
which is negative because \(x\coth x\) is strictly increasing for \(x>0\).

At \(\beta\downarrow0\), the left side tends to
\[
\frac K{\Delta_B},
\]
which is larger than
\[
\frac{G^2}{K\Delta_B}
\]
because \(K^2>G^2\). At \(\beta\to\infty\), the left side tends to zero. Thus \(q_B\) has exactly one critical point, and it is a strict maximum because
\[
q_B''(0)=2(K^2-G^2)>0
\]
while
\[
q_B(\beta)\to-\infty.
\]

For each fixed \(\beta>0\), the function
\[
\frac{\sinh(\Delta\beta)}{\Delta}
\]
is strictly increasing in \(\Delta\). Hence \(q_B(\beta)\) is strictly decreasing with \(B\), and therefore the unique maximum value
\[
m(B)=\max_{\beta\ge0}q_B(\beta)
\]
is strictly decreasing for \(B>B_0\).

As
\[
B\downarrow B_0,
\]
the model approaches \(\Delta_B=K\), where
\[
q_B(\beta)
=
1+
\left(1-\frac{G^2}{K^2}\right)
\sinh^2(K\beta)
\to\infty.
\]
Thus
\[
m(B)\to\infty.
\]
As
\[
B\to\infty,
\]
the maximizing \(\beta\) tends to zero, and consequently
\[
m(B)\to1.
\]
Continuity and strict monotonicity therefore give one unique \(B_*\) satisfying
\[
m(B_*)=2.
\]

The crossing patterns now follow from continuity and the facts
\[
q_B(0)=1,
\qquad
q_B(\beta)\to-\infty
\]
for \(B>B_0\). If \(m(B)>2\), the rising and falling sides cross \(q=2\) once each, after which the falling side crosses \(q=0\) once. If \(m(B)=2\), the two \(q=2\) roots merge tangentially. If \(m(B)<2\), there is no \(q=2\) crossing and only the \(q=0\) crossing remains.

Finally, the high-field threshold is defined by
\[
q_B(\beta_c)=0,
\]
or equivalently
\[
\cosh(K\beta_c)
=
\frac{G}{\Delta_B}
\sinh(\Delta_B\beta_c).
\]
As \(B\to\infty\), this forces
\[
\beta_c\to0
\]
while
\[
\Delta_B\beta_c\to\infty.
\]
Using
\[
\cosh(K\beta_c)=1+o(1)
\]
and
\[
\sinh(\Delta_B\beta_c)
=
\frac12e^{\Delta_B\beta_c}(1+o(1)),
\]
we obtain
\[
e^{\Delta_B\beta_c}
=
\frac{2\Delta_B}{G}(1+o(1)),
\]
which proves the stated asymptotic formula.

## Verification

`verify_xy_dm_field_phase.py` independently evaluates the two concurrence candidates and the scalar function \(q_B\). It checks their sign equivalence on a deterministic parameter grid, verifies the monotonic and one-maximum regimes, computes the unique tangency field for the source parameters, and confirms the predicted crossing counts on both sides of that field.

For
\[
J=1,\qquad\gamma=0.6,\qquad D=0.5,
\]
the checker obtains
\[
B_*=1.7495575301980955\ldots.
\]
It also verifies that the high-field critical temperature grows rather than remaining constant.

The finite replay is supplementary. The all-parameter phase classification is supplied by the analytic proof.

## Relationship to prior work

Qin, Xu, Tao, and Tian derive the exact Gibbs state and concurrence for this two-qubit XY model with a \(z\)-directed DM interaction. For their Figure 1(b), using
\[
J=1,\qquad\gamma=0.6,\qquad D=0.5,
\]
they state that the critical temperature is independent of the magnetic field \(B\). Their own concurrence formula contains the \(B\)-dependent scale
\[
\Delta_B=\sqrt{J^2\gamma^2+B^2},
\]
and the reduction above shows that the stated field independence does not hold.

The earlier work of Lagmago Kamta and Starace already established that anisotropy and a uniform magnetic field can jointly sustain two-qubit XY entanglement to arbitrarily high finite temperature, and it derived a large-field critical-temperature asymptotic in the DM-free model. That result is important prior evidence against a generic field-independent threshold. The present claim is narrower: it gives the exact scalar separability criterion and the complete \(B\)--\(T\) crossing topology for the later XY--DM model, including the unique intermediate-island annihilation field \(B_*\).

Kheirandish, Akhtarshenas, and Mohammadi study a more general XYZ model with DM interaction and inhomogeneous fields and report finite-temperature entanglement revival regions. Later papers by Qin and collaborators likewise find field-dependent critical behavior for different XXZ/XYZ models with inhomogeneous fields. Those results do not state the scalar \(q_B\) criterion, the unique \(B_*\), or the correction to the 2008 homogeneous-field XY--DM claim.

Targeted searches for the 2008 paper title, DOI, its exact field-independence sentence, magnetic-field critical-temperature corrections, re-entrant concurrence, and the two energy scales did not locate a published correction of this phase diagram.

## Limitations

The correction concerns the source's nondegenerate anisotropic regime
\[
0<G<K.
\]
The degenerate endpoint \(G=K\), possible only in special parameter choices, requires a separate boundary analysis and is not claimed here.

The intermediate entanglement island is an exact feature of the two-qubit Gibbs concurrence. It is not a thermodynamic phase in the infinite-volume sense.

The high-field asymptotic concerns the unique low-temperature-branch critical temperature. It does not assert that concurrence is monotone in field at fixed temperature.

A residual literature risk remains because the DM-free anisotropic XY model has a substantial prior literature and an equivalent reformulation of the scalar criterion may appear under different notation.

## References

1. M. Qin, S.-L. Xu, Y.-J. Tao, and D.-P. Tian, “Thermal entanglement in a two-qubit Heisenberg XY chain with the Dzyaloshinskii--Moriya interaction,” *Chinese Physics B* 17 (2008), 2800–2803, DOI: 10.1088/1674-1056/17/8/009.
2. G. Lagmago Kamta and A. F. Starace, “Anisotropy and Magnetic Field Effects on the Entanglement of a Two Qubit Heisenberg XY Chain,” *Physical Review Letters* 88 (2002), 107901, DOI: 10.1103/PhysRevLett.88.107901.
3. R. Kheirandish, S. J. Akhtarshenas, and H. Mohammadi, “Effect of spin-orbit interaction on entanglement of two-qubit Heisenberg XYZ systems in an inhomogeneous magnetic field,” *Physical Review A* 77 (2008), 042309, arXiv:0801.1897, DOI: 10.1103/PhysRevA.77.042309.
