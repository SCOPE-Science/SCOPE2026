---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-07.md",
      "INDEPENDENT_AUDIT_2026-11-07.json"
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

For all N>=3, nonempty S and strictly positive loss rates, diagonalize the uniform Peierls-cycle Hamiltonian with E_k=2J cos((2pi k+phi)/N). Away from 0/pi all eigenvalues are simple and plane waves cannot vanish on sinks. At ell*pi degenerate Fourier pairs k<- >-k-ell yield anchor-node vector; every remaining sink is nodal iff M=N/gcd(N,s-s0 for s in S) divides 2k+ell. Exactly G*gcd(2,M) solutions exist if gcd(2,M)|ell; remove fixed points of the involution (gcd(2,N) if it divides ell), divide by two. This proves the displayed dark dimension including all odd/even boundary cases. A=-iH-Gamma/2 has imaginary spectrum exactly on the reducing dark subspace and all complementary eigenvalues have negative real part, so limiting no-jump survival is the squared orthogonal dark projection, independent of positive loss strengths. For even N and a single site sink 0, at half flux the antipode belongs entirely to dark subspace and has survival one at every time, while at 0 flux it is dark-orthogonal. The modular-sink result and exact parity are the nontrivial steps; separate checks corroborate them, finite data are not a general proof.

## originality

PASS

Best-of-knowledge originality assessment limited to specific evaluated statements after Resultary, inspected primary sources and same-Git records; not historical priority certification.

## value

PASS

The arbitrary-sink flux-dependent exact formula and parity bifurcation answer a natural transport/control question in dissipative cycle networks; perfect lossless antipodal protection for all times is a sharp parameter-independent boundary phenomenon. This is more than rephrasing the known zero-flux nodal count because half-flux can create or remove all dark modes.

The dated certificate retains the supplied scientific assessment, sources and limitations.
