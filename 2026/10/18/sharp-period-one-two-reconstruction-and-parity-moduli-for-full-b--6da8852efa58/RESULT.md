# Sharp period-one/two reconstruction and parity moduli for full-branch zigzag maps

## Finding

**Theorem (minimal periodic-coordinate rigidity for a full-branch zigzag).** Fix an integer \(m\ge2\) and strictly increasing knots \(0=b_0<b_1<\cdots<b_m=1\). Let \(T_{\mathbf b}:[0,1]\to[0,1]\) be the unique continuous function affine on each \([b_{i-1},b_i]\), with \(T_{\mathbf b}(b_i)=0\) for even \(i\) and \(T_{\mathbf b}(b_i)=1\) for odd \(i\). Write its **unlabelled** fixed-point set, in increasing order, as \(\{p_1<\cdots<p_m\}\); here \(p_1=0\) and \(p_m=1\) precisely when \(m\) is odd. Define the smallest exact-period-two coordinate

\[
q(T_{\mathbf b})=\min\{x\in[0,1]:T_{\mathbf b}^{2}(x)=x,\ T_{\mathbf b}(x)\ne x\}.
\]

Then:

1. If \(m\) is even, the fixed-point set alone determines every knot \(b_i\), hence the map.
2. If \(m\) is odd, the family of all maps in this class with the given fixed-point set is naturally an open interval of pairwise distinct maps, with \(t=b_1\) as affine parameter for every other knot. No fixed-point information alone can distinguish them.
3. For **every** \(m\ge2\), the least exact-period-two point exists, visits branch one and then branch two, and obeys

\[
\boxed{q=\frac{p_2 b_1}{1-p_2+b_1}},\qquad
\boxed{b_1=\frac{q(1-p_2)}{p_2-q}}.
\]

Consequently, for odd \(m\), adjoining **only the scalar coordinate** \(q\) to the unordered fixed-point set determines the entire map. On the fixed-point fiber, \(q\) is strictly increasing, with

\[
\frac{dq}{dt}=\frac{p_2(1-p_2)}{(1-p_2+t)^2}>0.
\]

The optimal maximum period of periodic coordinates needed for universal exact identification in this class is therefore **one for even \(m\)** and **two for odd \(m\)**. The data do not include labels for the periodic orbits or an assignment of fixed points to branches; the ordering is recovered from their coordinates.

## Assumptions and scope

The number \(m\), the interval \([0,1]\), the alternating endpoint values, and the full-branch affine model class are known. All knots are strictly separated; no equal-length or constant-slope assumption is imposed. Branch \(i\) is \([b_{i-1},b_i]\) (one-indexed). Each branch maps onto \([0,1]\), with slope magnitude \(1/(b_i-b_{i-1})>1\). There are exactly \(m\) fixed points, one per branch, and the exact-period-two set is nonempty and finite. The quantities \(p_i\) and \(q\) are *locations* of periodic points in the original coordinate, not merely their counts or periods. No assertion is made about noisy, finite-precision recovery or general non-full-branch interval maps.

## Proof

**Step 1: fixed-point locations and the parity obstruction.** On odd branch \(i\), the formula is \(T(x)=(x-b_{i-1})/(b_i-b_{i-1})\); on even branch it is \(T(x)=(b_i-x)/(b_i-b_{i-1})\). The respective fixed points satisfy

\[
p_i=\begin{cases}
\dfrac{b_{i-1}}{1-b_i+b_{i-1}},&i\text{ odd},\\[2mm]
\dfrac{b_i}{1+b_i-b_{i-1}},&i\text{ even}.
\end{cases}
\]

Because each inverse branch is a strict contraction, each branch contains precisely one fixed point. These points appear in increasing branch order, and no interior knot is fixed because its image is an endpoint. Thus the indexed \(p_i\) are recovered just by sorting the unlabelled fixed-point set. The first fixed point is \(p_1=0\). For each interior branch \(2\le i\le m-1\) the knot equation rearranges to

\[
b_i=\begin{cases}
1-\dfrac{1-p_i}{p_i}b_{i-1},&i\text{ odd},\\[2mm]
\dfrac{p_i}{1-p_i}(1-b_{i-1}),&i\text{ even}.
\end{cases}
\tag{1}
\]

Here all denominators are nonzero because \(0<p_i<1\) for those indices. Starting from \(b_1=t\), equation (1) determines each \(b_i=A_i+B_i t\), with \(B_1=1\) and \(B_i\ne0\) by induction: every step multiplies the coefficient by a strictly negative nonzero number. If \(m\) is even, the last (even) branch has \(b_m=1\), so its fixed point is \(p_m=1/(2-b_{m-1})\). Hence \(b_{m-1}=2-1/p_m\); since \(B_{m-1}\ne0\), this determines exactly one \(t\). If \(m\) is odd, its last (odd) branch has the endpoint fixed point \(p_m=1\), imposing no new condition on \(b_{m-1}\). Conversely all choices of \(t\) for which \(0<t<b_2(t)<\cdots<b_{m-1}(t)<1\) hold yield the same entire fixed-point set by the displayed equations. These finitely many strict affine inequalities define a nonempty open interval containing the given \(t\); because \(b_1=t\), distinct parameters define distinct maps.

**Step 2: exhaust the exact-period-two points.** Write the inverse branch \(g_i:[0,1]\to[b_{i-1},b_i]\), which has Lipschitz constant \(b_i-b_{i-1}<1\). For each ordered pair \(i\ne j\), the contraction \(g_i\circ g_j\) has a unique fixed point \(x_{ij}\) in the interiors of branch \(i\), and \(T(x_{ij})\) lies in the interior of branch \(j\). (The fixed point lies in the interior because \(g_j([0,1])\) is contained in \((0,1)\) except possibly at an endpoint, and a boundary cycle would map within the two endpoints, which are fixed or preperiodic, not exactly period two.) This is an exact-period-two point: a point fixed by \(T\) would stay in the same branch, contrary to \(i\ne j\). Conversely every exact-period-two point has an ordered itinerary \(i,j\) with \(i\ne j\), because any two-periodic itinerary on one branch would be a fixed point of its contracting inverse. Thus the \(m(m-1)\) points \(x_{ij}\) exhaust the exact-period-two set, and no branch-boundary point belongs to it.

**Step 3: identify the globally least point without orbit labels.** Every exact-period-two point in branch \(i\ge2\) is strictly greater than \(b_1\). For \(i=1\), the inverse branch \(g_1(y)=b_1y\) is strictly increasing. Since the ranges of \(g_j\) are ordered left to right, for \(2\le j<k\le m\) their composite images satisfy \(g_1(g_j([0,1]))<g_1(g_k([0,1]))\) in interval order (allowing shared endpoints only at the extreme images, which no periodic point attains). Therefore the least exact-period-two point is \(x_{12}\), the branch-one/branch-two itinerary, with \(0<x_{12}<b_1\). Let \(u=b_2\), \(t=b_1\), and \(q=x_{12}\). Since \(T(q)=q/t\in(t,u)\) and the second branch descends linearly,

\[
q=T^2(q)=\frac{u-q/t}{u-t},\qquad
q=\frac{tu}{1+t(u-t)}.
\tag{2}
\]

The second fixed point satisfies \(p_2=u/(1+u-t)\), hence \(u=p_2(1-t)/(1-p_2)\). Substitute into (2) and simplify to obtain \(q=p_2t/(1-p_2+t)\). In particular \(q<p_2\) and solving for \(t\) gives the second boxed identity. Holding \(p_2\) fixed, differentiate the first boxed identity to obtain the stated strictly positive derivative.

**Step 4: optimality, not merely sufficiency.** For even \(m\), Step 1 shows period-one coordinates suffice. For odd \(m\), Step 1 supplies an open continuum of distinct maps having *identical* period-one sets, so the maximum period one cannot identify the map. Step 3 shows that one unmarked period-two coordinate then uniquely determines \(b_1\) and, through (1), all remaining knots, so maximum period two suffices. There is no smaller positive maximum period. \(\square\)

**Concrete boundary witness.** For \(m=3\), choose \(\mathbf b=(0,t,1-t,1)\), with \(0<t<1/2\). Then \(\operatorname{Fix}(T_{\mathbf b})=\{0,1/2,1\}\) independently of \(t\), whereas \(q=t/(1+2t)\). The choices \(t=1/4\) and \(t=1/3\) give distinct maps with identical fixed-point sets and respective least two-period coordinates \(1/6\) and \(1/5\).

## Verification

A self-contained standard-library script, `verification.py`, implements all branch inverse maps over exact rational numbers; computes every fixed point and every two-cycle from its ordered branch pair; and reconstructs the knot vector from the proposed data. Running `python verification.py` prints `Exact deterministic rational samples passed: 271`. The finite diagnostic covers \(2\le m\le14\) with twenty deterministic rational knot samples for each \(m\), plus distinct fixed-set-preserving perturbations and a whole five-sample three-lap family. Every identity above is proved for all admissible real knots independently of those finite tests.

## Relationship to prior work

Fuhrmann, Gröger and Passeggi [1, Theorem A] prove that the complete collection of periodic orbits, treated as unlabeled subsets, determines a topologically mixing interval map. Their result does **not** specify a sharp finite-period cutoff or finite inverse-coordinate formulas for this variable-knot full-branch affine family. The fixed-point-fiber parity and its resolution by a single leftmost period-two coordinate are the additions assessed here. Chen, Shi and Xu [2] provide formulas for periodic points of two-branch skew tent maps, and Shi [3] supplies formulas for periodic points of discontinuous asymmetric Bernoulli shifts. Neither inspected source gives the stated multibranch parity classification or minimal unmarked two-coordinate reconstruction. The original full text of [1] was inspected; the complete publisher text of [2] was not available, so a residual historical-priority risk remains.

## Limitations

The knot count, endpoint behavior and affine full-branch hypothesis are essential. The result concerns exact periodic **positions**, not period counts: all maps with the same \(m\) have the same abstract full-shift orbit counts, which cannot reconstruct knot lengths. It gives no error-stability bounds for approximate observations and does not address nonsawtooth or non-full-branch maps. It is a self-reviewed mathematical argument, not an independent audit or independent historical-priority certification.

## References

[1] Gabriel Fuhrmann, Maik Gröger, Alejandro Passeggi, *Period spectrum and rigidity of interval maps*, arXiv:2610.07435v1, first posted 2026-10-05, https://arxiv.org/abs/2610.07435.

[2] Kai Chen, Yong-Guo Shi, Bing Xu, *Periodic Points of Skew Tent Maps*, *Journal of Dynamical and Control Systems* (2022), DOI:10.1007/s10883-022-09594-1.

[3] Yong-Guo Shi et al., *Periodic Points of Asymmetric Bernoulli Shifts*, *Journal of Mathematics* (2021), DOI:10.1155/2021/1965479.
