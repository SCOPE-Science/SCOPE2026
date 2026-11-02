# Exact three-colour rotating-wave cutoff and an attracting weak-coupling cycle in a Chebyshev ring

## Finding
Consider the cyclic three-site quadratic Chebyshev lattice
\[
F_a(x)_i=(1-a)(2x_i^2-1)+\frac a2(x_{i-1}+x_{i+1}),\qquad 0\le a<1,
\]
with indices modulo three. Put \(P(x_0,x_1,x_2)=(x_2,x_0,x_1)\). A *three-colour rotating wave* is a real vector with pairwise distinct coordinates satisfying \(F_a(x)=Px\); its temporal least period is three.

Define \(a_{\rm fold}=1-\sqrt{6/7}\). There are exactly six such real vectors for \(0\le a<a_{\rm fold}\), exactly three at \(a=a_{\rm fold}\), and none for \(a_{\rm fold}<a<1\). Their two (respectively one) phase-orbit coordinate sums are
\[
S_\pm(a)=-\frac14\pm\frac{\sqrt{7a^2-14a+1}}{4(1-a)}.
\]
In particular the upper-sum wave at the **exact rational coupling** \(a=7/100\) has all coordinates in \((-1,1)\) and is locally exponentially attracting under the full three-dimensional dynamics. The classification is of real rotating waves; stability for every coupling in the existence interval is not asserted.

## Assumptions and scope
All coordinates and parameters are real. The map is a polynomial on \(\mathbb R^3\), although the physically natural invariant state space is \([-1,1]^3\), which is forward invariant for \(0\le a\le1\). The census concerns only rotating-wave states with three different site values and the chosen spatial orientation \(P\). The existence of the attracting wave is explicitly certified inside \((-1,1)^3\). The opposite spatial orientation is not included; it is not automatically realized by reversing a rotating-wave orbit.

## Proof
Write \(S=x_0+x_1+x_2\). The rotating-wave equation reduces componentwise to iteration of one scalar quadratic
\[
q_{a,S}(w)=2(1-a)w^2-\frac a2w-(1-a)+\frac a2S.
\]
Indeed the cyclically ordered coordinates must form a genuine scalar period-three orbit of this same quadratic. With \(A=2(1-a)\) and \(u=Aw-a/4\), it is affinely conjugate to \(u\mapsto u^2+c\), where
\[
c=A\bigl(aS/2-(1-a)\bigr)-a/4-a^2/16,
\qquad s=AS-3a/4.
\]
For a real parameter \(s\), define
\[
R_s(u)=u^3-su^2-(s^2+2s+3)u+s^3+2s^2+3s+1.
\]
Direct polynomial division gives the period-three dynatomic factorization: whenever \(c=-s^2-s-2\),
\[
\frac{(u\mapsto u^2+c)^{\circ3}(u)-u}{u^2+c-u}
=R_s(u)R_{-1-s}(u).
\]
The discriminant and the resultant with the fixed-point polynomial are, respectively,
\[
\operatorname{disc}(R_s)=(4s^2+6s+9)^2>0,
\quad \operatorname{Res}(R_s,u^2-u+c)=4s^2+6s+9>0.
\]
Thus \(R_s\) always has three distinct real roots forming one genuine scalar period-three orbit, and their sum is \(s\). Conversely every real scalar period-three orbit lies in one of these cubic factors, and its sum satisfies \(s^2+s+c+2=0\). Substituting the definitions of \(s,c\) gives
\[
\bigl(2(1-a)S-3a/4\bigr)^2+\bigl(2(1-a)S-3a/4\bigr)+c+2=0,
\]
whose two solutions are exactly \(S_\pm\). Its discriminant is \(7a^2-14a+1\), nonnegative on \([0,1)\) precisely for \(a\le a_{\rm fold}\). For each distinct root \(S_\pm\), the three roots of the corresponding cubic, transformed back by \(w=(u+a/4)/A\), furnish three cyclic placements and no others. At discriminant zero the two cubic orbits coincide, leaving three placements. This proves the complete count and sharp cutoff.

For attraction, take \(a=7/100\), the larger-sum branch, and let
\[
S_0=-\frac14+\frac{\sqrt{543}}{372}.
\]
The three site values are the three real roots obtained from \(R_{2(1-a)S_0-3a/4}\) by \(w=(u+a/4)/[2(1-a)]\). Exact sign tests put these roots, one each, in \((-1,-9/10)\), \((0,1/10)\), and \((7/10,4/5)\). All belong to the invariant cube. Cyclically ordering the roots according to the scalar iteration produces \(F_a(x)=Px\).

Let \(J=DF_a(x)\), with diagonal entries \(4(1-a)x_i\) and off-diagonal entries \(a/2\). The moving-frame Jacobian is \(B=P^{-1}J\). Cyclic equivariance \(F_a(Px)=PF_a(x)\) implies the three-step monodromy is \(B^3\). The characteristic polynomial of \(B\) is \(z^3+c_2z^2+c_1z+c_0\); at the stated coupling its coefficients are **exactly**
\[
\begin{split}
c_2&=-21/200,\\
c_1&=1449/40000-7\sqrt{543}/20000,\\
c_0&=-440363/500000+282221\sqrt{543}/4000000.
\end{split}
\]
For a real monic cubic, all zeros lie in the open unit disk precisely when \(|c_0|<1\), \(1+c_2+c_1+c_0>0\), \(1-c_2+c_1-c_0>0\), and \(1-c_1+c_2c_0-c_0^2>0\). Each strict inequality here follows by rational arithmetic from \(23302/1000<\sqrt{543}<23303/1000\), whose endpoint squares strictly enclose 543. Hence \(B\) and thus the three-step derivative have spectral radius less than one. The rotating wave is locally exponentially attracting by the discrete hyperbolic sink theorem. Strictness also implies attraction persists for all nearby admissible couplings.

## Verification
Run `python verification.py` with Python 3.10 or newer and SymPy installed. It checks the exact dynatomic division, discriminant, fixed-point exclusion, two sum branches, moving-frame characteristic coefficients, three disjoint rational root enclosures, and all strict Schur inequalities using rational enclosures of \(\sqrt{543}\). No finite sampling is used to establish the parameter-wide real-wave census; that part follows from the polynomial identities. The numerical root approximations are \((-0.9364366,0.0218005,0.7272768)\), ordered to satisfy the chosen cyclic shift.

## Relationship to prior work
Lippolis (2025, subsequently revised) defines this nearest-neighbour Chebyshev lattice and analyzes spatially homogeneous synchronized fixed points and temporal period-two synchronized states. The present result concerns spatially nonconstant period-three rotating waves, and proves their exact algebraic cutoff and one stable weak-coupling instance. Sotelo Herrera and San Martín (2008) established perturbative traveling-wave persistence for a distinct coupling scheme in which neighbouring mapped outputs, rather than neighbouring state values, are averaged; that existence theorem neither yields the present finite-parameter census nor the stated exact stability certificate. Shimada and Kikuchi (2000) studied period-three clusters in a globally coupled map system, also with a different coupling. These antecedents motivate but do not imply the precise statements above; historical priority beyond inspected material remains a limitation.

## Limitations
Only three sites, the specified local quadratic polynomial, nonnegative coupling below one, and rotating waves with spatial shift \(P\) are classified. The counts are over real vectors, not an all-parameter proof that every counted branch lies in the physical invariant cube. Exponential attraction is proved at the exact rational coupling and locally nearby, not on the full existence range. No global basin, opposite-orientation wave classification, or larger-ring extension is claimed. The 2000 global-coupling paper was compared through its accessible abstract; a complete-text priority inspection remains desirable.

## References
D. Lippolis, *Spatiotemporal stability of synchronized coupled map lattice states*, arXiv:2510.12532 (first submitted 14 October 2025); subsequently *Physica D*, DOI 10.1016/j.physd.2026.135148. Primary open full text: https://arxiv.org/html/2510.12532.

M. D. Sotelo Herrera and J. San Martín, *An Analytical Study in Coupled Map Lattices of Synchronized States and Travelling Waves, and of their Period-Doubling Cascades*, arXiv:0802.1700v2 (2008), https://arxiv.org/pdf/0802.1700.

T. Shimada and K. Kikuchi, *Periodicity manifestations in the turbulent regime of the globally coupled map lattice*, *Physical Review E* **62** (2000), 3489–3503, DOI 10.1103/PhysRevE.62.3489.
