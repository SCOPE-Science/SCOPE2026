# Five fixed chord-moment directions reconstruct every parallelogram, and four need not

## Finding
Let \(P\subset\mathbb R^2\) be an unknown nondegenerate Euclidean parallelogram. For each unoriented unit vector \(e\), sample an affine line parallel to \(e\) by selecting its signed orthogonal offset uniformly in the interval of offsets that meet \(P\). Write \(C_e\) for the resulting chord length and \(m_1(e)=\mathbb EC_e\), \(m_2(e)=\mathbb EC_e^2\).

**Five-view reconstruction theorem.** For *any* five pairwise nonparallel prescribed unoriented directions \(e_1,\ldots,e_5\), the ten numbers \(\{m_1(e_i),m_2(e_i)\}_{i=1}^5\) determine \(P\) uniquely up to translation. The statement includes directions parallel to sides and all positive aspect ratios.

**Sharp universal number of directions.** There exist four pairwise nonparallel directions and two noncongruent parallelograms with identical *entire* chord-length distributions along each of the four directions. Hence five is the smallest number guaranteeing recovery for **every** choice of prescribed distinct directions. No claim is made that every choice of four directions is ambiguous.

## Assumptions and scope
All bodies are nondegenerate compact Euclidean parallelograms; there is no measurement noise. Direction vectors have known Euclidean orientation and unit normalization, and the transverse offset, *not an interior point or a rotation angle*, is uniformly sampled at each fixed direction. Such a body, translated to its center, admits exactly the strip representation
\[
P=\{x\in\mathbb R^2:|\alpha(x)|\le1,\ |\beta(x)|\le1\},
\]
where \(\alpha,\beta\) are linearly independent real linear forms. Reversing the sign of either form, or swapping forms, does not change the body. In the formulae below, \(e\) is a Euclidean unit direction.

## Proof
**1. The exact one-direction chord law.** Change variables to \((u,v)=(\alpha(x),\beta(x))\), sending the parallelogram to \([-1,1]^2\). Replace the forms by their negatives if necessary, and swap them, so their directional evaluations are \(\alpha(e)=a\ge b=\beta(e)\ge0\), with \(a>0\). The transversal coordinate \(t=bu-av\) is constant on lines parallel to \((a,b)\), takes every value in \([-a-b,a+b]\), and is uniform because it is a fixed nonzero multiple of physical signed orthogonal offset. For \(|t|\le a-b\), the line crosses both vertical edges of the square, yielding Euclidean chord length \(2/a\). For \(a-b\le|t|\le a+b\), the remaining length decreases linearly from \(2/a\) to zero. At \(b=0\), the two tails vanish and every chord has length \(2/a\). Hence
\[
\mathcal L(C_e)=(1-p)\operatorname{Unif}[0,L]+p\delta_L,\qquad L=\frac2a,\quad p=\frac{a-b}{a+b}.
\]
This covers \(a=b\), for which \(p=0\) and the entire law is uniform, as well as \(b=0\), for which \(p=1\).

**2. Two moments invert that law.** Direct integration gives
\[
m_1=\frac{L(1+p)}2,\qquad m_2=\frac{L^2(1+2p)}3.
\]
Consequently, writing
\[
z=\sqrt{1-\frac{3m_2}{4m_1^2}}=\frac{p}{1+p}\in[0,1/2],
\]
we obtain \(p=z/(1-z)\), \(a=(1+p)/m_1\), and \(b=(1-p)/m_1\). In particular the two moments recover exactly the unordered nonnegative pair \(\{|\alpha(e)|,|\beta(e)|\}\).

**3. Five distinct projective directions suffice.** Given the recovered evaluations at \(e_i\), form
\[
s_i=|\alpha(e_i)|^2+|\beta(e_i)|^2,\qquad
 d_i=\big||\alpha(e_i)|^2-|\beta(e_i)|^2\big|.
\]
Write the homogeneous quadratic forms
\[
S(x)=\alpha(x)^2+\beta(x)^2,\qquad D(x)=\alpha(x)^2-\beta(x)^2.
\]
The values \(s_i=S(e_i)\) at any three distinct projective points determine the degree-two binary form \(S\), because a nonzero homogeneous quadratic cannot vanish on three distinct projective points. Suppose another form \(D'\) fits all five unsigned values \(|D'(e_i)|=d_i=|D(e_i)|\). Then the binary quartic \(D^2-D'^2\) vanishes at five distinct projective directions. Any nonzero binary quartic has at most four distinct projective zeros, so this quartic vanishes identically. Factorization in the integral domain \(\mathbb R[x,y]\) gives \(D'=D\) or \(D'=-D\). Thus the pair of positive-semidefinite rank-one forms \((S+D)/2=\alpha^2\), \((S-D)/2=\beta^2\) is uniquely determined up to swap. Each square recovers its linear form up to an irrelevant sign; the two strips and hence \(P\) are recovered up to their common center/translation. This argument holds even if some \(D(e_i)=0\).

**4. An exact four-direction obstruction.** Define
\[
P_0=\{(x,y): |2x|\le1,\ |y|\le1\},
\]
\[
P_1=\left\{(x,y):\left|\frac{6x+4y}{5}\right|\le1,\ \left|\frac{-8x+3y}{5}\right|\le1\right\}.
\]
Both pairs of strip forms have determinant \(2\), so they bound nondegenerate parallelograms of equal area. At the four respective nonunit direction vectors \((1,1)\), \((1,6)\), \((1,-4)\), and \((3,-2)\), the unordered absolute strip evaluations of *both* bodies are respectively \(\{1,2\}\), \(\{2,6\}\), \(\{2,4\}\), and \(\{2,6\}\). Normalizing each direction divides both evaluations by the same vector length, so Step 1 gives coincident whole chord laws and hence every moment. However \(P_0\) is a rectangle and \(P_1\) is not: its two strip-normal vectors have inner product \(-36/25\ne0\). They are not congruent. Any subcollection of the four directions also fails to distinguish them. This proves the sharp universal view threshold. \(\square\)

## Verification
The included standalone standard-library Python script `check_chords.py` reproduces the four-direction obstruction using exact rational arithmetic, enumerates all signs in an exact five-direction binary-quadratic recovery example, and numerically integrates independent line-clipping chords over 21 body/direction pairs. It separately checks moment inversion at the two endpoint atoms and intermediate mixture weights. Its successful output ends with `ALL_CHECKS_PASSED`. The finite checks are supplementary; the proof above establishes the universal statement.

## Relationship to prior work
Gasparyan and Ohanyan (2014) already derived the directional chord distribution for parallelograms, and Martirosyan (2023) gave orientation-dependent chord laws for general convex quadrilaterals. The per-direction forward law is **not claimed as new**. Nagel (1993) proved recognition of polygons using the entire direction-dependent chord distribution; Averkov and Bianchi (2009) established uniqueness from the full planar covariogram. These stronger *full-direction* data do not imply recovery at an arbitrary fixed finite selection, nor do they give the exact universal five-view threshold or the four-view counterexample. Gasparyan and Ohanyan (2013) reported that arbitrary finite directional chord data need not determine general triangles; that contrast emphasizes that the theorem is restricted to centrally symmetric four-sided bodies. The specific contribution is two-moment five-view identifiability **for every direction set** together with a matching four-view obstruction.

## Limitations
The body class is precisely the family of nondegenerate parallelograms. The theorem does not identify arbitrary quadrilaterals or triangles, and makes no claim that every four-direction configuration is ambiguous. It requires exact population chord moments with uniform transverse offsets, known observation directions, and full Euclidean length calibration. Stable finite-sample reconstruction and robustness to noise are unproved. Priority remains provisional if an earlier specialized finite-direction inverse theorem exists; author-uploaded full text of the closest 2014 paper was compared, but not every older tomography source was exhaustively indexed.

## References
1. A. G. Gasparyan and V. K. Ohanyan, "Covariogram of a Parallelogram," *Journal of Contemporary Mathematical Analysis* **49** (2014), 194–206, DOI: 10.3103/S1068362314040050. Public author-uploaded full text: https://www.researchgate.net/publication/270759872_Covariogram_of_a_Parallelogram.
2. D. M. Martirosyan, "Orientation-Dependent Chord Length Distribution in a Convex Quadrilateral," *Journal of Contemporary Mathematical Analysis* **58** (2023), 416–430, published 2023-12-28, DOI: 10.3103/S1068362323060055. Open article: https://link.springer.com/article/10.3103/S1068362323060055.
3. W. Nagel, "Orientation-dependent chord length distributions characterize convex polygons," *Journal of Applied Probability* **30** (1993), 730–736. https://doi.org/10.2307/3214779.
4. G. Averkov and G. Bianchi, "Confirmation of Matheron's conjecture on the covariogram of a planar convex body," *Journal of the European Mathematical Society* **11** (2009), 1187–1202. https://doi.org/10.4171/JEMS/179.
5. A. G. Gasparyan and V. K. Ohanyan, "Recognition of triangles by covariogram," *Journal of Contemporary Mathematical Analysis* **48** (2013), 110–122. https://doi.org/10.3103/S1068362313030023.
