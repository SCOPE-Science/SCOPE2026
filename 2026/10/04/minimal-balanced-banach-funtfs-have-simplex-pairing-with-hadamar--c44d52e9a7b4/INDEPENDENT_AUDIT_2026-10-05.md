# Independent mathematical audit

## correctness

PASS

Tightness gives a surjective synthesis map \(T\), so \(N\ge n\); balance \(T\mathbf1=0\) rules out \(N=n\), hence \(N\ge n+1\). At equality, trace gives \(\lambda=(n+1)/n\). The pairing matrix \(A=\Phi T\) obeys \(A^2=\lambda A\), has rank n and has \(\mathbf1\) as both left and right kernel generator. Therefore \(A/\lambda\) is the projection onto \(\mathbf1^\perp\) along \(\mathbf1\), namely \(I-(n+1)^{-1}\mathbf1\mathbf1^T\), forcing diagonal 1 and off-diagonal \(-1/n\). For a normalized Hadamard matrix of order n+1, deleting its first row gives a sign matrix S with \(S\mathbf1=0\), \(SS^T=(n+1)I\); columns scaled by 1/n in \(\ell_1^n\) with their sign functionals satisfy all unit-norm, norming, balance and tightness conditions. Exact Sylvester instances were independently replayed.

## originality

PASS

The direct motivating Cheng–Heil source was inspected at the balanced-FUNTF definition and its open Question 2.21. It asks balanced existence in real \(\ell_1^n\) but does not state the sharp universal lower bound, the equality-case simplex pairing matrix, or the Banach Hadamard realization. Searches under balanced FUNTF/Hadamard/simplex terminology and Resultary found no prior theorem with this combination. Hilbert-space balanced-frame and Hadamard-frame constructions do not automatically provide Banach norming pairs or the equality rigidity.

## value

PASS

The result resolves the sharp minimum-length edge of an explicit balanced Banach-FUNTF existence problem, completely classifies the pairing matrix at equality, and gives infinitely many sharp \(\ell_1^n\) realizations. The equality rigidity is reusable independently of Hadamard existence and is more than a routine dimension count.

The dated certificate retains the supplied scientific assessment, sources and limitations.
