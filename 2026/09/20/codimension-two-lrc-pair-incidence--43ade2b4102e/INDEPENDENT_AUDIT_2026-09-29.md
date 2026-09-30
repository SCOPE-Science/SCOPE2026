# Independent Audit — 2026-09-29

**Record:** `2026/09/20/codimension-two-lrc-pair-incidence--43ade2b4102e`  
**Title:** Exact codimension-two LRC distance criteria from pair-incidence covers  
**Repository:** `SCOPE-Science/SCOPE2026`  
**Audited tree:** `7f825bbf9b3e2c8295aa00a3e0e0a0a926433d09`  
**Disposition:** **PASSED**

## Three-axis assessment

- **Correctness — PASS:** Specializing the published LRC multigraph criterion to k1=n1-2 makes deletion of a vertex pair exact, so the condition is c_G(u,v)=d(u)+d(v)-m(u,v)>=q. For odd q=2h+1, the minimum-degree/handshake lower bound gives at least ceil((h+1)N/2) edges, and an almost-regular simple graph with minimum degree h+1 attains it when h+1<=N-1. The separate q=1,2,4 counting arguments and block constructions attain their stated thresholds. Substitution into the known d* versus d*-1 dichotomy and into the displayed infinite family is arithmetically consistent.
- **Originality — PASS:** Khabbazian–Médard’s open preprint/journal development gives the general multigraph equivalence and an exact codimension-one case, while noting that similar tools may extend further. Its accessible full preprint does not state the codimension-two odd-gap formula or q=2,4 thresholds. Focused searches did not locate those exact formulas or the resulting infinite LRC family, leaving only residual terminology risk for the elementary auxiliary graph invariant.
- **Scientific value — PASS:** The result converts the general graph characterization into sharp, closed-form d* versus d*-1 criteria across a broad codimension-two regime, including all feasible odd gaps in the stated range and two even gaps, and it supplies infinite parameter families beyond the exact cases in the source paper.

## Independent findings
- Re-derived c_G(u,v)=M-|E(G[V\{u,v}])| and the exact reduction to the pair-incidence cover number.
- Checked the odd-q lower bound in both minimum-degree cases and the almost-regular construction.
- Checked q=2 and q=4 lower-bound optimizations and the listed residue-block constructions.
- Recomputed (n1,k1,n2,k2)=(N,N-2,N+1,N-2), q=3 and d*=2N+3 for the infinite family.

## Independent checks
- Read the accessible arXiv preprint of Khabbazian–Médard and compared its exact theorem/case list with the filed specialization.
- Searched codimension-two, n1-k1=2, pair-incidence, and LRC/LMD synonyms for later exact formulas; none matching the record were located.
- Independently stress-tested the combinatorial lower/upper-bound logic on the small residue blocks described in the proof.

## Evidence and literature
- https://arxiv.org/abs/1809.09227 — Khabbazian and Médard, open preprint giving the general multigraph characterization and codimension-one exact case.
- https://doi.org/10.1016/j.disc.2024.114298 — Journal development of the LRC graph-theoretic largest-minimum-distance approach.
- https://doi.org/10.1109/TIT.2015.2472515 — Wang and Zhang (2015), earlier integer-programming LRC distance-bound context.

## Limitations
- The general odd formula is restricted to q<=2N-3; larger odd gaps and general even q>=6 are not settled.
- The coding statement is for the unrestricted-field linear LMD problem and does not optimize alphabet size.
- The auxiliary pair-incidence extremal lemma is elementary and could have appeared under other graph-theoretic terminology even though no such coverage was located.

The assigned source tree remains exactly `7f825bbf9b3e2c8295aa00a3e0e0a0a926433d09` at current main commit `eff2c6312cec5b0dee5115e5f42211a853092dfb`; it matches the assignment guard. GitHub was used only as read-only evidence and no repository writes were made. Audit timestamps and this audit-file date use UTC under the task-specific contract.
