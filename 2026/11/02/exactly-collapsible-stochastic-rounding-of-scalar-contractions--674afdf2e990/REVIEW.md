# Scientific review

## Correctness — PASS

The claim is a full equivalence for every positive contractive scalar factor and every nonnegative integer starting state. The exact rounding kernel has the required conditional mean, which propagates as \(q^n k\). For \(q=1/b\) with integer \(b\ge2\), mapping either member of a neighboring-integer pair through division by \(b\) and stochastic rounding never produces more than the neighboring-integer pair around the new mean. Conditional unbiasedness fixes its probabilities exactly; induction proves the fixed and variable reciprocal-integer laws. Conversely, any other factor has a two-step witness with three positive support atoms, which cannot equal one stochastic rounding. The pointwise integer quadratic inequality gives sharp variance minimality; the two-point laws and zero absorption give the exact extinction formula. Boundary cases \(k=0\), integer means, and \(n=1\) are covered by the definition. The rational checker confirms finite cases but does not replace these arguments.

## Originality — PASS, qualified

The 2020 Croci–Giles paper [1] provides the unbiased stochastic rounding definition and analyzes global errors of time-stepping PDE solvers; the fixed scalar integer-lattice transition law and its reciprocal-factor iff criterion are not among its inspected results. The 2022 Croci–Fasi–Higham–Mary–Mikaitis survey [2] explains rounding modes and ODE applications without the iterated-kernel collapse criterion. Dahlqvist–Salvia–Constantinides [3] give compositional *distribution computation* for floating-point errors rather than a closed-form characterization of the time-homogeneous ideal fixed-grid contraction kernel. Related known deterministic quantized affine maps and rounded heat/stationary-flux examples do not imply this iff theorem. Searches covered synonyms including iterative, repeated, one-shot, double rounding, geometric contraction, and Markov kernels, plus published mathematical finding records. Failure to find an equivalent is not proof of worldwide priority; obscure rounding/quantization literature could contain this elementary semigroup identity. The exact deterministic and stochastic models must not be conflated.

## Value — PASS

The mathematical object is a natural one: repeated unbiased stochastic nearest-integer rounding of a scalar numerical decay update, a minimal low-precision model. The exact all-horizon distribution law is special to reciprocal-integer scales, and the converse proves no other contraction factor has the same property for every input even after two steps. This is a complete classification rather than a single isolated example. It yields minimal possible output variance at all horizons, an exact extinction-time distribution and expectation, an order-independent result for varying reciprocal divisors, and a strict \(31/6\)-fold variance-inflation witness outside the class. These quantify when replacing many stochastic roundings by one is mathematically valid, a question not answered by ordinary zero-mean error guarantees.

## Sources and residual risks

[1] Croci and Giles, *Effects of round-to-nearest and stochastic rounding in the numerical solution of the heat equation in low precision*, arXiv:2010.16225 (first public 2020-10-30), full open arXiv text inspected, especially Introduction, sections 2–4. https://arxiv.org/abs/2010.16225

[2] Croci et al., *Stochastic rounding: implementation, error analysis and applications*, Royal Society Open Science 9 (2022), 211631; full openly available HTML inspected for the rounding definition, probabilistic analysis and numerical ODE uses. https://pmc.ncbi.nlm.nih.gov/articles/PMC8905452/

[3] Dahlqvist et al., *A Probabilistic Approach to Floating-Point Arithmetic*, arXiv:1912.00867 (2019), openly available paper text inspected especially the compositional model. https://arxiv.org/abs/1912.00867

Residual risk: equivalent randomized-integer-division or Markov-kernel results may exist under different terminology. This result does not address genuine IEEE nonuniform floating-point grids or limited random-bit rounding. Independent priority and scientific audits remain to be performed.

Self-review: passed. Independent audit: not yet performed.
