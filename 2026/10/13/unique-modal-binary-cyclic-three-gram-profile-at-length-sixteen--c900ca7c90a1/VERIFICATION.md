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

The scoped unit is an indexed binary array, not an equivalence class of rotations. A closed de Bruijn walk with its start specified determines exactly that array. The flow relations e=b, g=d, f=c+d−b and total a+b+2c+3d+h=16 are correct. With b,d>0 the four vertices form a directed cycle in the support, and a tree to 00 must use edges 10→00 and 11→10 and one of the c+d edges from 01, giving b d(c+d). For a fixed root the labeled last-exit count is t times its outdegree times the product of (r−1)!; summing roots gives the factor 16 and dividing by multiplicity factorials forgets the copy labels, without any assumption of aperiodicity. With b=0 or d=0, the disconnected loop is excluded unless it alone is active, giving the stated reduced supports. An independent direct census of all 65536 arrays matched all 271 CSV rows, including unique 1296 at all twos and unique 1280 at (1,2,3,2,2,3,2,1); next size 1152. At length 8 the 27-profile direct census gives the unique 24 at (0,1,2,1,1,2,1,0) vs 16 at the uniform vector. Independent replay: /workspace/branches/9d35c4e4-bed7-4118-aea7-e96320845b22/direct_census.py and direct_census_n8.log / direct_census_n16.log in that directory. This exhaustive calculation proves the scoped finite statement; it gives no general-length extremal assertion.

## originality

PASS

Supported here is the unrestricted length-16 uniqueness and full comparison with the runner-up, together with the contrast to the first possible uniform length. The size of the uniform fiber and the number of possible profiles are separately covered and are not credited as distinct results. The closest comparisons do not give the unrestricted exact ranking.

## value

PASS

Lengths 8 and 16 are the first two natural uniform-coverage scales for eight cyclic triples: one of each and two of each. The precise modality switches there, refuting the uniform-at-first-coverage guess and giving a usable extremal ambiguity benchmark at the next scale. The strict gap 1296−1280 and exact runner-up certify that the second result is not a tie or merely the standard uniform count. No all-length cutoff is inferred.

The dated certificate retains the supplied scientific assessment, sources and limitations.
