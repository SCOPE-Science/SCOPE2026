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

For any 3×3 matrix with unit-modulus entries, normalize first row/column to 1. If (u-1)(t-1)=(v-1)(w-1)≠0, conjugation and unimodularity imply ut=vw and u+t=v+w, hence equal two-element multisets and a repeated row or column; zero-product cases likewise produce a proportional pair. For characters on Z3×Zp, proportional rows occur exactly when their difference has order 3 or p and the three columns lie in its annihilator coset, yielding four pure/collision configurations including transposes. Rank one needs entire selected row space to be proportional and forces complementary 3-pure/p-pure sets. Count 3-pure row triples as 3*binom(p,3), p-pure as p; p-colliding as p+9p(p-1), 3-colliding as T-p³, subtract precisely the two 3pure/p-pure overlaps. This gives N1,N2,N3 as stated for all primes. Independently enumerated every possible triple-pair incidence for p=5 and p=7: (300,13800,192925) and (1470,91728,1675702). Those finite checks do not prove complex-character rigidity for all primes; the general proof does.

## originality

PASS

Published complete analogues for even semiprime Z2p, cyclic prime-square Zp², and elementary abelian Fp² are related but not this odd squarefree cyclic Z3p family. The Fp² paper already uses the identical elementary 3×3 unit-modulus lemma, expressly excluded from novelty. The fully quantified rank multiplicities for Z3p were not identified as prior results. Broader Kronecker-product maximal rank-deficient theory could imply an equivalent enumeration but its full paper was not accessible.

## value

PASS

An exact full rank-one/rank-two/full-rank incidence census for the natural odd squarefree cyclic Fourier family, with different small-minor behaviour than even semiprime Z2p, is a motivated finite-harmonic-analysis invariant. The all-prime structural classification and multiplicity formulas are useful to interpolation/uncertainty computations; the contribution is beyond a single finite table and uses an explicit group-annihilator proof.

The dated certificate retains the supplied scientific assessment, sources and limitations.
