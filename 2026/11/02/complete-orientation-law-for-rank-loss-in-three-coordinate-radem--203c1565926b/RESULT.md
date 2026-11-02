# Complete orientation law for rank loss in three-coordinate Rademacher rangefinding

## Finding
Let \(L\ge2\) be any integer. For every real \(2\times3\) full-row-rank matrix \(A\), draw \(L\) independent vectors with independent fair signs in each of the three coordinates and concatenate them as \(\Omega\). The probability that the projected sample \(Y=A\Omega\) loses its target rank depends only on the projective direction of \(\ker A\), and takes exactly four possible formulas.

Write \(h=(a,b,c)\in\ker A\setminus\{0\}\). Then
\[
\Pr(\operatorname{rank}Y<2)=
\begin{cases}
4^{1-L},& |a|,|b|,|c|\text{ pairwise distinct},\\
2^{-L}+2\,4^{-L},&\text{exactly two }|a|,|b|,|c|\text{ equal and nonzero},\\
2^{1-L},&\text{exactly two coordinates of }h\text{ zero},\\
3\,2^{-L}-2\,4^{-L},&|a|=|b|=|c|>0.
\end{cases}
\]
The cases are mutually exclusive and exhaust all nonzero \(h\). Moreover, \(\Pr(Y=0)=4^{-L}\) only in the last case, and equals zero in the other three.

If additionally \(AA^{\mathsf T}=I_2\), and \(Q\) is an orthonormal basis for the range of \(Y\), the standard rangefinder output \(\widehat A=QQ^{\mathsf T}A\) has exact mean-square loss
\[
\mathbb E\|A-\widehat A\|_F^2=\Pr(\operatorname{rank}Y<2)+\Pr(Y=0).
\]
In the same order as above these means are \(4^{1-L}\), \(2^{-L}+2\,4^{-L}\), \(2^{1-L}\), and \(3\,2^{-L}-4^{-L}\). The worst-to-best *rank-failure* ratio is \((3\,2^L-2)/4\), exponentially unbounded as \(L\) increases, despite identical singular values \((1,1)\) and isotropic sketch covariance \(I_3\).

## Assumptions and scope
The entries of \(\Omega\in\{-1,1\}^{3\times L}\) are mutually independent, each value occurring with probability \(1/2\). The real matrix \(A\in\mathbb R^{2\times3}\) has rank exactly two and its kernel is a line. No regularity, alignment, or normalization hypothesis on \(A\) is required for the rank probabilities. Row orthonormality is required **only** for the displayed numerical error means. Probabilities concern exact arithmetic and the untruncated orthogonal range projection; this is the entire two-dimensional target, not a subsequent rank-one truncation.

Every nonzero \(h\) is realized as the kernel of a coisometry: take as the two rows of \(A\) any orthonormal basis of \(h^\perp\). Hence these are genuine equal-spectrum examples, not comparisons of matrices with unequal conditioning. Representative kernel normals are \((1,2,3)\), \((1,1,2)\), \((1,0,0)\), and \((1,1,1)\).

## Proof
**Step 1: quotient the cube by sign.** The eight possible sampled columns are four equiprobable antipodal classes, represented by
\[
v_1=(1,1,1),\quad v_2=(1,1,-1),\quad v_3=(1,-1,1),\quad v_4=(-1,1,1).
\]
Each projective sign class has probability \(1/4\), and \(A(-v_i)=-Av_i\). An output class is zero exactly when \(v_i\) lies in the one-dimensional kernel of \(A\), so at most one antipodal class can have zero image. This occurs exactly for \(|a|=|b|=|c|>0\).

**Step 2: classify projected line collisions.** For nonzero images \(Av_i,Av_j\), collinearity is equivalent to linear dependence of \(v_i,v_j,h\), because \(\ker A=\operatorname{span}(h)\). Equivalently, \(h\cdot(v_i\times v_j)=0\). The six cross products are, up to nonzero scalar factors and signs, precisely \((0,1,1)\), \((0,1,-1)\), \((1,0,1)\), \((1,0,-1)\), \((1,1,0)\), and \((1,-1,0)\). Thus the only collision walls are \(a=\pm b\), \(a=\pm c\), and \(b=\pm c\).

When the three absolute coordinates are distinct there are four different nonzero projective image lines, each of mass \(1/4\). With exactly one equality of two *nonzero* absolute coordinates there is exactly one two-class merger, giving line masses \((1/2,1/4,1/4)\). When exactly two coordinates vanish, there are two two-class mergers, giving masses \((1/2,1/2)\). When all absolute coordinates are equal and nonzero, one antipodal class maps to zero (mass \(q_0=1/4\)) while the other three map to distinct lines, each of mass \(1/4\). These four situations exhaust all possible intersections of collision walls: equality of two absolute coordinates at zero belongs to the axis case, and equalities among all three at positive magnitude belong to the body-diagonal case.

**Step 3: count low-rank sketches.** If the probability of the zero image is \(q_0\) and the distinct nonzero output lines have masses \(q_1,\ldots,q_r\), then \(L\) independent output columns span dimension at most one iff they all lie in the zero class together with a single nonzero line class. Different such events intersect exactly in the event that all columns are zero. Hence
\[
\Pr(\operatorname{rank}Y<2)=\sum_{j=1}^r(q_0+q_j)^L-(r-1)q_0^L.
\]
Substituting the four mass patterns gives the four displayed probabilities. Likewise \(\Pr(Y=0)=q_0^L\). For \(L\ge2\), the four values strictly increase in the stated order; the ratio of largest to smallest is
\[
\frac{3\,2^{-L}-2\,4^{-L}}{4^{1-L}}=\frac{3\,2^L-2}{4}.
\]

**Step 4: translate rank loss into a Frobenius error.** For \(AA^{\mathsf T}=I_2\), orthogonality of the projector \(P=QQ^{\mathsf T}\) gives
\[
\|A-PA\|_F^2=\operatorname{tr}((I_2-P)AA^{\mathsf T})=2-\operatorname{rank}(Y).
\]
This equals \(1\) on rank-one outcomes, \(2\) on rank-zero outcomes, and \(0\) otherwise. Taking expectations yields the stated mean-square expression. Every such \(A\) has singular values exactly \((1,1)\). The Gaussian comparator holds because projecting a nondegenerate Gaussian in \(\mathbb R^3\) by a rank-two linear map gives an absolutely continuous nondegenerate Gaussian in \(\mathbb R^2\); two independent draws span almost surely.

## Verification
Run `python3 verify.py` with Python 3 and the standard library only. The verifier enumerates *every* sign matrix for each \(L\in\{2,3,4\}\) and each of the \(124\) nonzero integer normals in \(\{-2,-1,0,1,2\}^3\). It checks the exact fractions for rank deficiency, complete collapse, and expected squared loss, for a total of \(372\) distinct normal-width pairs. The tests avoid constructing floating-point coisometries: a signed triple has zero image iff it is parallel to the kernel normal, and two nonzero images are independent iff the normal has nonzero dot product with their cross product. The proof above, not this finite enumeration, covers every real normal and all integers \(L\ge2\).

## Relationship to prior work
Lynch-Davies and Webb, *Sketching Outside the Hilbert Space for the Infinite-Dimensional Randomised SVD* (arXiv:2610.31333v1, originally public 2026-10-22), give the randomized rangefinder framework and discuss Rademacher sketches in their Introduction, Example 3.9, and Remark 2.21. In particular Remark 2.21 acknowledges positive-probability rank deficiency for discrete projected sketches and provides a general sub-Gaussian bound, but does not provide these four exact orientation-conditioned laws. Saibaba and Międlar, *Randomized Low-Rank Approximations beyond Gaussian Random Matrices* (arXiv:2308.05814), develop broad non-Gaussian sketch error and probability bounds; these do not directly imply the enumerated exact projective mass patterns. Halko, Martinsson and Tropp's 2011 randomized matrix decomposition framework supplies the standard rangefinder. The proof here reduces the special finite case to elementary projective geometry and exact counting, and does not supersede those general methods.

## Limitations
The complete classification holds only for an input with three independent sign coordinates, rank-two targets, and exact arithmetic. The worst-to-best ratio compares orientations at the same width and covariance; it is **not** a lower bound for arbitrary sketch distributions or for all high-dimensional matrices. It does not estimate numerical conditioning when the sketch has full row rank, nor spectral-norm losses after a different postprocessing or truncation. Some related historical material could remain unidentified despite the comparisons made; independent verification of priority has not been performed.

## References
1. M. Lynch-Davies and M. Webb, *Sketching Outside the Hilbert Space for the Infinite-Dimensional Randomised SVD*, arXiv:2610.31333v1, first submitted 2026-10-22, https://arxiv.org/html/2610.31333v1 .
2. A. K. Saibaba and A. Międlar, *Randomized Low-Rank Approximations beyond Gaussian Random Matrices*, arXiv:2308.05814, https://arxiv.org/abs/2308.05814 .
3. N. Halko, P. G. Martinsson and J. A. Tropp, *Finding Structure with Randomness: Probabilistic Algorithms for Constructing Approximate Matrix Decompositions*, SIAM Review **53** (2011), 217–288, https://arxiv.org/abs/0909.4061 .
