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

The proof was reconstructed directly from the truncated metric \(d_2(x,y)=\min\{d(x,y),2\}\) on the crown graph. The critical checks are:

- two completely omitted deleted matched pairs leave an unresolved same-side pair, proving \(|S|\ge n-1\);
- equality forces one omitted pair and one selected vertex from every other pair;
- under that profile, every same-side unselected pair is distinguished by a selected matched counterpart;
- an unselected cross pair \(a_i,b_j\), \(i\ne j\), fails exactly when \(S\subseteq\{a_j,b_i\}\);
- this is impossible for \(n\ge4\) because \(|S|=n-1\ge3\), while for \(n=3\) it removes exactly the mixed-side one-hole transversals.

The bundled `verify.py` constructs the graph and truncated metric from definitions, exhausts all subsets smaller than the claimed optimum, and compares every optimum-size subset with the structural classifier for \(3\le n\le9\). Expected output:

`VERIFY_OK n_range=3..9 subset_checks=141658 basis_checks=59274 bases=4086 max_order=18`

The finite computation does not establish the theorem beyond \(n=9\); the symbolic argument supplies the proof for every \(n\ge3\). No independent audit has been performed.
