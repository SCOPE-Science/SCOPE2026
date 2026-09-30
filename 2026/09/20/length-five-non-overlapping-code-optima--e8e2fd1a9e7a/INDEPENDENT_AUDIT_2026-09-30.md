# Independent Audit — Exact size and enumeration of maximum length-five non-overlapping codes

**Audit date:** 2026-09-30 (UTC)  
**Repository:** `SCOPE-Science/SCOPE2026`  
**Assigned source tree:** `62c9260a171913144905420a87f00095cce09515`  
**Audited current source tree:** `62c9260a171913144905420a87f00095cce09515`  
**Audited repository commit:** `eff2c6312cec5b0dee5115e5f42211a853092dfb`  
**Disposition:** passed

The current `main` directory tree exactly matches the assigned source-tree SHA. GitHub was used only as read-only evidence. The dated independent-audit marker files were absent when this guarded change set was prepared.

## Correctness — PASS

PASS. Starting from the exact SQN(q,5) formulation, symmetry lets one assume a=x1>=b=y1. Writing u=x2, v=ab-u, w=x3 and z=M-w makes the objective affine in x4 and then affine in w; the endpoint reductions in the record are correct. The two branches reduce to the stated concave/monotone quadratics, and the strict normalized bounds separate every non-Blackburn pattern for q>=4, with q=7 handled separately. Equality forces x2=x3=x4=0 up to orientation, hence I^4J. The q=2,3 exceptions and the integer maximizer of l^4(q-l) follow directly. I independently brute-forced SQN(q,5) for 2<=q<=12: the maxima are 2,17,81,256,625,1296,2592,4802,8192,13122,20000, matching the theorem, and every normalized q>=4 optimum has exactly the Blackburn size pattern. Proposition 11 of the source paper then yields the stated maximum-code counts because n=5 is odd.

## Originality — PASS

PASS. Stanovnik–Moškon–Mraz’s open 2024 paper supplies the exact SQN formulation and reports computed length-five values, but explicitly says it cannot provide a simple formula for larger codeword length. Its Proposition 11 gives the counting mechanism, not an all-q optimizer. Searches across non-overlapping, cross-bifix-free, mutually uncorrelated and strong comma-free terminology found no prior unrestricted all-q formula for S(q,5) or N(q,5). A later 2026-09-21 SCOPE entry with a similar length-five title postdates this record and therefore is not prior art against it.

## Scientific value — PASS

PASS. Length five is the first case beyond the source paper’s exact length-four theorem and already has a genuine small-alphabet exception at q=3. The submitted result replaces a finite table with a complete all-alphabet formula, classifies every maximum code for q>=4, gives the unique maximizing split, and counts all maximum codes.

## Independent checks

- Read the open 2024 source at Proposition 10 (SQN), Proposition 11 (enumeration), and its explicit statement that no simple formula is available for larger codeword length; Table 1 supplies the small-q length-five values.
- Independently brute-forced SQN(q,5) for every 2<=q<=12 and reproduced the theorem’s maxima and q>=4 optimizer pattern.
- Rechecked the two symbolic objective branches and the equality conditions forcing the Blackburn k=4 pattern.
- Verified the residue-class formula for the unique integer maximizer of l^4(q-l).
- Applied the source’s Proposition 11 analytically to the forced q>=4 pattern and the q=2,3 exceptional patterns, recovering N(2,5)=8, N(3,5)=12 and N(q,5)=2 binom(q,l_q).
- Targeted later-literature searches found constrained/variable-length/generalized-overlap work but no unrestricted all-q length-five maximum theorem.
- Current main tree equals the assignment tree; the dated audit files are absent and VERIFICATION.md retains the expected blob SHA.

## Limitations

- The theorem is specific to block length five and does not settle Blackburn’s conjecture for arbitrary fixed length.
- The proof relies on the published exact SQN characterization and its enumeration Proposition 11.
- The independent brute-force audit covers q<=12; the all-q result rests on the symbolic inequalities, which were separately checked algebraically.

## Evidence and references

- https://doi.org/10.1007/s10623-023-01344-z
- https://arxiv.org/abs/2307.12593
- https://doi.org/10.1109/TIT.2015.2456634
- https://arxiv.org/abs/1303.1026
- https://github.com/SCOPE-Science/SCOPE2026/tree/eff2c6312cec5b0dee5115e5f42211a853092dfb/2026/09/20/length-five-non-overlapping-code-optima--e8e2fd1a9e7a

This guarded change set updates only the independent-audit channel. Lean verification and expert attestation remain exactly as previously recorded.
