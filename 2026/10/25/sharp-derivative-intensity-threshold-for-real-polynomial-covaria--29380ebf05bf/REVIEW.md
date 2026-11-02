# Independent mathematical audit

## correctness

PASS

The bivariate symmetric covariance kernel B_C(X,Y)=sum C_ij X^i Y^j satisfies J_k(x)=[d_X^k d_Y^k B_C]_(X=Y=x). With u=(X+Y)/2, w=(X-Y)/2 symmetry gives an even-power w expansion sum_j f_j(u)w^(2j). The operator d_X d_Y=(d_u^2-d_w^2)/4 makes vanishing J_0..J_K equivalent by induction to f_0=...=f_K=0, i.e. (X-Y)^(2K+2) divisibility. Multiplying by this monic factor raises both separate degrees by m=2K+2, leaving a symmetric S of bidegree at most r=N-m and dimension (r+1)(r+2)/2 when r>=0. At r>=0, the explicit nonzero D represented by (X-Y)^m yields distinct I±epsilon D positive definite for sufficiently small epsilon; above threshold kernel is zero. Each J_k has degree <=2(N-k), yielding its interpolation bound. Independent QQ matrix ranks rebuilt directly from falling-factorial coefficients matched formula for all N=1..8 and 0<=K<=N. Finite cases corroborate the all-degree algebra.

## originality

PASS

Chen--Wang (arXiv:2304.06206) Theorem 4.1 and Lemma 4.2 concern conjugate phase retrieval of pure complex spline/polynomial signals using value and first derivative magnitudes. Their rank-one/rank-two difference restrictions do not imply injectivity of the linear measurement map on every real symmetric covariance; the new theorem identifies the full nullspace, including positive-definite ambiguity witnesses, and sharp all-rank derivative threshold. Similar multi-window phase retrieval results use other measurement geometry. The diagonal-jet ideal itself is elementary algebra, so originality lies in the sharp applied covariance classification, with possible older jet tomography formulations as risk.

## value

PASS

The kernel dimension, exact measurement order necessary/sufficient for arbitrary covariance, and positive-definite nonidentifiability witnesses are natural all-rank inverse-problem invariants; they clarify why pure-state phase retrieval does not solve statistical second-moment tomography. The finite sampling corollary is practical but not the sole value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
