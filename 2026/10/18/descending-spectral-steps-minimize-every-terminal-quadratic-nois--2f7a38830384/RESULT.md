# Descending spectral steps minimize every terminal quadratic noise risk

## Finding

Let \(H\in\mathbb R^{d\times d}\) be symmetric positive definite and let \(\alpha_1,\ldots,\alpha_N>0\) be a fixed multiset of gradient steps. For the quadratic \(f(x)=\tfrac12(x-x_\star)^\mathsf TH(x-x_\star)\), apply these steps in any permutation to independent centered gradient errors with common covariance \(Q\succeq0\). **The nonincreasing ordering of step lengths simultaneously minimizes the expected terminal error \(\mathbb E[e_N^\mathsf TWe_N]\) for every positive semidefinite spectral weight \(W\) commuting with \(H\)**. This covers squared Euclidean distance and objective suboptimality, even when the intermediate steps are individually unstable and when \(Q\) does not commute with \(H\).

For adjacent steps \(\alpha,\beta\), let \(T\) be the product of all subsequent noiseless update matrices. The exact terminal covariance exchange formula is
\[
C_{(\alpha,\beta)}-C_{(\beta,\alpha)}
=\alpha\beta(\beta-\alpha)T(HQ+QH)T,
\]
and the spectral-risk difference is
\[
\operatorname{tr}\bigl(W[C_{(\alpha,\beta)}-C_{(\beta,\alpha)}]\bigr)
=2\alpha\beta(\beta-\alpha)\operatorname{tr}(WHT^2Q).
\]
The last trace is nonnegative. Thus every inversion can be removed without increasing any such terminal risk.

If \(Q\succ0\), \(W\succ0\), and every adjacent inversion has a nonzero suffix product, its correction strictly improves risk. In particular, when the steps are the distinct reciprocals of *all* distinct eigenvalues of \(H\), the decreasing-step ordering is the unique minimizer of either squared Euclidean or quadratic-objective terminal expectation.

For isotropic noise \(Q=\sigma^2I\), the decreasing-step ordering additionally minimizes the **entire covariance matrix in Loewner order**. The Loewner assertion need not hold for correlated, noncommuting \(Q\), even though all spectral-weighted risks are still jointly minimized.

## Assumptions and scope

Fix any integers \(d,N\ge1\). Let \(H=H^\mathsf T\succ0\), \(e_0=x_0-x_\star\) be deterministic, and \(\xi_k\), \(1\le k\le N\), be mutually independent random vectors, independent of the initial state, with \(\mathbb E\xi_k=0\), \(\mathbb E\xi_k\xi_k^\mathsf T=Q\succeq0\), and finite second moments. For a permutation \(\pi\), use the exact-arithmetic recursion
\[
e_k=(I-\alpha_{\pi(k)}H)e_{k-1}-\alpha_{\pi(k)}\xi_k.
\]
The step lengths are fixed in advance, positive, and may exceed the ordinary monotone-descent limit. The matrix \(W\) is any symmetric positive semidefinite matrix satisfying \(WH=HW\), and does not depend on the ordering. The statement concerns the *terminal* moment after exactly \(N\) steps, not intermediate peak norm or convergence over repeated cycles.

## Proof

**1. The deterministic contribution is order-independent.** All matrices \(I-\alpha H\) commute, so the terminal mean is \(P(H)e_0\), where
\[
P(H)=\prod_{i=1}^{N}(I-\alpha_iH).
\]
This same vector contributes \(e_0^\mathsf TP(H)WP(H)e_0\) to every expected quadratic risk.

**2. Exact covariance propagation.** Put \(A_i=I-\alpha_iH\) and \(T_k=\prod_{j=k+1}^N A_{\pi(j)}\), with empty products equal to identity. Unrolling the recursion and using independence gives
\[
C_\pi:=\operatorname{Cov}(e_N)
=\sum_{k=1}^N\alpha_{\pi(k)}^2T_kQT_k.
\]
Every \(T_k\) is real symmetric and commutes with \(H\). No Gaussian assumption was used.

**3. Adjacent interchange.** Compare the arrangements \((\alpha,\beta)\) and \((\beta,\alpha)\) at two adjacent positions. Contributions from earlier noises are unchanged because their propagation passes through the same commuting product. Contributions from later noises are unchanged. Writing \(T\) for the product of later updates, the first arrangement contributes
\[
T\left[\alpha^2(I-\beta H)Q(I-\beta H)+\beta^2Q\right]T,
\]
while the second contributes
\[
T\left[\beta^2(I-\alpha H)Q(I-\alpha H)+\alpha^2Q\right]T.
\]
Expanding and canceling the \(HQH\) terms yields
\[
C_{(\alpha,\beta)}-C_{(\beta,\alpha)}
=\alpha\beta(\beta-\alpha)T(HQ+QH)T.
\]
For \(W\succeq0\) commuting with \(H\), cyclicity of trace and commutativity of \(T,W,H\) imply
\[
\operatorname{tr}(WT(HQ+QH)T)
=2\operatorname{tr}(WHT^2Q)\ge0.
\]
Indeed \(WHT^2\succeq0\) by simultaneous diagonalization; the trace of a product of two positive semidefinite matrices is nonnegative. Whenever \(\alpha>\beta\), placing \(\alpha\) before \(\beta\) therefore weakly lowers every spectral risk. Repeated adjacent swaps sort any permutation in nonincreasing order, proving simultaneous global optimality.

**4. Strictness.** If \(W\succ0\), \(Q\succ0\), and \(T\ne0\), then \(WHT^2\) is a nonzero positive semidefinite matrix and \(\operatorname{tr}(WHT^2Q)>0\). Each strict inversion swap therefore reduces the risk. If the steps are reciprocal to all distinct eigenvalues exactly once, the suffix of any adjacent inversion omits both reciprocal factors being interchanged. Their two eigenspaces remain nonzero under \(T\); hence \(T\ne0\). The sorted order is the unique minimizing order of those distinct steps.

**5. Covariance ordering and its boundary.** If \(HQ+QH\succeq0\), then the covariance exchange formula itself has the favorable Loewner sign, so the sorted order is Loewner-minimal. In particular, \(Q=\sigma^2I\) satisfies this condition. Conversely, let
\[
H=\operatorname{diag}(1,9),\qquad
Q=\begin{pmatrix}1&4/5\\4/5&1\end{pmatrix}.
\]
Both are positive definite, but
\[
HQ+QH=\begin{pmatrix}2&8\\8&18\end{pmatrix}
\]
has determinant \(-28\). For steps \(1\) then \(1/9\), versus the reverse, the covariance difference is a nonzero multiple of this indefinite matrix, so neither ordering dominates in Loewner order. The spectral-risk comparison remains valid.

**6. A sharp-order conflict with high-frequency-first scheduling.** Let \(H=\operatorname{diag}(1,\kappa)\), \(\kappa>1\), \(Q=\sigma^2I\), and use the exact spectral steps \(1\) and \(1/\kappa\). Both orders annihilate the deterministic terminal error. The covariance of descending steps \((1,1/\kappa)\) is
\[
C_{\mathrm{desc}}=\sigma^2\operatorname{diag}
\left((1-1/\kappa)^2+\kappa^{-2},\;\kappa^{-2}\right),
\]
whereas ascending steps \((1/\kappa,1)\) yield
\[
C_{\mathrm{asc}}=\sigma^2\operatorname{diag}
\left(1,\;1+(\kappa-1)^2/\kappa^2\right).
\]
The corresponding expected squared-error noise coefficients are \(1-2/\kappa+3/\kappa^2\) and \(3-2/\kappa+1/\kappa^2\). For the quadratic objective, the coefficients before the common factor \(\sigma^2/2\) are, respectively,
\[
1-1/\kappa+2/\kappa^2
\quad\text{and}\quad
2\kappa-1+1/\kappa.
\]
Thus the objective-noise cost of high-frequency-first ordering relative to the optimal reverse grows asymptotically like \(2\kappa\), unbounded with the condition number. This does not imply superior intermediate stability: the long first step \(1\) amplifies the high-frequency deterministic mode by \(\kappa-1\) before the next step annihilates it.

## Verification

Run `python check.py` with NumPy. The program recomputes terminal covariances by backward propagation, exhaustively compares all 24 permutations of four independently sampled positive steps for random symmetric positive-definite Hessians and arbitrary positive-definite noise covariances in dimensions two through six, and compares the exact adjacent exchange identity against direct matrix covariance calculations. It also verifies the two-dimensional closed forms and gives a positive-definite correlated-noise counterexample to Loewner ordering. The finite experiments are diagnostic only; the all-dimensional statements follow from the exact trace argument above.

## Relationship to prior work

Zhou and Gu (2026) propose a high-frequency-first Hanoi ordering to control deterministic spectral rebound in quadratic gradient methods. The direction here is intentionally different: it concerns fixed, preselected steps and **persistent independent gradient-oracle noise**, for which the exact *terminal* stochastic risk rewards reverse ordering. Their accessible abstract does not report this stochastic ordering theorem; the complete preprint could not be checked, so possible overlap in uninspected material remains a risk.

Classical analyses of Chebyshev parameter ordering, including Lebedev and Finogenov (1973), emphasize suppressing intermediate amplification. Gutknecht and Röllin (2002) analyze the numerical effects of local floating-point errors in iterative implementations. Fox and Parker develop nonstationary stochastic solvers and Chebyshev-accelerated Gaussian samplers with step-dependent noise covariances selected to preserve a target stationary distribution. These are mathematically related but differ from optimizing a fixed multiset under a common gradient-oracle covariance. No claim is made that decreasing learning rates or covariance propagation as such are new.

## Limitations

The guarantee is about a fixed finite horizon and quadratic objectives with a *time-independent*, additive, mean-zero gradient-noise covariance. It does not apply as stated to multiplicative/state-dependent stochastic gradients, correlated noise across iterations, variable covariances, finite-precision roundoff, or adaptive step decisions. Arbitrary long early steps may cause very large intermediate iterates, so the terminal-risk optimum is not a robust floating-point recommendation. The covariance Loewner minimum requires the additional sufficient condition \(HQ+QH\succeq0\), whereas spectral-weighted trace minimality does not.

## References

1. Y. Zhou and R. Gu, *Structured Spectral Step-Sizes and a Hanoi Ordering Principle for Gradient Methods*, arXiv:2606.25311, first posted 2026-06-24. https://arxiv.org/abs/2606.25311
2. V. I. Lebedev and S. A. Finogenov, *Solution of the problem of parameter ordering in Chebyshev iteration methods*, Zh. Vychisl. Mat. Mat. Fiz. 13(1) (1973), 18–33. https://www.mathnet.ru/eng/zvmmf6595
3. M. H. Gutknecht and S. Röllin, *The Chebyshev iteration revisited*, Parallel Computing 28 (2002), 263–283. https://www.sam.math.ethz.ch/~mhg/pub/Cheby-02ParComp.pdf
4. C. Fox and A. Parker, *Convergence in Variance of First-Order and Second-Order Chebyshev Accelerated Gibbs Samplers*, manuscript, https://www.physics.otago.ac.nz/data/fox/publications/SIAM_CS_2012-11-30.pdf
