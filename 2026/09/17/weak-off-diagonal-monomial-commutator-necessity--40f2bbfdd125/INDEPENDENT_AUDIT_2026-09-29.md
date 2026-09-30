# Independent audit — 2026-09-29

**Record:** `2026/09/17/weak-off-diagonal-monomial-commutator-necessity--40f2bbfdd125`  
**Audited source tree:** `0ac8919dbefe9a0336fb7c491992a64ac63fc4d6`  
**Repository snapshot:** `SCOPE-Science/SCOPE2026@253a0fe5d0217455660a277f9adb940030e567ad`  
**Disposition:** **PASSED**

## Correctness — PASS

PASS. I inspected the complete Li--Zeng preprint after direct open-access retrieval in the browser was unavailable. Their proof of the all-dimensional diagonal necessity theorem is written in dimension three but explicitly states that the companion-cube determinant argument extends to arbitrary dimension, and their Section 3 reduces the mean oscillation to finitely many translated commutator outputs on indicators (or a bounded mean-zero substitute) before taking the final L^p norm. The record changes only that last function-space step. For 1<q<infinity, ||F||#=sup_A |A|^{-1/q'}∫_A|F| is an equivalent Banach norm on weak L^q, so Minkowski is legitimate and ||T f||#<=q'||T f||_{q,infinity}. On a major subset of the companion cube this yields m_Q |Q|^{1/q} <= C ||T|| |Q|^{1/p}; the complementary case has the same bound because the Li--Zeng test function satisfies |g|<=2 1_Q. Since alpha/|beta|=1/p-1/q, division gives exactly the claimed BMO^{gamma,alpha} seminorm. The q=p boundary reduces correctly to BMO^gamma, and translations do not affect the weak norm.

## Originality — PASS

PASS, qualified. Li--Zeng's September 2026 theorem is diagonal L^p-to-L^p necessity in every dimension. Oikari's earlier off-diagonal theory supplies sufficiency in arbitrary dimension but its necessity results are restricted to the plane, and the higher-dimensional necessity mechanism is identified as an open direction. Current searches did not locate an all-dimensional L^p-to-weak-L^q necessity theorem. The result is a concise consequence of a very recent proof rather than a new geometric construction, so contemporaneous independent observation is the principal priority risk.

## Scientific value — PASS

PASS. The weak-target formulation is genuinely stronger than strong L^q necessity and, inside the known Oikari sufficiency region, closes the equivalence between the anisotropic Campanato condition, strong boundedness, and weak boundedness in every dimension. Outside that region it still supplies a clean necessary condition. Although the proof modification is short, it resolves a named higher-dimensional necessity gap and exposes useful Lorentz-space flexibility in the companion-cube method.

## Sources checked

- https://arxiv.org/abs/2609.18613 — Li and Zeng, Curved commutators in higher dimensions; all-dimensional diagonal necessity and the companion-cube proof adapted here.
- https://arxiv.org/abs/2304.00621 — Oikari, off-diagonal boundedness/compactness along monomial curves; arbitrary-dimensional sufficiency with necessity restricted to the plane.

## Limitations

- The theorem is unweighted and covers only 1<p<=q<infinity; it does not settle q<p, q=infinity, Bloom weights, compactness, or general finite-type curves.
- The higher-dimensional geometry is inherited from Li--Zeng; the new contribution is the weak/off-diagonal final norm argument.
- Because the Li--Zeng preprint is only days old, originality is especially vulnerable to contemporaneous unindexed observations.

No GitHub content was modified during this audit. This file records an independent evidence review; it is not a peer-review or priority guarantee.
