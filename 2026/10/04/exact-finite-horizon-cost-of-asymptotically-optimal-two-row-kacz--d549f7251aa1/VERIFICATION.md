---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-05.md",
      "INDEPENDENT_AUDIT_2026-10-05.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

In coordinates \(a=(1,0)\), \(b=(c,s)\), applying one sweep to \(a^\perp\) gives squared norm \(c^2+s^2(\omega-1)^2\), proving the unique one-sweep optimum \(\omega=1\). Direct trace, determinant, and discriminant calculation gives the classical spectral-radius optimizer \(\omega_\star=2/(1+s)\) and a repeated eigenvalue \(q=(1-s)/(1+s)\). At that parameter \(T=qI+N\) with \(N^2=0\), so \(T^k=q^k(I+kN/q)\); determinant one and the Frobenius norm determine the displayed largest singular value exactly. The unrelaxed matrix is rank one with \(T_1^k=c^{2k-2}T_1\). Taylor expansion of the exact log-ratio with \(k\sqrt{s}\to\alpha\) gives coefficient \(\alpha(1-4\alpha^2/3)\). The bundled symbolic checker verifies every algebraic identity and exact rational power-norm replays; independent direct matrix calculations at multiple \(s,k\) values matched the formulas.

## originality

PASS

The asymptotically optimal two-cyclic SOR/Kaczmarz relaxation is classical, and modern sources analyze relaxed Kaczmarz convergence rates. The audited contribution begins where that asymptotic statement stops: the optimizer lands at a defective double root, producing an exact polynomial transient in the Euclidean power norm, a strict one-sweep disadvantage, and an \(s^{-1/2}\) finite-horizon crossover with a sharp scaled threshold. Targeted Resultary and literature searches found no source stating or implying that complete finite-horizon profile.

## value

PASS

The result exposes a concrete and practically meaningful separation between asymptotic rate tuning and finite-horizon worst-case performance in the smallest nontrivial Kaczmarz system. The exact Jordan transient, strict one-sweep cost, and crossover law quantify when the classical asymptotic optimizer becomes advantageous, making the fact reusable in relaxation/tuning analysis rather than a routine matrix exercise.

The dated certificate retains the supplied scientific assessment, sources and limitations.
