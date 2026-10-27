# A single zero arc for every Hardy-regularized harmonic Bergman kernel of the disk

## Finding
For every \(\kappa>0\), the reproducing kernel of the complex harmonic Hilbert space on the unit disk equipped with normalized area norm plus \(\kappa\) times normalized boundary norm has zeros. Their entire geometry is determined by a unique number \(\rho_\kappa\in(0,1)\), specified by
\[
\kappa\frac{1-\rho_\kappa}{1+\rho_\kappa}
=\int_0^1 s^{1/\kappa}\frac{1-s\rho_\kappa}{1+s\rho_\kappa}\,ds.
\]
Specifically, write \(t=z\overline w\), where \(z,w\in\mathbb D\). The kernel is strictly positive whenever \(|t|<\rho_\kappa\); at \(|t|=\rho_\kappa\) it vanishes only when \(t=-\rho_\kappa\). For each \(\rho_\kappa<r<1\), there are exactly two zeros on \(|t|=r\), of the form \(t=re^{\pm i\theta_\kappa(r)}\) for a unique angle \(\theta_\kappa(r)\in(0,\pi)\). There are no other zeros. This zero set is one embedded smooth real-analytic arc passing through \(-\rho_\kappa\), with both ends tending to the boundary point \(1\).

Its sharp first-zero radius has the two endpoint laws
\[
\lim_{\kappa\downarrow0}\rho_\kappa=\sqrt2-1,
\qquad
\lim_{\kappa\to\infty}\kappa(1-\rho_\kappa)
=2(2\log2-1).
\]
In particular, any finite positive boundary regularization leaves real-harmonic reproducing-kernel zeros, even though the limiting boundary-only kernel is everywhere positive.

## Assumptions and scope
Let \(\mathbb D=\{z\in\mathbb C:|z|<1\}\), let \(dA\) be Euclidean area measure, and let \(dm=d\phi/(2\pi)\) be normalized angular measure on the unit circle. Work with complex-valued functions satisfying the usual real Laplace equation \(\Delta h=0\), with finite norm
\[
\|h\|_\kappa^2
=\frac1\pi\int_{\mathbb D}|h(z)|^2\,dA(z)
+\kappa\int_0^{2\pi}|h(e^{i\phi})|^2\,\frac{d\phi}{2\pi},
\qquad \kappa>0.
\]
The boundary values are the \(L^2\) radial traces. Equivalently, complete harmonic polynomials in this norm; all functions then possess harmonic boundary traces. Point evaluation in \(\mathbb D\) is bounded. The reproducing kernel \(K_\kappa(z,w)\) is real-valued, though the function space is a complex Hilbert space. Set \(t=z\overline w\), \(r=|t|\), and \(c=\cos\arg t\). Every \(t\in\mathbb D\) is realized by some \(z,w\in\mathbb D\); therefore the following is a classification of all pairs \((z,w)\) through their product.

## Proof
**Step 1: Fourier diagonalization.** The harmonic monomials \(1,z^n,\overline z^{\,n}\) for positive integers \(n\) are mutually orthogonal. Their squared norms are \(1+\kappa\) and \(1/(n+1)+\kappa\), respectively. Consequently, with \(a_n=(n+1)/(1+\kappa(n+1))\),
\[
K_\kappa(z,w)=F_\kappa(t),\qquad
F_\kappa(re^{i\theta})=a_0+2\sum_{n=1}^\infty a_nr^n\cos(n\theta).
\]
The series and its derivatives converge locally uniformly on \(|t|<1\). Define the positive Poisson kernel
\[
P_r(c)=\frac{1-r^2}{1-2rc+r^2}\qquad(0\le r<1,\;-1\le c\le1).
\]
The identity \(a_n=\kappa^{-1}-[\kappa^2(n+1+\kappa^{-1})]^{-1}\), valid also for \(n=0\), and the moment formula \((n+1+\kappa^{-1})^{-1}=\int_0^1s^{n+\kappa^{-1}}\,ds\) yield the exact Poisson-mixture representation
\[
F_\kappa(re^{i\theta})=\frac{P_r(c)}\kappa
-\frac1{\kappa^2}\int_0^1s^{1/\kappa}P_{sr}(c)\,ds.\tag{1}
\]
All sums and integrals interchange absolutely on compact subdisks.

**Step 2: Strict angular comparison.** Divide by the strictly positive first Poisson factor and set
\[
H_\kappa(r,c)=\frac{\kappa F_\kappa(re^{i\theta})}{P_r(c)}
=1-\frac1\kappa\int_0^1s^{1/\kappa}Q_s(r,c)\,ds,
\quad Q_s(r,c)=\frac{P_{sr}(c)}{P_r(c)}.
\]
For \(0<r<1\) and \(0\le s<1\), direct differentiation gives
\[
\frac{\partial Q_s}{\partial c}
=-\frac{2r(1-s)(1-sr^2)(1-s^2r^2)}{(1-r^2)(1-2src+s^2r^2)^2}<0.
\]
Thus \(H_\kappa(r,c)\) is strictly increasing in \(c\), for every \(r\in(0,1)\). At \(c=1\) the inequality \(P_{sr}(1)<P_r(1)\) implies
\[
H_\kappa(r,1)>1-\frac1\kappa\int_0^1s^{1/\kappa}\,ds
=\frac\kappa{1+\kappa}>0.\tag{2}
\]
In particular, any zero on a given nonzero radius must occur at an angle where \(H_\kappa\) crosses its unique possible zero from negative to positive as \(c\) increases.

**Step 3: Unique first radial crossing.** At \(c=-1\),
\[
Q_s(r,-1)=\frac{1+r}{1-r}\frac{1-sr}{1+sr},
\qquad
\frac{\partial}{\partial r}\log Q_s(r,-1)
=\frac{2(1-s)(1+sr^2)}{(1-r^2)(1-s^2r^2)}>0.
\]
Hence \(H_\kappa(r,-1)\) decreases strictly in \(r\). At \(r=0\) it equals \(\kappa/(1+\kappa)>0\); as \(r\uparrow1\), the integral of \(Q_s(r,-1)\) diverges, since it contains the factor \((1+r)/(1-r)\) multiplied by an integral converging to a strictly positive finite value. Therefore \(H_\kappa(r,-1)\) has exactly one zero, at \(r=\rho_\kappa\), and inserting the explicit quotient gives precisely the scalar equation in the Finding section.

By strict angular increase and (2), for \(r<\rho_\kappa\) the kernel has no zero; for \(r=\rho_\kappa\) it vanishes only at \(c=-1\); and for \(r>\rho_\kappa\) it has exactly one angular cosine \(c\in(-1,1)\), hence exactly two conjugate points. This proves both the full zero set and sharp positivity radius.

**Step 4: Regularity and topology.** On the zero set with \(\rho_\kappa<r<1\), differentiation of \(F_\kappa=(P_r/\kappa)H_\kappa\) shows that \(\partial_cF_\kappa>0\), so the two angular branches are analytic and nondegenerate. At the common point \(t=-\rho_\kappa\), the strict radial derivative \(\partial_rH_\kappa(r,-1)<0\) proves that \(\partial_rF_\kappa\ne0\). The real-analytic implicit-function theorem then joins the conjugate branches smoothly through that point. Since each radius is met in exactly two opposite angular branches, and each branch has only one point per radius, there are no self-intersections or additional components.

As \(r\uparrow1\), equation (1) shows that \(F_\kappa(re^{i\theta})\) is eventually negative for each fixed \(\cos\theta<1\): its first term tends to zero, whereas its second tends to a strictly negative number. Equation (2) stays positive at \(\cos\theta=1\). Consequently the unique zero cosine tends to \(1\), proving that both ends of the arc approach \(t=1\).

**Step 5: Endpoint laws.** When \(\kappa\downarrow0\), for each fixed \(|t|<1\), dominated convergence of the Fourier series yields
\[
F_\kappa(t)\longrightarrow
F_0(t)=2\operatorname{Re}(1-t)^{-2}-1.
\]
Along \(t=-r\), the limiting zero is the unique root of \(2/(1+r)^2-1=0\), namely \(\sqrt2-1\). Uniform convergence on compact subdisks together with the unique-crossing characterization forces \(\rho_\kappa\to\sqrt2-1\).

When \(\kappa\to\infty\), for fixed \(r<1\), the coefficients \(\kappa a_n\) tend to \(1\), so \(\kappa F_\kappa(re^{i\theta})\to P_r(c)>0\). It follows that \(\rho_\kappa\to1\). Applying dominated convergence to the exact first-zero equation gives
\[
\lim_{\kappa\to\infty}\frac{\kappa(1-\rho_\kappa)}{1+\rho_\kappa}
=\int_0^1\frac{1-s}{1+s}\,ds
=2\log2-1.
\]
Since \(\rho_\kappa\to1\), the second claimed limit follows.

## Verification
The accompanying `checker.py` independently evaluates the Fourier coefficient series and the Poisson-mixture integral using elementary numerical routines, brackets the negative-axis crossing, checks the sign change, and samples strict monotonicity of the normalized angular comparison. `check_output.txt` contains one deterministic run. The checker performs 27 series/integral comparisons and verifies representative parameter values; these finite tests are consistency checks, not proof of the infinite-dimensional or all-parameter theorem. The proof above rests on exact identities and strict analytic inequalities. No external or independent mathematical audit has been performed.

## Relationship to prior work
Engliš's 2015 analysis of Poisson and harmonic Bergman kernels develops the general boundary-operator framework and discusses reproducing kernels of harmonic Sobolev-type spaces. The exact present disk norm fits this broad framework, but the inspected material does not supply its global nodal arc, unique first-zero radius, or sharp regularization asymptotics. Auchmuty's work on reproducing kernels of real harmonic spaces develops related harmonic-kernel and boundary spectral constructions without the mixed-norm zero-locus classification established here. The harmonic kernel must not be identified with the holomorphic Bergman–Hardy interpolation kernel: retaining both analytic and coanalytic harmonic modes changes the sign geometry.

## Limitations
The classification is for the complex Hilbert space of ordinary harmonic functions on the planar unit disk and the specified normalized area-plus-boundary norm. It does not address weighted radial area densities, other planar domains, higher-dimensional balls, or general boundary pseudodifferential weights. The theorem gives exact zero geometry, not operator-conditioning estimates. Historical priority for an equivalent representation in older harmonic reproducing-kernel literature cannot be entirely excluded; an inaccessible full text would require renewed comparison. The algebraic expressions for the zero arc are implicit, not elementary closed forms.

## References
1. M. Engliš, *Boundary singularity of Poisson and harmonic Bergman kernels*, arXiv:1503.06440, first version submitted 2015-03-22. https://arxiv.org/abs/1503.06440
2. G. Auchmuty, *Reproducing Kernels for Hilbert Spaces of Real Harmonic Functions* (author-hosted manuscript). https://www.math.uh.edu/~giles/PDFpapers/RevHarmRK.pdf
3. M. Engliš, D. Lukkassen, J. Peetre, L.-E. Persson, *On the formula of Jacques-Louis Lions for reproducing kernels of harmonic and other functions*, J. Reine Angew. Math. (2004), DOI 10.1515/crll.2004.035. Bibliographic abstract consulted; full text was not available in the present literature comparison.
4. M. Nishio and K. Tanaka, *Harmonic Bergman kernels and Toeplitz operators on the ball with radial measures*, Rev. Roumaine Math. Pures Appl. 62 (2017), 155–169. https://imar.ro/journals/Revue_Mathematique/pdfs/2017/1/8.pdf
