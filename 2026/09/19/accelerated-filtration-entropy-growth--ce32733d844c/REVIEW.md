# Review: Accelerated filtrations decouple algebraic entropy from affine growth

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

PASS.

For A=k[x] and V_n consisting of polynomials of degree at most q^n, multiplicativity follows from q^m+q^n <= q^(m+n) for q>=2 and m,n>=1. The successive quotient dimensions are exactly (q-1)q^(n-1), so the algebraic entropy is log q, whereas GKdim k[x]=1 and the intrinsic growth is polynomial. This directly contradicts the unrestricted positive-entropy implications in arXiv:2609.18144v1.

The universal acceleration construction is also purely formal: starting from any standard finite-dimensional generating filtration S_m of an infinite-dimensional affine algebra, recursively choose a superadditive index sequence r_n whose dimension jumps exceed exp(n^2). The reindexed filtration V_n=S_{r_n} remains multiplicative and exhaustive, while its entropy limsup diverges.

The repair theorem was stress-tested against the same reindexing mechanism. If V_n is contained in S_{Cn}, positive entropy yields an exponential lower bound on dim S_{Cn} along a subsequence. Submultiplicativity of dim S_n gives existence of the exponential growth rate, forcing it above 1. Exhaustivity gives the reverse linear comparison S_n subset V_{pn}. The classical sufficient condition that gr_F A be finitely generated implies such linear control by lifting finitely many homogeneous generators.

## Originality

PASS, qualified to the best of our knowledge.

The current arXiv:2609.18144v1 was inspected at the definitions and Theorems 3.7, 3.9, 3.14, Corollary 3.15, and the Leavitt path application. Its broad statements quantify over arbitrary finite-dimensional filtrations, and no accelerated-filtration exception is stated.

The 2024 paper introducing the filtered algebraic entropy was inspected in its filtration-comparison section. It proves that linear reindexing multiplies a nonzero entropy and explicitly remarks that its results might suggest zero entropy persists across filtrations; it does not provide the nonlinear k[x] construction or the universal acceleration theorem stated here.

Classical filtered GK theory is not an originality claim. Krause--Lenagan Proposition 6.6 is cited by the 2026 source, and accessible later literature quoting that proposition explicitly includes finite generation of the associated graded algebra. That standard hypothesis explains the failure of the unrestricted restatement.

Targeted searches for accelerated/reindexed filtrations, polynomial-ring positive entropy, and arbitrary-filtration algebraic entropy did not locate the counterexample family or the universal acceleration theorem. The principal residual risk is older re-filtering literature, particularly Bueso--Gómez-Torrecillas--Lobillo (2001), which predates this entropy definition and could contain an equivalent filtration-growth observation in different language. Its abstract and bibliographic description were inspected, but not the full article. The Krause--Lenagan book itself was not directly inspected; the relevant hypothesis was corroborated through accessible works quoting Proposition 6.6. These access limitations do not affect the elementary counterexample proof but leave residual terminology-level originality uncertainty.

## Value

PASS.

The result identifies a missing hypothesis in a central recent claim connecting algebraic entropy to GK and exponential growth. The k[x] family is minimal, explicit, and gives arbitrarily large finite entropy on the same polynomial-growth algebra. The universal acceleration theorem shows the issue is structural rather than exceptional: unrestricted finite-dimensional filtrations can manufacture entropy independently of intrinsic growth. The linear-control repair isolates a natural regime in which the intended implication is valid, while also showing that the recent paper's standard-filtration Leavitt path PI criterion is not challenged by this correction.

## Limitations

This record does not claim that finite generation of the associated graded algebra is necessary for every valid entropy-growth implication; it is a classical sufficient hypothesis, while linear domination by a standard filtration is a more flexible sufficient condition. No independent validation is asserted. The originality claim is restricted to the entropy counterexamples and acceleration theorem, not to classical filtered--graded GK theory.
