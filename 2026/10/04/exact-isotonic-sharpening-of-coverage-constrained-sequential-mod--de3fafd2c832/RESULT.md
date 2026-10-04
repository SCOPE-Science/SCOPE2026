# Exact isotonic sharpening of coverage-constrained sequential model confidence sets

## Finding

Consider a sequential model-comparison problem with methods \(m=1,\ldots,M\) and an ordered chain of \(R\ge2\) coverage constraints. At time \(t\), suppose a simultaneous confidence construction supplies, for every method and level,
\[
L_{mr,t}\le \Gamma_{mr,t}\le U_{mr,t},
\]
where \(\Gamma_{mr,t}\) is the prefix-average conditional miscoverage margin relative to tolerance \(\tau_r\).

Assume that, for every method and observation time \(s\), the prediction sets are nested
\[
C_{m1s}\subseteq C_{m2s}\subseteq\cdots\subseteq C_{mRs},
\]
that all levels use the same predictable exposure weights, and that
\[
\tau_1\ge\tau_2\ge\cdots\ge\tau_R.
\]
Write
\[
g_{mr,t}=\Gamma_{mr,t}+\tau_r.
\]
Then \(g_{m1,t}\ge\cdots\ge g_{mR,t}\). Define shifted interval endpoints
\[
\ell_{mr,t}=L_{mr,t}+\tau_r,\qquad
u_{mr,t}=U_{mr,t}+\tau_r.
\]
Intersect the rectangular confidence box with the order cone:
\[
K_{m,t}
=
\left\{
g\in\mathbb R^R:
\ell_{mr,t}\le g_r\le u_{mr,t}\ \text{for all }r,\quad
g_1\ge\cdots\ge g_R
\right\}.
\]

Whenever \(K_{m,t}\neq\varnothing\), the exact coordinate projections are
\[
\inf_{g\in K_{m,t}}(g_r-\tau_r)
=
\max_{j\ge r}\ell_{mj,t}-\tau_r,
\]
and
\[
\sup_{g\in K_{m,t}}(g_r-\tau_r)
=
\min_{i\le r}u_{mi,t}-\tau_r.
\]
Thus the sharp order-aware interval is
\[
\widetilde L_{mr,t}
=
\max_{j\ge r}\{L_{mj,t}+\tau_j\}-\tau_r,
\qquad
\widetilde U_{mr,t}
=
\min_{i\le r}\{U_{mi,t}+\tau_i\}-\tau_r.
\]

Under the monotone tolerance condition, possible feasibility is unchanged:
\[
m\in\widehat{\mathcal V}^{\mathrm{pos},\mathrm{iso}}_t
\quad\Longleftrightarrow\quad
L_{mr,t}\le0\ \text{for every }r.
\]
Certified feasibility is sharpened exactly to
\[
m\in\widehat{\mathcal V}^{\mathrm{cert},\mathrm{iso}}_t
\quad\Longleftrightarrow\quad
\widetilde U_{mr,t}\le0\ \text{for every }r.
\]
This contains every method certified by the original rectangular criterion \(U_{mr,t}\le0\) for all \(r\), and can contain more.

If the joint confidence region factors across methods, as in the rectangular construction, then its exact constrained-argmin projection remains available in closed form:
\[
q_t^{\mathrm{cert},\mathrm{iso}}
=
\min_{j\in\widehat{\mathcal V}^{\mathrm{cert},\mathrm{iso}}_t}
Q_{j,t},
\]
with the minimum of an empty set equal to \(+\infty\), and
\[
\widehat{\mathcal M}^{\mathrm{iso}}_t
=
\left\{
m\in\widehat{\mathcal V}^{\mathrm{pos}}_t:
Q_{m,t}\le q_t^{\mathrm{cert},\mathrm{iso}}
\right\}.
\]
Consequently,
\[
\widehat{\mathcal M}^{\mathrm{iso}}_t
\subseteq
\widehat{\mathcal M}^{\mathrm{rect}}_t
\]
at every structurally compatible time point. On the simultaneous confidence event of the underlying sequential construction, every true nested-risk vector lies in the corresponding \(K_{m,t}\), so this sharpening preserves the same simultaneous time-uniform coverage guarantee and therefore remains valid under data-dependent stopping.

The containment can be strict. Take two levels with
\[
\tau_1=\frac15,\qquad \tau_2=\frac1{10}.
\]
For method \(A\), with cost \(Q_A=1\), let
\[
[L_{A1},U_{A1}]
=
\left[-\frac4{25},-\frac3{25}\right],
\qquad
[L_{A2},U_{A2}]
=
\left[-\frac1{10},\frac15\right].
\]
The rectangular rule does not certify \(A\) because \(U_{A2}>0\). After shifting, however,
\[
u_{A1}=\frac2{25},\qquad u_{A2}=\frac3{10},
\]
so
\[
\widetilde U_{A2}
=
\min\left\{\frac2{25},\frac3{10}\right\}-\frac1{10}
=
-\frac1{50}<0.
\]
The first level is also certified, hence \(A\) is order-aware certified.

For method \(B\), with cost \(Q_B=2\), let both margin intervals be
\[
\left[-\frac1{20},\frac15\right].
\]
Both methods are possible, but \(B\) is not order-aware certified. The rectangular certified set is empty, so the original exact rectangular projection retains both \(A\) and \(B\). The order-aware certified set contains \(A\), hence its exact projection is the singleton \(\{A\}\).

## Assumptions and scope

The result is a deterministic structural refinement of a simultaneous sequential confidence rectangle. It assumes a chain of genuinely nested prediction sets and common predictable exposure weights across that chain. These assumptions make the prefix-average conditional miscoverage rates inherit the same order. The tolerances are assumed nonincreasing along the chain.

The theorem applies at time points for which every method-specific order-restricted box \(K_{m,t}\) is nonempty. On the simultaneous confidence event of the underlying method, this nonemptiness is automatic because the true risk vector belongs to the box and satisfies the order restriction. Off that event, an observed rectangular box can be incompatible with the known order; the theorem does not prescribe replacing an incompatible box by an invented nonempty one.

The claim concerns a simple total order of coverage levels. More general partial orders admit analogous cone intersections but need not have the same one-pass prefix/suffix formulas. If exposure weights differ across levels, or if the prediction sets are not pathwise nested, the stated ordering of prefix risks need not hold and the refinement is not justified.

## Proof

For a fixed method and time, suppress \(m,t\) and write
\[
K
=
\{g:\ell_r\le g_r\le u_r,\ g_1\ge\cdots\ge g_R\}.
\]
Assume \(K\neq\varnothing\).

For every \(g\in K\), every \(j\ge r\) satisfies
\[
g_r\ge g_j\ge\ell_j,
\]
so
\[
g_r\ge \max_{j\ge r}\ell_j.
\]
Similarly, every \(i\le r\) satisfies
\[
g_r\le g_i\le u_i,
\]
so
\[
g_r\le \min_{i\le r}u_i.
\]

Both bounds are attained. Define
\[
g_r^{\min}=\max_{j\ge r}\ell_j.
\]
This sequence is nonincreasing and dominates every lower endpoint. If \(h\in K\), then
\[
g_r^{\min}\le h_r\le u_r,
\]
because \(h_r\ge h_j\ge\ell_j\) for every \(j\ge r\). Hence \(g^{\min}\in K\), proving the lower projection formula. Likewise define
\[
g_r^{\max}=\min_{i\le r}u_i.
\]
It is nonincreasing and lies below every upper endpoint. For any \(h\in K\),
\[
\ell_r\le h_r\le g_r^{\max},
\]
because \(h_r\le h_i\le u_i\) for every \(i\le r\). Thus \(g^{\max}\in K\), proving the upper projection formula.

These constructions also show the exact compatibility criterion
\[
K\neq\varnothing
\quad\Longleftrightarrow\quad
\max_{j\ge r}\ell_j
\le
\min_{i\le r}u_i
\quad\text{for every }r.
\]

Now impose \(\tau_1\ge\cdots\ge\tau_R\). A method is possibly feasible exactly when some \(g\in K\) obeys \(g_r\le\tau_r\) for every \(r\). Necessity gives
\[
\ell_r\le\tau_r,
\]
equivalently \(L_r\le0\), for every \(r\). Conversely, if \(L_r\le0\) for all \(r\), then \(\ell_r\le\tau_r\). For the minimal feasible order-cone vector,
\[
g_r^{\min}
=
\max_{j\ge r}\ell_j
\le
\max_{j\ge r}\tau_j
=
\tau_r.
\]
Hence possible feasibility is unchanged.

A method is certified feasible exactly when every \(g\in K\) obeys \(g_r\le\tau_r\) for every \(r\). Since the coordinate supremum is \(g_r^{\max}\), this is equivalent to
\[
g_r^{\max}\le\tau_r
\]
for all \(r\), which is exactly \(\widetilde U_r\le0\).

For the constrained-argmin projection, suppose the global structural confidence region is the Cartesian product of the method-specific \(K_m\). If method \(m\) can be optimal at some point in that region, then \(m\) must be possibly feasible. Moreover, every certified method is feasible at every point in the region, so \(m\) cannot cost more than the cheapest certified method. This proves necessity of
\[
Q_m\le q^{\mathrm{cert},\mathrm{iso}}.
\]

Conversely, suppose \(m\) is possibly feasible and \(Q_m\le q^{\mathrm{cert},\mathrm{iso}}\). Choose a feasible vector in \(K_m\). For each method \(j\) with \(Q_j<Q_m\), the inequality \(Q_m\le q^{\mathrm{cert},\mathrm{iso}}\) implies that \(j\) is not certified, so there exists a vector in \(K_j\) under which \(j\) is infeasible. Because the region factors across methods, these choices can be made simultaneously. At the resulting parameter point, no cheaper method is feasible and \(m\) is feasible, so \(m\) belongs to the constrained argmin. This proves the exact projection formula.

Finally, on the original simultaneous confidence event, the true margin vector belongs to every rectangular interval at every monitored time. Pathwise nesting and common exposures imply that the shifted true risks also satisfy the order constraint. Hence the true joint parameter lies in the smaller structural confidence region at every monitored time. Projecting that smaller region onto the constrained argmin therefore preserves the same time-uniform coverage event.

## Verification

The proof is analytic. The standalone script `verify_nested_ccsmcs.py` uses exact rational arithmetic to check the suffix-maximum and prefix-minimum constructions, the compatibility criterion, the possible/certified feasibility rules over an exhaustive finite rational family, and the strict two-method example above. It prints `VERIFY_OK` when all checks pass.

The finite enumeration is supplementary. It does not prove the infinite sequential statement; that statement follows from the deterministic order inequalities and from the simultaneous confidence event supplied by the underlying sequential construction.

## Relationship to prior work

Li and Zhu introduce Coverage-Constrained Sequential Model Confidence Sets for multiple prefix-average conditional miscoverage constraints. Their formulation explicitly allows a constraint index to encode a nominal level, and their exact projection uses a simultaneous rectangular confidence region with separate possible-feasible and certified-feasible sets. The inspected source does not impose cross-level nesting or intersect the rectangle with an order cone. The present result retains their product-region constrained-argmin logic but gives the exact sharper projection when a chain of constraints is known to arise from nested prediction sets.

Ochoa Rivera and Tewari study online conformal prediction across multiple coverage levels and make nestedness a central design requirement. Their work establishes that the nested multi-level setting is practically and statistically motivated, but it does not address coverage-constrained sequential model selection or the order-cone sharpening of a model confidence set.

Classical order-restricted and isotonic inference shows broadly that known monotonicity can improve statistical inference, including simultaneous confidence procedures. That literature is important background for the structural idea. The specific result here is the closed-form suffix/prefix closure of the CC-SMCS rectangle, the unchanged possible-feasibility rule under monotone tolerances, the strengthened certification rule, and the resulting exact constrained-argmin projection with the original time-uniform error budget. Targeted searches did not identify this combination as a prior stated result. Because the underlying box/order-cone geometry is elementary, an equivalent deterministic lemma may exist under different terminology; no claim of exhaustive historical priority is made.

## Limitations

The theorem requires actual pathwise nesting, common exposure weights across the ordered levels, and monotone tolerances. It is not valid merely because nominal levels are ordered. If separate adaptive pipelines produce crossing prediction sets, the risk order can fail. If levels use different exposure sequences, weighted prefix averages can also fail to preserve the pointwise order.

The refinement does not improve the marginal confidence sequences themselves and does not change the source method's probability guarantee. Its gain comes entirely from deterministic structural information. More general partial orders, incompatible observed boxes, and data-dependent procedures that alter the nesting relation require separate treatment.

Literature inspection cannot exclude every equivalent formulation in unindexed or inaccessible work. The originality assessment concerns the stated sequential conformal-model-selection specialization and its exact closed-form consequences, not the general field of isotonic inference.

## References

1. J. Li and H. Zhu, “Sequential Confidence Sets for Coverage-Constrained Conformal Model Selection,” arXiv:2609.28522v1, first submitted 22 September 2026.
2. E. Ochoa Rivera and A. Tewari, “Online Conformal Prediction: Enforcing monotonicity via Online Optimization,” arXiv:2605.12668v1, first submitted 12 May 2026.
3. R. Dykstra and H.-c. Kuo, “Order Restricted Inference,” Wiley StatsRef: Statistics Reference Online, DOI: 10.1002/9781118445112.stat07403.
4. R. Berk and R. Marcus, “Dual Cones, Dual Norms, and Simultaneous Inference for Partially Ordered Means,” Journal of the American Statistical Association 91(433), 318–328 (1996), DOI: 10.1080/01621459.1996.10476691.
