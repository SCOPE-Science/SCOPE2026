# Independent mathematical audit

## correctness

PASS

The poles 3±i√3 are excluded by the spectrum {-h,0}, and Q times the all-ones vector is zero, so the endpoint exists and has row sums one. For h>0 substitute the transient shift into R(h(x−1)). With D0=h²+6h+12, rho=h/√D0 and theta=arctan(√3/(h+3)), the denominator is (D0/12)(1−2rho cos(theta)x+rho²x²); its inverse has coefficient a_j=(12/D0)rho^j sin((j+1)theta)/sin(theta). The transient coefficients are c0=((h−3)²+3)/D0 and c_j=h(a_(j−1)−a_j), and the absorption entry in row i is h a_(n−i−1) by telescoping the row sum. Using rho=cos(theta)−√3 sin(theta), the addition formula gives sign(c_j)=sign(sin((j+1)theta−pi/6)) for j≥1. For n≥3 the first-neighbor condition is theta≥pi/12, hence h≤2√3. Simultaneous absorption signs require (n−1)theta≤pi: if this fails the first sampled multiple strictly greater than pi lies below 2pi and has negative sine, even if a previous multiple equals pi. Together the two conditions put every transient angle in [0,5pi/6], so they are sufficient. For positive h, theta decreases strictly from pi/6 to zero. Thus n≤7 (with n≥3) has no positive lower threshold, n=8 through 13 has the stated lower endpoints, at n=13 the two bounds coincide, and n≥14 has none. At n=2 there is no c1 constraint, and h=0 is the identity for all n. Fresh exact matrix solves at n=13 verified all signs and row sums at h=2√3, with entries (1,2) and (1,13) exactly zero (one-based); at h=3 entry (1,13) was −5577374880/23298085122481, and at h=7/2 entry (1,2) was −168/32761. These are checks of selected instances, not the proof of the classification.

## originality

PASS

The eight-state window and the general seven-state small-step positivity guarantee are already covered, and the underlying Padé polynomial/derivative mechanism is not new. The distinction supported by the comparisons is the complete simultaneous classification for the unit-rate absorbing chain at every length, including positive recovery for 9≤n≤12, the isolated positive step at n=13, and impossibility at all positive steps for n≥14. No checked statement or immediate specialization supplied those conclusions. This assessment is bounded and not an absolute priority assertion.

## value

PASS

The natural absorbing chain isolates two opposed sign mechanisms for a standard fourth-order integrator: small steps can lose mass nonnegativity in the absorption column, while steps above 2√3 fail in the transient nearest-neighbor entry. Their competition yields the nontrivial recovered windows and a sharp maximal length with an isolated step; knowing a universal monotonicity radius is zero does not tell a numerical analyst these domains.

The dated certificate retains the supplied scientific assessment, sources and limitations.
