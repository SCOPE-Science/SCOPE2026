# Independent mathematical audit

## correctness

PASS

Root the cyclic spacings at the first labeled start and rotate it to 0: the other n-1 starts remain iid uniform, giving Dirichlet(1,...,1) spacings. Isolation is exactly two adjacent spacings greater than a. In the J times uncovered-length product, the two terms sharing an adjacent gap impose two shifts, and the n-2 terms with a distinct gap impose three; simplex volume times the shifted-coordinate mean gives the stated mixed moment. As an independent check, for a tagged arc [0,a] and an uncovered location y in [a,1], other starts must lie in [a,1-a] but not [y-a,y]. Their available measure is (y-2a)_+ + (1-a-y)_+. Integrating its (n-1)st power over y and multiplying by n gives 2b^n+(n-2)c^n directly. Below 1/3, the derivative factor Q has strictly convex log: at n=5 use the first positive term for t<=1/8 and 5(1+2t)^2>=(3-2t)^2 thereafter; for n>=6 use the two fractions with factor 4. The endpoint Q(1)=1 with positive log derivative and Q(0+)=infinity imply one interior crossing, hence one maximum of G; G(0)<0 and G(1)=0 give the single interior root there. The normalized expression above 1/3 decreases then increases through one root, with no boundary zero at 1/3. For a=lambda/n the leading cancellation follows from b^(n-1)(1-a)^n/c^n=(1-2a)^(-1)(1+2a^2/(1-3a))^n=1+2(lambda+lambda^2)/n+O(n^-2); fixed points on either side of the unique positive limit root bracket n*a_{n,-}. The upper-root equation brackets epsilon=1-2a between n/2^(n+1) and twice that value and then gives the stated equivalent since n*epsilon tends to zero. Fresh integer sign checks bracketed each of the six printed decimal roots at plus/minus half a unit in the last place; the frozen checker was inspected, not executed.

## originality

PASS

Pass the adjacency-isolation two-root theorem, particularly the reentrant positive covariance and exponentially thin second threshold, not the Dirichlet spacing method or novelty of the lower-root constant. The dependency on prior gap-count moments is stronger than the related-work prose suggests: the count of isolated arcs is not determined by the gap count pathwise, but exchangeability bridges their joint moments. This does not cover the two-switch analysis in the sources inspected.

## value

PASS

Isolation is a natural singleton-component statistic, distinguishing adjacent gaps from the number of gaps. The exact sign reentry absent for gap counts and the coexistence of a sparse 1/n threshold and an exponentially thin near-half threshold are structural information about the dependence of island formation and global coverage, not just substituted parameters or sampled zeros.

The dated certificate retains the supplied scientific assessment, sources and limitations.
