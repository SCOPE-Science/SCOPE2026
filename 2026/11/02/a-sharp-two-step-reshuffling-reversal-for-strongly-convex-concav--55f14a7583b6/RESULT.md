# A sharp two-step reshuffling reversal for strongly convex–concave quadratic games

## Finding

Two-component, finite-sum gradient descent–ascent can be *worse* under random reshuffling than under independent sampling with replacement, after the same two gradient evaluations, even when each individual gradient update is a strict Euclidean contraction. This reversal has an exact, dimension-free quantitative criterion.

**Theorem (one-epoch isotropic comparison).** Let \(d_x,d_y\ge1\) be integers, let \(A\in\mathbb R^{d_x\times d_x}\) and \(B\in\mathbb R^{d_y\times d_y}\) be symmetric positive definite, and let \(C\in\mathbb R^{d_x\times d_y}\) be arbitrary. For \(s\in\{+1,-1\}\), define the two strongly convex–strongly concave objectives

\[
f_s(x,y)=\tfrac12x^\top Ax-\tfrac12y^\top By+s\,x^\top Cy.
\]

Use simultaneous gradient descent in \(x\) and ascent in \(y\), with the same fixed step \(h>0\) on each component. Start independently of the component choices from any centered real random vector \(Z_0=(X_0,Y_0)\) with \(\mathbb E[Z_0Z_0^\top]=I\). After exactly two component updates, compare **RR**, which uses each of \(s=+1,-1\) exactly once in a uniformly random order, against **IID**, which draws each sign independently and uniformly at each update. Then

\[
\boxed{\mathbb E_{\mathrm{RR}}\|Z_2\|_2^2-\mathbb E_{\mathrm{IID}}\|Z_2\|_2^2
=2h^4\|AC-CB\|_F^2.}
\]

Both expectations include the common independent initial distribution. Thus the reshuffled error is **strictly larger** for every \(h>0\) if and only if \(AC\ne CB\); equality holds for every step if and only if \(AC=CB\). The statement also applies without a random initialization when the two squared errors are summed over a fixed orthonormal basis of deterministic initial conditions.

**Exact planar directional classification.** In dimension \(d_x=d_y=1\), write \(A=\mu+\delta\), \(B=\mu-\delta\), \(C=\omega\), with \(\mu>\delta>0\), \(\omega\ne0\), and \(0<h<1/(\mu+\delta)\). For any *fixed deterministic* initial state \(z=(x,y)\), the two-order/two-draw expectation gap is exactly

\[
\Delta(x,y)=4h^3\delta\omega^2\bigl[(1-h(\mu-\delta))y^2-(1-h(\mu+\delta))x^2\bigr].
\]

Hence RR is better for starts inside the cone \((1-h(\mu-\delta))y^2<(1-h(\mu+\delta))x^2\), worse outside, and tied precisely on its boundary. Averaging the two standard-basis starts gives \(8h^4\delta^2\omega^2>0\), explaining why the isotropic comparison can be strictly unfavorable while some individual starts benefit from reshuffling.

**Contractive exact witness.** Let \(A=3\), \(B=1\), \(C=1\), and \(h=1/8\). Each component step is a strict Euclidean contraction. Yet the isotropic RR-minus-IID squared-error gap is \(1/512\). For deterministic starting states \((1,0)\) and \((0,1)\), the respective exact gaps are \(-5/1024\) and \(+7/1024\).

## Assumptions and scope

There is no additive component-gradient offset or measurement noise. Both component games share the unique saddle \((0,0)\), and their average is the uncoupled strictly convex–concave quadratic \(\tfrac12x^\top Ax-\tfrac12y^\top By\). The two stochastic methods use exactly two gradient evaluations, the identical step \(h\), and the same initialization. The isotropic conclusion compares squared Euclidean saddle distance, not game value, duality gap, operator norm, fixed-initial-state distance, optimal step-size tuning, or multiple-epoch rates. No Gaussian distribution is required for the initialization; second moments suffice.

Define

\[
H=\begin{pmatrix}A&0\\0&B\end{pmatrix},\qquad
K=\begin{pmatrix}0&C\\-C^\top&0\end{pmatrix},\qquad M_s=I-h(H+sK).
\]

Because \(H^\top=H\) and \(K^\top=-K\), one has \(M_{-}=M_{+}^\top\). All matrices and vectors are real. Here \(\|\cdot\|_F\) denotes Frobenius norm and \([P,Q]=PQ-QP\) denotes a matrix commutator.

## Proof

**Step 1: Exact adjoint-product identity.** The following algebraic identity holds for **every real square matrix** \(M\). Set \(M_+=M\) and \(M_-=M^\top\). Let \(T\) denote the two-update matrix. Under RR the two possible products are \(MM^\top\) and \(M^\top M\), while under IID the four equiprobable products are \(M^2\), \((M^\top)^2\), \(MM^\top\), and \(M^\top M\). Since \(\mathbb E\|TZ_0\|_2^2=\operatorname{tr}(TT^\top)=\|T\|_F^2\) when \(\mathbb E[Z_0Z_0^\top]=I\), and since transposition preserves Frobenius norm, their difference is

\[
\mathbb E_{\rm RR}\|TZ_0\|_2^2-\mathbb E_{\rm IID}\|TZ_0\|_2^2
=\tfrac12\bigl(\|MM^\top\|_F^2-\|M^2\|_F^2\bigr).
\]

Put \(P=MM^\top\) and \(Q=M^\top M\). Both are symmetric and \(\|P\|_F^2=\|Q\|_F^2\). Cyclicity of trace gives \(\operatorname{tr}(PQ)=\|M^2\|_F^2\). Thus

\[
\|P-Q\|_F^2=\|P\|_F^2+\|Q\|_F^2-2\operatorname{tr}(PQ)
=2\bigl(\|MM^\top\|_F^2-\|M^2\|_F^2\bigr).
\]

Consequently the exact general comparison is

\[
\boxed{\mathbb E_{\rm RR}\|Z_2\|_2^2-\mathbb E_{\rm IID}\|Z_2\|_2^2
=\tfrac14\|MM^\top-M^\top M\|_F^2.}
\]

The expression is nonnegative, with equality if and only if \(M\) is normal. This identity, used here as a lemma, is directly established by the preceding trace calculation; it is not an appeal to a positive-semidefinite matrix-product inequality.

**Step 2: The game-geometry reduction.** Substitute \(M=I-h(H+K)\) and \(M^\top=I-h(H-K)\). Direct multiplication yields

\[
MM^\top-M^\top M=-2h^2[H,K],\qquad
[H,K]=\begin{pmatrix}0&AC-CB\\(AC-CB)^\top&0\end{pmatrix}.
\]

Therefore \(\|[H,K]\|_F^2=2\|AC-CB\|_F^2\), and Step 1 gives the asserted exact \(2h^4\|AC-CB\|_F^2\). Equality and strictness follow immediately for every \(h>0\). For an orthonormal basis \(\{e_j\}\), the identity \(\sum_j\|Te_j\|_2^2=\|T\|_F^2\) proves the deterministic-basis formulation.

**Step 3: Contractivity is compatible with strict reversal.** Let \(m=\min\{\lambda_{\min}(A),\lambda_{\min}(B)\}>0\) and \(L=\|H+K\|_2=\|H-K\|_2\). For either sign and every vector \(z\), skew-symmetry of \(K\) gives

\[
\|M_s z\|_2^2=\|z\|_2^2-2h\,z^\top H z+h^2\|(H+sK)z\|_2^2
\le(1-2hm+h^2L^2)\|z\|_2^2.
\]

Any \(0<h<2m/L^2\) therefore makes **both** component maps strict Euclidean contractions, while the gap remains positive whenever \(AC\ne CB\). This separates the comparison reversal from a trivial example of individually unstable updates.

**Step 4: Complete planar signs and exact witness.** For scalar \(A=\mu+\delta\), \(B=\mu-\delta\), \(C=\omega\), the two component matrices are

\[
M_+=\begin{pmatrix}a&-h\omega\\h\omega&b\end{pmatrix},\qquad
M_-=M_+^\top,\qquad
a=1-h(\mu+\delta),\ b=1-h(\mu-\delta).
\]

Expanding the four squared lengths for a deterministic \((x,y)\) gives exactly \(4h^3\delta\omega^2(by^2-ax^2)\). Since \(a,b>0\) in the stated range, its sign gives the claimed cone and its exact boundary. Summing the coefficients of \(x^2\) and \(y^2\) produces \(4h^3\delta\omega^2(b-a)=8h^4\delta^2\omega^2\), as required by the general theorem.

For the witness, the component update matrices and the positive-definiteness certificate are

\[
M_+=\frac18\begin{pmatrix}5&-1\\1&7\end{pmatrix},\qquad
I-M_+^\top M_+=\frac1{32}\begin{pmatrix}19&-1\\-1&7\end{pmatrix}.
\]

The leading principal minor is \(19/32>0\), and the determinant is \(33/256>0\), so both \(M_+\) and its transpose are strictly contractive. Substituting \((x,y)=(1,0),(0,1)\) into the planar formula yields \(-5/1024\) and \(+7/1024\), respectively; their sum is \(1/512\). This concludes every assertion.

## Verification

The independent script `verify.py`, requiring only the Python standard library, checks the all-matrix adjoint identity using exact rational arithmetic on \(400\) deterministic test matrices of sizes one through five. It checks the block-curvature formula on \(405\) strongly convex–concave examples with varying rectangular coupling matrices, the planar cone formula on \(200\) rational configurations, and six exact witness/contractivity assertions. It prints `PASS: 1011 exact-rational matrix and vector assertions`. The analytic trace identity and block algebra prove the quantified result; the finite computations are consistency checks, not an exhaustive proof over matrices or step sizes. Run with `python3 verify.py` from the extracted package directory.

## Relationship to prior work

The motivating finite-sum minimax study of Das, Schölkopf and Muehlebach [1] develops convergence-rate bounds for RR and related methods on strongly convex–concave games, including simultaneous GDA. It analyzes epoch-level updates in Section 3 and Appendix C and numerical comparisons over many epochs in Section 5. Its claims do **not** imply exact uniformly beneficial per-initial-state or per-epoch behavior at a fixed shared step. The present statement is a sharp, deliberately finite-horizon *isotropic* reversal and gives a pointwise cone separating benefits and harms. It does not contradict long-horizon, differently tuned, or upper-bound comparisons.

Recht and Ré [2] and Israel, Krahmer and Ward [3] investigate with- versus without-replacement matrix products for **positive-semidefinite** factors and establish special noncommutative arithmetic–geometric inequalities. Here the simultaneous game-update factors have nonzero skew parts and are generally neither symmetric nor positive-semidefinite, even for small steps; the stated inequalities do not supply this reverse comparison. Our exact identity instead exploits the adjoint-pair structure. Koloskova and colleagues [4] analyze shuffled SGD in scalar-objective optimization rather than coupled minimax simultaneous GDA. The distinction is mathematical, not merely terminological.

## Limitations

Only one two-update epoch, two equally probable components sharing a saddle, symmetric positive-definite within-block curvature, exactly opposite bilinear couplings, Euclidean squared distance and an isotropic initial second moment are classified. There is no claim about arbitrary component pairs, arbitrary fixed initial vectors in higher dimensions, adaptive or optimally tuned step sizes, later epochs, asymptotic convergence rates, alternate losses, or nonsymmetric stochastic-game distributions. The universal identity itself is an elementary trace lemma; publication priority for its exact application to reshuffling games remains subject to specialized literature not conclusively ruled out. No independent audit has been performed.

## References

1. A. Das, B. Schölkopf, and M. Muehlebach, *Sampling without Replacement Leads to Faster Rates in Finite-Sum Minimax Optimization*, NeurIPS 2022, arXiv:2206.02953 (first public June 7, 2022). https://arxiv.org/html/2206.02953v2
2. B. Recht and C. Ré, *Toward a Noncommutative Arithmetic-geometric Mean Inequality: Conjectures, Case-studies, and Consequences*, COLT/PMLR 23 (2012), 11.1–11.24. https://proceedings.mlr.press/v23/recht12/recht12.pdf
3. A. Israel, F. Krahmer, and R. Ward, *An arithmetic-geometric mean inequality for products of three matrices*, arXiv:1411.0333 (2014). https://arxiv.org/abs/1411.0333
4. A. Koloskova, N. Doikov, S. U. Stich, and M. Jaggi, *On Convergence of Incremental Gradient for Non-Convex Smooth Functions* (earlier version titled *Shuffle SGD is Always Better than SGD: Improved Analysis of SGD with Arbitrary Data Orders*), arXiv:2305.19259. https://arxiv.org/html/2305.19259v4
