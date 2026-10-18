---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-14.md",
      "INDEPENDENT_AUDIT_2026-10-14.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

For nonzero frequency difference (a,b), factor p^j where j is its minimum truncated p-adic valuation: K_k(a,b)=p^j K_{k-j}(a',b'). At m=1 a cyclotomic coefficient polynomial has p-1 total counts and cannot vanish at the primitive pth root; for m>=2 primitive stationary-phase cancellation gives zeros exactly when a'b' is zero or a nonsquare mod p, while the two lifted stationary phases and nonzero quadratic Gauss sum prove nonvanishing for nonzero squares. Orthogonality is exactly the first unequal base-p digit compatibility relation at a depth <=k-2. Distinct siblings have distinct v-u, hence <=p children; terminal level permits <=1. Construction {(j,0):0<=j<p^(k-1)} attains p^(k-1), strictly less than phi(p^k), even when k=1. Independent exact cyclotomic checks for p,k=(3,1),(3,2),(3,3),(5,2) matched the predicted zeros on all 1440 frequency pairs; these finite checks only corroborate the proof. Inspected bundled verify_hyperbola.py and all actual source package files, never treated VERIFY_OK as universal proof.

## originality

PASS

The prime-power Kloosterman zero evaluations used in the proof are classical, and are not claimed as new. Gurak/Salié and Iosevich–Murphy–Pakianathan do not, in the specifically examined material, establish the p^(k-1) maximal orthogonal packing for this ring hyperbola together with its all-family digit-tree criterion. Resultary found nearby parabolic/cubic spectral classifications on different curves. Best-of-knowledge new structural classification; older equivalent spectral-set packing formulation remains possible.

## value

PASS

The modular hyperbola is a canonical arithmetic curve. A sharp obstruction to a full orthogonal character basis plus an all-depth if-and-only-if combinatorial classification of every partial orthogonal spectrum is useful in finite-ring Fourier frame/spectral-set questions; not merely recomputing a known Kloosterman value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
