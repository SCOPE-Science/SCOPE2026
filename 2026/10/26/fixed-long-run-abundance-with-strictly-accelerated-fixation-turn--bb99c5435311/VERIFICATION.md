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

The focal sampling difference at each group composition is the first difference of binom(k,j)binom(N-k-1,n-j), by applying Pascal in both factors. It telescopes from zero and gives a mixed-return coefficient positive at k=j and zero at k=N-1. Solving the fixation recurrence with consecutive increment ratio exp(-delta Delta_i) gives the stated denominator and the factor exp(-delta S) between endpoint fixations. Thus each coordinate increase strictly lowers the common denominator while leaving S fixed. Every interior k has some positive mixed coefficient (choose max(1,n-(N-k-1)) <= j <= min(k,n-1)); this yields the sharp unattained gap supremum mu, and the coordinatewise law gives the minimum at zero mixed returns. On the half-split family, weighted Vandermonde gives sum_j j binom(k,j)binom(N-1-k,n-j)=k binom(N-2,n-1), yielding the stated falling-factorial expression. At fixed n its bracket divided by N tends uniformly to x-x^n, maximized at n^(-1/(n-1)); replacing the exponential sum by its largest term costs at most log(N)/N in the rate. This verifies the exponent in the reduced chain, not a joint finite-mutation limit. Independent bounded replay: /workspace/branches/29341c84-3bfe-4d65-b6c2-9c7dc0866338/independent_check.py. Separate focal-payoff sums agreed with the kernel at (N,n)=(7,3),(8,4); the half-split example gave both fixations about 0.0464086. For n=3 and epsilon=c=delta=1, the normalized logarithmic rate at N=40 to 640 went from 0.30442 to 0.26179 toward 0.25660012. These are consistency checks, not the asymptotic proof.

## originality

PASS

The generic Fermi fixation formulas and terminal-payoff cancellation already imply the all-intensity stationary split; it is not the new claim. The distinct content is the nonnegative and sometimes positive mixed-return coefficient at every partial-sum level, strict coordinatewise acceleration in both directions, and the sharp range and explicit exponential separation at fixed abundance. The closest inspected sources give the terminal quantity, weak-selection schedule comparisons, or different observables, not an implication of those results.

## value

PASS

The positive cumulative kernel resolves a genuine distinction between the frequency of a homogeneous state and the rate of switching between homogeneous states. In particular, systems with exactly the same 1/2 stationary share can range from exponentially slow switching to arbitrarily near the reduced chain's upper rate mu. The conclusion is useful precisely within the specified expected-payoff Fermi model and does not identify full-chain fixation durations.

The dated certificate retains the supplied scientific assessment, sources and limitations.
