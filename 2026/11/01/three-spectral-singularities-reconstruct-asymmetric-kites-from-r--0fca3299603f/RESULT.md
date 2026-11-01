# Three spectral singularities reconstruct asymmetric kites from random widths

## Finding
Let \(K_{r,p,q}\) be the strictly convex Euclidean kite with vertices \((\pm r,0),(0,-pr),(0,qr)\), where \(r>0\) and \(0<p\le q\). Let \(W\) denote the length of its orthogonal projection onto a Haar-uniform unoriented line. Write
\[
 \alpha=\arctan(1/q),\quad \beta=\arctan(1/p),\quad
 \tau=\arctan q,\quad R=\sqrt{1+q^2},\quad S=p+q,
\]
\[
 m_1=\frac{2q}{R},\qquad m_2=\frac{S}{\sqrt{1+p^2}}.
\]
For \(w>0\), set \(v=w/r\), and define the integer-valued branch counts
\[
 n_1(w)=\mathbf1_{\{m_1<v<2\}},\qquad
 n_3(w)=\mathbf1_{\{m_2<v<S\}},
\]
\[
 n_2(w)=\begin{cases}
 \mathbf1_{\{\alpha<\tau-\arccos(v/R)<\beta\}}+
 \mathbf1_{\{\alpha<\tau+\arccos(v/R)<\beta\}},&0<v<R,\\
 0,&v\ge R.
 \end{cases}
\]
Outside the finite set of critical widths, the exact probability density of \(W\) is
\[
 \boxed{ f_W(w)=\frac2\pi\left(
 \frac{n_1(w)}{\sqrt{(2r)^2-w^2}}
 +\frac{n_2(w)}{\sqrt{(rR)^2-w^2}}
 +\frac{n_3(w)}{\sqrt{(rS)^2-w^2}}
 \right). }
\]
A term with zero branch count is interpreted as zero, even when its denominator is not real. The distribution has no atoms; the density is zero outside its attained width interval. In the three-peak regime \(q>1\) and \(pq<1\), the width has exactly two strict angular cusp minima and three local-maximum height classes: \(2r\), \(rR\), and \(rS\), counting their possible coincident heights with multiplicity. In the other open regimes \(q<1\) and \(q>1,pq>1\), there is only one cusp minimum and no middle-branch interior maximum. Equality boundaries are obtained from the same density formula.

In the *ordered triple-peak region*
\[
 \boxed{1<q<\sqrt3,\qquad 0<p<\sqrt{1+q^2}-q,\qquad r>0,}
\]
the three distinct square-root divergence locations of \(f_W\), in increasing order, are
\[
 \boxed{z_1=r(p+q)<z_2=r\sqrt{1+q^2}<z_3=2r.}
\]
Their singular amplitudes satisfy
\[
 \boxed{\lim_{w\uparrow z_i}\sqrt{z_i^2-w^2}\,f_W(w)
 =\begin{cases}2/\pi,&i=1,3,\\4/\pi,&i=2.\end{cases}}
\]
There are no further diverging density points. Thus the *unlabeled width distribution alone* recovers the kite up to Euclidean congruence:
\[
 \boxed{r=z_3/2,\qquad q=\sqrt{(z_2/r)^2-1},\qquad p=z_1/r-q.}
\]
This inverse depends smoothly on the three singularity locations and is uniformly Lipschitz on compact subsets of the stated open parameter region with \(r\) bounded above and away from zero.

## Assumptions and scope
The random direction is Haar-uniform modulo sign, not a uniform affine line conditioned on intersection. The kite has a genuine reflection axis, with the shorter axial tip labelled \(p\). The ordered region is exactly a natural subregion of the three-peak phase in which its three stationary maximum heights are strictly ordered; it includes the numerically proposed asymmetric-kite minimizer of Akiyama and Kamae's four-gon width-deviation problem. The theorem does not claim that that numerical candidate globally minimizes the deviation rate.

## Proof
Write the unoriented direction as \((\cos\theta,\sin\theta)\). Reflection symmetry reduces its angular law to \(\theta\in[0,\pi/2]\) with constant density \(2/\pi\). The two opposed support functions give, exactly,
\[
 W(\theta)=r\bigl[\max(\cos\theta,p\sin\theta)+\max(\cos\theta,q\sin\theta)\bigr].
\]
Because \(p\le q\), the active vertices switch at \(\alpha\le\beta\), yielding
\[
 \frac{W(\theta)}r=\begin{cases}
 2\cos\theta,&0\le\theta\le\alpha,\\
 \cos\theta+q\sin\theta=R\cos(\theta-\tau),&\alpha\le\theta\le\beta,\\
 S\sin\theta,&\beta\le\theta\le\pi/2.
 \end{cases}
\]
The first branch is strictly decreasing, and the third strictly increasing. The middle branch has stationary point \(\tau\). It lies strictly inside its interval precisely when \(q>1\) and \(pq<1\). When it does, it is a strict maximum, and both switch points are strict local minima: at \(\alpha\), the two one-sided derivatives have respective signs \(-,+\), while at \(\beta\), they have signs \(-,+\). When the middle stationary point lies outside, its branch is monotone and only one switch point is a cusp minimum. At parameter equalities the formula itself gives the limiting degeneracies.

On a monotone subarc with profile \(A\cos(\theta-\theta_0)\), the change-of-variables Jacobian for \(W=rA\cos(\theta-\theta_0)\) is \(1/\sqrt{(rA)^2-w^2}\). For the first and third arcs the preimage count is the indicator stated above. The middle arc's preimages are \(\theta=\tau\pm\arccos(w/(rR))\), hence its exact count is \(n_2(w)\). Summing all preimages with weight \(2/\pi\) proves the density and absence of atoms.

In the ordered region, \(p+q<R<2\) holds by definition. The middle critical point exists because \(q>1\) and \(pq<1\) follows from \(p<R-q=1/(R+q)\). At \(z_1=rS\) and \(z_3=2r\), exactly one angular branch approaches a nondegenerate maximum; its inverse-Jacobian produces coefficient \(2/\pi\). At \(z_2=rR\), both sides of the middle maximum contribute, producing coefficient \(4/\pi\). All other angular branches are regular or absent at these heights. At each switching-point value, the relevant one-sided derivatives are nonzero, so the density has at most finite one-sided jumps; there are no other divergences. Sorting the three singularities then gives the displayed inverse algebraically. The inverse uses rational operations and a positive square root on the specified open region, so it is smooth there and uniformly Lipschitz on every compact parameter subdomain after bounding the scale.

## Verification
The accompanying standalone program evaluates the exact branch-count density and verifies its total mass against adaptive numerical integration for five different kite shapes in the three qualitative regimes. It checks the ordered-peak amplitudes at two successively smaller offsets from each singularity and exactly reconstructs a sample kite with \(p=1/4\), \(q=3/2\), \(r=17/10\). The output is `ALL_CHECKS_PASSED`. These finite numerical checks support, but do not replace, the all-parameter analytic proof above.

## Relationship to prior work
Akiyama and Kamae (first public preprint January 18, 2022) study directional-width deviation of convex polygons, prove extremal classifications outside powers of two, and exhibit a numerical asymmetric-kite candidate in their open four-gon problem. Their complete available preprint treats the first two width moments, not the full random-width density or its triple-singularity inversion. Kim, Yaskin and Zvavitch (2015) establish a broad geometric-tomography framework and show that arbitrary convex bodies need not be determined by unlabeled projection information; that general nonuniqueness does not cover the restricted inverse theorem here. A published classification for centrally symmetric tangential polygons determines angular-gap multisets from their width laws; the asymmetric kites here are not centrally symmetric or members of that class. A distinct sharp reconstruction theorem for parallelograms uses their mean, second moment, and maximum width; a kite in the ordered region is not a parallelogram. Research on kite geometric dilation concerns intrinsic boundary length divided by Euclidean chord length, not projection width. The forward branchwise change-of-variables computation is elementary; priority is claimed only for the stated all-parameter phase/density classification together with the ordered three-singularity reconstruction.

## Limitations
No global congruence classification is asserted outside the ordered region. The result requires exact population width distributions; it supplies no finite-sample rates for locating density singularities. Singular heights can collide or disappear on the parameter boundaries. The general inverse-projection literature is extensive, and historical-priority checks cannot exclude an unindexed equivalent calculation.

## References
1. S. Akiyama and T. Kamae, *Width deviation of convex polygons*, arXiv:2201.06736v1 (public January 18, 2022), https://arxiv.org/abs/2201.06736; full-text section 6 and section 7.
2. J. Kim, V. Yaskin and A. Zvavitch, *Distribution functions of sections and projections of convex bodies*, arXiv:1512.07289v1 (December 22, 2015), https://arxiv.org/abs/1512.07289.
3. *Inverse classification of projection-width distributions for tangential symmetric polygons*, publicly indexed research result (2026), published-finding corpus research repository.
4. *Three unlabeled width statistics reconstruct a parallelogram with sharp stability*, publicly indexed research result (2026), published-finding corpus research repository.
5. *Exact Geometric Dilation and Its Unique Minimizer Among Convex Kites*, publicly indexed research result (2026), published-finding corpus research repository.
