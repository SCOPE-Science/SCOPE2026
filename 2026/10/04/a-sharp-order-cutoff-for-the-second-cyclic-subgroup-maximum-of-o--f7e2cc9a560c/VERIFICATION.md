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
The universal extremal statement is proved from two exact inputs:
- Hall's theorem that a regular \(p\)-group has \(\Omega_1(G)=\{x:x^p=1\}\), and that nilpotency class strictly less than \(p\) implies regularity;
- the published odd-prime second-maximum theorem under \(\Omega_1(G)\ne G\), including its equality condition.

The sharpness calculation is independent of those extremal inputs. For
\[
W=C_p^p\rtimes C_p,
\]
the proof computes every \(p\)-th power and obtains the complete element-order distribution:
\[
p^{p-1}(2p-1)
\]
solutions to \(x^p=1\), including the identity, and all remaining elements of order \(p^2\). The cyclic-subgroup count follows by dividing nonidentity elements by the appropriate numbers of generators.

The packaged checker `artifacts/verify.py`:
- verifies the closed-form algebra for a range of odd primes and exponents;
- enumerates the equality example \(C_{p^2}\times C_p^{\,n-2}\) for small parameters;
- constructs \(C_p\wr C_p\) explicitly for \(p=3\) and \(p=5\);
- computes the order of every element by group multiplication;
- recovers the cyclic-subgroup count from the element-order distribution;
- checks the strict excess over \(M_{p,p+1}\).

It returns `VERIFY_OK`.

Finite enumeration is not used to prove the universal regularity or extremal assertions. No claim is made that the wreath product is extremal at order \(p^{p+1}\).
