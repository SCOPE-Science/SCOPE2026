# Exact Haar-unitary permanent variance corrects the full-unitary normalization
## Finding
For Haar-distributed \(U\in U(n)\),
\[
\mathbb E\,|\operatorname{perm}(U)|^2=\binom{2n-1}{n}^{-1}.
\]
The 2026 source instead identifies this second moment with \(n!/n^n\). These quantities agree only for \(n=1\); for \(n\ge2\) they differ, and their ratio is
\[
R_n=\frac{n!/n^n}{\binom{2n-1}{n}^{-1}}
=\frac{(2n-1)!}{(n-1)!n^n}
\sim 2^{-1/2}\left(\frac4e\right)^n.
\]
Hence the source's full-Haar variance normalization is exponentially too large. The correct root-mean-square scale is
\[
\left(\mathbb E|\operatorname{perm}(U)|^2\right)^{1/2}
=\binom{2n-1}{n}^{-1/2}
=\sqrt2(\pi n)^{1/4}2^{-n}(1+O(n^{-1})).
\]
The conclusion is a normalization correction, not a rejection of a possible circular-Gaussian shape after the correct rescaling.

There is also a direct anti-concentration consequence. For any positive polynomial \(q\), Markov's inequality gives
\[
\Pr\!\left\{|\operatorname{perm}(U)|^2\ge \frac{n!/n^n}{q(n)}}\right\}
\le \frac{q(n)}{R_n}
= q(n)\sqrt2\left(\frac e4\right)^n(1+o(1)).
\]
Thus a threshold at the source's \(n!/n^n\) full-Haar scale cannot have probability tending to one; for every fixed polynomial loss it is exponentially rare. This separates the full \(U(n)\) ensemble from the Gaussian or large-ambient-dimension submatrix regime relevant to standard boson-sampling approximations.

## Assumptions and scope
The statement is for the permanent of the entire \(n\times n\) Haar unitary matrix, with normalized Haar probability measure on \(U(n)\), and for every integer \(n\ge1\). It does not claim a limiting distribution beyond the exact second moment. It does not apply the full-unitary formula to a \(k\times k\) submatrix of a much larger Haar \(U(d)\) matrix when \(d\gg k\).

## Proof
Let
\[
v=\frac1{\sqrt{n!}}\sum_{\sigma\in S_n}
e_{\sigma(1)}\otimes\cdots\otimes e_{\sigma(n)}.
\]
The \(n!\) tensors in this sum are orthonormal, so \(v\) is a unit vector. It lies in the symmetric power \(\operatorname{Sym}^n(\mathbb C^n)\). A direct expansion gives
\[
\langle v,U^{\otimes n}v\rangle
=\frac1{n!}\sum_{\sigma,\tau\in S_n}
\prod_{j=1}^n U_{\tau(j),\sigma(j)}
=\operatorname{perm}(U),
\]
because, after fixing \(\sigma\), the change of permutation variable \(\pi=\tau\circ\sigma^{-1}\) produces one copy of every permanent monomial, and there are \(n!\) choices of \(\sigma\).

The representation of \(U(n)\) on \(\operatorname{Sym}^n(\mathbb C^n)\) is irreducible and has dimension
\[
d_n=\binom{2n-1}{n}.
\]
Schur orthogonality for a unit vector matrix coefficient of an irreducible unitary representation yields
\[
\int_{U(n)}|\langle v,U^{\otimes n}v\rangle|^2\,dU=\frac1{d_n},
\]
which proves the exact moment.

Since \(\binom{2n-1}{n}=\tfrac12\binom{2n}{n}\), the central-binomial asymptotic gives
\[
\binom{2n-1}{n}^{-1}=2\sqrt{\pi n}\,4^{-n}(1+O(n^{-1})).
\]
Taking square roots gives the stated root-mean-square scale. Stirling's formula applied to \(R_n\) gives \(R_n\sim2^{-1/2}(4/e)^n\). The probability estimate is then immediate from Markov's inequality.

## Verification
The bundled checker verifies exact factorial/binomial identities for \(1\le n\le100\), confirms the first nontrivial case \(n=2\) gives exact second moment \(1/3\) rather than \(1/2\), and numerically checks convergence of the exact ratio to \(2^{-1/2}(4/e)^n\). These finite checks corroborate arithmetic only; the all-\(n\) proof is the representation-theoretic argument above.

## Relationship to prior work
Rivin's arXiv:2602.10141v3 states in its Haar-unitary distribution section that the variance is \(n!/n^n\), calls that quantity the exact second moment from Weingarten calculus, and uses it for the typical-size and boson-sampling anti-concentration discussion. The correction above applies exactly to that full-unitary ensemble.

Nezami's 2021 work studies moments of permanents for \(k\times k\) submatrices of Haar \(U(d)\) matrices and Gaussian matrices by representation theory. That broader literature is consistent with treating the full-unitary case \(d=k=n\) separately from the large-ambient submatrix regime. The exact second-moment identity itself is classical representation theory; the contribution here is identifying and propagating its consequence for the recent full-Haar normalization and its claimed anti-concentration scale.

## Limitations
No claim is made that the source's empirical circularity or Gaussian-shape diagnostics fail after rescaling by the correct variance. No fourth-moment or central-limit theorem is proved. The Markov argument only rules out anti-concentration at the exponentially inflated \(n!/n^n\) full-Haar scale; it does not settle anti-concentration at the correct Haar scale or for Gaussian/large-ambient submatrix ensembles.

## References
1. Igor Rivin, *Permanents of matrix ensembles: computation, distribution, and geometry*, arXiv:2602.10141v3 (2026), especially Sections 3.2–3.3 and 8.3.
2. Sepehr Nezami, *Permanent of random matrices from representation theory: moments, numerics, concentration, and comments on hardness of boson-sampling*, arXiv:2104.06423 (2021).
