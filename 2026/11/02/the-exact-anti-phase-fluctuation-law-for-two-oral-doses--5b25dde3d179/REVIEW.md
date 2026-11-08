# Independent mathematical audit

## correctness

PASS

In the deterministic linear one-absorption-compartment periodic model with positive first-order rates a,b, positive weights w1,w2 and period T, periodic impulse profile G has integral over a period 1 and mean (w1+w2)/T. Expanding squared deviation yields phase variation 2w1w2[H(δ)-H(T/2)] where periodic autocorrelation sums the explicit difference of exponential tails. Re-derived R(s)=a²b²/[2(a+b)(b-a)]*(e^-a|s|/a - e^-b|s|/b) and periodic geometric-series identity. Penalty equals w1w2a²b²/[(a+b)(b-a)]*(F_a(d)-F_b(d)), F_r=(cosh(rd)-1)/(r sinh(rT/2)); integral F_r(d)=∫_0^d sinh(ry)/sinh(rT/2)dy decreases strictly in r for 0<y<T/2 because x*coth x increases. Hence unique anti-phase minimum for all distinct or coincident positive rates, including unequal doses; local quadratic coefficient positive. Independent numerical exact-formula penalty checks for a=1,b=4,T=1,w=(1,2) at d=.25,.5 gave 0.0487428383554 and 0.1163095966182; actual checker.py source separately integrates concentration with Simpson quadrature for rate/phase grids, including a=b. Quadrature diagnostic not infinite proof.

## originality

PASS

Classical periodic Bateman absorption/elimination, AUC exposure normalization, and multiple-dosing half-life are established. Relevant Plusquellec-De Biasi-Souhait 1999 primary article expressly addresses nonuniform repeated administration, but only abstract could be obtained; it is a material unresolved full-text priority risk, not evidence of noncoverage. Sahin-Benet 2008 and Grover-Benet 2011 focus operational half-life, peaks/troughs and simulations rather than this specifically squared integrated mean fluctuation formula in available descriptions. The exact two-dose phase penalty and global strict anti-phase theorem are best-knowledge additions.

## value

PASS

Natural precise analytic design question for stable periodic linear filters: optimal relative phase minimizing steady-state L2 deviations, including unequal weights and coalescing rate limit. The exact cost and curvature support sensitivity analysis, without making medical recommendations. Neither a generic instruction to stagger doses nor a routine mean AUC identity equals this exact global inequality.

The dated certificate retains the supplied scientific assessment, sources and limitations.
