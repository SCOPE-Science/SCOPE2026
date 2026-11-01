# Independent mathematical audit

## correctness

PASS

The claim is the multiplicative real d_BM for H_n={x in R^n:sum x_i=0}, n>=3 with inherited unnormalized ell4. Riener Theorem 1.3 applies to F_c(z)=sum_i(z_i-mean z)^4-c(sum_i(z_i-mean z)^2)^2, a symmetric quartic: global nonnegativity reduces to <=2 coordinate levels. For levels multiplicities k,n-k, exact Q_k=n/[k(n-k)]−3/n. Its max occurs k=1 and min at nearest k to n/2, yielding M_n=(n²−3n+3)/(n(n−1)), m_even=1/n, m_odd=(n²+3)/(n(n²−1)), attained. For any optimal Hilbert ellipsoid, feasibility K⊂E(Q)⊂dK is convex in positive Q via affine constraints Q(x)<=1 and Schur complement block [Q f;f^T d²]>=0 for all polar f. Averaging under coordinate permutations gives scalar Euclidean form on irreducible real H_n. Thus d_BM^4=M_n/m_n globally, not just for one coordinate basis. n=3 yields Q≡1/2 and d=1; asymptotic d~n^(1/4). Direct fractional checks n=3..10 confirm expressions, and the seven-file Git tree matched the assignment. Finite checks are not the theorem; critical half-degree hypothesis and optimality proof were inspected.

## originality

PASS

Best-of-knowledge PASS for the complete real all-n exact multiplicative Banach--Mazur invariant. Riener supplies symmetric-quartic positivity reduction, and Dalén may already supply the moment-extreme inequalities under finite-sample moment terminology; neither inspected source asserts the Euclidean BM distance for the constrained real space. Grundbacher--Kobos Theorem 1.1 is for direct ell-p sums. An adjacent published real p-dependent n=3 theorem covers only the n=3 member, while an adjacent complex result has different field and odd-n lower radial extrema. The full all-dimension real geometric invariant including parity and unrestricted ellipsoid optimality was not found in independent sources. A plausible historical moment source is inaccessible and flagged without using inaccessible material to claim absence.

## value

PASS

The canonical sum-zero S_n-standard subspace of classical real ell4 is a natural geometric object. Its Euclidean Banach--Mazur distance is a natural GL-invariant quantity, computed sharply for every n, including odd/even level imbalance and the n=3 Hilbertian exception. These are intrinsic geometric distinctions for a whole subspace family rather than an arbitrary slice or slight numerical improvement. Direct-sum bounds do not answer it. The value claim is limited to exact real ell4 hyperplanes; the moment ingredient itself is not claimed new.

The dated certificate retains the supplied scientific assessment, sources and limitations.
