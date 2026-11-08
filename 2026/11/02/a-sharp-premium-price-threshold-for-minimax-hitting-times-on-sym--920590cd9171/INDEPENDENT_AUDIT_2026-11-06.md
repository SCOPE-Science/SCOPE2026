# Independent mathematical audit

## correctness

PASS

The original frozen RESULT.md included a materially false example: it called four prices (100,1,1,1) a k=3 star and asserted T*=363 vs uniform 412; with k=4 the stated rates give true T=473 and equal-rate T=515. The general theorem remains correct. Re-derived H_0j=k/r_j and H_ij=1/r_i+k/r_j by first-step equations; hence T=k x_(1)+x_(2), x_i=1/r_i. Any lower waiting time can be raised to second-largest without increasing T, creating budget slack and disproving optimality. A unique exceptional larger waiting time must belong to the largest price. Minimizing T(t)=(kp+P+kPt+p/t)/B over t>=1 has unique minimizer max(1,sqrt(p/(kP))), giving exact closed form and the unique optimum for all k>=3 and positive prices. Replaced the false example with k=3,B=1,p=(54,1,1), r=(1/60,1/20,1/20), T*=200 vs uniform 224; checked budget=1 and all ordered hitting times exactly. All numbers and the limitation prose are corrected in supplied complete RESULT.md.

## originality

PASS

Best-of-knowledge original as the complete price-dominance/uniqueness threshold for symmetric star edge rates under a worst ordered-pair mean hitting-time objective. The complete Sun–Boyd–Xiao–Diaconis original paper optimizes spectral gap, not worst hitting time; Zeng treats average hitting time with constrained weight multiset; Aldous–Fill supply hitting-time identities without this optimizer. Unread old PERT allocation remains a priority risk.

## value

PASS

Sharp threshold p>kP gives a natural resource-design boundary: all rate prices can be heterogeneous but the optimal rates remain equal until a single price dominates. It determines exact minimax hitting performance and a unique optimizer on all star sizes, a meaningful constrained stochastic optimization invariant beyond tabulating existing hitting formulas.

The dated certificate retains the supplied scientific assessment, sources and limitations.
