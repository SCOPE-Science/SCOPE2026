# Independent mathematical audit — 2026-10-01

## Final claim assessed

Minimal prime support in arithmetic-progression Heronian triangles

## Correctness — PASS

PASS. For sides \((b-d,b,b+d)\), Heron's formula gives the exact reduction to \(b=2x\) and \(x^2-d^2=3y^2\), with area \(K=3xy\). Removing the common side gcd yields coprime \(X,Y,D\) with \(X^2-D^2=3Y^2\), \(D\) odd, and \(X,Y\) of opposite parity. Since every Heronian area here is divisible by \(6\), two-prime support forces support exactly \(\{2,3\}\). Then \(3\nmid X\), so \(X=2^A\), while coprimality forces \(Y=3^B\). If \(B\ge1\), the square equation is impossible modulo \(8\) for \(A\ge2\), and negative for \(A=1\). Hence \(B=0\), and \((2^A-D)(2^A+D)=3\) gives \(A=1,D=1\), namely the primitive \(3,4,5\) triangle. Scaling preserves exactly two area primes precisely for \(t=2^u3^v\). The bounded scan is supporting evidence only.

## Originality — PASS

PASS to the best of current knowledge. MacDougall's arithmetic-progression parameterization and Read's complete 2025 HAP treatment were both inspected in full. Read gives a complete primitive parameterization and the exact area formula, and also proves that \(3,4,5\) is the only primitive right triangle in the class, but neither source states or implies without an additional Diophantine argument that exactly two distinct area primes force the \(3,4,5\) similarity class. Published-record and targeted searches found no earlier exact prime-support classification.

### equivalent_formulations

Searches: Heronian triangle arithmetic progression area exactly two prime divisors 3 4 5; HAP triangle minimal prime support smooth area; Read 2025 On HAP triangles area formula

Evidence: Read's full article gives the primitive HAP parameterization and exact area formula but no two-prime-support theorem.

Reasoning: Prime support can be expressed through Read's parameters, but completing that reformulation requires the additional coprime and modulo-\(8\) argument in the audited proof.

### broader_coverage

Searches: MacDougall Heron triangles with sides in arithmetic progression; DOI 10.1017/mag.2025.10079; Bailey Gosnell Heronian triangles arithmetic progression

Evidence: The inspected full texts classify HAP shapes and their areas; none gives the claimed smooth-area classification.

Reasoning: A general parameterization is an ingredient, not a theorem that mechanically eliminates every other two-prime-support case.

### exact_database_or_table

Searches: OEIS A387908 HAP perimeter data; published-record semantic search for HAP area prime support

Evidence: Available enumerations list examples but do not establish the quantified all-triangle classification.

Reasoning: Finite tables cannot prove the claimed infinite exclusion; the proof supplies that step.

### claim_vs_prior_implication

Searches: Full Read 2025 Theorems 4-7 and Corollary 2; MacDougall 2003 parameterization

Evidence: The prior formulas reduce the problem to explicit coprime parameters, but the exact prime-support conclusion is not printed and is not a mere substitution.

Reasoning: The audited modular and factorization argument supplies a genuine additional implication.

## Scientific value — PASS

PASS. Minimal prime support of the integer area is a natural arithmetic invariant of a classical Diophantine family. The theorem gives a complete infinite classification, identifies a unique primitive shape, and converts a broad HAP parameterization into a sharp smoothness statement rather than reporting a bounded census.

## Source inspections

- **On HAP triangles** — https://doi.org/10.1017/mag.2025.10079. Material read: Complete 10-page primary article, including Theorems 4-7, the primitive parameterization, the area formula, and Corollary 2. Assessment: CLOSEST_FULL_TEXT_NOT_COVERING_PRIME_SUPPORT. Evidence: The paper parametrizes every primitive HAP triangle and gives its area, but does not classify the number of distinct prime divisors of that area.
- **Heron triangles with sides in arithmetic progression** — https://www.researchgate.net/publication/242732258_Heron_Triangles_With_Sides_in_Arithmetic_Progression. Material read: Full accessible article and its Diophantine parameterization. Assessment: GENERAL_PARAMETERIZATION_NOT_EXACT_COVERAGE. Evidence: It reduces HAP triangles to a quadratic Diophantine equation but does not state the audited prime-support classification.
- **OEIS A387908** — https://oeis.org/A387908. Material read: Sequence description and finite entries. Assessment: FINITE_DATA_NOT_COMPLETENESS. Evidence: The data are useful for examples but cannot establish the all-parameter prime-support theorem.

## Limitations and residual risks

The theorem is specific to integer Heronian triangles whose side lengths form a nonconstant arithmetic progression. It classifies the minimal possible area-prime support but does not classify areas having three or more distinct prime divisors.

- Older recreational-number-theory literature could contain the same smooth-area observation under different terminology, although the two comprehensive HAP sources inspected do not.

## Disposition

**passed**
