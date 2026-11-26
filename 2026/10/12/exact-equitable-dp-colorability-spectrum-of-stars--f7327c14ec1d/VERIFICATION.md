---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

The original quantifies over arbitrary covers with global labels and compares with EDP, not SEDP. Fixing any center color removes at most one choice per leaf. A nonempty subset of leaves sees at least k−1 labels, whose total remaining capacity is at least m(k−1)−1, after subtracting one slot for the center. Under the criterion this is at least n−1, so cloning labels according to their residual capacities proves all Hall inequalities. Conversely the common Z_k palette and the cyclic edge map forbid one label on every leaf different from the center label. The center also uses no copy of that forbidden label, so fewer than n total slots are accessible whenever m(k−1)<n. For k=1 one matched edge suffices. This includes n=2, k=n, k>n and the stated switches at n=9. Inspected VERIFICATION.md, verify.py and its recorded output; the proof is analytic, and the bundled census is confined to plain full covers and was not replayed.

## originality

PASS

The cyclic witness and the high-palette range have documented antecedents; the complete low-palette EDP criterion for stars, including its sufficiency direction for arbitrary covers, was not covered by the strongest inspected statements.

## value

PASS

The result completely resolves a natural graph family's palette spectrum under a new quantified coloring constraint, including below the general forest guarantee. A sharp obstruction-versus-capacity criterion explains when the failure to extend across palette sizes is inherent; the n=9 switches directly separate EDP behavior from the older SEDP example. The contribution is this boundary, not a new form of Hall's theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
