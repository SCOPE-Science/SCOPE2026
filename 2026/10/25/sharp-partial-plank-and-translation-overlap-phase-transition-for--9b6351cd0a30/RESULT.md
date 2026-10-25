# Sharp partial-plank and translation-overlap phase transition for squares

## Finding

Let \(Q=[-1,1]^2\) and \(0<W<2\). Among all finite families of Euclidean planks whose total width is at most \(W\), the maximum covered area is exactly
\[
\mathcal A_Q(W)=
\begin{cases}
 2\sqrt2\,W-\frac12W^2,&0<W\le\sqrt2,\\
 2+\frac12W^2,&\sqrt2\le W<2.
\end{cases}
\]
There is an optimal **single** plank, and every optimal single plank is centered at the origin. For \(0<W\le\sqrt2\), its unoriented normal is a square diagonal. For \(\sqrt2<W<2\), its normal is a unit vector \(n=(n_1,n_2)\) with
\[
 |n_1|+|n_2|=\frac2W.
\]
These descriptions give all optimizing single-plank directions, up to the dihedral symmetries of the square. In the oblique regime the normal makes the angle
\[
 \theta_*(W)=\frac\pi4-\arccos\!\left(\frac{\sqrt2}{W}\right)
\]
with the nearer coordinate axis. No coordinate-axis normal maximizes for \(0<W<2\).

Equivalently, if \(g_Q(z)=\operatorname{area}(Q\cap(Q+z))\), then the **minimum** at fixed translation length is
\[
 \min_{\|z\|_2=W}g_Q(z)=
\begin{cases}
 \left(2-\frac{W}{\sqrt2}\right)^2,&0<W\le\sqrt2,\\
 2-\frac12W^2,&\sqrt2\le W<2.
\end{cases}
\]
Every minimizing translation has exactly the same set of unit directions as the optimal single-plank normals. The gain over keeping a diagonal normal beyond the transition is exactly \((W-\sqrt2)^2\), and the optimizing oblique angle bifurcates at square-root speed:
\[
 \frac\pi4-\theta_*(W)\sim2^{1/4}\sqrt{W-\sqrt2}
 \quad (W\downarrow\sqrt2).
\]
This is one geometric phase-transition theorem, expressed in equivalent plank and covariogram forms.

## Assumptions and scope

A plank is a closed strip \(\{x\in\mathbb R^2: |\langle n,x\rangle-b|\le w/2\}\) with unit normal \(n\), center offset \(b\), and Euclidean width \(w\). Finite families may overlap and have nonparallel normals; their widths sum to at most \(W\). Boundaries have zero area. The square has side length two and area four. Only \(0<W<2\), below its minimum width, is asserted. The classification concerns maximizing *single* planks; it does not classify all possible optimal finite families. The covariogram concerns translations of one identically oriented square, never rotations.

## Proof

**1. Exact square-covariogram minimization.** For any translation \(z\) of Euclidean norm \(W\), put \(t=W/2\), \(a=|z_1|/2\), and \(b=|z_2|/2\). Since \(0<t<1\), both coordinate overlaps are positive, and
\[
 g_Q(z)=4(1-a)(1-b),\qquad a^2+b^2=t^2.
\]
Writing \(s=a+b\), the complete-square identity is
\[
 \frac{g_Q(z)}4=1-s+\frac{s^2-t^2}{2}
 =\frac{1-t^2}{2}+\frac{(s-1)^2}{2}.
\]
As \(a,b\ge0\) and \(a^2+b^2=t^2\), the attainable values are **exactly** \(s\in[t,\sqrt2t]\). If \(0<t\le1/\sqrt2\), this interval ends at or before one, and the unique optimal value is \(s=\sqrt2t\), realized by \(a=b=t/\sqrt2\). If \(1/\sqrt2<t<1\), the interval contains one in its interior; its unique minimizing sum is \(s=1\), realized by the two positive solutions of
\[
 \{a,b\}=\left\{\frac{1+\sqrt{2t^2-1}}2,\frac{1-\sqrt{2t^2-1}}2\right\}.
\]
Substitution yields the displayed minimum covariogram and every minimizing translation direction. In the latter range \(a+b=1\) is equivalent to \(|n_1|+|n_2|=1/t=2/W\) for \(n=z/W\).

**2. From overlap to arbitrary finite plank families.** We invoke the planar partial-plank theorem of Bakaev and Polyanskii, arXiv:2607.27483, Theorem 12 with its Corollary 7 and Lemma 11 (see References). Their result and its proof yield, for any planar convex body \(K\) and \(0<W<w(K)\),
\[
 \max_{\sum_i w_i\le W}\operatorname{area}\!\left(K\cap\bigcup_i P_i\right)
 =\operatorname{area}(K)-\min_{\|z\|_2=W}\operatorname{area}\bigl(K\div\{-z/2,z/2\}\bigr),
\]
where \(K\div A=\{x:x+A\subseteq K\}\). The upper bound comes from their Bang-map reduction to a two-point Minkowski subtraction (Corollary 7); Lemma 11 and Theorem 12 provide an attaining single plank. For the square, the subtraction set is the coordinate rectangle with side lengths \(2-|z_1|\) and \(2-|z_2|\). Its area equals \(g_Q(z)\) for every \(\|z\|_2=W<2\). Thus \(\mathcal A_Q(W)=4-\min_{\|z\|_2=W}g_Q(z)\). Evaluating Step 1 proves the complete two-branch formula for every finite family, not only parallel families.

**3. The maximizing single planks and their centers.** For a unit normal, by square symmetry take \(n=(C,S)\) with \(C=\cos\theta\ge S=\sin\theta\ge0\) and \(0\le\theta\le\pi/4\). If \(X,Y\) are independent uniform variables on \([-1,1]\), then the covered-area fraction of a central plank of half-width \(t\) is \(\Pr(|CX+SY|\le t)\). Direct convolution of two uniform densities gives
\[
 F(C,S,t)=\begin{cases}
 t/C,&0\le t\le C-S,\\
 1-\dfrac{(C+S-t)^2}{4CS},&C-S<t<C+S.
 \end{cases}
\]
The second line is understood only when \(S>0\). For a diagonal normal \(C=S=1/\sqrt2\), it equals \(\sqrt2t-t^2/2\), precisely \(\mathcal A_Q(W)/4\) in the first regime. For a normal with \(C+S=1/t\) in the second regime, \(t>C-S\): indeed \((C-S)^2=2-t^{-2}<t^2\) for \(0<t<1\). The formula now gives \(F=(1+t^2)/2=\mathcal A_Q(W)/4\). So every covariogram-minimizing direction is realized by its centered plank.

Conversely, the one-plank Bang-map bound of Lemma 5 of the cited paper gives the covered area of a single plank with unit normal \(n\) at most \(4-g_Q(Wn)\): its area-preserving map embeds the eroded set \(Q\div\{-Wn/2,Wn/2\}\) into the region not covered by that plank. If the plank attains \(\mathcal A_Q(W)\), the normal must therefore minimize \(g_Q\), so Step 1 lists every optimal direction. For each such direction, \(t>C-S\) (including the diagonal, whose difference is zero). The density of \(CX+SY\) is symmetric, constant only on \([-(C-S),C-S]\), and strictly decreasing on \((C-S,C+S)\). Since \(t>C-S\), shifting a width-\(2t\) interval away from zero strictly decreases its probability; thus the plank's center offset must be zero. This proves the complete single-plank optimizer classification.

**4. The phase-transition refinements.** In the oblique regime, \(C+S=\sqrt2\cos(\pi/4-\theta)=2/W\), giving \(\theta_*(W)\). The diagonal central plank still covers \(2\sqrt2 W-W^2/2\), and subtraction from the sharp second branch gives exactly \((W-\sqrt2)^2\). Since \(\arccos(1-\varepsilon)\sim\sqrt{2\varepsilon}\), the angle has the stated square-root onset. At \(W=\sqrt2\), both branches and optimizing directions coincide. No unstated extrapolation beyond \(0<W<2\) is used.

## Verification

The algebraic identity and constrained interval in Step 1 prove the covariogram claim for all admissible translations; the primary cited theorem passes this optimization to **all** finite plank families. The density formulas in Step 3 directly establish attainment and single-plank rigidity, including boundary and transition cases. The standalone standard-library checker `check_square.py` additionally performs exact rational convex-polygon clipping: at \(W=10/7\), the optimal normal \(n=(4/5,3/5)\) gives covered area \(148/49\); exact off-center cuts lose area. It verifies six other rational direction/width cases and performs ten dense angular sweeps and phase-gain comparisons. These finite computations corroborate but do not replace the analytic proof. Run `python3 check_square.py` after extracting both files to the same directory.

## Relationship to prior work

Bakaev and Polyanskii (2026), arXiv:2607.27483, prove the deep theorem that an optimal partial plank covering of **every planar convex body** can be chosen as a single plank. They do not calculate the square's sharp width-dependent value or classify its optimal directions; their geometric reduction is explicitly cited and used here. A published result entitled *A complete translation-distance phase diagram for hypercube covariograms* (2026) classifies **maximizers** of overlap at a fixed translation length; its RESULT.md explicitly excludes the **minimum**, which is the extremum calculated here. The maximum-overlap problem undergoes discrete coordinate-support transitions, whereas the new minimum-overlap counterpart develops continuously rotating oblique minimizers above \(W=\sqrt2\). General covariogram-reconstruction results such as Bianchi (2013/2016) and general overlap bounds such as Schymura (2010) address different quantifiers and do not state this sharp square-specific minimum/optimizer phase diagram. The computation is elementary once its structural reduction is isolated; no broad novelty beyond the stated exact profile and equality classes is asserted.

## Limitations

The finite-family partial-cover conclusion depends on the stated published planar theorem; a wholly independent new proof of that theorem is not claimed. The present computation is only for a Euclidean square under translations or strips, not for arbitrary rectangles, higher-dimensional cubes, rotations, infinite plank sequences, or a classification of all multistrip extremizers. A finite checker cannot certify an infinite statement; the analytic steps above carry that burden. Although searches found no equivalent published minimum-profile calculation, a classical treatment of fixed-distance square overlap under another terminology might exist.

## References

1. E. Bakaev and A. Polyanskii, *Optimal partial plank coverings*, arXiv:2607.27483, first submitted 2026-07-29, especially Corollary 7, Lemma 11, Theorem 12; https://arxiv.org/abs/2607.27483.
2. *A complete translation-distance phase diagram for hypercube covariograms*, publicly accessible result, 2026-10-11, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-a-complete-translation-distance-phase-diagram-for-hypercube-cova--5fadf7c81348/RESULT.md.
3. G. Bianchi, *The covariogram and Fourier-Laplace transform in* \(\mathbb C^n\), arXiv:1312.7816 (first submitted 2013-12-30); https://arxiv.org/abs/1312.7816.
4. D. Schymura, *An upper bound on the volume of the symmetric difference of a body and a congruent copy*, arXiv:1010.2446 (first submitted 2010-10-12); https://arxiv.org/abs/1010.2446.
