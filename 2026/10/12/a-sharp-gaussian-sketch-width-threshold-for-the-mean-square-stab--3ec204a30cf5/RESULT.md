# A sharp Gaussian-sketch width threshold for the mean-square stability of randomized LU pivots

## Finding

For a nonsingular real \(2\times2\) matrix \(A=(a_{ij})\), consider one rank-one LU cross update
\[
R=A-\frac{A_{:,j}A_{i,:}}{a_{ij}},
\]
where the pivot has \(a_{ij}\ne0\). Write \(s_2(A)>0\) for the smaller singular value and \(Z=\|R\|_F/s_2(A)\). The **exact squared-entry RPLU** chooses \((i,j)\) with probability \(a_{ij}^2/\|A\|_F^2\). Its **Gaussian-sketch variant of block width \(b\ge1\)** draws an independent \(2\times b\) standard Gaussian matrix \(\Omega\), chooses row \(i\) with probability proportional to \(\|A_{i,:}\Omega\|_2^2\), then column \(j\) within that row with probability proportional to \(a_{ij}^2\). All probabilities are unconditional over the Gaussian sketch and pivot draws.

The following is a sharp *sketch-size threshold*: 

1. For **every integer \(b\ge3\)** and every nonsingular real \(2\times2\) input,
\[
\mathbb E[Z_b^2]\le \frac{4b}{b-2}.
\]
For exact RPLU, \(\mathbb E[Z_{\mathrm{RPLU}}^2]\le4\).

2. For **\(b=1\) and \(b=2\)**, no finite uniform bound is possible, even for the diagonal positive-definite family \(D_e=\operatorname{diag}(e,1)\), \(0<e<1\). The exact results are
\[
\mathbb E[Z_1^2]=\frac1e,\qquad
\mathbb E[Z_2^2]=\frac{-2\log e}{1-e^2}.
\]
For every fixed integer \(b\ge3\), the same diagonal family has the finite exact limit
\[
\lim_{e\downarrow0}\mathbb E[Z_b^2]=1+\frac{b}{b-2}.
\]
Thus three Gaussian sketch columns are **necessary and sufficient** for a dimension-independent mean-square one-step approximation factor in the two-dimensional problem.

3. Even with \(b\ge3\), this cannot be upgraded to a uniform higher-than-second moment: for **every real \(p>2\)**, every integer \(b\ge1\), and exact RPLU, 
\[
\sup_{A\succ0,\ \kappa_2(A)\le2}\mathbb E[Z^p]=\infty.
\]
Indeed, for \(H_h=\begin{psmallmatrix}1&h\\h&1\end{psmallmatrix}\), \(0<h\le1/3\), both algorithms have exactly the same pivot distribution (for every \(b\ge1\)) and the complete moment law
\[
\mathbb E[Z^p]=\frac{(1+h)^p(1+h^{2-p})}{1+h^2},\qquad p>0.
\]
Moreover, for every \(T\ge4\), the exact strict-tail envelope along this well-conditioned family is
\[
\sup_{0<h\le1/3}\Pr\{Z>T\}=\frac{1}{1+(T-1)^2}.
\]
Therefore the polynomial upper-tail exponent \(2\) is optimal even among positive-definite inputs with condition numbers at most \(2\). This is a one-step, exact-arithmetic statement; no multi-iteration or finite-precision guarantee is claimed.

## Assumptions and scope

All matrices are real and nonsingular of order two. Singular values are Euclidean, and \(\|\cdot\|_F\) is Frobenius norm. Only nonzero entries may be pivoted; zero entries have zero selection probability. The Gaussian sketch consists of independent standard-normal entries and is independent of the input. For the lower bound in Part 2, \(D_e\) is positive definite with condition number \(1/e\). For Part 3, \(H_h\) is positive definite with condition number \((1+h)/(1-h)\le2\). The input is deterministic or independent of the sketch. The source algorithm of Divan and Gilles permits every \(b\ge1\), although its general expected-error theorem assumes \(b\ge3\).

## Proof

**Cross residual.** For every nonsingular \(2\times2\) matrix, pivoting on a nonzero entry \(a_{ij}\) annihilates row \(i\) and column \(j\). The sole surviving entry has absolute value \(|\det A|/|a_{ij}|\). Since \(|\det A|=s_1(A)s_2(A)\),
\[
Z_{ij}=\frac{s_1(A)}{|a_{ij}|}.
\]
Let \(N(A)\le4\) count nonzero entries. Under exact squared-entry RPLU,
\[
\mathbb E[Z^2]
=\sum_{a_{ij}\ne0}\frac{a_{ij}^2}{\|A\|_F^2}\frac{s_1(A)^2}{a_{ij}^2}
=\frac{N(A)s_1(A)^2}{s_1(A)^2+s_2(A)^2}\le4.
\]
This identity is also valid when some entries vanish.

**Uniform Gaussian-sketch bound for \(b\ge3\).** Denote row squared norms by \(w_i=\|A_{i,:}\|_2^2>0\), their total by \(W\), and unit row vectors by \(u_i\). Put \(X_i=\|u_i\Omega\|_2^2\); each marginal follows \(\chi_b^2\) and \(\widehat w_i=w_iX_i\). By Cauchy–Schwarz,
\[
W^2\le(\sum_i w_iX_i)(\sum_i w_i/X_i),
\]
so
\[
\mathbb E\left[\frac{w_iX_i}{\sum_jw_jX_j}\right]
\le\frac{w_i}{W^2}\sum_jw_j\mathbb E[X_i/X_j].
\]
For \(\rho=u_i^{\mathsf T}u_j\), conditional Gaussian regression represents the first projected row as \(\rho\) times the second plus an independent Gaussian vector scaled by \(\sqrt{1-\rho^2}\). Consequently,
\[
\mathbb E[X_i/X_j]=\rho^2+(1-\rho^2)b\mathbb E[(\chi_b^2)^{-1}]
=\frac{b-2\rho^2}{b-2}\le\frac b{b-2},
\]
where the inverse chi-square integral is finite exactly for \(b>2\). Thus the probability \(q_{ij}\) of selecting any pivot with the Gaussian sketch satisfies
\[
q_{ij}\le\frac b{b-2}\frac{a_{ij}^2}{W}.
\]
Multiplying each nonnegative squared residual by this domination and using the exact-RPLU identity proves \(\mathbb E[Z_b^2]\le4b/(b-2)\). No numerical experiment is used to prove the bound.

**Exact obstruction at small sketch widths.** Take \(D_e=\operatorname{diag}(e,1)\), where \(s_2(D_e)=e\). Its only possible pivots are the diagonal entries. If the first row is chosen, then \(Z=1/e\); otherwise \(Z=1\). Writing \(t=e^2\), the probability of choosing the first row is
\[
r_b(t)=\mathbb E\left[\frac{tX}{tX+Y}\right],
\quad X,Y\ \text{independent}\ \chi_b^2,
\]
and \(\mathbb E[Z_b^2]=1+(t^{-1}-1)r_b(t)\).

The random fraction \(U=X/(X+Y)\) has the \(\mathrm{Beta}(b/2,b/2)\) distribution. For \(b=1\), substitute \(U=\sin^2\theta\), with \(\theta\) uniform on \([0,\pi/2]\); direct integration gives
\[
r_1(t)=\frac{\sqrt t}{1+\sqrt t},
\quad \mathbb E[Z_1^2]=e^{-1}.
\]
For \(b=2\), \(U\) is uniform on \([0,1]\), so
\[
r_2(t)=\int_0^1\frac{tu}{1+(t-1)u}\,du
=\frac{t(t-1-\log t)}{(t-1)^2},
\quad \mathbb E[Z_2^2]=\frac{-\log t}{1-t}.
\]
For \(b\ge3\), as \(t\downarrow0\), monotone convergence yields
\[
\frac{r_b(t)}t\longrightarrow \mathbb E[X]\mathbb E[1/Y]=\frac b{b-2},
\]
giving the finite limit. This proves necessity as well as sufficiency of \(b\ge3\).

**Uniform high moments cannot hold.** For \(H_h\) the rows have equal Euclidean norms. Under exact RPLU, the combined probability of an off-diagonal pivot is \(h^2/(1+h^2)\). Under sketchy RPLU, exchanging the two coordinates of the Gaussian sketch interchanges the two sketched row norms in distribution, since \(H_h\) commutes with that permutation. Each row therefore has unconditional probability \(1/2\), for every \(b\ge1\). The within-row squared-entry rule then gives precisely the same off-diagonal probability. For diagonal pivots, \(Z=1+h\); for off-diagonal pivots, \(Z=(1+h)/h\). Summing these two possibilities proves the displayed moment formula. It tends to \(+\infty\) like \(h^{2-p}\) for \(p>2\); for \(p=2\), it tends to \(2\), whereas the input \(H_0=I\) has \(Z=1\) surely. Thus even the second moment is discontinuous at the identity, although uniformly bounded for \(b\ge3\).

For \(T\ge4\), the diagonal outcome is always below \(T\). The off-diagonal outcome exceeds \(T\) exactly if \(h<1/(T-1)\). Maximizing the increasing probability \(h^2/(1+h^2)\) on that strict interval produces the indicated nonattained supremum. Its asymptotic behavior is \(T^{-2}\), proving the optimal tail exponent.

## Verification

Run \(`python3 verify.py`\) in an environment with Python 3's standard library. The script independently constructs all four exact-rational cross residuals for 101 well-conditioned parameter values, checks their moments for five exponents, checks 360 deterministic sketch-coordinate-exchange identities, and numerically integrates the independent Beta-ratio formulas for twelve additional cases. The expected output contains two \(`VERIFY_OK`\) lines. Exact-rational finite checks support implementation accuracy only; the continuous-parameter and Gaussian-distribution conclusions are proved above.

## Relationship to prior work

Gilles and Wilber, *Low-Rank Approximation by Randomly Pivoted LU* (arXiv:2601.22344v1, January 29, 2026), introduced and analyzed entry-squared pivoting, including the one-step expected Gram residual and a general Frobenius mean-square bound. Divan and Gilles, *Convergence rates of randomly pivoted methods for low-rank approximation* (arXiv:2609.06287v1, September 5, 2026), introduced Gaussian sketchy pivoting, proved pivot-probability domination for \(b\ge3\), and established expected-error guarantees. Those exact results are acknowledged and reconstructed above. The present statement resolves the necessity of the sketch-width restriction for uniform mean-square accuracy, supplies exact small-width divergence laws, and establishes a high-moment and polynomial-tail impossibility even on uniformly conditioned positive-definite matrices. The related randomly pivoted Cholesky method samples only diagonal pivots of positive-semidefinite residuals and is not an identical update rule.

## Limitations

The universal moment bound and its sharp block-width obstruction are formulated for the first rank-one update in real two-dimensional matrices. The examples concern exact sketching, exact LU arithmetic, and independently generated Gaussian sketches, not finite-precision overflow or numerical safeguarding. For \(b=1,2\), the obstruction to universal mean-square accuracy uses ill-conditioned diagonal inputs; the separate obstruction to moments of order greater than two uses well-conditioned positive-definite inputs. The constants in the general upper bound for \(b\ge3\) are not asserted to be best possible. No higher-dimensional, multiple-step, or implementation-runtime claim is established.

## References

1. M. A. Gilles and H. Wilber, *Low-Rank Approximation by Randomly Pivoted LU*, arXiv:2601.22344v1, 2026-01-29, https://arxiv.org/abs/2601.22344.
2. R. Divan and M. A. Gilles, *Convergence rates of randomly pivoted methods for low-rank approximation*, arXiv:2609.06287v1, 2026-09-05, https://arxiv.org/abs/2609.06287.
3. Y. Chen, E. N. Epperly, J. A. Tropp, and R. J. Webber, *Randomly pivoted Cholesky: Practical approximation of a kernel matrix with few entry evaluations*, arXiv:2207.06503, 2022.
