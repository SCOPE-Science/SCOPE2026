# Independent mathematical audit

## correctness

PASS

For integer s>=3 and r,n>=1, characteristic roots alpha,alpha^{-1}, alpha>2, C=s^2-4>=5, z=alpha^{-2r}<1/4. With S=sum_{k>=n} U_{rk}^{-2} and A=U_{rn}^2-U_{r(n-1)}^2 integer, Binet gives AS=(1-z)(1-z^{2n-1})sum_{j>=0}z^j/(1-z^{n+j})^2. Lower bound using (1-w)^{-2}>1+2w yields AS>(1-z^{2n-1})(1+2z^n/(1+z))>1 (since 2(1-z^{2n-1})>z^{n-1}(1+z)). Upper bound AS-1< (32/9)z^n and S>Cz^n>=5z^n gives AS-1<S. Hence A-1<S^{-1}<A, proving floor exactly. Independent rational partial sums checked the inequalities for 96 parameter triples (s=3..6,r=1..3,n=1..8); finite checks do not establish infinity. At s=2,r=1,n=2 statement fails.

## originality

PASS

Best knowledge PASS for removing the sufficiently-large-s hypothesis of Park Theorem 18 over all hyperbolic integer s>=3. Park full text inspected; it does not claim unrestricted lower s. Original Amdeberhan-Chen-Moll-Sagan paper conjectures the formula. Distinguish other reciprocal powers and other recurrence determinants.

## value

PASS

Solves a specifically posed conjectural floor identity throughout the natural hyperbolic integer parameter regime, with uniform non-asymptotic margins and a demonstrably necessary exclusion s=2.

The dated certificate retains the supplied scientific assessment, sources and limitations.
