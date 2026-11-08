# Independent mathematical audit

## correctness

PASS

The spacing-aware greedy arch argument is bidirectional: every k-arch word embeds any k-target greedily (the next start is ≥e_j+s); choosing each arch terminal symbol forces any greedy pattern prefix to end at e_j and the incomplete suffix misses some letter, so k+1 cannot embed. Unique arch/spacer/terminal decomposition yields I_q(z) for missing-letter tails, F_q(z)=q!z^q/∏_{1≤j<q}(1−jz) for minimal full-letter arches, and T_{q,s}(z)=Σ_{0≤r<s−1}(qz)^r+(qz)^(s−1)I_q(z). Hence I_q+uF_qT/(1−u(qz)^(s−1)F_q), binary rational reduction, and minimal length qk+(s−1)(k−1) with exactly (q!)^k q^((s−1)(k−1)) hosts. Independent literal small-host enumeration checked q=2..3 and spacings including s≥2.

## originality

PASS

PASS for s≥2 complete indexed-word universality spectra and shortest-host classification; s=1 expressly prior.

## value

PASS

Positive minimum spacing is a natural constrained subsequence model; deriving its complete bivariate index spectrum and exact shortest hosts for all alphabet sizes and spacings supplies usable enumerative and algorithmic benchmarks beyond a yes/no matching test.

The dated certificate retains the supplied scientific assessment, sources and limitations.
