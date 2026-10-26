# Exact dilute-minority curvature for antagonistic lattice adsorption

## Finding
For the continuous-time, repeated-attempt antagonistic two-species adsorption process on the periodic square lattice \(\Lambda_L=(\mathbb Z/L\mathbb Z)^2\), with \(L\ge7\), initially empty sites, independent species-A attempts of rate \(1-p\) and species-B attempts of rate \(p\) at every site, and irreversible acceptance of an attempt when the site is empty and none of its four neighbors carries the opposite species, let \(\theta_{B,L}(p)\) be the expected eventual fraction of B-occupied sites. Then, for each fixed \(L\ge7\),
\[
\theta_{B,L}(p)=\frac p5+\frac{71}{225}p^2+O_L(p^3),\qquad p\downarrow0.
\]
The coefficient \(71/225\) is independent of lattice size in this range. The model admits arbitrarily many attempts at an empty site; replacing these by a single prescribed B attempt at each of two selected sites is not equivalent at quadratic order. In particular, the coefficient differs by exactly \(1/24\) from the tentative value \(493/1800\) in Martins–Dickman–Ziff (2022).

## Assumptions and scope
The square lattice has nearest-neighbor adjacency and both species deposit only at empty sites. Attempts at every site arrive as independent Poisson processes of respective rates \(1-p\) and \(p\), and rejected attempts do not occupy a site or forbid later attempts of the other species. Once a particle is deposited it never leaves. The final occupancy is well-defined on the finite torus; symmetry makes \(\theta_{B,L}(p)\) the probability that a prescribed site \(o\) is eventually B-occupied. The asymptotic is with fixed \(L\), not a simultaneous thermodynamic limit. Reparameterize time so A attempts have rate one and B attempts have rate \(\varepsilon=p/(1-p)\).

## Proof
Let \(C_x=\{x\}\cup\{z:z\sim x\}\) be the closed five-site neighborhood and let \(T_z\) be the first A-attempt time at site \(z\); these are independent rate-one exponentials. With no B attempt at any other site, the first B attempt at \(o\) occurs at time \(s\), density \(\varepsilon e^{-\varepsilon s}\), and succeeds precisely if all \(T_z>s\) for \(z\in C_o\). Its contribution is
\[
\int_0^\infty \varepsilon e^{-(5+\varepsilon)s}\,ds=\frac{\varepsilon}{5+\varepsilon}=\frac\varepsilon5-\frac{\varepsilon^2}{25}+O(\varepsilon^3).
\]
At first order in the **other-site** B rate, a single B attempt at some \(y\ne o\), at time \(0<u<s\), affects admissibility at \(o\) only if \(C_y\cap C_o\ne\varnothing\). Write \(m=|C_y\cap C_o|\). Its success requires \(T_z>u\) on all of \(C_y\). Conditional on that success, the B at \(y\) forever precludes A on \(C_y\), so the later B attempt at \(o\) is admissible exactly when \(T_z>s\) on \(C_o\setminus C_y\). The joint event therefore has probability
\[
\exp[-5u-(5-m)s].
\]
In the counterfactual evolution without the attempt at \(y\), the contribution from the same configurations requires all A clocks in \(C_o\) to exceed \(s\), and all A clocks in \(C_y\setminus C_o\) to exceed \(u\). It has probability
\[
\exp[-5s-(5-m)u].
\]
The integrated **net** increment contributed by a site with overlap \(m\) is thus
\[
\begin{aligned}
D_m&=\int_0^\infty\int_0^s\bigl(e^{-5u-(5-m)s}-e^{-5s-(5-m)u}\bigr)\,du\,ds\\
&=\frac1{(5-m)(10-m)}-\frac1{5(10-m)}
=\frac{m}{5(5-m)(10-m)}.
\end{aligned}
\]
The first term must involve absolute-time survival \(T_z>s\), not only survival during the interval \((u,s)\). On a square torus with \(L\ge7\), there are four nearest-neighbor and four diagonal sites with \(m=2\), and four axial distance-two sites with \(m=1\); every other \(y\) has \(m=0\). Therefore the first-order correction in the other-site rate is
\[
8D_2+4D_1=8\left(\frac1{60}\right)+4\left(\frac1{180}\right)=\frac7{45}.
\]
Combining the root-first-B density and the one-other-B correction gives
\[
\theta_{B,L}=\frac\varepsilon5+\left(-\frac1{25}+\frac7{45}\right)\varepsilon^2+O_L(\varepsilon^3)
=\frac\varepsilon5+\frac{26}{225}\varepsilon^2+O_L(\varepsilon^3).
\]
Since \(\varepsilon=p+p^2+O(p^3)\), the asserted coefficient is \(1/5+26/225=71/225\).

To justify the fixed-volume error: the acceptance status of an attempted species at a site is monotone in time after a failed attempt—an already deposited opposite neighbor cannot disappear—so only the first A and first B attempts at a site need be considered. For the coefficient through second order, histories with zero or one off-root B arrival preceding the root attempt suffice. On the square lattice any vacant site whose A attempt was obstructed by at most two already deposited B particles must have at least one eventually deposited A neighbor: one B must be adjacent to obstruct that site, and a second B can obstruct at most two of the site's three remaining neighbors, which themselves are not adjacent to the first B. Thus after the maximum of the finitely many first A-arrival times no later B arrival can deposit unless at least three B arrivals have intervened. A bounded-volume Poisson count then bounds all omitted histories by \(O_L(\varepsilon^3)\); the exponential integrands above give finite second-order coefficients. This also supplies the necessary continuity of the expansion at zero B rate.

## Verification
The standalone Python checker `check.py` enumerates the closed-neighborhood intersections, computes every exact integrated contribution with rational arithmetic, verifies \(8D_2+4D_1=7/45\), and checks the final coefficient and discrepancy. It also independently checks the leading two-B joint probabilities at nearest-neighbor, diagonal, axial distance-two, and disjoint closed neighborhoods: respectively \(1/12\), \(1/12\), \(1/18\), and \(1/25\) times \(p^2\), up to higher orders. These finite checks do not substitute for the argument controlling the Taylor remainder.

## Relationship to prior work
Martins, Dickman, and Ziff introduced and analyzed this repeated-attempt adsorption model. Their first-order coefficient \(1/5\) is retained. Section III.2 reports the quadratic number \(493/1800\) as believed exact, based on a two-designated-B-attempt approximation with numerical probabilities; it also gives a less stable fitted coefficient approximately \(0.298\). The present independent arrival-clock calculation accounts for B deposition at a site after an earlier A attempt at that same site was rejected by a neighboring B particle, a history permitted by the original repeated-attempt dynamics. This changes the second-order coefficient and explains the discrepancy. The distinction has also been compared with do Amaral–dos Santos's different one-attempt-per-site antagonistic model (2023) and the earlier general graph deposition framework of Penrose–Sudbury (2005), neither of which supplies this finite-torus coefficient. No implication is claimed for the authors' percolation-threshold estimates.

## Limitations
The \(O_L(p^3)\) bound may depend on \(L\); no exchange of the thermodynamic and dilute limits is proved. This is a low-density curvature statement, not a complete expression for the jammed coverages. The coefficient is specific to square-lattice nearest-neighbor antagonism with continued species-attempt clocks. Replacing the process by a single-attempt-per-site rule changes the question. Independent scholarly validation and priority checking remain outstanding.

## References
- P. H. L. Martins, R. Dickman, and R. M. Ziff, *Percolation in two-species antagonistic random sequential adsorption in two dimensions*, arXiv:2211.04622 (first posted November 9, 2022), especially Sections II and III. https://arxiv.org/abs/2211.04622
- C. S. do Amaral and D. C. dos Santos, *One-dimensional AB random sequential adsorption with one deposition per site*, arXiv:2306.09786 (first posted June 16, 2023). https://arxiv.org/abs/2306.09786
- M. D. Penrose and A. Sudbury, *Exact and approximate results for deposition and annihilation processes on graphs*, arXiv:math/0503519 (2005). https://arxiv.org/abs/math/0503519
