# Independent scientific audit — 2026-10-01

**Disposition:** passed

**Final claim:** For every weight-three syndrome in the original ternary Gashkov–Sidel'nikov norm-one-torus model, the number \(M(S)\) of successful first torus probes is exactly half the \(\mathbb F_q\)-point count of the stated genus-one curve \(C_{N(S)}\); hence the success probability is \(1/2+O(q^{-1/2})\), expected direct probes are \(2+O(q^{-1/2})\), and the number of minimum weight-three leaders is \(\#C_{N(S)}(\mathbb F_q)/6\).

## C — PASS

The source length-two character criterion converts success into \(\chi(a(a-1))=-1\) for \(a=N(S-\beta)\). Solving the norm fiber gives exactly \(1-\chi((n+1-a)^2-n)\) torus roots, so summing the character indicator yields \(M=(q+2+J_n)/2\). For \(n\ne0,1\) the quartic \(X(X-1)((n+1-X)^2-n)\) is squarefree; its square leading coefficient gives two rational points at infinity, hence \(\#C_n=q+J_n+2=2M\). Hasse then gives the stated bound. The inspected finite-field artifact independently enumerates \(q=9,27,81\), but the infinite theorem rests on the exact character-sum argument.

## O — PASS

An earlier published SCOPE record already gives \(q/6+O(\sqrt q)\) leader multiplicity and norm-orbit invariance, so those qualitative facts are prior art. The audited record is sharper: it identifies the exact count with a specific genus-one point count, improves the uniform discrepancy constant, and converts it to a \(1/2+O(q^{-1/2})\) success law for the direct torus probe. The 2026 source paper’s accessible abstract confirms the same torus decoding framework and use of character sums/Weil bounds but does not expose the full theorem text; the full text was unavailable through the accessible lawful route in this audit. That access gap is a material residual risk and was not treated as evidence of noncoverage.

### Equivalent formulations

**Searches:** Published SCOPE search: Gashkov–Sidel'nikov norm-one torus direct sampling elliptic curve success count; Web search: Gashkov Sidelnikov successful first summands elliptic curve torus

**Evidence:** The only exact published SCOPE hit for the elliptic point-count identity is the audited record itself. The 2026 source abstract states exact additive lengths and character-sum/Weil constructions but not the audited point-count formula.

**Reasoning:** No accessible equivalent statement of \(M(S)=\#C_{N(S)}(\mathbb F_q)/2\) was located.
### Broader coverage

**Searches:** Published SCOPE 2026/09/18 gashkov-sidelnikov-deep-hole-multiplicity--160ef35008b2; arXiv:2609.20402

**Evidence:** The earlier SCOPE result gives only an explicit \(q/6+O(\sqrt q)\) discrepancy and norm invariance; it explicitly says the qualitative scale traces to the 1986 character sum. The 2026 arXiv abstract describes complete decoding and character-sum constructions but does not state a stronger direct-probe count.

**Reasoning:** The earlier SCOPE theorem is partial coverage, not a dominating exact formula. The inaccessible full 2026 source remains the main risk.
### Exact database or table

**Searches:** Published SCOPE semantic search for deep-hole multiplicity and direct torus decoder; Exact search for "#C_n" with Gashkov–Sidel'nikov torus decoding

**Evidence:** The earlier SCOPE multiplicity record was found and compared theorem-by-theorem; no exact elliptic-curve table/count was located elsewhere.

**Reasoning:** The claim is an exact character-sum/curve identity, not a recomputation from a known table.
### Claim versus prior implication

**Searches:** Implication comparison with SCOPE-20260918-160ef35008b2 and arXiv:2609.20402 abstract

**Evidence:** A \(q/6+O(\sqrt q)\) bound and norm invariance do not determine the Frobenius trace or exact \(M(S)\), so they do not imply the audited curve identity. The source abstract does not provide enough theorem text to decide whether its internal character sums already simplify to the same curve.

**Reasoning:** Accessible prior results do not imply the exact identity; source-paper overlap remains a documented best-of-knowledge risk.

## V — PASS

The exact elliptic-curve count turns a worst-case direct-search description into a uniform two-probe-scale Las Vegas analysis and simultaneously quantifies all minimum leaders in each hard coset. This is a motivated structural refinement of a current decoding problem, not a cosmetic character-sum rewrite.

## Source inspections

- **A sharpened explicit deep-hole leader discrepancy for ternary Gashkov--Sidel'nikov codes** — Published SCOPE record 2026/09/18/gashkov-sidelnikov-deep-hole-multiplicity--160ef35008b2. Trigger: Closest prior SCOPE theorem on the same leader multiplicity Material read: Complete RESULT.md at the audited repository snapshot. Method: Repository full-text inspection Assessment: PARTIAL_COVERAGE. Evidence: It gives \(|L(S)-q/6|\le\sqrt q/2+14/3\), norm-orbit invariance, and the marked-leader factor three, but no exact elliptic point-count formula.
- **Norm-One Torus Decompositions and Decoding of Gashkov-Sidel'nikov Codes** — arXiv:2609.20402. Trigger: Primary source for the torus model and length-two criterion used by the proof Material read: Accessible abstract and bibliographic metadata only; full text was unavailable in this audit. Method: Public arXiv abstract and metadata Assessment: INACCESSIBLE_PLAUSIBLE_SOURCE. Evidence: The abstract confirms exact additive lengths, character sums, Weil bounds, and maximum-likelihood decoders, but cannot settle whether the exact direct-probe elliptic count appears in the full paper.

## Residual risks

- The full text of arXiv:2609.20402 was unavailable in this audit; because it is the same-object primary source and uses character sums, possible exact overlap remains the main originality risk.
- Older Zetterberg/Gashkov–Sidel'nikov decoding literature may encode the same curve under an eliminated conic formulation.

## Limitations

- Specific to the characteristic-three original Gashkov–Sidel'nikov torus model.
- The theorem improves candidate-probe counts, not total bit complexity.
- The primary 2026 source full text was inaccessible in this run; the abstract alone was not used to assert whole-document noncoverage.
