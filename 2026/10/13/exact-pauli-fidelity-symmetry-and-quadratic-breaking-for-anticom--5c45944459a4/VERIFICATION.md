---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-18.md",
      "INDEPENDENT_AUDIT_2026-10-18.json"
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

Mutually anticommuting Pauli terms imply H^2=omega^2 I and exact exp(-itH)=cI-isH. Multiplication by U†=(I+iL)/sqrt(2) gives each paired orbit Pauli probabilities s²(a+b)²/2 and s²(b-a)²/2; difference 2s²ab. Fourier characters on the affine anti-L coset are orthogonal modulo L-pairing, so all fidelities invariant iff s*a*b=0 for every orbit, and normalized square defect is 8s^4 sum(ab)². Character parity forbids third mutually anticommuting transverse term alongside an active Q,Q* pair. Independent direct one-qubit matrix exponential, twirl, and Pauli fidelity checks matched n=1 examples including paired and unpaired errors. Exact conditions require static real amplitudes, all active transverse terms mutually anticommute, and error channel U†exp(-itH).

## originality

PASS

Best-of-knowledge exact nonperturbative iff and aggregate squared defect for this Clifford Pauli rotation, distinct from generic Pauli twirling and first-order Lindbladian symmetry; full 2026 anchor unavailable, material risk explicit.

## value

PASS

The exact boundary between harmless single transverse-axis errors and quadratic two-quadrature symmetry breaking is a motivated diagnostic for coherent gate models. Quantitative global mean-square defect and exact zero-set are more than routine formal twirling.

The dated certificate retains the supplied scientific assessment, sources and limitations.
