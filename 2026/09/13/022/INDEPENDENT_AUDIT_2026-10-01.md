# Independent mathematical audit

## correctness

PASS

For the self-inclusive empirical-measure convention explicitly used in the record's gap calculation, the two independent rate-1 chains give p(u)=(1+exp(-2u))/2 and an extra running-cost term p(u)(1-p(u)) at N=2. Integrating gives V-U=T/4-(1-exp(-4T))/16 and N(V-U)=T/2-(1-exp(-4T))/8. The displayed master solution satisfies the stated two-state master equation, and F(x,m)=m_x is Lasry-Lions monotone. These identities were independently recomputed. The claimed verification script was not present at the audited commit.

## originality

PASS

Best-of-knowledge searches found no prior source stating this exact self-inclusive finite-horizon value counterexample. Cecchin-Pelino's standard finite-state N-player formulation evaluates a player's value against the empirical measure of the other players, while the submitted linear-in-T bias comes from including the tagged player in the empirical measure. Cohen-Huffman proves a different uniform-in-time weak-error result for stable interacting jump processes, not an accumulated finite-horizon value bound of this self-inclusive form.

## value

PASS

Under the explicitly used self-inclusive convention, the example isolates a clear mechanism—an O(1/N) self-interaction bias whose time integral grows linearly with the horizon—and gives an exact sharp obstruction to a T-uniform constant. This is a motivated boundary result, while the convention mismatch must remain explicit.

The dated certificate retains the supplied scientific assessment, sources and limitations.
