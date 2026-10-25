# A universal sharp Bowen-ball volume for nonlinear three-dimensional skew towers

## Finding
Let \(\alpha\in\mathbb R\setminus\mathbb Q\) and let \(\psi:\mathbb R\to\mathbb R\) be any real-valued one-periodic \(C^1\) function. On \(\mathbb T^3\), consider the Haar-preserving homeomorphism
\[
F_{\alpha,\psi}(x,y,z)=(x+\alpha,\ y+x+\psi(x),\ z+y)\pmod1.
\]
With the maximum of the three circular-coordinate distances, let \(B_n(u,\varepsilon)\) be the points that remain within distance \(\varepsilon\) of the first \(n\) iterates of \(u\). Put \(M=\|\psi'\|_\infty\) and \(\varepsilon_0=\min\{1/16,1/[8(1+M)]\}\). For every fixed \(0<\varepsilon<\varepsilon_0\),
\[
\boxed{\lim_{n\to\infty}\ \sup_{u\in\mathbb T^3}\left|n^3\,m_3(B_n(u,\varepsilon))-\frac{544}{9}\varepsilon^3\right|=0.}
\]
More precisely, initial lifted displacements rescaled by \((n^2/\varepsilon,n/\varepsilon,1/\varepsilon)\) converge, in the uniform volume-sandwich sense established below, to the universal convex body
\[
\mathcal K=\left\{(A,B,C)\in\mathbb R^3:\ \max_{0\le t\le1}\left|C+tB+\tfrac12t^2A\right|\le1\right\},\qquad \operatorname{vol}(\mathcal K)=\frac{544}{9}.
\]
The limit is independent of both \(\alpha\) and \(\psi\). In particular it does not require a Diophantine condition or a cohomological solution for \(\psi\). The polynomial orbit-covering exponent is \(3\); its existence is context, while the perturbation-independent sharp measure constant is the new point.

## Assumptions and scope
Here \(\mathbb T=\mathbb R/\mathbb Z\), \(m_3\) is normalized Haar measure and \(d_\infty(u,v)=\max_j\min_{k\in\mathbb Z}|u_j-v_j-k|\). For integers \(n\ge2\),
\[
B_n(u,\varepsilon)=\{v\in\mathbb T^3:d_\infty(F^j u,F^j v)<\varepsilon\text{ for every }0\le j<n\}.
\]
The first coordinate of a displacement is represented initially by a unique real \(h\in(-\varepsilon,\varepsilon)\); the others by \(b,c\in(-\varepsilon,\varepsilon)\). Asymptotics are for fixed \(\varepsilon\) in the displayed interval and \(n\to\infty\), uniformly in the center \(u\). Endpoint sets of the relevant convex bodies have Lebesgue measure zero, so strict or weak inequalities agree for volume purposes.

## Proof
**1. Exact lifted difference formula.** Choose consistent real lifts of both orbits. At the center's initial first coordinate \(x\), define
\[
g_h(s)=\int_0^1\psi'(s+th)\,dt,\quad D_j=h\,g_h(x+j\alpha).
\]
The real lifted differences of the second and third coordinates at time \(j\) are exactly
\[
Y_j=b+jh+h\sum_{r=0}^{j-1}g_h(x+r\alpha),
\]
\[
Z_j=c+jb+\binom j2h+h\sum_{r=0}^{j-2}(j-1-r)g_h(x+r\alpha).
\]
An empty sum is zero. These identities follow by iterating the triangular recurrence and the fundamental theorem of calculus. The first-coordinate difference is always \(h\).

**2. A uniform cancellation lemma.** The continuous function \(g_h\) has mean zero on \(\mathbb T\), since \(\int\psi'=0\). As \(h\) ranges over a compact interval, the functions \(g_h\) form a compact subset of \(C(\mathbb T)\). For irrational rotation and every continuous mean-zero function \(g\), uniform ergodicity gives \(\sup_s|\sum_{r<j}g(s+r\alpha)|/j\to0\). To see this without invoking an unproved quantitative rate, approximate \(g\) by a mean-zero trigonometric polynomial: each nonconstant Fourier mode has bounded geometric sums, and the uniform approximation error contributes at most \(j\eta\). A finite uniform net for the compact family extends this estimate to all \(g_h\). Therefore
\[
E_n:=\frac1n\sup_{|h|\le\varepsilon}\sup_{x\in\mathbb T}\max_{0\le j\le n}\left|\sum_{r<j}g_h(x+r\alpha)\right|\longrightarrow0.
\]
Summation in reverse order yields
\[
\sup_{x,h}\max_{j\le n}\left|\sum_{r=0}^{j-2}(j-1-r)g_h(x+r\alpha)\right|\le n^2E_n.
\]
No bound on Diophantine approximation of \(\alpha\) is needed.

**3. No hidden modular winding.** Suppose \(v\in B_n(u,\varepsilon)\). The real increment \(Y_{j+1}-Y_j=h[1+g_h(x+j\alpha)]\) has size at most \((1+M)\varepsilon<1/8\). Each \(Y_j\) is within \(\varepsilon\) of an integer modulo one, and \(Y_0=b\in(-\varepsilon,\varepsilon)\). Distinct integer neighborhoods are separated by \(1-2\varepsilon>7/8\), so the nearest integer cannot change between observations. Hence \(|Y_j|<\varepsilon\) as a real number for all observed times. Now \(Z_{j+1}-Z_j=Y_j\) has size below \(\varepsilon\), and the same induction from \(Z_0=c\) gives \(|Z_j|<\varepsilon\) in real lifts. Conversely, the three real inequalities are sufficient for Bowen membership. The restriction on \(\varepsilon\) is explicitly used only to guarantee this lifting step.

**4. Sharp anisotropic scaling.** Put \(N=n-1\), \(j_*=\lfloor N/2\rfloor\), and \(t_*=j_*/N\). Apply the linear-interpolation defect to the exact formula:
\[
Z_{j_*}-(1-t_*)Z_0-t_*Z_N
=-\tfrac12j_*(N-j_*)h+hR_N,
\]
where \(|R_N|\le 3n^2E_n\). Its left side has magnitude at most \(2\varepsilon\) on a Bowen ball. Since \(j_*(N-j_*)\sim N^2/4\), it follows uniformly in the center that \(|h|=O(\varepsilon/n^2)\). The difference \(Z_N-Z_0=Nb+\binom N2h+hO(n^2E_n)\) then gives \(|b|=O(\varepsilon/n)\). Of course \(|c|<\varepsilon\). Thus the rescaled variables
\[
A=n^2h/\varepsilon,\qquad B=nb/\varepsilon,\qquad C=c/\varepsilon
\]
lie in one fixed bounded box, uniformly over all centers and sufficiently large \(n\). Conversely every bounded triple with \(h=\varepsilon A/n^2\), \(b=\varepsilon B/n\), \(c=\varepsilon C\) has
\[
\sup_{0\le j<n}\left|\frac{Z_j}{\varepsilon}-\left(C+\frac jnB+\frac{j^2}{2n^2}A\right)\right|\longrightarrow0,
\]
uniformly in the center and in that bounded box. The binomial-to-quadratic error is \(O(|A|/n)\) and the nonlinear error is at most \(|A|E_n\). Simultaneously \(\max_j|Y_j|=O(\varepsilon/n)\), so all lower-coordinate constraints are automatically satisfied in bounded rescaled regions for large \(n\).

**5. Uniform coefficient-body volume limit.** The compact set \(\mathcal K\) has interior and boundary of three-dimensional Lebesgue measure zero because it is a full-dimensional convex body. For any fixed \(\eta>0\), the preceding estimates uniformly sandwich the rescaled Bowen ball between the corresponding strict continuous-polynomial constraint bodies \(\max_t|C+tB+A t^2/2|<1-\eta\) and \(\le1+\eta\), with the same bounded ambient box for all centers. The discrete observation times form an asymptotically dense grid in \([0,1]\). Letting \(n\to\infty\) and then \(\eta\downarrow0\) proves uniform convergence of the rescaled volumes to \(\operatorname{vol}(\mathcal K)\). The coordinate Jacobian is exactly \(\varepsilon^3/n^3\). This establishes the asserted volume limit.

**6. Exact limiting volume.** For \(p(t)=C+Bt+(A/2)t^2\), write the same polynomial as \(p(t)=u(1-t)+vt+wt(1-t)\). Here \(u=p(0)\), \(v=p(1)\), and the absolute coefficient Jacobian from \((u,v,w)\) to \((C,B,A/2)\) equals one. At \(|u|,|v|\le1\), the allowed curvature interval is
\[
-\left(\sqrt{1+u}+\sqrt{1+v}\right)^2\le w\le\left(\sqrt{1-u}+\sqrt{1-v}\right)^2.
\]
For example the upper inequality follows by minimizing \((1-u)/t+(1-v)/(1-t)\) over \(0<t<1\). Integrating its length over \((u,v)\in[-1,1]^2\) yields coefficient volume \(16+4(4\sqrt2/3)^2=272/9\). Because \(A=2(A/2)\), the absolute Jacobian to \((A,B,C)\) is two; hence \(\operatorname{vol}(\mathcal K)=544/9\). This coefficient-body evaluation is already known for the unperturbed Jordan map and is reused here; the novel assertion is its persistence under arbitrary periodic \(C^1\) skewing.

**7. Polynomial covering exponent.** The volume limit gives a lower bound of order \(n^3\) for the number of Bowen balls needed to cover the torus. Conversely, for a fixed sufficiently small accuracy, a coordinate grid with mesh \(O(n^{-2})\), \(O(n^{-1})\), and \(O(1)\) in the respective coordinates keeps all differences small for \(n\) iterates by the elementary Lipschitz bound on \(\psi\) and the exact triangular formulas. It has \(O(n^3)\) points. Thus the polynomial orbit-covering exponent is \(3\), as expected from the nilpotent shear structure.

## Verification
The standalone standard-library `verify.py` checks the exact curvature-volume integral algebra, the unperturbed binomial orbit identities with rational arithmetic, and the nonlinear lifted-difference identity for several deterministic trigonometric perturbations. It also compares finite-time rescaled Bowen membership against the limiting polynomial body's membership away from its boundary. These are finite checks only: the infinite, center-uniform limit rests on the compact-family unique-ergodicity argument and the three-point interpolation estimate in the proof. Run with `python3 verify.py`.

## Relationship to prior work
Polo's 2010 work proves equidistribution and ergodic properties for broad iterated toral skew products, including those with nontrivial circle-fiber degrees; it does not state an asymptotic Haar volume of Bowen balls. Cantat and Paris-Romaskevich (2020), Lemma 4.4, establish the polynomial entropy exponent of unipotent Jordan maps from orbit-covering arguments, not a sharp local Haar coefficient under nonlinear forcing. Two other published results supply complementary boundary cases: *Sharp Haar Bowen-ball constants for unipotent Jordan toral dynamics* establishes the precise \(544/9\) constant in three dimensions for the linear Jordan map (no nonlinear skew), and *Universal Bowen-ball volume law for irrational skew Dehn twists* establishes perturbation-independence for the two-dimensional one-step skew map (not the quadratic-time three-dimensional tower). Neither statement, even under a change of notation, contains all the assumptions and conclusion here. The present proof establishes the missing nonlinear three-dimensional combination using weighted uniform cancellation and a second-difference rigidity estimate; it does not claim that the previously computed coefficient-body volume is itself original.

## Limitations
The theorem requires an irrational base and \(C^1\) periodic perturbation; it gives no universal convergence rate and does not address arbitrary continuous skewing, general nonlinear dependence on the second fiber, or general compatible metrics. The explicit small-radius bound is sufficient, not claimed optimal. The limiting volume depends on the specified product max metric. The polynomial entropy exponent and the unperturbed coefficient \(544/9\) were known, and historical priority for this combined robustness statement remains subject to independent confirmation.

## References
1. F. Polo, *Equidistribution of singular measures on nilmanifolds and skew products*, arXiv:1003.3112v1, publicly submitted 2010-03-16; especially Theorems 1.4 and 1.7, https://arxiv.org/abs/1003.3112.
2. S. Cantat and O. Paris-Romaskevich, *Automorphisms of compact Kähler manifolds with slow dynamics*, arXiv:2002.03615, 2020; particularly Lemma 4.4, https://arxiv.org/abs/2002.03615.
3. *Sharp Haar Bowen-ball constants for unipotent Jordan toral dynamics*, publicly indexed 2026-10-11, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-sharp-haar-bowen-ball-constants-for-unipotent-jordan-toral-dynam--ab1c4e92842d.
4. *Universal Bowen-ball volume law for irrational skew Dehn twists*, publicly indexed 2026-10-11, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-universal-bowen-ball-volume-law-for-irrational-skew-dehn-twists--9c651d44a4c2.
