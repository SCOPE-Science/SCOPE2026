# Independent mathematical audit

## correctness

PASS

Both full inverse branches have maximal absolute slope γ=2/(3+α)<1. Substituting ψ(u)=(4u)^p Q((4u)^(p−1)) in 4u=3ψ+ψ^α gives an analytic implicit Q near Q=1. The convergent expansion bounds ψ^(j)(u)=O(u^(p−j)) at noninteger p and yields the asserted positive coefficient of ψ′. Thus for k<p the kth branch derivatives are bounded and the (k+1)st integrable, as needed for the Sobolev transfer estimate. The highest differentiated transfer term costs γ^k by change of variables; the coefficient of the next-highest derivative gives an integrable weight after change of variables, since its pushforward L¹ norm equals the original coefficient's L¹ norm. Splitting off a small L¹ tail and using the W^{1,1} sup bound absorbs it; lower terms cost only W^{k−1,1}. Iteration gives power bounds and the compact embedding gives essential radius <1. The invariant integration functional gives a fixed vector in each eligible space. For clarity on uniqueness and positivity, at order one, taking absolute values of a real fixed vector yields another fixed vector by positivity and conservation of the integral. Every nonzero nonnegative continuous fixed vector is positive on the entire interior by the full-cylinder argument. The positive and negative parts of a real fixed vector are fixed and cannot both be nonzero, so the fixed space is one-dimensional. The order-one power bound and quasi-compactness make its Cesàro averages converge to that space, and L¹ contraction and density of W^{1,1} in L¹ extend uniqueness to all L¹ invariant densities. All higher-order and analytic fixed vectors therefore represent the same density. The transfer equation gives the endpoint power with h(1/2)>0; its noninteger exponent lies strictly between ceil(p)−2 and ceil(p)−1, contradicting the endpoint Taylor expansion required by W^{ceil(p),1}. For integer p=m, the inverse of 4u=z+3z^m is analytic along the interval with simple roots, so ψ=z^m is holomorphic nearby. In a sufficiently thin complex tube the branch derivatives are uniformly <1; integrating along a segment to a closest real point puts both images in a compactly contained smaller tube. Signed holomorphic weights ±φ′ replace the real absolute weights. Compactness by Montel and invariance of integration again give a nonzero holomorphic fixed function, which restricts to a nonzero fixed vector on the real interval. No numerics are needed for either direction.

## originality

PASS

PASS for the complete all-order spatial Sobolev classification and reciprocal-integer holomorphic dichotomy for this family. The exact endpoint term and W^{2,1} obstruction for 1<p<2 themselves overlap a broader indexed family and are not credited as distinct in that regime. Primary exact-map and related transfer results cover regularity at some orders and parameters and analytic mechanisms under different hypotheses, not the complete classification. Dates alone do not settle priority.

## value

PASS

The theorem distinguishes intrinsic invariant-density regularity from the order available in low-order transfer estimates. The noninteger obstruction identifies sharp loss at an endpoint in the actual density, and isolated reciprocal-integer cases offer a different analytic regime despite an unbounded forward derivative. This is a unified classification for a family used in response theory, not simply another second-order estimate or a numeric endpoint calculation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
