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

The proof has two components.

First, the analytic component proves
\[
|\Delta_L-I|\le\frac{372\pi^2}{L^2},
\]
where \(I\) is the continuous mean of the signed-minus-positive third-moment integrand. This comes from the uniform derivative estimate \(|H_\pm''|\le558\), hence \(\|D''\|_1\le2232\pi\), followed by two integrations by parts and the exact root-of-unity aliasing identity. This component is the reason finitely many computations suffice for an all-order theorem.

Second, `artifacts/verify.py` uses outward-rounded interval arithmetic to check the required numerical certificates. It verifies:

- the order-\(10000\) enclosure for \(\Delta_{10000}\);
- the inferred lower bound \(I>0.1155042646511115\);
- every order \(5\le L\le199\), with the smallest certified lower endpoint occurring at \(L=10\) and exceeding \(0.1055728090000841\);
- the tail inequality for every \(L\ge200\), whose uniform lower bound exceeds \(0.0237169437209805\);
- the four low-order signs, including the exact formulas stated in the result.

The interval code requires `mpmath==1.3.0`, recorded in `artifacts/requirements.txt`. Finite verification is not an exhaustive check of infinitely many orders; it is coupled to the proved \(L^{-2}\) tail bound. No independent audit has been performed.
