# Exact phase geometry and critical logarithmic spiral in symmetric Lorenz-84

## Statement

Consider the Lorenz-84 atmospheric circulation model with zero asymmetric heating,
\[
\dot x=-ax-y^2-z^2+aF(t),\qquad
\dot y=-y+xy-bxz,\qquad
\dot z=-z+bxy+xz,
\]
where \(a>0\), \(b\in\mathbb R\), and \(F(t)\) is any forcing for which the displayed ODE has a classical solution. Put
\[
w=y+iz,\qquad R=|w|^2=y^2+z^2.
\]
On every solution with \(R(0)>0\), choose a continuous lift \(\theta(t)=\arg w(t)\).

### Exact phase-amplitude reconstruction

For every such solution,
\[
\dot R=2(x-1)R,\qquad \dot\theta=bx,
\]
and hence
\[
\boxed{\theta(t)-\theta(0)=bt+\frac b2\log\frac{R(t)}{R(0)}}.
\]
Equivalently,
\[
w(t)=w(0)\sqrt{\frac{R(t)}{R(0)}}\,
\exp\!\left(ibt+\frac{ib}{2}\log\frac{R(t)}{R(0)}\right).
\]
Thus if the reduced pair \((x,R)\) is \(T\)-periodic and \(R>0\), the lifted eddy phase advances by exactly \(bT\) in one reduced period.

### Exact global isochrons for constant \(F>1\)

Let \(F(t)\equiv F>1\), and write
\[
s=x-1,\qquad c=a(F-1)>0.
\]
Then
\[
\dot s=-as+c-R,\qquad \dot R=2sR.
\]
On \(R>0\),
\[
L(s,R)=\frac12s^2+\frac12\left(R-c-c\log\frac Rc\right)
\]
is proper and satisfies
\[
\boxed{\dot L=-as^2}.
\]
Its largest invariant zero-dissipation set is the single reduced equilibrium
\((s,R)=(0,c)\). Therefore every solution with \(R(0)>0\) converges to
\[
\mathcal C_F=\{x=1,\ y^2+z^2=c\}.
\]
For \(b\ne0\), this is a periodic orbit of period \(2\pi/|b|\).

Moreover
\[
\boxed{\Phi(x,y,z)=
\arg(y+iz)-\frac b2\log\frac{y^2+z^2}{a(F-1)}
\pmod{2\pi}}
\]
satisfies \(\dot\Phi=b\) throughout the basin \(R>0\), and \(\Phi=\arg(y+iz)\) on
\(\mathcal C_F\). Hence its level sets are explicit global isochrons. If
\(R_0>0\), the asymptotic phase offset is
\[
\boxed{\Phi_0=\theta_0+\frac b2\log\frac{a(F-1)}{R_0}}.
\]

The invariant axis \(R=0\) is excluded: the eddy phase is undefined there.

### Sharp critical spiral at \(F=1\)

At the bifurcation value \(F=1\),
\[
\dot s=-as-R,\qquad \dot R=2sR.
\]
For every off-axis solution \(R(0)>0\),
\[
W(s,R)=\frac12(s^2+R),\qquad \dot W=-as^2,
\]
and
\[
\boxed{tR(t)\to\frac a2,\qquad t(x(t)-1)\to-\frac12}.
\]
Consequently, for the eddy amplitude \(\rho(t)=\sqrt{y(t)^2+z(t)^2}\),
\[
\boxed{\sqrt t\,\rho(t)\to\sqrt{\frac a2}}.
\]
The exact phase identity then gives
\[
\boxed{\theta(t)-bt+\frac b2\log t
\to
\theta(0)-\frac b2\log R(0)+\frac b2\log\frac a2}.
\]
Thus the nonhyperbolic threshold is approached as a \(t^{-1/2}\) spiral with a logarithmic phase lag. On the exceptional axis \(R=0\), the eddy variables vanish identically and \(x-1\) decays exponentially.

## Proof

The complex eddy variable satisfies
\[
\dot w=((x-1)+ibx)w.
\]
Taking real and imaginary logarithmic derivatives yields
\[
\frac{\dot R}{R}=2(x-1),\qquad \dot\theta=bx,
\]
which proves the phase-amplitude identity and also shows that \(R(t)>0\) for all finite times whenever \(R(0)>0\).

For constant \(F>1\), differentiation of \(L\) gives
\[
\dot L
=s(-as+c-R)+\frac12\left(1-\frac cR\right)(2sR)
=-as^2.
\]
Because \(R-c-c\log(R/c)\to+\infty\) as either \(R\downarrow0\) or \(R\to\infty\), positive-\(R\) sublevel sets are compact in the reduced half-plane. On \(\dot L=0\) one has \(s=0\), and invariance then requires \(R=c\). LaSalle's principle gives global convergence on \(R>0\). Finally,
\[
\frac d{dt}\left(\theta-\frac b2\log\frac Rc\right)
=bx-b(x-1)=b,
\]
which proves the global phase formula.

At \(F=1\), \(W\) is nonincreasing and \(\dot W=-as^2\); the only invariant subset of \(s=0\) is \((0,0)\), hence \((s,R)\to(0,0)\). Every off-axis trajectory is eventually in \(s<0\): at \(s=0\), \(\dot s=-R<0\), while a trajectory remaining forever in \(s>0\) would have nondecreasing positive \(R\), contradicting \(R\to0\).

Set \(h=-s>0\) eventually and \(p=h/R\). Then
\[
\dot h=-ah+R,\qquad \dot R=-2hR,\qquad
\dot p+(a-2h)p=1.
\]
Since \(h(t)\to0\), comparison first bounds \(p\), and variation of constants then gives
\(p(t)\to1/a\). Therefore
\[
\frac d{dt}\frac1R=2\frac hR=2p(t)\to\frac2a.
\]
Cesàro averaging yields \(tR(t)\to a/2\), and
\[
th(t)=p(t)\,tR(t)\to\frac12.
\]
The critical phase limit follows by substituting \(tR(t)\to a/2\) into the exact phase-amplitude identity.

## Relation to prior literature

Lorenz introduced this three-variable atmospheric circulation model in 1984. In the symmetric case \(G=0\), Broer, Simó and Vitolo (2002) set
\[
u=x-1,\qquad r=y^2+z^2
\]
and obtained their reduced equation (9),
\[
\dot u=-au-r-a+aFf(t),\qquad \dot r=2ur.
\]
They also proved that, in the autonomous \(F>1\) case, the reduced equilibrium
\((u,r)=(0,a(F-1))\) is the unique global attractor.

Immediately after defining \(r=y^2+z^2\), their printed equation (10) reconstructs the Cartesian eddy components using \(r(t)\) itself as amplitude and a constant angular law. Read literally with the preceding definition of \(r\), that formula is not an identity for the displayed Lorenz-84 ODE. Direct complex-coordinate reconstruction gives the formula proved above: the Cartesian amplitude is \(\sqrt r\), and the phase contains the logarithmic amplitude correction. The corrected relation retains the parameter-independent phase advance over a periodic reduced orbit while supplying the full transient phase geometry.

The checked literature through the present includes the original model, the 1995 global bifurcation study of Shil'nikov--Nicolis--Nicolis, the 2002 Broer--Simó--Vitolo analysis, later stability/bifurcation studies, and work on nonautonomous Lorenz-84 attractors. Exact and synonymous searches for Lorenz-84 isochrons, asymptotic phase, logarithmic phase-amplitude reconstruction, and the critical \(t^{-1/2}\) law did not locate a prior statement of the theorem package above.

## Originality and limitations

Originality is **to the best of our knowledge**. The \(G=0\) reduction, the Hopf threshold at \(F=1\), and global attraction of the autonomous reduced \(F>1\) equilibrium are prior results and are not claimed as new.

The contribution claimed here is the exact phase-amplitude reconstruction, the resulting explicit global isochrons for the full three-dimensional \(F>1\) flow, and the sharp off-axis critical asymptotics at \(F=1\), including the logarithmic phase lag. The observation also corrects the printed full-state reconstruction following the otherwise valid reduced equations in Broer--Simó--Vitolo (2002).

Residual priority risk remains because the identity is elementary once complex eddy coordinates are introduced. Older Lorenz-84 literature includes K. Homan's 1998 master's thesis and the 1992 work of Masoller, Sicardi Schifino and Romanelli; their complete texts were not fully inspected here. The 1995 Shil'nikov--Nicolis--Nicolis paper was inspected at the model/bifurcation level and focuses on global bifurcation structure rather than this exact \(G=0\) phase reconstruction. Later nonautonomous work establishes attractors but does not, in the checked material, state this phase law. These sources remain residual rather than concrete evidence of prior coverage.

The theorem requires \(G=0\). Global isochrons additionally require constant \(F>1\); the critical asymptotics require constant \(F=1\). Phase is undefined on the invariant axis \(y=z=0\). No claim is made about the chaotic \(G\ne0\) regime.

## References

1. E. N. Lorenz, *Irregularity: a fundamental property of the atmosphere*, Tellus A **36A** (1984), 98--110. https://doi.org/10.1111/j.1600-0870.1984.tb00230.x
2. A. Shil'nikov, G. Nicolis and C. Nicolis, *Bifurcation and predictability analysis of a low-order atmospheric circulation model*, International Journal of Bifurcation and Chaos **5** (1995), 1701--1711. https://doi.org/10.1142/S0218127495001253
3. H. Broer, C. Simó and R. Vitolo, *Bifurcations and strange attractors in the Lorenz-84 climate model with seasonal forcing*, Nonlinearity **15** (2002), 1205--1267. https://doi.org/10.1088/0951-7715/15/4/312
4. M. Anguiano and T. Caraballo, *Asymptotic behaviour of a non-autonomous Lorenz-84 system*, Discrete and Continuous Dynamical Systems **34** (2014), 3901--3920. https://doi.org/10.3934/dcds.2014.34.3901
5. H. Wang, Y. Yu and G. Wen, *Dynamical Analysis of the Lorenz-84 Atmospheric Circulation Model*, Journal of Applied Mathematics (2014), 296279. https://doi.org/10.1155/2014/296279
