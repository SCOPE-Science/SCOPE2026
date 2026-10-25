---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-23.md",
      "INDEPENDENT_AUDIT_2026-10-23.json"
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

For even n=2,4 directly compare Hamming-ball complements. For n=6,8,10,12,14, normalize first source 0, second source Hamming weight d<n, third source by its coordinate intersections, fourth by the four resulting block counts. This enumerates all automorphism orbits of ordered first-four source tuples, not a sample. Independently implemented C++ bitset enumeration for Q14 examined exactly 115600 representative classes and found per-d minima 2478,2478,1554,1554,1260,1260,1008,1008,900,900,800,800,650,650, so universal lower minimum 650; direct supplied two distinct C++ certificates and every-d saved output agree, with smaller n minima 5,16,53,185. Total later ball capacities 0,1,12,93,592 are strictly smaller than these minima. Q14 explicit (0,4095,12415,16257) attains 650, so sharpness is real. This is exact finite orbit exhaustion; it does not establish conjecture for n>=16.

## originality

PASS

Resolves exactly the prescribed finite-range cases of a named existing all-even-dimensional first-source antipodality conjecture, which was not proved by Alon’s earlier existence construction or the 2018 Conjecture 11 statement. An unlocated later full proof would dominate this special case; no such proof was established by the targeted search.

## value

PASS

A provably exhaustive finite cutoff of a specific published hypercube burning conjecture, with sharp Q14 uncovered 650 versus remaining capacity 592, is a natural substantial graph-extremal certificate; the orbit reduction justifies rather than merely empirically observes the range.

The dated certificate retains the supplied scientific assessment, sources and limitations.
