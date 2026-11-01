---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-01.md",
      "INDEPENDENT_AUDIT_2026-11-01.json"
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

The two-update Laplacian equation L(f+g)=0 on connected loopless K_n forces complementary binary firing vectors in every nontrivial two-cycle. For a cut S of size a, exact iff threshold intervals are [n-1,n-1+(n-a)-1] for firing vertices and [n-1-a,n-2] for nonfiring vertices, giving independent lengths n-a and a. Summing labelled cuts and dividing by two proves the claimed all-mass polynomial; reciprocal exponents sum to n(2n-3) giving exact mean n²-3n/2. The entropy exponent h(u)=(1-2u)log(u/(1-u)) has sole maximum 0 at 1/2 and expansion -8(u-1/2)², so lattice Laplace gives N_n~n^n/4 and variance n/16 for cut size. Given a, the n chip counts are independent uniforms, common mass mean n²-3n/2 and total variance n[a(n-a)-1]/12; bounded increments relative to n^{3/2} justify the uniform conditional Lindeberg CLT and independent joint Gaussian. Checked the actual verify_cut_cycle.py and separately computed cut-population exact counts and conditional moments for n=2..13. These finite checks do not prove the limit.

## originality

PASS

The exact graph-cut phase-box lemma and qualitative period-two complete-graph constraints are earlier work, but none of the inspected relevant sources supplies the complete orbit-mass polynomial together with the independent two-observable central limit law. It is important to distinguish immediately periodic states from trajectories eventually reaching a period-two cycle. A looped K_n model is conjugate after a one-chip-per-vertex translation and does not by itself yield the claimed mass distribution. This is best-of-knowledge priority with an older article not fully inspected.

## value

PASS

The chip total is a conserved natural microcanonical coordinate in parallel chip-firing; the exact primitive-orbit mass generating function quantifies stationary two-cycles by every energy layer. The two-scale independent Gaussian limit captures both the population imbalance of alternating firing phases and mass fluctuations, beyond existence of a period-two window; it is an infinite family and not an arbitrary small enumeration.

The dated certificate retains the supplied scientific assessment, sources and limitations.
