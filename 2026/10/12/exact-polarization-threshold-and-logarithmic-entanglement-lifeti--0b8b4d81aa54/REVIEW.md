# Independent mathematical audit

## correctness

PASS

The 4x4 anti-exchange unitary only mixes |00> and |11>, so for a diagonal incoming system population p the reduced system map is p->q p+(1-q)(1+m)/2 and p_{k-1}=[1+m(1-q^{k-1})]/2. Under ancilla partial transpose the unique possible negative eigenvalue is in the 01/10 block, giving N_k=[m sqrt((2-h)^2+4q(1-q)h^2)-1-m^2(1-h)]_+/4 for h=q^{k-1}. Its strict positivity condition factors with one positive root h_*=(1-m^2)/[m(sqrt(1+4q(1-q))-m)], for 0<m<1; h decreases, hence the first L=ceil(log(h_*)/log q) collisions are entangling iff m>1/sqrt(1+4q(1-q)), with no late birth or revival. For m=1 every finite k has positive but vanishing negativity; for m=0 or q endpoints none. Maximization q(1-q)<=1/4 yields m>1/sqrt2 over angles, and h_*~(1-m^2)/(v-1) yields logarithmic growth. Independently constructed joint density matrices and ancilla partial transposes for five regimes up to k=17, agreeing with the formula to 1e-12; near machine precision late pure-bath positivity is analytic rather than inferred from numerical thresholding.

## originality

PASS

Best-of-knowledge originality comparison by actual statement and implication, with historical and unavailable-material risks recorded; no priority certification. Inspected closest prior statements use different scopes/estimands or do not directly entail this final exact claim.

## value

PASS

The pre-reset system–ancilla entanglement lifespan of the experimentally motivated anti-thermalizing repeated-collision model is a natural measurable finite-time quantity. Exact sharp polarization/angle boundary, no-revival theorem and all-index lifetime classification refine the source's early-collision negativity plot. It does not repackage the already-known population recursion as new physics or assert steady-state entanglement.

The dated certificate retains the supplied scientific assessment, sources and limitations.
