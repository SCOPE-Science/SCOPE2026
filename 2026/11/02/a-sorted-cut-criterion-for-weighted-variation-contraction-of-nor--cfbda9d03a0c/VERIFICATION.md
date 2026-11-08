---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-03.md",
      "INDEPENDENT_AUDIT_2026-11-03.json"
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

The fixed unweighted degree-normalized generator gives exact directional derivatives on right-only indicator cuts: (s/q)W-(1+2s/q)C(Y), with all such derivatives controlled by the q singleton columns (q+2)(a_j+b_j)>=W. For cuts containing u and a right set Y of size s, Phi=|d_s|B-(1+d_s)A+sum_{j in Y}tau_j(s), with d_s=1/2-s/q and tau_j(s)=(1+d_s+|d_s|)a_j-(1-d_s+|d_s|)b_j. Sorting maximizes the fixed-s derivative; taking complements exhausts the cuts. Each indicator has exact first-order Euler variation for eps<1/2; coarea of nested superlevels and triangle inequality extend contraction to all real functions and the Euler exponential limit to all t>=0. Any positive derivative yields small-t violation. Independently evaluated direct cut derivatives and the sorting test for 85 positive integer weight profiles with 1<=q<=5. For q=3, (a,b)=((4,1,1),(1,8,8)) has all singleton derivatives negative but Phi({u,y1})=1/6 and J=3. Finite checks corroborate, not prove the infinite classification.

## originality

PASS

Known coarea and graph-heat gradient bounds do not provide the all-weights normalized heat K_{2,q} sorted classification or first mixed-cut obstruction; no equivalent published indexed result was located. This remains a best-knowledge originality assessment.

## value

PASS

The family K_{2,q} transitions at q=3 from path/cycle to a genuine multicycle graph. Exact arbitrarily anisotropic variation-weight criteria and the first mixed-cut obstruction identify a natural failure of local certificates. The sorted test avoids enumerating exponentially many cuts; its q² log q complexity and constructive counterexample are mathematical structural information, not a trivial instance of coarea.

The dated certificate retains the supplied scientific assessment, sources and limitations.
