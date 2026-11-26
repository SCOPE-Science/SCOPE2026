---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

With R_y(x)=2y−x, the first good identity implies commutation with R_yR_0, i.e. translation by 2y. Thus the displacement is a map δ on B=A/2A. The second identity forces 2δ=0, and conversely these displacements satisfy both good identities since −x and x represent the same quotient class and −δ=δ. Squaring gives exactly δ(c+πδ(c))=δ(c). Its quotient involution decomposes separately in each coset of π(T). On a paired class c,c′ there are exactly K common displacements lifting c′−c, no fixed points, and no dependence on other pairs. An unpaired class has K−1 nonzero displacements with no fixed points and a zero displacement fixing all h points, giving K−1+z^h. The count of labeled j-edge matchings on L classes is L!/[2^j j!(L−2j)!]; the b independent blocks give the displayed power. Multiplication by 2 implies |T|=|B|, and the 2-primary cyclic factors of order exactly 2 contribute precisely the nonzero directions in π(T). This checks the total-count dependence, the elementary-abelian example and the identity-only odd-order and trivial-group boundaries. An independent enumeration generated actual involutions on group elements by singles and pairs in equal-double fibers, then tested commutation directly using the quandle operation table. Nine groups through order 16 agreed, including Z/2⊕Z/4 (total 36), (Z/4)^2 (256), and (Z/2)^2⊕Z/4 (5776). Finite checks do not establish the general case without the bijection. The supplied replay command is python3 check.py as named in RESULT.md and VERIFICATION.md; the source docstring alone uses an outdated filename. The uploaded code was inspected, not executed.

## originality

PASS

Credit the displacement parametrization, connected cases and matching precedents to the prior literature. The supported distinct claim is the evaluated fixed-point polynomial, with exact block factorization and simultaneous treatment of arbitrary finite abelian groups, including mixed order-two and higher 2-power factors. The strongest inspected structural classification admits those groups, but does not evaluate the count or its fixed-point weights. The inspected exact enumerators either count a different subset or concern a different family; specialized overlap is not credit for the full formula. This is a bounded comparison, not a priority guarantee.

## value

PASS

This is the natural fixed-point inventory for a standard class of maps on finite abelian core quandles. It evaluates a coupled classification into a closed census rather than asking the reader to enumerate allowed displacement functions. The factors explain why the total uses only two rank parameters and why actual fixed-point degrees also use the fiber size. A researcher needing the fixed-point-free count or quick comparison of groups with equal 2-rank can extract it directly, including mixed-factor groups not covered by the cyclic or exponent-four special cases. The method is short and has precedents, but the all-group weighted invariant is not a single parameter substitution into an established enumerator.

The dated certificate retains the supplied scientific assessment, sources and limitations.
