# Independent mathematical audit

## correctness

PASS

Reconstructed RESULT Steps 1–4. If the central site is occupied, the kth one on either side is at distance at least k(m+1), and the periodic orbit saturates both bounds. If it is vacant and both tails are occupied, the nearest distances a,b are positive integers with a+b≥m+1; convexity bounds 2^(−a)+2^(−b) by 1/2+2^(−m), strictly insufficient to beat the occupied maximum. The one-sided case is smaller as well. For a constant center the maximal distance is 3c+(1−2c)W_m up to c=1/2 and 3c thereafter. This gives radius 3/2 for m=1 and W_m for m≥2, with the entire support in the critical closed ball at c=1/2 and c=0, respectively. For an arbitrary ambient center x the maximum distance to the support is convex and 1-Lipschitz. Its average along forward translates is at least the value at their coordinatewise average, which is uniformly o(1) from a constant sequence (offset-j error ≤min(1,2|j|/N)). Thus below the threshold there are infinitely many separated times with positive slack. Truncating inside this slack produces admissible violating words. The m-zero prefixes reset every hidden state, so each word of length ell has conditional occurrence probability at least (1−p)^m min(p,1−p)^ell including its reset. Iterating the conditional avoidance bound gives zero mass in the ball. Irreducibility and the self-loop yield stationarity and mixing, the reset property yields full support, and bounded gaps between optional draws yield nonatomicity. The inspected verify.py is a finite exact-rational packing check, not a proof of the orbit or probability steps; its frozen output was not rerun.

## originality

PASS

The supported distinction is an exact metric-dependent radius, including the full critical closed ball, for this dependent binary hard-core law with all real-valued centers. It is not the introduction of measure expansivity or a new general Markov theorem. No covering statement was found in the inspected closest sources.

## value

PASS

A natural exact invariant for a standard constrained process: this supplies the optimal detection scale for Bowen balls under a fixed compatible metric, distinguishing the half-valued ambient witness at the shortest gap from the zero witness at longer gaps. In particular the proof addresses arbitrary nonstationary real-valued centers, not only points in the symbolic support, and resolves the endpoint as full mass rather than just producing a positive admissible radius. This utility does not require metric or law universality.

The dated certificate retains the supplied scientific assessment, sources and limitations.
