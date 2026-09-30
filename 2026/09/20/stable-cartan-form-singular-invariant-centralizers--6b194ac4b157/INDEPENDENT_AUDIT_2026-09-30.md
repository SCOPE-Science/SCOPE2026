# Independent Audit — Stable integral Cartan forms under singular equivalence of centralizer matrix algebras

**Audit date:** 2026-09-30 (UTC) (UTC)  
**Repository:** `SCOPE-Science/SCOPE2026`  
**Assigned source tree:** `b53ee294270fb7276345519cfa8ca964b3fe2fe3`  
**Audited current source tree:** `b53ee294270fb7276345519cfa8ca964b3fe2fe3`  
**Audited repository commit:** `eff2c6312cec5b0dee5115e5f42211a853092dfb`  
**Disposition:** passed

The current `main` record tree exactly matches the assignment snapshot. GitHub was used only as read-only evidence. The UTC-dated independent-audit files were absent when this guarded change set was prepared.

## Correctness — PASSED

PASS. For one primary block with distinct exponents t1>...>ts, the Cartan matrix C=(min(ti,tj)) is carried by successive unimodular simultaneous differences to diag(t1-t2,...,t_{s-1}-t_s,t_s). Taking the block sum over primary factors therefore gives the asserted stable integral diagonal form and Cartan cokernel. Chen–Xi's current singular-equivalence classification explicitly preserves the multiset U of non-unit gaps under Sg-equivalence; combining that with the known diagonalization gives stable integral congruence, not merely determinant equality. The realization argument is also exact: choosing ti=d_i+...+d_s for cyclic factors d_i>=2 yields gap multiset {d_i}. I independently checked determinant/gap identities on several nontrivial exponent sets and found exact agreement.

## Originality — PASSED

PASS, narrowly scoped. Dubey–Prasad–Singla compute the centralizer Cartan matrices; Li–Xi give the integral congruence used for derived/stable equivalence; Chen–Xi's 2026 singular-equivalence theorem preserves the gap multiset and advertises Cartan-determinant invariance. The inspected current Chen–Xi text does not state the stronger stable integral congruence, full Cartan-group invariant, or universal realization inside nilpotent one-matrix centralizers. The submitted contribution is therefore a short but genuine synthesis/consequence of prior structure theorems, not a new Cartan diagonalization.

## Scientific value — PASSED

PASS. The result upgrades a scalar determinant invariant to the full integral stable form and finite Cartan cokernel within a concrete singular-equivalence class, and it shows that every finite abelian group already occurs in nilpotent centralizer algebras. The refinement can distinguish examples with equal Cartan determinant, so it adds real classification power despite the elementary final argument.

## Independent checks

- Re-derived the unimodular simultaneous-difference diagonalization of the min-matrix Cartan block.
- Checked sample exponent sets (7,4,1), (9,6,5,2), and (5,3): determinants equal the products of the asserted gap diagonal entries.
- Inspected the current Chen–Xi public full-text extraction: its singular-equivalence proof gives Sg-equivalence and equality of the U-multisets, while the theorem statement records Cartan-determinant invariance rather than the full cokernel.
- Compared against Li–Xi arXiv:2312.08794 and Dubey–Prasad–Singla arXiv:math/0611897 so the known Cartan formula and integral diagonalization receive no novelty credit.
- Searched the current SCOPE repository for a duplicate stable-Cartan/Cartan-group centralizer theorem; no overlapping record was located.
- Verified the current main tree SHA exactly equals the assigned source-tree SHA; the 2026-09-30 audit pair is absent and VERIFICATION.md retains blob SHA 31a3bb079c3be0cdcbee536377edadb1613bf629.

## Limitations

- The singular-equivalence conclusion is only for centralizer matrix algebras.
- The integral diagonalization itself is prior work; originality is restricted to its singular-equivalence consequence and the concrete realization statement.
- Because the main new invariant is a concise corollary of recent classification results, differently phrased prior observations remain a residual priority risk.

## Evidence and references

- https://arxiv.org/abs/math/0611897
- https://arxiv.org/abs/2312.08794
- https://arxiv.org/abs/2603.20643
- https://arxiv.org/abs/1804.01168
- https://github.com/SCOPE-Science/SCOPE2026/tree/eff2c6312cec5b0dee5115e5f42211a853092dfb/2026/09/20/stable-cartan-form-singular-invariant-centralizers--6b194ac4b157

This guarded change set updates only the independent-audit channel. Lean verification and expert attestation remain exactly as previously recorded.
