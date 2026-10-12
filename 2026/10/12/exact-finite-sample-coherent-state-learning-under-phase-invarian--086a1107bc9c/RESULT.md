# Exact finite-sample coherent-state learning under phase-invariant amplitude priors

## Finding

Let \(n\ge1\) be an integer. A single unknown amplitude is \(\alpha=\sqrt R e^{i\Theta}\), where \(R\ge0\) has an arbitrary probability law and \(\Theta\) is independent and uniform on \([0,2\pi)\). One receives \(n\) identical training modes \(|\alpha\rangle\) and, with equal hypothesis probabilities, either a vacuum signal or another copy \(|\alpha\rangle\). After passive compression of the training modes, the two averaged states are
\[
\rho_0=\mathbb E_\alpha[|\sqrt n\alpha,0\rangle\langle\sqrt n\alpha,0|],\qquad
\rho_1=\mathbb E_\alpha[|\sqrt n\alpha,\alpha\rangle\langle\sqrt n\alpha,\alpha|].
\]
For every \(k\ge0\), set
\[
 a_k=\mathbb E\left[e^{-nR}\frac{(nR)^k}{k!}\right],\quad
 b_k=\mathbb E\left[e^{-(n+1)R}\frac{((n+1)R)^k}{k!}\right],\quad
 q_k=\left(\frac n{n+1}\right)^k.
\]
Then the exact optimal collective minimum-error probability is
\[
 \boxed{P_{\mathrm{err}}=\frac12-\frac14\sum_{k=0}^{\infty}
 \sqrt{(a_k-b_k)^2+4a_kb_k(1-q_k)}.}
\]
An optimal receiver first measures total photon number \(k\), then performs a binary Helstrom projection inside the two-dimensional span of \(|k,0\rangle\) and the normalized vector
\[
 |\phi_k\rangle=\frac{1}{(n+1)^{k/2}}
 \sum_{j=0}^k\sqrt{\binom{k}{j}}\,n^{j/2}|j,k-j\rangle.
\]
For \(k=0\) that span is one-dimensional. No measurement outside those spans is needed. Truncating the exact probability series after \(K\) gives an upper approximation with absolute error at most \(\frac14\sum_{k>K}(a_k+b_k)\).

For a centered circular complex Gaussian prior with \(\mathbb E|\alpha|^2=v>0\), the weights are exactly
\[
 a_k=\frac{(nv)^k}{(1+nv)^{k+1}},\qquad
 b_k=\frac{((n+1)v)^k}{(1+(n+1)v)^{k+1}},
\]
so the truncation error is at most
\[
 \frac14\left[\left(\frac{nv}{1+nv}\right)^{K+1}
 +\left(\frac{(n+1)v}{1+(n+1)v}\right)^{K+1}\right].
\]
In the local-energy scaling \(v=\mu^2/n\) with fixed \(\mu>0\), there is an exact nonregular asymptotic law
\[
 \boxed{\lim_{n\to\infty}\sqrt n\left(\frac12-P_{\mathrm{err}}\right)
 =\frac12\sum_{k=1}^\infty \frac{\mu^{2k}\sqrt{k}}{(1+\mu^2)^{k+1}}
 =\frac{\operatorname{Li}_{-1/2}(\mu^2/(1+\mu^2))}{2(1+\mu^2)}.}
\]
These equations are one theorem for circular-prior coherent-state learning: an exactly optimal finite-sample receiver and risk, with the Gaussian case and its local-energy limit evaluated explicitly.

## Assumptions and scope

Coherent states use the standard normalized Fock convention \(|z\rangle=e^{-|z|^2/2}\sum_{j\ge0}z^j|j\rangle/\sqrt{j!}\). The hypotheses have equal priors and refer to the same unknown amplitude, shared across training and reflected signal. The angular prior is uniform independently of the nonnegative intensity; the intensity distribution can be discrete, singular or continuous, with no moment assumptions. The training modes are jointly accessible and lossless and can be compressed to one mode by a passive number-preserving interferometer. This is the unconditional minimum-error quantum measurement, not an estimate-then-measure restriction.

## Proof

**Compression and sector decomposition.** Number-preserving interferometry maps \(|\alpha\rangle^{\otimes n}\) to \(|\sqrt n\alpha\rangle\otimes|0\rangle^{\otimes(n-1)}\), so discarding the known vacua does not change discrimination. In the two retained modes, fixing \(R=r\) and averaging the common uniform phase deletes matrix elements between different total photon numbers. Direct expansion gives
\[
 \rho_0=\bigoplus_{k=0}^\infty a_k|k,0\rangle\langle k,0|,
 \qquad
 \rho_1=\bigoplus_{k=0}^\infty b_k|\phi_k\rangle\langle\phi_k|.
\]
The binomial theorem normalizes every \(|\phi_k\rangle\), and \(|\langle k,0|\phi_k\rangle|^2=q_k\). The two weight sequences are probability distributions because, conditional on \(R\), they are Poisson probabilities with means \(nR\) and \((n+1)R\), respectively.

**Spectrum and optimality.** Each block difference is the Hermitian rank-at-most-two operator \(\Delta_k=b_k|\phi_k\rangle\langle\phi_k|-a_k|k,0\rangle\langle k,0|\). Its nonzero eigenvalues are
\[
 \lambda_{k,\pm}=\frac{b_k-a_k\pm\sqrt{(a_k+b_k)^2-4a_kb_kq_k}}2.
\]
Their product is \(-a_kb_k(1-q_k)\le0\), so the two signs are opposite unless one eigenvalue vanishes, and hence
\[
 \|\Delta_k\|_1=\sqrt{(a_k-b_k)^2+4a_kb_k(1-q_k)}.
\]
For \(k=0\), this becomes \(|b_0-a_0|\) as required. The differences are trace-class, since \(\sum_k(a_k+b_k)=2\). Thus the trace norm of their orthogonal direct sum is the sum of the block norms. Helstrom's equal-prior formula gives \(P_{\mathrm{err}}=\frac12-\frac14\|\rho_1-\rho_0\|_1\). Its maximizing positive/negative spectral projectors commute with total photon number, proving the optimal receiver. Also \(\|\Delta_k\|_1\le a_k+b_k\), proving the universal truncation bound.

**Gaussian specialization.** For \(\alpha\) circular complex normal with variance \(v\), the intensity has exponential density \(v^{-1}e^{-r/v}\) on \(r\ge0\). Integrating each Poisson probability against that density gives the displayed geometric weights, and summing their geometric tails gives the certified bound.

**Local-energy limit.** Fix \(x=\mu^2>0\), take \(v=x/n\), and let \(c_k=x^k/(1+x)^{k+1}\). Then \(a_k=c_k\), \(b_k\to c_k\), \(n(b_k-a_k)^2\to0\), and \(n(1-q_k)\to k\) for every fixed \(k\). Consequently \(\sqrt n\|\Delta_k\|_1\to 2c_k\sqrt{k}\). To exchange limit and sum, put \(r=2x/(1+2x)<1\). Uniformly in \(n\ge1\), both \(a_k\) and \(b_k\) are bounded by a constant times \(r^k\); applying the mean-value theorem to \(z^k/(1+z)^{k+1}\) for \(z\in[x,2x]\) gives \(\sqrt n|a_k-b_k|\le C_x(k+1)r^k\). Also \(n(1-q_k)\le k\), so \(2\sqrt{na_kb_k(1-q_k)}\le 2\sqrt{k}(a_k+b_k)\). These are summable majorants independent of \(n\); dominated convergence completes the limit. The polylogarithm expression is its defining absolutely convergent power series at \(r=x/(1+x)<1\).

## Verification

The included `verify.py` constructs the small photon-number block matrices directly from binomial number-state amplitudes for three rational parameter pairs and checks their trace and squared trace against the analytic expressions for \(k=0,\dots,8\). It independently evaluates two Gaussian finite-sample examples, tests the exact geometric tail bounds, and corroborates the singular scaling at large finite \(n\). Run `python3 verify.py` in the folder containing this report. The all-\(k\) and all-prior assertions are analytical consequences of the proof; finite cases are not exhaustive certification. For \(n=1,v=1\), the result gives \(P_{\mathrm{err}}\approx0.21356409008209\).

## Relationship to prior work

Sentís, Guţă, and Adesso (arXiv:1410.8700, 2014; EPJ Quantum Technology 2, 17, 2015) formulate exactly this vacuum-versus-unknown-coherent-state training task for a Gaussian prior. Their equations (5)--(11) specify the same averaged states and note that an exact finite-sample trace norm is generally difficult; their subsequent derivation uses a perturbative large-training limit at nonzero localization center. The present theorem takes the rotationally invariant, zero-center class and obtains an exact finite-sample block diagonalization, optimal measurement, and different local-energy scaling. It is not an exact solution for their general displaced-prior problem.

Sasaki and Carlini (arXiv:quant-ph/0202173, 2002) formulate universal quantum template matching for a family of qubit states, rather than the bosonic vacuum-versus-reflection model with circular amplitude mixing. The general Helstrom principle and number-sector twirling are established tools; this result claims neither of those ingredients as new, only their explicit all-radial-prior consequence and local-energy law in the indicated learning model.

## Limitations

Exact block reduction depends essentially on a common uniform phase and a shared amplitude between training and signal. A nonzero mean displacement breaks this total-photon-number block structure and is not covered. The optimal blockwise Helstrom projections are a mathematically specified joint POVM, not a claim of a passive-optics-only physical implementation. General radial priors have an exact convergent series but may lack a closed formula for its weights or a geometric convergence rate. The local-energy limit holds only for the specified centered Gaussian scaling and does not establish any general displaced-prior asymptotic formula. Equivalently phrased results under phase twirling or bosonic state-comparison terminology may exist outside the inspected literature; independent literature validation is not asserted.

## References

1. G. Sentís, M. Guţă and G. Adesso, *Quantum learning of coherent states*, arXiv:1410.8700 (first submitted 2014-10-31); EPJ Quantum Technology **2**, 17 (2015), doi:10.1140/epjqt/s40507-015-0030-4. https://arxiv.org/abs/1410.8700 ; https://link.springer.com/article/10.1140/epjqt/s40507-015-0030-4
2. M. Sasaki and A. Carlini, *Quantum learning and universal quantum matching machine*, arXiv:quant-ph/0202173 (2002); Physical Review A **66**, 022303 (2002). https://arxiv.org/abs/quant-ph/0202173
3. American Mathematical Society, Mathematics Subject Classification 2020, category 81P18 (quantum state tomography and discrimination). https://mathscinet.ams.org/mathscinet/msc/msc2020.html?s=81P18
