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

# Verification of repeated HED ranking reversals

Run `python3 verify.py` in the directory containing the accompanying standalone checker; no third-party packages or datasets are needed. The checker uses exact `fractions.Fraction` arithmetic throughout and returns the `VERIFY_OK` marker on success.

The checker reconstructs the complete seven-leaf tree from twelve positive rational edges, checks that all leaves have height \(4\), confirms every internal vertex is binary and every child has the stated descendant clade, and verifies both focal HED polynomials and their cubic factorization at seven rational values of \(q\). It separately enumerates every subset of the six nonfocal leaves for all seven focal choices and all seven probability values, totaling \(3136\) exact survivor-state contributions. The direct rooted phylogenetic-diversity enumeration agrees with the edge formula. Signs at \(q=1/10\), \(q=1/2\), and \(q=9/10\) alternate negative, positive, negative.

The checker also generates all unordered rooted binary shape types with two through six tips and confirms the child-clade size pairs used in the analytic lower-bound proof. Shape counts are \((1,1,2,3,6)\) for sizes two through six. This finite topology check is a supplementary sanity test: the no-double-switch theorem is established algebraically for arbitrary positive real branch lengths, not by testing finitely many numerical choices.

The general proof's decisive steps are the exact HED edge contribution, cancellation of shared root paths, the ultrametric factor \((q-1)\), and the complete lowest-common-ancestor size split argument. The root-grafting extension is algebraic and not directly enumerated. This verification does not certify originality or validate any empirical conservation inference.
