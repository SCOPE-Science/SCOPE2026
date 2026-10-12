---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Reproducibility and limits

The defining bracket is \([x,y]=z\), \([x,z]=w\); all other independent basis brackets vanish. The claimed polynomial is derived by a complete symbolic classification of subalgebra lifts and all cross-bracket noncontainment cases. To replay finite corroboration, run `python3 verify.py` from this directory with Python 3 and no third-party dependencies.

The checker creates every reduced-row-echelon subspace of \(\mathbb F_q^4\), tests closure under the Lie bracket, and tests all ordered pairs by recomputing ranks for cross-brackets. It checks each of the fourteen oriented failure families individually. The finite fields checked were \(q=2,3,4,5,7\); the \(q=4\) implementation is the extension \(\mathbb F_2[\alpha]/(\alpha^2+\alpha+1)\), not integer arithmetic modulo four.

Actual successful output:

```
q=2 subalgebras=31 nonpermutable_ordered=328 permutable_ordered=633
q=3 subalgebras=68 nonpermutable_ordered=2538 permutable_ordered=2086
q=4 subalgebras=129 nonpermutable_ordered=11328 permutable_ordered=5313
q=5 subalgebras=220 nonpermutable_ordered=37000 permutable_ordered=11400
q=7 subalgebras=516 nonpermutable_ordered=228438 permutable_ordered=37818
VERIFY_OK
```

All checks were executed against the included standalone script in its actual package directory. Finite enumeration provides corroboration only, not a universal proof; the proof in `RESULT.md` independently covers all prime powers. No claim of independent audit or external certification is made. Historical equivalence in previously published group-lattice results remains possible.
