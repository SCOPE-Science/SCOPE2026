# Independent mathematical audit

## correctness

PASS

For the repaired finding only. The frozen Finding's eighth power is false: it is 3ω²+2, as in the later proof. More materially, the frozen tuple sums to 2b and so is not in the ideal of (x−1)(x−α) for b≠0; its verifier enumerates that tuple without testing cyclic-code membership. The repair derives the actual coefficients of ag+bxg, and identifies an invertible base-field coordinate map taking the printed tuple to them, which explains why the frozen counts survive. The quartic forces order 32 and ord_32(7)=4 proves irreducibility. α²=−1 implies F_7(α)=F_49. For affine t the span is that of 1,tα,t−α: rank ≤2 iff t∈F_49, rank 1 iff t=α, and infinity has rank 2. A rank-three line and the base-field zero-sum hyperplane give M_2=3 by Frobenius closure. The separately written repairs/3/artifacts/verify.py replayed all 2402 points from g,xg, tested both roots on each representative, and gave (1,49,2352), with the expected ordinary counts. The repaired publication files and unchanged verification JSON front matter were inspected; no external attestation or formal verification is claimed.

## originality

PASS

Pass for the narrowed double correction of Example 4.25 only. The frozen claim that the ordinary rank spectrum is an uncovered contribution does not survive comparison: it follows from the published MacWilliams identity and the explicitly enumerated length-three comparator. The repaired text credits that implication and retains the numbers as a check. The primary text inspected still contains both defects; no equivalent correction was established in the indexed comparisons.

## value

PASS

The surviving finding makes a named construction reproducible: the printed primitive element cannot exist and directly implementing the printed tuple creates a different subspace not in the stated cyclic ideal. Corrected generators and a rank isometry recover the example and explain why its rank conclusions remain usable. The independently checked spectrum is not counted as a new contribution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
