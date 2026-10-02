# Independent audit — SCOPE-20260909-080

Audited at: 2026-09-30T23:18:42Z

Disposition: **repaired**

## Correctness

**PASS** — A fresh independent finite-field reconstruction from the two defining brackets gives second cohomology dimension 6. Recomputing the induced action of 12 explicit automorphism generators and performing a new breadth-first orbit enumeration over all 15625 classes gives exactly eight orbit sizes 1, 4, 24, 96, 600, 2400, 5000 and 7500. The class-preserving subspace has dimension 1 and its four nonzero classes form one orbit; direct center computation for the split and nonzero class-preserving extensions gives center dimension 3 in both cases. These checks reproduce the headline obstruction.

Sources/evidence:
- Actual package s0_h2_aut_orbits.py, w_orbits.py, verify.py and committed_log.json at the audited source revision.
- Fresh independent Python reconstruction of the cohomology quotient, automorphism action, full 15625-class orbit partition and extension centers.

Residual risks:
- The Phi_7 family label itself is inherited from the cited classification context and was not independently re-derived; the algebraic obstruction does not depend on that label.
## Originality

**PASS** — The algebra is the known five-dimensional nilpotent algebra L_{5,8}, and general Lazard/cohomology theory is prior art, but searches found no published finite-field order-5 automorphism-orbit census on its second cohomology with these eight sizes or the stated center-25 extension obstruction. Existing classifications identify the algebra or classify broader low-dimensional families without implying this exact F5 orbit partition.

### Originality comparison details

**Equivalent formulations.** Naming the stem as L_{5,8} is an equivalent formulation of the base object, not prior coverage of the finite-field orbit result.
- The same algebra appears in low-dimensional Lie algebra classifications under L_{5,8}; no matching F5 cohomology orbit table was located.

**Broader coverage.** General theory supplies the framework, not the enumerated invariant or obstruction.
- Lazard correspondence transports cohomological information in its range, and dimension classifications list L_{5,8}, but neither inspected source gives the eight F5 Aut-orbits or the exact center obstruction.

**Exact database or table.** The orbit partition is not a recomputation of an identified published table.
- No exact table with the eight sizes was found.

**Claim versus prior implication.** Substantial finite-field computation remains after applying the general theorems.
- The prior sources do not determine the action of Aut(Q) on second cohomology over F5 or the center dimensions of the two class-preserving orbit types.

### Source inspections
- **Transporting cohomology in Lazard correspondence** — NOT_COVERING. Material read: Full HTML text. Evidence: Provides general cohomology transport, not this finite orbit census.
- **Low-dimensional nilpotent Lie algebra classification material identifying L_{5,8}** — OBJECT_IDENTIFICATION_ONLY. Material read: Search-accessible classification excerpt identifying L_{5,8} by the same two brackets. Evidence: Identifies the algebra but does not give the F5 second-cohomology Aut-orbits.

Originality residual risks:
- A computational p-group database may encode equivalent groups without presenting the cohomology orbit calculation; no decisive implication was found.
## Scientific value

**PASS** — A complete automorphism-orbit census of a natural stem over F5 and a sharp obstruction for class-2 one-step extensions are standard, motivated classification data. The result is not an arbitrary finite slice: it closes one explicit extension route and identifies exactly why the desired center size cannot occur from this stem.

Sources/evidence:
- Low-dimensional classification literature establishes the naturality of L_{5,8}.
- The full orbit census and obstruction are exact finite classification statements.

Residual risks:
- The result should remain scoped to the exponent-5 Lazard stratum and this stem.

## Limitations

- The algebraic statement is confined to the exponent-5 Lazard stratum and the displayed stem.
- The Phi_7 family label is contextual and not needed for the proved obstruction.
