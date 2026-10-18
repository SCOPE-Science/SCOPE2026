---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-18.md",
      "INDEPENDENT_AUDIT_2026-10-18.json"
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

Triple-column Vandermonde-type determinants factor as pairwise differences times e1({a,b,c}) or e2({a,b,c}), so arc assumption ensures MDS. Three-dimensional GRS columns lie on a nonsingular plane conic, and conversely five or more arc points on a smooth rational conic give GRS up to monomial equivalence. Five arc points uniquely determine smooth conic (nonsmooth conic cannot contain a 5-arc; Bezout). Substituting [1:t:t³] into conic monomials gives t degrees {0,1,2,3,4,6} missing t^5, so six-point kernel iff monic vanishing polynomial has e1(T)=0; for [1:t²:t³] degrees {0,2,3,4,5,6} missing t, so iff e5(T)=0. Degree<=6 and injectivity forbid any conic for seven distinct t. The e5 extension equation e5(U)+t e4(U)=0 has at most one solution because e4,e5 cannot both vanish on 5 distinct elements (including 0), proving 5-packing. Independently modular-eliminated conic constraints for F19 S={0,...,6} r1, obtaining one qualifying T=(0,1,3,4,5,6), all 21 5-subsets, no 7, confirming published weak-boundary counterexample; all-characteristic proof symbolic.

## originality

PASS

Ning 2025/26 introduces degree-deleted GRS subcode families and MDS e_r triple tests; classical plane conic characterization of [n,3] GRS is prior. Jin-Ma-Xing-Zhou 2024 Proposition VI.1 proves non-GRS for n>2k (known >=7 obstruction). Their Proposition V.1 instead asserts non-GRS at weak n>=2k for first family; Abdukhalikov-Ding-Verma 2025 Theorem 3.2 likewise asserts weak n>=2k for related family. Original primary PDFs at explicit theorem pages were inspected: in equality case n=2k=6 the explicit F19 arc conic gives contradiction. Thus retained novelty is exact six-point boundary and optimal deletion/puncturing five-packing, not longer-length non-GRS. No prior equivalent positive six-subset criterion found in inspected relevant primary text.

## value

PASS

GRS equivalence under puncturing is a natural central coding-theory structural question. The complete sharp length-six exception, correction of overly strong published non-GRS statements, and exact deletion threshold with 5-packing constraint give nontrivial classification and practical information for code shortening/decoding, not just recomputed MDS tests.

The dated certificate retains the supplied scientific assessment, sources and limitations.
