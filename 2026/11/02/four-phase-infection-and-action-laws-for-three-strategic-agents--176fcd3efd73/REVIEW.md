# Independent mathematical audit

## correctness

PASS

In the 3-agent homogeneous irreversible-infection asynchronous best-response process with 0<a<1 and a/2<tau<min(a,1/2), the first update event and subsequent independent uniform first-appearance races partition all trajectories. Infected initial vertex chosen first (prob 1/3) yields one survivor phase iff tau>=theta1=a/(1+a); otherwise all infected. If a susceptible is chosen first (2/3), next two-label race is fair; one survivor after agent1 update requires tau>=theta0=(sqrt(1+8a)-1)/4 and the remaining susceptible to be updated next (prob 1/3). A further two-race exceptional event requires tau>=theta2=(sqrt(a^2+8a)-a)/4, giving contribution 1/18. Hence P(K=1)=1/3 indicator(tau>=theta1), P(K=2)=1/9 indicator(tau>=theta0)+1/18 indicator(tau>=theta2), and all remaining mass K=3. Equality is safe because infection is strict >tau. Independent rational 17-epoch Markov state propagation checked exact probability enclosures for seven parameter pairs including threshold boundaries, with unresolved tail about 0.001015 each; these are finite-horizon corroboration, not proof of infinite-time convergence.

## originality

PASS

Best-of-knowledge PASS: Karmakar–Podder–Roy–Sadhukhan define this same game and treat two disjoint threshold domains tau>=1/(n-1) and tau<=a/(n-1) under the relevant a<1 regime, leaving a/(n-1)<tau<1/(n-1) open for this same n=3 model. The exact four-phase three-agent law with boundary atom probabilities and limiting action profiles is not implied by the inspected theorems of their revised primary manuscript.

## value

PASS

PASS: the original epidemic game's smallest open intermediate-threshold population is naturally motivated; exact infection cardinality and limiting action distribution with sharp three threshold surfaces answer a genuine model question, including equality boundaries that qualitative monotonicity misses.

The dated certificate retains the supplied scientific assessment, sources and limitations.
