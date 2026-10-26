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

# Verification and reproducibility

The theorem is established by cohomology, Atiyah's indecomposable rank-two bundle, and a fixed-exceptional-divisor argument. The key reductions are: the elementary transform \(\mathcal F\) has filtration \(0\to\mathcal O_M(C_+)\to\mathcal F\to\mathcal O_M\to0\); the negative-section restriction is \(\mathscr F_2\); and the direct images of \(\mathcal O_M(jC_+-C_-)\) for \(j\geq1\) are \(\bigoplus_{i=1}^{j}L^{-i}\), all with vanishing first cohomology. This gives \(h^0=1+d\binom{m+2}{3}\) for all nonnegative integers \(m\), not just those tested by a computer.

The self-contained Python 3 script `verify.py` was run from the delivered package's source directory with `python verify.py`, and printed `VERIFY_OK 1220 exact finite parameter checks`. It verifies by exact integer and rational arithmetic the filtration formula, the cubic Hilbert coefficients, and the Hirzebruch--Riemann--Roch polynomial for all tested degrees \(1\leq d\leq20\) and exponents \(0\leq m\leq60\). As a separate mathematical check, the Riemann--Roch computation gives \(\chi(M,\operatorname{Sym}^m\mathcal F)=d\binom{m+2}{3}\), consistent with the unique additional section from \(\mathscr F_{m+1}\).

Finite checks cannot certify all exponents or identify prior published work. The precise nonstandard geometric inputs are in Denisi--Höring, arXiv:2610.03048v1, Section 3. The rational function was compared against the full coefficient identity, and the top-intersection calculation was separately checked with \(c_1(T_M)^2=c_2(T_M)=0\). Independent audit remains unperformed.
