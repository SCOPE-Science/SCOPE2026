# Mathematical review

## Correctness — PASS

For multiplicity vectors of total \(n\), common deletion outputs of length \(k\) occur exactly when coordinatewise minima sum to at least \(k\). Heavy coordinates (multiplicity at least \(k\)) are disjoint between codewords, giving at most \(q\) heavy words. Two light vectors intersect in at least \(2n-q(k-1)\), excluding a second light word past the stated first threshold. The absence of any light vector after \(q(k-1)\), and the pure-word/light-word constructions, establish both exact values. The parity-dependent construction at the first threshold establishes sharpness. At the two upper endpoints the light word has respectively zero deficit and a single unit deficit, and compatibility forces all heavy words to be pure except a single possible one-symbol transfer. This proves the unique and \(q^2\) classifications. Exact finite counts in the supplied checker agree, but are not used to justify the infinite assertion.

## Originality — PASS, subject to residual literature risk

The initial 2026 preprint and its July revision were inspected at their definitions, high-deletion sections and stated contributions. Their exact cases concern smaller survivor counts and single-deletion regimes; their bounds do not algebraically imply the sharp \(k\ge4\) plateau or both classifications. Existing public three-survivor findings are deliberately excluded from the theorem's range. Searches across mathematical research records, aliases using integer-simplex constant-weight \(\ell_1\) codes, and primary papers identified no stronger covering statement. A newer 2026 multiset construction preprint was available at abstract level only and remains a residual priority risk; absence of a search hit does not prove priority.

## Mathematical value — PASS

In the high-deletion regime, the number of surviving symbols \(k\), not the number deleted, controls whether a tiny exact code is possible. The result determines an infinite two-parameter transition with a sharp first boundary, then completely identifies the maximizing codebook structure at both upper endpoints. It strengthens the known coarse high-deletion bounds without requiring large blocklength asymptotics or arbitrary finite enumeration.

## Scientific limitations

No statement about \(n\le\lfloor(q+1)(k-1)/2\rfloor\) beyond one construction, about all interior maximizing codebooks, or about ordinary string deletion codes. Cross-checks are finite; mathematical validity rests on the exact intersection argument. Earlier literature not fully accessible may affect priority.

Self-review: passed. Independent audit: not yet performed.
