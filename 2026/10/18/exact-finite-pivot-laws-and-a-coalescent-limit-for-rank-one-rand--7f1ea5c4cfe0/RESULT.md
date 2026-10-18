# Exact finite-pivot laws and a coalescent limit for rank-one randomized Jacobi diagonalization

## Finding

For a symmetric rank-one perturbation of a scalar identity, independent uniform pair pivots in the exact Jacobi eigenvalue algorithm diagonalize in a finite random time. If \(n\ge2\) is the matrix dimension and the initial rank-one vector has exactly \(s\in\{1,\ldots,n\}\) nonzero entries, the number \(T_{n,s}\) of sampled pairs needed for diagonalization is equal in distribution to a sum of independent geometric random variables:

\[
T_{n,s}\ \overset{d}{=}\ \sum_{j=2}^{s}G_{n,j},\qquad
\Pr(G_{n,j}=t)=(1-p_{n,j})^{t-1}p_{n,j},\qquad
p_{n,j}=\frac{j(j-1)}{n(n-1)},\quad t=1,2,\ldots.
\]

The empty sum for \(s=1\) equals zero. In particular,

\[
\mathbb E T_{n,s}=n(n-1)\left(1-\frac1s\right),\qquad
\mathbb E T_{n,n}=(n-1)^2,
\]

and

\[
\operatorname{Var}(T_{n,s})=
\sum_{j=2}^{s}\frac{1-p_{n,j}}{p_{n,j}^2}.
\]

For full-support initial vectors, the normalized stopping time has a nondegenerate limit:

\[
\frac{T_{n,n}}{n^2}\ \xrightarrow{d}\
L=\sum_{j=2}^{\infty}X_j,\qquad
X_j\stackrel{\mathrm{ind}}{\sim}\operatorname{Exp}(j(j-1)).
\]

This is one half of the classical Kingman-coalescent absorption-time law. In particular \(\mathbb EL=1\), \(\operatorname{Var}(L)=\pi^2/3-3\), and its Laplace transform is \(\mathbb E[e^{-tL}]=\prod_{j=2}^{\infty}j(j-1)/(j(j-1)+t)\) for \(t\ge0\).

There is also an exact block-size generalization: if a uniformly sampled set of \(b\in\{2,\ldots,n\}\) coordinate indices is Jacobi-diagonalized at each step, define

\[
q_{s,r}=\frac{\binom sr\binom{n-s}{b-r}}{\binom nb},\qquad
h_s=\sum_{r=2}^{\min(s,b)}q_{s,r},
\]

with binomial coefficients outside their natural ranges taken as zero. The exact expected number \(E_s^{(b)}\) of sampled blocks until diagonalization satisfies

\[
E_1^{(b)}=0,\qquad
E_s^{(b)}=\frac{1+\sum_{r=2}^{\min(s,b)}q_{s,r}E_{s-r+1}^{(b)}}{h_s},\quad 2\le s\le n.
\]

Here \(h_s>0\). This recurrence gives \(E_s^{(2)}=n(n-1)(1-1/s)\) and \(E_s^{(n)}=1\) for \(s\ge2\).

## Assumptions and scope

Fix \(n\ge2\), \(\lambda>0\), \(\rho\ne0\), and a nonzero real vector \(v\in\mathbb R^n\), with \(\lambda+\rho\|v\|_2^2>0\) if positive definiteness is desired. Begin with \(A_0=\lambda I_n+\rho vv^{\mathsf T}\). At every step independently sample a uniform unordered coordinate pair from all \(\binom n2\) possibilities, including pairs with zero off-diagonal entry. For a nonzero selected off-diagonal, apply an exact orthogonal Jacobi similarity that diagonalizes the associated two-coordinate principal block. For a zero off-diagonal, use the identity update. Count every sampled pair, including ineffective ones. The exact-arithmetic model has no thresholding, rounding, noisy observations, or truncation.

For blocks of size \(b\), sample uniform \(b\)-subsets independently, diagonalize the selected principal block orthogonally, and use the identity when it is already diagonal. There is a unique exceptional eigenvector direction on every sampled block containing at least two nonzero entries of the rank-one vector; any orthogonal diagonalizer maps that direction to one block coordinate. The block formula concerns *block samples*, not scalar rotation/flop cost.

## Proof

**1. Invariant rank-one form and exact support deletion.** After every orthogonal similarity \(Q\), one has

\[
Q^{\mathsf T}A_kQ=\lambda I_n+\rho(Q^{\mathsf T}v_k)(Q^{\mathsf T}v_k)^{\mathsf T}.
\]

If selected coordinates \(i,j\) both have nonzero entries, the selected rank-one block has eigenvectors parallel and perpendicular to \((v_{k,i},v_{k,j})\), with distinct eigenvalues \(\lambda+\rho(v_{k,i}^2+v_{k,j}^2)\) and \(\lambda\). The exact Jacobi rotation therefore sends that two-vector to \((\pm\sqrt{v_{k,i}^2+v_{k,j}^2},0)\), up to coordinate swap and signs. It deletes exactly one nonzero coordinate. Otherwise the off-diagonal entry \(\rho v_{k,i}v_{k,j}\) is zero, and the identity update leaves support unchanged. No nonzero coordinate can vanish outside the selected pair. The matrix becomes diagonal exactly when its rank-one vector has a single nonzero coordinate.

**2. Pure-death chain.** At support size \(j\), exactly \(\binom j2\) of the total \(\binom n2\) pairs meet two active coordinates. Their conditional sampling probability is \(p_{n,j}=j(j-1)/(n(n-1))\), irrespective of which coordinates are active or their magnitudes. A success decreases support by one; a failure preserves support. Since new pair samples are independent, the holding time at each level \(j\) is geometric with this parameter, and different holding times are independent by the strong Markov property of the independent pivot sequence. This proves the full sum law. The probability-generating function, for \(0\le z\le1\), is

\[
\mathbb E[z^{T_{n,s}}]=\prod_{j=2}^{s}\frac{p_{n,j}z}{1-(1-p_{n,j})z}.
\]

Taking geometric means and variances yields the expressions above; in particular \(\sum_{j=2}^s1/[j(j-1)]=1-1/s\).

**3. Limit law.** For fixed \(j\ge2\), the geometric holding time scaled by \(n^{-2}\) converges to \(\operatorname{Exp}(j(j-1))\) because \(n^2p_{n,j}\to j(j-1)\). The finite collection of holding times is independent, so any fixed partial sum converges to its independent exponential counterpart. For the remaining levels,

\[
\sup_{n>K}\mathbb E\left[\frac1{n^2}\sum_{j=K+1}^{n}G_{n,j}\right]
\le\sum_{j=K+1}^{\infty}\frac1{j(j-1)}=\frac1K.
\]

Markov's inequality permits the partial-sum limit to pass to the entire sum. The infinite exponential series converges almost surely and in \(L^1\) because its mean is finite. Independently summing its variances gives \(\sum_{j=2}^{\infty}1/[j^2(j-1)^2]=\pi^2/3-3\); its Laplace transform follows from independence and bounded convergence. The finite-n variance formula divided by \(n^4\) converges to the same constant using the explicit geometric variance sum and dominated convergence.

**4. Block hypergeometric recurrence.** Conditional on current support size \(s\), the number \(r\) of active indices in a uniform block of size \(b\) is hypergeometric with mass \(q_{s,r}\). A block holding \(r\ge2\) active coordinates has rank-one exceptional eigendirection and, after its exact eigendecomposition, exactly one active coordinate in that block. Hence the global support becomes \(s-r+1\). Blocks with \(r=0,1\) leave support size unchanged. The one-step first-exit equation is \(E_s^{(b)}=1+(1-h_s)E_s^{(b)}+\sum_{r\ge2}q_{s,r}E_{s-r+1}^{(b)}\); solve for \(E_s^{(b)}\). For \(s,b\ge2\), a uniform block has positive probability of containing two active coordinates, so \(h_s>0\). Base case and recurrence uniquely determine the expected block counts.

## Verification

The accompanying standard-library-only `reproduce.py` constructs the expected-block-count recurrence using exact rational arithmetic, checks the pair-pivot expectation and variance identities in finitely many dimensions, directly checks orthogonal-similarity matrix identities for mixed-sign rank-one vectors, and compares the expectation with independent Monte Carlo samples. The finite checks passed in the recorded run. Run locally with `python reproduce.py` under Python 3.10 or later. Numerical simulations do not prove the all-dimension or limit-law statements, which follow from the preceding analytic argument.

## Relationship to prior work

Detherage and Shah, *Matrix Factorizations with Uniformly Random Pivoting*, arXiv:2505.02023, place Jacobi diagonalization in a general uniform-pivot framework and prove convergence and stability guarantees. Their generic potential-decay analysis is not, by itself, an exact support-death or all-horizon stopping-time law for a scalar identity plus rank-one matrix. The present calculation supplies that special family's exact absorption distribution and a block-size recurrence rather than a competing general algorithm.

Möhle and Pitters, *Absorption Time and Tree Length of the Kingman Coalescent and the Gumbel Distribution*, arXiv:1502.03983, analyze the classical coalescent absorption law. That law and its moments are prior work: the present identification concerns its appearance as the asymptotic cost distribution of independently sampled rank-one Jacobi rotations. The finite geometric holding-time derivation does not require a coalescent theorem. Traditional rank-one eigenvalue-update methods and deterministic pivoting are distinct comparisons: they need not have the uniform independent pivot overhead addressed here.

## Limitations

The exact finite-time cancellation depends on a scalar identity plus a rank-one perturbation, exact eigendecomposition of each selected principal block, independent uniform coordinate selection, and identity action on zero off-diagonals. It does not establish finite termination or the same law for generic dense symmetric matrices, floating-point arithmetic, approximate Jacobi angles, different pivot selection policies, or rank higher than one. The block recurrence counts samples, not computational complexity per sample. Similarity to classical coalescent calculations means the probabilistic form is not claimed to be a new distribution; unindexed or incompletely inspected Jacobi literature could contain an equivalent matrix-specific statement.

## References

1. Isabel Detherage and Rikhav Shah, *Matrix Factorizations with Uniformly Random Pivoting*, arXiv:2505.02023, first publicly posted 2025-05-04, https://arxiv.org/abs/2505.02023.
2. Martin Möhle and Helmut Pitters, *Absorption Time and Tree Length of the Kingman Coalescent and the Gumbel Distribution*, arXiv:1502.03983, 2015, https://arxiv.org/abs/1502.03983.
