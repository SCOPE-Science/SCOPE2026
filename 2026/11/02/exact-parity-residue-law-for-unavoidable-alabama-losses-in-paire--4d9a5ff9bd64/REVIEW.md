# Independent mathematical audit

## correctness

PASS

Reassessed the replacement RESULT.md in repairs/4. The frozen count defined E and O only for l≤u but uses them on empty intervals (a=1,b=2 gives l_e=4,u_e=3, and l_o=2,u_o=1). The replacement defines both for all integer endpoints, with the displayed positive parts giving zero on empty intervals. It computes the full set of possible small-pair totals at both parities, including x=0, x=1/2, every cross-pair tie and quota wrap. No individual loss is possible for some allocation pair exactly when the small-pair total can change by 0 or 1: the large-pair total then does not fall, and equal-pair symmetry lets residual recipients nest when base quotas are unchanged; a base-quota increase already protects both members. The two parity comparisons give the stated strict intervals and explain why neither endpoint forces a loss. The orbit count follows from gcd(a,P)=1 for a odd and gcd(a,P)=2, a+b odd for a even. Each parity interval has real length (b−a)/2, and endpoint and parity errors are uniformly bounded. The minimality checks exhaust the primitive pairs with a+b≤5 and rule out h=1,2 analytically. A fresh independent exact-integer enumeration of all Hamilton allocations and both tie resolutions for all primitive 1≤a<b≤20 over one joint period matched the transition and count laws on 127 profiles and 5,232 transitions. The independent finite check does not replace proof; the frozen verify.py was inspected, not run.

## originality

PASS

For the corrected result, the distinct content is the exact rational four-constituency transition classification with both ties quantified, and its period count. The strongest exact indexed analogue is genuinely three-state and uses a different tie restriction. The standard general probability theorem has a rational-independence hypothesis, and a general periodicity observation alone leaves the two intervals and their sampling by residue orbit undetermined.

## value

PASS

The two-pair family naturally has systematic ties and rational remainders, outside the usual general probability theorem. Exact size-by-size inevitability answers a stronger operational question than showing a selected tie break can lose a seat. The two windows, count and sharp small witness resolve this degeneracy, and the positive limiting frequency shows that the phenomenon is not confined to isolated examples.

The dated certificate retains the supplied scientific assessment, sources and limitations.
