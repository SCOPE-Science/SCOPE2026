---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-04.md",
      "INDEPENDENT_AUDIT_2026-11-04.json"
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

For Cerny automaton a:x->x+1 mod n and b:n-1->0 otherwise fixed, reverse preimages in a rotating frame give first appearances of n-1 missing states in forced predecessor order. For final singleton t, each successive productive inverse b needs at least n-1 inverse a advances, yielding |w| >= (n-1)^2+t. Equality t=0 gives unique palindrome U=b(a^{n-1}b)^{n-2}. One-letter slack only t=0 or1. Extensions aU,Ua, n-1 doubled-b insertions and (n-2)(n-3) valid nonforbidden interior splits are exhaustive, giving (n-2)^2+3. Independently counted exact reset target distributions by forward subset DP for n=2..7 and found shortest multiplicity 1, next counts [3,4,7,12,19,28]; unrestricted count rests on inverse-image proof, not finite checks.

## originality

PASS

Classical Černý shortest reset length (n-1)^2 and special word are prior; Szykuła–Zyzik compute shortest length algorithmically. Rodaro 2017 studies languages of factor-minimal reset words and ideals, a different invariant: second-shortest reset words need not be factor-minimal. Other published SCOPE findings count reset words in different families D_n/W_n, not this Cerny next layer. The exact all-n quadratic count and structural split classification were not located, best-of-knowledge PASS qualified by specialised word-enumeration risk.

## value

PASS

First nontrivial growth layer for a canonical extremal slowly synchronizing automaton: unique shortest word followed by exactly quadratic many at one extra symbol, plus full classification and target state. Natural exact invariant of reset-language geometry, not an arbitrary tiny-instance table.

The dated certificate retains the supplied scientific assessment, sources and limitations.
