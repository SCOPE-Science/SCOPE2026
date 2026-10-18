# Independent mathematical audit

## correctness

PASS

Starting from Wang Prop.3.17, put P=prod_i a_i, q_I=prod_{i not in I}a_i, S_I=sum_{i in I}a_i. Its term equals S_I/P+(|I|-3)/q_I. For full I=A of size n+1, theta_A=S/P+n-2. For proper admissible I (|I|>=4), all positive weights give S_I<S, |I|<=n, q_I>=1, so theta_I <= S_I/P+n-3 < theta_A. Thus the full stratum uniquely maximizes for n>=3, yielding global hyperbolicity at the same strict m>n-2+S/P threshold as the off-boundary Prop.3.11. For P(1,1,2,3,5), n=4, P=30, S=12, threshold 12/5, so integral m>=3. Uses Wang hypotheses and sufficiency only; not claiming necessity or nonisolated singularity extension.

## originality

PASS

Direct comparison of Wang full primary arXiv HTML propositions 3.11, 3.17 and corollary 3.18 finds the ambient value already as an off-boundary bound, the global bound left as a maximum over strata, and only a special P(1,...,1,r) evaluation in the corollary. The strict all-weight equality is not stated in accessible source; although algebra elementary, the global-improvement implication requires showing ALL strata dominated. Best-of-knowledge not indexed elsewhere.

## value

PASS

Evaluates the controlling maximum of a general geometric hyperbolicity theorem, proving that no toric stratum ever raises the sufficient degree threshold in the full isolated-singularity class. This upgrades an off-boundary result to a global result uniformly in all weights, including the previously off-boundary-only P(1,1,2,3,5) example; the substantive geometric consequence, not the one-line algebra alone, motivates the claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
