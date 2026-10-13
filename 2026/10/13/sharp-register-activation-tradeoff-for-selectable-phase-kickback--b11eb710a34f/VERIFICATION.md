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

The infinite theorem is verified analytically by counting allowed subsets and constructing the matching power-of-two bank.

For \(r\) bank registers and activation cap \(h\), there are only \(\sum_{j=0}^{h}\binom{r}{j}\) permitted subsets. Universal coverage of the \(2^n-1\) phase residues therefore requires that quantity to be at least \(2^n-1\). Setting \(h=r\) yields \(r\ge n\). Setting \(r=n\) shows \(h\ge n-1\). The labels \(a2^i\) attain the bound because each residue has a representative whose \(n\)-bit word is not all ones.

`artifacts/verify.py` exhaustively checks the source bank for \(2\le n\le12\), including complete residue coverage, worst-case minimum activation count, and the exact binomial inequalities. The finite check does not certify the all-\(n\) statement and is not used in place of the proof.

The scientific scope excludes repeated use of a bank element and target-dependent controlled powers. In particular, the later single-catalyst construction uses controlled \(U_f^{d'}\) and is outside the model.
