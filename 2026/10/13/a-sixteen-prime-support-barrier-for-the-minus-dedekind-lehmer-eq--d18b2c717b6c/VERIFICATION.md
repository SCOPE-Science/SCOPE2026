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

The proof was checked symbolically from the defining identity
\[
\psi(N)=N\prod_{p\mid N}\left(1+\frac1p\right).
\]

Checks performed:

- repeated prime powers are incompatible with \(\psi(N)=MN-1\) modulo that repeated prime;
- even squarefree \(N>2\) gives an even left side and odd right side;
- odd solutions force odd \(M\ge3\);
- the exact fixed-support quantity \((\prod(p_i+1)+1)/\prod p_i\) decreases in each prime variable;
- the maxima for support sizes \(1\) through \(15\) occur on the first odd primes and are all less than \(3\);
- the largest checked maximum is
\[
\frac{3746042448844705477}{1253429172199617105}<3.
\]

`verify.py` replays these rational calculations and performs a finite scan through \(10^6\). The scan is corroborative and is not used to infer the unrestricted theorem.
