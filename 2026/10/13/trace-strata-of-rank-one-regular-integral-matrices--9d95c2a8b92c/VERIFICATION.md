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

The theorem was checked by reconstructing every symbolic step from the stated hypotheses. The key boundary is that \(A\) is nonzero, rank one, and von Neumann regular in \(M_2(\mathbb Z)\); the regularity premise is used only to force content \(1\), which permits the primitive Smith factorization. The trace-zero case is separated because the unique nonzero eigenspace argument used for \(t\ne0\) is unavailable there.

For \(t\ne0\), the conjugator calculation was performed explicitly and gives \(b'\equiv\pm b\pmod{|t|}\), with a constructive converse. The class count follows from the free sign action on \((\mathbb Z/n\mathbb Z)^\times\) for \(n>2\). The exact fine criterion is sourced from Corollary 5.4 of the 2016 paper and is stable under similarity. The classification of \(n\) with \(\varphi(n)\le2\) is standard and yields \(1,2,3,4,6\); trace zero is handled separately.

`verify_rank_one_fine.py` is a bounded sanity check only. It checks the conjugation formula for a finite parameter box and enumerates residue orbits through modulus \(100\). It is not used as evidence for the infinite quantifiers. Its recorded output terminates with `CHECK_OK`.

The 2026 primary PDF text was inspected for publication date, MSC, Theorem 3.2, Proposition 3.4, and Example 3.13. A page screenshot was attempted as part of PDF inspection, but the host redirected to a URL unavailable to the screenshot endpoint; the full parsed PDF text remained accessible. The 2016 primary author-hosted text was inspected at Corollary 5.4. The 2006 second-order similarity paper was identified as a high-relevance residual-risk source, but only its bibliographic page was accessible in this run.

No claim is made about independent validation or independent audit.
