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

The source gives the birational marked-line model as the rank-three relative quadric in \(\mathbb P(E)\) and says it is double over \(Y_4\). Locally its equation is \(d^2-4ce=0\) with two kernel coordinates, so the singular locus is the kernel \(\mathbb P^1\)-bundle of codimension two; hypersurface \(S_2\) plus \(R_1\) gives normality. The proper map is quasi-finite because a conic pencil cannot contain a projective line inside the Veronese surface of double lines, hence finite and therefore the normalization. Over reduced pairs the preimage marks one of the two lines; the explicit collision charts extend this as the blow-up of the diagonal. A fresh polynomial replay verified both quadric and blow-up-chart equations. The exceptional divisor equals the kernel bundle and is the branch divisor over the nonreduced locus \(Y_3\).

## originality

PASS

The full Hauenstein-Manivel-Szendrői text was inspected: Proposition 1.1 states that \(Y_5\) is birational to the quadric bundle, is nonnormal with singular locus \(Y_4\), and that the marked model is a double cover over \(Y_4\); it identifies \(Y_4\) with \(\operatorname{Hilb}^2\mathbb P^2\) and \(Y_3\) with the nonreduced divisor. It does not identify the marked model as the normalization, its own singular locus, or the reduced conductor preimage as the universal family. Song gives the independent general fact that the universal family for \(n=2\) is the diagonal blow-up, but does not identify the HMS preimage with it. The submitted collision charts supply that object-specific bridge. Resultary found no distinct same-object theorem.

## value

PASS

The result upgrades a published nonnormal orbit closure from a birational model to an explicit normalization/conductor picture and ties branching, collision geometry and singularities of the normalization to the universal Hilbert family. This is a coherent structural identification of the source's main orbit strata rather than a numerical invariant.

The dated certificate retains the supplied scientific assessment, sources and limitations.
