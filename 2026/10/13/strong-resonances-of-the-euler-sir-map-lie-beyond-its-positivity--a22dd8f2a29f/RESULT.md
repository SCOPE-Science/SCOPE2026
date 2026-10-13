# Strong resonances of the Euler SIR map lie beyond its positivity barrier

## Finding

Consider the forward-Euler SIR map
\[
S_{n+1}
=
S_n+h(A-dS_n-\lambda S_nI_n),
\]
\[
I_{n+1}
=
I_n+h(\lambda S_nI_n-(d+r)I_n),
\]
with positive parameters and
\[
\mathcal R_0
=
\frac{A\lambda}{d(d+r)}
>1.
\]
Its endemic fixed point is
\[
E_1
=
\left(
S_1,I_1^*
\right)
=
\left(
\frac{d+r}{\lambda},
\frac{A}{d+r}-\frac d\lambda
\right).
\]

At this fixed point, every unit-determinant stability boundary satisfies
\[
h(d+r)
=
\frac{\mathcal R_0}{\mathcal R_0-1}
>1.
\]
Consequently every endemic Neimark-Sacker boundary point, including every \(1{:}2\), \(1{:}3\), and \(1{:}4\) strong resonance of the source, lies beyond the elementary positivity barrier
\[
h(d+r)\le1.
\]

The incompatibility is not restricted to the boundary state
\[
S=0.
\]
At any such unit-determinant point, every state satisfying
\[
0<S<
\frac{S_1}{\mathcal R_0},
\qquad
I>0,
\]
is mapped to a negative infected value.

For the three numerical resonance examples printed in the source,
\[
h(d+r)
\approx
5.158016,\quad
3.37952,\quad
3.21524
\]
for the \(1{:}2\), \(1{:}3\), and \(1{:}4\) cases respectively.

The source also constructs a global \((h,\lambda)\) phase diagram from
\[
(S_0,I_0)=(1.4222,0.9861).
\]
At the rounded \(1{:}3\) resonance values
\[
A=1.2,\quad
d=0.4,\quad
r=0.24,\quad
\lambda=0.303,\quad
h=5.2805,
\]
one Euler step gives
\[
I_1
=
-0.10256632066707.
\]
Thus that positive initial condition leaves the epidemiological state space immediately at the resonance point.

The local resonance calculations can still be mathematically valid for the polynomial map near the positive fixed point. The correction is to the epidemiological interpretation: the strong-resonance and Neimark-Sacker boundaries cannot occur while this explicit Euler map remains positivity-safe near the disease-free edge.

## Assumptions and scope

All parameters satisfy
\[
A,d,r,\lambda,h>0
\]
and the endemic equilibrium exists,
\[
\mathcal R_0>1.
\]

The term “positivity barrier” means the necessary condition obtained from the infected update at small susceptible density. It is not claimed that
\[
h(d+r)\le1
\]
alone makes the entire two-dimensional Euler map positive for every nonnegative state; the susceptible update imposes additional restrictions when infection density is large.

The result is about the explicit Euler discretization printed in the source. It does not assert that strong resonances are impossible in discrete epidemic models generally. Positivity-preserving nonstandard discretizations can have their own bifurcation structures.

## Proof

The Jacobian of the Euler map at the endemic equilibrium is
\[
J(E_1)
=
\begin{pmatrix}
1-hA\lambda/(d+r) & -h(d+r)\\
h(A\lambda/(d+r)-d) & 1
\end{pmatrix}.
\]
Its determinant is
\[
\Delta
=
1-\frac{hA\lambda}{d+r}
+
h^2\bigl(A\lambda-d(d+r)\bigr).
\]

Using
\[
A\lambda
=
d(d+r)\mathcal R_0,
\]
this becomes
\[
\Delta
=
1-hd\mathcal R_0
+
h^2d(d+r)(\mathcal R_0-1).
\]

At a Neimark-Sacker boundary, the two conjugate multipliers lie on the unit circle and therefore have product
\[
\Delta=1.
\]
The same product condition holds at the \(1{:}2\), \(1{:}3\), and \(1{:}4\) strong resonances. Since \(h>0\),
\[
-hd\mathcal R_0
+
h^2d(d+r)(\mathcal R_0-1)
=
0
\]
implies
\[
h(d+r)
=
\frac{\mathcal R_0}{\mathcal R_0-1}.
\]
Because
\[
\mathcal R_0>1,
\]
the right-hand side is strictly larger than \(1\).

Now rewrite the infected update as
\[
I_{n+1}
=
I_n
\left[
1+h(\lambda S_n-(d+r))
\right].
\]
At
\[
S_n=0,\qquad I_n>0,
\]
positivity requires
\[
1-h(d+r)\ge0.
\]
This is impossible on the unit-determinant endemic boundary.

The open-strip statement follows by solving
\[
1+h(\lambda S-(d+r))<0.
\]
It is equivalent to
\[
S<
\frac{(d+r)-1/h}{\lambda}.
\]
On the unit-determinant boundary,
\[
\frac1h
=
(d+r)\frac{\mathcal R_0-1}{\mathcal R_0},
\]
so
\[
\frac{(d+r)-1/h}{\lambda}
=
\frac{d+r}{\lambda\mathcal R_0}
=
\frac{S_1}{\mathcal R_0}.
\]
This is positive, proving that an open set of strictly positive states is mapped outside the nonnegative quadrant.

For the source's \(1{:}3\) rounded example, direct substitution into the infected update gives the stated negative first iterate from its global-phase-diagram initial condition.

## Verification

The bundled `verify.py` checks the exact algebraic identities with rational arithmetic.

It verifies the universal unit-determinant formula
\[
h(d+r)
=
\frac{\mathcal R_0}{\mathcal R_0-1},
\]
the open-strip threshold
\[
S_{\mathrm{crit}}
=
\frac{S_1}{\mathcal R_0},
\]
and the source's rounded \(1{:}3\) one-step computation.

For
\[
A=\frac65,\quad
d=\frac25,\quad
r=\frac6{25},\quad
\lambda=\frac{303}{1000},
\]
the checker obtains
\[
\mathcal R_0
=
\frac{909}{640}
\]
and
\[
S_{\mathrm{crit}}
\approx
1.487145414211388.
\]
Since the source's global-diagram initial value is
\[
S_0=1.4222<S_{\mathrm{crit}},
\]
the computed infected multiplier is negative and
\[
I_1
=
-0.10256632066707.
\]

The verifier is a replay of exact formulas and source-rounded parameters. The general theorem does not depend on the numerical examples.

## Relationship to prior work

Liu, Liu, and Liu obtain their discrete SIR model by applying the explicit Euler scheme to a continuous demographic SIR system. They analyze \(1{:}2\), \(1{:}3\), and \(1{:}4\) strong resonances and then use one- and two-parameter simulations to interpret periodic, quasiperiodic, and chaotic behavior epidemiologically.

Hu, Teng, and Zhang previously studied the same Euler SIR map and derived flip and unit-circle bifurcation conditions. Their unit-circle step size is algebraically the same determinant-one boundary used here. The inspected material does not identify its incompatibility with positivity at the disease-free edge.

Suryanto and Darti study dynamically consistent SIR discretization and explicitly compare a positivity-conscious nonstandard construction against explicit Euler behavior. Their work establishes that preserving epidemic structure under discretization is a substantive issue rather than a cosmetic numerical preference, but it does not state the strong-resonance barrier proved here.

Naik and collaborators later analyze strong resonances in a discrete SIR setting built with a nonstandard finite-difference construction. This provides context that strong-resonance analysis itself is not tied to the explicit Euler discretization.

## Limitations

The result does not say that the local normal-form calculations around \(E_1\) are algebraically false. Since \(E_1\) is strictly positive, sufficiently small local invariant sets may remain inside the positive quadrant even though the map fails to preserve the full epidemiological state space.

The condition
\[
h(d+r)\le1
\]
is necessary for infected positivity near
\[
S=0,
\]
not a complete sufficient condition for positivity of every component at every nonnegative state.

The source's global parameter plots can contain mathematically meaningful attractors of the polynomial map even where the map is not a biologically admissible SIR update. The distinction established here is between map dynamics and epidemic-state-space validity.

## References

1. X. Liu, P. Liu, Y. Liu, “The existence of codimension-two bifurcations in a discrete-time SIR epidemic model,” AIMS Mathematics 7 (2022), 3360–3378. DOI: 10.3934/math.2022187.
2. Z. Hu, Z. Teng, L. Zhang, “Stability and bifurcation analysis in a discrete SIR epidemic model,” Mathematics and Computers in Simulation 97 (2014), 80–93. DOI: 10.1016/j.matcom.2013.08.008.
3. A. Suryanto, I. Darti, “On the nonstandard numerical discretization of SIR epidemic model with a saturated incidence rate and vaccination,” AIMS Mathematics 6 (2021), 141–155. DOI: 10.3934/math.2021010.
4. P. A. Naik, Z. Eskandari, A. Madzvamuse, Z. Avazzadeh, J. Zu, “Complex dynamics of a discrete-time seasonally forced SIR epidemic model,” Mathematical Methods in the Applied Sciences 46 (2023), 7045–7059. DOI: 10.1002/mma.8955.
