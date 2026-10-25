---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-21.md",
      "INDEPENDENT_AUDIT_2026-10-21.json"
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

The integral formula follows from Lagrange inversion for U=1+zU^p. For an off-diagonal pair p!=r and every prime ell>max(p,r), Lucas gives binom(p ell+r,ell)=p mod ell, while p ell+r is invertible mod ell; hence R(ell)-R(1)=p-r mod ell, contradicting Dold divisibility for any fixed multiplier. On the diagonal p=r=s>=2, a_n=binom(s(n+1),n)/(n+1), and for odd ell>2s Lucas gives a_ell=s and a_(2ell)=s(2s-1) modulo ell. The Möbius sum at 2ell is s(s-1)/2 mod ell, a fixed nonzero residue, again impossible for a fixed multiplier. At (1,1), the constant-one sequence is realized by a singleton. Denominators used modulo ell are explicitly invertible. The finite verifier is only a spot-check of these formulas; the proof is unrestricted.

## originality

PASS

Raney numbers themselves and their combinatorial interpretations are classical. Earlier dynamics literature covers polynomial Dold sequences and specific Catalan/Motzkin/Schroder examples. The reviewed result classifies the entire positive-integer two-parameter Raney family, including the nonpolynomial diagonal obstruction; targeted Resultary search found no equivalent full classification.

## value

PASS

The theorem gives a complete natural classification for a standard two-parameter family of generalized Catalan numbers under a meaningful dynamical constraint. The diagonal case requires a distinct twice-prime Möbius obstruction, so this is not just renaming the Catalan example or a routine finite computation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
