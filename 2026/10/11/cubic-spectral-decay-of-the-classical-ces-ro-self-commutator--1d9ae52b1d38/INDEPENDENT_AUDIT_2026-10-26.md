# Independent mathematical audit

## correctness

PASS

Direct matrix multiplication gives K_ij=d_max(i,j), d_j=sum_{k>=j}(k+1)^-2-(j+1)^-1 and a_j=d_j-d_{j+1}=1/((j+1)^2(j+2)). Hence K=sum_j a_j v_jv_j* in trace norm because sum_j(j+1)a_j=1; positivity, trace 1, injectivity follow. Lower minmax: on E_n=span(e_n,...,e_{2n-1}), the partial-sum vector has norm >=||x||/2 and a_j>=a_{2n-1}>=1/(12n^3), giving λ_n>=1/(48n^3). Upper: impose first-n-zero and disjoint dyadic zero-sum blocks of L_j=ceil(2^(3j/2)) on I_j=[2^jn,2^(j+1)n); J=ceil(2log_2 n), M=2^Jn>=n^3, codimension <7n. Blockwise Cauchy Schwarz gives <=4n^-3 energy per band norm and the tail has <=1/M<=n^-3; Rayleigh on F_n <=4n^-3, so λ_(7n+1)<=4/n^3. Monotonic interpolation gives exact n^-3 order, Schatten iff p>1/3 and weak endpoint. No leading coefficient is proven. Fresh separately written rational checker verified 192 finite cutoff matrix/Gram identities, trace telescoping at 3 N values and all 698 block counts n=2..699, plus matched the pinned seven-blob Git tree SHA; these tests only corroborate arithmetic, not the universal minmax proof.

## originality

PASS

Fresh comparison by exact operator and implication, including full open primary Sang and Ma manuscripts and the same-commutator compactness work of Gül. Exact trace-one is already covered by a related published generalized-trace result; novelty lies in the matching cubic two-sided eigenvalue estimates and exact Schatten p=1/3 threshold. No independent prior theorem subsuming this entire claim identified, best of knowledge only.

## value

PASS

A canonical nonnormal operator has a positive self-commutator whose trace-class membership alone leaves all p<1 Schatten thresholds undecided. The self-contained cubic eigenvalue comparison gives a natural precise spectral-order and weak-Schatten endpoint for this classic operator, relevant to ideal-theoretic quantitative nonnormality; the n^-3 exponent is neither automatic from positivity nor from trace=1. This is a naturally motivated analytic invariant, not an arbitrary finite table or relabeling.

The dated certificate retains the supplied scientific assessment, sources and limitations.
