# Three sharp fixed-point transitions and invariant islands for reduced planar rotations

## Finding

Let \(Q=[0,1)^2\) and, for \(0<\theta<2\pi\), define the generally discontinuous map
\[
T_\theta(x,y)=\bigl\{R_\theta(x,y)\bigr\}\in Q,
\qquad R_\theta=\begin{pmatrix}\cos\theta&-\sin\theta\\\sin\theta&\cos\theta\end{pmatrix},
\]
where braces mean reduction of both coordinates into \([0,1)\). Set
\[
\alpha_1=2\arctan(1/2),\qquad \alpha_2=\pi/2,
\qquad \alpha_3=2\arctan(2).
\]
The **complete fixed-point count** is
\[
\#\operatorname{Fix}(T_\theta)=
1+\sum_{j=1}^{3}\mathbf 1_{\{\alpha_j<\theta<2\pi-\alpha_j\}}.
\tag{1}
\]
In particular the successive counts, as the angle increases from zero to \(\pi\), are \(1,2,3,4\). All inequalities at the three birth angles are strict, so a newly born fixed point is absent exactly at its threshold.

The fixed-point locations are also explicit. For \(0<\theta<\pi\), put \(u=\cot(\theta/2)>0\). Besides the origin, the entire fixed set consists exactly of the following points whenever their displayed condition holds:
\[
\begin{array}{c|c}
\text{condition}&\text{center}\\\hline
u<2&z_1=(1/2,u/2)\\
u<1&z_2=((1-u)/2,(1+u)/2)\\
u<1/2&z_3=(1-u/2,1/2+u).
\end{array}
\tag{2}
\]
For \(\pi<\theta<2\pi\), replace \(u\) by \(|\cot(\theta/2)|\) and interchange both coordinates in each listed point. At \(\theta=\pi\), the four fixed representatives are \((0,0)\), \((1/2,0)\), \((0,1/2)\), and \((1/2,1/2)\).

Every nonzero fixed point in (2) lies in the interior of \(Q\) and is the center of a **nonempty exactly invariant open Euclidean disk**. The sharp radii of the largest disks centered at these points and contained in the fundamental square are
\[
\begin{aligned}
r_1(u)&=\tfrac12\min\{u,2-u\} &&(0<u<2),\\
r_2(u)&=\tfrac12(1-u) &&(0<u<1),\\
r_3(u)&=\min\{u/2,1/2-u\} &&(0<u<1/2).
\end{aligned}
\tag{3}
\]
The disks are pairwise disjoint and support mutually singular, absolutely continuous invariant probabilities (normalized planar area on each disk). In fact each disk is acted on by the exact Euclidean rotation through \(\theta\) about its own center. At \(\theta=\pi\), the disk of radius \(1/2\) centered at \((1/2,1/2)\) is invariant; the other two nonzero fixed representatives lie on the square's boundary.

Writing \(\mathcal A(\theta)\) for the area of the disjoint union of the displayed invariant disks, for \(\theta\ne\pi\) one has the **exact constructive invariant-area law**
\[
\mathcal A(\theta)=\pi\left[
\mathbf1_{\{u<2\}}r_1(u)^2+
\mathbf1_{\{u<1\}}r_2(u)^2+
\mathbf1_{\{u<1/2\}}r_3(u)^2
\right],\qquad u=|\cot(\theta/2)|.
\tag{4}
\]
At \(\theta=\pi\), \(\mathcal A(\pi)=\pi/4\). The birth of each nonzero fixed-center island has a strictly positive quadratic area onset on the side where it exists. Equation (4) describes these particular fixed-center islands, **not** all possible periodic islands of \(T_\theta\).

## Assumptions and scope

The domain is the canonical half-open square \(Q=[0,1)^2\). The map uses **coordinatewise fractional-part reduction after an ordinary Euclidean rotation**; unless the rotation matrix is integral it is not a continuous torus group endomorphism. The angle is any real \(0<\theta<2\pi\). The excluded angles congruent to zero modulo \(2\pi\) give the identity map, with an uncountable fixed set. The special angle \(\theta=\pi\) is handled separately because several fixed points lie on the chosen half-open boundary.

The fixed-point count is exhaustive. The invariant-disk statements concern only positive-radius disks centered at nonzero fixed points and contained in \(Q\), and provide constructive invariant probabilities. They do not classify other ergodic invariant measures, periodic cycles, or maximal invariant regions of more general shapes.

## Proof

**Step 1: All fixed points reduce to a finite lattice problem.** A point \(z=(x,y)\in Q\) is fixed if and only if
\[
(I-R_\theta)z=(a,b)\in\mathbb Z^2.
\tag{5}
\]
For \(0<\theta<\pi\) put \(u=\cot(\theta/2)>0\). Direct inversion of \(I-R_\theta\), whose determinant is \(4\sin^2(\theta/2)>0\), gives
\[
(x,y)=\left(\frac{a-ub}{2},\frac{ua+b}{2}\right).
\tag{6}
\]
Also \(\cos\theta=(u^2-1)/(u^2+1)\) and \(\sin\theta=2u/(u^2+1)\), whence
\[
a=\frac{2(x+uy)}{1+u^2},\qquad b=\frac{2(y-ux)}{1+u^2}.
\tag{7}
\]
As \(0\le x,y<1\), the first quantity is nonnegative and strictly less than \(2(1+u)/(1+u^2)\le1+\sqrt2<3\). Equality \(a=0\) forces \(x=y=0\). Moreover,
\[
-1\le\frac{-2u}{1+u^2}< b <\frac{2}{1+u^2}\le2,
\]
where the lower strict bound remains true even at \(u=1\), because \(x<1\). Consequently, at a nonzero fixed point \(a\in\{1,2\}\) and \(b\in\{0,1\}\). The four possibilities are completely exhausted by (6): \((a,b)=(2,0)\) gives \(x=1\), excluded; \((1,0)\) is valid precisely for \(u<2\); \((1,1)\) precisely for \(u<1\); \((2,1)\) precisely for \(u<1/2\). This proves (2) with every boundary convention checked.

**Step 2: The opposite rotation orientation and the central angle.** Coordinate interchange \(J(x,y)=(y,x)\) preserves \(Q\) and satisfies \(JR_\theta J=R_{2\pi-\theta}\). It conjugates the reduced maps. Thus the classification for \(\pi<\theta<2\pi\) is the coordinate swap of (2) at angle \(2\pi-\theta\). At \(\theta=\pi\), equation (5) becomes \(2(x,y)\in\mathbb Z^2\), giving the four stated representatives. Finally \(u<2,1,1/2\) is respectively equivalent to \(\alpha_j<\theta<2\pi-\alpha_j\). Equation (1) follows for all permitted angles.

**Step 3: The invariant disks and their exact radii.** If \(z\) is an interior fixed point and \(R_\theta z=z+k\), with \(k\in\mathbb Z^2\), let \(r=\operatorname{dist}(z,\partial Q)\). For every \(v\) with \(\|v\|<r\), both \(z+v\) and \(z+R_\theta v\) lie in \(Q\), so coordinatewise reduction gives exactly
\[
T_\theta(z+v)=z+R_\theta v.
\tag{8}
\]
Thus the open disk \(B(z,r)\) maps bijectively onto itself, by rotation. Its radius is maximal among open disks centered at \(z\) and contained in \(Q\), by the definition of boundary distance. Computing the four distances \(x,1-x,y,1-y\) for the centers in (2) gives (3); the swapped centers have the same radii. At \(\pi\), the center \((1/2,1/2)\) has radius \(1/2\).

To prove that the disks are pairwise disjoint, for \(0<u<1\) the squared center separation of \(z_1,z_2\) is \((1+u^2)/4>1/4\), whereas \(r_1+r_2=1/2\). For \(0<u<1/2\) the separation of \(z_2,z_3\) is again \(\sqrt{1+u^2}/2>1/2\), whereas \(r_2+r_3\le1/2\). The separation of \(z_1,z_3\) is \(\sqrt{(1+u^2)/2}>1/\sqrt2\), while \(r_1+r_3\le u<1/2\). Reflection preserves all separations. Normalized two-dimensional Lebesgue measure on each disk is invariant by (8), and disjoint support makes these probabilities mutually singular. Taking areas proves (4).

**Step 4: The sharp area-onset exponent.** At a birth threshold \(u=c\in\{2,1,1/2\}\), the newly appearing disk radius on the valid side is respectively \((2-u)/2\), \((1-u)/2\), and \(1/2-u\) for sufficiently close \(u<c\). Since \(d(\cot(\theta/2))/d\theta=-(1+u^2)/2\ne0\), its area is a positive constant times squared angular displacement from the threshold plus a higher-order remainder. This uses a local statement about the newly added disk, not a claim that the total area is differentiable at every threshold.

## Verification

An accompanying standard-library Python checker computes rotation matrices at rational half-angle cotangents, exhaustively solves (5) over an integer rectangle guaranteed to contain all admissible displacement vectors, and compares the result with (2), including exact thresholds and both orientations. It also verifies the boundary-distance radii and squared-separation disjointness inequalities in exact rational arithmetic, plus the four-point special case at \(\theta=\pi\). All 23 classification cases passed.

The infinite-angle theorem follows from the lattice bounds and explicit proof above, not the finite test set. Reproduction command: `python3 check.py`.

## Relationship to prior work

Michael Blank, *Invariant measures of torus piecewise isometries* (first public version June 30, 2021), studies this exact map as the restriction of planar rotation in Section 7. Proposition 7.1 supplies a sufficient angle range for existence of a nontrivial fixed point, and Propositions 7.2–7.3 describe invariant neighborhoods of periodic points. That analysis does **not** give the exhaustive fixed-point count, three sharp fixed-point threshold angles, complete location table, or explicit disjoint fixed-center island-area function (1)–(4). The present result is a quantitative specialization and does not replace the general existence theory.

Lowenstein and Vivaldi, *Approach to a rational rotation number in a piecewise isometric system* (2009), analyze a different square piecewise-isometric map defined by a nonorthogonal \(2\times2\) matrix with a single-coordinate modulo correction, and obtain asymptotic areas of periodic islands. Their model, invariant metric and return-map claims do not imply the angle-by-angle fixed-center classification here.

These comparisons concern actual mathematical implications. No priority claim is made against sources not inspected in full or against unindexed special-case formulas that may already exist.

## Limitations

The classification concerns period-one points, not points of all periods. Equation (4) measures an explicit, provably invariant subset rather than the complete invariant or recurrent area. The half-open representative matters at exactly the angle \(\pi\), where some fixed points sit on the boundary; a statement for alternative boundary conventions must be adjusted. Circle measures inside the disks are ergodic for irrational \(\theta/(2\pi)\), but normalized disk area is not claimed ergodic. Independent scientific or publication-priority validation has not been performed.

## References

1. M. Blank, *Invariant measures of torus piecewise isometries*, arXiv:2106.16021 (v1 first public June 30, 2021; inspected v2, especially Section 7, Propositions 7.1–7.3). https://arxiv.org/abs/2106.16021
2. J. H. Lowenstein and F. Vivaldi, *Approach to a rational rotation number in a piecewise isometric system*, arXiv:0909.3458 (first public September 18, 2009; inspected Introduction, definitions and main results). https://arxiv.org/abs/0909.3458
3. J. H. Lowenstein and F. Vivaldi, *Renormalization of a one-parameter family of piecewise isometries*, arXiv:1406.6910 (abstract and model compared). https://arxiv.org/abs/1406.6910
