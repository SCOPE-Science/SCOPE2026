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
The symbolic proof uses
\[
c(T(\mathbb P^2\times\mathbb P^n))=(1+x)^3(1+y)^{n+1}
\]
and \(H=x+y\). The standard polar transform gives
\[
\left(\binom{n+2}{2},2n(n+1),3n^2,2(n^2-1),\binom{n+1}{2}\right).
\]
The dual determinantal codimension is \(n-1\), hence higher polar degrees vanish.

The gcd is forced by
\[
\delta_0-\delta_4=n+1
\]
and
\[
\delta_2=3n^2.
\]

The bundled checker reconstructs the first five degrees through \(n=500\) and the full zero tail through \(n=40\). These finite checks are regression evidence only.
