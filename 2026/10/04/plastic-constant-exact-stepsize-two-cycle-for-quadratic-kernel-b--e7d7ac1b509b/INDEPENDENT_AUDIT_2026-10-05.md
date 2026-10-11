# Independent mathematical audit

## correctness

PASS

The scalar quadratic specialization gives the exact normalized recurrence \(t_{k+1}=t_k\min\{\sqrt{1+t_k/t_{k-1}},[2(t_k^2-t_k)]^{-1/2}\}\) on the proposed orbit. For the plastic constant \(r^3=r+1\) and the stated \(a,b=ra\), direct algebra shows that at state \((b,a)\) the growth branch equals \(r\) and is smaller, producing \(b\), while at \((a,b)\) the curvature branch equals \(1/r\) and is smaller, producing \(a\). Thus the stepsizes alternate forever. Both lie in \((1,2)\), so the iterates never hit a degeneracy and the local curvature estimates remain defined. Their two-step contraction factor \((a-1)(b-1)\) is strictly between zero and one, proving Q-linear convergence. The high-precision verifier reproduces these identities but is not needed for the exact proof.

## originality

PASS

Originality passes on a best-of-knowledge basis with an explicit direct-source access risk. The defining Bregman adaptive-gradient source gives the update and reports alternating/fluctuating stepsizes as behavior needing explanation; the Euclidean predecessor describes seemingly cyclic adaptive stepsizes. The audited theorem supplies an exact period-two orbit on a scalar strongly convex quadratic, with a closed plastic-constant initialization and simultaneous Q-linear iterate convergence. Fresh Resultary search did not return an implication-equivalent exact adaptive cycle. The focal manuscript could not be independently read in full after open-route failure and one authorized institutional attempt failed, so no whole-document noncoverage claim is made.

## value

PASS

Whether adaptive stepsizes themselves converge is a meaningful algorithmic behavior distinct from iterate convergence, and the cited line of work explicitly flags oscillatory steps as needing explanation. An exact strongly convex quadratic cycle demonstrates persistent nonconvergence in the cleanest possible setting while retaining rapid convergence of the iterates, sharply separating these two notions.

The dated certificate retains the supplied scientific assessment, sources and limitations.
