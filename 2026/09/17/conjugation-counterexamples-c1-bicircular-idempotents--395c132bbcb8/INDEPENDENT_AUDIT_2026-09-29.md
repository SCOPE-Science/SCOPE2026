# Independent Audit — conjugation-counterexamples-c1-bicircular-idempotents--395c132bbcb8

**Audit date:** 2026-09-29 (UTC)  
**Repository:** `SCOPE-Science/SCOPE2026`  
**Assigned source tree:** `f9d97c12d28ca9d55a3112ced4dce0bbb653fbc1`  
**Audited current source tree:** `f9d97c12d28ca9d55a3112ced4dce0bbb653fbc1`  
**Audited repository commit:** `eff2c6312cec5b0dee5115e5f42211a853092dfb`  
**Disposition:** passed

The current `main` directory tree SHA exactly matches the assignment tree SHA. No intervening source change required a stale-source re-audit.

## Correctness — PASSED

PASS. Under the isometry Jf=(f(0),f'), the real-linear maps Q_lambda=(C-mu I)/(lambda-mu) and Q_mu=(lambda I-C)/(lambda-mu) are complementary idempotents onto the real eigendirections of conjugation and satisfy C=lambda Q_lambda+mu Q_mu. I independently checked these identities for the nonopposite pair (lambda,mu)=(1,i). The resulting Form III and Form IV weighted sums are surjective isometries, while the explicit phase combination P1+rho P2 annihilates a nonzero function, so the families are not bi-circular. This directly contradicts the 2026 preprint's stated dichotomy for nonopposite phases. The separate phase correction beta(t)beta(phi(t))=lambda_1^2 follows algebraically from the source equations when phi^2=id and lambda_2=-lambda_1.

## Originality — PASSED

PASS, SOURCE-SPECIFIC AND WITH ACCESS LIMITATION. The public arXiv source states the global either-opposite-phases-or-bicircular dichotomy that the construction disproves. Botelho--Miura's 2019 corrigendum is highly relevant prior art because it corrects an earlier C1 GBI classification and adds omitted cases; open-access searching exposed its abstract but not the decisive full text. Institutional retrieval was attempted and revisited, but the publisher flow stopped at a human-verification requirement, so this audit does not claim to have read it. Even if that older paper contains a related conjugation mechanism, the explicit contradiction to the stated 2026 theorem for this norm and arbitrary distinct phases is a distinct source-specific correction; priority for the underlying mechanism remains qualified.

## Scientific value — PASSED

PASS. The record identifies a concrete failure of central structural theorems and the abstract-level dichotomy in a current preprint, supplies exact counterexamples for both conjugation forms, and isolates the real-linearity mechanism causing the failure. That is scientifically useful corrective work even though it is not a complete replacement classification.

## Independent checks

- verified Q_lambda^2=Q_lambda, Q_mu^2=Q_mu, Q_lambda Q_mu=0 and lambda Q_lambda+mu Q_mu=conjugation for lambda=1,mu=i
- rechecked the annihilating non-bicircular phase combination
- matched the target preprint's public abstract dichotomy
- revisited the Oxford retrieval job until it reached needs_human rather than claiming inaccessible full-text review
- verified current tree SHA and absence of 2026-09-29 audit markers

## Limitations

- The 2019 Botelho--Miura corrigendum full text was not accessible automatically: the Oxford institutional retrieval job reached a publisher human-verification gate, so only its abstract/bibliographic record was inspected.
- Originality is claimed only for the explicit source-specific 2026 correction, not for conjugation eigenspaces or real-linear idempotent techniques in general.
- A later revision of arXiv:2609.18967 could repair the statements; this audit is of v1/current record evidence.

## Evidence and references

- https://github.com/SCOPE-Science/SCOPE2026/tree/eff2c6312cec5b0dee5115e5f42211a853092dfb/2026/09/17/conjugation-counterexamples-c1-bicircular-idempotents--395c132bbcb8
- https://arxiv.org/abs/2609.18967
- https://doi.org/10.1016/j.jmaa.2019.02.032
- https://arxiv.org/abs/2607.03403
