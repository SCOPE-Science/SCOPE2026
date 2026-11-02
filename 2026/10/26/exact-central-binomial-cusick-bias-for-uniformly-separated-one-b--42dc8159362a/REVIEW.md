# Independent mathematical audit

## correctness

PASS

Read exact RESULT.md and carry-automaton verify.py. The digit sum identity s2(n+t)−s2(n)=h−K(n,t) is exact for carries K. In any accepted configuration K≤h, a carry launched at one occupied bit cannot reach the next occupied position at distance at least h+1. Hence separate bit windows e_j..e_j+h produce independent geometric isolated chains L_j with P(L=ℓ)=2^{-ℓ-1}, and {K≤h} equals {∑_j min(L_j,h+1)≤h}. The sum of h independent geometric variables is negative-binomial, with P(sum≤h)=P(Bin(2h,1/2)≥h), giving the central-binomial formula. Uniform fixed-length binary prefixes and exponentially vanishing carry tails establish natural density for fixed t. Independent exact rational carry DP including tail verified 15 isolated examples h=1..5. The finite tests do not prove all h or gaps.

## originality

PASS

Relevant published research-index and primary literature comparisons found no directly covering exact claim, subject to the explicit priority limitations. The novel result is the exact claim stated, not its previously known foundational object or general theory.

## value

PASS

Cusick digit-sum correlations are natural arithmetic densities. A universal finite separation condition causes exact stabilization of a density across every support pattern of a specified weight; the closed central-binomial law and asymptotic furnish a structural family, not a one-off computation. It is not the known universal positivity bound or the large-weight minimum.

The dated certificate retains the supplied scientific assessment, sources and limitations.
