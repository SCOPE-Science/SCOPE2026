# Independent mathematical audit

## correctness

PASS

Read original RESULT.md and all seven tree entries, including proof, code and verification description. For a=1 the n-side agents each see one red and one blue neighbor, attaining h(0) and blocking any mutually strict swap; same-side swaps preserve same open neighbor sets. For a=0 the only candidate is a blue 2-side agent with red n-side agent; the red agent improves from zero same-neighbor fraction iff b>=2 (postfraction (b-1)/n strictly between 0 and 1), and blue improves from (n-b)/n to 1/2 iff 2b != n. a=2 follows by color reversal. Every allowed swap changes a to 1 and hence terminates after one move. Disjoint coefficients produce E_n(t) with exceptional n-even b=n/2 term (only n>=4). Exact binomial ratios simplify to (k+2)(3k+1)/(2(k+1)(2k+1)) and (k+1)/(2k+1); difference k(k+3)/(2(k+1)(2k+1))>0, limits 3/4 and 1/2. E_n(1)/2^(n+2) yields the stated even central-binomial correction 1/sqrt(2*pi*n)+O(n^-3/2) and exact odd correction. Independently enumerated 8,160 colorings n=3..10, evaluating 30,192 strictly profitable ordered-combination swaps at destination vertices with open neighborhoods and checking all coefficients and stability cases; zero mismatches. Reconstructed source Git tree SHA from actual seven blob identities. No claim for n<3, agents with labels or other payoff shapes; finite test alone is not infinite proof.

## originality

PASS

Best-of-knowledge PASS for the FULL new conjunction (strict open-neighborhood peak-half K_{2,n} one-step characterization, exact fixed-population equilibrium polynomial, and parity spikes), not for underlying Schelling definitions, general bipartite existence/FIP, or binomial algebra. Same-payoff primary Bilò et al. is closed-neighborhood; same-open-neighborhood Agarwal et al. has monotone utility; later diversity-seeking study uses three other payoff shapes and equitable populations. Actual Resultary/published SCOPE searches returned no same-claim record. No stronger theorem or table was identified from inspected relevant statements; this is not exhaustive novelty proof.

## value

PASS

The degree-asymmetric K_{2,n} is a natural small-hub versus large-group network, not an arbitrary graph or unsystematic finite slice. Exact per-composition equilibrium polynomial, one-step improvement dynamics, and especially two order-one conditional spikes (near-balance limit 3/4 versus balanced 1/2) give an interpretable nonmonotone stability law absent from mere existence/price-of-anarchy or generic potential arguments. Unconditional parity asymptotics quantify a distinct global statistic. Substantive though specialized; it is not claimed to settle general complete bipartite Schelling games or asymmetric peaks, and much of the combinatorial proof is elementary once the two-part geometry is isolated.

The dated certificate retains the supplied scientific assessment, sources and limitations.
