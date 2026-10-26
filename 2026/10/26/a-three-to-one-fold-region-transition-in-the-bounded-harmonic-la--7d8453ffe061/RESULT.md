# A three-to-one fold-region transition in the bounded harmonic Landau shear

## Finding

For \(M>1\), put
\[
 u(z)=\frac{2}{\pi}\operatorname{Arg}\left(\frac{1-z^2}{1+z^2}\right),\qquad
 F_M(z)=z+i(M-1)u(z),\qquad z\in\mathbb D.
\]
The argument takes values in \((-\pi/2,\pi/2)\). Let \(J_M=\det DF_M\) be the real Jacobian and let the orientation-reversing region be
\[
 \mathcal N_M=\{z\in\mathbb D:J_M(z)<0\}.
\]
Set
\[
 M_{\mathrm{fold}}=1+\frac{\pi\sqrt2}{2\,3^{3/4}}
 =1.974527129583\ldots.
\]
Then the **number of connected components** has the sharp classification
\[
 \boxed{\#\pi_0(\mathcal N_M)=
 \begin{cases}3,&1<M\le M_{\mathrm{fold}},\\
 1,&M>M_{\mathrm{fold}}.\end{cases}}
\]
In the three-component phase, the components approach respectively the boundary points \(1\), \(i\), and \(-i\); after merging, the single component approaches all three. At the transition, the Jacobian-zero curve has exactly two interior nondegenerate critical crossings, at
\[
 z=3^{-1/4}e^{i\pi/4}\quad\text{and}\quad
 z=3^{-1/4}e^{-i\pi/4}.
\]
This statement concerns the topology of the **entire** negative-Jacobian region, not just the first Jacobian zero or the number of preimages of a selected target.

## Assumptions and scope

The domain is the open unit disk \(\mathbb D=\{z\in\mathbb C:|z|<1\}\), with Euclidean orientation and the real Jacobian. The parameter satisfies \(M>1\). The real harmonic function \(u\) is well-defined because \((1-z^2)/(1+z^2)\) has positive real part for \(|z|<1\). All connected components are taken within the **open** unit disk, and the inequalities defining \(\mathcal N_M\) are strict. In particular, the equality parameter belongs to the three-component phase. The original boundedness \(|F_M|<M\) and normalization at zero belong to the motivating construction; no global univalence conclusion is claimed here.

## Proof

**1. Exact Jacobian and reduction to a harmonic superlevel set.** Differentiating the analytic logarithm gives
\[
 \partial_y u(z)=-\frac8\pi\operatorname{Re}\frac{z}{1-z^4}.
\]
Since \(F_M(x+iy)=x+i(y+(M-1)u(x+iy))\),
\[
 J_M(z)=1-\frac{8(M-1)}\pi U(z),\qquad
 U(z)=\operatorname{Re}\frac{z}{1-z^4}.
\]
Thus \(\mathcal N_M=\{U>k\}\), where \(k=\pi/[8(M-1)]>0\). For \(z=x+iy\), direct multiplication yields
\[
 U(x+iy)=\frac{x(1-x^4+2x^2y^2+3y^4)}{|1-z^4|^2}.
\]
The parenthesized factor is positive in \(\mathbb D\); hence \(U>0\) precisely in the right half disk.

**2. Candidate transition and separating rays.** The derivative of \(H(z)=z/(1-z^4)\) is
\[
 H'(z)=\frac{1+3z^4}{(1-z^4)^2}.
\]
Its four simple critical points satisfy \(z^4=-1/3\). The two lying in the right half disk are
\(z_\pm=a e^{\pm i\pi/4}\), where \(a=3^{-1/4}\). At these points
\[
 U(z_\pm)=k_*=\frac{3a}{4\sqrt2}
 =\frac{3^{3/4}}{4\sqrt2}.
\]
On each separating ray we have, for \(0<r<1\),
\[
 U(re^{\pm i\pi/4})=\frac{r}{\sqrt2(1+r^4)}\le k_*;
\]
the maximum occurs uniquely at \(r=a\). Therefore, when \(k\ge k_*\), the superlevel set \(\{U>k\}\) cannot cross either ray. It lies in three disjoint angular sectors:
\[
 -\pi/4<\arg z<\pi/4,\quad
 \pi/4<\arg z<\pi/2,\quad
 -\pi/2<\arg z<-\pi/4.
\]

**3. Exactly one component per sector for \(k\ge k_*\).** On the smooth part of the unit circle, away from the four poles, one has the exact boundary identity
\[
 U(e^{i\theta})=\frac1{4\cos\theta}.
\]
The boundary values in the central sector are bounded above by \(\sqrt2/4<k_*\); hence a component in that sector can reach the unit circle only at the pole \(1\). In the upper sector, the points with boundary value greater than \(k\) form exactly the connected arc
\[
 \arccos(1/(4k))<\theta<\pi/2,
\]
ending at the pole \(i\); the lower sector has the conjugate arc ending at \(-i\). The superlevel set has exactly one connected local tongue near each of the three poles: this follows either by expanding \(H\) at the simple poles or by using the half-plane coordinate \(w=(1-\overline p z)^{-1}\), in which the leading real part is a nonzero linear form in \(w\). In each case the local positive half-plane intersection is connected.

Every nonempty component of a harmonic superlevel set must accumulate at the unit-circle boundary: an entirely relatively compact component would contradict the maximum principle. At a smooth boundary point with \(U=k\), the boundary expression above has nonzero tangential derivative unless the point is a pole; thus such an accumulation leads to the neighboring open arc with \(U>k\). Since each sector has just one relevant boundary arc or pole tongue, every component in that sector joins its unique boundary tongue. Each of the three tongues is nonempty (\(U\) tends to \(+\infty\) there along an appropriate interior approach). Consequently there is exactly one component per sector, hence three in total. The argument includes \(k=k_*\), because the separating rays themselves are excluded by the strict inequality.

**4. A connecting core for \(0<k<k_*\).** On the circle \(|z|=a\) write \(t=\sqrt2\cos\theta\). Algebraic simplification gives the exact identity
\[
 U(ae^{i\theta})-k_*
 =k_*\frac{(t-1)^2(3t^2+4t-1)}{1+6t^2-3t^4}.
\]
For \(|\theta|\le\pi/3\) we have \(t\in[1/\sqrt2,\sqrt2]\); both the quadratic factor and denominator are positive. Hence the entire circle arc \(\{|z|=a,\ |\arg z|\le\pi/3\}\) lies in \(\{U>k\}\).

The real radial segment from \(a\) to \(1\) also lies in \(\{U>k\}\), since \(U(r)=r/(1-r^4)\) is increasing and \(U(a)>k_*\). On either ray \(\arg z=\pm\pi/3\) we have
\[
 U(re^{i\pi/3})=\frac{r(1/2+r^4)}{1+r^4+r^8}.
\]
On \(a\le r\le1\), its derivative has the sign opposite to \(6r^{12}+5r^8-7r^4-1\). As a polynomial in \(r^4\), this has exactly one zero in \([1/3,1]\): its derivative \(18t^2+10t-7\) changes sign once from negative to positive, while the cubic itself is negative at \(1/3\) and positive at \(1\). Therefore the radial function has only an interior maximum. Its minimum occurs at an endpoint: the first is strictly above \(k_*\) by the circle identity, and the second equals \(1/2>k_*\). Thus these two radial segments also lie in \(\{U>k\}\).

Finally, the unit-circle arcs from \(\theta=\pm\pi/3\) toward \(\pm\pi/2\) have boundary values at least \(1/2>k_*\), so narrow interior collars connect the above core to the tongues approaching \(\pm i\). The central radial segment already reaches the tongue approaching \(1\). All three pole tongues therefore lie in the same component of \(\{U>k\}\).

Any other component would have to accumulate at a regular boundary arc where \(U\ge k\), or at one of the three poles (maximum principle). Every regular boundary arc with \(U>k\) lies in one of the two arcs meeting the already connected collars: for \(k>1/4\) these arcs start at \(\pm\arccos(1/(4k))\), while for \(k\le1/4\) the whole right semicircular boundary has \(U\ge k\). The transverse level crossings at regular boundary points and the one-tongue local pole structure show that no separate component can accumulate there. Hence \(\{U>k\}\) is connected for every \(0<k<k_*\).

**5. Parameter and crossing classification.** The relation \(k=\pi/[8(M-1)]\) gives \(k\ge k_*\) precisely when
\[
 M\le1+\frac\pi{8k_*}
 =1+\frac{\pi\sqrt2}{2\,3^{3/4}}.
\]
Finally, \(H''(z_\pm)=\frac{27}{4}z_\pm^3\ne0\), so each is a nondegenerate harmonic saddle of \(U\). The two saddles share the same level \(k_*\), producing the two simultaneous critical crossings claimed. No other interior critical point has positive \(U\)-value. This proves the theorem.

## Verification

The embedded `CHECK.py` verifies by exact rational polynomial arithmetic the circle-arc factorization and radial derivative numerator, checks the critical-value identity at high precision, and performs independent numerical spot checks of the Jacobian relation. Run `python3 CHECK.py` to reproduce these identity checks. They do not replace the maximum-principle and connectedness arguments above. The exact connected-component classification is established analytically.

## Relationship to prior work

Borovikov's September 2026 counterexample introduces precisely the harmonic shear \(F_M\), determines its real-axis Jacobian-zero radius, and uses it to disprove a proposed harmonic Landau radius. Those facts are prior work. Earlier indexed results additionally determine the exact centered univalence radius and a distinct three-to-five **real-target valence** threshold; neither assertion supplies the number of components of the **global orientation-reversing region** for all \(M>1\). The new statement isolates the two simultaneous saddle reconnections and their independent exact parameter.

## Limitations

Only the explicit one-parameter harmonic shear is classified. The theorem does not determine the full caustic image, count preimages of arbitrary complex target points, optimize the Landau radius, or assert stability of the symmetric double transition under perturbations. The component count uses the open disk and strict negative-Jacobian set; changing either convention can change topological boundary statements. Historical priority remains subject to work not present in accessible indices.

## References

- M. Borovikov, *A Counterexample to the Liu–Luo–Luo Conjecture on the Harmonic Landau Radius*, arXiv:2609.39676v1, first public 2026-09-30, in particular Section 2 and equations (5)–(13).
- published-finding corpus, *Exact centered univalence radius of the Borovikov shear*, record `2026/10/11/SCOPE-exact-centered-univalence-radius-of-the-borovikov-shear--16de77633d7a` (statement-level comparison).
- published-finding corpus, *Exact three-to-five real-fiber valence transition in a harmonic Landau shear*, record `2026/10/11/SCOPE-exact-three-to-five-real-fiber-valence-transition-in-a-harmonic--c0d4ae0d2148` (statement-level comparison).
- published-finding corpus, *Sharp transverse derivative and optimality of the harmonic Landau shear*, record `2026/10/11/SCOPE-sharp-transverse-derivative-and-optimality-of-the-harmonic-landa--f86aa34f1bf1` (statement-level comparison).
