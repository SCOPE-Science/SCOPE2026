---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

The fixed-hole centered variance and its least-overlap-period allocation are correct. The repair distinguishes symbolic period classes from physical membership at the excluded endpoint 1: the all-(q-1) word has least period 1 and contributes nonzero limiting weight, although its half-open cylinder does not contain the corresponding endpoint. The first-occurrence decomposition gives the stated autocorrelation denominator. Its first positive pole is the unique root in the claimed band, with nonzero numerator; submultiplicativity makes the exponential rate a limit, not just a limsup. Uniform Taylor control gives Y=1/C_w(1/q)+O_q(nq^-n). At most q^r words have least period r, so their squared deviations from 1 have a uniform O_q(q^-r) tail per class. A full primitive block fits in every overlap at shifts at most n-p for fixed period p, so that class has a_q(p) phases with deviation tending to -q^-p. The summed squared expansion error and mean-centering correction are O_q(n^2 q^-n). The repair also shows the allocation denominator is positive. An independent scaled-root enumeration reproduced binary scaled variances 0.7918088529466 at n=9 and 0.8196180256213 at n=14.

## originality

PASS

The closest inspected papers provide the autocorrelation escape equation, primitive-word multiplicities and a cross-hole mean, not the limiting centered variance with its primitive-symbolic-period allocation. Known per-hole formulas make the new moments derivable with additional analysis, but an extremal or mean result alone does not fix them.

## value

PASS

In a standard fixed-hole ensemble, the mean normalized rate hides rare large deviations at short symbolic periods. The exact variance scale and nondegenerate period allocation quantify that distinction with a natural invariant and identify the classes carrying it; neither is a recomputation of an extremal rate or a small finite example.

The dated certificate retains the supplied scientific assessment, sources and limitations.
