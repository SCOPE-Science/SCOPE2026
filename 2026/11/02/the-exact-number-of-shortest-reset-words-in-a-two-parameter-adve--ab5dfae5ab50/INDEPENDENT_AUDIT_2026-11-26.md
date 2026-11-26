# Independent mathematical audit

## correctness

PASS

For the stated left-to-right transitions, distinct live tokens never merge at nonzero states. Each of the k+m initial tokens needs its own kill; each cycle decreases the live high count by at most one. The exhibited word attains k+2m by clearing low positions and then rotating and killing high tokens in increasing initial order. At equality every cycle demotes one live token and does not promote a token from position k. Before cycle j, if the token originally at k-j+1 survives it has been incremented j−1 times (each cycle starts at ≤m≤k−m+1), so it occupies k and the gate kill is necessary. For sufficiency, initial low tokens ≤k−m can have advanced by at most j−1; the gate tokens with index k−r+1 for r≤j have been killed and those with r>j are still below k. A previously demoted high token starts at ≤m and can advance by at most j−2, so it lies below k since m+j−2≤2m−2≤k−1. Thus the chosen high token determines a legal rotating letter and each kill determines a unique letter. Reading the resulting string reproduces the token events, proving distinctness and exhaustion. Conditioning independent arrival times on the cycle times u_h, the distinct gate constraints have probability product u_h and the distinct subsequent kills probability product (1−u_h), giving 6^(−m). This includes m=k=1 and the tight boundary k=2m−1. Fresh independent reverse subset-graph computation, preserving parallel labeled arcs and counting shortest paths from the empty live set, verified counts 1, 4, 140, 184800, 1009008000, 15643660032000 at (k,m)=(1,1),(2,1),(3,2),(5,3),(7,4),(9,5), and 16 at the excluded (2,2).

## originality

PASS

The exact reset threshold and the existence of an optimal word are already known. The supported distinct content is the enumeration of all shortest strings and the sufficient, reversible event-order characterization, neither of which is given by the inspected threshold theorem or its equality-case constraints. The result is specific to the published transition family in the stated parameter range.

## value

PASS

A closed count of optimal words measures how many choices remain at the minimum reset length in an established family. A researcher can use the event characterization to generate or recognize every optimal schedule without enumerating the subset automaton. The nontrivial gating constraints and probability factorization are explanatory rather than a table or repetition of the known threshold.

The dated certificate retains the supplied scientific assessment, sources and limitations.
