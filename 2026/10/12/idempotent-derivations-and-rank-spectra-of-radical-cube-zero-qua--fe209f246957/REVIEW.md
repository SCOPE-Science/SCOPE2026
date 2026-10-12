# Scientific review: idempotent derivations of cubic-truncated quantum exterior algebras

## Correctness — PASS
In the algebra specified in RESULT.md, the basis is \(1\), the \(n\) generators, and the \(\binom n2\) ordered quadratic products. Since \(c_{ij}\notin\{1,-1\}\), differentiating the skew relations kills scalar generator terms, while differentiating the square relations kills off-diagonal linear terms. All and only diagonal linear plus quadratic generator images define derivations. The equations for \(D^2=D\) then force the stated subset support conditions and exact free-quadratic-coefficient counts. Explicit quadratic shears conjugate admissible forms to diagonal representatives. Square-zero linear combination constraints on generator images force every automorphism's degree-one matrix to be monomial; its permutation must preserve the complete ordered commutation matrix. The proof covers arbitrary fields, not merely the checked finite cases. The Python verifier enumerates all possible n=2 generator images including scalars over \(\mathbb F_4\) and \(\mathbb F_5\), checking every Leibniz equation and rank. It independently recomputes spectra for \(2\le n\le6\) over \(\mathbb F_4,\mathbb F_5,\mathbb F_7\).

## Originality — PASS, with bibliographic risk
The nearest primary work is Jin–Zhang (arXiv:2208.05687), which establishes the quantum-exterior/complete-intersection setting and analyzes Frobenius coalgebras and Hopf behavior, but does not assert the composition-idempotent derivation problem. Grimley's quantum-complete-intersection Hochschild calculations (arXiv:1606.01727) and Bergh–Erdmann–Jorgensen's constant-Jordan-type work (arXiv:1910.06714) are relevant yet concern respectively cohomological classes and module multiplication ranks. In the inspected full text, none entails the cubic quotient's shear-conjugacy orbit theorem or its complete labeled rank polynomial. Search coverage is necessarily incomplete; a formulation involving gradings or derivation projectors could duplicate some or all of the theorem.

## Value — PASS
Classification of composition-idempotent derivations records algebra-compatible linear projections. The result yields a uniform formula and complete orbit invariant for arbitrarily many generators over every admissible field, with striking characteristic-two proliferation of rigid normal forms and parameter-independent rank multiplicities. Its quadratic-shear parametrization and parameter-preserving permutation group are structural, not a numerical special case. The result does not claim any broader downstream theorem.

## Scope and limitations
The proof depends on \(c_{ij}\ne1,-1\) and cubic truncation. The checker is finite corroboration only, and the originality conclusion is conditional on inspected published sources. Independent scientific audit remains unperformed.

Self-review: passed. Independent audit: not yet performed.
