# Review of Automorphisms of truncated coordinate-cross algebras over arbitrary fields

## Correctness
PASS. For \(d\ge3\), the induced map on \(\mathfrak m/\mathfrak m^2\) must be monomial because pairwise-zero products force disjoint supports in \(\mathfrak m^2/\mathfrak m^3\). On each target branch, multiplication by the principal image has annihilator exactly \(k x_j^{d-1}\), forcing every off-branch component into the top degree. This gives the unique normal form, and the converse is immediate from the defining relations and invertible linear part. The semidirect product follows from the additive shear subgroup and branch substitutions. For \(d=2\), \(\mathfrak m^2=0\), giving \(\operatorname{GL}_n(k)\). The finite-field order follows from \(|J_d(\mathbb F_q)|=(q-1)q^{d-2}\). Exhaustive checks in six small cases agree and end with `CHECK_OK`.

## Originality
PASS for the stated arbitrary-field claim. The 2024 and 2026 monomial-algebra papers explicitly work in characteristic zero and therefore strongly cover the characteristic-zero specialization in principle. The accepted statement is broader: its normal form is proved over every field, including positive characteristic, and yields an exact finite-field order formula. published-finding corpus searches for the exact quotient, truncated-axis/fiber-product aliases, symmetric component group, and finite-field order found no equivalent record. Web searches likewise found the characteristic-zero general theory but no positive-characteristic treatment of this exact family. Residual risk remains that older fiber-product or Artinian Stanley--Reisner literature contains the same elementary description under different terminology.

## Value
PASS. The family \(A_{n,d}\) is a canonical truncation of the Stanley--Reisner algebra of isolated vertices. The theorem identifies its full symmetry group uniformly in the field and exposes a sharp structural change at the first non-square-zero level: \(d=2\) has the full connected reductive group \(\operatorname{GL}_n\), whereas \(d\ge3\) has only monomial linear parts, component group \(S_n\), and solvable identity component. The finite-field formula converts that structural statement into an exact invariant for all prime powers. This is a natural family-level classification rather than an arbitrary finite computation.

## Closest literature and limitations
The closest direct literature is arXiv:2609.13741v1, together with arXiv:2408.02197 and arXiv:2409.15081. These sources establish general characteristic-zero structure and reconstruction results; arXiv:2409.15081 even uses \((x^3,xy,y^3)\), the \((n,d)=(2,3)\) member, as a derivation example. Accordingly, no novelty is claimed for the characteristic-zero case by itself. The final claim is the characteristic-free closed normal form and its finite-field consequences.

Same-model review: passed. Independent audit: not yet performed.
