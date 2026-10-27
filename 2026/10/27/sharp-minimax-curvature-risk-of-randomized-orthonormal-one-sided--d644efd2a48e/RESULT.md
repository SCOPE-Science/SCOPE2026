# Sharp minimax curvature risk of randomized orthonormal one-sided numerical differentiation

## Finding

Consider the one-sided, \(k+1\)-evaluation estimator of a gradient projected onto a fixed \(k\)-dimensional subspace, obtained by probing along an orthonormal basis of that subspace. For quadratic objectives, its entire basis dependence is the squared Euclidean norm of the diagonal of the compressed Hessian in the chosen basis. This yields exact attainable best and worst errors and a sharp minimax theorem when the compressed Hessian eigenvectors are unknown.

More precisely, let \(C\) denote the real symmetric \(k\)-by-\(k\) compressed Hessian and let \(h>0\). The minimum and maximum **squared** estimation errors over all orthonormal probe bases are, respectively,
\[
 E_{\min}=\frac{h^2}{4k}(\operatorname{tr}C)^2,
 \qquad E_{\max}=\frac{h^2}{4}\operatorname{tr}(C^2).
\]
If the designer chooses any probability law on orthonormal bases before an adversary chooses the eigenvector orientation of \(C\), with its eigenvalues fixed, the sharp minimax expected squared error is
\[
 E_{\mathrm{mm}}=\frac{h^2}{4(k+2)}\bigl[(\operatorname{tr}C)^2+2\operatorname{tr}(C^2)\bigr].
\]
The Haar-uniform orthonormal basis attains this value simultaneously for every orientation; no other distribution can have a smaller worst-orientation risk. Its estimator is unbiased for the projected gradient on every quadratic, despite using one-sided differences.

In particular, a curvature-aware basis makes the estimator **exact at every point and every positive step length** if and only if \(\operatorname{tr}C=0\). For a rank-one positive-semidefinite compressed Hessian, switching from an eigenbasis to a Haar basis cuts expected squared error by the exact factor \(3/(k+2)\); a curvature-aware balanced basis cuts it by \(1/k\).

## Assumptions and scope

Let \(d\ge k\ge1\) be integers, \(S\subseteq\mathbb R^d\) a fixed \(k\)-dimensional linear subspace, and \(B_0\in\mathbb R^{d\times k}\) any matrix with orthonormal columns spanning \(S\). Let
\[
 f(x)=c+\ell^{\mathsf T}x+\tfrac12x^{\mathsf T}Hx,
 \qquad H=H^{\mathsf T}\in\mathbb R^{d\times d},
 \qquad C=B_0^{\mathsf T}HB_0.
\]
Neither convexity nor invertibility is assumed. For any orthonormal basis matrix \(B=[b_1,\ldots,b_k]=B_0Q\), where \(Q\in O(k)\), define
\[
 D_{B,h}f(x)=\sum_{j=1}^k\frac{f(x+hb_j)-f(x)}{h}b_j,
 \qquad P_S=B_0B_0^{\mathsf T}.
\]
The common value \(f(x)\) is reused, so this requires \(k+1\) function evaluations; the analysis is in exact arithmetic without evaluation noise. Squared error means \(\|D_{B,h}f(x)-P_S\nabla f(x)\|_2^2\), not total optimization error. For minimax risk, the adversary ranges over all \(U\in O(k)\), replacing \(C\) by \(UCU^{\mathsf T}\); the designer must choose a distribution on \(Q\in O(k)\) independently of the unknown \(U\). The spectral multiset of \(C\) is held fixed. The theorem includes \(k=1\), with the evident zero orientation gap.

## Proof

**Exact finite-difference identity.** A quadratic expansion gives, for every unit probe \(b\),
\[
 \frac{f(x+hb)-f(x)}h=b^{\mathsf T}\nabla f(x)+\frac h2b^{\mathsf T}Hb.
\]
Consequently
\[
 D_{B,h}f(x)-P_S\nabla f(x)
 =\frac h2\sum_{j=1}^k(b_j^{\mathsf T}Hb_j)b_j,
\]
and orthonormality gives
\[
 \|D_{B,h}f(x)-P_S\nabla f(x)\|_2^2
 =\frac{h^2}4\sum_{j=1}^k\bigl[(Q^{\mathsf T}CQ)_{jj}\bigr]^2. \tag{1}
\]
This is independent of \(x\) and of the linear term of \(f\).

**All attainable extrema.** The diagonal entries of \(Q^{\mathsf T}CQ\) sum to \(\operatorname{tr}C\), so Cauchy--Schwarz bounds the sum of their squares below by \((\operatorname{tr}C)^2/k\), with equality precisely when all diagonal entries are equal. Such a real orthonormal basis always exists: if \(k>1\), the mean eigenvalue lies between the smallest and largest eigenvalue, so continuity of the Rayleigh quotient supplies a unit vector having quotient exactly the mean. Compress to its orthogonal complement, whose remaining trace equals \((k-1)\) times the same mean, and apply induction. The case \(k=1\) is immediate. Conversely, orthogonal invariance of the Frobenius norm yields
\[
 \sum_j[(Q^{\mathsf T}CQ)_{jj}]^2
 \le\|Q^{\mathsf T}CQ\|_F^2=\operatorname{tr}(C^2),
\]
with equality if and only if all off-diagonal entries vanish, i.e., the selected basis diagonalizes \(C\). This establishes the stated minimum and maximum. Exactness of some basis is equivalent to vanishing minimum, hence to \(\operatorname{tr}C=0\), including for indefinite \(C\).

**Haar risk and unbiasedness.** For a Haar-uniform \(Q\in O(k)\), each column \(q_j\) is uniform on the unit sphere. The exact spherical fourth moment is
\[
 \mathbb E[(q_j^{\mathsf T}Cq_j)^2]
 =\frac{(\operatorname{tr}C)^2+2\operatorname{tr}(C^2)}{k(k+2)}.
\]
It follows from \(\mathbb E[q_a^4]=3/[k(k+2)]\) and \(\mathbb E[q_a^2q_b^2]=1/[k(k+2)]\) for distinct coordinates, first in an eigenbasis and then by orthogonal invariance. Summing over \(k\) columns in (1) yields \(E_{\mathrm{mm}}\). Also, right multiplication of \(Q\) by a diagonal sign matrix preserves Haar law but changes the sign of one corresponding vector in the error expression; each error component therefore averages to zero. Thus \(\mathbb E[D_{B,h}f(x)]=P_S\nabla f(x)\) exactly for every \(h>0\).

**Sharp minimax property.** Let \(\mu\) be any distribution on designer frames \(Q\), independent of adversarial orientation \(U\). For any fixed \(Q\), averaging the squared error over Haar-distributed \(U\) gives \(E_{\mathrm{mm}}\), since \(U^{\mathsf T}Q\) is Haar. Hence
\[
 \sup_{U\in O(k)}\mathbb E_{Q\sim\mu}\bigl[\operatorname{error}^2(U,Q)\bigr]
 \ge\mathbb E_{U\sim\mathrm{Haar}}\mathbb E_{Q\sim\mu}
 \bigl[\operatorname{error}^2(U,Q)\bigr]=E_{\mathrm{mm}}.
\]
Choosing Haar \(\mu\) makes the expected error independent of \(U\) and equal to \(E_{\mathrm{mm}}\), proving equality and optimality against every frame distribution, including deterministic ones. No uniqueness of the optimal distribution is claimed.

**Cost-preserving randomized signs for general smooth functions.** Fix any orthonormal basis and independently select signs \(\varepsilon_j\in\{-1,1\}\) uniformly, probing along \(\varepsilon_jb_j\). The same \(k+1\) evaluations suffice. For any \(C^3\) function, the expected signed estimator is the projected centered-difference vector
\[
 \mathbb E_\varepsilon D_{B\operatorname{diag}(\varepsilon),h}f(x)
 =\sum_{j=1}^k\frac{f(x+hb_j)-f(x-hb_j)}{2h}b_j.
\]
If all third directional derivatives along the displayed line segments have magnitude at most \(M\), Taylor's formula and orthonormality imply
\[
 \bigl\|\mathbb E_\varepsilon D_{B\operatorname{diag}(\varepsilon),h}f(x)
       -P_S\nabla f(x)\bigr\|_2\le\frac{M h^2\sqrt{k}}6.
\]
This is a bias-of-expectation statement; randomization need not improve a single-sample mean-square error. For quadratics \(M=0\), it reduces to the exact unbiasedness already proved.

## Verification

Run `python verify.py` in an environment with NumPy and SymPy. The standalone program checks an exact rational two-dimensional rotation, independent sign unbiasedness, an exact traceless-indefinite zero-error rotation, a rank-one four-dimensional Hadamard balancing frame, and numerical realizations of (1) and its extrema. It also checks the Haar second-moment formula against reproducibly seeded simulations. In the present reproduction it passed 4 exact rational/symbolic cases, 900 deterministic numerical identities/inequalities, and 54,000 Haar frame samples. Simulations are sanity checks only; all universal, minimax and exactness assertions follow from the preceding algebraic argument.

The \(k=2\) traceless example \(C=\operatorname{diag}(1,-1)\) is instructive. In an eigenbasis the squared bias is \(h^2/2\); after a \(45^\circ\) rotation both diagonal curvatures vanish, giving exact differentiation for all \(h\). The opposite rank-one positive-semidefinite case \(C=\operatorname{diag}(4,0,0,0)\) has squared error \(4h^2\) in an eigenbasis and \(h^2\) in a balanced Hadamard frame, with Haar risk \(2h^2\) by the displayed formula.

## Relationship to prior work

Ryabchenko, Qian and Mou (arXiv:2609.08277v1, September 8, 2026), Section 4.1, Algorithm 2 and Lemma 4.1, introduce precisely the one-sided projected-gradient estimator examined here and prove the general smoothness estimate \(\|D_{B,h}f-P_S\nabla f\|_2^2\le kh^2L^2/4\). Their argument does not identify the exact quadratic basis dependence, matched-basis extrema, adversarial-orientation minimax risk, or Haar moment law. Their broader gradient-estimation and convergence guarantees are not contradicted.

Abdul Fattah, Van Niekerk and Rue (arXiv:2106.07313v1, June 14, 2021), Sections 2--3 and Appendix A, study basis rotation for numerical gradients, principally with **central differences**. Quadratic curvature bias cancels under central differencing at double-sided evaluation cost; this does not establish the one-sided \(k+1\)-evaluation error frontier or minimax distribution above. The classical real Schur--Horn diagonal theorem (see Devadas, Haine and Stubis, 2015) implies the balanced-diagonal existence used here; it is explicitly treated as prior mathematical background, not a new standalone theorem. The spherical fourth moments and group-averaging method are likewise classical ingredients. The asserted contribution is their exact numerical-differentiation and sharp adversarial-frame-risk consequence for this particular estimator, not independent novelty of those ingredients.

## Limitations

The exact error range and minimax formula rely on a quadratic objective, exact function values, an orthonormal \(k\)-frame, a common positive step length, and a distribution over frames chosen independently of the unknown curvature orientation. They do not characterize adaptive frame selection that learns curvature through earlier queries; nor do they prove convergence rates for full zeroth-order optimization with finite probes. The signed-frame \(C^3\) bound controls expected bias only and does not claim second-order single-run mean-square accuracy. Constructing the best deterministic frame generally requires curvature information; the Haar minimax strategy does not. Equivalent prior special-case results outside the inspected sources cannot be excluded without broader expert review.

## References

1. A. Ryabchenko, J. Qian and W. Mou, *Adaptively Incorporating Directional Hints into Zeroth-Order Optimization*, arXiv:2609.08277v1, September 8, 2026, especially Section 4.1, Algorithm 2, Lemma 4.1 and Appendix D.1. https://arxiv.org/pdf/2609.08277
2. E. H. Abdul Fattah, J. Van Niekerk and H. Rue, *Smart Gradient -- An Adaptive Technique for Improving Gradient Estimation*, arXiv:2106.07313v1, June 14, 2021, Sections 2--3, Appendix A. https://arxiv.org/pdf/2106.07313
3. S. Devadas, P. J. Haine and K. Stubis, *The Schur--Horn Theorem*, manuscript dated May 13, 2015, real diagonal majorization background. https://math.berkeley.edu/~phaine/files/Schur-Horn.pdf
