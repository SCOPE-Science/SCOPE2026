---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-16.md",
      "INDEPENDENT_AUDIT_2026-10-16.json"
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

For odd q, n>=3 and 2<=m<=n-1, s=n-m, Lee–Park Proposition 3.6 directly identifies E1 matrices as shifted coefficients f,xf,...,x^(m-1)f with deg f<=s. No truncation because deg(x^(m-1)f)<=n-1. Thus U_f=f Fq[x]_<m. If f=da,g=db coprime a,b, common elements fu=gv imply u=bh,v=ah; dim intersection=max(0,m-(max(deg f,deg g)-deg d)). Distinct classes iff f,g not proportional. Ordered gcd decomposition into monic pair plus monic d yields A_t-A_(t-1)=(q+1)q^(2t-1) and N_t=(q+1)q^(2t-1)*(q^(s-t+1)-1)/(q-1), summing to L(L-1). Independent q=3,m=2,n=4 full 13-projective-word intersection enumeration gets t1=48,t2=108, distances 2,4. This is a proof for all odd prime powers, finite checks supplementary.

## originality

PASS

Best-of-knowledge statement/implication-level comparison for Exact Grassmann distance spectrum of a dihedral Toeplitz quasi-MRD family: precise new invariant not located as prior theorem; accessible direct sources and nearest indexed records compared, with explicit access and alias risks. A failed index search alone does not establish originality.

## value

PASS

A complete sharp Grassmann distance distribution for direct row spaces of a natural published family of full-rank Toeplitz quasi-MRD codes is a nontrivial geometric refinement; it tells a coding theorist exact pair-distance multiplicities, not given by rank metric parameters or identity-block lift, and is a useful precise invariant even without a new global optimum.

The dated certificate retains the supplied scientific assessment, sources and limitations.
