# Independent Audit — 2026-09-29

**Record:** `2026/09/20/all-characteristic-graphical-group-character-rank-formula--a74f4be4d9c8`  
**Title:** All-characteristic character rank formula for graphical groups  
**Repository:** `SCOPE-Science/SCOPE2026`  
**Audited tree:** `9b5815edae9904a273f858f1cf11daf2c28e2312`  
**Disposition:** **PASSED**

## Three-axis assessment

- **Correctness — PASS:** PASS. For any central extension of the graphical group by C=F_qE with abelian quotient A=F_qV, fixing a central character lambda_y identifies the corresponding complex group-algebra block with a twisted group algebra of A. For a finite abelian A, the commutator bicharacter radical R has |R| simple modules, all of dimension sqrt(|A|/|R|). Rossmann's all-ring commutator formula makes this radical exactly ker B_Gamma(y), because the finite-field trace pairing is nondegenerate. Alternating matrices have even rank also in characteristic 2, so rank 2i yields q^{n-2i} characters of degree q^i. Summing over y gives the boxed formula. The K_{a,b} and K_n corollaries use standard rank counts and check in small cases; for K_3 over F_2 the formula gives 8 linear and 14 degree-2 characters, whose squared degrees sum to 64=|G|.
- **Originality — PASS:** PASS, narrowly construed. Rossmann's open-problem section explicitly records the character-rank relation only for odd q via O'Brien--Voll and asks about character enumeration for general prime powers. The twisted-group-algebra mechanism itself is classical, so novelty is not claimed for projective representation theory; the new content is the observation/application that it removes the characteristic-2 restriction for graphical groups and yields the explicit all-q complete-bipartite formulas. Focused searches did not locate this application elsewhere.
- **Scientific value — PASS:** PASS. The result closes a visible parity gap in the motivating paper, gives a clean characteristic-free character formula, and converts an all-q representation-theoretic problem into a concrete alternating-matrix rank count. It does not overclaim polynomiality for arbitrary support patterns.

## Independent findings
- The central-character block decomposition works independently of Lazard/orbit-method hypotheses and is therefore valid at p=2.
- The radical condition is exactly a finite-field linear kernel condition, not merely an F_p-kernel, because the trace pairing F_q/F_p is nondegenerate.
- The twisted-group-algebra center has basis indexed by the radical and each primitive central block has dimension |A/R|, giving the common irreducible degree sqrt(|A/R|).
- Small q=2 checks for K_2 and K_3 satisfy both the predicted degree counts and the global sum-of-squares identity.

## Independent checks
- Re-proved the finite twisted-group-algebra lemma from central basis elements and semisimplicity.
- Checked the trace-pairing argument identifying the bicharacter radical with ker B_Gamma(y) in characteristic 2.
- Checked even rank for alternating matrices and the complete-bipartite block rank identity.
- Compared with Rossmann's open-access full text, whose Section 1.6 states the odd-q restriction and rank-count relation.

## Literature evidence
- https://doi.org/10.1112/blms.12665 — Rossmann (2022), open-access full text; Section 1.6 poses character enumeration and records the rank-count relation only for odd q.
- https://doi.org/10.1090/tran/6276 — O'Brien--Voll (2015), orbit-method character enumeration under the class<p regime used for the odd-characteristic statement.
- https://doi.org/10.1090/S0002-9947-1970-0264418-8 — Busby--Smith (1970), classical twisted-group-algebra representation background.

## Limitations
- The general projective-representation lemma is classical; originality is only in the characteristic-free graphical-group application and explicit corollaries.
- The formula does not prove that the support-constrained alternating rank counts are polynomial in q for arbitrary graphs.
- No modular-character theory is claimed; the audit concerns ordinary complex irreducible characters.

The assigned source tree was unchanged between inventory commit `e9ed144c13b7834896a844cc4f9cac3c25a168a6` and audited commit `253a0fe5d0217455660a277f9adb940030e567ad`; the assigned tree SHA therefore remains the exact current tree audited. GitHub was used only as read-only evidence; no repository writes were made. Audit timestamps and this audit-file date use UTC as required by the task-specific audit contract.
