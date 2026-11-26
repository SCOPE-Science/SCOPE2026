---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

The fence has only adjacent comparabilities between distinct vertices; in the sorted domain/image these can only occur between consecutive entries. Matching parity makes their directions agree, so the allowed simultaneous gap types are exactly (1,1), even/even >=2, and odd/odd >=3. An increasing injection induces the identity on any finite cyclic component, so nilpotency is exactly exclusion of fixed pairs. Removing the last pair gives the three disjoint predecessor terms and parity-prefix inclusion-exclusion gives P. There are O(n^2) states of O(n) coefficients; to obtain all output polynomials in the same O(n^3) bound, accumulate the new row and column on growing the square one step, rather than resumming every square as the supplied checker does. For defect k the omitted-position sequences a_i=d_i-i and b_i=m_i-i are nondecreasing in [0,k]. At a displacement change both sequences must increase by at least one. After exchanging domain and image if needed, the old displacement is positive: old displacement >=4 forces b_next>=5, and if it is 2, new displacement >=4 forces b_next>=5 while new displacement <=-2 forces a_next>=5. This gives the uniform translation restriction for positive rank at k<=4. Counting its domains gives the stated coefficients; the displayed example has displacements 2 then 4 and simultaneous gaps of 1 after its initial (2,4) gap, for every n>=7. Independent bounded replay: python3 /workspace/reproduction.py 4 checks induced order and literal iterates on every pair of subsets for n=1..10, verifies coefficientwise agreement with direct predecessor scans (e.g. N_7 coefficients 1,18,32,22,10,2,0,0), and finds least nonconstant defect 5 for n=7..10. Those computations corroborate, but do not prove, the infinite claims. The complexity bound is arithmetic, not bit complexity.

## originality

PASS

The membership characterization is established prior work, and the terminal-pair recurrence builds directly on it. The evidence supports a distinct fixed-point-free rank refinement together with a sharp universal failure threshold for constant displacement, not a claim of novelty for the gap characterization, enumerating the whole monoid, or classifying maximum-index nilpotents.

## value

PASS

Domain rank filters this finite inverse monoid by size of a partial bijection, while nilpotency measures eventual extinction under iteration. A full coefficient recurrence avoids exhaustive subset-pair search, but the strongest contribution is structural: omitting up to four points cannot accommodate a change in displacement, and one more omission suffices for all n>=7. It identifies a meaningful boundary and explains the three top nonzero coefficients, not just a table of small cases.

The dated certificate retains the supplied scientific assessment, sources and limitations.
