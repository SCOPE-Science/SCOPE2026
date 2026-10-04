# Numerical index one half for every finite equilateral Lipschitz-free space
## Finding
Let \(M\) be a finite equilateral metric space over the real scalars, meaning that all distances between distinct points have one common positive value. If \(|M|\ge 3\), then
\[
n(\mathcal F(M))=\frac12.
\]
For \(|M|=2\), the space \(\mathcal F(M)\) is one-dimensional and therefore has numerical index \(1\). Thus the value \(1/2\) begins exactly at three points and then remains independent of the cardinality.

## Assumptions and scope
Scaling the common distance does not change the numerical index, so normalize every nonzero distance to \(1\). Label the points by \(0,1,\ldots,N-1\), where \(N=|M|\). The free space can then be represented as
\[
H_0=\left\{\mu=(\mu_0,\ldots,\mu_{N-1})\in\mathbb R^N:\sum_{k=0}^{N-1}\mu_k=0\right\}
\]
with norm
\[
\|\mu\|=\frac12\sum_{k=0}^{N-1}|\mu_k|.
\]
Indeed, the total positive mass equals the total negative mass in absolute value, and transporting all positive mass directly to the negative support costs exactly that amount because every nonzero transport distance is \(1\). The reverse inequality follows by testing against the indicator of the positive support, which is a \(1\)-Lipschitz function for the equilateral metric.

For distinct indices \(i,j\), write \(u_{ij}=e_i-e_j\). Every \(u_{ij}\) has norm \(1\), and the unit ball of \(H_0\) is the convex hull of these molecules: any unit vector is decomposed by sending its positive mass to its negative mass.

## Proof
Let \(S:H_0\to H_0\) satisfy \(\|S\|=1\). Because the unit ball is the convex hull of finitely many molecules, there are distinct \(i,j\) with
\[
\|Su_{ij}\|=1.
\]
Put \(w=Su_{ij}\). The positive coordinates of \(w\) have total mass \(1\), and its negative coordinates have total mass \(-1\).

A dual norm-one functional may be represented, modulo additive constants, by a function on \(M\) of oscillation at most \(1\). In particular, if \(A\subsetneq M\) is nonempty, the indicator \(1_A\) has dual norm \(1\). To norm \(u_{ij}\), it suffices to choose \(A\) with \(i\in A\) and \(j\notin A\).

Such an \(A\) can always be chosen so that
\[
|1_A(w)|\ge\frac12.
\]
If \(w_i\ge0\) and \(w_j\le0\), take the positive support, adjusting zero coordinates only to include \(i\) and exclude \(j\); this gives value \(1\). If \(w_i\le0\) and \(w_j\ge0\), use the negative support analogously and obtain absolute value \(1\). If both \(w_i,w_j\ge0\), the two admissible choices obtained from the positive support with \(j\) removed and from the negative support with \(i\) inserted give absolute values \(1-w_j\) and \(1-w_i\). Since \(w_i+w_j\le1\), at least one is at least \(1/2\). If both \(w_i,w_j\le0\), the analogous two values are \(1-|w_i|\) and \(1-|w_j|\), and \(|w_i|+|w_j|\le1\) gives the same conclusion. Therefore the numerical radius of every norm-one operator is at least \(1/2\), so
\[
n(H_0)\ge\frac12.
\]

For the matching upper bound, choose three distinct indices \(0,1,2\) and define \(T:H_0\to H_0\) by
\[
(T\mu)_0=\frac{\mu_1-\mu_2}{2},\qquad
(T\mu)_1=\frac{\mu_2-\mu_0}{2},\qquad
(T\mu)_2=\frac{\mu_0-\mu_1}{2},
\]
with \((T\mu)_k=0\) for \(k\ge3\). The output coordinates sum to zero. If both endpoints of a molecule lie among \(0,1,2\), its image has one coordinate of absolute value \(1\) and two of absolute value \(1/2\), hence norm \(1\). If exactly one endpoint lies among those three indices, the image has norm \(1/2\); if neither does, the image is zero. Since the unit ball is the convex hull of molecules,
\[
\|T\|=1.
\]

Now let a norm-one dual functional \(f\) norm a molecule \(u_{ij}\), so \(f(u_{ij})=1\). Subtracting a constant, assume \(f_j=0\) and \(f_i=1\). The oscillation bound forces every other value of \(f\) into \([0,1]\). If neither endpoint lies among \(0,1,2\), then \(f(Tu_{ij})=0\). If exactly one endpoint lies there, then \(|f(Tu_{ij})|\le1/2\). If both endpoints lie there and \(k\) is the third distinguished point, then
\[
Tu_{ij}=\pm\left(e_k-\frac12(e_i+e_j)\right),
\]
so
\[
|f(Tu_{ij})|=\left|f_k-\frac12\right|\le\frac12.
\]
Finally, if \(x\) is any unit vector and \(f(x)=1\), write \(x\) as a convex combination of molecules. Since each molecule has \(f\)-value at most \(1\), every molecule receiving positive weight in this convex combination must itself have \(f\)-value \(1\). Hence
\[
|f(Tx)|\le\frac12.
\]
Thus \(v(T)\le1/2\). Together with the lower bound and \(\|T\|=1\), this proves
\[
n(\mathcal F(M))=\frac12.
\]

## Verification
The argument is finite-dimensional and analytic. The norm formula is checked directly by a transport plan and a matching dual Lipschitz function. The lower bound quantifies over an arbitrary norm-one operator and exhausts the four possible sign patterns of the two coordinates selected by a norming molecule. The upper-bound operator is defined on the whole zero-sum hyperplane; its norm is determined on the molecular convex hull, and its numerical radius estimate is first proved for every normed molecule and then extended to every norming pair by convex decomposition.

The boundary case \(|M|=2\) is separately checked: the free space is one-dimensional, so its numerical index is \(1\), not \(1/2\). No finite experiment or unproved classification is used in the proof.

## Relationship to prior work
Cobollo, Guirao, and Montesinos give an explicit formula for every two-dimensional Lipschitz-free space and identify the equilateral triangle as the case with numerical index \(1/2\). Their result therefore establishes the three-point instance but does not state the all-cardinality equilateral theorem above. The present argument uses the additional zero-sum \(\ell_1\)-hyperplane structure to obtain one dimension-independent formula for every finite equilateral metric with at least three points.

Sain, Paul, Bhunia, and Bag give a general finite-dimensional polyhedral method for estimating numerical indices and compute a particular family of three-dimensional prism norms. That general method does not itself imply the value for the equilateral Lipschitz-free family without the family-specific argument above. Aliaga and Pernecká characterize finitely supported extreme points of Lipschitz-free unit balls; for an equilateral metric their criterion is consistent with all molecules being extreme, but it does not determine this numerical-index value.

## Limitations
The theorem is only for finite equilateral metrics and real scalars. It makes no claim for complex Lipschitz-free spaces, infinite equilateral metrics, or non-equilateral finite metrics. Literature searches under Lipschitz-free, Arens--Eells, transportation-cost, root-polytope, and zero-sum \(\ell_1\)-hyperplane terminology did not reveal a statement implying the all-cardinality formula, but terminology outside those searches remains a residual originality risk.

## References
1. C. Cobollo, A. J. Guirao, and V. Montesinos, “The numerical index of 2-dimensional Lipschitz-free spaces,” arXiv:2304.13183, first submitted 25 April 2023; later published in Journal of Mathematical Analysis and Applications.
2. D. Sain, K. Paul, P. Bhunia, and S. Bag, “On the numerical index of polyhedral Banach spaces,” arXiv:1809.04778, first submitted 13 September 2018; Linear Algebra and its Applications 577 (2019), 121–133.
3. R. J. Aliaga and E. Pernecká, “Supports and extreme points in Lipschitz-free spaces,” Revista Matemática Iberoamericana 36 (2020), 2073–2089, DOI:10.4171/RMI/1191.
