# Independent mathematical audit

## correctness

PASS

Stationarity lets one add a voter at either end of the contiguous middle window. Only the two endpoint-and-count events change the majority indicator. In a gain word there are m+2 ones and m+1 zeros, but with final state 1 the outgoing counts are m+1 from each state. The equal endpoints imply N01=N10, so N11=N00 as well. Complementation bijects gains and losses, preserves transition factors exactly, and changes only initial mass from pi1 to pi0, a ratio t/s. Thus the signed increment is (1-t/s) times gain mass. The gain event contains a word for every m, including 101 for m=0, and every word has positive mass. When s=t complementation gives J_m=1/2 at every size; otherwise the bounded indicators converge in expectation to the appropriate endpoint by the Markov ergodic theorem. No assumption on the sign of 1-s-t is used. The exact-rational checker was read, not run: its majority cross-check reaches 11 voters; its separate gain/loss and complement checks cover m=0 through 3 only. This finite scope does not restrict the proof.

## originality

PASS

The distinct claim is the exact endpoint-pivotal identity and hence strict monotonicity for stationary serial Markov votes in contiguous odd windows. It is not a priority claim for monotonicity with independent voters or asymptotic success under dependence. Accessible comparisons do not establish equivalent coverage; the precise scope of Berend–Sapir (2007) remains unresolved.

## value

PASS

Asymptotic consistency does not decide monotonicity at every finite size under dependence, and dependent-jury models can have finite optima. The exact all-size comparison for a single stationary serial law explains why neither persistent nor alternating local dependence changes the competence sign, and quantifies each increment through one positive pivotal probability.

The dated certificate retains the supplied scientific assessment, sources and limitations.
