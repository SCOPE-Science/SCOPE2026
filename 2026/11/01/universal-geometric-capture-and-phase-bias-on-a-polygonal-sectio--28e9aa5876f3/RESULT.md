# Universal geometric capture and phase bias on a polygonal section of an absolute-value planar map

## Finding

Let \(a>0\), \(b>2a\), and consider
\[
F_{a,b}(x,y)=(|x|-y+a,\ x-|y|+b),\qquad T=F_{a,b}^{3}.
\]
Put \(d=b-2a>0\) and define the natural bounded polygonal section \(K_{a,b}\) as the two-edge path joining
\[
P=(d,a),\qquad O=(0,b-a),\qquad V=(b+2a,2b+a).
\]
Let \(\lambda\) be normalized Euclidean arclength on \(K_{a,b}\), and set \(R=(d,2b-3a)\). The points \(P\) and \(R\) belong to the **same** prime-three orbit of \(F_{a,b}\), but are distinct fixed points of \(T\). Let \(J\subset K_{a,b}\) be the two-edge path \(P\to O\to R\), and \(\sigma\) its normalized arclength law. Write
\[
w=\frac{b-2a}{4b},\qquad \alpha=\frac{b-2a}{3b},\qquad\beta=\frac{2b+2a}{3b}.
\]
Then, for every integer \(m\ge1\), there is the **exact probability-measure identity**
\[
\boxed{T_*^m\lambda=
\left(\alpha-\frac{w}{3\,4^{m-1}}\right)\delta_P+
\left(\beta-\frac{2w}{3\,4^{m-1}}\right)\delta_R+
\frac{w}{4^{m-1}}\sigma.}
\tag{1}
\]
In particular \(\nu=\alpha\delta_P+\beta\delta_R\) is the limiting measure and, with the standard total-variation convention \(\|\mu-\nu\|_{\mathrm{TV}}=\sup_A|\mu(A)-\nu(A)|\),
\[
\boxed{\|T_*^m\lambda-\nu\|_{\mathrm{TV}}=\frac{b-2a}{4b}\,4^{-(m-1)}\quad(m\ge1).}
\tag{2}
\]
Thus the conditional mixing/capture factor \(1/4\) is **universal**, while the eventual phase probabilities vary with the ratio \(b/a\). For the original one-step dynamics, the three subsequences of pushforward probabilities converge to \(\nu\), \(F_*\nu\), and \((F^2)_*\nu\), respectively. They are distinct, so the full sequence has a period-three limiting ensemble rather than a single limit.

For \(z\in K_{a,b}\), define the block-clock capture time \(\tau(z)=\min\{m\ge0:T^m(z)\in\{P,R\}\}\), with \(\tau=\infty\) if necessary. Under \(\lambda\),
\[
\boxed{\mathbb P(\tau=1)=1-w,\qquad
\mathbb P(\tau=m)=\frac{3w}{4^{m-1}}\quad(m\ge2),\qquad
\mathbb E[\tau]=1+\frac{b-2a}{3b}.}
\tag{3}
\]
The probability-generating function is \(\mathbb E[z^\tau]=(1-w)z+3wz^2/(4-z)\), valid for \(|z|<4\). Every point of \(K_{a,b}\) except the unique repelling point \(Q=((b-2a)/3,(2b-a)/3)\) reaches \(\{P,R\}\) in finitely many block steps. The exceptional singleton has zero arclength probability.

## Assumptions and scope

All parameters are real with \(a>0\) and \(b>2a\). The initial probability is **uniform arclength on the specified two-edge finite section**, not planar Lebesgue measure, not an invariant law, and not a uniform distribution on the noncompact complete image \(F^3(Q_1)\). The finite section terminates at the natural breakpoint \(V\) where the image polygon becomes a horizontal ray. The clock counts applications of \(T=F^3\); it does not count individual updates of \(F\). The notation \(T_*^m\) denotes the measure pushforward under \(m\) iterates.

The segment paths meet only at their endpoints. The source's positive-quadrant image yields the coordinates of \(K\) and its breakpoints, but the probability and hitting-time identities are established below rather than assumed from the image description. The two atoms \(P,R\) are separated whenever \(b>2a\). At \(b=2a\) they merge at a fixed point of \(F\), so the strict inequality is essential for a two-phase statement.

## Proof

**Step 1: Exact two-edge conjugacy.** The length of \(K\) is \(2\sqrt2\,b\). Parameterize it by \(r\in[0,2b]\) so that Euclidean arclength equals \(\sqrt2\,dr\):
\[
X(r)=\begin{cases}
(d-r,a+r),&0\le r\le d,\\
(r-d,b-a+r-d),&d\le r\le2b.
\end{cases}
\tag{4}
\]
The points \(P,O,V,R\) correspond to \(r=0,d,2b,2d\), respectively. Directly evaluating the three affine absolute-value branches gives
\[
T(X(r))=X(S(r)),\qquad
\boxed{S(r)=\begin{cases}
0,&0\le r\le d/2,\\
4r-2d,&d/2\le r\le d,\\
2d,&d\le r\le2b.
\end{cases}}
\tag{5}
\]
Here are the critical sign checks, which also rule out unexamined changes of branch for arbitrary real parameters. On the first leg, \(X(r)=(d-r,a+r)\), the first image is
\[
F(X(r))=(d-2r,\ 2b-3a-2r),
\]
whose second coordinate stays at least \(a>0\). For \(r\le d/2\), the second image is \((-d,a)\) and the third image is \(P\). For \(r\ge d/2\), the second image is \((4r-3d,a)\), and its first coordinate changes sign exactly at \(r=3d/4\). The two resulting third-image expressions trace first \(P\to O\) and then \(O\to R\), at coordinate speed \(4\). On the second leg, \(X(r)=(r-d,b-a+r-d)\), the first image is always \((-d,a)\); its third image is \(R\). Thus (5) is an identity on all of the closed section, including boundaries.

The points \(0\) and \(2d\) are fixed by \(S\); the unique indefinitely nonabsorbed coordinate is \(r=2d/3\), the fixed point of the expanding middle branch. Its inverse branch contracts by \(1/4\), so the intersection of all finite survivors is this singleton. The corresponding point is \(Q=X(2d/3)\). Furthermore, \(F(P)=R\), \(F(R)=(2a-b,a)\), and \(F(2a-b,a)=P\), establishing the prime-three cycle claim.

**Step 2: Exact transfer on three probability types.** Let \(\mathsf u_J\) denote uniform arclength on \(J=X([0,2d])\). Formula (5) shows that \(S\) is constant at \(0\) on \([0,d/2]\), affine with slope \(4\) on \([d/2,d]\), and constant at \(2d\) on \([d,2d]\). These intervals occupy respectively \(1/4,1/4,1/2\) of the total \(r\)-length \(2d\). Since the middle interval maps linearly and bijectively onto \([0,2d]\), its uniform conditional law remains uniform after mapping. Consequently,
\[
\boxed{T_*\mathsf u_J=\tfrac14\delta_P+\tfrac12\delta_R+\tfrac14\mathsf u_J.}
\tag{6}
\]
Likewise, the three intervals \([0,d/2]\), \([d/2,d]\), and \([d,2b]\) have normalized lengths \(w,w,1-2w\) under uniform \(r\in[0,2b]\). Hence
\[
\boxed{T_*\lambda=w\delta_P+(1-2w)\delta_R+w\mathsf u_J.}
\tag{7}
\]
Since both atoms are fixed by \(T\), equations (6) and (7) solve by a geometric series, giving (1) with \(\sigma=\mathsf u_J\). Their coefficients sum to one exactly. The uniform component is nonatomic while the other components are atoms, so subtracting \(\nu\) from (1) and taking the supremum over Borel sets gives the **equality** (2), not merely an upper bound. Applying \(F_*\) and \((F^2)_*\) gives the original-time subsequence limits; all three are distinct because the prime-three cycle has three different points and both limiting weights are strictly between zero and one.

**Step 3: Capture law.** For \(m\ge1\), the surviving mass at time \(m\) is exactly the coefficient of \(\sigma\) in (1), namely \(w4^{-(m-1)}\). The only noncaptured orbit of positive-time indefinite duration is the repelling singleton \(Q\), which is null for \(\lambda\). Thus \(\Pr(\tau>m)=w4^{-(m-1)}\) for every \(m\ge1\); since \(\Pr(\tau>0)=1\) under nonatomic \(\lambda\), differencing successive tails proves the probability formulas in (3). Summation of the tails yields the mean, and summation of the geometric probability masses yields the generating function.

## Verification

The package contains the standalone Python standard-library checker `check_exact.py`. Run `python3 check_exact.py` from the extracted package directory. It compares the **original three-step planar map**, not merely the reduced interval formula, with (5) at all critical breakpoints and at points inside each branch for 36 exact rational parameter pairs. It additionally checks the three-cycle, polygon endpoints, normalization, finite-step mixture coefficients, limiting weights and expected capture time. The observed successful output is `EXACT_POLYGONAL_PHASE_LAW_OK: 3636 rational branch tests, 36 parameter pairs, 14 distribution levels`. The universal result follows from the symbolic sign argument and transfer equations (5)–(7), not from those finite tests.

## Relationship to prior work

Cima, Gasull, Mañosa and Mañosas explicitly construct this planar map, describe its eventual periodicity when \(a\ge0\), and give the relevant polygonal image and return-map branch actions in their 2024 preprint, Proposition 13 and Figure 1. Those facts and the two attracting fixed points of the three-step return are prior results, not claims of novelty here. The additional result is a **complete exact time-dependent arclength law** for a naturally bounded part of the image graph: parameter-dependent endpoint-phase weights, an exact total-variation coefficient for every step, and a full geometric capture-time distribution.

Published analyses of the same absolute-value family with the opposite affine sign \(a<0\) establish planar area escape and periodic-itinerary survivor laws near repelling cycles; those are different dynamics, sampling measures and questions, and their conclusions do not imply the present positive-\(a\) arclength phase distribution. General elementary transfer calculations explain the method but do not supply the exact parameter-dependent law on this geometrically defined section. Literature priority outside the inspected records is not guaranteed.

## Limitations

The conclusions describe uniform arclength on \(K_{a,b}\) and its pushforwards, not a global uniform initial distribution in the plane. The rate \(1/4\) is per **three** updates of the original map. While the original source describes the finite polygon and return branches, no wholly new attractor, periodic orbit, or entropy formula is asserted. The computation does not address the separate non-generic repelling three-cycle beyond the unique point of this section. It does not cover \(a\le0\) or \(b<2a\). The source's return-map diagram makes the renewal mechanism accessible, so independent assessment of publication priority is particularly important. No independent mathematical audit has been performed.

## References

1. A. Cima, A. Gasull, V. Mañosa and F. Mañosas, *Invariant graphs and dynamics of a family of continuous piecewise linear planar maps*, arXiv:2410.01052v1, publicly submitted 2024-10-01; especially Proposition 13, Figure 1 and Section 3. https://arxiv.org/abs/2410.01052
2. A. Cima, A. Gasull, V. Mañosa and F. Mañosas, *Invariant Graphs and Dynamics of a Family of Continuous Piecewise Linear Planar Maps*, *Qualitative Theory of Dynamical Systems* **24** (2025), article 70, DOI:10.1007/s12346-025-01221-1. https://link.springer.com/content/pdf/10.1007/s12346-025-01221-1.pdf
3. *Sharp three-visit onset and geometric escape from a repelling quadrant focus*, public mathematical note, 2026-10-11; a distinct negative-affine-sign regime and planar-area observable. https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-sharp-three-visit-onset-and-geometric-escape-from-a-repelling-qu--6aab6efd2c66
4. *Exact survival-area phase transitions near a repelling three-cycle*, public mathematical note, 2026-10-11; a distinct negative-affine-sign regime and itinerary-area observable. https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-exact-survival-area-phase-transitions-near-a-repelling-three-cyc--b99c0542d5f5
