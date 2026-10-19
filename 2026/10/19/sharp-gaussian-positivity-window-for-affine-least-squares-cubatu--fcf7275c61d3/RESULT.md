# Sharp Gaussian positivity window for affine least-squares cubature

## Finding

Unweighted least-squares cubature exact for affine functions of a standard Gaussian variable has an exact finite-sample random-weight representation. It undergoes a sharp **Gumbel positivity transition** at approximately \(M=2d\log M\) samples in dimension \(d\), although the existence of some positive exact weights on the same random nodes already occurs at linear sample count.

Let \(M>d\ge1\), and sample independent \(X_1,\ldots,X_M\sim N_d(0,I_d)\). Set \(A\in\mathbb R^{M\times(d+1)}\) to have rows \((1,X_i^\top)\), and let \(b=(1,0,\ldots,0)^\top\). The unique minimum-Euclidean-norm affine-exact weights are
\[
w=A(A^\top A)^{-1}b,\qquad\sum_{i=1}^M w_i=1,\quad\sum_{i=1}^M w_iX_i=0.
\]
Here and below the equalities and inverses hold almost surely. Let \(U\sim\chi^2_{M-d}\), \(V\sim\chi^2_d\), and \(Z_1,\ldots,Z_M\) be independent \(N(0,1)\) variables, with \(U,V,Z\) mutually independent. Write \(\bar Z=M^{-1}\sum_i Z_i\) and \(s_M^2=M^{-1}\sum_i(Z_i-\bar Z)^2\). Then the **whole random vector** has the exact law
\[
(Mw_i)_{i=1}^M\ \stackrel{\mathrm d}=\left(1+\sqrt{\frac VU}\frac{Z_i-\bar Z}{s_M}\right)_{i=1}^M.
\tag{1}
\]

Define \(B_M=2\log M-\log\log M-\log(4\pi)\). For every fixed \(t\in\mathbb R\) and integer sequence \(1\le d_M<M\) satisfying
\[
\frac{M-d_M}{d_M}-B_M\longrightarrow 2t,
\tag{2}
\]
we have the sharp distributional limit
\[
\Pr\{w_1>0,\ldots,w_M>0\}\longrightarrow\exp(-e^{-t}).
\tag{3}
\]
In particular, when \(2d_M\log M/M\to\gamma\in(0,\infty)\), the positivity probability tends to \(1\) for \(\gamma<1\) and to \(0\) for \(\gamma>1\). The critical window (2), not the leading ratio alone, determines the boundary law.

For comparison, if \(d_M/M\to\delta\in(0,1/2)\), these specific least-squares weights are all strictly positive with probability tending to zero, but **some** strictly positive weights on the sampled nodes matching the same affine moments exist with probability tending to one. Thus the least-squares positivity requirement has a genuine logarithmic oversampling penalty relative to unconstrained positive cubature existence.

## Assumptions and scope

The sampling law is exactly the isotropic standard Gaussian in \(\mathbb R^d\); the target linear functional is population expectation; the cubature space is exactly the affine span of the constant and coordinate functions; no importance sampling or post-processing to enforce nonnegativity is used. The least-squares solution means the minimum \(\ell_2\)-norm vector among solutions to the affine moment equations. The Gaussian design has full column rank almost surely for \(M>d\). A positive rule means **every** one of its \(M\) weights is strictly positive. Probability and asymptotics are over the sample nodes, with \(M\to\infty\) and the specified sequence of dimensions.

## Proof

**Step 1: minimum-norm projection identity.** Let \(\boldsymbol1\in\mathbb R^M\) be the all-ones vector, \(u=\boldsymbol1/\sqrt M\), and \(P=X(X^\top X)^{-1}X^\top\) the orthogonal projector onto the \(d\)-dimensional column span of the Gaussian matrix \(X\). Set \(z=(I-P)u\) and \(T=\|z\|_2^2>0\). The minimum-norm vector constrained by \(X^\top w=0\) and \(\boldsymbol1^\top w=1\) must be proportional to \((I-P)\boldsymbol1\). Its normalization gives
\[
w=\frac{z}{\sqrt M\,T}.
\tag{4}
\]
This also equals \(A(A^\top A)^{-1}b\) by uniqueness of the Euclidean minimum-norm solution of the full-row-rank linear constraints.

**Step 2: exact Gaussian geometry.** The Gaussian column space is Haar-distributed on the Grassmannian of dimension \(d\). By orthogonal invariance, the squared norm \(T\) of the projection of a fixed unit vector onto its orthogonal complement is beta-distributed:
\[
T\ \stackrel{\mathrm d}=\frac{U}{U+V},\qquad U\sim\chi^2_{M-d},\quad V\sim\chi^2_d,\quad U\perp V.
\]
Since \(\langle z,u\rangle=T\), conditional on \(T\) the residual decomposes as
\[
z=T u+\sqrt{T(1-T)}\,v,
\]
where \(v\) is uniform on the unit sphere of \(u^\perp\), independent of \(T\). Indeed, the distribution is invariant under every orthogonal transformation fixing \(u\), and those transformations act transitively on the indicated sphere. An independent standard Gaussian vector provides the standard representation
\[
v_i=\frac{Z_i-\bar Z}{\sqrt{\sum_j(Z_j-\bar Z)^2}}.
\]
Substituting this representation and \(T/(1-T)=U/V\) into (4) proves (1). In particular, setting
\[
R_M=\max_i\left(-\frac{Z_i-\bar Z}{s_M}\right)
\]
gives the exact probability identity
\[
\Pr\{w_i>0\ \forall i\}=\Pr\left\{R_M<\sqrt{U/V}\right\}.
\tag{5}
\]
The two sides of the inequality in (5) are independent. Equality has probability zero.

**Step 3: extreme-value normalization.** Let \(Y_M=\max_i(-Z_i)\). The Gaussian maximum obeys \(Y_M=O_{\Pr}(\sqrt{\log M})\), the sample mean obeys \(\bar Z=O_{\Pr}(M^{-1/2})\), and \(s_M=1+O_{\Pr}(M^{-1/2})\). Hence
\[
R_M=\frac{Y_M+\bar Z}{s_M},\qquad R_M^2-Y_M^2=o_{\Pr}(1).
\tag{6}
\]
For each fixed \(t\), the Gaussian tail asymptotic \(\overline\Phi(x)\sim e^{-x^2/2}/(x\sqrt{2\pi})\) and the precise definition of \(B_M\) give
\[
M\overline\Phi\bigl(\sqrt{B_M+2t}\bigr)\longrightarrow e^{-t}.
\]
Therefore
\[
\Pr\{Y_M^2\le B_M+2t\}=\Phi\bigl(\sqrt{B_M+2t}\bigr)^M+o(1)
\longrightarrow\exp(-e^{-t}).
\tag{7}
\]
The \(o(1)\) accounts for the negligible event \(Y_M<0\), on which squaring reverses the monotonicity. Equations (6) and (7) prove the same weak limit for \((R_M^2-B_M)/2\).

**Step 4: degrees-of-freedom concentration.** Condition (2) forces \(d_M\sim M/(2\log M)\) and \(M-d_M\sim M\). Standard chi-square variance estimates imply
\[
\frac UV-\frac{M-d_M}{d_M}=o_{\Pr}(1),
\tag{8}
\]
because its stochastic scale is at most of order \((\log M)^{3/2}/\sqrt M\). Combining (5)--(8) and continuity of the Gumbel distribution proves (3). For \(2d_M\log M/M\to\gamma\in(0,\infty)\) different from one, \(U/V\) divided by \(2\log M\) converges in probability to \(1/\gamma\), whereas \(R_M^2/(2\log M)\to1\) in probability. The asserted zero-one phase transition follows.

**Step 5: existence versus the least-squares rule.** If \(d_M/M\to\delta\in(0,1/2)\), chi-square laws give \(U/V\to(1-\delta)/\delta\) in probability, while \(R_M\to\infty\); thus (5) tends to zero. In contrast, Wendel's theorem for points in general position with an absolutely continuous centrally symmetric law gives
\[
\Pr\left\{0\notin\operatorname{conv}(X_1,\ldots,X_M)\right\}
=2^{1-M}\sum_{j=0}^{d_M-1}\binom{M-1}{j}.
\tag{9}
\]
For \(d_M/M\to\delta<1/2\), the right-hand side vanishes by a binomial large-deviation bound, so the origin is in the interior of the convex hull with probability tending to one. Interior inclusion implies a representation with **strictly positive coefficients on all sampled nodes**: first assign every node a sufficiently small common positive mass and then represent the correspondingly shifted target, still inside the hull, by a convex combination of the nodes. Normalizing produces the required positive affine-exact cubature. This proves the claimed logarithmic separation.

## Verification

The accompanying standalone `verify.py` uses only Python's standard library, no external data, and a fixed seed. Run `python verify.py` from the package directory. It compares exact-rational minimum-norm and residual-projection formulas over nonsingular finite designs, directly generated Gaussian designs against an independent chi-square-and-centered-sphere construction, and finite-sample probabilities against elementary two-dimensional and Wendel benchmarks. Larger seeded samples illustrate both sides of the asymptotic threshold. These numerical experiments verify identities and detect implementation mistakes but are **not** proofs of the infinite-dimensional-sequence asymptotics; the proof above is analytical.

## Relationship to prior work

Bělík, Narayan and Turnage [1] develop randomized least-squares quadrature, prove general finite-sample concentration and positivity statements using relative admissibility, and describe constructive Tchakaloff pruning. The least-squares construction analyzed here is their method specialized to affine functions and direct Gaussian sampling, with an exact **joint random-weight law** and sharp growing-dimensional positivity asymptotics, neither stated by their general bounds. In this case the Christoffel function is \(1+\|x\|_2^2\) and is unbounded, making worst-case bounded-Christoffel sampling results inapplicable without modifications.

Migliorati and Nobile [2] prove sample-size sufficient conditions and positive randomized cubature for appropriately weighted/induced sampling; their results are not an equivalent sharp probability law for these unweighted Gaussian affine weights. Wendel's geometric theorem [3] characterizes when *some* convex coefficients can match the affine moments, but it does not imply that the distinguished minimum-norm least-squares coefficients are nonnegative. Indeed, the final part of the proof gives a regime in which these two events separate with asymptotic probability one. The exact finite-dimensional distribution and limiting constant may have equivalent representations elsewhere in the extensive Gaussian random-projection literature; the novelty assessment is limited to the sources explicitly checked.

## Limitations

Results rely on independent continuous isotropic Gaussian samples, the exact affine moment space, and unweighted minimum-norm least-squares coefficients. They are not universal positivity bounds for arbitrary polynomial spaces, importance-weighted designs, non-Gaussian distributions or finite-precision solvers. The sharp Gumbel law concerns a specific dimensional-growth critical window; it does not assert a fully uniform finite-sample probability estimate. Stronger prior work containing this specialized calculation would supersede the originality assessment. All independent verification remains unperformed.

## References

[1] F. Bělík, A. Narayan and J. Turnage, *Constructive Tchakaloff results and well-conditioned quadrature through randomized least squares*, arXiv:2609.09506v1, first public September 8, 2026. https://arxiv.org/abs/2609.09506

[2] G. Migliorati and F. Nobile, *Stable high-order randomized cubature formulae in arbitrary dimension*, arXiv:1812.07761 (2018). https://arxiv.org/abs/1812.07761

[3] J. G. Wendel, *A Problem in Geometric Probability*, Mathematica Scandinavica 11 (1962), 109–111. https://doi.org/10.7146/math.scand.a-10655
