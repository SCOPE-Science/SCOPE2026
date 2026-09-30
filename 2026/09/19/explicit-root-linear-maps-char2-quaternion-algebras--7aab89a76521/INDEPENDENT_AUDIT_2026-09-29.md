# Independent Audit — Explicit root-linear maps for characteristic-two quaternion division algebras

**Audit date:** 2026-09-29 (UTC)  
**Repository:** `SCOPE-Science/SCOPE2026`  
**Assigned source tree:** `bf2414e12ceaacdb8f7105293cafb869140756d3`  
**Audited current source tree:** `bf2414e12ceaacdb8f7105293cafb869140756d3`  
**Audited repository commit:** `eff2c6312cec5b0dee5115e5f42211a853092dfb`  
**Disposition:** passed

The current `main` record tree exactly matches the assigned source-tree SHA. GitHub was used read-only as evidence, and the dated independent-audit files were absent when this guarded plan was prepared.

## Correctness — PASS

PASS. For Q=K⊕Kj with standard involution, H=F⊕Kj and A=F. Direct multiplication modulo A gives (c+dj)·z=c^2z+b d^2 sigma(z). Division forces b notin F^2, so b extends to a 2-basis of F. Because K/F is separable quadratic and F/F^2 is purely inseparable, F and K^2 are linearly disjoint over F^2; since i=i^2+a, FK^2=K. Thus {m_S,bm_S} is a K^2-basis of K and each Q-span of m_S is exactly K^2m_S⊕bK^2m_S, proving dim_Q(H/A)=2^{r-1}. Frobenius K→K^2 then makes the displayed coordinate roots unique, and the coordinate projections are precisely all left-Q linear maps H/A→Q, hence all root-linear maps. The F_2((t)) specialization is consistent with the unramified norm/valuation criterion.

## Originality — PASS

PASS, qualified. The complete September 2026 de Seguins Pazzis preprint proves that root-linear maps are exactly left-D linear maps H/A→D and, for quaternion division rings with standard involution, explicitly says A=F, H is the trace kernel, and that it has no constructive description of a root-linear map without choice. The submitted finite-2-rank 2-basis decomposition directly fills that stated constructive gap and computes the whole dual. Targeted searches using the new terminology and older characteristic-two quaternion/p-basis terminology found no equivalent coordinate theorem. Classical quaternion presentations, p-bases, and separability facts receive no originality credit.

## Scientific value — PASS

PASS. The result turns a nonconstructive term in a new classification theorem into an explicit finite coordinate basis, with exactly 2^{r-1} quaternion parameters and a concrete local-field formula. That materially improves the usability of the source classification while staying appropriately narrow.

## Independent checks

- Read the complete relevant portion of de Seguins Pazzis's lawful-open 20-page preprint; Section 2.1 explicitly states the choice-based existence result and the lack of a constructive quaternion example.
- Independently multiplied (c+dj)(zj)bar(c+dj) and recovered the quotient action c^2z+b d^2 sigma(z).
- Reproved b notin F^2 from division and checked the separable/purely-inseparable linear-disjointness step.
- Checked the K^2 direct-sum decomposition and the identification of root-linear maps with left-Q coordinate projections.
- Checked the F_2((t)) example through even/odd Laurent powers and the valuation obstruction to t being a norm.
- Searched targeted root-linear/quaternion and older characteristic-two p-basis literature; no covering explicit dual basis was located.
- Verified the assigned record tree is unchanged from the dispatcher source-check commit to current main and that the dated audit markers are absent.

## Limitations

- The finite-coordinate theorem assumes finite 2-rank and depends on a chosen quaternion presentation and 2-basis; it is not canonical.
- The originality search cannot rule out an older equivalent semilinear decomposition under unrelated p-basis/Hermitian terminology.
- The range-compatible classification itself is prior work; novelty is only the constructive quaternion root-linear term.

## Evidence and references

- https://arxiv.org/abs/2609.20363
- https://doi.org/10.1007/978-3-030-56694-4_6
- https://github.com/SCOPE-Science/SCOPE2026/tree/eff2c6312cec5b0dee5115e5f42211a853092dfb/2026/09/19/explicit-root-linear-maps-char2-quaternion-algebras--7aab89a76521

This change set updates only the independent-audit channel. Lean verification and expert attestation remain exactly as previously recorded.
