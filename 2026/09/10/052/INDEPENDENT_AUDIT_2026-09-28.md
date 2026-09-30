# Independent Audit — 2026/09/10/052

**Audit date:** 2026-09-28 (UTC)  
**Audited tree:** `fbc76cd25e4a064649f95b3aee5bbec87c418059`  
**Disposition:** **PASSED**

## Correctness

**Verdict:** PASS

The exact-resonance arithmetic is correct. Eliminating l1 with momentum gives l2=-Σ(j^3-j)/6 and l1=-2l2-Σj, so the bounded censuses can be recomputed without the submitted code. An independent combinations-with-replacement enumeration over the stated normal-mode boxes reproduced exactly 166 canonical cubic classes, 106 satisfying the no-opposite-pair exclusion, 130 quartic classes, and 94 non-integrable quartic classes. The witnesses (-3,0;-5,4,4), (3,0;-4,-4,5), and (-1,0;-9,-5,7,8) satisfy both momentum and divisor equations exactly. A separate divisor-factor enumeration using D=L+6l2-L^3-3(j1+j2)(j2+j3)(j3+j1) found no nontrivial cubic solution with |l|_2<3 and only the four norm-3 classes stated, with max|j|=5 for l=(±3,0) and 10 for l=(0,±3). The pair-cancel family formula P=6l2-L^3+L is algebraically valid because L^3-L is divisible by 6.

## Originality

**Verdict:** PASS

Kappeler–Montalto provide the KdV stability framework, the lossy Melnikov conditions, and the motivation for momentum-preserving perturbations, but the inspected open-access paper does not give this S+={1,2} exact-resonance census or these explicit nontrivial cubic/quartic witnesses. Targeted exact-tuple and exact-count searches found no covering source. The method and cubic identities are prior art; originality is limited to the explicit certified resonance data and its application to this benchmark, not to normal forms or covering identities themselves.

## Scientific value

**Verdict:** PASS

The result has concrete value as a compact obstruction certificate for a motivated second-step KdV normal-form program: it shows that momentum conservation plus the standard pair exclusion does not remove all linear exact resonances, and it supplies minimal witnesses and replayable finite census data. The value is bounded—the analysis is only at zero amplitude and does not rule out nonlinear detuning/transversality—but the obstruction is precise enough to redirect subsequent work.

## Limitations

- Zero-amplitude divisor analysis only; no finite-amplitude detuning, measure estimate, tame remainder, or eps^-4 stability theorem is established.
- Priority checking was targeted to the exact benchmark and nearest KdV normal-form literature, not an exhaustive proof of first discovery.
- Window counts are cutoff-dependent; the cutoff-independent value lies mainly in the explicit minimal witnesses and algebraic family.

## Literature and evidence

- [Kappeler–Montalto, On the Stability of Periodic Multi-Solitons of the KdV Equation](https://pmc.ncbi.nlm.nih.gov/articles/PMC8550510/): Open-access primary source for the O(eps^-2) stability framework and Melnikov conditions; no exact S+={1,2} resonance table or submitted tuples were found in the inspected source.

- Independent integer enumeration reproduced 166/106 cubic and 130/94 quartic counts.
- Independent factor-triple enumeration established the stated norm-3 cubic minimality without a j cutoff.
- Repository RESULT.md, METADATA.json, AUDIT.json, SLOGAN.txt and VERIFICATION.md were read at the assigned tree; no GitHub writes were made.

Repository evidence was read from `SCOPE-Science/SCOPE2026`. No repository writes were made by this audit.
