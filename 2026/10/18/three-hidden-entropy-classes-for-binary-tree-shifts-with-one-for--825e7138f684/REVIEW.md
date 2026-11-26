# Independent mathematical audit

## correctness

PASS

The child subtrees are independent once the root star is chosen; for M/P/F the forbidden pair removes B_n^2, A_n B_n, or B_n^2 respectively, in the root-1, root-0, and root-0 counts. Appending zeros below all leaves extends these representatives, and complementation/child exchange extends the rest. Thus the ratios p=B_n/S_n and the S recursion agree with the stated formulas. At n=2 the ratios are 3/7,4/7,4/7; substitution at the endpoints using monotonicity verifies the invariant intervals. For M, 2p<=1 and 2-p^2>=7/4 bound |f'| by 16/49; for P, |1-2p|<=1/7 and q>=7/4 give the stronger bound 16/343; for F the largest derivative is at 2/3 and equals 27/49. From n=2 the deletion fractions have the strict separated bounds (40/89)^2 < 12/49 and 1/4 < (4/7)^2, so both the finite-count ordering from n=3 and the strict entropy ordering follow coefficient by coefficient. Telescoping 2^(-n)log S_n gives the positive convergent series and discarded tail <(log 2)2^(-N), implying the coarser log 2 limit. Multiplying the tail by 2^n gives a weighted average of log q at future iterates with weights summing to 1; contraction gives log q(p*)+O((27/49)^n), hence the stated relative error and reciprocal prefactor. The factor p-1 in F's fixed-point cubic lies outside the invariant interval. An independent script (python3 /workspace/review-evidence/check_tree_and_particle.py) enumerated all eight rules through n=4, giving M/P/F totals (89,86,82) at n=3 and (14242,12979,11047) at n=4, and reproduced the displayed decimals by bounded series evaluation. The finite/decimal checks are not used in the all-height proof; the uploaded checker was inspected, not run.

## originality

PASS

Credit is limited to the complete one-forbidden-star census with strict hidden-entropy separation and finite-height ordering and asymptotic prefactors. General recurrence methods, the normalization, existence of a normalized entropy, and the common coarse entropy are prior. The inspected recurrence framework is applicable but does not give the interval separation or contraction-based relative asymptotic for these rules without the claim-specific analysis.

## value

PASS

A complete census of single local prohibitions is a natural minimal test case for whether hidden entropy improves discrimination over the standard coarse invariant. It gives three provably different normalized growth constants where coarse entropy gives none, plus quantitative asymptotics from which finite-level counts can be interpreted. It is not merely a numerical table or a reformulation of general entropy existence.

The dated certificate retains the supplied scientific assessment, sources and limitations.
