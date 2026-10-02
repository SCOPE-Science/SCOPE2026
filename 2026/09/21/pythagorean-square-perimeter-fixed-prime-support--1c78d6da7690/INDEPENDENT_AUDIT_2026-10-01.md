# Independent mathematical audit — Fixed prime support in square-perimeter primitive Pythagorean triangles

Audit date: 2026-10-01 (UTC) UTC

Scientific disposition: **passed**.

## Correctness

**PASS** — The primitive Pythagorean parametrization gives perimeter \(2m(m+n)\). If this is a square, coprimality and parity force \(m=2U^2\), \(m+n=V^2\), with \(V\) odd and \(\gcd(U,V)=1\); positivity of the second Euclidean parameter is exactly \(\sqrt2\,U<V<2U\). Exact prime support then assigns each odd prime power wholly to either \(U\) or \(V\), and the unique power of two in \(U\) converts this inequality into the stated signed logarithmic fractional-part condition. For counting, the exact relation \(P=2^{2(1-f)}V^4\) with \(f\in(1/2,1)\) permits replacing \(P\le X\) by a fixed-width perturbation of a simplex boundary. Weyl equidistribution of the irrational linear form modulo one supplies the factor \(1/2\), and direct integration of the split-simplex region followed by Vandermonde's identity gives the displayed leading constant. Independent exact enumeration reproduced the construction and approached the predicted constants for one- and two-prime supports.

Checked sources: Assigned RESULT.md and inspected verifier source; Yiu, Recreational Mathematics, section 6.2 full PDF page; OEIS A120089/A120090; Independent exact support enumeration and asymptotic spot checks.

Residual correctness risks: The Weyl step is asymptotic and analytic; finite counts only corroborate it.; The count is for primitive triangles up to leg interchange, not distinct perimeter values..

## Originality

**PASS** — Yiu's full section 6.2 gives exactly the square-perimeter normal form and initial examples, and OEIS records the resulting perimeter sequences. Neither inspected source refines the parametrization by a prescribed finite odd-prime support, proves that every such support occurs infinitely often, or gives the support-wise logarithmic asymptotic. Resultary and targeted searches under prime-support, smooth/S-unit, and asymptotic terminology found no earlier equivalent theorem.

### Equivalent formulations

Searches/sources: Resultary query: primitive Pythagorean triangle square perimeter fixed prime support asymptotic S-unit; Yiu, Recreational Mathematics, section 6.2; OEIS A120089/A120090.

Evidence: The Resultary exact hit was the audited record. Yiu gives \(m=2U^2\), \(m+n=V^2\), \(\gcd(U,V)=1\), and the square perimeter \((2UV)^2\), but no fixed-support refinement. OEIS records values and references back to Yiu rather than the signed-log classification or asymptotic.

No equivalent fixed-support theorem was found.

### Broader coverage

Searches/sources: Searches for S-unit Pythagorean square perimeters; smooth Pythagorean triples with square perimeter; fixed number of prime factors in square perimeters.

Evidence: No inspected source provided a broader S-unit counting theorem whose specialization yields the audited explicit constant. The classical parametrization alone leaves a nontrivial coprime allocation and equidistribution problem.

No broader published coverage was located.

### Exact database or table

Searches/sources: OEIS A120089/A120090; Resultary exact theorem search.

Evidence: The OEIS entries tabulate square perimeters/root perimeters but not counts by exact support. No prior published-result entry contained the fixed-support asymptotic.

The theorem is not a table recomputation; it establishes infinitely many cases and a continuous asymptotic.

### Claim versus prior implication

Searches/sources: Can Yiu's parametrization alone imply every prescribed support occurs infinitely often?; Can the OEIS sequences imply the leading constant?.

Evidence: The parametrization must still be split by coprime allocation of each prescribed prime and by the irrational inequality \(\sqrt2\,U<V<2U\). The asymptotic requires Weyl equidistribution and a nontrivial \(r\)-dimensional polytope volume; neither appears in the prior source.

The fixed-support bijection and asymptotic are additional results rather than immediate restatements.

### Source inspections

- **Recreational Mathematics, section 6.2: Primitive Pythagorean triangles with square perimeters** — FOUNDATIONAL_PRIOR_NOT_COVERING.
  Identifier: https://web.bogazici.edu.tr/topcu/RecreationalMathematics.pdf
  Trigger: Foundational square-perimeter parametrization cited as prior input.
  Material read: Complete section 6.2 in the 360-page PDF, including the derivation \(m=2q^2\), \(m+n=p^2\), coprimality/range conditions, and examples.
  Method: lawful open-access full text
  Evidence: It supplies the normal form but not prime-support allocation, infinitude for arbitrary prescribed support, or the counting theorem.
- **OEIS A120090** — DATABASE_CONTEXT.
  Identifier: https://oeis.org/A120090
  Trigger: Current sequence reference for square roots of square perimeters.
  Material read: Complete public sequence entry and links to Yiu.
  Method: public database
  Evidence: The sequence records values from the classical parametrization and does not state the fixed-support classification or asymptotic.

Residual originality risks:
- Because the normal form is elementary and old, a fixed-support refinement could exist in recreational or problem literature under terminology not indexed by modern searches.

## Scientific value

**PASS** — Prescribing the complete prime support is a natural arithmetic refinement of the classical square-perimeter family. The theorem gives an exact bijection, proves every finite odd-prime support occurs infinitely often, and derives a closed asymptotic whose constant separates support size from the individual prime logarithms. This is a meaningful structural/counting result, not a finite census.

Residual value risks: The result counts triangles rather than distinct perimeter values, and does not study secondary terms..

## Final assessment

The final claim survives unchanged on correctness, originality, and scientific value. No change to `RESULT.md` or `SLOGAN.txt` is proposed.

Earlier review evidence remains separately identified and is not relabeled as this independent assessment.

This is a best-of-knowledge mathematical audit, not formal proof-assistant verification or a guarantee against undiscovered prior art.
