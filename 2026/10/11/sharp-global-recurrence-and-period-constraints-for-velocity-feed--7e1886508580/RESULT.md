# Sharp global recurrence and period constraints for velocity-feedback jerk equations

## Finding
For the velocity-feedback jerk equation
\[
\dddot x+A\ddot x+x=f(\dot x),\qquad A\in\mathbb R,
\]
write \(v=\dot x\), \(a=\ddot x\), and \(e=(f(0),0,0)\). The following unified recurrence theorem holds for every locally Lipschitz \(f:\mathbb R\to\mathbb R\).

**Nonpositive damping.** If \(A\le0\), every bounded complete solution is the equilibrium \(e\); every bounded forward solution converges to \(e\). Hence the only nonempty compact invariant set is \(\{e\}\).

**Positive damping.** If \(A>0\), every compactly supported invariant Borel probability measure \(\mu\) satisfies
\[
\int v^2\,d\mu=A\int a^2\,d\mu,
\qquad
\int vf(v)\,d\mu=-\int a^2\,d\mu.
\tag{1}
\]
Either \(\mu=\delta_e\), or both quadratic moments are strictly positive and the velocity-energy-weighted *secant feedback slope* is exactly the linear imaginary-pair threshold:
\[
\frac{\displaystyle\int_{v\ne0}v^2\frac{f(v)-f(0)}{v}\,d\mu}
{\displaystyle\int v^2\,d\mu}=-\frac1A.
\tag{2}
\]
Every nonconstant periodic orbit of least period \(P\) satisfies the sharp bound
\[
P\ge2\pi\sqrt A.
\tag{3}
\]
Equality holds precisely when, for some \(R>0\), the velocity is \(v(t)=R\cos(t/\sqrt A+\theta)\) and \(f(s)=f(0)-s/A\) throughout \([-R,R]\). Conversely, whenever this affine identity holds on \([-R,R]\), it produces an equality orbit \(x(t)=f(0)+R\sqrt A\sin(t/\sqrt A+\theta)\).

For the original 1997 quadratic example \(f(v)=v^2\), every compact invariant measure other than \(\delta_{(0,0,0)}\) gives positive mass both to \(v<-1/A\) and to \(v>0\); each nonconstant periodic orbit crosses \(v=-1/A\) at least twice per least period and has strict period bound \(P>2\pi\sqrt A\).

## Assumptions and scope
Coordinates are \((x,v,a)\in\mathbb R^3\) with vector field
\[
\dot x=v,\qquad\dot v=a,\qquad\dot a=-Aa-x+f(v).
\tag{4}
\]
Local Lipschitz regularity guarantees uniqueness of solutions on their maximal intervals. A *bounded complete solution* is defined for all positive and negative times and has bounded image. A *compact invariant set* is invariant under all time translations of the flow. An invariant probability is carried by a compact invariant set (hence every generator integral below is justified). The positive-damping statements concern such measures without requiring ergodicity or existence of a chaotic attractor. The local spectral comparison requires that \(f\) also be differentiable at zero.

## Proof
Let \(F(v)=\int_0^v f(s)\,ds\) and introduce the differentiable scalar observable
\[
H(x,v,a)=\frac{a^2}{2}+xv-F(v).
\]
Differentiation along (4) yields an *exact coboundary*, with no approximation:
\[
\frac{dH}{dt}
=a(-Aa-x+f(v))+v^2+xa-f(v)a
=v^2-Aa^2.
\tag{5}
\]
For compactly supported invariant \(\mu\), every continuously differentiable observable used here has zero mean generator. Equation (5) proves the first identity (1). Differentiating \(v^2/2\) and \(x^2/2\) gives
\[
\int va\,d\mu=0,\qquad \int xv\,d\mu=0.
\]
Differentiation of \(va\) then yields
\[
0=\int\left(a^2-Ava-xv+vf(v)\right)d\mu
=\int\left(a^2+vf(v)\right)d\mu,
\]
which proves the second identity (1). Also \(\int v\,d\mu=0\) from \(\dot x=v\). For \(A>0\), substitute the first identity into the second and subtract the constant term \(f(0)\int v\,d\mu=0\); dividing by \(\int v^2\,d\mu\) gives (2) when the denominator is positive. If this denominator vanishes, \(v=0\) almost surely. Invariance at every rational time and continuity of sample trajectories force \(v(t)=0\) for all time almost surely, hence \(a=0\), \(x=f(0)\); thus \(\mu=\delta_e\).

For \(A\le0\), equation (5) is nonnegative along all trajectories. Its zero set is \(v=a=0\) when \(A<0\), and \(v=0\) when \(A=0\). In either case the largest invariant subset of the zero set is \(\{e\}\): an orbit lying in \(v=0\) has \(a=\dot v=0\), then \(\dot a=f(0)-x=0\), so \(x=f(0)\). On every bounded forward orbit, \(H\) is bounded, monotone and convergent; its omega-limit set is nonempty, compact and invariant, and lies in the zero-derivative set, so it equals \(\{e\}\). Hence that orbit converges to \(e\). On a bounded complete orbit the same argument applied to both the alpha- and omega-limit sets forces \(H(t)\to H(e)\) as \(t\to\pm\infty\). Monotonicity then makes \(H\) constant, so the complete orbit is \(e\). Every point of any compact invariant set lies on a bounded complete orbit, proving the claim.

For a nonconstant periodic orbit with \(A>0\), the periodic velocity has zero mean and \(\int_0^P v^2\,dt=A\int_0^P(v')^2\,dt\) by (5). The sharp periodic Wirtinger inequality gives
\[
\int_0^P(v')^2\,dt\ge\left(\frac{2\pi}{P}\right)^2\int_0^P v^2\,dt,
\]
so (3) follows. Equality holds exactly for a nonzero fundamental harmonic \(v(t)=R\cos(2\pi t/P+\theta)\). The moment equality sets its angular frequency to \(A^{-1/2}\). Integrating once gives \(x(t)=m+R\sqrt A\sin(t/\sqrt A+\theta)\). Substitution into (4) gives \(f(v)=m-v/A\) for every attained \(v\in[-R,R]\). In particular at \(v=0\), \(m=f(0)\). Conversely, substitution of the stated harmonic trajectory verifies the jerk equation whenever \(f(s)=f(0)-s/A\) throughout this interval.

For \(f(v)=v^2\), equation (2) is \(\int v^2(v+1/A)\,d\mu=0\). Were \(\mu\) supported in \(v\ge-1/A\), nonnegativity would force \(v\in\{0,-1/A\}\) almost surely; the zero mean \(\int v\,d\mu=0\) then forces \(v=0\) and hence \(\mu=\delta_e\). Thus every other invariant measure has \(\mu\{v<-1/A\}>0\); zero mean also forces \(\mu\{v>0\}>0\). A nonconstant periodic velocity traverses both regions and crosses the separating level at least twice. Equality in (3) would demand \(v^2=-v/A\) for all \(v\in[-R,R]\), impossible for \(R>0\), so the period bound is strict in this quadratic case.

Finally, when \(f\) is differentiable at zero, the equilibrium Jacobian has characteristic polynomial
\[
\lambda^3+A\lambda^2-f'(0)\lambda+1.
\]
At \(f'(0)=-1/A\) and \(A>0\) this factors as \((\lambda+A)(\lambda^2+1/A)\). Hence the same value on the right of (2) is precisely the local *imaginary-pair spectral threshold*. No nonlinear Hopf-bifurcation nondegeneracy is asserted.

## Verification
The derivations (5), the generator of \(va\), the equilibrium characteristic polynomial and its imaginary-pair factorization, and the equality-orbit substitution were separately checked by the standalone script `artifacts/verify_identities.py`, using exact symbolic algebra. Running `python artifacts/verify_identities.py` with SymPy prints `VERIFY_OK`. The actual observed output is embedded in `artifacts/verification_output.txt`. Wirtinger's equality classification, the compact-invariance argument, and the support-crossing proof are analytic steps presented above; the symbolic script is not a computer proof of these global implications.

## Relationship to prior work
Sprott's 1997 paper introduced the quadratic velocity-feedback case, its numerical period-doubling regime, and its volume contraction; it did not state an invariant-measure secant identity, a sharp universal least-period bound with its equality case, or a rigorous global exclusion of compact recurrence at nonpositive damping. Munmuangsaen, Srisuchinwong and Sprott (2011), Eq. (3), studied the wider \(A=1\) velocity-feedback class, including smooth and nonsmooth nonlinearities, and calculated the local spectral condition \(f'(0)=-1\). Formula (2) is an exact finite-amplitude statistical counterpart to that local condition; the local condition itself is not new.

The published third-order Goodwin feedback identity (see reference 4) concerns nonlinear *position* feedback and a weighted derivative slope rather than the *velocity* feedback and weighted secant slope here. Eichhorn, Linz and Hänggi (2002) analyze two polynomial jerk families, one with a product \(x\dot x\), the other with \(x^2\), unlike the current class \(f(\dot x)\) with a linear restoring \(x\) term. These bounds are not obtained by matching their parameters. A prior published forced-oscillator result for \(\dddot x+\beta\ddot x+\dot x=f(x)\) also has a different restoring term and feedback coordinate, so its fixed period bound does not imply the present \(\sqrt A\)-dependent one.

## Limitations
The identities constrain invariant states but do not establish existence, uniqueness, entropy, or stability of any nonlinear recurrent state for \(A>0\). The equality case in (3) is attained by critical affine feedback, not by Sprott's quadratic nonlinearity. For discontinuous feedback, singularities in the attained velocity range, set-valued impact limits, or nonunique flows, the stated locally Lipschitz theorem does not apply without a separate argument. The spectral factorization alone does not prove a nonlinear Hopf bifurcation. Older third-order-ODE multiplier literature and the inaccessible complete text of a 2009 study of piecewise jerk nonlinearities remain possible coverage risks; the originality comparison is conditional on the primary texts and public searches described in the accompanying review.

## References
1. J. C. Sprott, “Simplest dissipative chaotic flow,” *Physics Letters A* **228** (1997), 271–274, DOI: `10.1016/S0375-9601(97)00088-1`. Author/publication PDF: https://wippl.wisc.edu/pub_files/journal/Sprott116.pdf (dated 14 April 1997).
2. B. Munmuangsaen, B. Srisuchinwong, J. C. Sprott, “Generalization of the simplest autonomous chaotic system,” *Physics Letters A* **375** (2011), 1445–1450, DOI: `10.1016/j.physleta.2011.02.028`. Author PDF: https://sprott.physics.wisc.edu/pubs/paper354.pdf (available online 16 February 2011).
3. R. Eichhorn, S. J. Linz, P. Hänggi, “Simple polynomial classes of chaotic jerky dynamics,” *Chaos, Solitons & Fractals* **13** (2002), 1–15, DOI: `10.1016/S0960-0779(00)00237-X`; lawful full text: https://www.physik.uni-augsburg.de/theo1/hanggi/Papers/266.pdf.
4. “Global Hopf-slope balance for third-order feedback cycles and the Goodwin oscillator,” public mathematical result (2026), https://github.com/published-finding corpus/2026/tree/main/2026/9/20/SCOPE-goodwin-global-hopf-slope-balance--69bab068e3f7.
5. L. M. Kocić and S. Gegovska-Zajkova, “On a jerk dynamical system,” *Facta Universitatis, Series: Automatic Control and Robotics* **8** (2009), 35–44. (Bibliographic source only; complete text was not available for comparison.)
