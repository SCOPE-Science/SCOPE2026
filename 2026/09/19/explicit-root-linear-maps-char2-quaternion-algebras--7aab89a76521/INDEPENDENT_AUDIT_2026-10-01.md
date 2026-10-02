# Independent mathematical audit — 2026-10-01

Record: `SCOPE-20260919-7aab89a76521`

## Correctness — PASS

For the standard characteristic-two quaternion involution, \(H=F\oplus Kj\) and the alternate subgroup is \(A=F\). Division forces \(b
otin F^2\), so it extends to a finite 2-basis. Since \(K/F\) is separable quadratic whereas \(F/F^2\) is purely inseparable, \(F\) and \(K^2\) are linearly disjoint over \(F^2\), and the chosen 2-basis of \(F\) becomes a \(K^2\)-basis of \(K\). Modulo \(A\), congruence by \(c+dj\) acts on \(z\in K\) as \(c^2z+bd^2\sigma(z)\). On each central monomial \(m_S\), its \(Q\)-span is exactly \(K^2m_S\oplus bK^2m_S\), and these blocks form a direct sum. Thus the stated classes form a left-\(Q\) basis. Frobenius inversion on each coefficient block gives the coordinate maps \(lpha_S\), and the source paper's identification of root-linear maps with \(Q\)-linear maps \(H/A	o Q\) proves completeness. The Laurent-series example also checks: the unramified norm has even valuation, so \([1,t)\) is division and even/odd exponents give \(F=F^2\oplus tF^2\).

### Correctness sources

- assigned RESULT.md
- de Seguins Pazzis arXiv:2609.20363 full text, Lemma 2.1 and Section 2.1
- standard characteristic-two quaternion structure

### Correctness risks

- The coordinate basis depends on the chosen quaternion presentation and 2-basis.
- Finite coordinates require finite 2-rank.

## Originality — PASS

The primary 2026 source was inspected in full through its root-linear section. It proves abstractly that root-linear maps are left-division-ring linear maps \(H/A	o D\), and for quaternion division rings with standard involution explicitly notes that nonzero maps exist but gives no constructive description without a choice-of-basis argument. Fresh semantic searches found no prior finite-2-rank quaternion coordinate basis or resulting explicit normal form. Older quaternion and p-basis literature remains a terminology-level risk, but no decisive equivalence was located.

### equivalent_formulations

Searches:
- Resultary search for characteristic-two quaternion root-linear maps and finite 2-rank bases
- search under p-basis/Frobenius-twisted quotient formulations

Evidence:
- The audited record was the only exact root-linear coordinate theorem returned.
- The primary source supplies only abstract \(H/A\) duality.

Reasoning:
Equivalent formulations as a Frobenius-twisted semilinear decomposition of \(K\) and as explicit coordinates on \(H/A\) were considered.

### broader_coverage

Searches:
- de Seguins Pazzis arXiv:2609.20363
- standard characteristic-two quaternion references

Evidence:
- The source classification is broader for range-compatible maps but leaves the quaternion root-linear term nonconstructive.
- Classical quaternion theory supplies the presentation, involution, and 2-basis ingredients, not the displayed coordinate dual in the recent root-linear language.

Reasoning:
No broader inspected theorem mechanically states the complete coordinate basis and normal form.

### exact_database_or_table

Searches:
- current Resultary quaternion/root-linear records
- standard quaternion/p-basis references

Evidence:
- No exact database/table of \(\dim_Q(H/A)=2^{r-1}\) with these coordinate maps was located.

Reasoning:
This is a structural module computation, not a finite census or known table recomputation.

### claim_vs_prior_implication

Searches:
- implication comparison with source Lemma 2.1 and abstract Zorn-basis argument

Evidence:
- Abstract existence of a nonzero \(Q\)-linear functional on \(H/A\) does not give the dimension, a basis, or coordinate formulas.
- The audited 2-basis decomposition supplies the additional constructive content.

Reasoning:
The final theorem is therefore not a corollary of the source classification without the new semilinear module calculation.

### source_inspections

- **Range-compatible homomorphisms on Hermitian matrices** — https://arxiv.org/abs/2609.20363. Trigger: Primary source introducing the noncommutative root-linear formulation. Material read: Primary full text through pages 1--12, including Theorems 1.4--1.7 and Section 2.1, obtained through authorized access after open routes failed. Method: Full theorem and root-linear-module comparison. Assessment: NOT COVERING the explicit quaternion coordinates. Evidence: Section 2.1 identifies root-linear maps with linear maps on \(H/A\) and explicitly describes quaternion construction as nonconstructive.
- **Quaternion Algebras, characteristic-two chapter** — https://link.springer.com/chapter/10.1007/978-3-030-56694-4_6. Trigger: Classical structural background for \([a,b)\), involution, and cyclic algebra notation. Material read: Background theorem scope as cited by the record. Method: Ingredient comparison. Assessment: Classical background only. Evidence: No root-linear range-compatible coordinate classification was located there.

### checked_sources

- https://arxiv.org/abs/2609.20363
- Voight, Quaternion Algebras, Chapter 6
- current Resultary root-linear/quaternion search
- assigned RESULT.md

### residual_risks

- Older p-basis or semilinear quaternion literature could contain an equivalent module decomposition under different terminology; no such source was located.

## Scientific value — PASS

The theorem fills a construction gap explicitly identified in the source classification: it computes the quotient-module dimension, gives a concrete basis of every root-linear map, and turns the nonlocal term in the Hermitian range-compatible classification into finite coordinates. That is a natural constructive structural refinement rather than a cosmetic basis choice.

### Value sources

- de Seguins Pazzis root-linear classification
- audited finite 2-basis module decomposition

### Value risks

- The basis is noncanonical and depends on presentation choices, but the dimension and complete coordinate description are intrinsic enough to be reusable.

## Limitations

- Finite-coordinate form assumes finite 2-rank.
- The displayed basis is not canonical.
- Originality is best-of-knowledge with older p-basis/quaternion terminology as residual risk.

## Disposition

**PASSED**
