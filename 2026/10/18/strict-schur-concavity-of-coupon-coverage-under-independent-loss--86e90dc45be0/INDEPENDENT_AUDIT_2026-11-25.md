# Independent mathematical audit

## correctness

PASS

Given the complete draw word, presence of a drawn type depends precisely on its independent survival from the last draw through the post-draw loss at the observation time. For two target labels, condition on the locations of their combined draws and all other labels. This conditioning leaves the pair allocation free. The last run K has tail a^k+(1-a)^k. For K<M the pair's survival product uses the newest combined draw and the draw immediately preceding the terminal run; it is nonincreasing in K, and is zero at K=M. Writing its expectation using adjacent differences gives nonnegative coefficients multiplying the subtracted power sums. The total coefficient is positive when M>=2, and every power sum with k>=2 strictly decreases on balancing. All other target labels contribute a nonnegative weight independent of the pair split; a word-pattern of positive probability has M>=2 and all other targets drawn when t>=|A|. This covers common deterministic time-dependent retention including the no-loss case. For homogeneous 0<q<1, iid draws and independent loss masks over an infinite past give a stationary law via finite last-draw times. The same pair expansion is valid by bounded convergence and has positive coefficients, while the other-target weight is positive almost surely. The chain can reach the empty set in one step and every state from empty by consecutive draws and retentions, so stationarity is unique. Directly, the singleton moment is q w_i/(1-q+q w_i), and the full two-type moment is q^2(a s_2+(1-a)s_1), giving the stated rational expression. This optimizes simultaneous coverage, not first-passage times; at q=1 stationary coverage is constant across positive laws. The submitted finite exact checker was inspected but not run.

## originality

PASS

The distinct claim is strict allocation majorization at fixed time and at equilibrium under independent losses applied to all currently present types. The strongest comparisons use uniform sampling, different loss mechanisms, or first-passage objectives; the special case of permanent collection is prior.

## value

PASS

The result resolves an allocation question for a natural nonmonotone process: it identifies the unique optimum at every feasible observation time, and not just for a constant loss schedule or asymptotically. Equilibrium strictness is distinct from a completion-time optimum and remains informative when stopped-collection methods no longer identify observation-time coverage.

The dated certificate retains the supplied scientific assessment, sources and limitations.
