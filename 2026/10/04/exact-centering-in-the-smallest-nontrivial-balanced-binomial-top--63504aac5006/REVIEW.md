# Independent mathematical audit

## correctness

PASS

Independent continuous jitters encode uniform tie-breaking. Conditioning on the lower of the two high scores gives the stated three-bin integral. I independently rebuilt the full \(3^4\) exact score-vector sum and the integral in SymPy; they agree identically. Re-centering at \(h=p-(1-\delta)/2\) factors \(P(p)-P(\mathrm{center})\) exactly as \(\delta h^2G_\delta(h^2)/24\). The polynomial \(G_\delta\) decreases in \(u=h^2\) on the admissible interval, and its endpoint value \(7+110\delta+14\delta^2-2\delta^3-\delta^4\) is positive for \(0<\delta<1\), proving the unique minimum.

## originality

PASS

Wu--Chen's current abstract proves exact centering for two populations and eventual exact centering for fixed balanced k=2t. An indexed quotation of their conclusion explicitly leaves unique centering for every balanced even n>=2 as a conjecture. Thus the submitted k=4,t=2,n=2 case is not implied by their eventual theorem and is the smallest nontrivial balanced instance beyond the exact two-population result. The primary arXiv PDF could not be fetched and the authorized fallback failed, so whole-body noncoverage is not asserted; that access gap remains a residual risk. Fresh Resultary search found no covering published SCOPE result.

## value

PASS

This is the smallest balanced top-selection case beyond two populations and the smallest even sample size covered by the explicit open conjecture. The exact positive factorization is a motivated base case rather than an arbitrary finite check.

The dated certificate retains the supplied scientific assessment, sources and limitations.
