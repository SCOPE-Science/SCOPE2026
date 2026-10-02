# Independent audit — 2026-10-01

## Final claim

For the radical-cube-zero linear Nakayama algebra \(A_n/J^3\), the Coxeter matrix is periodic exactly outside dimensions congruent to \(9\) or \(11\) modulo \(12\), with the exact periods stated in RESULT.md; in the two exceptional classes eigenvalue \(1\) has the unique nontrivial two-by-two Jordan block.

## Correctness — PASS

The odd-dimensional Coxeter-polynomial formulas follow from the six-step recurrence, and the exceptional residue classes have eigenvalue \(1\) of algebraic multiplicity two. Solving \((C_n+C_n^T)v=0\) gives a one-dimensional eigenspace in residues \(9\) and \(11\) modulo \(12\), so the repeated root produces one nontrivial Jordan block and infinite order. In the other odd classes the polynomial is squarefree and the surviving primitive roots give the stated exact periods. For even dimension the derived-equivalent tensor-product model is diagonalizable and the eigenvalue ratios force divisibility by \(2\), \(3\), and \(n/2+1\). A fresh exact-rational replay for dimensions \(3\) through \(15\) verified every predicted finite order and the first exceptional Jordan defects.

Checked sources:
- J.-A. de la Peña, Algebras whose Coxeter polynomials are products of cyclotomic polynomials, Algebras and Representation Theory 17 (2014), arXiv:1310.1557.
- J.-A. de la Peña, Cyclotomic and Littlewood Polynomials Associated to Algebras (2019), DOI 10.5772/intechopen.82309.
- M. Marczinzik, Periodics of Coxeter matrices for truncated Nakayama algebras, MathOverflow question 369054 (2020).
- Published-record semantic search for radical-cube-zero linear Nakayama Coxeter periodicity and exact periods.

Residual risks:
- The bounded replay is corroborative; the infinite classification rests on the displayed recurrence, root-order, and kernel arguments.

## Originality — PASS

Best-of-knowledge originality passes. The primary de la Peña sources prove cyclotomicity and supply the recurrence and even-dimensional derived-equivalence ingredients, but cyclotomicity alone does not imply finite order. The 2020 problem explicitly asks for the exact periodicity classification after those results, and the published-record search returned no earlier theorem with the residue-class classification and exact periods.

### Equivalent formulations

Searches:
- Resultary semantic query: radical cube zero linear Nakayama Coxeter matrix periodicity exact period Jordan block modulo 12
- MathOverflow question 369054

Evidence:
- The only exact published-record hit was the assigned finding.
- The 2020 question asks which matrices are periodic and for their exact periods.

Reasoning: Equivalent formulations include finite order of the Coxeter transformation, semisimplicity of its cyclotomic spectrum, and a Jordan obstruction at eigenvalue \(1\); the searched prior material did not identify the full equivalence classification.

### Broader coverage

Searches:
- de la Peña arXiv:1310.1557
- de la Peña 2019 cyclotomic-polynomial chapter

Evidence:
- The 2014 and 2019 sources cover cyclotomic Coxeter polynomials for the same radical-cube-zero Nakayama family and give the even tensor model and recurrence.
- They do not establish that every cyclotomic Coxeter matrix is semisimple or finite order.

Reasoning: The prior results are broader on cyclotomicity but weaker on the property at issue; the audited Jordan calculation is exactly what separates finite from infinite order.

### Exact database or table

Searches:
- MathOverflow question 369054 and its cited computed-period sequence
- Resultary exact-topic query

Evidence:
- A finite table of periods was acknowledged in the open problem, but no general formula/proof was located.
- No exact published database theorem covering all dimensions was found.

Reasoning: A finite table can suggest the congruence pattern but does not imply the infinite classification or the unique Jordan-block statement.

### Claim versus prior implication

Searches:
- de la Peña 2014/2019 statements versus the audited theorem
- 2020 open question

Evidence:
- Cyclotomicity puts all eigenvalues at roots of unity but does not control nontrivial Jordan blocks.
- The open question postdates the cyclotomicity work and still asks the exact finite-order problem.

Reasoning: The audited theorem is not a mechanical corollary of the known cyclotomic-polynomial formulas; semisimplicity and exact root orders must be established separately.

### Source inspections

- **Algebras whose Coxeter polynomials are products of cyclotomic polynomials** — Covers cyclotomicity and structural ingredients, not exact finite order. Material read: Full primary preprint, including the radical-cube-zero examples and tensor-product discussion. Evidence: The paper treats the Coxeter polynomials as cyclotomic; finite order would additionally require semisimplicity.
- **Cyclotomic and Littlewood Polynomials Associated to Algebras** — Supplies ingredients used by the proof but not the periodicity classification. Material read: Relevant full-text sections containing the derived-equivalence model and six-step recurrence. Evidence: The exposition identifies the even tensor model and recurrence and concludes cyclotomicity.
- **Periodics of Coxeter matrices for truncated Nakayama algebras** — Strong evidence that the exact classification remained open in 2020. Material read: Complete question and the listed finite data. Evidence: It asks, for fixed truncation exponent, which dimensions are periodic and what the exact period is.

Checked sources:
- J.-A. de la Peña, Algebras whose Coxeter polynomials are products of cyclotomic polynomials, Algebras and Representation Theory 17 (2014), arXiv:1310.1557.
- J.-A. de la Peña, Cyclotomic and Littlewood Polynomials Associated to Algebras (2019), DOI 10.5772/intechopen.82309.
- M. Marczinzik, Periodics of Coxeter matrices for truncated Nakayama algebras, MathOverflow question 369054 (2020).
- Published-record semantic search for radical-cube-zero linear Nakayama Coxeter periodicity and exact periods.

Residual risks:
- Older computed-period tables cited by the 2020 question were not treated as a proof of the general classification.
- A differently phrased older finite-order classification not indexed by the searched terminology remains a best-of-knowledge risk.

## Scientific value — PASS

The theorem completely resolves the first nontrivial radical-cube-zero case of a stated Coxeter-periodicity problem, gives exact periods in every finite-order class, and pinpoints a single Jordan-block obstruction showing why cyclotomicity does not suffice. This is a natural structural boundary classification.

Checked sources:
- J.-A. de la Peña, Algebras whose Coxeter polynomials are products of cyclotomic polynomials, Algebras and Representation Theory 17 (2014), arXiv:1310.1557.
- J.-A. de la Peña, Cyclotomic and Littlewood Polynomials Associated to Algebras (2019), DOI 10.5772/intechopen.82309.
- M. Marczinzik, Periodics of Coxeter matrices for truncated Nakayama algebras, MathOverflow question 369054 (2020).
- Published-record semantic search for radical-cube-zero linear Nakayama Coxeter periodicity and exact periods.

Residual risks:
- Older computed-period tables cited by the 2020 question were not treated as a proof of the general classification.
- A differently phrased older finite-order classification not indexed by the searched terminology remains a best-of-knowledge risk.

## Conclusion

The unchanged final claim passes correctness, best-of-knowledge originality, and scientific value.
