# Independent Audit — Sharp lower bound for the average size of maximal matchings in cyclic graphs

**Audit date:** 2026-09-30 (UTC) (UTC)  
**Repository:** `SCOPE-Science/SCOPE2026`  
**Assigned source tree:** `558d0935725d6fd542cd6f9aad1f5c9117da7b7b`  
**Audited current source tree:** `558d0935725d6fd542cd6f9aad1f5c9117da7b7b`  
**Audited repository commit:** `eff2c6312cec5b0dee5115e5f42211a853092dfb`  
**Disposition:** passed

The current `main` record path has no changes from the assignment snapshot, so the audited tree equals the assigned source tree. GitHub was used read-only. The UTC-dated independent-audit files were absent when this guarded change set was prepared.

## Correctness — PASS

PASS. If a connected graph has no maximal matching of size one then avm≥2, so only an edge uv that dominates every edge matters. Every outside vertex is then private to u, private to v, or common to both; if their counts are a,b,q, then n=2+a+b+q and |E|=1+a+b+2q, so the cyclomatic number is exactly r=q. For r≥2, uv is the unique one-edge maximal matching. Every two-edge matching covers both u and v and is maximal, and its count is (a+r)(b+r)-r=ab+r(n-3). Hence avm=2-1/(ab+r(n-3)+1), immediately giving the bound and the equality condition ab=0. Independent exhaustive Graph Atlas computation through order seven reproduced the claimed minimum and a unique extremal isomorphism class for all ten admissible (n,r) parameter pairs.

## Originality — PASS

PASS, with a disclosed source-access residual. Zhang's 2026 full text explicitly says Engbers–Erey asked for extension of the unicyclic average-maximal-matching problem to k-cyclic graphs and then proves only the bicyclic k=2 minimum, matching the r=2 specialization here. Targeted searches did not locate the all-r formula or the book-plus-leaves extremal classification. The Engbers–Erey 2023 full text was not obtained: after open-access search failed, authorized institutional retrieval reached a human-verification gate, so it is not represented as read. Zhang's explicit quotation of their open question and scope makes that residual nondecisive for this narrow all-r theorem.

## Scientific value — PASS

PASS. The result solves the lower-extremal problem uniformly for every cyclomatic number r≥2 in the full attainable regime n≥r+2, converts a core-by-core bicyclic analysis into a one-line dominating-edge count, and identifies a unique extremal family. It is a clean structural extension of the recent bicyclic theorem.

## Independent checks

- Re-derived the dominating-edge partition and verified that the common-neighbor count equals the cyclomatic number.
- Recounted all two-edge maximal matchings and obtained t=ab+r(n-3).
- Checked the equality classification and the n≥r+2 attainability condition.
- Exhaustively enumerated connected Graph Atlas graphs through order seven and recomputed all maximal matchings; all ten admissible parameter pairs matched the formula and had one extremal isomorphism class.
- Read Zhang arXiv:2604.28033 in full; it quotes the k-cyclic extension question and proves only the bicyclic case.
- After open-access search failed for Engbers–Erey 2023, authorized institutional retrieval reached a human-verification gate; no inaccessible text was claimed as read.
- GitHub comparison found no changes under the assigned record path; both dated audit files are absent and VERIFICATION.md retains the verified blob SHA.

## Limitations

- The exact fixed-(n,r) minimum is asserted only for n≥r+2; denser n<r+2 cases are not classified.
- The Engbers–Erey 2023 full text remained behind human verification and was not read.
- The theorem concerns the minimum average size of maximal matchings, not the maximum side of the k-cyclic problem.

## Evidence and references

- https://arxiv.org/abs/2604.28033
- https://doi.org/10.1016/j.dam.2023.08.022
- https://arxiv.org/abs/2608.06818
- https://doi.org/10.1007/s10878-024-01144-8
- https://github.com/SCOPE-Science/SCOPE2026/tree/eff2c6312cec5b0dee5115e5f42211a853092dfb/2026/09/20/sharp-average-maximal-matchings-cyclic-graphs--f5f7fbdc881f

This guarded change set updates only the independent-audit channel. Lean verification and expert attestation remain exactly as previously recorded.
