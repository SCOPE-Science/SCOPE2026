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

# Verification record

The proof derives conditional crossing expectations and the covariance operator analytically, then uses the previously established exact variance of the total crossing count as cited in the result. Equations for \(\operatorname{Cov}(X,I_e)\), \(\operatorname{Cov}(Q,I_e)\), the orthogonal projection, variance subtraction and Pell classification apply for every integer \(n\ge2\).

Reproduce the independent finite checks with `python verify.py` using Python 3 without third-party packages. The program exhaustively enumerates all perfect matchings through seven chords (146,598 diagrams in total), computes each crossing and squared span deficit from endpoints, checks individual-edge and length-class covariances and exact moments using fractions, and confirms three Pell-zero cases below 2,000 chords. On the prepared scientific artifact the output is `VERIFY_OK 1106 exact assertions; 3 Pell-zero pairs through n=1999`.

Finite enumeration is not a proof for arbitrary \(n\). The cited crossing-variance theorem and Pell equation's classical positive-solution parametrization are analytical inputs. The projection is optimal among additive edge indicators, not among arbitrary nonlinear functions. Orthogonality is not stochastic independence. The work has received self-review; independent audit has not been performed.
