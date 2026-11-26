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

The effective time A increases at unit speed and jumps to its value at the sampled past time. Its distribution is input-independent, giving a random-unitary CPTP map at every fixed time. For the coherence f the jump compensator gives f'=−(r+iω)f+(r/t)∫₀ᵗf(s)ds with f(0)=1; its regular solution has the stated Kummer parameters. The chosen state difference has eigenvalues ±|f|, so its trace distance is |f|. An independent exact rational reproduction verified 17/10000<|S₃|²<18/10000 and 119/10000<|S₄|²<120/10000 for the 80-term sums, with the claimed margins beyond the 1/20 and 1/10 thresholds. The tail bound follows from |a|<1, |z|<11 and the ratio bound 11/81 after the first omitted term; the verified bound is below 10⁻¹⁰. The strict revival contradicts trace-distance contractivity under positive trace-preserving maps, without requiring invertibility. Since 0≤rA_(u/r)≤u, the change in the two endpoint moduli across ratios is at most 7|Δh|, leaving >3/200 throughout the band. Any pair of eigenstates with the given gap isolates the same coherence, regardless of other levels. Replay: python3 /workspace/branches/5096d329-af1e-4b98-bc22-b92a792f594c/recheck_witness.py. The supplied check_backflow_exact.py was inspected, not executed. This is a sufficient spectral band, not a classification of all ratios or a computation of the optimized backflow measure.

## originality

PASS

Credit the established history-reset model and Kummer solution and the established trace-distance criterion. The supported distinct finding is a certified strict modulus revival under constant positive hazard, with an explicit lower bound and uniform spectral window. A rotating coherence phase or oscillatory polarization is not a revival of its modulus. Later closely related certificates are distinguished by their statements, not by title or date alone.

## value

PASS

The main result is an operational counterexample, not a reevaluation of a special function for its own sake. It distinguishes a constant positive physical event rate and CPTP snapshots from positive divisibility, with a finite robustness margin against changing the gap. The uniform statement makes the witness usable in a multilevel Hamiltonian without checking its full spectrum or solving any intermediate map.

The dated certificate retains the supplied scientific assessment, sources and limitations.
