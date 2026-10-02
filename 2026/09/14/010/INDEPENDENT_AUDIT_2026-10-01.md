# Independent mathematical audit — 2026-10-01

Record: `SCOPE-20260914-010`

Disposition: **PASSED**

## Correctness — PASS

For the symmetric two-box law, direct integration gives \(A(v)=\arctan(2/v)-\arctan(1/v)>0\) and \(G_\mu(iv)=-iA(v)\). The support bounds imply \(v/(4+v^2)\le A(v)\le v/2\). Thus \(f_t(v)=tv-(t-1)/A(v)\) is negative below \(\sqrt{2(t-1)/t}\) and exceeds one above \((1+\sqrt{1+16(t-1)})/2\). Subordination keeps the imaginary-axis solution in a compact positive interval, so \(-\operatorname{Im}G_{\mu^{\boxplus t}}(i\eta)\) stays bounded below as \(\eta\downarrow0\). Therefore zero belongs to the support for every \(t>1\), ruling out a symmetric support with exactly two interval components.

## Originality — PASS

General free-power support theory and component monotonicity were inspected, but no located source states immediate inclusion of zero for this disconnected uniform two-box law or the resulting refutation of a finite two-to-one merger time. The proof needs an additional law-specific imaginary-axis estimate and symmetry argument.

## Scientific value — PASS

The symmetric union of two equal uniform boxes is a natural disconnected input. Proving that the central gap is hit immediately for every parameter value above one rules out an intuitive single finite merger scenario by a structural all-parameter argument rather than a finite numerical check.

## Literature and prior-coverage checks

- **Supports of Measures in a free additive convolution semigroup** — https://arxiv.org/abs/1205.5542. framework, not exact coverage: General component monotonicity and density/support formulas are present; the two-box immediate central-support statement is not stated.

## Limitations and residual risk

- Only the impossibility of the proposed two-component regime is validated; the later complete support-component evolution is not claimed.
- Originality is best-of-knowledge against general free-power support theory.
- The exact law may have been treated in a numerical/free-probability example under different normalization; no such source was found.
