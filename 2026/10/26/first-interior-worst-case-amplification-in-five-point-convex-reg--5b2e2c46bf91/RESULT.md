# First interior worst-case amplification in five-point convex regression

## Finding
For an integer \(n\ge2\), consider the discrete convexity cone
\[
C_n=\{x\in\mathbb R^n:x_i-2x_{i+1}+x_{i+2}\ge0\text{ for }1\le i\le n-2\},
\]
and let \(\Pi_n:\mathbb R^n\to C_n\) be the Euclidean nearest-point map. Its sharp sensitivity to coordinatewise bounded changes in observations is
\[
L_n=\sup_{a\ne b}\frac{\|\Pi_n(a)-\Pi_n(b)\|_\infty}{\|a-b\|_\infty}.
\]

**Theorem (first interior extremizer and a persistent lower bound).** The exact small-dimensional constants are
\[
L_2=1,\qquad L_3=\frac43,\qquad L_4=\frac75,\qquad \boxed{L_5=\frac{11}{7}}.
\]
In dimension five, the sole possible maximizer among strictly complementary active-set Jacobians is the face where the **first and third** second differences vanish but the middle second difference is strictly positive. Its unique maximizing output index is the central, third coordinate. In dimensions two through four, every maximizing output is an endpoint; in dimension four the maximizing face is the entirely affine face. Thus five is the *first* observation count where the sharp amplification is controlled by an interior output under a noncontiguous active pattern, rather than by an affine fit. For every integer \(n\ge5\),
\[
\boxed{L_n\ge\frac{11}{7}}.
\]
These are statements about global input-to-output \(\ell^\infty\) sensitivity, not stochastic mean-squared risk.

## Assumptions and scope
All observations and fits are real. The design consists of \(n\) equally spaced positions with unit observation weights. The projection \(\Pi_n(a)\) minimizes \(\frac12\sum_{i=1}^n(x_i-a_i)^2\) subject to the displayed second-difference inequalities. The set \(C_n\) is a nonempty closed convex cone, so the minimizer exists uniquely. The sensitivity is measured by the coordinatewise maximum norm on both the input and output, whereas minimization uses the Euclidean norm. There is no bound on the input data or constraint on its sign.

## Proof
**1. Attainable active-set projectors.** Let \(D_n\) be the \((n-2)\times n\) second-difference matrix, with row \(i\) containing \((1,-2,1)\) in columns \(i,i+1,i+2\). Its rows are linearly independent: prescribing arbitrary second differences and any first two coordinates recursively determines a sequence. Consequently every subset \(A\subseteq\{1,\ldots,n-2\}\) of rows is independent. Denote the selected row matrix by \(D_A\), and set
\[
P_A=I_n-D_A^{\mathsf T}(D_AD_A^{\mathsf T})^{-1}D_A,
\]
with \(P_\varnothing=I_n\). This is the Euclidean orthogonal projector onto the subspace where the selected second differences vanish.

Every subset \(A\) occurs on an open cell of the cone projection. To see this, choose \(x\) with second differences equal to zero for \(i\in A\) and one otherwise; such \(x\) exists by the independence just established. Choose multipliers \(\lambda_i=1\) for \(i\in A\), and set \(a=x-D_A^{\mathsf T}\lambda\). Then \(x\) obeys the Karush–Kuhn–Tucker conditions for projection of \(a\): feasibility, positive active multipliers, zero active differences, and the stationarity identity \(x=a+D_A^{\mathsf T}\lambda\). All inactive inequalities are strictly slack and all chosen multipliers strictly positive. Hence, in a neighborhood of \(a\), the same active pattern persists, and the projection equals the linear map \(P_A\). The empty set is obtained from any strictly convex sequence.

Conversely, the projection onto a polyhedral cone is a continuous piecewise-linear function: on every strict-complementarity cell it equals one of these finitely many projectors, and boundary points are obtained by continuity. A segment between two inputs can be partitioned at finitely many linear-cell boundaries; integrating the matrix norm bound along each piece gives a global bound. Local attainability of every \(P_A\) proves equality:
\[
\boxed{L_n=\max_{A\subseteq\{1,\ldots,n-2\}}\max_{1\le j\le n}\sum_{k=1}^n|(P_A)_{jk}|.}\tag{1}
\]
This finite active-face formula serves only as a proof tool; the new sharp conclusion is the five-point extremal classification below.

**2. Exact small-dimensional classification.** For \(n=2\), the cone is all of \(\mathbb R^2\), so \(L_2=1\). For \(n=3\), the empty face gives one and the unique nonempty face has norm \(4/3\), attained in rows one and three. For \(n=4\), the two singleton faces each have norm \(4/3\), whereas the full two-row active face has norm \(7/5\), attained in the first and fourth rows.

In dimension five there are exactly eight subsets of the three constraints. Label each subset by its binary membership pattern in order, with \(1\) meaning an equality constraint. Direct inversion of matrices of order at most three in (1) yields the following *complete* list of maximum absolute row sums:

| Active pattern | \(\max_j\sum_k|(P_A)_{jk}|\) |
| --- | ---: |
| 000 | \(1\) |
| 100, 010, 001 | \(4/3\) |
| 110, 011, 111 | \(7/5\) |
| **101** | **\(11/7\)** |

For the exceptional pattern \(A=\{1,3\}\), direct calculation gives
\[
P_{\{1,3\}}=\frac1{35}\begin{pmatrix}
29&12&-5&-2&1\\
12&11&10&4&-2\\
-5&10&25&10&-5\\
-2&4&10&11&12\\
1&-2&-5&12&29
\end{pmatrix}.
\]
Its five row sums are \(7/5,39/35,11/7,39/35,7/5\), respectively, so the third row is the unique maximizing row. The table proves that this pattern is the unique maximizing pattern among all active-set projectors and that \(L_5=11/7\). It also proves the stated smallest-dimension transition.

**3. Explicit finite-distance equality witness.** Define
\[
a=(-1,2,-2,3,1),\qquad v=(-1,1,1,1,-1),\qquad \varepsilon=\frac14.
\]
At \(a\), the exact convex fit is \(x=(0,0,0,1,2)\). Its second differences are \((0,1,0)\), and its positive KKT multipliers on active constraints one and three both equal one. For \(a+\varepsilon v\), the fit remains on the same active face, with multipliers \(1+2\varepsilon/7=15/14>0\) and middle second difference \(1-16\varepsilon/7=3/7>0\). Consequently
\[
\Pi_5(a+\varepsilon v)-\Pi_5(a)
=\varepsilon P_{\{1,3\}}v
=\frac1{28}(-5,3,11,3,-5).
\]
The ratio of output and input maximum norms is therefore *exactly* \(11/7\) for these two distinct data vectors. Neither a limiting derivative nor finite sampling is needed for attainability.

**4. Persistence in every larger dimension.** For \(n>5\), retain active second-difference rows one and three, and prescribe all other second differences to be strictly positive. The preceding attainability construction creates an open cell with this active set. Its Jacobian is the direct sum of the displayed five-by-five projector and an identity matrix on the remaining observations, because the two selected second differences use only the first five coordinates. Hence its maximum absolute row sum remains \(11/7\). The full nonlinear projector has at least that global Lipschitz constant by (1). This proves \(L_n\ge11/7\) for every \(n\ge5\). \(\square\)

## Verification
The self-contained standard-library program `verify_convex.py` uses exact rational arithmetic, independently forming all selected second-difference Gram matrices, inverting them by Gaussian elimination, and checking projection symmetry and idempotence. It exhaustively checks all active sets for \(2\le n\le8\), including the five-point exact matrix, unique maximizing face/output, and an explicit finite-distance witness. It also checks the embedded lower-bound projector for all \(5\le n\le8\). It reports `PASS 13069 exact-rational assertions`. The finite checks are reproducible corroboration only; the global formula, attainability, all-dimension persistence, and all-input statements are proved analytically above.

## Relationship to prior work
Guntuboyina and Sen, *Global risk bounds and adaptation in univariate convex regression* (first public May 2013), explicitly formulate univariate least squares as Euclidean projection onto the convex-sequence cone, but analyze stochastic risk and approximation, not sharp \(\ell^\infty\) input-to-output stability. Chatterjee, Guntuboyina and Sen, *On risk bounds in isotonic and other shape restricted regression problems* (first public November 2013), establish polyhedral-cone regression risk estimates, including convex sequences and derivatives related to effective dimension; their Euclidean one-Lipschitz observation does not imply nonexpansivity in the maximum norm or an exact five-point constant. An examined published result on finite-chain isotonic \(\ell_p\) regression concerns *first* differences with the same input/output \(\ell_p\) metric, rather than second-difference convexity constraints under Euclidean least squares. Another examined result computes the \(L^\infty\) norm of a *linear* local affine projector on a simplex, not the global nonlinear convex-sequence projector. No inspected result proves or implies the displayed five-point sharp norm and first-interior-extremizer classification.

## Limitations
This theorem determines the exact global constant only through \(n=5\), together with the nontrivial uniform lower bound for every larger \(n\). It makes no assertion that \(11/7\) is sharp when \(n>5\), nor that a particular face continues to maximize there. It uses equally spaced design points and identical least-squares weights. The search and source comparisons cannot certify absolute historical priority, especially under approximation-operator or isotonic/convex regression aliases. Independent review has not been performed.

## References
1. A. Guntuboyina and B. Sen, *Global risk bounds and adaptation in univariate convex regression*, arXiv:1305.1648 (first version 2013-05-07), https://arxiv.org/abs/1305.1648 . Full accessible HTML is available through the arXiv abstract's text rendering.
2. S. Chatterjee, A. Guntuboyina, B. Sen, *On risk bounds in isotonic and other shape restricted regression problems*, arXiv:1311.3765 (first version 2013-11-15), https://arxiv.org/html/1311.3765v3 .
3. *Sharp \(\ell_p\) stability of finite-chain isotonic metric projections*, published mathematical record, https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-sharp-ell-p-stability-of-finite-chain-isotonic-metric-projection--f78c125227d5 .
4. *Exact positivity defect and max norm of the affine least-squares projector on a simplex*, published mathematical record, https://github.com/Resultary/2026/tree/main/2026/10/4/SCOPE-exact-positivity-defect-and-max-norm-of-the-affine-least-squares--99c2b9dd9b34 .
