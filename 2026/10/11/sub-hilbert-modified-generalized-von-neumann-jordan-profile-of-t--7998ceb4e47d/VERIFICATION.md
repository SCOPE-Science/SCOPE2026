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

The proof has two logically distinct parts. First, Fu–Li's ball formulation and separate convexity reduce the regular-octagon supremum exactly to extreme-point pairs for every \(p\ge1\). The bundled `verify.py` then checks the finite geometry in exact \(\mathbb Q(\sqrt2)\) arithmetic: all eight vertices have unit norm, all sixty-four ordered pairs reduce to the three shifted-norm patterns used in the proof, and the shared endpoint is \(4-2\sqrt2\).

Second, the continuum inequalities in \(p\) are analytic. Jensen convexity applied to the two unequal numbers \(1\) and \(\sqrt2-1\) proves
\[
1+(\sqrt2-1)^p\ge2^{1-p/2}
\]
for \(p\ge1\), strictly for \(p>1\). For \(1<p<2\), the strict gap from the unrestricted Yang–Wang formula is the sharp dimension-two norm comparison between \(\ell_p^2\) and \(\ell_q^2\), where \(q=p/(p-1)\). These universal steps are proved symbolically in `RESULT.md`; the checker is not used as a substitute for them.

The literature comparison used the complete 2017 unrestricted-octagon PDF and the complete 2022 Fu–Li article. The full text of the 2017 defining modified-constant article was unavailable from the lawful sources checked; its official abstract and metadata and the later Fu–Li reconstruction were used, with the residual source-access risk retained in `REVIEW.md` and `AUDIT.json`.
