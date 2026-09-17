# Review

**Same-model review: passed. Cross-model review: not yet performed.**

## Correctness

The proof was checked from the definitions of Apéry representatives and Kunz coordinates. For \(r\in hX\), summing \(h\) semigroup elements representing residues in \(X\) produces an element \((h+t)m+r\in S\) with \(0\le t\le h-1\); minimality of the Apéry representative therefore gives \(x_r\le2h-1\). Repeated Cauchy--Davenport in \(\mathbb Z/p\mathbb Z\) then yields
\[
\Theta_{2h-1}\ge \min(p-1,h\eta).
\]

The layered lower bound follows by inserting these odd-layer estimates, together with monotonicity of \(\Theta_t\), into the exact cumulative-layer identity
\[
|L|=q+\sum_{t=1}^{q-2}\Theta_t+\Theta_{q-1,\rho}.
\]
The count of terms in the terminal block is \(q-2k\), and the stated Wilf inequality follows from \(c=qp-\rho\). The monotonicity calculation between consecutive admissible \(k\) was also checked algebraically.

A standalone exact-integer computation verifies the displayed example \(S=\langle29,41,42,54,56,57\rangle\), including its Apéry set, Kunz populations, conductor data, left-element count, Wilf number, and the comparison with the prior first-layer tests.

## Originality

Originality is assessed to the best of our knowledge.

The closest source inspected is Yang--Zhang (2026), which defines the cumulative Kunz populations \(\Theta_t\), proves the exact cumulative-layer formula and a hierarchy of criteria assuming information about \(\Theta_t\), and explicitly points to interactions among low Kunz layers as a direction for refinement. No statement there derives higher-layer population from additive growth of the first-layer residues, and no Cauchy--Davenport specialization for prime multiplicity was found.

Searches also covered combinations and synonymous formulations involving:
- Cauchy--Davenport with numerical semigroups, Apéry sets, Kunz coordinates, and Wilf's conjecture;
- prime multiplicity with Kunz coordinates and Wilf;
- sumsets and first/cumulative Kunz layers;
- additive combinatorics in earlier Wilf literature.

Eliahou (2018) uses sumsets and Macaulay growth in the \(c\le3m\) analysis, and Eliahou--Fromentin (2019) uses \(B_h\) sets to construct near-misses. These are important conceptual neighbors but do not state the sumset-to-Kunz-layer containment proved here. Bruns--García-Sánchez--O'Neill--Wilburne (2020) treats fixed multiplicity through Kunz polyhedra and finite-poset methods; its accessible preprint and indexed descriptions were checked for the relevant terminology and no matching criterion was located.

The 2026 first-layer paper is recent and non-peer-reviewed. Very recent or incompletely indexed follow-up work is therefore the main residual originality risk. No inaccessible paper was identified whose available metadata or surrounding citations specifically suggest that it contains the theorem proved here.

## Value

The result links two quantities that previously entered the recent Wilf analysis separately: the first Kunz layer and higher cumulative layers. For arbitrary multiplicity it gives a reusable structural containment; for prime multiplicity it converts this into explicit linear layer growth by a classical additive theorem. Combining all forced layers produces a family of checkable Wilf lower bounds depending only on \(p,e,q,\rho,\eta\), rather than requiring higher \(\Theta_t\) as additional input.

The example of multiplicity \(29\) demonstrates that the resulting criterion reaches parameter values not certified by either first-layer condition in the closest 2026 paper.

## Limitations

The Cauchy--Davenport numerical bound is prime-specific; composite multiplicities may have periodic sumsets and require Kneser-type information. The Wilf inequality obtained here is only sufficient and deliberately drops a nonnegative trimmed cumulative-layer term. No claim of a complete solution to Wilf's conjecture is made.
