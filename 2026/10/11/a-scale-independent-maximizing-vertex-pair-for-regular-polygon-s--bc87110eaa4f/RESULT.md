# A scale-independent maximizing vertex pair for regular-polygon smoothness moduli
## Finding
For each integer \(n\ge2\), let \(X_n\) be the real normed plane whose unit ball is the regular Euclidean \(2n\)-gon with vertices
\[
v_j=\bigl(\cos(j\pi/n),\sin(j\pi/n)\bigr),\qquad 0\le j<2n.
\]
Write \(\beta_n=\pi/(2n)\), and put \(q_j=1\) if \(j\) is even and \(q_j=\sec\beta_n\) if \(j\) is odd. For every real \(t\ge0\), its classical modulus of smoothness is exactly
\[
\rho_{X_n}(t)=\max_{0\le j\le n}
\left[q_j\cos(j\beta_n)+tq_{n-j}\sin(j\beta_n)\right]-1.
\]
Moreover, the same two unit vertices
\[
x=v_0,\qquad y=v_{\lfloor n/2\rfloor}
\]
attain the defining supremum for every \(t\ge0\); the maximizing pair need not change when the active affine branch changes. In particular, for the regular decagonal plane \(X_5\), let
\[
\varphi=\frac{1+\sqrt5}{2},\quad
s=\frac{\sqrt5-1}{4},\quad
a=\frac{1+\sqrt5}{4},\quad
b=\frac{\sqrt5-1}{2}.
\]
Then its complete scale profile is the sharp four-phase law
\[
\rho_{X_5}(t)=
\begin{cases}
s t,&0\le t\le\varphi^{-1},\\
a+b t-1,&\varphi^{-1}\le t\le1,\\
b+a t-1,&1\le t\le\varphi,\\
t+s-1,&t\ge\varphi.
\end{cases}
\]
In particular \(\rho_{X_5}(1)=(3\sqrt5-5)/4\), and the fixed pair \((v_0,v_2)\) attains the entire decagonal profile. This statement asserts existence of a universal maximizing vertex pair, not uniqueness or a complete classification of all maximizers.

## Assumptions and scope
All spaces are real and two-dimensional. For each integer \(n\ge2\), let \(B_n\) be the convex hull of \(2n\) Euclidean unit vectors
\[
v_j=\left(\cos(j\pi/n),\sin(j\pi/n)\right),\quad 0\le j<2n.
\]
The norm \(N_n\) is the Minkowski gauge of \(B_n\), so \(N_n(v_j)=1\). The classical (Day) modulus is
\[
\rho_{X_n}(t)=\sup_{N_n(x)=N_n(y)=1}
\left\{\frac{N_n(x+ty)+N_n(x-ty)}2-1\right\},\qquad t\ge0.
\]
This differs from angle-restricted smoothness moduli and supporting-functional-diameter invariants. Indices on polygon vertices are taken modulo \(2n\). The theorem concerns exact global maxima, not local or infinitesimal maxima alone.

## Proof
**1. Dual reduction for the entire modulus.** Set \(\beta=\pi/(2n)\) and define the polar vertices
\[
w_j=\sec\beta\left(\cos((2j+1)\beta),\sin((2j+1)\beta)\right),\qquad 0\le j<2n.
\]
The polar ball is \(B_n^*=\operatorname{conv}\{w_j\}\), and for all \(z\in\mathbb R^2\),
\[
N_n(z)=\max_{0\le j<2n}\langle w_j,z\rangle.
\]
The function \((x,y)\mapsto N_n(x+ty)+N_n(x-ty)\) is convex in each input. Consequently its maximum on \(B_n\times B_n\) is attained at a pair of extreme points, which are unit vectors; hence replacing the two spheres by the two balls does not change the maximum. Independent maximization over the two polar support vectors then gives the exact identity
\[
1+\rho_{X_n}(t)=\frac12
\max_{f,g\in B_n^*}
\left(N_n^*(f+g)+tN_n^*(f-g)\right).
\tag{1}
\]
The expression in parentheses is convex in \(f\) and separately convex in \(g\). Thus a maximizing dual pair can be chosen among the polar vertices. Dihedral symmetry and interchanging and negating the second vertex reduce all pairs to \((w_0,w_k)\) with \(0\le k\le n\). Since
\[
B_n^*=\sec\beta\,R_\beta B_n
\]
where \(R_\beta\) is Euclidean rotation by \(\beta\), this linear map is an isometry from \((\mathbb R^2,N_n)\) to \((\mathbb R^2,N_n^*)\). Therefore
\[
N_n^*(w_0\pm w_k)=N_n(v_0\pm v_k).
\tag{2}
\]

**2. Exact polar chord norms.** For an integer \(k\) with \(0\le k\le n\), put \(q_k=1\) for even \(k\), and \(q_k=\sec\beta\) for odd \(k\). The chord identities are
\[
v_0+v_k=2\cos(k\beta)\bigl(\cos(k\beta),\sin(k\beta)\bigr),
\]
\[
v_0-v_k=2\sin(k\beta)
\bigl(\sin(k\beta),-\cos(k\beta)\bigr).
\]
A Euclidean unit ray at angle an even multiple of \(\beta\) meets \(B_n\) at a vertex, and has \(N_n\)-norm one. A ray at an odd multiple of \(\beta\) meets the midpoint of a side at radius \(\cos\beta\), and has \(N_n\)-norm \(\sec\beta\). Therefore
\[
N_n(v_0+v_k)=2q_k\cos(k\beta),\qquad
N_n(v_0-v_k)=2q_{n-k}\sin(k\beta).
\tag{3}
\]
Substituting (2)--(3) into (1) proves the finite exact affine-envelope formula in the claim for every \(t\ge0\).

**3. A fixed maximizing pair works at all scales.** Take any vertex pair \((w_j,w_k)\) that maximizes (1). Both polar vertices have the same Euclidean length. Consequently the vectors \(w_j+w_k\) and \(w_j-w_k\), whenever nonzero, are Euclidean perpendicular. The polar vectors have angles that are integer odd multiples of \(\beta\), so the two perpendicular supporting directions have angles differing by \(n\beta=\pi/2\), and each is an integer multiple of \(\beta\).

The supporting vertices of the primal regular polygon are those closest in Euclidean angle to these directions. If \(n\) is even, both directions have the same parity as multiples of \(\beta\): either both are vertex rays or both are side-midpoint rays. In the latter case, choose corresponding nearest endpoints of the two sides. This produces vertex indices separated by exactly \(n/2\). If \(n\) is odd, one direction is a vertex ray and the other a side-midpoint ray; choose the endpoint of that side at an angular index separation of \((n-1)/2\), possibly negating a vector. Thus in either parity there exist primal maximizing vertices \((x,y)\) whose angular separation, up to an independent sign change, is
\[
\frac{\lfloor n/2\rfloor\pi}{n}.
\]
The dihedral symmetries of \(B_n\) act transitively on these pairs, while changing the sign of \(y\) only exchanges \(N_n(x+ty)\) and \(N_n(x-ty)\). Therefore \((v_0,v_{\lfloor n/2\rfloor})\) attains (1) for each \(t\ge0\). If one of the two perpendicular vectors vanishes, its primal supporting vertex may be chosen arbitrarily, and the same conclusion follows. This gives existence at every scale without imposing uniqueness.

**4. The regular decagon and its phase boundaries.** For \(n=5\), let \(\varphi=(1+\sqrt5)/2\), \(s=(\sqrt5-1)/4\), \(a=(1+\sqrt5)/4\) and \(b=(\sqrt5-1)/2\). The six affine expressions inside the maximum in the exact formula, corresponding to \(k=0,1,2,3,4,5\), are
\[
1,\quad 1+s t,\quad a+b t,\quad b+a t,\quad s+t,\quad t.
\]
For positive \(t\), the first is dominated by the second and the last by the penultimate. The remaining four lines have strictly decreasing intercepts and strictly increasing slopes, with successive intersections exactly at
\[
\frac{1-a}{b-s}=\varphi^{-1},\qquad
\frac{a-b}{a-b}=1,\qquad
\frac{b-s}{1-a}=\varphi.
\]
These intersections increase strictly, so all four lines appear consecutively on their upper envelope. Subtracting one gives the stated four-phase formula, including equality at the junctions. The fixed maximizing pair is \((v_0,v_2)\), and substitution at \(t=1\) gives \(\rho_{X_5}(1)=(3\sqrt5-5)/4\).

## Verification
The proof establishes a genuine all-scale, all-polygon identity, not just a finite numerical maximization. Its independently checkable components are the polar polygon identity, the convexity-based extreme point reduction, the two regular-polygon chord norms, the perpendicular-support geometry, and the exact golden-ratio line intersections.

For a finite numerical sanity check only, one may construct \(v_k,w_k\) as above for any fixed \(n\), evaluate
\[
N_n(z)=\max_j\langle w_j,z\rangle
\]
and compare all \(2n\) values
\[
\frac{N_n(v_0+t v_k)+N_n(v_0-t v_k)}2-1
\]
against the closed formula. Sampling \(2\le n\le17\) across fourteen positive scales and all vertex indices matched both the formula and the fixed-pair prediction to floating-point tolerance. The sampling is a cross-check only; the complete proof is the analytic reduction above. The exact decagonal intersection identities were also checked symbolically in the quadratic field \(\mathbb Q(\sqrt5)\).

## Relationship to prior work
Guirao, Ivanov and Lajara (2010) study which asymptotic equivalence classes of classical smoothness moduli can arise and construct examples through Orlicz spaces. Their complete paper discusses neither the regular \(2n\)-gon nor its exact finite-scale affine envelope.

Ivanov (2015) explicitly recalls the same classical modulus and studies newly defined supporting moduli and equivalence at zero. The complete preprint supplies background and inequalities but no all-scale formula for regular polygons.

Chmieliński, Khurana and Sain (2023) calculate the norming-functional diameter \(\mathcal E(X_n)\) of the same regular \(2n\)-gonal planes, including explicit polar vertices. That result implies the right-hand derivative of the classical modulus at zero, which is **not** claimed as new. Their Section 4 does not compute the entire \(t\)-dependent classical modulus or establish one fixed pair attaining it for every \(t\).

Banaś, Ochab and Zając (2024) survey classical smoothness and a different midpoint-deficit modulus, discussing general inequalities and continuity, but give no regular-polygon all-scale computation. The present uniform dual-vertex reduction and the golden-ratio phase diagram are not special cases of those displayed results.

## Limitations
The theorem is limited to centered regular even polygons as unit balls in real dimension two. It does not classify *all* maximizing pairs: at phase boundaries and at \(t=0\) there may be many maximizers. No quantitative near-extremizer stability or closed interval-by-interval expression for each general \(n\) is claimed beyond the finite maximum formula.

The 2010 archival comparison is securely dated by publication year, but the consulted full-text record exposes no day-resolved first-public date. The first verified day-level publication among the inspected archive-period anchoring records is the 2015-03-30 article record, used in the associated metadata rather than assigning a fabricated day to the 2010 source.

## References
1. A. J. Guirao, M. Ivanov, and S. Lajara, “On Moduli of Smoothness and Squareness,” *Journal of Convex Analysis* 17 (2010), 441--449, DOI 10.68381/jca17031; year-resolved public source.
2. G. M. Ivanov, “Modulus of Supporting Convexity and Supporting Smoothness,” *Eurasian Mathematical Journal* 6 (2015), 26--40; article-record public date 2015-03-30; arXiv:1503.08912 (first arXiv submission 2015-03-31).
3. J. Chmieliński, D. Khurana, and D. Sain, “Approximate smoothness in normed linear spaces,” *Banach Journal of Mathematical Analysis* 17 (2023), article 41, DOI 10.1007/s43037-023-00263-4, online 2023-04-27.
4. J. Banaś, J. Ochab, and T. Zając, “On the smoothness of normed spaces,” *Annals of Functional Analysis* 15 (2024), article 9, DOI 10.1007/s43034-023-00310-z, online 2023-12-16.
