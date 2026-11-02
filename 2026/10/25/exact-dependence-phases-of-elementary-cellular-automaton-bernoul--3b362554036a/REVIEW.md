# Independent mathematical audit

## correctness

PASS

For centered radius-one output Y_i=f(X_(i-1),X_i,X_(i+1)) with iid Bernoulli p, output past i<=0 and future i>=2 share exactly input X_1. Conditional on X_1 they are independent; the covariance of any past/future cylinder events is p(1-p) times their conditional-law contrasts. For 0<p<1 true one-dependence is therefore equivalent to at least one entire side being independent of X_1, a stronger test than lag-two covariance. The four-state weighted transducer has reachable row and column spans of dimension ≤4, so conditional shielding for output words of lengths 0..3 extends to all words. Independent rational-polynomial GCD enumeration for all 256 rule truth tables checked exactly 32 all-bias one-dependent rules, 56 at p=1/2, with only fair p as an extra interior parameter. Independent symbolic pairwise polynomial analysis found exactly 42 generic lag-two-independent rules and the seven exceptional biases/counts, and seven-input enumeration confirmed Rule22 p=1/3 block gap 32/6561. Additional interleaved separated index-set tests on all 56 fair candidates showed no omitted dependence. All bias assertions rely on exact symbolic polynomial identities, not finitely chosen numeric sample biases.

## originality

PASS

Existing cellular-automata Bernoulli literature establishes invariance/preservation of uniform Bernoulli under particular surjective or algebraic/permutative rules, which gives known iid special cases but not the 256-rule all-bias one-step one-dependence census. Kari–Taati analyze Gibbs invariance and temporal randomization and Borriello–Walker transfer-entropy classes; these observables are not equivalent to conditional shielding of separated spatial output half-lines. The 32/56 phase classification, seven special pairwise biases, and explicit Rule22 false-negative were not identified in inspected primary results. However, an older CA dependence table or transducer-based classification could subsume the result; this risk persists.

## value

PASS

One-dependence of a one-step factor of iid is a canonical probabilistic property, not reducible to pairwise correlation tests. An exhaustive exact classification across a standard finite 256-rule family identifies a unique exceptional fairness phase and striking seven different algebraic pairwise resonances; the Rule22 block witness sharply explains how pairwise independence can conceal true sigma-field dependence. The result is a motivated complete classification, not a statement about temporal iteration or general finite-range factors.

The dated certificate retains the supplied scientific assessment, sources and limitations.
