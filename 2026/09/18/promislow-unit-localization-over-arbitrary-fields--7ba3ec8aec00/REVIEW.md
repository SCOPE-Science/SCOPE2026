# Same-model review

## Result reviewed

**Coefficient transport removes the characteristic-two restriction in Promislow unit localization**

The reviewed claims are:

1. Tabei's effective localization radius \(D_u(n)\) for \(\mathbb F_2[\mathsf P]\) also works over an arbitrary coefficient field \(k\);
2. the extension follows from a coefficient-sum coarsening lemma that preserves the original coefficient lists while the support geometry is compressed;
3. over every finite field \(\mathbb F_q\), existence of a nontrivial unit with prescribed total support is decidable and the least total support is computable in principle.

## Correctness review

### Coefficient-sum coarsening

For a unit pair
\[
\alpha=\sum_i a_i g_i,\qquad \beta=\sum_j b_j h_j,\qquad \alpha\beta=1,
\]
partition the index pairs by the original product \(g_i h_j\). The coefficient sum of the identity class is \(1\), and every other class has coefficient sum \(0\).

If a new realization keeps each old class monochromatic, then every new product fiber is a union of whole old classes. A nonidentity new fiber cannot contain the anchored class and therefore has coefficient sum \(0\); the identity fiber contains the anchored class plus zero-sum classes and therefore has coefficient sum \(1\). This proves the weighted coarsening lemma over an arbitrary field.

A possible merger of an old nonidentity class into the anchored product is harmless: it adds zero. A merger among several nonidentity classes is also harmless: it adds zeros.

### Reuse of the localization geometry

Tabei's Steps 2--3 encode only:

- the coset labels in the index-four quotient of the Promislow group;
- equalities of products within each old product fiber;
- the requirement that the anchored fiber have product \(1\);
- pairwise distinctness of support elements on each side.

The resulting integer linear system and the small-solution/distinctness argument contain no coefficient-field data. Thus the same small realization and the same radius bound \(D_u(n)\) can be used while the coefficients \(a_i,b_j\) are carried along unchanged.

Because the new support elements are pairwise distinct on each side and all carried coefficients remain nonzero, support cardinalities are unchanged.

### Two-sided invertibility

The weighted lemma yields \(\alpha'\beta'=1\). The Promislow group is virtually abelian and hence amenable and sofic. Elek--Szabó direct finiteness applies to group algebras of sofic groups over arbitrary fields, so \(\beta'\alpha'=1\) as well. Therefore the constructed element is genuinely a unit.

### Finite-field decision procedure

For fixed \(q,n\), both the bounded ball and the coefficient field are finite, so the candidate support pairs and coefficient assignments form a finite set and can be checked exactly. Murray's units over every prime field embed into every finite extension of the same characteristic, guaranteeing termination when total support sizes are tested in increasing order.

### Adversarial checks

- The argument does not assume that distinct old product fibers remain distinct after compression; the coarsening lemma was formulated precisely to allow mergers.
- It does not replace coefficients by arbitrary new ones; retaining the original coefficients is essential.
- The radius bound is unchanged because coefficients never enter the integer realization system.
- Direct finiteness is needed because the construction first gives a right inverse. It is available for \(k[\mathsf P]\) over every field.
- The finite-search conclusion is restricted to finite fields. Bounded support alone does not make coefficient search finite over an infinite field.
- No assertion is made that Tabei's characteristic-two proof itself was incorrect; the result extends a limitation explicitly identified in Remark 7.3.

**Correctness: PASS.**

## Originality review

Tabei's arXiv:2609.17559v1 was inspected at Theorem 7.2, its proof, and Remark 7.3. The paper proves effective localization only for \(\mathbb F_2[\mathsf P]\). Remark 7.3 states that coefficients enter over \(\mathbb F_p\), that the pattern would need coefficient sums modulo \(p\), and that this direction is not pursued.

Adjacent prior work was checked for stronger coverage:

- Murray supplies nontrivial units in every prime characteristic but does not provide the total-support-to-radius localization theorem.
- Craven--Pappas property (U), as summarized and compared by Tabei, bounds inverse support from a prescribed support set; Tabei explicitly distinguishes this from a search radius depending only on total support.
- Claramunt--Grabowski develop arbitrary-field criteria for units in virtually abelian group rings and specialize them to the Promislow group; this is related structural prior work, not the coefficient-transport localization statement.
- Elek--Szabó supplies the direct-finiteness input.

Targeted searches for Promislow-unit localization over \(\mathbb F_p\), finite-field minimal-support decidability, coefficient-weighted coarsening, and equivalent support-geometry formulations did not reveal the same extension.

The originality claim is therefore limited to the coefficient-transport/coarsening extension of Tabei's effective localization and the resulting finite-field computability statement. The underlying group coordinates, integer compression bound, existence of positive-characteristic units, property (U), and direct finiteness are explicitly excluded from the novelty claim.

The source preprint is recent and currently presented as v1, so a subsequent author revision or concurrent independent observation remains a material originality risk.

**Originality: PASS, to the best of our knowledge.**

## Value review

The result closes an explicit limitation in a recent quantitative study of Gardam/Murray units. It shows that the obstruction in passing from \(\mathbb F_2\) to other fields is not geometric: once one starts from an actual unit, its coefficients already encode all necessary cancellation and can simply be transported through the geometric compression.

The consequence is substantive: the global minimum-support problem becomes computable in principle over every finite field, not only over \(\mathbb F_2\), with no deterioration of the localization radius bound.

**Value: PASS.**

## Scientific limitations

- The result is conditional on the existence of a unit when the coefficient field is arbitrary; existence over finite fields follows from Murray's prime-characteristic constructions.
- It gives computability, not a practical search radius.
- It does not establish finite-search decidability over infinite coefficient fields.
- The source is a recent v1 preprint and may be revised.
- Originality is to the best of our knowledge; no independent validation is asserted.

Same-model review: passed. Cross-model review: not yet performed.
