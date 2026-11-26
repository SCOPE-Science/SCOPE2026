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

An adjacent prescribed pair forces crossing diagonals for n≥5. A cyclically independent S cuts off |S| distinct triangular faces and leaves a convex (n−|S|)-gon of at least three vertices; gluing back the prescribed ears is the inverse even when new ears appear in the smaller polygon. Thus all inclusion moments, and by Boolean inversion the law, follow. The covariance is (p−q)I−qH+(q−p²)J with H cycle adjacency. The constant mode agrees with Var(total ears)/n; the other modes are obtained by annihilating J. The minimum nonconstant mode is positive by p−3q≥0 for n≥8, with strict positivity contributed by 1−cos; for n=5,6,7 the maximal nonconstant cosine is <1/2, =1/2, and <9/10 respectively and the exact Catalan ratios give the claimed signs. Only the constant mode at n=5 vanishes. A fixed nonadjacent set has limiting inclusion moment 4^(−|S|); consecutive 01 patterns conflict and nonconsecutive ones use disjoint pairs of bits, so all finite-block moments match. An independent enumeration of noncrossing diagonal sets (not the supplied root recursion) checked all 480 inclusions and Fourier spectra for n=5 through 8; replay: OPENBLAS_NUM_THREADS=1 python /workspace/independent_checks.py (NumPy and SciPy). These checks are finite corroboration, not a general proof.

## originality

PASS

The total-ear law and constant covariance mode are prior results. The distinct claim supported by the comparison is the labeled site law together with the finite all-mode spectrum/rank and identified finite-block limit. The strongest indexed spectrum overlap is a later-dated Resultary record; it is explicitly credited as equivalent second-order coverage there, not treated as earlier priority evidence. This assessment is bounded by inspected material.

## value

PASS

The labeled field rather than the total count is a natural observable: its spectrum controls the variance of every weighted position statistic and identifies an exact rank transition, i.e. the disappearance of deterministic linear constraints beyond the pentagon. The explicit limiting process describes complete fixed-window laws rather than just pair decorrelation. The credited total-ear moments and standard Catalan methods are not the proposed value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
