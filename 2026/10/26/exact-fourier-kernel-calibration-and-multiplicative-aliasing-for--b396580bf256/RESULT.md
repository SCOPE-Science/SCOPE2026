# Exact Fourier-kernel calibration and multiplicative aliasing for an expanding circle chain

## Finding
Let \(q\ge2\) be an integer and let \(U\) be uniform on \([0,1)\). Set \(X_t=q^tU\pmod 1\) for integers \(t\ge0\). For a finite nonempty \(M\subset\mathbb N\), positive weights \(a_m\), and the positive-definite kernel
\[
k(x,y)=\sum_{m\in M}a_m\cos(2\pi m(x-y)),
\]
define \(D_T^2=\operatorname{MMD}_k^2(T^{-1}\sum_{t=0}^{T-1}\delta_{X_t},\mathrm{Leb})\). Then for **every** integer \(T\ge1\),
\[
\mathbb E[T D_T^2]=\sum_{m\in M}a_m,
\]
exactly matching independent uniform observations. Factor each \(m\) uniquely as \(q^jr\) with \(q\nmid r\), and write \(A_r=\sum_{j:q^jr\in M}a_{q^jr}\). As \(T\to\infty\),
\[
T D_T^2\ \Longrightarrow\ \sum_{r}A_rE_r,
\]
where the variables \(E_r\) are independent mean-one exponentials. By comparison, the independent-uniform limit is \(\sum_{m\in M}a_mE_m\). **The two limiting laws agree if and only if** no two members of \(M\) lie in the same multiplicative orbit under multiplication by \(q\). Otherwise the limiting variance gap is strictly positive and equals
\[
\sum_r A_r^2-\sum_m a_m^2=2\sum_r\sum_{\substack{i<j\\q^ir,q^jr\in M}}a_{q^ir}a_{q^jr}>0.
\]
For the natural single-orbit case \(M=\{rq^j:j\in J\}\), where \(J\) is any finite nonempty set of nonnegative integers and \(q\nmid r\), there is also an **exact finite-sample variance formula**. Put \(h_{jk}=(T-|j-k|)_+\). Then
\[
\operatorname{Var}(T D_T^2)=T^{-2}\sum_{j,k\in J}a_{rq^j}a_{rq^k}\,h_{jk}(h_{jk}-1).
\]
For two consecutive frequencies with respective weights \(a,b>0\), this is
\[
(a^2+b^2)(1-T^{-1})+2ab(T-1)(T-2)T^{-2}.
\]
The usual independent-data limiting variance \(a^2+b^2\) is therefore strictly smaller than the actual asymptotic value \((a+b)^2\), although the expected squared discrepancy is identical at every sample size.

## Assumptions and scope
The initial state is uniform and hence the process is stationary under the deterministic map \(x\mapsto qx\pmod1\). All frequencies are positive integers; the set and weights remain fixed as \(T\to\infty\). The kernel is continuous, bounded, translation-invariant and positive definite, but the **finite-frequency kernel is not characteristic** on arbitrary probability measures. The theorem concerns its finite Fourier-feature discrepancy, not full weak convergence against every test function. All limits refer to randomness of the initial uniform state; the orbit after initialization is deterministic.

## Proof
**Step 1: Fourier identity and exact mean.** Writing \(e_m(x)=\exp(2\pi i mx)\) and \(S_{m,T}=\sum_{t=0}^{T-1}e_m(X_t)\), orthogonality of Fourier characters gives \(T D_T^2=\sum_m a_m|S_{m,T}|^2/T\). For \(s\ne t\), \(\mathbb E[e_m(X_t)\overline{e_m(X_s)}]=\int_0^1\exp(2\pi im(q^t-q^s)u)\,du=0\). Consequently \(\mathbb E|S_{m,T}|^2=T\), proving the exact mean.

**Step 2: A joint reverse-martingale central limit theorem.** The sigma fields \(\mathcal F_t=\sigma(X_t)\) decrease in \(t\). The conditional expectation, under uniform stationary measure, satisfies \(\mathbb E[e_r(X_t)\mid\mathcal F_{t+1}]=\mathcal Le_r(X_{t+1})\), where \(\mathcal Le_n=e_{n/q}\) if \(q\mid n\) and \(0\) otherwise (with the obvious interpretation of \(e_{n/q}\)). Thus \(e_r(X_t)\) is a bounded reverse-martingale difference for each primitive \(r\) with \(q\nmid r\). For any two such \(r,s\), the conditional covariance is \(\mathcal Le_{r-s}(X_{t+1})\), and the conditional pseudocovariance is \(\mathcal Le_{r+s}(X_{t+1})\). Their Cesàro averages converge almost surely to \(\mathbf1_{r=s}\) and \(0\), respectively: each nonconstant Fourier mode has zero spatial mean, and the expanding map is ergodic for Lebesgue measure (its base-\(q\) digit shift is Bernoulli). Boundedness yields the Lindeberg condition. The vector reverse-martingale central limit theorem therefore implies
\[
T^{-1/2}(S_{r,T})_{r\in R}\ \Longrightarrow\ (Z_r)_{r\in R},
\]
where \(Z_r\) are independent standard circular complex Gaussians, so \(|Z_r|^2\) are independent mean-one exponentials. The decreasing filtration can be read backward on each finite row; its conditional quadratic variation is the same Cesàro sum.

**Step 3: Exact aliasing.** If \(m=rq^j\), stationarity is not enough for this step: the orbit identity gives directly
\[
S_{m,T}=\sum_{t=j}^{T+j-1}e_r(X_t),\qquad |S_{m,T}-S_{r,T}|\le2j.
\]
Therefore all frequencies within one multiplicative orbit converge jointly to the same \(Z_r\). The continuous mapping theorem yields the asserted weighted exponential law. In the independent uniform experiment, distinct Fourier characters have orthogonal spatial covariance and zero pseudocovariance; the ordinary multivariate iid CLT instead produces independent \(Z_m\). Positive weights make the variance gap strictly positive whenever an orbit contains at least two selected frequencies, hence the two laws cannot agree then. When all selected orbits are distinct, the sums evidently have identical laws.

**Step 4: Exact finite-sample fourth moments.** Fix a single primitive \(r\), and write \(I_j=\{j,\ldots,j+T-1\}\). For nonnegative integers \(a,b,c,d\), the equality \(q^a+q^b=q^c+q^d\) implies equality of the two multisets \(\{a,b\}=\{c,d\}\): for \(q\ge3\) use the base-\(q\) digits, and for \(q=2\), unequal exponents give two 1-bits while coincident exponents give a single carried 1-bit, so the same conclusion holds. Therefore the Fourier integral of \(|S_{rq^j,T}|^2|S_{rq^k,T}|^2\) counts exactly the identity matching (\(T^2\) choices), the swapped matching (\(h_{jk}^2\) choices) and subtracts their intersection (\(h_{jk}\) choices). Thus
\[
\mathbb E[|S_{rq^j,T}|^2|S_{rq^k,T}|^2]=T^2+h_{jk}(h_{jk}-1).
\]
Subtracting the product of the means, dividing by \(T^2\), and summing with weights proves the exact variance formula, including \(T=1\).

## Verification
The standalone `verify.py` recomputes the fourth-moment Fourier integral directly by exhaustive integer-frequency quadruple counting for \(q\in\{2,3,5\}\), \(T\le8\), all shifts \(j,k\le4\) and several primitive frequencies; it checks the exact overlap formula in 2,418 cases. It independently checks the two-frequency weighted covariance by rational arithmetic. Run `python verify.py`; its recorded output is `verification_output.txt`. These finite checks only corroborate Step 4 and cannot replace the infinite-time reverse-martingale proof.

## Relationship to prior work
Kachaiev, Brogat-Motte, Villa and Rosasco (first posted October 9, 2026) investigate high-probability convergence of Markov empirical embeddings assuming a kernel contraction and an \(L^2\) spectral gap. They do not assert the above finite Fourier aliasing classification or the exact single-orbit finite-sample fourth moment. The deterministic expanding map has an isometric (generally non-surjective) Koopman operator on \(L^2\) and does not meet a strict \(L^2\) spectral-gap condition. Collet, Martínez and Schmitt (2004) establish general Gaussian-bridge convergence for empirical distributions of expanding interval maps; this supplies a related generic Gaussian-limit framework, not the stated exact finite-time MMD fourth-moment identity or the sharp iid-calibration condition. Classical reverse-martingale CLTs and iid Fourier central limit theory underpin, rather than constitute, the new calibration statement. Published related examples of expanding-circle correlations and of randomly switched expanding maps concern different statistics or dynamics.

## Limitations
The kernel has finite Fourier support and cannot distinguish all probability measures. The calibration theorem is a null-limit statement for stationary uniform starting states; it does not address nonuniform initial states, noninteger expansion, noisy or random maps, growing frequency collections, or nonasymptotic quantile errors. No claim is made that the general martingale CLT is new. The full 2004 primary manuscript could not be inspected through available lawful access, so specialized historical coverage remains an originality risk. Independent mathematical validation has not been performed.

## References
1. O. Kachaiev, L. Brogat-Motte, S. Villa and L. Rosasco, *Markov Chain Convergence in Kernel-Induced Geometry*, arXiv:2610.13916 (first public October 9, 2026). https://arxiv.org/abs/2610.13916
2. P. Collet, S. Martínez and B. Schmitt, *Asymptotic distribution of tests for expanding maps of the interval*, Ergodic Theory and Dynamical Systems 24 (2004), 707–722, doi:10.1017/S0143385703000476.
3. A. Gretton et al., *A Kernel Two-Sample Test*, Journal of Machine Learning Research 13 (2012), 723–773. https://jmlr.org/papers/v13/gretton12a.html
