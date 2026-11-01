# Rational pointwise-unitary Toeplitz symbols have closed numerical ranges

## Finding

Let \(M:\mathbb T\to M_m(\mathbb C)\) have rational entries without poles on the unit circle and assume that for every \(\zeta\in\mathbb T\) there is some unitary \(U_\zeta\) (with no continuity or rationality assumption on its selection) such that \(M(\zeta)=U_\zeta A U_\zeta^*\) for one fixed \(A\in M_m(\mathbb C)\). If \(T_M=P_+M|_{H^2(\mathbb D,\mathbb C^m)}\), then

\[W(T_M)=W(A).\]

In particular, the numerical range is **closed**, and each extreme point of the finite-matrix numerical range has an **analytic-polynomial vector witness** for the Toeplitz operator. As an application, whenever a bidisk rational inner function factors as \(\Theta(z_1,z_2)=B_1(z_1)B_2(z_2)\) with finite Blaschke products, the numerical ranges of both Agler-compressed coordinate shifts are closed for **every** permitted Agler decomposition and choice of basis. The degenerate zero-dimensional compression has empty numerical range and is included.

The rationality assumption is genuinely substantive. The real-analytic, nonrational projection symbol

\[u(\zeta)=\exp(\zeta-\zeta^{-1}),\qquad P(\zeta)=\frac12\begin{pmatrix}1&\overline{u(\zeta)}\\u(\zeta)&1\end{pmatrix}\]

is pointwise unitarily similar to \(\operatorname{diag}(1,0)\), but its Toeplitz numerical range is exactly \((0,1)\), not \([0,1]\).

## Assumptions and scope

The Hardy space is the vector-valued \(H^2(\mathbb D,\mathbb C^m)\) with its standard normalized circle boundary norm. Rationality means that every entry extends meromorphically to the Riemann sphere and has no pole on \(\mathbb T\); poles elsewhere are allowed. The unitary matrices \(U_\zeta\) are not assumed rational, measurable, or continuous. Only pointwise conjugacy is used. Numerical ranges use \(W(T)=\{\langle Tf,f\rangle:\|f\|=1\}\). The bidisk application uses the finite-dimensional fiber model for Agler-compressed shifts from Bickel, Quertermous and Trachana (2026), and the model-space representation of Bickel and Gorkin (2018). No claim is made about the nonfactorable direction of their Conjecture 7.1.

## Proof

**Step 1 (one inclusion).** The finite-matrix numerical range \(K=W(A)\) is compact and convex. Pointwise unitary equivalence yields \(\langle M(\zeta)v,v\rangle\in\|v\|^2K\) for all \(v\). If \(f\) is a normalized Hardy vector, integration on \(\mathbb T\) of these weighted values gives \(\langle T_Mf,f\rangle\in K\) because \(K\) is convex and closed. Thus \(W(T_M)\subseteq K\).

**Step 2 (rational polynomial witnesses for exposed-face endpoints).** Fix an extreme point \(\lambda\) of \(K\) and a supporting direction \(\theta\) at it. Define, on the circle,

\[H(\zeta)=\operatorname{Re}(e^{-i\theta}M(\zeta)),\qquad J(\zeta)=\operatorname{Im}(e^{-i\theta}M(\zeta)).\]

The adjoint of a rational circle matrix is again rational in the complex variable, using the reflected-adjoint extension \(M^\#(z)=M(1/\bar z)^*\). Thus \(H\) and \(J\) extend as rational matrix functions. Because all fibers are unitarily similar to \(A\), the eigenvalues of \(H(\zeta)\) are fixed. Put \(h=\lambda_{\max}(\operatorname{Re}(e^{-i\theta}A))\). The orthogonal projection \(E(\zeta)\) onto the \(h\)-eigenspace is a *rational* matrix polynomial in \(H(\zeta)\):

\[E(\zeta)=\prod_{\mu\in\sigma(H),\,\mu\ne h}\frac{H(\zeta)-\mu I}{h-\mu},\]

where the product is over the distinct smaller eigenvalues of the constant Hermitian matrix \(\operatorname{Re}(e^{-i\theta}A)\); the empty product is \(I\). Let \(b\) be the largest eigenvalue of the Hermitian compression \(E(\zeta)J(\zeta)E(\zeta)\) **restricted to** \(\operatorname{ran}E(\zeta)\). The number \(b\) is independent of \(\zeta\), by pointwise unitary similarity. Since \(\lambda\) is an extreme point of \(K\) on the supporting line, it is one of the two endpoints of this line segment. For the upper endpoint, form

\[R(\zeta)=(hI-H(\zeta))+(bE(\zeta)-E(\zeta)J(\zeta)E(\zeta)).\]

Both summands are positive semidefinite on the circle: the second is zero on \(\ker E\) and positive on its range. Its common kernel consists exactly of vectors whose associated numerical value is the upper endpoint \(e^{i\theta}(h+ib)\). Therefore \(R(\zeta)\) is singular for every \(\zeta\). For the lower endpoint, replace the second term by \(EJE-aE\), where \(a\) is the smallest eigenvalue of the same compression. This again yields a positive semidefinite rational singular matrix with kernel vectors giving \(e^{i\theta}(h+ia)\). The argument includes faces consisting of a single point.

Since a rational square matrix is singular for every circle point, its determinant vanishes identically as a rational function. Gaussian elimination over the field \(\mathbb C(z)\) produces a nonzero rational column \(v(z)\) in its kernel. Multiplying by a common polynomial denominator gives a nonzero *analytic polynomial vector* \(p(z)\) with \(R(\zeta)p(\zeta)=0\) almost everywhere. Consequently its normalized Hardy vector \(p/\|p\|_{H^2}\) has expectation exactly \(\lambda\). Every extreme point of \(K\) is therefore in \(W(T_M)\).

**Step 3 (all values, and the compressed-shift consequence).** By Toeplitz–Hausdorff, \(W(T_M)\) is convex; by finite-dimensional Minkowski's theorem, \(K\) is the convex hull of its extreme points. Hence \(K\subseteq W(T_M)\), proving equality. If \(\Theta=B_1B_2\), the 2026 paper's Proposition 7.2 supplies an Agler decomposition whose symbol is the constant compressed-Blaschke matrix \(M_{B_1}\), while Corollary 5.3 gives pointwise unitary equivalence of the rational Toeplitz symbols for **all** decompositions. Apply the theorem to each, and interchange coordinates for the other shift.

**Step 4 (real-analytic boundary counterexample).** On \(\mathbb T\), the function \(u(\zeta)=\exp(\zeta-\zeta^{-1})\) is unimodular. Thus \(P(\zeta)\) is an orthogonal projection of rank one, real analytic in its angular parameter, with \(W(P(\zeta))=[0,1]\). The compressed Toeplitz operator \(T_P\) is a positive contraction, so its numerical range lies in \([0,1]\). If a nonzero Hardy vector \(f=(f_1,f_2)\) had expectation \(1\), positivity would force \(P(\zeta)f(\zeta)=f(\zeta)\) a.e., i.e. \(f_2=uf_1\) on the circle. If expectation were \(0\), it would force \(Pf=0\) and \(f_2=-uf_1\). Either identity is impossible for nonzero analytic Hardy functions: multiplying by \(e^{-z}\) gives the punctured-disk identity \(e^{-z}f_2(z)=\pm e^{-1/z}f_1(z)\), by uniqueness of Laurent/Fourier boundary coefficients. A nonzero analytic \(f_1\) has a zero of finite order at zero and cannot remove the essential singularity of \(e^{-1/z}\); thus \(f_1=f_2=0\), contradiction. Therefore neither endpoint is attained. Normalized vector-valued reproducing kernels localized at any boundary point in the range or kernel of \(P(\zeta)\) have expectations tending respectively to \(1\) or \(0\), by continuity of \(P\). Convexity then yields \(W(T_P)=(0,1)\).

## Verification

A standalone standard-library checker evaluates exact rational conjugacy and a polynomial extremal witness in a two-by-two model, verifies the idempotence and Hermiticity of the real-analytic projection at numerous boundary points, and compares localized boundary expectations against the stated limiting values. These are finite diagnostics, **not** proofs of the rational-kernel lemma, its all-dimensional quantifiers, or the nonattainment argument; the analytic proof above supplies those claims. Run \(`python3 verify.py`\) using Python 3 without third-party dependencies.

## Relationship to prior work

Bickel–Gorkin (2018), Theorem 3.2 and Corollary 3.4, represent the compressed shifts as Toeplitz operators and identify the **closure** of their numerical range. Bickel–Quertermous–Trachana (2026), Theorem 5.1 and Corollary 5.3, prove pointwise unitary equivalence of symbols for alternative decompositions; Proposition 7.2 produces **one** decomposition with a constant symbol when the inner function factors. Their Conjecture 7.1 asks whether *all* the resulting compressed-shift numerical ranges are closed in this factorable case. The theorem here establishes that affirmative direction; it adds the unconditional rational-symbol endpoint-witness mechanism, which cannot be obtained merely from equality of the closed numerical-range hulls. The 2012 matrix-Toeplitz paper of Bebiano–Spitkovsky provides a broader background description of closed numerical-range hulls, but its full text was not accessible for detailed implication comparison.

## Limitations

Rationality is essential to the proof and cannot be replaced by real-analytic boundary regularity, as the explicit projection shows. The theorem requires a **fixed** matrix unitary similarity class for all circle fibers. It does not address nonfactorable bidisk rational inner functions, whose numerical ranges may be open, or general matrix symbols with changing fiber numerical ranges. Earlier results about full numerical-range attainability under different formulations may remain unidentified. Independent mathematical validation and publication-priority assessment have not been performed.

## References

1. K. Bickel, K. Quertermous and M. Trachana, *Two-Variable Compressions of Shifts, Toeplitz Operators, and Numerical Ranges*, arXiv:2603.08559, first public March 9, 2026. Theorem 5.1, Corollary 5.3, Proposition 7.2 and Conjecture 7.1. https://arxiv.org/abs/2603.08559
2. K. Bickel and P. Gorkin, *Compressions of the shift on the bidisk and their numerical ranges*, Journal of Operator Theory 79 (2018), 225–265, doi:10.7900/jot.2017feb14.2143. Theorem 3.2 and Corollary 3.4. https://www.theta.ro/jot/archive/2018-079-001/2018-079-001-010.pdf
3. N. Bebiano and I. Spitkovsky, *Numerical ranges of Toeplitz operators with matrix symbols*, Linear Algebra and its Applications 436 (2012), doi:10.1016/j.laa.2011.06.019. Full text unavailable during this comparison.
