# Independent Audit — 2026-09-30

**Record:** `2026/09/20/local-pseudo-morphic-nilpotent-radical-left-special--4e457d3ea9da`  
**Title:** Local left pseudo-morphic rings with nilpotent radical are left special  
**Repository:** `SCOPE-Science/SCOPE2026`  
**Audited tree:** `1ba7e5e54531e32c3b73a147a3ce7ce1318a84fd`  
**Disposition:** **PASSED**

## Three-axis assessment

- **Correctness — PASS:** The radical-filtration proof is correct and sided consistently. If 0!=a in J^{n-1}, then J annihilates a and every element outside J is a unit, so l(a)=J and Ra~=R/J is simple. From Ra=l(c), nonzero properness forces c in J, while J^{n-1}c=0 gives J^{n-1}<=l(c)=Ra<=J^{n-1}; hence S=J^{n-1}=Ra=l(c) is simple. Right multiplication by c is a homomorphism of left R-modules with kernel S, so R/S~=Rc, and on J^i it gives J^i/S ~= J^ic <= J^{i+1}. Downward induction from S proves finite left length. Since both S and R/J are simple, Rc and J have the same finite length and Rc<=J, hence Rc=J. Nilpotence of c follows from c in J. The J=0 division-ring case is separately harmless.
- **Originality — PASS:** Camillo–Nicholson (2015) explicitly pose exactly whether a local left pseudo-morphic ring with nilpotent Jacobson radical must be left special. The principal residual risk in the filed record was the 2023 CEFR paper of Neishabouri–Tolooei–Bagheri. After open routes did not expose full text, I obtained and read the complete 19-page paper through authorized institutional access (Oxford job 1234f534b699f4566cf759e305a1226e). Its Section 6 treats left pseudo-morphic rings—reversible/duo consequences, semiprime and prime cases, regularity of the center, finite-over-center regularity, and nonsingular-extending cases—but it does not state the local nilpotent-radical theorem or answer Camillo–Nicholson Question 1. The filed result therefore clears its strongest identified originality risk.
- **Scientific value — PASS:** The theorem gives an affirmative solution to an explicit published open question and strengthens it substantially: one pseudo-morphic witness in the last nonzero radical layer already forces the whole radical to be principal and the ring left special. The proof also derives finite length rather than assuming it.

## Independent findings
- The equality l(a)=J uses locality essentially: every r outside J is a unit, so ra=0 would contradict a!=0.
- The quotient embeddings J^i/S -> J^{i+1} are induced by right multiplication by c and are left-module maps; there is no left/right reversal.
- The 2023 CEFR paper was read completely. Its Section 6 contains no local-plus-nilpotent-radical left-special theorem and does not resolve Camillo–Nicholson Question 1.
- The theorem is stronger than the published question because it assumes pseudo-morphic behavior only for one nonzero a in J^{n-1}, not for every element.

## Independent checks
- Reconstructed all module-kernel and finite-length steps independently, including the restriction of multiplication by c to each radical power.
- Checked the exact Camillo–Nicholson question and the left-special criterion against the 2015 source.
- After OA/preprint routes failed, obtained all 19 pages of Neishabouri–Tolooei–Bagheri (2023) through authorized institutional access and inspected its complete Section 6 result list.
- Confirmed the current repository tree equals the assignment guard and contains no pre-existing 2026-09-30 independent-audit files.

## Literature evidence
- https://doi.org/10.24330/ieja.266221 — Camillo–Nicholson (2015), source of the explicit local nilpotent-radical question and left-special equivalences.
- https://doi.org/10.1080/00927872.2022.2115504 — Neishabouri–Tolooei–Bagheri (2023), complete 19-page text read through authorized institutional access; Section 6 does not contain the filed theorem.
- https://doi.org/10.1142/S0219498818500755 — Alkan–Nicholson–Özcan (2018), stronger comorphic-ring context rather than the present left pseudo-morphic local theorem.

## Limitations
- The theorem assumes locality and nilpotence of the Jacobson radical; it does not classify the nonnilpotent or nonlocal cases.
- Originality is assessed against the searched pseudo-morphic/CEFR/comorphic literature; differently named older annihilator-ring terminology remains a low residual risk.

The assigned source tree remained unchanged from the inventory/source-tree-check interval through current main commit `eff2c6312cec5b0dee5115e5f42211a853092dfb`; the exact tree audited is `1ba7e5e54531e32c3b73a147a3ce7ce1318a84fd` and matches the assignment guard. GitHub was used only as read-only evidence; no repository writes were made. Audit timestamps and this audit-file date use UTC under the task-specific audit contract.
