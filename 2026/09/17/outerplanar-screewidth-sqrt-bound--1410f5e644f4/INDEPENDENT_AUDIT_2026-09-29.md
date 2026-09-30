# Independent Audit — outerplanar-screewidth-sqrt-bound--1410f5e644f4

**Audit date:** 2026-09-29 (UTC)  
**Repository:** `SCOPE-Science/SCOPE2026`  
**Assigned source tree:** `764a80cd8f6c63b116a4f73f77054a1425294b42`  
**Audited current source tree:** `764a80cd8f6c63b116a4f73f77054a1425294b42`  
**Audited repository commit:** `eff2c6312cec5b0dee5115e5f42211a853092dfb`  
**Disposition:** passed

The current `main` directory tree SHA exactly matches the assignment tree SHA. No intervening source change required a stale-source re-audit.

## Correctness — PASSED

PASS. The recursive tree-cut proof checks. A centroid of the subcubic weak dual supplies an interior edge whose two dual sides have at most 3(n-2)/4 faces, hence every component after deleting the edge endpoints has fewer than 3n/4 vertices. If one such component has boundary larger than (2+sqrt(2))*sqrt(n)+4, all those boundary edges hit the two separator endpoints, forcing the larger degree above sqrt(2n) so Rivera Laboy's Lemma 3.10 applies. Enlarging the separator preserves the balance. In the recursive assembly, every old link or node adhesion in a child can gain only edges from that child's external boundary, the new attachment link has exactly that boundary, and the central node adhesion is zero. The numerical recurrence closes with constant 40 for n>=6, while one-bag decompositions cover n<=5.

## Originality — PASSED

PASS, WITH RECENT-WORK QUALIFICATION. Rivera Laboy's September 2026 preprint explicitly asks whether outerplanar graphs have screewidth O(sqrt n), and its accessible text supplies the bounded-boundary separator lemma rather than the recursive tree-cut conclusion. The foundational screewidth paper supplies definitions, subgraph monotonicity, and sn<=scw. Targeted searches through the audit date did not locate another resolution of the stated outerplanar screewidth question.

## Scientific value — PASSED

PASS. The theorem answers an explicit open question and, combined with the fan scramble lower bound, determines the extremal order Theta(sqrt n). The proof isolates a reusable separator-to-tree-cut recursion rather than reporting a finite computation.

## Independent checks

- independently rederived the weak-dual 3/4-balanced interior-edge lemma
- checked the degree-threshold implication needed to invoke Rivera Laboy's separator lemma
- checked all old-link, old-node, new-link, and central-node adhesion bounds in the recursive tree-cut assembly
- checked 40*sqrt(3/4)+(2+sqrt(2))+4/sqrt(n) <= 40 for n>=6
- verified current tree identity and absence of 2026-09-29 independent-audit marker files

## Limitations

- The constant 40 is coarse and not claimed sharp.
- The argument depends on Rivera Laboy's Lemma 3.10 as stated in arXiv:2609.03755v2.
- The motivating question is extremely recent, so unindexed contemporaneous work remains a residual originality risk.

## Evidence and references

- https://github.com/SCOPE-Science/SCOPE2026/tree/eff2c6312cec5b0dee5115e5f42211a853092dfb/2026/09/17/outerplanar-screewidth-sqrt-bound--1410f5e644f4
- https://arxiv.org/abs/2609.03755
- https://arxiv.org/abs/2209.01459

This audit changes only the independent-audit channel. Lean verification and expert attestation remain exactly as previously recorded.
