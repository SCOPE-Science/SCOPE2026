# Independent mathematical audit

## correctness

PASS

For every q>0, all five latencies are continuous/nonnegative/nondecreasing and f is any Wardrop flow. The Wardrop average equals qL; if an outer count increases, an originally used shortest U/D/M path weakly decreases in cost, giving psi<=eps. When both outer counts decrease, f_U,f_D>0; direct edge-cost cancellation gives c_U(g)+c_D(g)=c_M(g)+L-R with each term of R nonnegative. Since g_M>f_M and its path cost is at most the minimum outer cost plus eps, min path cost<=L+eps-R and psi<=2eps-R. Equality forces R=0, c_U(g)=c_D(g)=L+eps, c_M(g)=L+2eps, g_U=g_D=0 and every stated plateau. The converse reproduces these exact values. Independent exact-Fraction checks covered 5040 rational-affine Wardrop comparison cases and the nonaffine sharp instance with theta=3/4; checked the full proof, not inferred an infinite result from finite tests.

## originality

PASS

The previously known factor-two instance and the regret/social-cost definitions are credited. The actual addition is an exact nonnegative deficit certificate for all monotone five-edge costs plus necessary-and-sufficient plateaus for ALL positive equality cases; primary material inspected did not show these full conditions. Priority remains qualified due to inaccessible specialized literature.

## value

PASS

A robust sharpness-rigidity theorem identifies exactly when a worst-case bounded-rationality performance loss can be attained; the explicit nonnegative deficit quantifies strict inequality and isolates three simultaneous plateaus. These are natural network-model structural questions not a relabeling of the prior fixed example.

The dated certificate retains the supplied scientific assessment, sources and limitations.
