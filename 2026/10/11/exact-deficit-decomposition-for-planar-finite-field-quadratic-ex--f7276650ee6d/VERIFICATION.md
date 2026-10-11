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

The universal proof is the algebraic argument in `RESULT.md`.

The critical exact identities are
\[
W(f)=2T^2-\sum_i t_i^2-2\sum_i r_i^2+4\left|\sum_i z_i\right|^2
\]
and
\[
\begin{aligned}
\left(3-\frac3M\right)T^2-W(f)
&=\frac32\left(\sum_i t_i^2-\frac{T^2}{m}\right)
+\frac12\sum_i(u_i-v_i)^2\\
&\quad+2\sum_{i<k}(t_it_k-4r_ir_k)
+4\left(\left(\sum_i r_i\right)^2-\left|\sum_i z_i\right|^2\right).
\end{aligned}
\]

`verify.py` independently enumerates pair-sum fibers for split and anisotropic representative conics over the prime fields of orders \(3,5,7,11,13,17,19,23,29,31\). It then evaluates the fourth moment directly and compares it to the decomposition using deterministic nonconstant Gaussian-integer weights and exact rational arithmetic.

Successful replay output from the packaged file:

`VERIFY_OK primes=10 conics=20 pair_fibers=3384 energy_checks=20`

The replay checks prime-field representatives only. It is corroborative, not an exhaustive proof over all odd prime powers. The proof uses only finite-field linear algebra, the quadratic-line intersection bound, and character orthogonality, so it covers every odd prime power under the stated hypotheses.
