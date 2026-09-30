# Independent Audit — corrected-riccati-linearization-and-degree-parity-criterion--87314e58dbdf

**Audit date:** 2026-09-29 (UTC)  
**Repository:** `SCOPE-Science/SCOPE2026`  
**Assigned source tree:** `447c19cd07272702497818a822918da01179cef5`  
**Audited current source tree:** `447c19cd07272702497818a822918da01179cef5`  
**Audited repository commit:** `eff2c6312cec5b0dee5115e5f42211a853092dfb`  
**Disposition:** passed

The current `main` directory tree SHA exactly matches the assignment tree SHA. No intervening source change required a stale-source re-audit.

## Correctness — PASSED

PASS. Direct symbolic differentiation of gamma=-z'/(p z) gives the corrected linear equation z''+(d-p'/p)z'-pq z=0; multiplying the Riccati residual by pz produces -d z'+pqz-z''+(p'/p)z', so the source's displayed equation is valid only when p is constant. The concrete p=q=x,d=0 example behaves as claimed. The degree-parity theorem is also correct: for a rational solution gamma~kappa x^m at infinity, gamma' cannot be the sole top-order term; under 2D<B+Q, any top cancellation involving d gamma forces the opposite inequality, leaving B+2m=Q, which requires equal parity of B and Q. Thus opposite parity excludes rational solutions and the source's rank-two irreducibility criterion applies.

## Originality — PASSED

PASS, NARROWLY. Riccati linearization and valuation-at-infinity methods are classical, and modern rational-Riccati algorithms explicitly use valuation/parity information at infinity. The defensible originality is the correction of Wu--Hong Remark 4.21 and the tailored representation-theoretic degree-parity corollary for their newly introduced modules. Searches found no public erratum/revision or earlier note making this source-specific correction. The record itself correctly disclaims novelty for the general ODE techniques.

## Scientific value — PASSED

PASS. The missing p'/p term changes the actual second-order equation whenever c21 is nonconstant, so this is a substantive correction to the computational route in a current paper. The parity criterion adds a simple closed-form irreducibility test for an infinite family and can bypass full rational-Riccati computation, while explicitly leaving inconclusive regimes to general algorithms.

## Independent checks

- symbolically rederived the corrected Riccati-to-linear substitution
- checked the p=q=x,d=0 counterexample algebra
- reproved the degree-parity leading-order case split at infinity
- confirmed general rational-Riccati tooling already uses infinity valuation/parity conditions
- verified current tree SHA and absence of 2026-09-29 audit markers

## Limitations

- The audit does not challenge Wu--Hong Theorem 4.20 itself; it corrects the auxiliary linearization in Remark 4.21.
- The degree-parity condition is sufficient, not necessary, and its valuation idea is classical prior art.
- The source preprint is very recent, so a later author revision or contemporaneous correction may supersede the source-specific novelty claim.

## Evidence and references

- https://github.com/SCOPE-Science/SCOPE2026/tree/eff2c6312cec5b0dee5115e5f42211a853092dfb/2026/09/17/corrected-riccati-linearization-and-degree-parity-criterion--87314e58dbdf
- https://arxiv.org/abs/2609.18184
- https://docs.sympy.org/latest/modules/solvers/ode.html
- https://doi.org/10.1090/gsm/122
