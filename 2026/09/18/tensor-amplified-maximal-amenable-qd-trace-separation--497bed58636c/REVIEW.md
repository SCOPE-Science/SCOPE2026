# Same-model review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

The proof was checked at the level of the two nontrivial permanence steps.

First, conditioning a quasidiagonal trace on a projection in a commuting tensor
factor preserves quasidiagonality. The argument uses a quasidiagonal u.c.p.
approximation, replaces the approximate image of the projection by its spectral
projection at \(1/2\), compresses the other tensor factor to that spectral
subspace, and normalizes the matrix trace. The denominator converges to the
positive mass of the conditioning projection, while approximate multiplicativity
controls both the spectral compression and the compressed products.

Second, the exact distance formula is forced by the sector projection itself.
Every quasidiagonal trace on the \(r\)-fold tensor power has mass \(2^{-r}\) on
each word projection, giving the lower bound with the norm-one observable
\(2E_\omega-1\). The quasidiagonal product trace
\(\lambda^{\otimes r}\) attains the same bound because its complementary
component is supported on \(1-E_\omega\). No compactness or attainment argument
for the quasidiagonal trace set is needed.

For the infinite tensor power, restriction of a quasidiagonal trace to each
finite tensor stage remains quasidiagonal. The resulting lower bounds
\(2(1-2^{-r})\) tend to the universal state-space diameter \(2\). Amenability of
the product trace follows from the standard tensor-product approximation and
finite-stage slice-map argument.

## Originality

The claim is qualified **to the best of our knowledge**.

Moradi's arXiv:2609.18793 was inspected at the theorem and proof level. It proves
the two-sector balance
\(\rho(e^0)=\rho(e^1)=1/2\) for every quasidiagonal trace and constructs the
sector traces \(\mu_0,\mu_1\), but it does not state a tensor-power amplification
or a norm-distance formula. Searches for combinations of quasidiagonal traces,
amenable traces, tensor powers, dual norm distance, maximal distance, and
distance \(2\) did not locate a prior statement equivalent to the result here.

The largest prior-art risk is general permanence theory for quasidiagonal and
amenable traces, especially Brown's 2006 memoir and later work on
finite-dimensional approximation. Such results may subsume the compression or
tensor-product lemmas. The claimed contribution does not rely on those
permanence lemmas being new; it is the sector amplification and the exact
formulas
\[
2(1-2^{-r})\quad\text{and}\quad 2
\]
for distance from the entire quasidiagonal trace set.

No inaccessible source was found whose title or available description gives
specific evidence for this exact tensor-amplified metric statement. General
older trace-permanence literature was not exhaustively inspected theorem by
theorem, so equivalent formulations there remain a residual originality risk.

## Value

Moradi's example establishes that quasidiagonal traces need not form a face.
The present result measures how severe that failure can become. Finite tensor
powers stay in a concrete separable unital RFD setting while the amenable
non-quasidiagonal component moves to exact distance
\(2(1-2^{-r})\) from every quasidiagonal trace. The spatial infinite tensor
power reaches the maximal possible state-space distance \(2\).

The mechanism is reusable: a rigid finite sector distribution for all
quasidiagonal traces propagates to product sector distributions under tensor
powers through conditional compression. This converts a qualitative facial
obstruction into a quantitative separation principle.

## Scope and limitations

The infinite tensor product is not asserted to be RFD, and no exactness,
nuclearity, UCT, or simplicity statement is made. The result is specific to
settings with a rigid sector-mass theorem and does not claim a universal
amplification theorem for every nonfacial quasidiagonal trace set.
