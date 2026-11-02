# Scientific review: sparse labeled coupon recovery crossover

## Correctness (PASS)

The finite incidence-signature criterion is exactly the one established in Tan et al., arXiv:2610.32251v1. The proof separates uncovered signatures from duplicate nonzero signatures. Zero-count factorial moments converge for every permitted sequence of group sizes; the exact nonzero-pair expectation vanishes at the \(c=0\) boundary. For \(0<c<\infty\), the fixed-row-size hypergeometric law is multiplicatively \(1+o(1)\)-close on any fixed family of signatures to an independent Bernoulli-row model, since \(t/k_n=O(\log^3 n/n)\). In that model the nonzero word masses have second moment of order \(n^{-2}\) and every higher fixed moment \(o(n^{-h})\); factorial-moment graph enumeration yields independent Poisson zero and nonzero-twin counts. The two recovery-time formulas follow from the exact incidence criterion. The proof's normalization, integer time rounding, boundary \(c=0\), and the no-within-draw-replacement assumption have been explicitly checked. The finite verifier reproduced 57,768 exact-state/rational assertions. Its large-\(n\) evaluations are illustrative and not used to certify limits.

## Originality (PASS, bounded historical assessment)

The identified LCCP sources give the sample model, deterministic distinguishing criterion, finite Markov computations, and fixed-pair expectations, not this joint critical sparse-group distribution. The new statement is the \(k_n\sim cn/\log n\) onset of nonzero twin signatures with independent Poisson intensity \(\tfrac12(e^c-1)e^{-2x}\) and its precise effect on both full-recovery laws. The 2025 Barak-Pelleg–Berend fixed-\(k=2\) expectations do not imply this nonzero-twin component. General birthday-collision arguments are conceptually relevant, but a typical iid-column result does not by itself cover the dependent fixed-size row model without the multiplicative deconditioning proof. Searches of accessible mathematical records and the identified primary literature produced no directly covering formula. Historical random separating systems or nonuniform occupancy results remain a priority risk; the search cannot establish universal priority.

## Mathematical value (PASS)

The inference problem has two distinct operational versions, known and unknown label alphabets. At the critical group-size scale the ordinary coupon-covering approximation misses a positive-probability obstruction caused by **nonzero** duplicate incidence histories. The exact limiting laws separate these mechanisms, quantify their dependence on sampling density, and capture a real transition between vanishing and persistent extra ambiguity. This is a motivated sharp distributional boundary rather than a numerical exercise, arbitrary parameter slice, or restatement of deterministic separation.

## Scope, closest literature and limitations

The result assumes independent uniform fixed-cardinality draws and \(p_n=k_n/n\to0\), \(p_n\log n\to c<\infty\), with no independent-audit claim. It does not cover constant sampling density, \(c=\infty\), or convergence-rate bounds. Closest primary sources: Berrebi et al., arXiv:2502.02968v1; Tan et al., arXiv:2507.15231v1; Barak-Pelleg and Berend, arXiv:2510.23249v1; Tan et al., arXiv:2610.32251v1. Older classical deterministic separating-system papers do not state the inspected stochastic law; broader unsurveyed random-code and occupancy theory is the main residual risk.

Self-review: passed. Independent audit: not yet performed.
