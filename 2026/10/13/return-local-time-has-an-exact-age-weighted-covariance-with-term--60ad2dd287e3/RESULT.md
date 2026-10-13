# Return local time has an exact age-weighted covariance with terminal energy
## Finding
Let \(X_1,X_2,\ldots\) be iid \(\mathbb R^d\)-valued increments satisfying
\[
\mathbb E X_1=0,
\qquad
0<\tau:=\mathbb E\|X_1\|^2<\infty.
\]
Write
\[
S_k=\sum_{i=1}^kX_i,
\qquad
L_n=\sum_{k=1}^n\mathbf 1\{S_k=0\}.
\]
Then for every integer \(n\ge1\),
\[
\boxed{
\operatorname{Cov}(L_n,\|S_n\|^2)
=
-\tau\sum_{k=1}^n k\,\mathbb P(S_k=0).
}
\]
Equivalently, the contribution of the possible return at time \(k\) is exactly
\[
\boxed{
\operatorname{Cov}(\mathbf 1\{S_k=0\},\|S_n\|^2)
=
-k\tau\,\mathbb P(S_k=0).
}
\]
Thus every nontrivial return probability contributes negatively, with a weight proportional to the age of the return.

For the one-dimensional simple symmetric random walk, put
\[
N=\left\lfloor\frac n2\right\rfloor,
\qquad
p_N=4^{-N}\binom{2N}{N}.
\]
Since only even times can be returns,
\[
\boxed{
\operatorname{Cov}(L_n,S_n^2)
=
-\frac{2N(2N+1)}3p_N.
}
\]
For \(n\ge2\), define
\[
\mu_N=(2N+1)p_N-1.
\]
Then
\[
\operatorname{Var}(L_n)=2N-3\mu_N-\mu_N^2,
\qquad
\operatorname{Var}(S_n^2)=2n(n-1),
\]
and therefore
\[
\boxed{
\operatorname{Corr}(L_n,S_n^2)
=
-\frac{2N(2N+1)p_N/3}
{\sqrt{(2N-3\mu_N-\mu_N^2)\,2n(n-1)}}.
}
\]
Stirling's formula gives the nonzero limiting correlation
\[
\boxed{
\operatorname{Corr}(L_n,S_n^2)
\longrightarrow
-\frac1{3\sqrt{\pi-2}}.
}
\]

## Assumptions and scope
The local time counts exact returns to the starting point and excludes time zero. The increments need not be symmetric, lattice-valued, or one-dimensional. If every exact return probability vanishes, the identity reduces to zero on both sides. The finite-second-moment assumption is used only to make terminal quadratic energy integrable.

The explicit closed form and correlation limit are specialized to the one-dimensional simple symmetric walk with steps \(\pm1\) of equal probability.

## Proof
Fix \(1\le k\le n\), and write
\[
R_{k,n}=X_{k+1}+\cdots+X_n.
\]
The future increment \(R_{k,n}\) is independent of \(S_k\), has mean zero, and satisfies
\[
\mathbb E\|R_{k,n}\|^2=(n-k)\tau.
\]
On the event \(\{S_k=0\}\), one has \(S_n=R_{k,n}\). Hence
\[
\mathbb E\!
\left[
\mathbf 1\{S_k=0\}\|S_n\|^2
\right]
=
\mathbb P(S_k=0)(n-k)\tau.
\]
Also
\[
\mathbb E\|S_n\|^2=n\tau.
\]
Therefore
\[
\operatorname{Cov}
\left(
\mathbf 1\{S_k=0\},\|S_n\|^2
\right)
=
-k\tau\,\mathbb P(S_k=0).
\]
Summing over \(k\) proves the general identity.

Now specialize to the simple symmetric walk. Its return probability at time \(2j\) is
\[
p_j:=\mathbb P(S_{2j}=0)=4^{-j}\binom{2j}{j},
\]
while odd-time return probabilities vanish. The central-binomial recurrence
\[
p_j=\frac{2j-1}{2j}p_{j-1}
\]
implies by induction
\[
\sum_{j=1}^{N}j p_j
=
\frac{N(2N+1)}3p_N.
\]
Thus
\[
\sum_{k=1}^{n}k\,\mathbb P(S_k=0)
=
2\sum_{j=1}^{N}j p_j
=
\frac{2N(2N+1)}3p_N,
\]
which yields the finite covariance formula.

For the local-time variance, first note the standard finite sum
\[
\mathbb E L_n
=
\sum_{j=1}^{N}p_j
=
(2N+1)p_N-1
=\mu_N.
\]
The generating function
\[
\sum_{j\ge0}p_jz^j=(1-z)^{-1/2}
\]
gives the convolution identity
\[
\sum_{a=0}^{b}p_ap_{b-a}=1.
\]
Using the Markov property at the first return time in an ordered pair of returns,
\[
\mathbb E[L_n(L_n-1)]
=
2\sum_{1\le a<b\le N}p_ap_{b-a}.
\]
For fixed \(b\), the inner sum equals \(1-2p_b\). Summing and using the preceding formula for \(\sum p_j\) gives
\[
\mathbb E L_n^2=2N-3\mu_N,
\]
so
\[
\operatorname{Var}(L_n)=2N-3\mu_N-\mu_N^2.
\]

For the endpoint, independence of the Rademacher increments gives
\[
\mathbb E S_n^2=n,
\qquad
\mathbb E S_n^4=3n^2-2n,
\]
and hence
\[
\operatorname{Var}(S_n^2)=2n(n-1).
\]
Substitution gives the exact correlation formula.

Finally,
\[
p_N\sim\frac1{\sqrt{\pi N}},
\qquad
\mu_N\sim2\sqrt{\frac N\pi},
\]
so
\[
\operatorname{Cov}(L_n,S_n^2)
\sim
-\frac{\sqrt2}{3\sqrt\pi}n^{3/2},
\]
\[
\operatorname{Var}(L_n)
\sim
n\left(1-\frac2\pi\right),
\qquad
\operatorname{Var}(S_n^2)
\sim2n^2.
\]
The displayed correlation limit follows.

## Verification
The accompanying `checker.py` performs two independent finite replays. First, it exhaustively enumerates all simple-walk sign sequences through length \(18\) and checks the covariance, local-time variance, and endpoint-energy variance formulas with exact rational arithmetic. Second, it enumerates a nonsymmetric centered three-point increment law and checks the general age-weighted return identity directly, showing that the theorem is not using sign symmetry.

The checker also verifies the two finite central-binomial identities and the correlation formula over a larger symbolic range. These finite computations supplement the proof; they do not establish the all-\(n\) theorem by enumeration.

## Relationship to prior work
Random-walk local time is a classical object. Csáki, Csörgő, Földes, and Révész study the same simple-walk local time \(\xi(k,n)\), including the origin local time \(\xi(0,n)\), and develop strong Brownian-sheet approximations for its spatial profile. Their paper is therefore a direct same-object comparison, but its stated results concern local-time approximation and fluctuation fields rather than finite mixed moments with the terminal squared displacement.

Document-wide searches of the public full text for terminal-energy language and covariance formulas did not locate the identity above. The exact covariance here instead comes from conditioning each return indicator on the independent future and keeping the age of that return explicit.

The simple-walk local-time variance used for the correlation is derived inside the proof from the central-binomial generating function rather than imported from an external table.

## Limitations
The exact general identity is specific to terminal quadratic energy. It does not by itself determine the full joint distribution of \(L_n\) and \(S_n\), stochastic ordering, or covariances with arbitrary nonlinear endpoint functionals.

For continuous increment laws with no atomically possible exact return, \(L_n=0\) almost surely and the identity is degenerate. The result is most informative for recurrent or partially recurrent lattice walks.

Older random-walk literature may encode the same mixed moment through Green functions, additive functionals, or last-exit decompositions without using covariance terminology. That remains the principal originality risk.

## References
1. E. Csáki, M. Csörgő, A. Földes, and P. Révész, “Random walk local time approximated by a Wiener sheet combined with an independent Brownian motion,” arXiv:0709.0389, first submitted 2007-09-04; journal version, *Annales de l'Institut Henri Poincaré, Probabilités et Statistiques* 45 (2009), 515–544, DOI: 10.1214/08-AIHP173.
