# Finite-jet Crofton tomography of the distance spectrum of circular perforations

## Finding
Let \(W\subset\mathbb R^2\) be an arbitrary compact convex body with interior and known perimeter \(P>0\). Let \(p_1,\ldots,p_n\in\operatorname{int}W\) be distinct, with \(n\ge2\), and write \(d_{ij}=\|p_i-p_j\|\), \(M=\binom n2\). For all sufficiently small radii \(r>0\), remove the open disks \(B(p_i,r)\) from \(W\). Sample an unoriented affine line by Euclidean-motion-invariant line measure, conditioned on hitting \(W\), and let \(C_r\) be the number of connected components of its intersection with the perforated body. Define the one-dimensional observable
\[
G(r)=\mathbb E\binom{C_r-1}{2}.
\]
For \(s_{ij}=2r/d_{ij}\), the **exact second factorial component law** is
\[
\boxed{G(r)=\frac2P\sum_{i<j}d_{ij}\left(s_{ij}\arcsin s_{ij}+\sqrt{1-s_{ij}^{2}}-1\right).}
\]
In particular, if
\[
c_k=\frac{\binom{2k-2}{k-1}}{4^{k-1}(2k-1)(2k)}>0,
\]
then, in a neighborhood of zero,
\[
\boxed{G(r)=\frac2P\sum_{k\ge1}c_k(2r)^{2k}
\sum_{i<j}d_{ij}^{1-2k}.}
\]
**Finite-jet inverse theorem:** The first \(2M\) nonzero even Taylor coefficients of \(G\), namely the coefficients of \(r^2,r^4,\ldots,r^{4M}\), uniquely and constructively determine the entire unordered multiset \(\{d_{ij}:i<j\}\), including repeated distances. No directions, line offsets, labels, or individual hole-hit events are observed. The result holds for every convex window \(W\); its geometry enters the formula only through \(P\).

An auxiliary exact identity is \(\mathbb E C_r=1+2\pi nr/P\), so \(n\) itself is encoded by the initial mean slope when the perimeter is known.

## Assumptions and scope
Set
\[
r_* =\min\left\{\min_i\operatorname{dist}(p_i,\partial W),\ \frac12\min_{i<j}d_{ij}\right\}>0.
\]
The theorem concerns every real \(0<r<r_*\). Then the open holes have disjoint closures and are strictly contained in \(W\). The perforated body is \(K_r=W\setminus\bigcup_i B(p_i,r)\). A line is written \(\ell_{\theta,t}=\{x:x\cdot u_\theta=t\}\), with \(u_\theta=(\cos\theta,\sin\theta)\) and \(0\le\theta<\pi\); its invariant measure is \(d\theta\,dt\), normalized by the total measure \(P\) of lines meeting \(W\). Tangent lines form a null set, so \(C_r\) is unambiguous almost surely. The theorem concerns exact idealized probability laws, not recovery from finitely many noisy observations.

## Proof
**1. Normalization and topological reduction.** For each direction, the set of offsets for lines meeting \(W\) is an interval of length \(w_W(u_\theta)\). Cauchy's projection formula yields
\[
\int_0^\pi w_W(u_\theta)\,d\theta=P.
\]
Because \(W\) is convex, almost every hitting line cuts \(W\) in one interval. Each of its transversal crossings of an interior circular hole removes one disjoint open subinterval and therefore increases the number of surviving components by exactly one. If \(I_i(\theta,t)\) is the indicator that \(\ell_{\theta,t}\) crosses hole \(i\), then almost surely
\[
C_r-1=\sum_{i=1}^n I_i.
\]
The offsets hitting a fixed hole constitute an interval of length \(2r\) for each direction. Hence \(\mathbb E(C_r-1)=n(2\pi r)/P\).

**2. Pairwise Crofton kernel.** For a pair of distinct centers at distance \(d>2r\), the offset intervals have centers separated by \(d|\cos\theta|\), after rotating coordinates. Their common offset length is
\[
(2r-d|\cos\theta|)_+.
\]
Writing \(s=2r/d\in(0,1)\) and integrating over \(\theta\in[0,\pi)\) gives
\[
\begin{aligned}
\int_0^\pi(2r-d|\cos\theta|)_+\,d\theta
&=2\int_{\arccos s}^{\pi/2}(2r-d\cos\theta)\,d\theta\\
&=2d\bigl(s\arcsin s+\sqrt{1-s^2}-1\bigr).
\end{aligned}
\]
Divide by \(P\) for the joint crossing probability. Since \(\binom{C_r-1}{2}=\sum_{i<j}I_iI_j\), linearity of expectation proves the exact formula; intersections of three or more projected offset intervals do not change this pair factorial moment.

**3. Positive analytic expansion.** Put \(F(s)=s\arcsin s+\sqrt{1-s^2}-1\). Then \(F(0)=0\) and \(F'(s)=\arcsin s\). Termwise integration of the classical absolutely convergent arcsine series for \(|s|<1\) gives
\[
F(s)=\sum_{k\ge1}c_ks^{2k},\qquad
c_k=\frac{\binom{2k-2}{k-1}}{4^{k-1}(2k-1)(2k)}.
\]
As \(r<r_*\le\frac12\min_{i<j}d_{ij}\), the finite sum can be expanded termwise. Let
\[
\mu_j=\sum_{i<j}d_{ij}^{-(2j+1)},\qquad j=0,1,\ldots .
\]
The coefficient of \(r^{2j+2}\) in \(G\) is exactly \(2^{2j+3}c_{j+1}\mu_j/P\). All denominators are nonzero, so the first \(2M\) even coefficients determine \(\mu_0,\ldots,\mu_{2M-1}\).

**4. Finite Hankel reconstruction, including collisions.** Let \(t_1,\ldots,t_L\) be the distinct positive values in the multiset \(\{d_{ij}^{-2}\}\), with \(1\le L\le M\), and define the strictly positive weights \(w_a=\sum_{d_{ij}^{-2}=t_a}d_{ij}^{-1}\). Then
\[
\mu_j=\sum_{a=1}^L w_a t_a^j.
\]
The \(M\)-by-\(M\) Hankel matrix \(H=(\mu_{i+j})_{0\le i,j<M}\) factors into a Vandermonde matrix, a positive diagonal matrix, and its transpose, so \(\operatorname{rank}H=L\). The leading \(L\)-by-\(L\) Hankel block is positive definite. Solve uniquely for \(a_0,\ldots,a_{L-1}\) from
\[
\sum_{h=0}^{L-1}a_h\mu_{j+h}=-\mu_{j+L},\qquad0\le j<L.
\]
The monic polynomial \(T(z)=z^L+\sum_{h=0}^{L-1}a_hz^h\) has exactly the simple roots \(t_1,\ldots,t_L\). Its roots recover the distinct distances \(t_a^{-1/2}\). The first \(L\) moments form an invertible Vandermonde system for the weights \(w_a\), and each distance's multiplicity is exactly \(w_a/\sqrt{t_a}\). This reconstruction uses at most \(\mu_{2M-1}\), hence precisely the stated finite jet suffices. All assertions include coinciding pair distances.

## Verification
The accompanying self-contained Python 3 file `check.py` checks the pairwise Crofton kernel against independent angular quadrature for five geometries, performs exact rational Hankel recovery on the four collinear centers \(0,1,3,6\) with distance multiset \(\{1,2,3,3,5,6\}\), checks twelve Taylor coefficients, and uses invariant-line Monte Carlo sampling for a two-hole square window. It passed with

`LINE_TOPOLOGY_INVERSE_OK comparisons=19 exact_roots=5 sample_pair=0.065274 predicted_pair=0.065062`

The exact rational reconstruction explicitly tests a repeated distance. This finite verification corroborates the formulas but does not replace the proof in the previous section. Reproduce by running `python3 check.py` with standard Python 3; no third-party package is required.

## Relationship to prior work
Classical Cauchy–Crofton integral geometry provides the invariant-line normalization and perimeter formula. Jiao, Stillinger and Torquato (2009) study pair-distance distributions and demonstrate that they may be shared by noncongruent point configurations. Their data are pair correlations, not a finite Taylor jet of random line-section component counts of a perforated convex window. Jiao, Stillinger and Torquato's work on the connectedness of random textures (public arXiv version in 2012, with an earlier 2009 journal article) develops lineal-path and cluster functions and numerical inverse reconstructions, not the displayed exact two-hole crossing kernel combined with the finite-jet multiset reconstruction. The present claim is the inverse identifiability of the **unlabeled distance multiset** from a one-parameter family of section-topology factorial moments, not a claim to introduce pair correlations or Crofton measure.

## Limitations
The theorem does **not** recover labels, orientations, absolute center positions, or necessarily a configuration up to congruence: noncongruent finite point sets can share the same pair-distance multiset. It does not claim that identical pair distances imply identical full component-count distributions, which can contain higher-order information. It assumes equal disk radii varying together, disks pairwise disjoint and wholly inside one convex window, and the motion-invariant offset-and-angle distribution (not the distribution obtained by sampling a random point inside the window and then a line through that point). The inverse uses exact high-order Taylor data and no numerical stability bound is established. Older stereology literature may contain an equivalent transform; priority has not been independently adjudicated.

## References
1. Y. Jiao, F. H. Stillinger, S. Torquato, *Geometrical Ambiguity of Pair Statistics. I. Point Configurations*, arXiv:0908.1366, publicly submitted 2009-08-10; https://arxiv.org/abs/0908.1366.
2. Y. Jiao, F. H. Stillinger, S. Torquato, *A Superior Descriptor of Random Textures and Its Predictive Capacity*, arXiv:1201.0710, publicly submitted 2012-01-03; https://arxiv.org/abs/1201.0710; earlier journal appearance in 2009.
3. B. Lu and S. Torquato, *Lineal-path function for random heterogeneous materials*, Physical Review A 45 (1992); full primary text was not available for inspection in this review.
4. R. Coleman, *Random paths through convex bodies*, Journal of Applied Probability 6 (1969), 430–441; relevant abstract inspected, full text not inspected.
