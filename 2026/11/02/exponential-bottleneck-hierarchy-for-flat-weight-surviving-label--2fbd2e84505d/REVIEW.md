# Independent mathematical audit

## correctness

PASS

The occupancy formula counts the choice of occupied labels and the onto assignments. Missing one specified label gives the uniform one-step escape lower bound, so each visited level is left almost surely, and fixed-k inclusion–exclusion gives q_{n,k}∼k((k−1)/k)^n. A skip below j at departure from k>j requires all n choices in a set of j−1 labels. Dividing the corresponding union bound by q_{n,k} is valid at first departure, not just at the first round, by summing the geometric self-loop probabilities. Summing over at most n candidate departures proves the uniform skip bound (j=n is visited initially). The exact factorization (1−q)^(m−1)P_n(k,j) of the duration/destination probabilities justifies the independent clocks of the repair: the embedded path is chosen independently of the full array of holding times. Products of the fixed-k rescaled geometric tails yield the claimed joint exponential limit; the error of using the uncensored clocks is confined to the event of a skip, which tends to zero. The omitted original total-time claims are mathematically sound: the time spent above 2 is bounded in mean by n(3/2)^n, the levels k≥4 contribute at most n(4/3)^n in mean, and skip errors for 2 and 3 are polynomial after multiplying by their exact inverse escape probabilities. The frozen checker was read, not executed: the mean-remainder check at lines 40–41 is floating-point, despite the description. The repair drops that check and uses only rational validation of finite transitions and visitation; its recurrence is conditioned on a departure and has the correct boundary values.

## originality

PASS

PASS applies only to the repaired theorem: the unconditional joint law of separately scaled fixed-level residence times, with explicit skip control. The frozen package is not passed as stated: a distinct indexed statement for the identical endpoint gives a stronger total-time law and expressly includes the highlighted secondary exponential correction to the mean. Those headline contributions are removed, not relabeled. The exact joint law with the rates k and explicit fixed-level skip control are not stated in the available matching statement and do not follow from the overlapping total-time facts. The exact remainder of the indexed expansion was not available for comparison; no historical priority is inferred.

## value

PASS

The total absorption clock conceals all but the last bottleneck. The repaired theorem resolves actual fluctuations at all fixed low levels simultaneously and establishes that those levels are typically visited rather than simply conditioning on visits. This is a structural statement about the extinction trajectory and can be used for observables that distinguish different remaining support sizes.

The dated certificate retains the supplied scientific assessment, sources and limitations.
