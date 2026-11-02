# Mathematical review

## Correctness

**PASS.** The defining floor recurrence is equivalent to the divisor recurrence (1). Every omitted term in the finite difference vanishes unless its divisor divides the index; the remaining factor is exactly \(2n/d-1\). The parity proof is induction using the classical divisor sum of \(\mu\), valid even for prime powers. On squarefree inputs, coefficient extraction in the finite square-zero algebra is exact, the constant terms being units. The last full-support term cancels, giving the claimed proper-subset sum. Positivity separates squarefree composites from the value \(-1\), while the parity argument excludes all nonsquarefree composites. The attached integer checker independently compares recurrences and finite specializations; it is not treated as an infinite proof.

## Originality

**PASS on the available record; historical-priority uncertainty remains.** Andrews, Kauffman and Sahoo (arXiv:2609.25628v1, 2026-09-22) explicitly supply the generalized recurrence, its divisor version, and values at prime squares and two-distinct-prime products. They introduce power kernels. Their stated primality equivalence is stronger in wording than the quantified converse actually established in their proof, which is an identity-in-the-kernel assertion. Crucially, it does not give the present **exact arbitrary-squarefree evaluation** in geometric moments, and its published two-prime case does not evaluate three or more distinct prime factors. A prior exact theorem for the same quadratic kernel provides the sharp zero tail \(a(2^h m)=0\) for odd \(m\) once \(h\ge\Omega(m)+3\), including the last nonzero dyadic boundary, and expresses the sequence through an implicit Dirichlet inverse; it neither evaluates unrestricted squarefree inputs nor supplies the moment-polynomial and parity-derived prime classification. A separate published observation treats the constant kernel and demonstrates that a fixed-kernel converse cannot be presumed. Searches for direct, alias and stronger-formula coverage found no equivalent expression; this is not a proof of absolute novelty. A previously indexed or differently named equivalent remains possible.

## Mathematical value

**PASS.** The source motivates understanding power-kernel recurrences, yet all-index prime recognition for a *fixed* nonlinear kernel requires information absent from the source's universal symbolic argument. The theorem evaluates the function on every squarefree integer by a positive combinatorial polynomial indexed by prime subsets, gives exact signs and nontrivial magnitude bounds for any number of prime factors, and combines these with a global parity invariant to settle the quadratic kernel's prime criterion. This is a structural extension beyond substitution into the known two-prime formula.

## Scope and limitations

The squarefree formula is not claimed for repeated prime factors. The parity assertion alone controls nonsquarefree inputs sufficiently for the stated primality consequence. The verifier exhausts only finite ranges. No independent audit or independent priority adjudication has been conducted.

Self-review: passed. Independent audit: not yet performed.
