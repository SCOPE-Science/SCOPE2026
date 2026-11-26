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

Two holes in one blade obstruct each other permanently: every possible sender to either sees both. With one hole in each of t blades there are binom(k,t)m^t labelled choices. With the hub seeded, t=0 succeeds, t=1 requires beta<=U, and t>=2 requires beta<=L. Without the hub, t=k cannot start; t=0 requires beta<=H; 2<=t<k requires beta<=L, which also guarantees the hub first fills. For t=1, the hub receives A=m(k-1)alpha in round one, and the last hole receives L+alpha A in round two. It received nothing in round one, and any no-fill round terminates the process, so cumulative weights do not supply an uncounted later opportunity. The hub retains its full received weight, not beta. Thus both inequalities at T=min(A,L+alpha A) are inclusive. Summing binom(k,t)m^t z^(N-t) or z^(N-1-t) over these cases gives exactly the two polynomials; L<T<=H and U<=H yield the four minimum-size regimes. For alpha=1/(4mk) the jump k-2 is realized for k>=3. The minimum-multiplicity example starts at 2^4+4*2^3=48 in the low-threshold regime; the rest follows from the one- and two-hole coefficients. The supplied exact-rational verifier was inspected, not run; its stated 337 instances do not prove the theorem. Replay: RESULT.md lines 36–56 and the case derivation here; python3 /workspace/review_evidence/bounded_checks.py reproduces the first sample multiplicity.

## originality

PASS

The supported distinction is the complete two-parameter transmission enumerator, especially the two-round, uncapped alpha-squared threshold. The ordinary low-threshold branch is demonstrably covered by a same-date heterogeneous-bouquet record; it should not be credited as a separate novel contribution, and date alone does not establish ordering. The frozen novelty assertion is for the full mixed-parameter polynomial, not the ordinary friendship-graph count. No inspected result covers that full assertion.

## value

PASS

A complete labelled enumerator on an unbounded natural block-graph family identifies a genuine two-round threshold and an unbounded k-2 change in the minimum seed size. It also locates a failure of seed-set upward closure, so ordinary forcing enumerators cannot simply be carried over. The value is in these mixed-threshold conclusions, not in recomputing the already covered ordinary branch.

The dated certificate retains the supplied scientific assessment, sources and limitations.
