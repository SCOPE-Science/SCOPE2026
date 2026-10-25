---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-25.md",
      "INDEPENDENT_AUDIT_2026-10-25.json"
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

For n>=17 the triangles are the quotient of the triangular lattice by L_n={(a,b):a+3b=0 (mod n)}, with H1=L_n and basis u=(-3,1),v=(n,0). The exact step norm is N=max(|a|,|b|,|a-b|). For any nonzero closed edge walk of length ell<=4, |a+3b|<=4ell<=16<n, hence a+3b=0 as an integer and (a,b)=tu. The norm N(tu)=4|t| excludes essential loops of length <4 and forces endpoints +/-u at length4. A word realizing -u in 4 steps must consist of three -e1 and one e2 step; its projections are exactly the n distinct consecutive four-cycles C_i, all primitive. For classes outside Zu, |a+3b|>=n and <=4N<=4ell, giving ell>=ceil(n/4). For n=4r+s the four explicit endpoints (r,r),(r+1,r),(r-1,r+1),(r,r+1) respectively have a+3b=n and N=ceil(n/4); monotone step words of 4s plus at most two final 1/3-steps have no repeated cyclic vertices. The conclusion is unbounded in n; bounded independent checks are corroboration only.

## originality

PASS

Best-of-knowledge PASS: the exact family is published, and general quotient-lattice classification is known, but inspected earlier primary full texts do not state or dominate the exact n-carrier bent four-edge shell plus independent min ceil(n/4). Brehm--Kühnel's shortest STRAIGHT loop normal form does not cover shortest bent essential cycles. The matching Resultary record is the same finding; the same-family flag-count and Klein-bottle systole findings have different invariants. These deductions are elementary after constructing the lattice and word norm, so historical priority remains qualified by explicit risks.

## value

PASS

The natural combinatorial edge homology systole on a published vertex-transitive torus triangulation has a complete first carrier shell and two exact independent minima for an infinite parameter family. All n shortest essential cycles lie in a single primitive direction while the next independent minimum grows ceil(n/4), yielding an explicit unbounded rank-two anisotropy ratio. The threshold n>=17 is mathematically meaningful (n=16 admits an extra independent 4-edge +4-step cycle); this is neither a finite isolated datum nor a generic graph-theory exercise, despite the elementary lattice proof. No stronger global metric or torus-optimality statement is claimed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
