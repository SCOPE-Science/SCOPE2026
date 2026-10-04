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
# Verification

Run `python3 verify.py`.

The verifier constructs \(\mathrm{PG}(2,3)\) from normalized nonzero vectors over \(\mathbb F_3^3\), obtaining \(13\) points and \(13\) four-point lines. For each of the nine base multisets \(B_s\), \(4\le s\le12\), it checks spanning rank \(3\), exact Griesmer length, distance both from maximum line multiplicity and by enumerating all \(26\) nonzero messages, and the geometric locality-\(2\) condition.

It separately checks the length-\(5\), distance-\(2\) and length-\(6\), distance-\(3\) witnesses and verifies that \(\mathbb F_3^2\) has exactly four projective one-spaces, the finite fact used to exclude a ternary \([5,3,3]\) code.

For every \(4\le d\le1000\), it then forms the claimed lifted multiset, verifies its length equals \(d+\lceil d/3\rceil+\lceil d/9\rceil\), verifies distance \(d\), and checks locality \(2\). This finite range is only a replay check. The proof for all \(d\) uses the explicit residue construction and the identity \(g_3(3,d+9)=g_3(3,d)+13\).

The verifier does not search all codes or claim an independent literature audit. The Griesmer lower bound and the standard projective locality criterion are literature premises inspected in the cited source.
