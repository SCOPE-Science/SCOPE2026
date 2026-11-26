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

Under whole-hyperedge copying, homogeneous petals stay homogeneous. With j mutant petals, a resident hub changes the petal count downward at relative rate j/m, and flips to mutant at rate srj; a mutant hub changes the count upward at rate r(m-j)/m and flips at rate s(m-j). All share the corresponding total-fitness denominator, so the harmonic equations give the geometric ratio q for the gap between the two hub-conditioned fixation probabilities. The boundaries u_0=0 and v_m=1 give v_0=H. A hub-only sequence that visits every petal provides a positive-probability path to absorption from any homogeneous configuration. For peripheral initialization the first event reaching that petal either fixes its type as mutant, with probability r/(r+s-1+1/m), and takes the chain to v_1=H(1+sm/r), or causes extinction. Averaging over the sm+1 sites proves the uniform formula. The one-petal case simplifies to r/(r+s); at neutrality q=1 and uniform fixation equals 1/(sm+1). Differentiating the finite geometric sum gives the stated weak-selection slope and the Moran-minus-sunflower difference; the numerator polynomial in the proof is −(m−1)^3 at s=1, positive for s=2, and positive for s≥3 (the only negative coefficient to check there is −m at s=3). For fixed r>1, the exact geometric-sum simplification H=(r²−1)/(r²+smr−(1+smr)q^m) yields the limit and at s=2 the relative first-order correction −1/2−1/(r+1), yielding precisely the stated coefficient. Independent full labeled chains through N=7 matched the fixation formulas within 1.3e−15 and independent differentiated chains matched the slope within 1.9e−15 in four tested cases. Replay: python3 /workspace/branches/a765d51b-25cf-4de1-88e9-d6055527ea2c/independent_sunflower_chain.py. The supplied scripts were inspected rather than executed.

## originality

PASS

The ordinary graph-star case and the update mechanism are prior; the exact arbitrary-petal-size fixation and size transition survive the comparison. The closest earlier primary paper uses the same Model 1 but a dense three-uniform star, not disjoint petals. Its weighted projection is also not equivalent. A later indexed loose-star result is an exact partial overlap at s=2, not full arbitrary-s coverage. This is a bounded originality assessment, not a priority certification.

## value

PASS

Disjoint petals isolate the effect of the broadcast group size from overlap between hyperedges. The exact formulas distinguish the location effect (which holds for every fitness) from the weak-selection and fixed-advantage comparisons; they identify a three-person threshold and a finite-size deficit at that threshold. The arbitrary-size result, including strict suppression relative to the asymptotic reference for groups of four or more, gives a useful model benchmark beyond the ordinary star and a single fixed petal size.

The dated certificate retains the supplied scientific assessment, sources and limitations.
