---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

Integration by parts with continuous flux f'/s and the killed/reflecting boundary conditions makes the generator symmetric in m dx; the divergence coefficients are bounded and bounded away from zero. Integrating the first two killed moment equations gives u'=sM and, by reversing the integral for w'−2uu', v'=2sK for M=∫_x^1 m and K=∫_x^1 sM². At layer boundaries u,v and their scaled fluxes are continuous, not in general u',v'; the wording 'join continuously' in the proof should be understood for the matched moment functions/fluxes. The Green integral bounds the mean uniformly; the strong Markov property then gives a geometric tail on a sufficiently coarse time grid, justifying the Laplace expansion through order two. Renewal gives J=u²−w/2=(u²−v)/2. Exact rational integration independently recovered all three layer polynomials and the four alternating rational witnesses. In the first layer the cubic factor rises from a negative value to its sole in-layer maximum, then decreases to a positive value, so its one zero is simple. The middle polynomial is strictly decreasing; e.g. F''=4s²M²−2smu<0 there and F'(1/3+) is already −1/1536. The last derivative has one interior sign switch, from negative to positive, and the layer values are negative at 2/3 and positive at 1, so the one zero is simple. Neither interface is a zero, and 0 is excluded. Bounded positive L¹ smoothing gives uniform moment convergence; smoothings equal to the constants near the three simple zeros can be chosen, giving local derivative convergence there as well and preserving a simple crossing in each neighborhood. The claim of at least three smooth-model sign changes is therefore valid.

## originality

PASS

Weak-rate expansion in terms of hitting-time moments and spatially heterogeneous sign diagrams are prior. The surviving distinct contribution is the fully explicit reversible absorbing–reflecting scale–speed construction with exactly three simple crossings of the mean-response derivative, and existence of its smoothly robust analogue. The strongest inspected analyses do not state or force this exact reversal count. This is a bounded assessment, not a claim of first historical discovery of nonmonotone resetting response.

## value

PASS

An exact multiple-reversal example distinguishes this problem from a single crossover in spatial reset benefit. It gives a simple, reproducible counterexample under uniform ellipticity and reversibility, with one threshold in each layer and two disconnected regions of infinitesimal benefit. Smooth robustness shows the phenomenon is not an artifact of jump interfaces in scale or speed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
