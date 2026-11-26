---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

For a partition-preserving inner inverse g, all points of an occupied target block must be sent to a single source block by g, so that source block's f-image must cover the entire occupied image union. Conversely choosing preimages in one such source block per occupied target defines g on the image and allows a partition-preserving extension everywhere. With the union fixed at size s, subtract the product of the numbers of non-surjections into it from all tuples of block maps into it. An onto component guarantees that this chosen set really is the union; distinct targets are independent. The multinomial allocation of m labelled source blocks to m labelled targets gives m![z^m] A_n(z)^m and exponentiating the resulting coefficients gives (3). For fixed n>=2 the normalized local weights p_k=c_n(k)/n^(nk) are positive, p_0=p_1=1, and p_2<1 (two distinct constant images). The mean of the tilted lattice law is strictly increasing because its derivative with respect to log t is the variance; its limits are zero and infinity, the latter by the unique leading e^t term. At the tilt of mean one the law has span one and positive finite variance, so the lattice local CLT and Stirling cancel the sqrt(2 pi m) factor and yield precisely 1/sqrt(v_n) times rho_n^m. The minimizing ratio B_n(t)/t is no greater than B_n(1)<e, ensuring rho_n<1. For n=1 all maps are regular, as in the full transformation monoid. The independent replay /workspace/branches/18e98930-9a7c-4913-bcb1-84179dc4aec6/independent_check_record3.py found 341 of 405 for (1,2,2) by exhaustive inner-inverse search as well as the formula, checked the first uniform weights (1,4,14,58) for n=2 and 60 for m=n=2, and reproduced rho_2=0.969592013730826. This replay is finite; the source verifier was inspected, not executed.

## originality

PASS

Credit the published regularity criterion and the exact two-equal-block enumerative overlap. The supported distinction is the arbitrary-block full-monoid census, its uniform EGF, and the fixed-block-size asymptotic with explicit saddle-point prefactor for increasing number of blocks. Neither the whole-block-surjective count nor the inspected rank enumerators at two equal blocks cover this joint statement.

## value

PASS

The exact census quantifies a natural algebraic property on the full monoid, where regularity differs materially from that in the block-surjective submonoid. The many-block asymptotic answers how strongly regularity is lost in a large random member and supplies both a strict exponential rate and its asymptotic constant, not merely a few reported counts.

The dated certificate retains the supplied scientific assessment, sources and limitations.
