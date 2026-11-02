# Review: sharp exponential obstruction width

## Correctness (PASS)

The theorem uses the standard splitting semantics, which is equivalent to coverage by one coordinate-value slice per variable. An induction gives finite failing subteams even for infinite alphabets and infinite teams. Minimality supplies one slice-covering tuple for every deleted assignment; evaluations of their coordinate-product polynomials form an invertible diagonal matrix. Because the polynomials lie in a \(2^m\)-dimensional multilinear space, there are at most \(2^m\) assignments. The full Boolean cube is minimally failing and attains equality. Boundary cases include \(m=1\), empty teams, extra unused variables, and nonempty arbitrary domains. Standalone enumeration and cube-witness checks agreed with the proof; those checks are limited to stated finite parameter ranges.

## Originality (PASS within inspected evidence)

The closest explicit statement is Corollary 23 of Fröhlich–Kolaitis–Meier, *Disjunctions of Two Dependence Atoms* (arXiv:2508.16146; CSL 2026), proving the \(m=2\) special case. The more recent Barlag et al. *Aspects of Coherence in Dependence Logic* (arXiv:2605.31269), Theorems 27–28, does use multi-constancy-atom disjunctions but only for lower-bound/undecidability reasoning, not the exact all-\(m\), unbounded-domain upper bound. Its trivial cardinality bound for binary propositional teams does not imply a uniform domain-independent bound. Semantic searches of published records and the inspected primary text found no covering statement. A broader older polynomial-interpolation or axis-parallel-cover theorem might imply the result without using dependence-logic terminology; historical priority remains uncertain and requires independent specialist review.

## Mathematical value (PASS)

This is an exact natural invariant, not a chosen sample size: it gives a sharp finite obstruction theorem for every arity and every alphabet, replacing an unspecified existence bound with a uniform exponential formula. The dimension-free local certificate and explicit extremal teams can be used when translating multi-disjunction semantic conditions into finite first-order obstruction tests. The proof also distinguishes the domain-independent result from trivial bounded-alphabet pigeonhole arguments. No claim is made for arbitrary functional-dependence atoms.

## Boundaries and independent work

The invariant is stated using all subteams of size **at most** the threshold; some smaller failing teams exist. The proof and checker are available in the artifact package. Published two-atom results are credited as prior work. Independent mathematical and historical-priority assessments have not been performed.

Self-review: passed. Independent audit: not yet performed.
