# A neutral coexistence segment and sharp stability exchange in a symmetric fear-dependent food web

## Finding

For the exchange-symmetric, positive-parameter subfamily of the Cao–Wang–Liu two-prey–one-predator model (equation (1.7) of [1]), the predator-positive phase has an exact stability-exchange threshold. Assume \(A>b>0\), and define
\[
\sigma=\frac{\delta}{c},\quad y_c=\frac{A/b-1}{k},\quad
 g_0=h+\frac{(A+b)\sigma}{2},\quad
 g_1=h+A\sigma,\quad
 g_c=(1+k y_c)(h+p y_c+b\sigma).
\]
Then \(g_0<g_1<g_c\). For \(g>g_0\) there is exactly one strictly positive symmetric equilibrium \(E_s\). It is locally asymptotically stable for \(g_0<g<g_c\) and a hyperbolic saddle of unstable dimension one for \(g>g_c\). For \(g>g_1\) there are two predator-positive single-prey equilibria \(E_u,E_v\); both are saddles for \(g_1<g<g_c\) and locally asymptotically stable for \(g>g_c\). At \(g=g_c\), the **entire segment**
\[
\mathcal L=\{(u,v,y_c):u\ge0,\ v\ge0,\ u+v=\sigma\}
\]
consists of equilibria: every point has one simple neutral eigenvalue tangent to the segment and two eigenvalues with strictly negative real part, uniformly over the segment. There are no asymmetric strictly positive equilibria away from \(g=g_c\). Thus a unique attracting coexistence equilibrium gives way to two attracting exclusion equilibria through a normally attracting neutral composition segment, rather than through an isolated pitchfork. Here “attracting” is a **local spectral/normal-stability** statement, not global convergence.

## Assumptions and scope

The precise deterministic equations on the nonnegative octant are
\[
\begin{aligned}
 \dot u&=u\left(\frac{g-Au}{1+ky}-bv-h-py\right),\\
 \dot v&=v\left(\frac{g-Av}{1+ky}-bu-h-py\right),\\
 \dot y&=y\bigl(c(u+v)-\delta\bigr),
\end{aligned}
\]
with all eight real parameters \(g,A,b,k,h,p,c,\delta\) positive and \(A>b\). This is an exchange-symmetric coefficient slice of [1, equation (1.7)], obtained by setting its two prey growth coefficients to \(g\), its within-prey competition coefficients \(A_2/K_1\) and \(B_2/K_2\) to \(A\), its cross-prey competition coefficients to \(b\), its fear coefficients to \(k\), its harvest coefficients to \(h\), its direct predation coefficients to \(p\), its predator conversion coefficients to \(c\), and combined predator mortality to \(\delta\). It is a deterministic fixed-coefficient slice of the paper's reduced fuzzy-parameter model, not a theorem about the full uncertainty set. Holding \(A\) fixed while changing \(g\) specifies a path in this coefficient space; it need not hold all primitive fuzzy and carrying-capacity parameters fixed.

Here predator-positive means \(y>0\), all-positive additionally means \(u,v>0\), and an exclusion equilibrium has one prey coordinate zero and the other positive. Eigenvalues are for the ordinary three-dimensional ODE in the real ambient state space (including the missing-prey invasion direction at a boundary equilibrium). Local asymptotic stability of a hyperbolic equilibrium follows from strict negativity of all eigenvalue real parts. At the degenerate threshold, no single point of the segment is claimed asymptotically stable.

## Proof

**Equilibrium classification.** Write \(G(y)=g/(1+ky)-h-py\) and \(a(y)=A/(1+ky)\). At any predator-positive equilibrium, the predator balance forces \(u+v=\sigma\). When both prey are positive, their per-capita equilibrium equations imply
\[
0=(b-a(y))(u-v).
\]
If \(u=v\), then \(u=v=\sigma/2\), and the prey balance is
\[
g=\frac{A\sigma}{2}+(1+ky)\left(h+py+\frac{b\sigma}{2}\right).
\]
The right side is strictly increasing for \(y\ge0\), equals \(g_0\) at \(y=0\), and takes the value \(g_c\) precisely at \(y=y_c\). Thus the unique symmetric predator-positive equilibrium \(E_s=(\sigma/2,\sigma/2,y_s)\) exists exactly for \(g>g_0\), with \(y_s<y_c\) for \(g<g_c\), and \(y_s>y_c\) for \(g>g_c\). If \(u\ne v\), then \(a(y)=b\), forcing \(y=y_c\); their shared per-capita equation then forces \(G(y_c)=b\sigma\), equivalent to \(g=g_c\). Conversely, at that value every nonnegative prey split with total \(\sigma\) satisfies all three equations. On the prey-exclusion face \(v=0\), predator-positive equilibrium requires \(u=\sigma\) and
\[
g=A\sigma+(1+ky)(h+py).
\]
The right side strictly increases, equals \(g_1\) at \(y=0\), and equals \(g_c\) at \(y_c\); hence exactly one such equilibrium exists for \(g>g_1\), and similarly for \(u=0\). Their predator coordinate \(y_b\) is below or above \(y_c\) according as \(g\) is below or above \(g_c\). Finally, \(g_1-g_0=(A-b)\sigma/2>0\) and \(g_c-g_1=(A/b)(h+py_c)-h>0\).

**Symmetric branch.** Introduce \(s=u+v>0\), \(w=(u-v)/(u+v)\), and retain \(y\). Algebra gives the exact system
\[
\begin{aligned}
 \dot s&=sG(y)-\frac{s^2}{2}\bigl(a(y)+b+(a(y)-b)w^2\bigr),\\
 \dot w&=-\frac{s}{2}(a(y)-b)w(1-w^2),\\
 \dot y&=y(cs-\delta).
\end{aligned}
\]
At \(E_s\), the exchange eigenvalue is
\[
 \lambda_{\rm ex}=\frac{\sigma}{2}\bigl(b-a(y_s)\bigr),
\]
while the other two eigenvalues solve
\[
\lambda^2+\frac{\sigma(a(y_s)+b)}{2}\lambda+c\,y_s\sigma D_s=0,
\quad D_s=p+\frac{k(g-A\sigma/2)}{(1+ky_s)^2}>0.
\]
Thus the other two roots always have negative real parts. Since \(a(y)\) decreases and \(y_s\) increases with \(g\), \(\lambda_{\rm ex}\) changes sign once, from negative to positive, at \(g_c\). In fact it crosses transversely with positive speed
\[
\left.\frac{d\lambda_{\rm ex}}{dg}\right|_{g_c}
=\frac{\sigma A k}{2(1+k y_c)\bigl(k(g_c-A\sigma/2)+p(1+k y_c)^2\bigr)}>0.
\]

**Boundary branches.** At \((\sigma,0,y_b)\), the excluded-prey invasion eigenvalue is \(\lambda_{\rm inv}=\sigma(a(y_b)-b)\). The two tangent eigenvalues solve
\[
\lambda^2+\sigma a(y_b)\lambda+c\,y_b\sigma D_b=0,
\quad D_b=p+\frac{k(g-A\sigma)}{(1+ky_b)^2}>0.
\]
Therefore the tangent pair is strictly stable and the invasion eigenvalue is positive for \(g<g_c\) and negative for \(g>g_c\). The other exclusion branch is identical by symmetry.

**Entire neutral segment and its normal spectrum.** At \(g=g_c\), let \(s=\sigma\), \(y=y_c\), and let \(w\) range over \([-1,1]\). Since \(a(y_c)=b\), the exact transformed system gives a zero tangent column at each point of \(\mathcal L\). The two nonzero eigenvalues solve
\[
\lambda^2+b\sigma\lambda+c\,y_c\sigma D_\ell(w)=0,
\quad D_\ell(w)=p+\frac{k\left(g_c-\frac12 A\sigma(1+w^2)\right)}{(1+k y_c)^2}.
\]
Because \(g_c>A\sigma\) and \(|w|\le1\), one has \(D_\ell(w)>p>0\) uniformly. Both roots lie strictly in the open left half plane uniformly across the compact segment, and the remaining eigenvalue is a simple zero tangent to \(\mathcal L\). This includes the two endpoints, whose missing-species invasion eigenvalue vanishes exactly at the threshold. Each point is an equilibrium so no point on the segment can attract all its neighboring segment points; local normal attraction and individual asymptotic stability are distinct.

## Verification

The standalone `check.py` recomputes the vector field and each of the three characteristic-polynomial factorizations symbolically using SymPy, checks that every member of the critical segment is an equilibrium, tests the threshold ordering algebraically, and checks one fully rational example. Execute from this directory using `python check.py`; `requirements.txt` specifies the only nonstandard dependency. For \(A=2\) and \(b=k=h=p=c=\delta=1\), one obtains \(\sigma=1\), \(y_c=1\), \(g_0=5/2\), \(g_1=3\), \(g_c=6\), and the normal characteristic polynomial along \((z,1-z,1)\) is \(\lambda^2+\lambda+(2+z-z^2)\), which has negative-real-part roots for every \(0\le z\le1\). The symbolic tests check derived polynomial identities, not global dynamical properties; the sign and monotonicity arguments above establish those analytical assertions.

## Relationship to prior work

Cao, Wang and Liu [1] study the general asymmetric equation (1.7), list seven equilibrium classes in Section 3, and establish sufficient local and global stability tests and Hopf conditions in Sections 4–5. Their internal-equilibrium existence argument uses a nondegenerate algebraic equation and their local Routh–Hurwitz stability test requires strict positivity of the constant characteristic-polynomial term; neither formulates the degeneracy \(a(y_c)=b\), the full continuum of coexistence splits, or a two-sided exchange involving both exclusion equilibria. Their local calculations cover nondegenerate stability regimes but do not imply the stated neutral line and its uniform normal spectrum.

Ahmed et al. [2] analyze a related three-species fear-effect system with extended Holling-II predator intake and different state-dependent interactions; its published equilibrium/bifurcation theorems do not yield the exact coefficient threshold or segment in [1]. Mukherjee [3] studies one prey species with antipredator behavior in a different competitive-predation model using saturating interference and prey-dependent capture. Its open-access equations (2) and Sections 4–6 were inspected; its stability and Hopf theorems do not specialize to the symmetric fear-dependent coefficient model or its neutral composition segment. The general occurrence of neutral equilibrium manifolds in symmetric competition is background intuition, not a novel principle claimed here; the new statement is the **model-specific sharp threshold and uniform normal-spectrum classification** for [1].

## Limitations

The theorem concerns the precisely specified exchange-symmetric deterministic coefficient slice, not generic asymmetric biological parameters or solutions of an uncertain/fuzzy differential inclusion. It classifies predator-positive equilibria and their local linear/normal types, not global attractor basins, non-equilibrium recurrence, or persistence. No robustness to asymmetry or uniqueness of global attractors is asserted. A literature search cannot exclude every unindexed neutral-competition analysis; an independent audit has not been performed. Ecological parameter paths outside the specified slice need separate analysis.

## References

[1] X. Cao, Q. Wang, J. Liu, “Hopf bifurcation in a predator-prey model under fuzzy parameters involving prey refuge and fear effects,” *AIMS Mathematics* 9 (2024), 23945–23970. DOI: 10.3934/math.20241164. Published 2024-08-12. Open-access full text: https://www.aimspress.com/aimspress-data/math/2024/9/PDF/math-09-09-1164.pdf.

[2] H. J. Ahmed, K. Y. Abdulrahman, K. A. Hamzah, A. N. Mustafa, “Local Bifurcation and Global Stability of Two-Prey-One-Predator Model,” *International Journal of Mathematics and Mathematical Sciences* (2025), article 9391001. DOI: 10.1155/ijmm/9391001.

[3] D. Mukherjee, “Stability and bifurcation of a two competing prey-one predator system with anti-predator behavior,” *Jambura Journal of Biomathematics* 3 (2022), article landing page: https://ejurnal.ung.ac.id/index.php/JJBM/article/view/13820.
