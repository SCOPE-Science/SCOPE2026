---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-31.md",
      "INDEPENDENT_AUDIT_2026-10-31.json"
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

PASS. For n>=6 the four ±1,±2 neighbors are distinct. Direct gap analysis proves: every cyclic gap between selected vertices is 1..4; each gap of four must be flanked by two gaps of one, and this condition suffices for every outside vertex to have 0 or >=2 fort neighbors. Counting 4-to-1 incidences yields a<=b and n=3m+a-2b-c<=3m, so |F|>=ceil(n/3). Explicit gap words attain this. At minimum size, the deficit delta=3m-n equals 2b+c-a; exhaustive small-deficit patterns give all-three, one-two, one-one, two-two, and the sole alternating 1,4,1,4 n=10 anomaly. Rooted cyclic-gap word double-counting (n/m) yields counts 3, n, n(n+5)/6+5*1_{n=10}. Independent bitmask enumeration on every subset n=6..13 matched the gap biconditional and exact minimum counts; the source verifier/certificate independently extends checks to n=24 but neither proves the infinite theorem.

## originality

PASS

PASS, qualified by an inaccessible closely related circulant paper. The minimum fort size, equivalently graph spark or n minus failed zero forcing number, is a known numerical corollary and expressly not claimed new. The assessed novel object is the complete cyclic-gap structural classification of all forts and number of minimum-cardinality forts, including 5 isolated n=10 anomalies. Earlier 2024 minimal-fort paper treats inclusion-minimal forts of ordinary cycles and other graph families; generic spark/failed-forcing equivalences yield only a number. The 2025 Gomez et al. paper targets circulant failed zero forcing and might have an uninspected optimal-configuration classification; only its abstract could be inspected; authorized institutional full text request gave vpn_disconnected. This is a genuine residual priority risk, not grounds by itself to reject the statement.

## value

PASS

PASS. Minimum forts are natural obstructions to zero forcing and possible sparse null supports. Explicitly characterizing ALL forts by cyclic gaps and counting every minimum support across every cycle square is a reusable structural result and not implied by a minimum-size number. The exceptional n=10 orbit and the quadratic arithmetic phase are mathematically motivated complete classifications, not an arbitrary finite slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
