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

For the final claim in /workspace/repairs/2/RESULT.md. The frozen iff set is correct, but the unqualified Finding sentence excluding a physical dark sector at even-index roots is false if the root is zero. For n=6, k=2 gives δ=0, and the antiperiodic orbitals sin(πj/6) and sin(3πj/6) are independent eigenvectors vanishing at site 0 (energies √3 J and 0). Their wedge is a physical p=2 dark eigenvector, since its boundary sign is minus. The replacement limits the exclusion to nonzero roots, exhibits that zero-detuning boundary case, and spells out the invariance argument rather than claiming pointwise strict Lyapunov decrease. Independently, monotonicity of tr(Nρ) implies each limit state's forward orbit is supported in ker σ⁻_0; there the dissipator vanishes, and an excited component of the invariant span of the orbit's supports would give a fixed-number dark H-eigenvector. At fixed p the hop across the cut has the wedge sign (−1)^(p−1), internal hops have sign plus, and site 0 lowering is contraction. A dark eigenvector is annihilated by contractions with the whole h_q-cyclic span of e_0 by covariance of exterior powers, so it lies in the pth wedge of that span's complement even for degenerate many-body energies. The endpoint recurrence gives U_(n−2)=−q and U_(n−1)=η U_(n−2) with η=δ/J and at λ/(2J); Cassini forces U_(n−3)=0 if η≠0. At those roots η=λ/J=2cos(kπ/(n−2)) with q=(−1)^(k+1), and each fixed nonzero η gives at most one dark orbital. Only p=1 and odd k can therefore obstruct cooling away from zero. The periodic sine eigenvector separately obstructs cooling at zero for every n≥4. An independent direct-spin exact check found sector dark dimensions [0,0,0,0,0] for n=5, η=−1 and [1,0,0,0,0] for η=+1 (with an auxiliary antiperiodic orbital at −1). Replay: python3 /workspace/branches/728d4a19-01cd-4cc1-82e5-e69ab682e23e/direct_spin_n5.py. This checks dark subspaces, not the time-dependent Lindblad solution. The frozen verifier was read, not executed.

## originality

PASS

For the repaired finding, the distinguishable claim is the explicit resonance set for global trace-norm cooling of the physical periodic XX spin model, not the generic dark-state attractivity test, zero forcing, or an abstract one-body controllability criterion. The closest inspected claims have different hypotheses or do not supply the parameter classification. The repaired zero-detuning example qualifies the assertion; it is not a separate novelty claim.

## value

PASS

This gives an exact all-detuning cooling rule on the natural simplest periodic topology missed by singleton zero forcing. It explains why an auxiliary spectral resonance need not prevent physical cooling, with the exact n=5 ±J contrast and a zero-detuning limitation. The few-body argument controls all excitation sectors, a substantive improvement over merely checking one-body overlap or generic detunings.

The dated certificate retains the supplied scientific assessment, sources and limitations.
