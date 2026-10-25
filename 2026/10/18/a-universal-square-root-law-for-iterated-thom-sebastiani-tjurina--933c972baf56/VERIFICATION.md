---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-23.md",
      "INDEPENDENT_AUDIT_2026-10-23.json"
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

Separated-variable Jacobian quotient A_(F_r)=A_h^⊗r has dimension μ^r; multiplication by F_r is the diagonal Kronecker sum N_r of nilpotent Milnor multiplication N. Embedding each nilpotent Jordan block into an sl2 irreducible realizes N_r as diagonal raising operator. The weight character is P_h(z)^r; for irreducible highest weight j, multiplicity c_j-c_(j+2), and telescoping by parity gives dim ker N_r=c_0+c_1. Hence τ(F_r)=[z^0]P^r+[z^1]P^r exactly for r>=1. The symmetric finitely supported weight law has variance ∑ℓ(ℓ²-1)/(3μ). When N!=0 the lattice span is 1 if mixed parity or 2 if pure parity; exactly two adjacent sites together yield sqrt(2/(π σ² r)) with a relative O_h(1/r) via symmetric Fourier expansion and exponential suppression away from maximal-modulus points. N=0 gives ratio one. I independently compared Kronecker matrix kernels to character coefficient dimensions in nine exact small cases.

## originality

PASS

Best-of-knowledge original combined claim, not merely its known premises: A general tensor-multiplicity local CLT plausibly implies the leading square-root behavior, but the exact τ(F_r)=c0+c1 formula plus explicit Jordan variance are presented as a combined singularity-specific theorem; do not assert that general character theory itself is original. Broader works and residual risks below qualify priority.

## value

PASS

Exact all-iterate Tjurina numbers and sharp fixed-germ Gaussian decay constant for arbitrary nilpotent Jordan type materially refine two-factor Thom–Sebastiani formulas. The cubic Jordan variance is a natural singularity invariant necessary for the leading decay, beyond earlier square-zero examples, with no unsupported claim of new sl2 representation theory.

The dated certificate retains the supplied scientific assessment, sources and limitations.
