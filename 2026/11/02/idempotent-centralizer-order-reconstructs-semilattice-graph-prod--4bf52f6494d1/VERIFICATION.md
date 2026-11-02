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

# Reproduction and limits

`verify.py` is a standalone Python 3 program requiring no third-party packages. Execute `python3 verify.py` from a directory containing the script. Its successful output is `VERIFY_OK: 75 graphs; 10971 normal forms inspected`.

It inspects every finite simple graph of order one, two, three or four (75 labelled graphs altogether). It generates all generator words up to length six for orders at most three, and up to length five for order four; after normalizing by commuting and idempotence relations, 10,971 element representations are tested in total across those graphs. Each normalized word is checked for (i) whether it is idempotent exactly when its support is a clique, (ii) whether it is central exactly when its support consists of universal vertices, (iii) whether centralizing an idempotent is equivalent to centralizing each of its vertex factors, and (iv) whether it lies in the specified support-indexed sandwich piece. Additionally every ordered pair of clique idempotents is checked against the proposed exact inclusion criterion; all required strict-noncontainment witnesses are constructed explicitly.

This computation is finite, not a certificate for the infinitely many graphs or infinitely many elements. The unrestricted claim is based on the proof in RESULT.md. The claimed literature distinction concerns inverse reconstruction, not the previously studied general problem of finding centralizers in graph products of semigroups. Independent scientific audit and exhaustive publication-priority checking have not been performed.
