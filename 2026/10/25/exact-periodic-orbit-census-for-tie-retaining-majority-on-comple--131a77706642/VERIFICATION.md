---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-27.md",
      "INDEPENDENT_AUDIT_2026-10-27.json"
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

Reconstructed the Boolean synchronous rule as sigma_v(t+1)=sgn(((A+I/2)sigma(t))_v). Symmetry gives a strictly decreasing finite two-time energy whenever sigma(t+2) differs from sigma(t), so eventual periods <=2. Classifying fixed configurations by number of mixed parts leaves two unanimous states plus all-even half-filled families. On a genuine two-cycle, a part is stationary or flips homogeneously; one oscillating part is impossible, two require equal sizes and a strict middle binomial band on the stationary part, three require a uniquely strictly largest part. This yields P1=2+all-even*prod binom(n_i,n_i/2), P2=1_{unique maximum}+sum_{i<j,n_i=n_j} B(n_i,n_k), and dynamical zeta denominator (1-z)^P1(1-z^2)^P2. Independently enumerated every labelled state for the 27 size triples a,b,c=1..3 and confirmed fixed and primitive two-cycle counts.

## originality

PASS

The Goles–Olivos symmetric threshold theorem supplies the general period-at-most-two mechanism; it does not give the size-dependent exact census. Kaaser–Mallmann-Trenn–Natale arXiv:1508.03519 studies deterministic majority convergence time and Turán graph bounds but does not enumerate recurrent configurations in its inspected primary full text. Goles–Tchuente 1983 is a plausible prior treatment of generalized majority, yet only abstract/metadata were accessible and authorized full-text download returned disconnected VPN; equivalent classification there remains a material risk. Resultary complete multipartite XOR parity automata have different nonlinear update and periods up to four.

## value

PASS

The exact number of all recurrent states and primitive oscillations, not just a universal period bound, is a natural invariant of deterministic majority on labelled networks. It exhibits a sharp arithmetic symmetry transition: pairwise distinct sizes have precisely one primitive two-cycle, whereas equal-sized pairs permit entire binomial families of oscillating communities with an unchanged third part.

The dated certificate retains the supplied scientific assessment, sources and limitations.
