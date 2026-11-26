# Independent mathematical audit

## correctness

PASS

Every ordered draw sequence with counts n has probability ∏(a_i)_{n_i}/(A)_t, giving exchangeability and the multinomial multiplicity in (1). Grouping colors yields the beta-binomial marginal; taking the Gamma ratios with each count k fixed gives Γ(A)(a_i)_k/[Γ(A−a_i)k!] times t^{−a_i}(1+O(t^{−1})). Grouping into three blocks gives O(t^{−a_i−a_j}) for joint deficiencies; with d=2 the combined deficient counts cannot sum to large t. The union bounds with pair corrections give C_*; the discrete tail-sum has the same convergence as ∑t^{q−1−a_*}, including divergence at equality. Independently, conditioning on the final counts and using exchangeability, the marked completion mass is exactly (r_i/t) times the probability of N_i(t)=r_i with all other counts meeting quota. The pair bound shows their constraint changes only lower order, giving the coefficient Γ(A)(a_i)_{r_i}/[Γ(A−a_i)(r_i−1)!]=a_i c_i. Summing and taking ratios gives both reported unmarked and conditional limits. At unit masses count compositions are uniform; shifting by quotas gives the CDF and imposing N_i(t)=r_i gives the same marked formula for each i except for the factor r_i. For rigidity, at t=R the only permissible count vector is r. Comparing one 2 against the other possible location at R=d+1 forces symmetry, then comparing (3,1,…) with (2,2,1,…) at R=d+2 yields 2(a+2)/[3(a+1)]=1, hence a=1; both comparisons are available at d=2.

## originality

PASS

The pointwise finite-time Pólya completion law, including a prior sum that resolves the last color, is covered. The distinct result evaluates the fixed arbitrary-quota joint tail constants and marked local asymptotics and characterizes the exact quota-blind case; it does not claim the model or underlying exact summation law as new.

## value

PASS

This turns a finite occupancy sum into a sharp heavy-tail and marked-exit law, identifying which colors dominate late completions and how the fixed quotas alter their weights, including tied minimal masses. The finite-moment criterion and exact converse for when quota allocation is invisible are usable structural consequences. Neither value assessment rests on newness of the urn or the unit-mass stars-and-bars calculation alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
