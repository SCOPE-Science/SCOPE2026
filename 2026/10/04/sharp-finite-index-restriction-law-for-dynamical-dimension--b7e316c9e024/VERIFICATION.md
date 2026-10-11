---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-05.md",
      "INDEPENDENT_AUDIT_2026-10-05.json"
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

The two inequalities follow from the actual definition. Since every \(\Gamma\)-invariant probability is \(H\)-invariant, the first inequality is immediate. For the reverse bound, averaging any \(H\)-invariant measure over a full left-coset transversal gives a \(\Gamma\)-invariant measure even when \(H\) is not normal. Refining a cover jointly over the \(m\) coset translates and iterating Meyerovitch's pointwise cover-order Lemma 2.4 gives an \(H\)-cover whose integrated order is at most \(m\) times the corresponding \(\Gamma\)-order, hence \(\dim(X,T|_H)\le m\dim(X,T)\). The empty-measure case is simultaneous by the same coset averaging. The cyclic-layer sharpness example factors through the free finite quotient \(\mathbb Z/m\mathbb Z\), so Meyerovitch's finite-group formula gives \(d/m\), while the \(m\mathbb Z\)-restriction is trivial and has dimension \(d\). Boundary cases \(m=1\), infinite dimension, and empty invariant-measure simplices are correctly separated.

## originality

PASS

Meyerovitch's paper was inspected in full at the load-bearing statements. It records a finite-index lower obstruction involving a fixed-point set, and separately the free finite-group formula, but not a comparison between an action and its restricted \(H\)-action. The audited upper inequality requires combining the source's cover-order subadditivity with coset averaging of invariant measures. Current Resultary search returned the assigned theorem as the only close same-invariant finite-index statement; the later Shi papers located in the source record remain an abstract-level overlap risk.

## value

PASS

Finite-index restriction and passage to powers are basic permanence questions for any dynamical dimension. The theorem gives a sharp universal distortion law, handles nonnormal subgroups, and identifies equality-scale examples. This is a natural structural property of a new invariant rather than a cosmetic reformulation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
