# Scientific review: Frobenius orbits of Klein-quartic fourfold tangents

## Correctness — PASS
For the exact plane model in characteristic three, its gradient is \((Z^3,X^3,Y^3)\), so the quartic is smooth. The directional expansion contains linear, cubic, and quartic terms but no quadratic term. At a hyperosculation point, equality of the cubic functional with a scalar multiple of the cube of the tangent linear functional gives \([1:u^{10}:u]\) with \(u^{91}=1\) and \(u^{28}+u^7+1=0\). The separable quartic equation for \(u^7\), together with the orders of \(3\) modulo \(7,13,91\), proves the 28-point classification and exact Frobenius orbit sizes. The standalone finite-field checker passed and is a corroborating check, not the source of the infinite proof. No two-point bitangent exists by Bézout and universal contact at least three.

## Originality — PASS, with priority risk
The 28 fourfold tangent count and vanishing Hessian are known (Elkies 1999); the classical 28 bitangent arrangement is known (Janasz--Pokora--Zieliński 2023). Geometric equivalence of the characteristic-three Klein and Fermat quartics is also known (Dolgachev--Martin 2024). The result here is instead the explicit Frobenius permutation on those tangencies for the displayed \(\mathbb F_3\)-model: one rational tangent, one degree-three orbit, four degree-six orbits, and the resulting extension-field formula. The complex bitangent arrangement and algebraically closed automorphism classification do not determine this field-of-definition pattern, and the distinct maximal-model arithmetic described by Elkies cannot be transferred without tracking the twist. Targeted historical and statement-level searches did not find a covering orbit formula, but indexed search cannot establish universal novelty. Residual risk: older arithmetic treatments of Klein twists or an unindexed computation may already imply the same orbit decomposition.

## Mathematical value — PASS
The rational structure of all special tangent lines is a natural arithmetic invariant of a distinguished genus-three curve. It is not determined by its geometric count or automorphism group. The exact six Frobenius orbits and minimal splitting field give a complete, reusable finite-field classification of distinguished tangents of this integral model, where a geometric equivalence to a Hermitian quartic can obscure the arithmetic twist.

## Limitations
This is a theorem about the particular model over \(\mathbb F_3\), not an assertion about the field of definition of distinguished points on every isomorphic geometric model. It does not compute all line incidences, and literature priority beyond accessible material is not established. Independent mathematical validation has not been carried out.

Self-review: passed. Independent audit: not yet performed.
