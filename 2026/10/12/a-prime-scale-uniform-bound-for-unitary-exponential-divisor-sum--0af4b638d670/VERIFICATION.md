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
# Verification and scope

Run `python verify.py` with Python 3's standard library. The script recomputes both divisor-sum functions from the exact prime-power definitions for every integer \(1\le n\le100000\), tests pairwise uniqueness of the squarefree ratios in that range, and compares the equality hits with the published initial examples. The observed output is:

`VERIFY_OK limit=100000 squarefree_unique=60794 equality_hits=[1, 20, 45, 320, 6615]`

The finite check is not an exhaustive proof for larger integers. The infinite argument independently establishes squarefree injectivity by a largest-prime obstruction, decomposes arbitrary integers uniquely, and bounds rough cofactors by the published Fan–Pomerance theorem \(\Phi(X,y)<0.6X/\log y\). A unique \(d=a^2b^3\) representation supplies both the powerful-number Euler product and its reciprocal tail estimate. The bound applies uniformly to all positive real target values; it does not claim optimality, an asymptotic equality, or infinitude/finiteness of any particular fiber. No independent audit has been performed.
