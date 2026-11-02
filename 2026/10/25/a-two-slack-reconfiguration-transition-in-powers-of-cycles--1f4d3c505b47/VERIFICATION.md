---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-29.md",
      "INDEPENDENT_AUDIT_2026-10-29.json"
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

Cyclic gap lengths d_i≥r+1 for an m-set give nonnegative slack g_i with Σg_i=s. Counting marked selected vertices and weak compositions yields m|V|=L C(m+s−1,s). For a fixed common (m−1)-subset, at most one gap allows reinsertion, because two gaps of length ≥2(r+1) contradict total length L<(m+1)(r+1); feasible positions are an interval of length ≤s+1≤3. Thus every exchange moves at distance ≤2≤r. Unit slides transfer one slack unit to an adjacent gap. With s=1 all degrees 2 and slack circulates, giving connected C_L; with s=2, one double unit gap or two single-unit gaps gives exactly four distinct moves per configuration. Slack transportation collects and rotates surplus, giving connectedness. Three pairwise exchange-adjacent maximum sets must share m−1 vertices by maximality, hence one feasible 3-point interval and one displacement-two edge; exactly L double-gap configurations supply 2L incidences/2=L such edges and L triangles. Independent brute-force adjacency/independent-set/exchange enumeration checked 27 complete small (r,m,s) configurations including components, degrees and triangles; infinite proof is the gap argument.

## originality

PASS

Prior literature gives independent-set counts, token-jumping/sliding definitions, and general equivalence of jumping/sliding for maximum independent sets. The result isolates previously unstated all-parameter s=0/1/2 transition, 4-regularity and the exact L triangle enumeration; vertex-count formula alone is elementary and not claimed as a novelty.

## value

PASS

Near-packed maximum independent sets of natural cycle powers exhibit a sharp frozen→cyclic→4-regular connected reconfiguration transition when exactly two excess sites become available. Exact triangle count measures local move redundancy and distinguishes the two-slack regime; extends directly to antiprism graphs. Motivated structural classification, not mere recounting of an independence polynomial.

The dated certificate retains the supplied scientific assessment, sources and limitations.
