---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-06.md",
      "INDEPENDENT_AUDIT_2026-10-06.json"
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

The affine change \(X=x+\beta/\alpha\) transforms the first trace equation to the second with \(\gamma'=\gamma+\operatorname{Tr}(\beta/\alpha)\), and the accompanying parameter change \(c'=c-\operatorname{Tr}(a\beta/\alpha)\) preserves codeword coordinates, proving permutation equivalence. For each nonzero \(b\), the relevant trace map in \(a\) is a surjective \(\mathbb F_p\)-linear functional with fibers of size \(p^{m-1}\), while \(c\) makes the other scalar uniform. Independently recounting the discriminant classes gives \(p-1\) zero, \((p-1)(p-2)/2\) nonzero-square, and \(p(p-1)/2\) nonsquare cases, yielding the displayed frequencies. Independent MacWilliams calculations for \((p,m)=(3,2),(5,2),(3,3)\) gave dual coefficients \((1,0,0,A_3^\perp)\) with the claimed positive formula. The four weights order with \(w_3\) minimal, and subtraction gives the claimed correction. The frozen direct GF(9)/GF(25) verifier and certificate were also read in full.

## originality

PASS

Accessible primary metadata confirms the exact code paper and its four augmented families. A detailed secondary paper assessment specifically reports that Theorems III.2 and III.5 leave the two weight distributions undetermined, while the frozen package gives the source theorem labels and table consistency. Fresh Resultary and exact-web searches found no public correction, common enumerator, affine equivalence, or dual-distance completion. The primary full text could not be obtained through open routes, and one authorized institutional retrieval returned an operational error; under the owner rule this access limitation is recorded as a residual risk rather than converted into failure.

## value

PASS

Complete weight distributions are central invariants of the source's few-weight-code program. Closing two explicit omissions simultaneously, explaining their equivalence, proving exact dual distance/projectivity, and correcting a theorem-level minimum-distance formula constitute a substantive source-specific completion rather than a single finite recomputation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
