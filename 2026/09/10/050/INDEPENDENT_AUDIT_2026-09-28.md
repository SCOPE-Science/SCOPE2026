# Independent Audit — 2026-09-28

**Record:** `2026/09/10/050`  
**Title:** E1(Q) empty and U_3(Z) empty by a mod-8 obstruction  
**Repository:** `SCOPE-Science/SCOPE2026`  
**Audited tree:** `0750682798c512e0cc853b99fc5a94a939050ff2`  
**Disposition:** **PASSED**

## Independent checks

- Enumerated the complete mod-8 residue space independently.
- Verified the quartic factorization, gcd identities, sign split, and square residues by hand/Python.
- Compared the exact parameter k=3 against the cited open-access Dao results.

## Three-axis assessment

- **Correctness — PASS**: Both main claims survive independent checking. For E1, the factorization N=(12a²−5b²)(5a²−2b²), the gcd identities 5v−2u=a² and 12v−5u=b², and the mod-8 exclusion of both sign branches are valid for coprime a,b; projective boundary cases require a nonsquare rational ratio. For U_3, direct enumeration of all 8^3 residue triples gives zero solutions to the stated congruence, so U_3(Z_2) and U_3(Z) are empty.
- **Originality — PASS**: Dao’s open-access papers provide the Markoff-type K3/Brauer-Manin context but the retrieved results do not cover k=3 with this elementary mod-8 obstruction or the z=1 fibre rational-point proof. Resultary search likewise returned no earlier exact k=3 statement. This is specific new arithmetic information rather than a restatement of the cited families.
- **Scientific Value — PASS**: A local obstruction that proves integral emptiness is stronger and simpler than the proposed Brauer-sieve/height route, and the fibre’s lack of rational points prevents an ill-posed elliptic-rank computation. The result is parameter-specific but materially prunes future work on this named MK3 member.

## Findings

- Current main tree equals assigned SHA.
- Independent mod-8 enumeration found 0 solutions among 512 triples.
- The E1 coprime-factor proof and all parity/mod-8 branches were checked algebraically.
- The result does not require re-deciding smoothness, Picard rank, or the Brauer class status.

## Sources compared

- Repository record 050 RESULT.md: https://github.com/SCOPE-Science/SCOPE2026/blob/e9ed144c13b7834896a844cc4f9cac3c25a168a6/2026/09/10/050/RESULT.md — Contains the E1 and U3 emptiness proofs.
- Dao, Brauer-Manin obstruction for Wehler K3 surfaces of Markoff type: https://arxiv.org/abs/2302.11515 — Provides the F3/MK3 Brauer-Manin setting and families under different parameter hypotheses; it does not supply this k=3 mod-8 obstruction.
- Dao, Rational and integral points on Markoff-type K3 surfaces: https://arxiv.org/abs/2504.10992 — Provides later MK3 arithmetic context but studies different families and does not cover the exact E1/U3 conclusions.

## Limitations

- The audit did not independently verify the record-title adjective “smooth” or Picard-rank background because those facts are not used in the two emptiness proofs.
- The E1 proof is characteristic-zero/rational arithmetic; the U3 conclusion concerns the stated integral model.

This audit is independent of the repository’s pre-existing audit material. GitHub was read only as evidence; no repository changes were made by this audit run.
