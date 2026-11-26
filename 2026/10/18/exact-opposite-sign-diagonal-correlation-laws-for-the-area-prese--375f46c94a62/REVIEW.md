# Independent mathematical audit

## correctness

PASS

Independently recovered both formulas for all n with one area computation. Let N=2^n and condition on strip k, writing x=(k+u)/N, y=v; after n iterates the coordinates are u and (r(k)+v)/N with r the reversal of the n binary digits. The plus joint event is u+Nv<P and Nu+v<Q with P=N-k, Q=N-r(k). For the minus event, reflecting u to 1-u yields the same inequalities with P=k+1 and the same Q. In both cases 1<=P,Q<=N, so the intersection in the unit square is the quadrilateral (possibly with a coinciding vertex) bounded by the axes and the two lines. Its nonaxis vertex is ((NQ-P)/(N^2-1),(NP-Q)/(N^2-1)); the axis intercepts are Q/N and P/N. The conditional area is [PQ-(P^2+Q^2)/(2N)]/(N^2-1). Both marginals are uniform on 1,...,N, so E[P^2+Q^2]=(N+1)(2N+1)/3; independent unbiased digits give Cov(k,r(k))=nN/8, hence E[PQ]=(N+1)^2/4 ± nN/8. The mean of each sensor is 1/2, also after iteration because the strip map preserves area and partitions the square modulo null boundaries. Subtracting 1/4 gives the exact laws. In particular C_-(1)=0, C_-(2)=-1/40; for n>=2 the inequality 3nN^2>4(N^2-1) verifies negativity. Zero covariance for the two Bernoulli variables at lag one gives their independence; it says nothing about higher-order independence. The sum and remainder follow directly by expanding 1/(1-N^-2). The supplied verifier was inspected, not executed; even its exact n<=12 test is not evidence for the unrestricted lag quantifier in place of the proof.

## originality

PASS

The evaluated signed all-lag laws for the two specified diagonal indicators distinguish this result from the inspected coordinate correlations on other baker maps and from periodic-orbit action correlations. The bit reversal and general area-preserving baker-map framework are not credited as new. This is a bounded comparison; identified inaccessible sources are not treated as noncovering.

## value

PASS

The two straight diagonal cuts are natural half-area, discontinuous observations of the same elementary chaotic map. The exact result shows that equal means and similar geometry give very different finite-time dependence: one pair is independent at time one and negatively correlated thereafter, while the other is always positively correlated. It gives an exact correlation benchmark with the sharp n·2^-n scale and sign cancellation in the sum; a qualitative mixing bound would not supply these facts. No extension to unrelated polygon sensors or periodic-orbit statistics is claimed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
