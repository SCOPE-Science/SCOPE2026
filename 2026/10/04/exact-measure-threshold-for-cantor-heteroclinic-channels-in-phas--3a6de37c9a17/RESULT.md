# Exact measure threshold for Cantor heteroclinic channels in phase-induced tipping
## Finding
In the Cantor-intersection modification of the phase-induced tipping construction of Dueñas and Vieiro, the size of the heteroclinic channel set has an exact threshold.

Write
\[
\Delta(\tau)=\widehat W^u_\varepsilon(\tau)-\widehat W^s_\varepsilon(\tau).
\]
On the compact region where \(\Delta\le 0\), choose a nonnegative smooth function \(q\) whose zero set \(C_\tau\) is contained in the strict region \(\Delta<0\), and choose the angular modulation \(\psi\ge1\) so that \(\psi^{-1}(1)=C_\phi\). With the source's cutoff construction, the heteroclinic representatives in one fundamental domain are exactly
\[
C_\tau\times C_\phi.
\]

Suppose each factor is a central Cantor set obtained from a base interval of length \(L_i\) by removing at stage \(n\) the relative middle fraction \(\rho_{i,n}\in[0,1)\), where \(i\in\{\tau,\phi\}\). Then
\[
m_2(C_\tau\times C_\phi)
=
L_\tau L_\phi
\prod_{n\ge1}(1-\rho_{\tau,n})(1-\rho_{\phi,n}).
\]
Consequently the heteroclinic representative set has positive area exactly when both series
\[
\sum_{n\ge1}-\log(1-\rho_{\tau,n}),
\qquad
\sum_{n\ge1}-\log(1-\rho_{\phi,n})
\]
converge.

If both factors instead use the same fixed relative middle-deletion fraction \(0<\rho<1\), then the area is zero and
\[
\dim_H(C_\tau\times C_\phi)
=
\frac{2\log 2}{\log(2/(1-\rho))}.
\]
For a fixed relative middle-quarter rule, \(\rho=1/4\), so
\[
m_2(C_\tau\times C_\phi)=0,
\qquad
\dim_H(C_\tau\times C_\phi)
=
\frac{2\log 2}{\log(8/3)}
\approx 1.4133901052.
\]
Thus positive-area “middle-quarter” behavior is obtained only under a fat-Cantor convention in which the relative losses decrease sufficiently fast; it is not obtained by deleting a fixed relative quarter at every stage.

## Assumptions and scope
The result concerns the specific smooth Cantor-intersection mechanism in Section 4.2.2 of Dueñas--Vieiro. The source first reduces its splitting function on one fundamental domain to a positive denominator times a numerator of the form
\[
\Delta(\tau)+\eta_0(\tau)\psi(\phi).
\]
On the region \(K_0=\{\tau:\Delta(\tau)\le0\}\), its cutoff is chosen to equal one. The present statement assumes that the prescribed Cantor zero set \(C_\tau\) lies in the interior region where \(\Delta<0\). This avoids the endpoint degeneracy that could otherwise create an entire angular fiber at a point where simultaneously \(\Delta=q=0\).

The measure formula applies to stagewise *relative* middle deletions. A Smith--Volterra--Cantor construction removes decreasing absolute lengths and is therefore a different schedule; it can have positive measure and is consistent with the positive-area side of the criterion.

## Proof
On \(K_0\), the source's construction sets \(\eta_0=q-\Delta\). Therefore the splitting numerator at the final parameter value is
\[
E(\tau,\phi)
=
\Delta(\tau)+(q(\tau)-\Delta(\tau))\psi(\phi)
=
\psi(\phi)q(\tau)+(1-\psi(\phi))\Delta(\tau).
\]
Here \(q\ge0\), \(\psi\ge1\), and \(\Delta\le0\). Both terms on the right are therefore nonnegative. If \(q(\tau)>0\), then \(E(\tau,\phi)>0\). If \(q(\tau)=0\), the assumption \(C_\tau\subset\{\Delta<0\}\) gives
\[
E(\tau,\phi)=0
\quad\Longleftrightarrow\quad
\psi(\phi)=1.
\]
Thus the zeros inside \(K_0\) are exactly \(C_\tau\times C_\phi\). Outside \(K_0\), one has \(\Delta>0\), while the added cutoff term is nonnegative in the source construction, so the numerator is strictly positive. The denominator in the source's displayed splitting formula is positive for its sufficiently small perturbation regime. Hence the splitting function vanishes exactly on \(C_\tau\times C_\phi\), and these points are exactly the representatives of heteroclinic connections in the chosen fundamental domain.

For a stagewise relative middle-deletion construction, after \(N\) stages the surviving total length in coordinate \(i\) is
\[
L_i\prod_{n=1}^N(1-\rho_{i,n}).
\]
The stage sets decrease to \(C_i\), so continuity from above of Lebesgue measure gives
\[
m_1(C_i)=L_i\prod_{n\ge1}(1-\rho_{i,n}).
\]
Fubini's theorem then yields the displayed product formula for \(m_2(C_\tau\times C_\phi)\). An infinite product of numbers in \((0,1]\) is positive exactly when the corresponding sum of negative logarithms is finite, proving the positive-area criterion.

If \(\rho_{i,n}=\rho\) is constant, the surviving length is \(L_i(1-\rho)^N\to0\), hence the limiting set has zero one-dimensional measure. Each factor is the self-similar two-branch Cantor set with similarity ratio
\[
s=\frac{1-\rho}{2}.
\]
The open set condition holds, so its Hausdorff dimension is the unique \(d\) satisfying \(2s^d=1\), namely
\[
d=\frac{\log2}{\log(2/(1-\rho))}.
\]
For the Cartesian product of two such factors, the four product similarities have ratio \(s\), so the Hausdorff dimension is \(2d\). Substituting \(\rho=1/4\) gives the stated value.

## Verification
The proof is symbolic and uses only the source's exact splitting formula, sign conditions, continuity from above of Lebesgue measure, Fubini's theorem, and the elementary similarity-dimension equation. No numerical experiment is used as proof.

A numerical evaluation of the closed-form middle-quarter dimension gives
\[
\frac{2\log2}{\log(8/3)}\approx1.4133901052,
\]
only as a decimal rendering of the exact expression.

The source's full relevant construction and conclusion were inspected directly. Its text distinguishes a null middle-third example from a positive-measure “middle-quarter” example without specifying in that sentence whether “middle-quarter” means a fixed relative fraction or a fat-Cantor absolute-length schedule. The present criterion resolves that ambiguity rather than attributing a contradiction to either convention.

## Relationship to prior work
Dueñas and Vieiro construct smooth splitting functions whose heteroclinic representatives form finite sets and then Cantor sets. They explain how flat bump functions realize the desired Cantor zero sets and state examples with null and positive Lebesgue measure. They do not give the exact product zero-set identity under the strict-splitting hypothesis, the infinite-product area threshold for stagewise relative deletions, or the Hausdorff-dimension formula for the self-similar regime.

The general measure and dimension facts for central Cantor sets are classical. The new point here is their exact transfer through the displayed splitting formula to the phase-induced heteroclinic channel set, including the convention-sensitive distinction between fixed relative middle-quarter deletion and a fat-Cantor schedule.

Targeted searches for phase-induced tipping, Cantor heteroclinic intersections, positive-measure fat Cantor channels, and Hausdorff dimension did not locate a prior statement implying this exact classification. A semantically close published database result on central Cantor dimensions concerns uniform disconnectedness on the line and does not address asymptotically autonomous maps or heteroclinic splitting.

## Limitations
The claim is restricted to the separable Cantor-engineering mechanism of the source and to one fundamental domain. It does not assert structural stability of the Cantor channel set under arbitrary perturbations, nor does it classify dimensions of general non-product heteroclinic intersections.

For variable deletion schedules the result gives the exact Lebesgue-measure threshold but not a general Hausdorff-dimension formula. The stated dimension formula is only for the equal fixed-ratio self-similar case. The phrase “middle-quarter” is convention-dependent; the result deliberately distinguishes fixed *relative* quarter deletion from fat-Cantor schemes based on decreasing absolute deletion lengths.

## References
1. J. Dueñas and A. Vieiro, *Asymptotically Autonomous Maps: Heteroclinic connections, Splitting and Phase-induced tipping*, arXiv:2609.24217v1, especially Sections 4.2.1--4.2.2.
2. J. E. Hutchinson, *Fractals and self similarity*, Indiana University Mathematics Journal 30 (1981), 713--747.
