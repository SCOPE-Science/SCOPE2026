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

The proof has two independently checkable layers.

First, the structural input is the finite-monounary classification: polymorphism-homogeneity is equivalent to having no sources or having all sources at one common height. The cited source states this explicitly as Theorem 4.9.

Second, `verify.py` checks the new enumerative layer without symbolic-algebra dependencies. It builds the truncated formal series from
\[
T_0(z)=z,\qquad T_h(z)=z(\exp(T_{h-1}(z))-1),
\]
forms
\[
F_h(z)=\frac1{1-z\exp(T_{h-1}(z))},
\]
and evaluates the coefficientwise finite sum. In parallel it exhaustively scans all \(n^n\) maps \([n]\to[n]\) for \(1\le n\le7\), computes the indegree-zero sources and their exact heights, and compares the counts height by height.

The exhaustive totals are
\[
1,4,27,232,2285,25716,324583,
\]
and agree with the generating-function computation. The latter continues with
\[
4571904,71321769,1225291780
\]
for orders eight through ten.

The script also checks the explicit numerical bounds used to separate the dominant \(h=1\) singularity from all strata \(h\ge2\): at \(r=0.58\),
\[
r(e^r-1)=0.4559022898\ldots<r,
\]
and
\[
r\exp(r(e^r-1))=0.9150057902\ldots<1.
\]
The infinite asymptotic conclusion itself is proved analytically in `RESULT.md`; the finite computation is a consistency check, not a substitute for that proof.
