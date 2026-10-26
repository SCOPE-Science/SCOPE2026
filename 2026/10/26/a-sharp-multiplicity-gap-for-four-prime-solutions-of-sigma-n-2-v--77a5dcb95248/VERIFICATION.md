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

# Verification of the multiplicity-five exclusion

The mathematical proof uses two kinds of exact argument: a structural congruence modulo the squared largest prime, and a finite rational inequality reduction for all other placements. The accompanying executable `verify_multiplicity_gap.py` checks every rational bound and all remaining triples, with integer and rational arithmetic only.

A successful execution reports `VERIFY_OK`, five possible leading-prime pairs, 21 enumerated third-prime cases, six integral fourth-prime candidates (all composite), and an independently enumerated finite sample through \(300000\). This finite sample does not imply the infinite theorem; the monotonic bounds and forced-fourth-prime equation do.

The known sharp witness is \(2011009=7^3\cdot11\cdot13\cdot41\), with \(\sigma=2822400\) and \(\varphi=1411200\). The classification does not address other prime support counts or total multiplicities greater than five. Independent audit has not been performed.
