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
# Verification

The analytic proof reduces the source high-energy sign condition at quarter flux to a periodic sign product and evaluates its measure by exact floor arithmetic. The critical steps are: the quarter-flux trigonometric identity; the coprime residue permutation modulo \(p+q\); the exact count \(N(x)=p+q-1-\lfloor px\rfloor-\lfloor qx\rfloor\); and the parity formula for the two half-period floor integrals.

`verify.py` performs an independent exact-rational replay. It partitions one normalized period at every zero of \(\cos(\pi(p+q)u)\), \(\sin(\pi p u)\), and \(\sin(\pi q u)\), evaluates the sign on each open interval by integer-floor parity, and sums interval lengths as `Fraction` objects. It compares the result with the closed formula for every coprime pair \(1\le p,q\le40\), and separately checks the floor-integral identity for \(1\le n\le100\).

The finite checker does not prove the infinite theorem by enumeration; it is a replay guard for the independent analytic derivation. The conclusion is a high-energy momentum-density statement. No finite-energy band-width classification and no arbitrary-flux closed form are asserted.
