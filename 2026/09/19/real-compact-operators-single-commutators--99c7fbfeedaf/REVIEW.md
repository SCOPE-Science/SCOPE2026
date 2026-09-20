# Same-model review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

The proof was checked by separating the genuinely field-sensitive steps from
the block-operator estimates that are algebraic over either field.

The real diagonal-balancing lemma is self-contained. The greedy permutation
forces partial sums to zero while preserving opposite signs at each rotation
step. The two-dimensional rotation is valid for a general real operator because
only the quadratic form \(x\mapsto\langle Rx,x\rangle\) and invariance of the
finite-dimensional compression trace are used. The residual subspace has
codimension at most one, and any residual unit vector has zero quadratic value
because the residual partial sums converge to zero.

For non-trace-class compacts, the sparse compression error
\(PT+TP-PTP\) is trace class. If the symmetric part of the remaining compression
is not trace class, the displayed \(2\times2\) similarities place divergent
positive and negative mass on a chosen diagonal. If the symmetric part is trace
class, the skew-adjoint part is not; its standard real two-dimensional spectral
blocks and the displayed shear produce diagonal pairs \((-s_n,s_n)\). Trace-class
perturbations have absolutely summable diagonals, so they cannot remove the two
divergences. The similarity bounds are uniform.

The zero-diagonal factorization in Liu's argument uses a dimension-free
trace-zero matrix commutator estimate, scalar-separated Sylvester equations,
Neumann series, compact block truncations, and norm estimates. Tran's 2026
theorem supplies the required matrix estimate over \(\mathbb R\) with an
absolute constant; the other displayed operations preserve the real field.

For trace-class operators, the zero-trace case follows directly from the
balancing lemma. The finite-rank step is real because the Anderson block
matrices reproduced in Beltiţă--Patnaik--Weiss have real entries; tensor
amplification is field-preserving. In the nonzero-trace infinite-rank case,
Liu's trace-concentration argument remains real after replacing its
complex-polarization sentence by the observation that the symmetric part has
nonzero trace, hence a nonzero quadratic value. The subsequent idempotent,
compression, and gluing steps are real-algebraic once Tran's finite-matrix
theorem is used.

No step uses the false implication that a complex commutator representation can
simply be restricted to the real form.

## Originality

Liu's arXiv:2609.20672v1 explicitly states the theorem for separable
infinite-dimensional **complex** Hilbert space and says throughout that the
Hilbert spaces in the paper are complex. Tran's arXiv:2609.20161v1 explicitly
proves the dimension-free finite-matrix bound over both \(\mathbb R\) and
\(\mathbb C\).

Searches for the exact statement and synonymous formulations involving
"real Hilbert space", "real compact operators", "single commutator", "commutator
of two compact operators", Pearcy--Topping, zero-diagonal similarity, and the
two recent arXiv identifiers did not locate an existing all-compact real-Hilbert
theorem. The current SCOPE archive was also searched by these objects and claim
families and no overlap was found.

The Anderson rank-one construction and zero-diagonal methods are prior art and
are not claimed as new. The novelty claim is limited to the real-field
all-compact theorem with a dimension-free square-root factor bound and the
field-preserving reduction supplied above.

### Residual prior-art risk

The full text of Fan--Fong (1987), *Operators similar to zero diagonal
operators*, was not inspected here; the bibliographic record and Liu's description
were inspected. It is the older source most plausibly capable of containing a
real-field zero-diagonal statement relevant to the reduction. Fan's 1984 paper
on diagonals was likewise not fully inspected. Anderson's 1977 original article
was not inspected in full, but the later Beltiţă--Patnaik--Weiss paper was
inspected at the explicit rank-one block construction and shows real
coefficients.

Older real-operator and real-Banach-algebra commutator literature could use
different terminology, so first-discovery certainty is not asserted. No source
found in the searches stated the full theorem proved here.

## Value

The result closes the field gap left by the new complex solution: the real
compact-operator algebra on an infinite-dimensional real Hilbert space also has
commutator width one, with the same \(\|T\|^{1/2}\) scaling for factor norms.
The proof also isolates a reusable real replacement for the complex
four-phase zero-diagonal balancing step. The distinction is meaningful because
complexification alone does not preserve a single-commutator representation in
the real form.

## Limitations

The universal constant is not optimized. Finite-dimensional real Hilbert
spaces are excluded, necessarily, because commutators have trace zero. No
stronger Schatten-ideal membership of the factors is proved, and no extension
to arbitrary real Banach spaces is claimed. The result has not received
independent audit.
