# Independent mathematical audit

## correctness

PASS

Center the four scalar levels 0,t,t+1,t+2 with group sizes r,1,1,q-1, and attach a centered simplex of squared radius 1-t² to the r left leaves. The spokes and bridge have unit length, the right internal edges collapse, and the left internal squared length is 2r(1-t²)/(r-1), giving t≥sqrt(p/(2r)) for r>1. For p=q=2 the interval is just t=1 and the simplex is zero. The centered squared norm is the scalar squared deviation plus r(1-t²), which expands to the stated D(t). Summing the Laplacian Rayleigh inequalities over coordinates gives lambda_2 D(t)≤B; maximizing the quadratic clips t0 as claimed and yields the three cases including both equality boundaries. At t=t*, the left and right leaf equations fix a and b, summing the eigen-equations over the larger clique fixes the bridge h=lambda(p mu-t), and the remaining equations follow by balance. All three are positive: mu>0, t+1>mu, and p mu-t=(q r t+p(2q-1))/N>0. Both contrast blocks have eigenvalues at least lambda (left a+rc, right b, when present); when t<1 the simplex gives the left contrast eigenvalue lambda. The positive scalar gradients on the three quotient edges identify lambda as the least eigenvalue of C^(1/2) Delta M^(-1) Delta^T C^(1/2), by the negative off-diagonals and irreducibility. This proves it is the first positive quotient eigenvalue. All positive conductances are on unit-length embedding edges, so the coordinate eigen-equations give the exact budget lambda D*. Equality for any competing allocation forces zero on short edges and the eigen-equations individually on each scalar coordinate level. In particular the individual spoke weights are forced at leaves and the bridge is forced by summing over one clique. When t<1 the simplex coordinates span the left-leaf zero-sum space and determine its internal Laplacian to be (lambda-a) times the orthogonal projector; when t=1 the left internal weights vanish by strict slackness. This proves unrestricted uniqueness even at equality of the regime conditions. The wording about activated edges concerns non-spoke clique edges; the spokes and bridge are positive throughout. Frozen barbell_verification.py and VERIFICATION.md were inspected, not run; the supplied NumPy sweep is diagnostic, not the proof.

## originality

PASS

The variance-unfolding dual and the optimum realized by the double-broom support are covered. A separate indexed gateway result also exhibits three regimes but on a different topology and activates different edges. The supported distinct result is the exact single-bridge unequal-clique solution, in particular the third-regime transition where the larger clique's non-spoke edges necessarily become positive and the optimum exceeds the tree-support value. No inspected result covers the full formula and unrestricted uniqueness.

## value

PASS

The bottleneck of a single bridge makes the spoke tree a natural guess. The two thresholds show when this support remains optimal, when a contrast mode first becomes binding, and when the largest clique genuinely needs internal edges. The certificate establishes exact value and individual conductances in a natural family, including the unrestricted uniqueness and boundary behavior, rather than just a numerical instance or a balance approximation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
