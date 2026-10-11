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

# Reproducibility and verification

The proof is explicit in RESULT.md. The center return maps are \(g_k(c)=(c+k-1)/M\) on an opening branch and \(g_k^{-1}\) on a closing branch. At a cyclic excursion minimum, exact bracket cancellation fixes every allowed center value and leaves an original-time fiber of length \(M^{-j}\). The classical reflection formula counts paths with minimum \(-j\); dominated convergence with \(M^{-j}\), Stirling, and the exact bridge-binomial CDF establish the asymptotic and depth distributions. None of the conclusions is extrapolated from numerical data.

The package includes `verify.py`, requiring only Python 3 standard library. Run `python3 verify.py` within the extracted package. Its `verify()` exhaustively enumerates word lengths \(2m\) for \(m=1,2,3\) and branch counts \(M=2,3\). Using `fractions.Fraction`, it derives fixed-center admissible intervals, verifies exact unstable/stable periodic coordinates at test parameters \(a=1/(M+2)\), \(b=1/(M+3)\), and checks each histogram against \(M^m[\binom{2m}{m+j}-\binom{2m}{m+j+1}]\). It prints `CHECK_OK`; this test covers only those finite cases.

The full theorem requires strict interior itineraries in the two-sided smooth core; boundary conventions and primitive-period restrictions are not asserted. No external independent audit has been performed.
