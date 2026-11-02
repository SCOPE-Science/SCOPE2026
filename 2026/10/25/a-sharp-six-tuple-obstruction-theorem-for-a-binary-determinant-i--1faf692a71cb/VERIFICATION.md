---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-29.md",
      "INDEPENDENT_AUDIT_2026-10-29.json"
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

Reconstructed exact two-register normal form f0,f1 in Y or absent by recolouring each x-red y fibre; all other tuples blue must have one z per y. A mixed y fibre (two distinct z values) must be covered by at least one register. Three distinct mixed fibres require two tuples each and six-tuples are minimal exactly for types L/R/C with at most one L and at most one R; independent enumeration of weights t,t,2t gives 44 t^3 per y-triple. With two mixed fibres both register assignments (a,d) and (d,a) must fail, giving four-tuple LL/RR and six-tuple L+R on one fibre plus C on the other; counts 2t² and 4t³ per unordered y pair. Zero or one mixed fibre always satisfies, unmixed fibres cannot survive minimality. Explicit six-tuple (b,c)=(2,2) shows sharpness and b=1 or c=1 trivial satisfaction. Independently implemented direct exhaustive splitting and register equivalence for (b,c)=(2,2),(3,2),(2,3), matching exact counts; universal classification follows structural argument, not finite enumeration.

## originality

PASS

Best-knowledge PASS for the sharp fixed-two-value forbidden basis and exact labelled spectrum, while unrestricted incoherence of the SAME formula is prior work. Fröhlich–Kolaitis–Meier 2026 Theorem 25 constructs arbitrarily large counterexamples using growing x alphabets and does not imply fixed-X six-bound. Barlag et al general coherence/rewritability concern unrestricted quantifiers; the specialization z=x is a different, more constrained logic. An old finite-domain database dependency decomposition theorem may imply this specialized bound, residual priority risk.

## value

PASS

The two-element determinant alphabet is a natural Boolean domain restriction of an otherwise incoherent team-semantic disjunction. A complete finite forbidden-pattern basis with sharp uniform six-tuple bound and labelled counting polynomials is a substantive structural classification and provides exact small-counterexample certificates for databases, not merely an arbitrary tiny instance.

The dated certificate retains the supplied scientific assessment, sources and limitations.
