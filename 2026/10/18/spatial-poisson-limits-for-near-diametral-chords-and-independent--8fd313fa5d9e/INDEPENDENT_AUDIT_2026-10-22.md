# Independent mathematical audit

## correctness

PASS

Uniform matching of 2n vertices has P(t disjoint specified edges)=[(2n-1)(2n-3)⋯(2n-(2t-1))]^-1. For each fixed deficiency 0≤j≤J the candidate class contains n antipodal edges at j=0, 2n near-antipodal edges otherwise, with bounded incident candidate degree. O(n^(t-1)) t-tuples conflict while disjoint t-tuples have matching probability (2n)^-t(1+O(t²/n)); joint spatial factorial moments then yield independent Poisson processes of rates 1/2 and 1. Flajolet–Noy Theorem 3 independently provides exact E C_n=n(n-1)/6, Var C_n=n(n-1)(n+3)/45 and crossing CLT. Conditioning on ANY t specified disjoint candidate chords leaves uniform matching of remaining 2(n-t) cyclically ordered vertices, so residual crossings have law C_(n-t); t imposed chords affect at most t(n-t)+t(t-1)/2 crossing pairs, O_t(n), negligible against n^1.5. This uniform conditional CLT factors with all marked factorial moments, proving Gaussian independence from Poisson marks. D_n≥k iff no deficiency 0..k-1, giving e^(-(k-1/2)); tail →0 ensures tightness. The finite covariance follows by conditioning on a prescribed edge, counting ab/(2n-3) expected other crossings plus residual mean. Independently enumerated matching sets n=2..6 and exactly checked published crossing means, variance and derived class-crossing covariances, rather than inferring CLT from enumerations.

## originality

PASS

Flajolet–Noy exactly covers Gaussian crossing count, Acan Theorem 4.2 exactly covers Poisson counts of fixed *short* chord classes, and Paguyo concerns individual convergence rates. None of these inspected statements covers moving near-diametral deficiency j=n-s(e), spatial Poisson locations, and asymptotic independence from crossing Gaussian. Conditional stability supplies genuinely additional joint information; best-knowledge priority acknowledges possible broad matching rare-edge theorems.

## value

PASS

Near-antipodal chords are natural geometric extreme structures in uniform chord diagrams, while the total crossing count is a central global statistic. The result identifies a sharp discrete extreme-deficiency tail, a full spatial limiting process, and a nontrivial independence between sparse extremes and dense Gaussian fluctuations. The exact covariance order n underlines why covariance alone is not enough to show the joint theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
