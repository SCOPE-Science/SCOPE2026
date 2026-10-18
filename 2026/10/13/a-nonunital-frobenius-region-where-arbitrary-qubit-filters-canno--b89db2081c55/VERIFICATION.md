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

Let Psi=(N,d), a=||MN||F, s=||M||F,r=||c||2. The composed data are A=MNM,b=MNc+Md+c. Schatten Holder gives ||A||_1 <= a s, and ||b||2 <= ar+||Md||2+r. The exact source Lemma 7, applied to this qubit positive TP Psi and auxiliary M, yields ||Md||2+a<=s. Sum <=s+r+a(s+r-1)<=1 when s+r<=1; source Proposition 5 then makes the composite EB. Since Phi is not already EB, filtered index equals two; the ideal property under all left/right unitaries forces n(U Phi)=2 for each U. For GAD p=1/5,gamma=3/5, s=sqrt(11)/5, r=4/25, s+r<1 because 275<441, while p=125/625>gamma(1-gamma)(1-p)^2=96/625 so it is not EB. The critical external lemmas were inspected in Lami-Giovannetti primary full text; independent exact fractional checks reproduce the witness, without treating them as proof of the general claim.

## originality

PASS

The original Lami–Giovannetti paper defines the full filtered indices, its Prop 5 and Lemma 7 yield the tools, and its Theorem 8 asserts an index-two relationship for unital qubit channels, not this nonunital sufficient norm region. The new implication is a controlled extension using the translation norm and an actual nonunital non-EB witness. Later optical channel-amendability results concern selected unitary reordering and do not imply arbitrary CPTP-filter impossibility on this rotation-invariant region. No stronger same-region theorem appeared in targeted semantic search.

## value

PASS

Conjecture 1 in the source concerns whether arbitrary CPTP filters outperform unitary filters for qubits. A certified, genuinely nonunital parameter region for which all arbitrary filters are impossible at two uses advances that mathematical boundary beyond the unital theorem, even though it does not settle the whole conjecture.

The dated certificate retains the supplied scientific assessment, sources and limitations.
