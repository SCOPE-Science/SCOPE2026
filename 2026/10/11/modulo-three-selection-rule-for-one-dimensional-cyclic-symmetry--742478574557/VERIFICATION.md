---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-17.md",
      "INDEPENDENT_AUDIT_2026-10-17.json"
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

Fourier product cos(px)cos(qx)=1/2[cos((p+q)x)+cos((p-q)x)] restricts quadratic self-interactions of critical residue pair ±r to 0 and ±2r. A simple kernel and invariant sector decomposition put it in a unique nonzero sector. The symmetric sector is in range by the cited source Lemma 5.1; the new doubled sector is in range under the explicitly assumed index-zero Fredholm restriction and absence of another kernel. Thus the quadratic reduced coefficient vanishes unless 2r=±r mod n, equivalent for r!=0 to 3r=0 mod n. Under source Theorem 2.4’s nondegeneracy, this is the pitchfork criterion. Independently enumerated residue pairs for n=2..500; symbolic equivalence handles all n.

## originality

PASS

Published source provides n=2,3,5 examples and its n=5 invariant-sector/Fredholm method; the audited theorem gives a conditional all-n arithmetic classification. A general equivariant-character argument may imply it under equivalent assumptions, but the searched Antoneli–Dias–Matthews and accessible source abstracts did not provide a decisive full PDE-sector theorem. Best-of-knowledge with a significant older normal-form priority risk.

## value

PASS

The sharp mod-three exceptional sector is a motivated structural bifurcation-selection rule: it compresses isolated n=2,3,5 cases into a criterion for arbitrary cyclic period under explicit Fredholm hypotheses. It restricts where transcritical branches can appear but does not claim existence in exceptional cases. This is a natural whole-class obstruction rather than an arbitrary congruence experiment.

The dated certificate retains the supplied scientific assessment, sources and limitations.
