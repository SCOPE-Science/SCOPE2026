---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-07.md",
      "INDEPENDENT_AUDIT_2026-11-07.json"
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

For 0<p<=1, k>=2, 1/2<=r<=1, Cuth–Raunig Theorem 2.2 gives the p-th free norm as a minimum over rooted spanning trees of edge-length^p times signed descendant mass^p. Nonnegative charges make reattaching the zero-charge center c to root o cost-nonincreasing, and reattaching all leaves beneath other leaves to their parents is cost-nonincreasing since the new edge length is <=1 and intermediate carried mass decreases. Every tree thus reduces to a two-level root-center star, giving min_S[Σ_{i not in S}a_i^p+r^p(Σ_{i in S}a_i^p+(Σ_{i in S}a_i)^p)]. For S size m, subadditive power-mean gives (Σ_S a_i)^p>=m^(p-1) Σ_S a_i^p>=k^(p-1) Σ_S a_i^p. The lower bound min(1,r^p(1+k^(p-1)))Σa_i^p is attained by a singleton or all equal coefficients, so cone inverse distortion is max(1,1/(r(1+k^(p-1))^(1/p))). Checked metric range and p=1 boundary. Independently enumerated all 5^3=125 rooted tree candidates for k=3 and compared 27 (p,r,charge-vector) cases, all agree. Signed vectors are explicitly outside claim.

## originality

PASS

Cúth–Raunig (arXiv:2311.02920) Theorem 2.2 supplies the general tree variational formula and Theorem 2.8 discusses the positive cone; neither inspected theorem states the exact two-level central extension or the k,r,p threshold. Resultary's 2026-10-11 one-point p-Banach extension constant addresses optimizing a Lipschitz extension, not this canonical free-p embedding inverse restricted to the nonnegative Dirac cone; a shared star geometry is not mathematical implication. The three-point inclusion constant cannot dominate arbitrary k. Best-of-knowledge separate exact specialization with a required structural tree reduction; general algorithm alone does not give the sharp closed form.

## value

PASS

For p<1 inclusions of Lipschitz-free p-spaces need not be isometric. The positive cone is a geometrically natural subcone, and computing its exact distortion as a function of leaf count, exponent, and new-point distance identifies a sharp onset of nonisometry and the large-k limit 1/r. The restriction to positive coefficients is essential and stated; no full inverse-norm claim is made.

The dated certificate retains the supplied scientific assessment, sources and limitations.
