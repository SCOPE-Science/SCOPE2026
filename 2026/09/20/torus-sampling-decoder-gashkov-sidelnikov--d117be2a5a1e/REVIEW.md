# Independent audit review — 2026-10-01

## Final claim

For every weight-three syndrome in the original ternary Gashkov–Sidel'nikov norm-one-torus model, the number \(M(S)\) of successful first torus probes is exactly half the \(\mathbb F_q\)-point count of the stated genus-one curve \(C_{N(S)}\); hence the success probability is \(1/2+O(q^{-1/2})\), expected direct probes are \(2+O(q^{-1/2})\), and the number of minimum weight-three leaders is \(\#C_{N(S)}(\mathbb F_q)/6\).

## Correctness — PASS

The source length-two character criterion converts success into \(\chi(a(a-1))=-1\) for \(a=N(S-\beta)\). Solving the norm fiber gives exactly \(1-\chi((n+1-a)^2-n)\) torus roots, so summing the character indicator yields \(M=(q+2+J_n)/2\). For \(n\ne0,1\) the quartic \(X(X-1)((n+1-X)^2-n)\) is squarefree; its square leading coefficient gives two rational points at infinity, hence \(\#C_n=q+J_n+2=2M\). Hasse then gives the stated bound. The inspected finite-field artifact independently enumerates \(q=9,27,81\), but the infinite theorem rests on the exact character-sum argument.

## Originality — PASS

An earlier published SCOPE record already gives \(q/6+O(\sqrt q)\) leader multiplicity and norm-orbit invariance, so those qualitative facts are prior art. The audited record is sharper: it identifies the exact count with a specific genus-one point count, improves the uniform discrepancy constant, and converts it to a \(1/2+O(q^{-1/2})\) success law for the direct torus probe. The 2026 source paper’s accessible abstract confirms the same torus decoding framework and use of character sums/Weil bounds but does not expose the full theorem text; the full text was unavailable through the accessible lawful route in this audit. That access gap is a material residual risk and was not treated as evidence of noncoverage.

## Value — PASS

The exact elliptic-curve count turns a worst-case direct-search description into a uniform two-probe-scale Las Vegas analysis and simultaneously quantifies all minimum leaders in each hard coset. This is a motivated structural refinement of a current decoding problem, not a cosmetic character-sum rewrite.

## Source inspections

- **A sharpened explicit deep-hole leader discrepancy for ternary Gashkov--Sidel'nikov codes** (Published SCOPE record 2026/09/18/gashkov-sidelnikov-deep-hole-multiplicity--160ef35008b2): PARTIAL_COVERAGE. It gives \(|L(S)-q/6|\le\sqrt q/2+14/3\), norm-orbit invariance, and the marked-leader factor three, but no exact elliptic point-count formula.
- **Norm-One Torus Decompositions and Decoding of Gashkov-Sidel'nikov Codes** (arXiv:2609.20402): INACCESSIBLE_PLAUSIBLE_SOURCE. The abstract confirms exact additive lengths, character sums, Weil bounds, and maximum-likelihood decoders, but cannot settle whether the exact direct-probe elliptic count appears in the full paper.

## Residual risks

- The full text of arXiv:2609.20402 was unavailable in this audit; because it is the same-object primary source and uses character sums, possible exact overlap remains the main originality risk.
- Older Zetterberg/Gashkov–Sidel'nikov decoding literature may encode the same curve under an eliminated conic formulation.
