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

With \(N\) nonzero e-values, base e-BH rejects under the complete null exactly when \(Nc\ge K/\alpha\), so FDR is the corresponding binomial tail. For fixed \(p>0\) validity makes \(c=1/p\) worst, and partitioning \(p\) by the integer rejection threshold reduces the exact envelope to \(\max_r \Pr\{\mathrm{Bin}(K,r\alpha/K)\ge r\}\). For \(r\ge2\), the factorial-moment inequality bounds the tail by \((e\alpha)^r\), whereas the \(r=1\) term is at least \(\alpha-\alpha^2/2\); the stated \(\alpha_0\) makes the latter strictly larger. The equality constraints also force the unique law \(p=\alpha/K,c=K/\alpha\). Independent recomputation for several levels and sample sizes reproduced the envelope and the one-spike optimizer.

## originality

PASS

Wang--Ramdas define base e-BH, prove its general FDR control, discuss all-or-nothing e-values, and give dependent sharpness constructions; the relevant primary PDF pages were read. No exact iid two-point complete-null binomial envelope or optimization over all valid \((p,c)\) was located there. Later calibration work modifies e-BH rather than tabulating this base-procedure iid family. Targeted Resultary search for iid all-or-nothing e-BH and exact binomial calibration returned no equivalent theorem.

## value

PASS

All-or-nothing e-values are a canonical sharpness family in the foundational e-BH paper. The result quantifies exactly how independence changes that sharpness picture and identifies a unique extremizer at standard FDR levels, giving a useful calibration benchmark rather than a routine numerical example.

The dated certificate retains the supplied scientific assessment, sources and limitations.
