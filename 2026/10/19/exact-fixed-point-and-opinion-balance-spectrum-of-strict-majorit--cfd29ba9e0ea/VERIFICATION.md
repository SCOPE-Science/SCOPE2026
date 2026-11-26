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

On a mismatched rung the rung neighbor has the wrong color, so both horizontal neighbors of each endpoint must have that endpoint's color. This propagates the same ordered mismatch through the connected cycle, giving exactly two separated states. Otherwise the rungs agree and each vertex needs only one horizontal neighbor of its own color, exactly excluding singleton cyclic runs. With k blue columns and r runs of each color, counting ordered compositions of k and n−k into parts at least two and then marking a labeled blue-run start gives the stated binomial product times n/r. This argument counts labeled words correctly even when they have rotational symmetry, since each specific word has exactly r marked starts. The separated colorings add twice at m=n regardless of parity. In synchronized words the color-change edges are an even matching of C_n and the initial color is free. The two-state cycle matching trace and parity filter at z=±1 give L_n+2cos(nπ/3), plus two separated states. This gives the stated entropy and the minimum nonzero blue counts, with six four-blue states at n=4 where both classes contribute. An independent bounded check inspected all 87,360 labeled colorings for n=3 through 8, checking neighbor agreement and comparing every mass bin; totals were 4, 8, 14, 22, 32, 48. Replay the direct check by iterating masks 0 through 2^(2n)−1, rejecting any mask with more than one differing neighbor at any vertex, and accumulating by popcount. The supplied verifier was inspected, not executed.

## originality

PASS

The general internal-partition equivalence and the no-isolated-letter condition on cyclic words are prior. The strongest inspected earlier sources do not give the all-state prism classification and its labeled mass spectrum. A later indexed record explicitly overlaps on the prism classification and exact total but not the blue-count spectrum. The pass credits the supported prism-specific result, not priority for internal cuts, the synchronized-word motif, or the Lucas calculation in isolation.

## value

PASS

The prism is a natural cubic benchmark where tie behavior disappears but the layers can still separate. The exact blue-mass spectrum answers more than a total or a positive exponential rate: it distinguishes the exceptional two separated states from all synchronized states, including their contribution at odd n, and gives the smallest self-sustaining groups. The full labeled census is useful even without basin or convergence information.

The dated certificate retains the supplied scientific assessment, sources and limitations.
