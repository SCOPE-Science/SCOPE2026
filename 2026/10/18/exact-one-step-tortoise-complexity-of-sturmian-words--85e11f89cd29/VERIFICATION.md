---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

Checked the mechanical threshold argument (RESULT.md, lines 21–52) independently. In phases 0<=t<1, the cumulative ones through j bits are floor(t+j alpha). Each j from 1 through n gives exactly one threshold ceil(j alpha)-j alpha; irrationality makes them interior and pairwise distinct. The half-open intervals give the common Sturmian language by the dense irrational orbit, and the endpoint choices of lower/upper coding give values already realized on one side. Moving through the thresholds in phase order strictly increases the input lexicographically: for j<n the change is 01 to 10 in positions j-1,j (zero-based), and for j=n only the last bit changes 0 to 1. At j<n the changed pair is erased down to its common zero exactly when the prefix preceding the pair contains no 1; then both outputs coincide, including the common appended 1. Otherwise the first 1 is removed from the common prefix and the change survives as a strict increase. A final-bit change also gives a strict increase, including the case with no earlier 1. At the threshold the prefix count equals ceil(j alpha)-1, so mergers occur exactly at the internal labels j<=floor(1/alpha). Nondecreasing image order rules out any further loss from nonadjacent collisions. Thus the stated defect is exactly min(n-1,floor(1/alpha)); n=1 has two images and the empty word has one. The proof is for frequency of 1 and one application only. The two finite factor sources and recorded five PASS lines were inspected, not executed or used to justify the universal claim.

## originality

PASS

The one-step slope-dependent exact loss is distinct from the inspected antecedent literature. The closest indexed record explicitly does cover the same one-step specialization as a mathematical statement, but is listed a week later and expressly does not claim that specialization as its own novel content; this is evidence of later coverage, not existing prior coverage of the bound Oct. 18 statement. The indexed dates are not independent proof of priority.

## value

PASS

This computes an invariant introduced for factor languages precisely where the motivating paper invites Sturmian work. It turns a bounded-loss statement into an exact slope-sensitive crossover: two images up to n=floor(1/alpha)+1, then linear growth with known deficit. Neither classical factor complexity nor a qualitative deficit bound gives that profile. It is a natural one-step benchmark independent of the later iterate extension.

The dated certificate retains the supplied scientific assessment, sources and limitations.
