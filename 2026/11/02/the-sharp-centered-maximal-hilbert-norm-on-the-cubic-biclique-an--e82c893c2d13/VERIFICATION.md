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

# Reproducible verification

Run `python3 verify_k33.py` from the directory containing this file. It needs Python 3 only (the standard-library `fractions` and `itertools` modules).

The checker constructs the exact three centered balls for each of six vertices, enumerates all \(3^6=729\) row selections, and reduces them by within-class permutation and class interchange to exactly 55 canonical types. It independently verifies each of the 727 nonexceptional raw choices and all 54 nonexceptional representatives by exact rational Sylvester positive-definiteness tests on \(39I/25-A^{\mathsf T}A\). The two remaining raw choices are exchanged-class versions of one exceptional canonical representative.

The six smallest leading principal minors over the 54 strict types, in order of principal-submatrix size, are

\[
\left(\frac{1141}{3600},\frac{1631}{22500},\frac{2989}{93750},\frac{12691}{390625},\frac{357749}{9765625},\frac{7529536}{244140625}\right).
\]

The exceptional two-class-constant action has Gram matrix \(\frac1{16}\begin{psmallmatrix}1&3\\3&25\end{psmallmatrix}\), with characteristic equation \(16z^2-26z+1=0\). Its top eigenvalue lies strictly above \(39/25\); its eigenspace is one-dimensional and has the positive ray \((\sqrt{17}-4,1)\) on the classes. A direct comparison of the three averages confirms that the row selections are active. The all-order lower law follows analytically from a two-by-two Rayleigh quotient and is not inferred from testing finitely many orders.

Successful exact execution prints `CERTIFICATE_OK canonical=55 strict=54 raw=729 winning_raw=2`, followed by the rational minima and exact squared norm. Floating-point eigenvalue comparisons are auxiliary only. No independent mathematical audit is represented by this verification.
