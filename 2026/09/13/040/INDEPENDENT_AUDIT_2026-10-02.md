# Fresh independent audit

Assessed at: 2026-10-02T17:01:01Z (UTC).
Disposition: repaired. Correctness / Originality / Value: PASS / PASS / PASS.

## Correctness

The complete finite table and all-k degrees-at-most-four proof pass. Corrected a genuine k=3 intermediate-rank typo: I=2, cap=2, D=0, hence H5=(2-2)-0=0; the final dimension was already right. The strengthened verify_low_degree.py independently implements quotient projection and vertexwise diagonal multiplication, compares every free-domain basis to the historical specialized differential, checks ALL 6,36,120,300,630 relation columns and every adjacent-transposition action for k=3..7, and asserts exact I/cap/D/H5 and A6 ranks. Actual run exited 0 with VERIFY_LOW_DEGREE_OK. Historical dense quotient k4..7, finite characters, degree-four boundary k10/11 and A6 ranks were also independently replayed. Rational model applicability is supplied precisely by Lambrechts--Stanley 2008 Theorem10.1's equivariant DGmodule quasi-isomorphism: M is closed oriented triangulated and formal, A is a connected rational Poincare-duality model with the required zigzag. Idrissi 2018v4 Theorem95 initial real CDGA statement needs no framing; its framing conditions concern the stronger comodule clause, and no general rational CDGA inference is made. Transfer plus exact finite-group invariants is stated correctly; the falling-factorial moment formula includes k>=a+2b and proves the claimed all-k H4 multiplicity. No total H6, geometric map isomorphism, uniform slope-two range or sharpness witness is certified.

## Originality

Read the highly relevant primary full texts, not only abstracts. Palmer's theorem concerns open connected manifolds and a qualitative stable range; the assigned closed four-manifold exact low-degree table is not a theorem there. Idrissi supplies the general equivariant Lambrechts-Stanley model for simply connected closed manifolds but no computed CP2#CP2 exterior-square multiplicities. Felix--Tanre computes ordinary unordered rational cohomology, including CP2 but not this connected sum with the nontrivial W_k local system. Maguire/Christie/Francour's concrete tables are likewise ordinary unordered cohomology. Searched equivalent Specht (k-2,1,1) and the precise manifold/coefficient/degree formulation, including Resultary public corpus. The closest Resultary hit was the assigned SCOPE040 self-entry; other hits concern different manifolds and coefficients. A 2025 stable Specht multiplicity computation concerns ordered configurations in the complex plane, not this manifold. No precise earlier H4/H5 quotient table or dominant theorem was located. Discovery limitations remain acknowledged.

## Value

A reproducible exact low-degree table for a natural nontrivial FI local system on a closed positive-definite four-manifold constrains the proposed slope-2 stability problem. The H5 quotient calculation is substantive: unquotiented invariant rank four would falsely suggest a two-dimensional kernel until the Kriz relations are accounted for. The source honestly limits H6 and geometric-map claims.

## Primary-source comparison

- The Lambrechts-Stanley Model of Configuration Spaces: https://arxiv.org/pdf/1608.08054. Read: Version4 primary PDF, diagonal/model definitions, Theorem95 full two-clause statement/proof scope, Corollary116 and Proposition115; PDF lines2644-2682 and3324-3333.. Assessment: MODEL_VALIDATES_METHOD_NOT_THE_EXACT_TABLE. Theorem95 first equivariant CDGA zigzag is over R and requires simply connected closed smooth dim>=4; framing/chi=0 applies to further operadic enhancement. Corollary116 has no framing hypothesis. The statement validates the method but does not give this exact table.
- The cohomology algebra of unordered configuration spaces: https://arxiv.org/abs/math/0311323. Read: Introduction lines 7-42, model relations lines 10-18, transfer/invariants Proposition 1 lines 63-77, CP2 Section 5 lines 313-345. Assessment: ORDINARY_COEFFICIENTS_AND_DIFFERENT_MANIFOLD. The detailed table is for CP2 and trivial S_n invariants, not CP2#CP2 with W_k.
- Twisted homological stability for configuration spaces: https://arxiv.org/abs/1308.4397. Read: Abstract and theorem scope, open-connected-manifold hypothesis. Assessment: QUALITATIVE_OPEN_MANIFOLD_NOT_EXACT_CLOSED_CASE. Paper's stated M is open connected.
- Computing cohomology of configuration spaces: https://arxiv.org/html/1612.06314. Read: Abstract, computational scope and examples; searched full HTML for matching manifold/coefficient. Assessment: ORDINARY_UNORDERED_TABLES_NOT_MATCH. The paper computes untwisted rational cohomology and does not furnish the assigned exterior-square CP2#CP2 H5 quotient table.
- A remarkable DGmodule model for configuration spaces: https://msp.org/agt/2008/8-2/agt-v8-n2-p21-p.pdf. Read: Introduction/model scope, Definition3.4 complete relations; Section10 setup and Theorem10.1, PDF lines1587-1600. Assessment: EXACT_MODEL_APPLIES_NOT_THE_SPECIFIC_TABLE. Closed oriented triangulated M, connected Poincare-duality CDGA A with zigzag A_PL(M)<-R->A; equivariant DGmodule quasi-isomorphism, sufficient for rational cohomology representations. Does not evaluate CP2#CP2 exterior-square ranks.

## Explicit remaining risks

- No exhaustive literature database guarantee: poorly indexed thesis or unpublished notes could have matching exact ranks.
- The H6 claim is explicitly only the A6 summand, not full H6; geometric stabilization map identification remains unproved as source says.
- The original general-stability target remains unproved; this is only the explicitly stated low-degree table. Historical exploratory scripts are not separately certified as new theorems.

All source-tree, original-line and artifact evidence is preserved. The old assessment is inactive historical evidence, not this audit. This review is an independent scientific assessment to the best of our knowledge, not expert attestation or formal Lean verification; the latter two channel states remain exactly as in the frozen source. Publication is not performed by this isolated package.

