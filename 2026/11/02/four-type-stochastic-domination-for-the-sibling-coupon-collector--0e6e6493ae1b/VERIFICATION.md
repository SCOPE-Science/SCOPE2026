---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Reproducible exact checks

Place `verify_certificate.py` and `certificate.tsv` in the same directory and run:

```bash
python3 verify_certificate.py
```

Expected stdout, reproduced from the packaged source and table:

```text
CERTIFICATE_OK; positive_terms=955; min_coeff=47; uniform_middle_tail=47/144; assertions=1942
```

The verifier reconstructs equation (2) of `RESULT.md` using sparse integer-polynomial arithmetic without importing a symbolic algebra package. It confirms degree sixteen, all 955 nonzero coefficients positive, smallest coefficient 47, exact equality with all 955 file rows, and positive \(r^{14}v^2\), \(r^{14}w^2\), and \(r^{14}z^2\) coefficients. These checks are exhaustive for the four-variable polynomial, providing the rational inequality for every positive coupon vector. The one-dimensional integral in the proof is independently expanded with exact fraction arithmetic on eight positive rational probability vectors to cross-check the displayed closed tail formula; those eight examples are not treated as universal proof. The uniform mass vector is also checked exactly.

Proof limits: the stochastic-order tails outside the new middle case use Long's proved Poissonized PGF comparison and the ordinary arithmetic-geometric mean inequality. No computer experiment proves the external transform theorem or historical novelty; the supporting source and scope are identified in `RESULT.md` and `REVIEW.md`. Independent mathematical audit has not been performed.
