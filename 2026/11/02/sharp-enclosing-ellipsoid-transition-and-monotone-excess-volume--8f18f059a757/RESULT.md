# Sharp enclosing-ellipsoid transition and monotone excess volume for Euclidean ball caps

## Finding
For every integer \(d\ge2\) and \(-1<a<1\), the **unique smallest-volume ellipsoid containing the unit Euclidean ball cut by \(x\ge a\)** is explicit and has exactly one transition. Define
\[
K_{d,a}=\{(x,z)\in\mathbb R\times\mathbb R^{d-1}:x^2+\|z\|^2\le1,\ x\ge a\}.
\]
The optimal ellipsoid is
\[
E_{d,a}=\left\{(x,z):\frac{(x-t)^2}{u^2}+\frac{\|z\|^2}{v^2}\le1\right\},
\]
with the following complete parameter classification:
\[
(t,u,v)=\begin{cases}
(0,1,1),&-1<a\le-1/d,\\[2pt]
\left(\dfrac{1+da}{d+1},\dfrac{d(1-a)}{d+1},\dfrac{d\sqrt{1-a^2}}{\sqrt{d^2-1}}\right),&-1/d<a<1.
\end{cases}
\]
The competing ellipsoids may have arbitrary centers, axes and orientations. For \(a>-1/d\), the **complete** boundary-contact set consists of the north pole \((1,0)\) and the rim \(x=a\), \(\|z\|=\sqrt{1-a^2}\). At or below the threshold the unit ball is itself the optimum, and all the surviving spherical boundary points are contacts.

Writing \(\kappa_j=\pi^{j/2}/\Gamma(j/2+1)\) and \(q=(d-1)/2\), put
\[
\mathcal R_d(a)=\frac{\operatorname{Vol}_d(E_{d,a})}{\operatorname{Vol}_d(K_{d,a})}
=\frac{\kappa_d}{\kappa_{d-1}}\,
\frac{uv^{d-1}}{\int_a^1(1-x^2)^q\,dx}.
\]
Then \(\mathcal R_d(a)\) is **strictly increasing throughout** \((-1,1)\), including across the contact transition, and
\[
\lim_{a\downarrow-1}\mathcal R_d(a)=1,\qquad
\lim_{a\uparrow1}\mathcal R_d(a)
=\frac{\kappa_d}{\kappa_{d-1}}\frac{d^d}{2(d^2-1)^{(d-1)/2}}.
\]
A fixed positive cut \(0<a<1\) obeys
\[
\mathcal R_d(a)\sim\sqrt{2\pi d}\,\frac{a}{1+a}\quad(d\to\infty).
\]
At the finer central-limit scale \(a=\tau/\sqrt d\), for any fixed \(\tau\in\mathbb R\),
\[
\mathcal R_d(\tau/\sqrt d)\longrightarrow
\frac{\exp\big(-\max(\tau,0)^2/2\big)}{\overline\Phi(\tau)},\qquad
\overline\Phi(\tau)=\frac1{\sqrt{2\pi}}\int_\tau^\infty e^{-s^2/2}\,ds.
\]

## Assumptions and scope
The body is a **solid**, closed, unit-radius Euclidean ball truncated by exactly one affine halfspace; \(d\ge2\) and \(-1<a<1\). The ellipsoids are full-dimensional, closed, Euclidean and unrestricted. All volumes are ordinary \(d\)-dimensional Lebesgue volumes. Rotations, translations and uniform changes of radius reduce general single-cap balls to the model above.

## Proof
**1. A finite simplex certificate for any containing ellipsoid.** Choose unit vectors \(w_1,\ldots,w_d\) in \(\mathbb R^{d-1}\) with \(w_i\cdot w_j=-1/(d-1)\) for distinct indices and \(\sum_iw_i=0\). The \(d+1\) points
\[
p_0=(1,0),\qquad p_i=\left(-\frac1d,\sqrt{1-\frac1{d^2}}\,w_i\right)\quad(1\le i\le d)
\]
satisfy \(\frac1{d+1}\sum_{i=0}^dp_i=0\) and \(\frac1{d+1}\sum_{i=0}^dp_ip_i^T=I_d/d\). Suppose \(F=\{y:(y-c)^TQ^{-1}(y-c)\le1\}\) contains these points, with \(Q\) positive definite. Averaging the \(d+1\) containment inequalities gives
\[
\frac1d\operatorname{tr}(Q^{-1})+c^TQ^{-1}c\le1.
\]
Arithmetic-geometric mean applied to the positive eigenvalues of \(Q^{-1}\) yields \((\det Q)^{-1/d}\le\operatorname{tr}(Q^{-1})/d\le1\), hence \(\det Q\ge1\). Equality forces \(c=0\), \(Q=I_d\). Thus the unit ball is the **unique** minimum-volume ellipsoid containing this simplex, and every affine image enjoys the analogous uniqueness property.

**2. The inactive cut.** When \(a\le-1/d\), all the points \(p_i\) belong to \(K_{d,a}\), and the unit ball contains \(K_{d,a}\). The preceding certificate proves global optimality and uniqueness. The entire inherited spherical boundary is tangent to the unit ball.

**3. The active cut.** For \(a>-1/d\), define \(t,u,v\) by the second branch. Under the affine coordinate transformation \(y=((x-t)/u,z/v)\), the pole \((1,0)\) maps to \(p_0\), while the rim points \((a,\sqrt{1-a^2}\,w_i)\) map to the other \(p_i\). Therefore \(E_{d,a}\) is an affine image of the unique enclosing ellipsoid of a regular simplex of contacts. To establish that it contains **the entire cap**, observe that, for \(a\le x\le1\),
\[
1-\left(\frac{(x-t)^2}{u^2}+\frac{1-x^2}{v^2}\right)
=A_{d,a}(x-a)(1-x),\quad
A_{d,a}=\frac{2(d+1)(1+da)}{d^2(1-a)^2(1+a)}>0.
\]
As \(\|z\|^2\le1-x^2\), the displayed identity proves containment. Strict positivity at intermediate \(x\) proves the complete contact description. The simplex certificate rules out every smaller enclosing ellipsoid, without any symmetry restriction.

**4. Strict monotonicity and endpoints.** For the inactive branch, the numerator \(\kappa_d\) is constant and the cap volume strictly decreases with \(a\). For the active branch,
\[
uv^{d-1}=\frac{d^d}{(d+1)(d^2-1)^q}(1-a)(1-a^2)^q.
\]
Set \(h=1-a\), with \(0<h<1+1/d<2\). Cancelling the common power \(h^{q+1}\) reduces the variable factor of \(\mathcal R_d\) to
\[
F(h)=\frac{(2-h)^q}{\int_0^1 y^q(2-hy)^q\,dy}.
\]
Its logarithmic derivative has the sign of
\[
-\frac1{2-h}+\frac{\int_0^1y^q(2-hy)^q\,\frac{y}{2-hy}\,dy}{\int_0^1y^q(2-hy)^q\,dy},
\]
which is strictly negative because \(y/(2-hy)<1/(2-h)\) for \(0\le y<1\). Thus \(F\) decreases as \(h\) increases, proving strict increase in \(a\). Both branches agree at \(a=-1/d\). The full-ball limit gives \(1\); at \(h\downarrow0\), \(F(h)\to q+1=(d+1)/2\), giving the stated thin-cap limit.

**5. Dimensional asymptotics.** For each fixed \(0<a<1\), a one-sided Laplace estimate at the endpoint gives
\[
\int_a^1(1-x^2)^q\,dx\sim\frac{(1-a^2)^{q+1}}{2qa}.
\]
Together with \(\kappa_d/\kappa_{d-1}\sim\sqrt{2\pi/d}\) and \(d^d/[(d+1)(d^2-1)^q]\to1\), this proves the fixed-cut asymptotic. For \(a=\tau/\sqrt d\), the first coordinate of a uniform point in \(B_d\), multiplied by \(\sqrt d\), converges in law to a standard normal; hence the cap's volume fraction tends to \(\overline\Phi(\tau)\). If \(\tau<0\), the cut is eventually inactive and the enclosing ellipsoid is the ball. If \(\tau\ge0\), the active semiaxis product tends to \(e^{-\tau^2/2}\). Their quotient gives the final formula.

## Verification
The separate script `verify_cap_lowner.py` checks the defining quadratic containment identity exactly over rational test cases, reconstructs the affine simplex contact certificate, integrates volume ratios and tests strict monotonicity numerically in dimensions \(2\) through \(11\), checks the thin-cap limit and known hemispherical benchmarks, and independently tests the Gaussian window through a beta-integral formula. Run `python3 verify_cap_lowner.py` with SymPy and mpmath installed. These computations check representative instances; the dimension-uniform results are established by the analytic proof above.

## Relationship to prior work
Ivanov and Naszódi, *Functional John and Löwner conditions for pairs of log-concave functions* (arXiv:2212.11781, first public on December 22, 2022, primary MSC 52A23), gives general contact/optimality theory. Its accessible complete HTML treatment does not state an explicit all-height ball-cap classification or the present volume-ratio laws. A March 2025 Mathematics Stack Exchange discussion, *Smallest volume ellipsoid containing half ball*, directly obtains the **hemisphere** specialization \(a=0\) in every dimension. That solved case is not claimed as new. The additional statements assessed here are the all-height contact transition, global strict monotonicity, thin-cap endpoint, and dimension-dependent Gaussian crossover, none of which is logically supplied by a formula for the single hemisphere. Published general enclosing-ellipsoid characterizations are used as conceptual context, not presented as new methodology.

## Limitations
The result applies to one-halfspace cuts of Euclidean balls (and their affine images). It does not determine enclosing ellipsoids of arbitrary intersections of balls, nonellipsoidal smooth bodies, or multiple independent cuts. The pointwise thin-cap limit and the fixed-cut high-dimensional limit are different asymptotic regimes. The novelty assessment is provisional: literature beyond inspected sources may contain equivalent full-height formulas under different terminology. There has been no independent mathematical audit.

## References
- G. Ivanov and M. Naszódi, *Functional John and Löwner conditions for pairs of log-concave functions*, arXiv:2212.11781v1 (December 22, 2022); *International Mathematics Research Notices* (2023), DOI:10.1093/imrn/rnad210. https://arxiv.org/abs/2212.11781
- *Smallest volume ellipsoid containing half ball*, Mathematics Stack Exchange, question 5040265, questions and answers dated February 27–March 7, 2025. https://math.stackexchange.com/questions/5040265/smallest-volume-ellipsoid-containing-half-ball
- F. John, *Extremum problems with inequalities as subsidiary conditions*, in *Studies and Essays Presented to R. Courant on His 60th Birthday*, 1948, pp. 187–204 (background theory only).
