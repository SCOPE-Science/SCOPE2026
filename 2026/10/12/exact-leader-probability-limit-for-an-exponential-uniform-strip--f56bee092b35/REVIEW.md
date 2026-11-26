# Independent mathematical audit

## correctness

PASS

The competitor's first-coordinate exceedance contributes exp(-x); at shortfall d in [0,min(w,x)] the second-coordinate contribution has conditional probability w-d and density exp(-x+d). This yields the verified two-branch CDF. As exp(-X) is uniform, transform by z=1-F conditional on w. Its inverse density is constant 1/(exp(w)-w) until z0=1-w exp(-w) and strictly increasing thereafter. The Beta(1,n) coupling yields strict decrease; the positive error is supported where 1-z<=1/e. A compact interior rectangle with w approaching 1 and 1-z approaching 1/e from below gives the matching root lower bound. Jensen and the exponential series give L>=3/(e+1)>4/5. Independent Simpson checks for the corrected and frozen integrals give 0.843078886983059 and 0.732359299691928 at 1048576 subdivisions; replay files under /workspace/branches/e36104ac-0029-4247-973e-b3c4cfb85308/ are independent_quad_corrected.py and independent_quad_results.txt. The newly written replacement verifier also ran successfully. The original script was inspected, not executed; its diagnostics take the faulty CDF as given.

## originality

PASS

Pass the repaired strip-specific result: correct the primary source's CDF, prove finite-n strict decrease, and identify the sharp root rate 1/e. Do not claim a new general concurrence theorem or novelty solely from evaluating the corrected limiting integral.

## value

PASS

This resolves a specific published model inconsistency, with an analytic confirmation of the simulated threshold and a finite-sample ordering plus sharp rate showing how that threshold is approached. It is not just a numerical re-evaluation of a known integral.

The dated certificate retains the supplied scientific assessment, sources and limitations.
