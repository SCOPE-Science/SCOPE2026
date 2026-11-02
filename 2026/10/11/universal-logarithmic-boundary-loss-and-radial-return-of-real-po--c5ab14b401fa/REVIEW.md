# Independent mathematical audit

## correctness

PASS

For 1≤p<∞ fixed, normalized probability Haar and real mean-zero ||f||∞≤1, Kovalev Prop 2.1 gives exact sharp square-wave extremizer by conformal strip Φ=4 arctan(z)/π and Littlewood subordination of |Re Φ|^p. With a=(1-r²)/(2r), the exact moment-deficit integral is (2/π)∫_0^1 [1-(1-(2/π)atan(a/x))^p]/sqrt(1-x²) dx. On (0,a), its contribution is bounded by O(a); for a≤x≤1 use uniform 1-(1-(2/π)atan t)^p=(2p/π)t+O_p(t²), valid t∈[0,1] even p=1, because inner base≥1/2 and p fixed. The weighted error a²∫_a^1 dx/(x² sqrt(1-x²))=a sqrt(1-a²)=O(a); the main integral equals log((1+sqrt(1-a²))/a)=log(1/a)+O(1). Hence 1-Np(r)^p=(4p/π²)a log(1/a)+O_p(a); p-th root and a=1-r+O((1-r)²) establish Np(r)/r=1-(4/π²)(1-r)log(1/(1-r))+O_p(1-r). The log loss dominates O_p(1-r) so Np<r near 1. As r→0, Np/r→(4/π)||cos||_p; it exceeds 1 exactly for p>4.1095286347..., and continuity produces at least one equality radius. No claim of uniqueness, p→∞ uniformity, complex data or nonzero mean. Independently reconstructed the 7-blob Git tree and checked p=2 Fourier equality high precision plus 12 (p,epsilon) consistency cases; finite checks support, not replace, proof.

## originality

PASS

Best-of-knowledge PASS restricted to the evaluated exact leading logarithmic coefficient simultaneously for each fixed finite real p. Kovalev (2026) already supplies the sharp maximizer, all-(p,r) norm integral, p=2 Fourier series, and global p-threshold: these are powerful antecedents, and the p=2 special asymptotic is not new. Moreover his Lemmas 2.7–2.8 give φ(s)^(p-2)B2(s) upper control near s=1, with φ(s)=1+O(1-s); summing the p=2 series gives 1-B2(s) of order (1-s)log(1/(1-s)), hence eventual return of Np(r)<r for ANY fixed finite p≥2, including supercritical p, as a corollary. Therefore radius-return is NOT independently original despite not being printed. The submitted all-finite-p SHARP 4/π² leading coefficient is not stated or evaluated in that source and requires an additional endpoint singular-integral estimate with an O_p(a) error; it is more than copying a table or changing notation. No inspected separate source proves this evaluated entire family. Indexed and semigroup coverage remains incomplete; do not mistake negative searches for novelty proof.

## value

PASS

The sharp decay rate of the already-optimized real Poisson L∞_0→Lp norm as radial smoothing vanishes is a natural analytic invariant, for a complete fixed-finite-p family rather than an arbitrary parameter slice. Quantifying the leading logarithmic boundary layer with an explicit p-independent 4/π² coefficient and O_p(1-r) remainder is useful when differentiating/benchmarking semigroup norm sharpness and comparing fixed p. The qualitative supercritical radius return is already a consequence of Kovalev but remains an instructive geometric interpretation; value is anchored in the quantified universal coefficient, not an alleged new qualitative phase transition. This is a bounded mathematical refinement, not a new general Schwarz theorem or a paper-scale advance.

The dated certificate retains the supplied scientific assessment, sources and limitations.
