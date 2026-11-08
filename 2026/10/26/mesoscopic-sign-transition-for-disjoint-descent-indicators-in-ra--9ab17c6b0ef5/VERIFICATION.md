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

For all n>=4, f in {0,...,n} with n-f even, and disjoint comparisons j-i>=2, the weighted Littlewood/RSK identity supplies label-independent counts of one and two forced ascents. The two-color Burnside computation gives A2=(I_nf-I_(n-2,f)+I_(n-2,f-2))/2 and 4A22=I_nf-2I_(n-2,f)+3I_(n-4,f)+2I_(n-2,f-2)-2I_(n-4,f-2)+I_(n-4,f-4). Dividing by I_nf and using exact falling-factorial ratios reproduces Cov=-(n-f)B_n(f)/(2n^2(n-3)(n-2)(n-1)^2), B_n(f)=(2n-3)f^3-nf^2+n^2f-n^2(n-2), as an independently factored sympy identity. B_n(0)<0, B_n(n-2)>0, and B_n prime has discriminant 4n^2(10-6n)<0, giving exactly one positive root; f=n is deterministic. Rescale f=cn^(2/3) to obtain n^2 Cov -> (1-2c^3)/2 and root/n^(2/3)->2^(-1/3). Independently recursively generated all involutions n=4..9 (3728 total), checked 24 conditional fixed-point classes with exact Fraction single and disjoint ascent probabilities and covariance, and verified roots numerically at n=4,6,10,50,100,1000,100000. Finite tests are corroborative only.

## originality

PASS

Best-of-knowledge priority assessment of the explicit conditional nonadjacent descent covariance sign phase and mesoscopic n^(2/3) threshold, NOT of full descent-set enumeration, fixed-point-free f=0 pair probabilities, or standard RSK/Littlewood machinery. Direct primary source comparisons show extensive prior exact encoding of the entire underlying probability law. The nontrivial extraction/factorization, all-f one-crossing statement and critical window do not appear as stated or as an explicitly worked consequence in the materially inspected primary sources. This is a qualified original derived structural classification, with substantial residual stronger-enumerator implication risk, not a priority certificate.

## value

PASS

The conditioned involution conjugacy class is a standard natural probability model, and disjoint descent correlations are a meaningful local-dependence invariant used in variance/normality analysis. The theorem identifies a complete size-uniform one-crossing positive-to-negative phase diagram and nonobvious mesoscopic scale f~n^(2/3) with explicit scaled profile; neither the sign pattern nor transition scale is visible from a fixed-positive-fraction central limit theorem. The derivation is more than a renaming, raw coefficient table, or trivial finite evaluation, even though it is an exact consequence of classical enumeration.

The dated certificate retains the supplied scientific assessment, sources and limitations.
