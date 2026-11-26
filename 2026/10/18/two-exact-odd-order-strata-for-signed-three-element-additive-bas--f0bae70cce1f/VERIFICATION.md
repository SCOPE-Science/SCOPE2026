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

Set h=2m+1 and Y=m+1. For the constructed triple, the q copies of the largest element give an arithmetic progression of step R=2t+1, and gcd(R,Y)=1 identifies one q class per sum residue. Successive progressions have L_(q+R)−U_q=R(q−m), so the uninterrupted run in each residue ends at U_q for its representative q in [m+2,m+1+R]. The initial points are less than R, the next progression skips at least one point, and U_q increases since m−2t>0. The smallest skipped nonnegative integer is U_(m+2)+R=N−t. For the upper bound, an interval of h+2 values forces gcd(x,y)=1 and y≤h+1 (there are at most h+1 possible residues modulo y when y>h+1). In the residue ha−x mod y the middle-element multiplicity is at least y−1. Using the first and last y positions in the target interval gives the two bounds on ha and their slack d−(y−m−2)^2. Hence only j=y−m−2∈{−1,0,1} occurs for d=2,3. With r=x−1 and v=U−ha, divisibility by h imposes (1+2j)r+2v≡0 mod h. At j=0 only zero is possible and gives a=0; at j=−1, r=2v gives x=3 or (only for d=3) 5, each forbidden in its applicable regime; at j=1 the only positive multiple is h, forcing x and y both even. The small boundary m=5 meets all d=2 inequalities; d=3 is only needed at m≥29. Applying the construction with t=2 or t=3 proves the inclusive exact-h optima as stated, with no claim for 35|(k+1). For sets not representing zero, the potentially empty definition of initial length can be read as excluding them from the maximum, or assigning length −1 as in the verifier; this does not affect the extremum. Inspected VERIFICATION.md and verify.py without executing the supplied script. The latter checks finite exact sumsets and screens high-coverage candidates using the endpoint bounds; the all-order argument is independent of finite replay.

## originality

PASS

The same signed extremal problem and residue obstruction are prior work. The claim supported as distinct is the pair of exact positive-length deficits with matching constructions on the stipulated odd-order families, not the benchmark, the obstruction method, or the qualitative odd-order strict inequality. No examined source covers those strata or implies both matching bounds.

## value

PASS

This quantifies a known qualitative obstruction for a natural signed postage-stamp extremum. The deficits three and four are sharp, and the divisibility distinctions have an arithmetic cause in consecutive residue coverage and its first obstructions, not in arbitrarily selected isolated parameters. These families give exact benchmarks and a useful slack-based approach without purporting to settle the complementary stratum.

The dated certificate retains the supplied scientific assessment, sources and limitations.
