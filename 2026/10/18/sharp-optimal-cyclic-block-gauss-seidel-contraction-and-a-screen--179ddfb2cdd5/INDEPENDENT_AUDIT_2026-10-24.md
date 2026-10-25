# Independent mathematical audit

## correctness

PASS

The exact block minimization identity gives expected loss (Ge)^T B_p(Ge) and worst-case generalized Rayleigh minimum. G1=(1−2t)1 makes the constant-error quotient the same ℓ_q=(1−2t)1_q^T T_q^{-1}1_q/n for every fixed p, hence universal upper bound on Λ(p). For uniform p, each block update I−E_j T_q^{-1}E_j^TG is entrywise nonnegative since T_q^{-1}≥0 and off-block G couplings are nonpositive. Their average is circulant, symmetric and has constant row sum 1−ℓ_q, therefore Perron spectral radius equals 1−ℓ_q and the minimum energy-decrement eigenvalue equals ℓ_q. Solving Dirichlet recurrence T_q z=1 with zero artificial boundaries yields the stated hyperbolic sum. The qα→s crossover follows by explicit small-α limits with q<n. Independent tests at all 105 triples n=3..9, 1≤q<n, t in {1/8,.35,.48} checked numerical eigenvalue, Green sum, closed hyperbolic formula and nonnegative mean update to 6e−16. These finite tests do not establish the universal result.

## originality

PASS

The actual prior inverse-positive single-coordinate sampling theorem optimizes p for q=1 over a broader SPD Stieltjes class; here q is arbitrary and blocks are overlapping cyclic intervals with a separate exact closed contraction and screened crossover. Full relevant parts of Xie–Yang's randomized batch-selection paper and the published coordinate-sampling RESULT were inspected; neither supplies this sharp all-distribution contiguous-block result. Existing sketch-and-project framework yields a spectral optimization but not the computed optimum and scaling. Best-of-knowledge acceptance, not historical priority certification.

## value

PASS

Optimizing the sharp one-step worst-case convergence factor over all static overlapping block probabilities is a meaningful algorithm-design question. The explicit Green sum quantifies how block length and coupling correlation length trade off and gives a scaling crossover between inefficient short blocks and near-full-block sampling. These are reusable exact convergence invariants, not a routine substitution in a published table.

The dated certificate retains the supplied scientific assessment, sources and limitations.
