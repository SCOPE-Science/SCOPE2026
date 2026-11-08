# Independent mathematical audit

## correctness

PASS

Reconstructed the exact mixed-sign EF1 shortfall E_ij=s_j-s_i-max(a 1_{g_j>0}, b 1_{c_i>0}) and checked both greedy branches. If agent 1 owns a chore, an E_1k>0 witness implies s_k-s_1>b; donating to maximum-other h keeps the recipient happy by removing the received chore; all other happiness survives by the explicit own-chore / available-good split, while the loss of the last-chore threshold is offset by raising s_1 by b. If agent 1 has no chore, E_1k>0 forces a good-owning highest h with M>s_1+a; the h-to-1 good transfer preserves happiness including final-good case and nonincreases E_1j. Each step consumes a distinct original chore of agent 1 or original good outside 1, hence <=m termination. For a=b, scores z_i=g_i-c_i obey EF1 iff spread <=1; all original others are at two adjacent levels, agent 1 stays minimal through greedy steps, and its final score is floor(sum z_i/n). Every transfer increases z_1 by at most one, proving the exact global lower bound. Independently implemented exact count-vector checker reproduced 8331 near-EF1 states and 14259 valid transfers for 7 ratios, n<=4,m<=8. Finite checks corroborate, not prove, unrestricted real parameters/all n.

## originality

PASS

Best-of-knowledge originality for the all-n signed two-valued mixed-manna near-EF1 restoration theorem and sharp a=b transfer distance. Chandramouleeswaran et al. 2026 revised Table 1 leaves general mixed feasibility/optimality open and its Example 4.18 has many distinct per-sign magnitudes, not two-valued. Its all-goods/chores theorems do not handle the mixed sign-branch switch. Igarashi et al. 2024 and Yuen et al. 2026 address nonnegative goods exchanges/reformation. No matching published finding surfaced in the actual semantic search; unindexed special cases remain a risk.

## value

PASS

Meaningful positive structural boundary at a published heterogeneous mixed-manna obstruction: arbitrary agent number and positive magnitude ratio, strong per-pair non-worsening invariant, at most m one-item repairs. The equal-magnitude exact shortest transfer law is a natural discrete distance invariant, not a mere restatement of existence or a renamed all-goods proof.

The dated certificate retains the supplied scientific assessment, sources and limitations.
