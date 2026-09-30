# Independent audit — 2026-09-29

**Record:** `2026/09/12/081`  
**Disposition:** **repaired**  
**Audited tree:** `21ae32671df593a3db11895549c19e8c0f3ce619`

## Correctness
The boundary-block calculation is correct: at t=q=1/2 the horizontal term vanishes on V^n_{i0}, the vertical eigenvalues tend to -2/3 with multiplicity n+1, and the ordinary resolvent is non-compact. For every real s the positive trace Tr(|D|^{-s}) diverges. For non-real z, however, the correct statement is failure of trace-class convergence, not the extended-real value +infinity.

## Originality
Kaad-Kyed explicitly identify D_{q,q} with the Kaad-Senior Dirac operator, while Kaad-Senior already state that its resolvent becomes compact only relative to a semifinite trace. Thus the chosen t=q=1/2 witness is an explicit corollary of known ordinary-resolvent non-compactness, not a new obstruction.

## Scientific value
The explicit eigenfamily is still a useful, concise diagnostic showing why an ordinary-trace dimension-spectrum ansatz has no convergence half-plane for this specialization.

## Findings
- Ordinary non-compact-resolvent obstruction is prior art in the t=q specialization.
- Complex-z language corrected from “+infinity” to absence of trace-class convergence.
- Repository artifact paths corrected to `artifacts/...`.

## Independent checks
- Inspected the Kaad-Kyed formulas and the submitted eigenvalue script.
- Verified e_n=(t^(n+1)-1)/(t^-1-t) approaches -2/3 at t=1/2 and remains bounded away from 0.
- Compared Kaad-Kyed introduction with Kaad-Senior prior operator and trace statement.

## Limitations
- Audit does not classify general t != q spectral behavior beyond the explicit boundary-block formula.

## Sources
- https://arxiv.org/abs/2205.06043
- https://arxiv.org/abs/1109.2326
- repository:2026/09/12/081/artifacts/kk_formulas.txt
