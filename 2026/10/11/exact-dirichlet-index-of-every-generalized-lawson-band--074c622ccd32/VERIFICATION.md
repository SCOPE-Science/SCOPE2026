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

Put
\[
H=1+(4k^2-1)\sin^2x.
\]
The separated radial operator is
\[
\mathcal L_{k,n}
=
\frac{d^2}{dx^2}
+
\frac{(4k^2-1)\sin x\cos x}{H}\frac{d}{dx}
-
\frac{n^2}{H}
+
2+\frac{8k^2}{H^2}.
\]

The checker verifies symbolically that
\[
\mathcal L_{k,2k+1}
\left(
\frac{1+(2k-1)\sin^2x}{\sqrt H}
\right)=0.
\]
It also verifies
\[
\frac{\mathcal L_{k,2k-1}(\sin x)}{\sin x}
=
\frac{
(2k-1)(2k+1)(4k-1)\sin^2x+8k^2+4k-1
}{
H^2
}.
\]
Both coefficients in the numerator are positive for every integer \(k\ge1\).

The positive zero-mode gives the exact ground-state identity
\[
E_{2k+1}^k[f]
=
\int_0^\pi
\sqrt{2H}\,
u_+^2
\left|
\left(\frac f{u_+}\right)'
\right|^2dx
\]
for Dirichlet \(f\). Thus this mode is strictly positive, while the displayed \(\sin x\) calculation gives a genuinely negative Rayleigh value at \(2k-1\).

The checker additionally verifies the stated unit normal and the decomposition of the ambient rotational Jacobi field \(R_{13}\), whose \(2k+1\) Fourier coefficient is the positive zero-mode.

The mode-count step uses the primary paper's proved Sturm--Liouville facts: even sectors contribute neither index nor nullity except for the \(n=0\) Jacobi field, and in each odd sector only the lowest radial eigenfunction can contribute at nonpositive energy.

Finite numerical eigenvalue checks are included only as implementation diagnostics and are not used as proof of the all-\(k\) theorem.
