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
# Verification

The central all-order check is the derivative numerator for
\[
\Lambda_\theta(q)=\frac{D_k(q)^k}{E_k(q)^k\bigl(C_k(q)-\theta D_k(q)\bigr)}.
\]
Writing \(H_\theta=C_k-\theta D_k\), direct differentiation gives
\[
N_\theta=k(D_k'E_k-D_kE_k')H_\theta-H_\theta'D_kE_k.
\]
Coefficient collection yields
\[
\frac{N_\theta}{q-1}=(1-\theta)D_kP_k+kq^{k-1}R_k,
\]
with
\[
R_k(q)=\sum_{j=0}^{k-2}(j+1)(k-1-j)q^j
\]
and
\[
P_k(q)=\sum_{i=0}^{k-2}\binom{i+3}{3}q^i+
\sum_{i=k-1}^{2k-4}\binom{2k-1-i}{3}q^i.
\]
For \(q>1\) and \(0<\theta<1\), every factor on the right is positive, establishing strict monotonicity analytically for every \(k\ge4\).

The bundled `verify.py` independently constructs \(D_k,E_k,C_k\) and their derivatives using exact integer polynomial arithmetic and checks the factorization for every \(4\le k\le200\). It also checks reciprocal invariance and representative numerical reconstructions of the original two boundary-law equations. These finite checks are corroborative only and do not substitute for the coefficientwise proof.

The claim is limited to soft-core TISGMs. No extremality, periodicity, nonperiodic-measure, or full-Gibbs-simplex statement is verified here.
