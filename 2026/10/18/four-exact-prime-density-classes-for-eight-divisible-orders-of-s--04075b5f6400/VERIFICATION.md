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

# Reproduction and scope

The package contains `checker.py`, an ordinary Python 3 script with no third-party dependencies. In the extracted package directory, execute `python3 checker.py`; it must terminate successfully and print `CERTIFICATE_OK`. The `certificate.txt` attachment records one verified run.

The script enumerates every subspace of \((\mathbb F_2)^3\) exactly, verifies the sixteen resulting sign-pattern fractions and the spectrum \(\{1/2,5/8,3/4,1\}\), checks squareclass relation spaces for the four example curves and the worked \(D(8)\)-model, and makes \(852\) independent direct point-order comparisons for primes up to \(1031\). All arithmetic and primality checks use exact integer operations, including integer square-root bounds. Counts are deterministic; no sampling is used.

The infinite assertion is *not* inferred from these finite tests. The proof uses (1) the order-four point/halved-two-torsion equivalence for elliptic curves with full rational two-torsion, (2) the standard two-descent criterion for halving a nonzero two-torsion point, and (3) Chebotarev equidistribution of the independent quadratic-character signs. The script certifies the finite sixteen-subspace enumeration and gives finite counterexample checks against sign mistakes; it is not a machine verification of the general algebraic input or of Chebotarev.

No external independent audit has been performed.
