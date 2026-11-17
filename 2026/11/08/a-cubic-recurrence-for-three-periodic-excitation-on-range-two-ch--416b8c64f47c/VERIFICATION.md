---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-09.md",
      "INDEPENDENT_AUDIT_2026-11-09.json"
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

For connected P_n² any F³-periodic nontrivial initial state has all vertices advancing at every time; otherwise a resting neighbor would encounter an excited cycling vertex. Hence colors c_i mod3 must have a successor-color neighbor within distance 2, and that is sufficient for true minimal period three. Four-site transfer left/right boundary vectors and 81×81 transition matrix are explicit. Independently rebuilt them and verified the polynomial vector identity (M³−3M²+2M−2I)r=0 for all 81 states, as well as direct transfer counts N3..N12=(6,18,42,102,258,654,1650,4158,10482,26430). It entails Nn=3Nn−1−2Nn−2+2Nn−3 for n≥7 plus separately checked n6=102, giving genfun 6/(1−3z+2z²−2z³); positive simple dominant root 2.521379… controls growth. Inspected verify_transfer.py and direct simulation verifier. Finite certificate establishes the identity on 81 states exactly, not extrapolation from finite n.

## originality

PASS

Fisch–Gravner 1995 studied one-dimensional GH stable periodic patterns for arbitrary interaction range, and the successor-neighbor eligibility condition is classical; it does not state this exact free-boundary P_n² all-length enumeration. Published exact counts for two-row ladders, triangle-cactus chains and other graph classes are not graph/parameter equivalents. No prior explicit cubic rational primitive-three census found.

## value

PASS

The complete sequence and low-order recurrence for a natural finite-range excitable path model give an exact finite-size population and growth constant, a motivated classification inaccessible from mere existence criteria. The 81-state transfer unexpectedly collapses to a cubic cyclic relation. Restricted to initial three-periodic states, not other periods or basins.

The dated certificate retains the supplied scientific assessment, sources and limitations.
