# Independent Audit — QEACom membership is PSPACE-complete even for neutral-letter NFAs

**Audit date:** 2026-09-29 (UTC)  
**Repository:** `SCOPE-Science/SCOPE2026`  
**Assigned source tree:** `26bf6b72401810296a52f26cfca37c9ba3552015`  
**Audited current source tree:** `26bf6b72401810296a52f26cfca37c9ba3552015`  
**Audited repository commit:** `eff2c6312cec5b0dee5115e5f42211a853092dfb`  
**Disposition:** passed

The current `main` record tree is unchanged from the dispatcher-audited source tree. GitHub was used read-only as evidence; this staged change set is not claimed to be already published.

## Correctness — PASS

PASS. With a neutral letter, the stable semigroup is the whole syntactic monoid; substituting the identity for the idempotent/context variables in the EACom identities forces x^{omega+1}=x^omega and xy=yx, and the converse is immediate. A finite commutative aperiodic monoid therefore yields the truncated-Parikh characterization. For NFA input, transition matrices have polynomial-size representations; stable-membership and syntactic-equality tests from the source machinery allow polynomial-space enumeration of identity witnesses, and an idempotent power is reachable using only a matrix plus an O(|Q|^2)-bit counter. The hardness construction is sound: K_A=(Delta* minus Sigma+cd) union L(A)cd is logspace constructible, adding a looped erasing neutral letter preserves the dichotomy, and in the one-missing-word case wcd is rejected while wdc is accepted, proving noncommutativity. Thus PSPACE membership and neutral-letter PSPACE-hardness both follow.

## Originality — PASS

PASS, narrowly scoped. Göller--Manuel introduce QEACom, characterize it, prove its O(log n) circuit upper bound, and prove PSPACE-completeness for deciding constant circuit complexity from NFAs; their public 2026 statement does not give QEACom-membership complexity. The neutral-letter algebra collapse is elementary, but combining it with the source transition-semigroup machinery and special universality instances yields the QEACom-specific PSPACE-completeness theorem, including hardness under the neutral-letter restriction. Generic PSPACE results for star-freeness/aperiodicity are prior art and are not credited as new.

## Scientific value — PASS

PASS. The theorem supplies the natural decision complexity of a newly introduced pseudovariety and shows that the hardness survives a strong structural restriction where the class reduces to commutative aperiodicity. The resulting neutral-letter constant-versus-logarithmic jump also connects the algebraic classification to the source paper's circuit-complexity program.

## Independent checks

- Re-derived the neutral-letter collapse of the EACom identities and the truncated-Parikh equivalence.
- Checked that syntactic idempotents can be represented by idempotent transition-matrix powers in polynomial space.
- Checked the special-universality reduction, the regular construction of K_A without NFA complementation, and neutral-letter insertion via loops.
- Verified that wcd versus wdc witnesses noncommutativity in the missing-word case.
- Compared the claim with the 2026 QEACom source abstract and older PSPACE star-freeness/aperiodicity literature.
- Verified no assigned-path file changed between the dispatcher source-check commit and current audited main.

## Limitations

- The neutral-letter algebra collapse is elementary; originality is assigned primarily to the QEACom-membership complexity theorem and restricted hardness result.
- The audit does not claim a complexity classification for membership in all regular languages of O(log n) circuit complexity.
- The QEACom source is extremely recent, so a near-simultaneous revision or follow-up remains a residual priority risk.

## Evidence and references

- https://arxiv.org/abs/2609.18484
- https://acta.bibl.u-szeged.hu/12575/
- https://github.com/SCOPE-Science/SCOPE2026/tree/eff2c6312cec5b0dee5115e5f42211a853092dfb/2026/09/18/qeacom-membership-pspace-neutral-letter--97ba5069cc3b

This change set updates only the independent-audit channel. Lean verification and expert attestation are preserved exactly as previously recorded.
