# Independent mathematical audit

## correctness

PASS

Both the original inequalities and the narrowed result are true. For any symmetric nonnegative-weight rule, the three pure losing profiles force 3u,4v,5w<q with q>0 if correctly classified, implying u+v+2w<59q/60 and contradicting the winning (1,1,2). Every symmetric surrogate therefore loses at least one full obstruction orbit. For 5<=m<=8 all orbit sizes exceed binom(m,5) except the C-only losing profile, and the A-only losing profile ties it at m=8. These strict comparisons also imply the repaired claim about all optimal symmetric error profiles. Exact score checks confirm the two displayed integer-weight rules err on just their named profile: integer scores H<=61 are an exhaustively bounded box and H>=62 is covered by componentwise factors 6/5 and 4/3. The low-score maxima at a=0,1,2 are 70,72,66 and 76,78,80, respectively. The minima and allowed profiles at m=5,6,7,8 are 1:C, 6:C, 21:C, 56:A or C. An unrestricted perfect rule would remain perfect after averaging its weights over within-class permutations because the quota and strict loss inequalities are preserved; no such rule exists. At m=5 exactly one C-only coalition exists, and independent enumeration found only that error (mask 31744) among 32768. Replay: python3 /workspace/branches/reproduce_frozen_math.py 2. The repaired reproducibility note corrects the minimum Python version for int.bit_count.

## originality

PASS

PASS applies to the repaired claim, not the novelty of the original as a whole. The same-family Resultary record dfb016c86552 proves the exact large-class symmetric answer and a stronger unrestricted asymptotic order. The repair credits these entirely, and establishes instead the remaining small-class regime, its optimizer-profile tie and switch, and the exact unrestricted first case. The inspected stronger large-class result uses an A-only outlier construction and does not determine a C-only fit: it does not imply the sharp orbit lower bound is attainable at m=5,6,7, or the second attaining profile at m=8. The new C-only certificate proves this attainability. No earlier-priority inference is drawn from the path dates.

## value

PASS

The repair gives the finite crossover of optimal approximations for a published natural example that exposes disagreement between margin error and coalition-frequency error. The small-class solution is not mere numerical recomputation: an optimal rule knowingly sacrifices a different type of losing coalition before the tie, and this switch completes the equal-treatment classification across the allowed class sizes. The sole labelled error in the first size remains optimal when equal treatment is relaxed, giving a usable exact benchmark. The already covered large-size rate is context, not value claimed by the repair.

The dated certificate retains the supplied scientific assessment, sources and limitations.
