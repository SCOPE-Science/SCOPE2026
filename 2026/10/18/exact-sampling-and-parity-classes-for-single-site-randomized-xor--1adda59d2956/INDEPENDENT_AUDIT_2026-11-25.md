# Independent mathematical audit

## correctness

PASS

The shift is an invertible binary map. The columns Ae_j,…,A^te_j are the linear image of the independent fair noise bits, so each affine support point has identical mass. Independently, take e_1 as cyclic generator and write m=n+1: the state module is F₂[z]/P with P=(z^m−1)/(z−1), and z acts by A. The cyclic basis in the proof telescopes to e_j=z(1+…+z^{m−j−1})e_1. The gcd of P with this generator polynomial is (z^g−1)/(z−1), of degree g−1; this uses the polynomial gcd of z^m−1 and z^{m−j}−1 and does not require square-freeness in characteristic two. Thus its annihilator has degree m−g and the first t noise columns have rank min(t,m−g). The uniform-affine-to-uniform TV distance is exactly one minus the support fraction, including t=0 and n=1. In the rotation model, residue-class parity is onto the even-parity g-bit words, its kernel is the span of the within-class edge incidences, and noise fills each reachable parity fiber after m−g steps. Reachability at all sufficiently large compatible times gives exactly one closed communicating class per quotient orbit and period equal to that orbit length. The Burnside fixed words repeat each free bit g/d_s times, so even parity is either automatic or one independent constraint. Independent direct binary elimination matched all 348 ranks for n=1,…,8, all sites and t=0,…,n+3; direct fair-noise propagation through t=11 and SCC/return-period computation in the 256-state n=8,j=3 example gave support plateau 64 and classes of sizes 64 and 192 with periods 1 and 3. The all-dimension result follows from the proof, not these checks.

## originality

PASS

The fixed middle-site uniformization theorem and general affine/controllability methods are not new. The evaluated all-site finite-time profile together with the parity rotation-orbit classification, exact class periods and count are a distinct supported claim. The cited theorem and the most plausible catalog matches do not have those statements or a stronger result that mechanically yields the combined classification.

## value

PASS

For the natural fixed-site variant, exact sampling at the previously analyzed site does not distinguish sites that sample uniformly from sites trapped forever in a cycle of affine fibers. The theorem supplies that sharp design criterion, the entire distance profile, and the complete reducible-case partition with periods. These answer concrete reachability and sampling questions beyond an isolated rank check.

The dated certificate retains the supplied scientific assessment, sources and limitations.
