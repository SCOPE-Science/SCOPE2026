# Independent mathematical audit

## correctness

PASS

PASS. Hankel H_overline(az+bz²) acts through complex symmetric 2×2 block [[a-bar,b-bar],[b-bar,0]], operator norm (A+sqrt(A²+4B²))/2. For normalized Szego kernel w, squared output is (1-|w|²)(|a+bw|²+B²); phase optimization yields F(B,r) after norm-one parameterization A=1−B². For B<=1/2, tested r=B gives 1−B^4>=15/16>25/27. For B>=1/2, fixed r0=1/sqrt6 derivative factor 2(1-r0²)(B-r0)(2B²−Br0−1) yields unique minimum B0=sqrt(2/3) and lower 25/27. At B0 the exact factorization 25/27−F(B0,r)=(sqrt6*r−1)^2*((sqrt6*r)^2+4sqrt6*r+8)/54 gives global upper 25/27, with unique maximizing radius r0. All identities and derivative verified independently by SymPy; pure coefficient endpoints satisfy N=G, and equality iff A/B=1/sqrt6. Supplemental verify.py sampled phases and grids cannot prove the universal inequality; displayed global certificates do.

## originality

PASS

PASS best of knowledge. Dyakonov arXiv:2609.33242 formulates Hankel strong reproducing kernel thesis and identifies the kernel/Garsia testing norm, noting strictness for some az+z² but the accessible abstract does not supply sharp all-quadratic multiplicative constant or equality classification. Published Resultary logarithmic Hilbert-Hankel exact gap is for a particular infinite-rank symbol and does not imply optimal bound on all quadratic symbols; published monomial/Blaschke classifications address zero-gap rather than positive maximum gap. Dyakonov full manuscript inaccessible through arXiv/OA and authorized Oxford VPN disconnected, so this major primary comparison remains residual risk rather than automatic failure.

## value

PASS

PASS. The full two-coefficient polynomial subspace is the first nontrivial rank-two Hankel family: its sharp quantitative kernel test-vs-operator gap and precise phase-invariant equality classification are a naturally motivated exact norm constant, not mere renaming of an SRKT counterexample.

The dated certificate retains the supplied scientific assessment, sources and limitations.
