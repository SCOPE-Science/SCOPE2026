# Independent mathematical audit

## correctness

PASS

Thue-Morse block identities A_{4n}=1-t_n, A_{4n+1}=0, A_{4n+2}=t_n, A_{4n+3}=A_n yield E_{4n}=E_n, E_{4n+1}=E_n+2-3t_n, E_{4n+2}=E_n+1-3t_n, E_{4n+3}=E_n. Reading base-4 digits makes t a two-state toggle; max/min dynamic programs solve inductively for extrema of E_N=3D_N on N<4^k: 1+ceil(k/2), -floor(k/2). Odd/even all-1/all-2 digit witnesses attain each. Independent fresh direct 01 prefix enumeration verified extrema for k=1..8 after corrected cumulative-prefix accounting. Comparing log_2 N=2k+O(1) yields limsup=1/12 and liminf=-1/12. Elementary induction, not finite extrapolation, proves all k.

## originality

PASS

Spiegelhofer, Gaps in the Thue-Morse Word, arXiv:2102.01018 and J Aust Math Soc 114 (2023), main Theorem 1.2 and §3.3, proves D_N is finite-transducer output, D_N=O(log N), exact range (1/3)Z and explicit positive/negative unbounded subsequences. His p34 equation (60) does not give the exact global N<4^k maxima nor sharp limiting coefficient 1/12. The two-state recurrence and exact envelope refine those qualitative bounds. Risk: related automatic-sequence literature might independently optimize the transducer.

## value

PASS

Sharpens a central automatic-sequence discrepancy estimate from order of growth to exact extrema on every natural digital prefix and matching leading constants on both signs, answering a useful extremal finite-state optimization question.

The dated certificate retains the supplied scientific assessment, sources and limitations.
