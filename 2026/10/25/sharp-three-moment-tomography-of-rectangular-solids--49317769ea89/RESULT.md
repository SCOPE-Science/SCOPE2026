# Sharp three-moment tomography of rectangular solids

## Finding

Let \(B\subset\mathbb R^3\) be any nondegenerate Euclidean rectangular solid with three positive edge lengths. Choose \(X,Y\) independently and uniformly in its three-dimensional volume; write \(D=\|X-Y\|\) and \(M_{2j}=\mathbb E[D^{2j}]\). The triple \((M_2,M_4,M_6)\) determines \(B\) up to congruence. No shorter initial segment of consecutive even moments does so. The observable triples admit the exact scale-free feasibility description below, and reconstruction of normalized squared edge lengths has an optimal globally uniform Hölder exponent \(1/3\).

Put
\[
S_1=6M_2,\qquad S_2=\frac{180}{7}(M_4-M_2^2),\qquad
S_3=\frac{945}{11}(M_6-3M_4M_2+2M_2^3).
\]
Then the **squares** of the three edge lengths are precisely the three positive real roots, counted with multiplicities, of
\[
P(z)=z^3-e_1z^2+e_2z-e_3,
\quad e_1=S_1,\quad e_2=\frac{S_1^2-S_2}{2},\quad
 e_3=\frac{S_1^3-3S_1S_2+2S_3}{6}.
\]
For an explicit feasibility criterion let
\[
x=\frac{M_4}{M_2^2},\quad y=\frac{M_6}{M_2^3},\quad
u=\frac57(x-1),\quad v=\frac{35}{88}(y-3x+2),\quad
H(u)=\frac{[2(3u-1)]^{3/2}}{36}.
\]
A triple of real moments arises from a nondegenerate rectangular solid if and only if \(M_2>0\) and one of the following mutually exclusive conditions holds:

* \(u=1/3\) and \(v=1/9\);
* \(1/3<u<1/2\) and \(u-2/9-H(u)\le v\le u-2/9+H(u)\);
* \(1/2\le u<1\) and \((3u-1)/2<v\le u-2/9+H(u)\).

Both curved boundary branches where admissible correspond to two equal edge lengths. The excluded lower boundary for \(u\ge1/2\) corresponds to a vanishing edge, and the isolated cusp corresponds to cubes. Moreover,
\[
\operatorname{Vol}(B)^2=36M_2^3(1-3u+2v).
\]
If \(r_1\le r_2\le r_3\) and \(\tilde r_1\le\tilde r_2\le\tilde r_3\) are the sorted squared edge lengths normalized to sum one for two solids, then with \(\delta=|u-\tilde u|+|v-\tilde v|\),
\[
\max_{1\le i\le3}|r_i-\tilde r_i|\le6(2\delta)^{1/3}.
\]
The exponent \(1/3\) cannot be replaced by any larger exponent in a uniform bound, even in an arbitrarily small neighborhood of a cube.

## Assumptions and scope

The sampling measure is normalized three-dimensional Lebesgue measure **inside** the box, not boundary arclength or area, random lines, directional widths, or projected areas. \(D\) is Euclidean straight-line distance, not surface geodesic distance. The box is nondegenerate, so all three edges are strictly positive. Orientation and permutation of edges are immaterial to congruence. No assumption that lengths are pairwise distinct is made. The feasibility criterion concerns exact population moments; statistical finite-sample estimators and their sampling-error rates are not asserted.

## Proof

**1. Independent squared coordinate differences.** Write the squared edge lengths \(s_i>0\). In a coordinate-aligned box, the differences \(X_i-Y_i\) in different coordinates are independent, and \(X_i-Y_i=\sqrt{s_i}(U_i-V_i)\) with independent \(U_i,V_i\sim\operatorname{Unif}[0,1]\). Thus \(Z=D^2=\sum_{i=1}^3s_iW_i\), where the \(W_i=(U_i-V_i)^2\) are independent copies of \(W\). The density of \(|U-V|\) on \([0,1]\) is \(2(1-t)\), giving
\[
\mathbb E[W^k]=2\int_0^1 t^{2k}(1-t)\,dt=\frac{2}{(2k+1)(2k+2)}
\]
for every nonnegative integer \(k\). Therefore its first three cumulants are exactly
\[
\kappa_1(W)=1/6,\quad\kappa_2(W)=7/180,\quad\kappa_3(W)=11/945.
\]
Independence and homogeneity of cumulants yield \(\kappa_j(Z)=\kappa_j(W)\sum_i s_i^j\) for \(j=1,2,3\). Replacing cumulants by raw moments of \(Z\) gives the displayed formulas for \(S_j=\sum_i s_i^j\). Newton's identities prove the cubic reconstruction, including all repeated-root cases.

**2. Exact feasible moment region.** Normalize \(r_i=s_i/S_1>0\), so \(\sum r_i=1\). The first step proves \(u=\sum r_i^2\) and \(v=\sum r_i^3\). Hence \(1/3\le u<1\), and Newton's identities show these numbers are the roots of
\[
q(z)=z^3-z^2+\frac{1-u}{2}z-\frac{1-3u+2v}{6}.
\]
Writing \(z=w+1/3\), the cubic becomes
\[
w^3-\frac{3u-1}{6}w+\frac{9u-9v-2}{27}=0.
\]
Its discriminant is nonnegative exactly when
\[
|v-(u-2/9)|\le\frac{[2(3u-1)]^{3/2}}{36}=H(u).
\]
A real-rooted cubic with roots summing to one, \(0<(1-u)/2\), and positive product has three positive roots: if two roots were negative, the sum of pair products would be negative; one negative root would force the product negative. Positivity of the product is precisely \(v>(3u-1)/2\). For \(1/3<u<1/2\), even a triple of nonnegative roots has \(u\ge1/2\) if any root vanishes, so the full discriminant interval consists of positive roots. At \(u=1/2\), its lower endpoint has a zero root, and for \(u>1/2\) the positivity condition cuts off the lower discriminant branch. At \(u=1/3\), all roots equal \(1/3\). These observations prove necessity and sufficiency of the three displayed cases, including every endpoint; \(e_3=s_1s_2s_3\) gives the volume identity.

**3. Two moments do not suffice.** For any \(0<t<1/2\), consider squared-edge triples
\[
(s_1,s_2,s_3)^+=(1+2t,1-t,1-t),\qquad
(s_1,s_2,s_3)^-=(1-2t,1+t,1+t).
\]
Both have \(S_1=3\) and \(S_2=3+6t^2\), so both have \(M_2=1/2\) and \(M_4=11/30+7t^2/30\), but their unordered squared-edge sets are different. Their sixth moments differ by \(44t^3/315>0\). In fact, at every normalized second power sum strictly between \(1/3\) and \(1/2\), the positive intersection of the plane \(\sum r_i=1\) and sphere \(\sum r_i^2=u\) is a circle of noncongruent shapes, so an initial two-moment observation can have continuously many solutions.

**4. Uniform stability.** For two normalized root triples, write their cubics \(q,\tilde q\) as in step 2 and \(\delta=|u-\tilde u|+|v-\tilde v|\). Their \(z\)-coefficients differ by at most \(\delta/2\), and their constant coefficients by at most \(\delta/2\). If \(0<\delta<1/2\), put \(R=(2\delta)^{1/3}<1\) and take the union of the three closed complex disks of radius \(R\) centered at the roots of \(q\). On the boundary of this union, every distance to an old root is at least \(R\), so \(|q(z)|\ge R^3=2\delta\); also \(|z|\le2\) and \(|q(z)-\tilde q(z)|\le\delta(|z|+1)/2\le3\delta/2\). Rouché's theorem on each connected component, with tangencies resolved by an arbitrarily small increase of \(R\), gives the same root count with multiplicity for the two cubics in that component. Since all their roots are real, order-matching within each component pairs every root at distance at most \(6R\) (there are at most three overlapping disks). The components are separated along the real axis, so this is also the globally sorted matching. For \(\delta\ge1/2\), the asserted bound is trivial since both normalized triples lie in \((0,1)^3\). At \(\delta=0\), the cubics agree exactly. This proves the Hölder bound.

For the two families in step 3, the normalized \(u\) is the same, the normalized \(v\) differs by \(4t^3/9\), and the maximum difference between the sorted normalized squared-edge triples is \(2t/3\). A putative larger uniform exponent would demand \(O(t)\le O(t^{3\alpha})\) with \(\alpha>1/3\), impossible as \(t\downarrow0\). Thus the exponent is sharp near the cube.

## Verification

The standalone `verify.py` uses Python's standard library alone. It **independently** computes the first three raw moments using a multinomial expansion of \(\sum s_iW_i\), rather than the cumulant inversion used in the proof. It checks exact rational recovery of all three elementary symmetric functions and the normalized moment identities for 2,197 triples of positive rational squared lengths; verifies the discriminant, strict volume condition and box volume identity; checks four exact two-moment ambiguity pairs and their sixth-moment differences; and checks the unit cube's moments \((1/2,11/30,211/630)\). A seeded simulation of 260,000 independent pairs is a secondary numerical diagnostic only. The executable exits nonzero on a failed assertion. Finite checks do not replace the all-parameter analytic proof.

## Relationship to prior work

The density and arbitrary moments for the **single unit cube** were calculated by Mathai, Moschopoulos and Pederzoli (1999); their forward cube formulas do not by themselves state the present three-parameter inverse identification, complete normalized feasible region or sharp reconstruction stability. Marsaglia, Narasimhan and Zaman (1990), and Bäsel (2012), treat forward point-distance laws for planar rectangles and related triangles, not volume-uniform point pairs in three-dimensional variable boxes. Coleman (1981) treats intercept lengths for random probes through boxes, a different sampling operation. Abas (2026), Theorem 6.8 and Corollary 6.9, reconstructs rectangular boxes from the first three cumulants of **uniform random-direction width** and provides its own feasible set; it studies a different observable, not independently sampled interior-point distances. The box-parameter cubic and its generic discriminant are shared algebraic geometry, not claimed new as general algebraic identities. The finding claimed here is the exact identification, feasible observation map and sharp stability for the specified **interior-pair Euclidean distance moments**.

## Limitations

The result is restricted to three-dimensional orthogonal rectangular boxes and exact noiseless population moments. It does not claim reconstruction of arbitrary parallelepipeds, other convex solids or non-Euclidean distances; nor does it provide an optimal Hölder constant or a finite-sample estimator. Historical priority is not independently certified. The full original 1999 cube paper was not obtained despite checking its open journal and author-posted locations; the verified metadata describes a cube rather than general rectangular solids. The 2026 width manuscript was inspected in the relevant inverse theorems, not exhaustively read in every section. Analogous unlocated work could reduce the priority claim.

## References

1. A. M. Mathai, P. G. Moschopoulos and G. Pederzoli, *Distance between random points in a cube*, Statistica 59 (1999), 61–81. DOI: `10.6092/issn.1973-2201/1104`; `https://rivista-statistica.unibo.it/article/view/1104`.
2. G. Marsaglia, B. Narasimhan and A. Zaman, *The distance between random points in rectangles*, Communications in Statistics: Theory and Methods 19 (1990), 4199–4212. DOI: `10.1080/03610929008830437`.
3. U. Bäsel, *The distribution function of the distance between two random points in a right-angled triangle*, arXiv:`1208.6228`, public version 30 August 2012, `https://arxiv.org/abs/1208.6228`.
4. R. Coleman, *Intercept lengths of random probes through boxes*, Journal of Applied Probability 18 (1981), 276–282. DOI: `10.2307/3213189`.
5. O. Abas, *Width distributions for rectangular boxes*, arXiv:`2608.03305`, public version 4 August 2026, particularly Theorem 6.8 and Corollary 6.9, `https://arxiv.org/abs/2608.03305`.
