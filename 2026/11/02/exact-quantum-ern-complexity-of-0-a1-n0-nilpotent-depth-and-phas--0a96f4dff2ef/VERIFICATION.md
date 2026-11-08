---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-04.md",
      "INDEPENDENT_AUDIT_2026-11-04.json"
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

On reachable-density differences V (dim_R V<=d^2-1), synchronizing iff the real channel-letter linear product vanishes. The target word yields XY^n X^a=0 in right-to-left matrix multiplication; the shorter words X^a and XY^n X^(a-1) must not vanish, so im X^a is a proper nonzero subspace of im X^(a-1). Once consecutive image ranks stabilize they never decrease, forcing at least a prior strict drops plus nonzero a-th image: dim V>=a+1, d>=ceil(sqrt(a+2)). On U=R^(a+1), X fixes e0, kills e1 and shifts e_j to e_(j-1) for j>=2; Y rotates (e0,e1) by theta=pi/(2n), fixes others. X has rank loss at most one, Y invertible; killing e0 requires at least n Y letters because cos(j theta) never vanishes for 0<=j<n. Each zero product thus needs a+1 X letters and n Y letters. At the minimal total length the only possible mixed run candidate is 0^k1^n0^(a+1-k); evaluating e_(k+1) excludes k<a, leaving exactly 0^a1^n0. Embed U in traceless Hermitian d-dimensional operators and perturb the completely depolarizing channel by small epsilon; full-rank Choi positivity ensures CPTP while an initial near-maximally-mixed state produces reachable difference span U. An independent SymPy exact exhaustive matrix check verifies unique shortest zeros for 12 (a,n) pairs; no finite extrapolation.

## originality

PASS

Lee–Lee–Kjos-Hanssen 2026 already define qc, linearization, depolarizing perturbation, qc(0^m), and qc(01^n0)=2. Those are explicitly credited; the a>=2 mixed-run optimum with n-independence and sharp a=2/3 qubit transition is not stated or mechanically implied by their broad length upper bound, which grows with n. The Lakshmanan dissertation that supplied a=1 was not independently available in full and remains a substantive priority caveat.

## value

PASS

The least quantum dimension of a prescribed unique reset word is a natural complexity invariant. This all-parameter two-run family isolates a nilpotent-depth cost decoupled from phase counting, provides an exact qubit-vs-higher-dimensional transition, and extends the previously known a=1 construction; not merely a small instance or routine parameter substitution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
