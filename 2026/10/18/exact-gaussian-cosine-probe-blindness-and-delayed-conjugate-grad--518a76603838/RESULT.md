# Exact Gaussian cosine-probe blindness and delayed conjugate gradients

## Finding

The flattened Gaussian cosine diagnostic of an SPD operator admits a complete finite-dimensional law on two-eigenvalue spectra, with a sparse-spectral crossover independent of the number of probes. More decisively, there is a sequence of positive diagonal matrices on which the cosine diagnostic converges to zero in mean and probability uniformly in the probe count, while a right-hand side exists for which conjugate gradients makes asymptotically no relative energy-error progress after an arbitrarily growing number of steps.

**Exact diagnostic.** For integers \(n\ge2\), \(1\le r<n\), \(s\ge1\), real \(K>1\), an orthogonal rank-\(r\) projector \(P\), and independent standard-normal entries of \(Z\in\mathbb R^{n\times s}\), set \(B=I+(K-1)P\) and
\[
\mathcal L_s(B,Z)=1-\frac{\langle Z,BZ\rangle_F}{\|Z\|_F\|BZ\|_F}.
\]
With \(T\sim\operatorname{Beta}(rs/2,(n-r)s/2)\),
\[
\mathcal L_s\overset d=1-\frac{1+(K-1)T}{\sqrt{1+(K^2-1)T}}.
\]
Its exact support is \([0,1-2\sqrt K/(K+1)]\). For \(0<\ell<1-2\sqrt K/(K+1)\), write \(u=1-\ell\) and
\[
t_\pm=\frac{u^2(K+1)-2\pm u\sqrt{u^2(K+1)^2-4K}}{2(K-1)}.
\]
Then its cumulative distribution function is
\[
\Pr\{\mathcal L_s\le\ell\}=I_{t_-}(rs/2,(n-r)s/2)+1-I_{t_+}(rs/2,(n-r)s/2),
\]
where \(I_t\) denotes the regularized incomplete beta function; the CDF is zero below and one above the stated support.

**Sparse-spectral crossover.** Suppose \(n\to\infty\), \(r=r_n<n\) with \(r_n/n\to0\), \(s=s_n\ge1\), and \(K=K_n>1\). Put \(\vartheta_n=K_n\sqrt{r_n/n}\) and \(q_n=r_ns_n\). If \(\vartheta_n\to c\in[0,\infty)\) and \(q_n\to q\) for a finite positive integer \(q\), then
\[
\mathcal L_{s_n}\ \xrightarrow{d}\ 1-(1+c^2W_q)^{-1/2},\qquad W_q=\chi_q^2/q.
\]
If instead \(q_n\to\infty\), the limit is the constant \(1-(1+c^2)^{-1/2}\). If \(\vartheta_n\to\infty\), the loss converges to \(1\) in probability. In the weak regime \(\vartheta_n\to0\), the finer normalization obeys
\[
\frac{2n\mathcal L_{s_n}}{(K_n-1)^2r_n}\xrightarrow{d}W_q
\]
for finite \(q\), and converges in probability to \(1\) when \(q_n\to\infty\). Thus increasing the probe count concentrates, but does not move, the crossover \(K\asymp\sqrt{n/r}\).

**Conjugate-gradient obstruction.** For every integer \(k\ge2\), every \(K>1\), and every integer \(n\ge k+1\), define
\[
\lambda_j=\frac{K+1}{2}+\frac{K-1}{2}\cos(j\pi/k),\quad j=0,\ldots,k,
\]
\(A=\operatorname{diag}(\lambda_0,\ldots,\lambda_k,1,\ldots,1)\), and take identity preconditioning. The eigenvalues of \(A\) lie in \([1,K]\), and at most \(k\) eigenvalues differ from \(1\). For any \(s\ge1\),
\[
0\le\mathbb E\mathcal L_s(A,Z)\le\frac{k(K-1)^2}{n}.
\]
There exists an explicit right-hand side \(b\) such that starting conjugate gradients at zero leaves, after exactly \(k\) iterations, the sharp relative energy error
\[
\frac{\|x_*-x_k\|_A}{\|x_*\|_A}=\frac1{T_k((K+1)/(K-1))}=\operatorname{sech}\!\left(k\operatorname{arcosh}\frac{K+1}{K-1}\right).
\]
In particular choose \(K=k^4\) and \(n=k^{10}\); then the expected probe loss is at most \(1/k\), for every probe count (even increasing counts), while the displayed exact relative error tends to \(1\). The same loss statement holds after the two Jacobi probe-smoothing sweeps with damping \(0.6\) specified in the motivating method, since for a diagonal positive matrix both sweeps simply multiply all Gaussian probes by \(0.16\).

## Assumptions and scope

All matrices and probes are real; all calculations are in exact arithmetic. The diagnostic uses **one flattened Frobenius cosine over all probes**, not an average of separately normalized probe cosines. \(A\) is a fixed diagonal SPD matrix independent of the probes. The displayed CG lower-performance example concerns a carefully selected right-hand side, not Gaussian or application-specific right-hand sides. Identity preconditioning is an admissible baseline, not a claim about an output of any trained preconditioner. For the sparse-spectral limits, only the stated asymptotic hypotheses are used; in the fixed finite-\(q\) case the limit law is a chi-square mixture.

## Proof

**1. Gaussian splitting, exact CDF, and maximum.** Orthogonally diagonalize \(P\). The independent Gaussian squared norms \(X=\|PZ\|_F^2\) and \(Y=\|(I-P)Z\|_F^2\) have \(\chi^2_{rs}\) and \(\chi^2_{(n-r)s}\) laws. Hence \(T=X/(X+Y)\) has the claimed beta law. The three quadratic forms in the loss are \(X+Y\), \(KX+Y\), and \(K^2X+Y\), proving the distribution identity. Differentiating its cosine factor shows its sole interior minimum at \(T=1/(K+1)\) and value \(2\sqrt K/(K+1)\); the loss equals zero at both endpoints. Squaring the positive cosine equation and solving the quadratic gives exactly \(t_-,t_+\), with the loss exceeding \(\ell\) strictly between the two roots. Beta integration yields the CDF without changing orientations or missing either branch.

**2. Crossover.** The beta representation gives \(W_n=(n/r)T\xrightarrow d\chi_q^2/q\) whenever \(rs\to q\) (a finite integer), since \(Y/(ns)\to1\) in probability; when \(rs\to\infty\), the beta variance gives \(W_n\to1\) in probability. Thus \(T\to0\), \(K T=(K\sqrt{r/n})\sqrt{r/n}\,W_n\to0\) in probability whenever the first factor stays bounded, and \(K^2T\to c^2W\). This gives the critical limit. For \(\vartheta_n\to\infty\), the cosine is bounded by \(\sqrt{T}+1/(K\sqrt{T})\), both terms tending to zero in probability; \(W_n\) has no limiting atom at zero. For weak scaling, rationalize the loss exactly:
\[
\mathcal L_s=\frac{(K-1)^2T(1-T)}{\sqrt{1+(K^2-1)T}\bigl[\sqrt{1+(K^2-1)T}+1+(K-1)T\bigr]}.
\]
The denominator tends to \(2\) in probability and \(T/(r/n)=W_n\), proving the normalized limits.

**3. Uniform expectation bound.** Flatten \(Z\) into \(z\) and put \(v=(I+E)z\) for any symmetric \(E\succeq0\). Their cosine is nonnegative. Their sine satisfies \(\sin\angle(z,v)\le\|Ez\|/\|z\|\) because the perpendicular component of \(v\) is the perpendicular component of \(Ez\). Consequently \(1-\cos\angle(z,v)\le\sin^2\angle(z,v)\le\|Ez\|^2/\|z\|^2\). Gaussian rotational symmetry in dimension \(ns\) gives
\[
\mathbb E\frac{\|EZ\|_F^2}{\|Z\|_F^2}=\frac{\operatorname{tr}(E^2)}n.
\]
For the specified diagonal \(A\), at most \(k\) positive deviations are bounded by \(K-1\), hence \(\operatorname{tr}(A-I)^2\le k(K-1)^2\). Markov's inequality also gives convergence in probability whenever the right-hand bound vanishes. This bound is valid for every positive integer \(s\), not merely a fixed probe count.

**4. Exact CG extremizer.** Write \(c_0=c_k=1/2\), \(c_j=1\) for interior \(j\), and
\[
w_j=\frac{c_j/\lambda_j}{\sum_{i=0}^k c_i/\lambda_i},\qquad e_{0,j}=\sqrt{w_j/\lambda_j},\qquad b=Ae_0,
\]
with remaining coordinates zero. Then \(\|e_0\|_A=1\). Let \(\delta=1/T_k((K+1)/(K-1))\) and
\[
p_k(\lambda)=\frac{T_k((2\lambda-K-1)/(K-1))}{T_k(-(K+1)/(K-1))}.
\]
We have \(p_k(0)=1\) and \(p_k(\lambda_j)=(-1)^{j+k}\delta\). Classical Chebyshev-Lobatto barycentric weights give the elementary interpolation identity \(\sum_{j=0}^k(-1)^jc_j h(\lambda_j)=0\) for any polynomial of degree at most \(k-1\): it follows by comparing the leading coefficient in the Lagrange interpolation formula and using \(1/\prod_{i\ne j}(\lambda_j-\lambda_i)\propto(-1)^jc_j\). Therefore \(\sum_jw_jp_k(\lambda_j)\lambda_j h(\lambda_j)=0\) for all such \(h\). Every admissible degree-\(k\) CG error polynomial is \(p_k+\lambda h\), so this vanishing cross term proves \(p_k\) uniquely minimizes the squared \(A\)-energy error \(\sum_jw_jp(\lambda_j)^2\). The minimizing value is \(\delta^2\), establishing the exact CG ratio. This is the classical CG polynomial extremal mechanism applied with an explicitly chosen discrete spectral measure, not a claim of discovering Chebyshev extremality.

**5. Asymptotic obstruction and smoothing.** For \(K=k^4,n=k^{10}\), the loss bound is at most \(k\cdot k^8/k^{10}=1/k\). Meanwhile \(k\operatorname{arcosh}((K+1)/(K-1))\sim 2k/\sqrt K=2/k\), so \(\delta\to1\). On each diagonal positive \(A\), the damped-Jacobi operator \(I-0.6\operatorname{diag}(A)^{-1}A\) equals \(0.4I\). Two sweeps multiply every probe by \(0.16\), which cancels out of the normalized cosine.

## Verification

The standalone `verify_cosine.py` reproduces the exact incomplete-beta CDF against direct Gaussian sampling; checks the Gaussian quadratic-ratio identity; checks the CG polynomial orthogonality at high precision and by direct finite-dimensional CG; checks two Jacobi smoothing sweeps; and evaluates the asymptotic construction. Run with `python verify_cosine.py` using NumPy, SciPy, and mpmath. Its finite tests supplement but do not replace the exact proof above.

## Relationship to prior work

Osborne, Guo, Owens, and Matusik (2026, §6.1 and supplementary probe procedure) define the *same flattened cosine objective* and specify Gaussian probes with two damped-Jacobi smoothing sweeps. Their work establishes positive-scale invariance, formulates the objective as angular distance, and reports numerical performance; the exact beta CDF, the sparse-spectral phase law, and the uniform-in-probe-count Chebyshev CG obstruction established here are distinct questions. Their paper also recalls classical CG polynomial convergence theory. Yang et al. (2025, §3.3) develop a different sparse-approximate-inverse learning objective and compare cosine variants. The two-eigenvalue angular extremum is an instance of the classical Kantorovich inequality, and Chebyshev polynomial CG worst-case constructions are classical; the point is their precise **joint relation to the stated global probe diagnostic**, including the diagnostic's dependence on probe batch size and smoothing. Database and primary-literature comparison did not identify the combined quantitative statement; this does not prove uniqueness.

## Limitations

The construction uses diagonal SPD operators and identity preconditioning, and the slow-CG right-hand side is designed adversarially. It is not a statement about the accuracy of any learned preconditioner, actual physics simulation inputs, average-CG behavior, or floating-point implementations. The standalone two-eigenvalue probe distribution alone does **not** imply delayed CG: a two-eigenvalue SPD system is solved by CG in at most two steps. The delayed-CG statement requires the separate \(k+1\)-node spectral construction. The exact CDF assumes iid real Gaussian probes and a single global cosine; correlated or nontrivially smoothed probes generally have a different law. Unindexed literature or equivalent older spectral extremal analyses may exist, and independent external review has not been performed.

## References

1. C. Osborne, M. Guo, C. Owens, and W. Matusik, *Hierarchical Transformer Preconditioning for Interactive Physics Simulation*, arXiv:2605.13343v1 (13 May 2026); accessible full-text revision: https://arxiv.org/html/2605.13343v2 , especially §6.1, §6.2, and supplementary §3.
2. Y. Yang et al., *Learning Sparse Approximate Inverse Preconditioners for Conjugate Gradient Solvers on GPUs*, arXiv:2510.27517v1 (31 October 2025), https://arxiv.org/html/2510.27517v1 , especially §§3.3 and 4.4.
3. Y. Saad, *Iterative Methods for Sparse Linear Systems*, 2nd ed., 2003; classical CG minimax-polynomial convergence theory.
4. Classical Kantorovich inequality for the angular factor between a vector and its SPD image, and Chebyshev-Lobatto interpolation identities (credited mathematical background).
