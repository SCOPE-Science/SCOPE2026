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
The published coefficient formula was reconstructed with \(a=\min\{k,\ell\}\), \(b=\max\{k,\ell\}\), and \(r=b/a\). The algebraic identity
\[
\frac{B(r)}{A(r)}=\frac{2r}{r^2-1}=\frac{1}{\sinh(\log r)}
\]
was checked directly.

The transcendence step is exact: after clearing rational denominators, any nonzero rational constant in the logarithmic relation would give a positive rational number equal to \(e^Q\) for a nonzero integer \(Q\), contradicting Hermite--Lindemann. Once the constant vanishes, strict decrease of \(h(x)=x/\sinh x\) on \(x>0\) forces equality of the exponent ratios.

The accompanying script performs a high-precision finite stress test on all unordered pairs \(1\le a<b\le200\). It is not an exhaustive proof and is not used as one. No quantitative coefficient-separation bound, finite-precision reconstruction guarantee, or extension to other submodule families has been verified.
