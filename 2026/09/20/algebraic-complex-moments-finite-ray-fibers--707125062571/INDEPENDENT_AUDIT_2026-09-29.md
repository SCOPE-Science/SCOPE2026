# Independent Audit — 2026-09-29

**Record:** `2026/09/20/algebraic-complex-moments-finite-ray-fibers--707125062571`  
**Title:** Finite ray fibers remove the injectivity hypothesis in algebraic complex-moment extensions  
**Repository:** `SCOPE-Science/SCOPE2026`  
**Audited tree:** `85bc9230c5ac6c5e47d542726b2727ba4f797056`  
**Disposition:** **PASSED**

## Three-axis assessment

- **Correctness — PASS:** PASS. Even-total-degree moments determine, for each q, the circle pushforward weighted by |z|^{2q}; odd-total-degree moments likewise determine the complex measure weighted by z|z|^{2q}. Fourier uniqueness therefore gives equality of both families. Disintegration over u=z/bar z reduces the problem to each finite line fiber. Vandermonde inversion recovers the total mass at every distinct squared radius, and the z-weighted moments recover the signed mass difference between the only possible antipodal pair at that radius. This determines every conditional measure. For an algebraic zero set avoiding 0, restricting p(z,bar z) to any line gives a nonzero one-variable polynomial because p(0,0) is nonzero, so finite fibers are automatic. The stated bijection and determinacy consequences then follow from Theorem 22(i)-(ii) of the source together with the new separation lemma.
- **Originality — PASS:** PASS. The 2019 Cichon--Stochel--Szafraniec theorem explicitly assumes injectivity of psi on the algebraic support for the bijection/determinacy conclusion, and the source itself notes that this geometry fails for common curves. Focused searches did not locate a later finite-fiber replacement or the even/odd fiberwise Vandermonde argument. The result therefore appears to remove a genuine unnecessary hypothesis in the algebraic-away-from-zero setting.
- **Scientific value — PASS:** PASS. The improvement substantially enlarges the source theorem from at-most-one point on each radial line to every algebraic zero set avoiding the origin, which includes most standard algebraic curves excluded by the injective formulation. The proof is conceptually clean and clarifies exactly what the upper-diagonal moments recover on a finite angular fiber.

## Independent findings
- The index pairs (q+k,q-k) and (q+k+1,q-k) remain in the upper-diagonal lattice for every integer k, so full Fourier uniqueness is available.
- For fixed angular coordinate and squared radius there are at most two points, necessarily antipodal, and the pair of recovered quantities (mass sum, z-weighted mass) separates their weights.
- Absolute integrability of z|z|^{2q} follows from the assumed upper-diagonal moments (or adjacent even radial moments), so the complex pushforwards are finite.
- The publisher-extracted text of Theorem 22 confirms that the original algebraic conclusion uses injectivity of psi_p.

## Independent checks
- Re-derived the Fourier coefficient identities for both alpha_q and beta_q for arbitrary positive and negative k.
- Checked the regular conditional/disintegration step and the finite Vandermonde reconstruction on each fiber.
- Checked the algebraic-line restriction Q_t(r) and the role of p(0,0) != 0.
- Compared directly with the searchable publisher text of Theorem 22 and Corollary 23; the PDF itself could not be reopened for screenshot rendering because the publisher download URL returned 404 in the web tool.

## Literature evidence
- https://doi.org/10.7146/math.scand.a-112091 — Cichon--Stochel--Szafraniec (2019), Theorem 22; searchable publisher text states the injectivity hypothesis and its consequences.
- https://arxiv.org/abs/1803.03066 — Open preprint of the same complex-moment determinacy/extendibility work.
- https://doi.org/10.1007/s43036-020-00089-z — 2020 survey context on Szafraniec's work; no finite-fiber strengthening located.

## Limitations
- The theorem still requires finite ray fibers and does not settle the general singleton-PDE determinacy question.
- Algebraic supports containing the origin or a whole radial line are outside the corollary.
- The publisher PDF URL exposed searchable theorem text but returned 404 when reopened for page rendering, so no claim is made of a fresh visual PDF inspection in this run.

The assigned source tree was unchanged between inventory commit `e9ed144c13b7834896a844cc4f9cac3c25a168a6` and audited commit `253a0fe5d0217455660a277f9adb940030e567ad`; the assigned tree SHA therefore remains the exact current tree audited. GitHub was used only as read-only evidence; no repository writes were made. Audit timestamps and this audit-file date use UTC as required by the task-specific audit contract.
