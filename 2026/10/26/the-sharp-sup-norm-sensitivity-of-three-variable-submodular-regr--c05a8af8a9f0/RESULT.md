# The sharp sup-norm sensitivity of three-variable submodular regression

## Finding
Let \(E=\{1,2,3\}\) and identify a real set-function \(f:2^E\to\mathbb R\) with its eight values, indexed by the subsets of \(E\). Write \(\mathcal C\subset\mathbb R^8\) for the closed convex cone of submodular functions, without monotonicity or normalization restrictions. Let \(\Pi_{\mathcal C}\) be the Euclidean nearest-point projection (unweighted least-squares submodular regression). Its exact global coordinatewise stability constant is
\[
\boxed{\sup_{u\ne v}\frac{\|\Pi_{\mathcal C}u-\Pi_{\mathcal C}v\|_\infty}{\|u-v\|_\infty}=\frac74.}
\]
The constant is attained on arbitrarily short perturbations near a concrete three-constraint active face. For comparison, the analogous constants for ground sets with one and two elements are \(1\) and \(3/2\), respectively. The complete face calculation has twenty-two feasible equality patterns, exactly five of which have local norm \(7/4\).

## Assumptions and scope
Every data vector and fitted vector lies in \(\mathbb R^{2^E}\); the fitting objective is the unweighted sum of squared coordinate residuals. The input/output perturbation norm is \(\ell^\infty\), not the Euclidean norm of the fitting objective. Submodularity means
\[
 f(S\cup\{i\})+f(S\cup\{j\})-f(S)-f(S\cup\{i,j\})\ge0
\]
for every distinct \(i,j\in E\) and \(S\subseteq E\setminus\{i,j\}\). There are six inequalities. Coordinates are ordered by binary subset encoding \(0,1,\ldots,7\) and inequalities by the ordered list \(((1,2),\varnothing),((1,2),\{3\}),((1,3),\varnothing),((1,3),\{2\}),((2,3),\varnothing),((2,3),\{1\})\). Let their six normal row vectors be \(a_0,\ldots,a_5\), and let \(A\) be the resulting \(6\times8\) integer matrix. Then \(\mathcal C=\{f:Af\ge0\}\).

## Proof
**1. Classify exactly the possible active faces.** Directly from the six elementary mixed-difference rows,
\[
 a_0-a_1=a_2-a_3=a_4-a_5,
 \qquad \operatorname{rank}A=4.
\]
Thus \(\operatorname{im}A\) is exactly the four-dimensional subspace of \(r\in\mathbb R^6\) with \(r_0-r_1=r_2-r_3=r_4-r_5\). An equality pattern \(I\subseteq\{0,\ldots,5\}\) is feasible precisely when some such \(r\) vanishes on \(I\) and is strictly positive off \(I\). The common difference immediately yields the following exhaustive classification:

* The empty pattern is feasible.
* If no pair \(\{0,1\},\{2,3\},\{4,5\}\) is wholly contained in \(I\), the nonempty pattern is a subset either of \(\{0,2,4\}\) or of \(\{1,3,5\}\).
* If any pair is wholly contained in \(I\), the common difference is zero and \(I\) must be a union of whole pairs.

Conversely every listed pattern is feasible: choose common difference \(-1\), \(+1\), or \(0\), respectively, with zeros on the specified entries and strictly positive values elsewhere. Since \(\operatorname{im}A\) is the stated subspace, these slack vectors come from actual set-functions. There are exactly \(1+2(2^3-1)+(2^3-1)=22\) patterns (the empty one counted only once). No unlisted combination can describe an active face.

**2. Calculate every local linear operator.** On an open projection region whose fitted point has exactly the constraints in \(I\) active and whose normal vector is in the relative interior of its normal cone, the metric projection has derivative
\[
 Q_I=I_8-A_I^{\mathsf T}(A_IA_I^{\mathsf T})^{\dagger}A_I.
\]
Here \(\dagger\) denotes the Euclidean Moore--Penrose inverse; equivalently, delete dependent rows of \(A_I\), form the invertible Gram matrix of the remaining rows, and use its ordinary inverse. Each \(Q_I\) is the orthogonal projector onto \(\ker A_I\). Symmetry between the ground-set labels and complementing the subsets reduces the twenty-two possible patterns to the following exact row-sum table:

| Active constraints | Number of patterns | \(\max_x\sum_y |(Q_I)_{xy}|\) |
| :--- | ---: | ---: |
| none | 1 | \(1\) |
| one of the six inequalities | 6 | \(3/2\) |
| two of \(\{0,2,4\}\), or two of \(\{1,3,5\}\) | 6 | \(5/3\) |
| all three of one such triple | 2 | \(7/4\) |
| one whole pair | 3 | \(3/2\) |
| two whole pairs | 3 | \(7/4\) |
| all three whole pairs | 1 | \(3/2\) |

These numbers follow by rational Gram-matrix inversion and eight absolute row sums for each row-projector. The accompanying `check.py` constructs the six rows, verifies the rank and relations, explicitly enumerates all twenty-two feasible masks, performs the Gram inversions in exact rational arithmetic, and checks the full table, including idempotence and symmetry of every computed projector. This is an exhaustive finite calculation for the complete three-element problem, not sampling.

**3. Pass from local to global stability.** The Euclidean projector onto a polyhedral cone is continuous and piecewise affine (here positively homogeneous), with linear pieces given by the \(Q_I\) for feasible active faces. Along any straight segment \([u,v]\), subdivide at the finitely many boundaries of its linear regions (or take a limiting generic segment if necessary). Summing the resulting inequalities gives
\[
 \|\Pi_{\mathcal C}(u)-\Pi_{\mathcal C}(v)\|_\infty
 \le\max_I\|Q_I\|_{\infty\to\infty}\,\|u-v\|_\infty
 =\frac74\|u-v\|_\infty.
\]

**4. Exhibit a sharp perturbation.** Let \(f\) be zero on every proper subset and \(f(E)=-1\). Its six mixed-difference slacks are \((0,1,0,1,0,1)\), so the active face is \(I=\{0,2,4\}\). Put \(z=f-a_0-a_2-a_4\). As \(z-f\) lies in the interior of the outward normal cone to this face, the projection equals \(f\) at \(z\), and in a sufficiently small neighborhood the projection is affine with derivative \(Q_I\). Its row corresponding to the empty subset is
\[
 \bigl((Q_I)_{\varnothing,S}\bigr)_{S=0}^7
 =\left(\frac58,\frac14,\frac14,-\frac18,\frac14,-\frac18,-\frac18,0\right).
\]
Its absolute row sum is \(7/4\). Taking a small data perturbation with coordinate signs matching this row realizes the ratio \(7/4\). This proves sharpness, not merely an upper bound.

**5. Baseline dimensions.** With one ground-set element there are no restrictions and the projection is the identity. With two elements there is a single four-entry mixed-difference normal \(a\), whose squared Euclidean norm is \(4\); its nontrivial derivative \(I_4-aa^{\mathsf T}/4\) has maximum absolute row sum \(3/2\). The same active-face argument proves that bound sharp.

## Verification
Run `python3 check.py`. The program uses Python's standard-library `fractions.Fraction`, verifies all twenty-two feasible faces within the sixty-four candidate subsets, checks the seven class entries of the table, confirms exactly five maximizers, independently computes the explicit sharp witness row, and checks the two-element baseline. Every matrix inverse and row sum is rational; no floating-point tolerances or approximate certificates are used. The script does not replace the analytical proof that the twenty-two patterns exhaust all possible active sets or the piecewise-affine projector principle; those facts are justified above.

## Relationship to prior work
Iyer and Bilmes (2015, arXiv:1506.07329) develop polyhedral properties of submodular functions and their superdifferentials. Bach (2015, arXiv:1511.00394) treats submodularity and convex extensions and contains projection operations in a distinct optimization construction. Neither inspected source establishes this exact \(\ell^\infty\) stability modulus for Euclidean projection onto all eight set-function coordinates. General isotonic regression and projection methods, including Németh and Németh (2015, arXiv:1503.08458), concern different order-constraint cones and do not imply the present eight-coordinate calculation. These comparisons do not establish absolute historical priority.

## Limitations
The sharp constant applies only to the complete three-element ground set, unweighted Euclidean least-squares fitting, unrestricted real submodular functions, and coordinatewise input/output errors. It does not settle arbitrary ground-set size, weighted fitting, non-Euclidean metric projection, or monotone or normalized subclasses. Originality is provisional pending independent bibliographic examination.

## References
1. R. Iyer and J. Bilmes, *Polyhedral aspects of Submodularity, Convexity and Concavity*, arXiv:1506.07329, initially public 24 June 2015. https://arxiv.org/abs/1506.07329
2. F. Bach, *Submodular Functions: from Discrete to Continous Domains*, arXiv:1511.00394, initially public 2 November 2015. https://arxiv.org/abs/1511.00394
3. A. B. Németh and S. Z. Németh, *Isotonic regression and isotonic projection*, arXiv:1503.08458, 2015. https://arxiv.org/abs/1503.08458
