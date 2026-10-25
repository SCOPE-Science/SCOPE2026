# Scientific review of the mixed evil–odious multiplicity theorem

## Correctness — PASS
The coefficient identities follow directly from \(T(z)=(1-z)T(z^2)\). At even indices the absolute sum of two previously indexed coefficients is bounded by \(2m+1\); the ratio to \(4m+1\) reaches \(3/5\) only at \(m=1\) and is strictly lower in the other even residue class. Repeated removal of terminal binary ones preserves absolute normalized coefficient size; this determines every equality case. The indicator convolution then gives exactly \(R(n)=(n+1-C(n))/4\). This handles \(n=0\), \(n=2\), all Mersenne exceptions and all non-Mersenne indices with no finite-to-infinite inference. The executable independently checked 2049 direct mixed convolutions and 524288 recurrence cases.

## Originality — PASS within inspected evidence
The 2017 coefficient paper provides the signed series, its coefficient theory and dyadic extrema; the 2021 additive paper treats same-parity evil/odious two-sums and higher sumsets. Direct inspection of those papers and the relevant coefficient table found no statement equivalent to the sharp normalized non-Mersenne inequality, the mixed-sum density bounds, or both infinite equality classes. An exact bound could nevertheless have appeared in unindexed literature or as an unpublished observation. The normalized inequalities are not implied merely by a full-sequence global dyadic block extremum at a Mersenne position: locating the extremal *non-Mersenne normalized ratio* and classifying its equality indices require the residue and trailing-ones arguments.

## Mathematical value — PASS
For a natural, well-studied binary additive partition, the result not only classifies its zero-sum exceptions but gives a global lower multiplicity guarantee of one-tenth of all possible decompositions away from the Mersenne cases, with the exact sharp upper envelope and infinite extremizers. This supplies a quantitative, uniform additive-combinatorial fact rather than a special-value lookup or a restatement of an existing coefficient recurrence.

## Scope and residual risks
Zero is allowed as an evil summand; the positive-summand variant is not asserted. Prior results already cover definitions and many Thue–Morse coefficient properties, and publication priority is not independently established. The result has not undergone independent mathematical audit.

Self-review: passed. Independent audit: not yet performed.
