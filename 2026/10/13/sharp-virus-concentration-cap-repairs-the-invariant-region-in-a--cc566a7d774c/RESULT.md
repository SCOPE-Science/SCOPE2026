# Sharp virus-concentration cap repairs the invariant region in a metacommunity COVID-19 model

## Finding

The environmental-virus equation in the metacommunity model is
\[
V_i'
=
p_i\left[
(1-m_I)(\lambda A_i+I_i)
+\lambda_eD_i
+
m_I\sum_{j=1}^nQ_{ji}(\lambda A_j+I_j)
\right]
-\mu_VV_i.
\]

The source derives
\[
S_j+A_j+I_j\le H_j=\frac{\Lambda_j}{\mu},
\qquad
D_j\le L_j=\frac{\xi_{e j}H_j}{\mu_D}.
\]
It then defines a live-infection quantity \(M_i\) and asserts
\[
V_i'\le M_i-\mu_VV_i,
\qquad
V_i\le\frac{M_i}{\mu_V}.
\]
The displayed \(M_i\) omits the positive deceased term \(\lambda_eD_i\), and the asserted inequality also omits the outer shedding factor \(p_i\).

The exact rectangular maximum of the virus-production bracket under the source's own upstream bounds is
\[
B_i^{\max}
=
c_\lambda\left(
(1-m_I)H_i+m_I\sum_{j=1}^nQ_{ji}H_j
\right)
+\lambda_eL_i,
\qquad
c_\lambda=\max\{1,\lambda\}.
\]
Therefore the repaired coordinate cap is
\[
\widehat V_i
=
\frac{p_i}{\mu_V}
\left[
c_\lambda\left(
(1-m_I)H_i+m_I\sum_{j=1}^nQ_{ji}H_j
\right)
+\lambda_eL_i
\right].
\]
Replacing the virus bound in the feasible region by \(0\le V_i\le\widehat V_i\) restores a compact positively invariant box.

The cap is sharp relative to the upstream rectangular information. For every \(j\),
\[
\lambda A_j+I_j
\le
c_\lambda(A_j+I_j)
\le
c_\lambda H_j.
\]
Equality is attained by placing all live infected mass in \(A_j\) when \(\lambda\ge1\), and in \(I_j\) when \(0<\lambda\le1\), while taking \(D_i=L_i\).

A two-patch witness proves that the published cap can point outward. Let
\[
Q_{12}=Q_{21}=1,\quad
H_1=H_2=L_1=1,\quad
m_I=\frac12,\quad
\lambda=1,\quad
\lambda_e=2,\quad
p_1=\mu_V=1.
\]
At
\[
A_1=A_2=1,\qquad I_1=I_2=0,\qquad D_1=1,
\]
the actual bracket is
\[
\frac12+2+\frac12=3.
\]
Even a generous independent-coordinate maximization of the live-only expression is at most \(2\). Hence any published boundary value \(V_1=M_1\) with \(M_1\le2\) satisfies
\[
V_1'=3-M_1\ge1>0.
\]

## Assumptions and scope

All parameters are positive as in the source, states are nonnegative, and the mobility matrix \(Q\) is stochastic with zero diagonal. The statement uses only the source's already-derived population and deceased-person bounds.

“Sharp” means the smallest coordinatewise constant virus cap obtainable solely from the rectangular inequalities \(A_j+I_j\le H_j\) and \(D_i\le L_i\). It is not asserted to be an exact reachable-set maximum for every prescribed initial condition.

If \(V_i(0)>\widehat V_i\), scalar comparison gives
\[
V_i(t)\le\max\{V_i(0),\widehat V_i\}.
\]

## Proof

Nonnegativity and \(S_j+A_j+I_j\le H_j\) give \(A_j+I_j\le H_j\). Therefore
\[
\lambda A_j+I_j
\le
\max\{1,\lambda\}(A_j+I_j)
\le
c_\lambda H_j.
\]
Together with \(D_i\le L_i\), the virus equation yields
\[
V_i'\le p_iB_i^{\max}-\mu_VV_i.
\]
At \(V_i=\widehat V_i=p_iB_i^{\max}/\mu_V\), the right-hand side is nonpositive. The source already supplies inward inequalities on the \(N_i=H_i\) and \(D_i=L_i\) faces and invariance of the nonnegative cone, so the corrected box is positively invariant.

The equality choices described above attain every term in \(B_i^{\max}\) simultaneously, proving sharpness relative to the rectangular bounds.

For the two-patch certificate, the actual bracket equals \(3\). The source's live-only expression is at most \(2\) even when every live coordinate is independently maximized. Therefore the derivative is strictly positive on the source virus boundary, proving failure of positive invariance.

## Verification

The bundled checker uses exact rational arithmetic to replay the two-patch certificate. It verifies the generous live-only bound \(2\), the actual bracket \(3\), the outward derivative for every source boundary value \(M_1\le2\), and the corrected cap \(3\).

The universal result is analytic; the finite replay is only a certificate check.

## Relationship to prior work

The primary article prints the full virus equation with the factor \(p_i\) and deceased forcing \(\lambda_eD_i\). Immediately afterward it derives \(V_i'\le M_i-\mu_VV_i\) from an \(M_i\) containing only live-infection terms and uses \(V_i\le M_i/\mu_V\) in its feasible region.

The article states disease-free global stability on that region. In the supercritical case it explicitly invokes both uniform persistence and invariance of the feasible region to infer existence of an endemic equilibrium. The repaired bound therefore restores a premise used downstream.

Targeted searches by title, DOI, environmental-virus terminology, invariant-region terminology, shedding-rate aliases, and correction terminology did not locate a published repair.

## Limitations

The result repairs the virus-coordinate bound and rectangular invariant region. It does not alter the reproduction-number formula or independently re-prove every downstream Lyapunov calculation.

The corrected cap is sharp for the rectangular upstream bounds, not necessarily over the smaller set dynamically reachable from every initial condition.

An unindexed author note could contain the same correction.

## References

1. J. Rebaza, “On a model of COVID-19 dynamics,” Electronic Research Archive 29 (2021), 2129–2140. DOI: 10.3934/era.2020108. Early access 19 October 2020.
