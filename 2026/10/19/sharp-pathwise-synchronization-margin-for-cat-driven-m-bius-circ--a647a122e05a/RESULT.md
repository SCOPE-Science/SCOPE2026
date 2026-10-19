# Sharp pathwise synchronization margin for cat-driven Möbius circle maps

## Finding

Consider a circle map with a possibly nonperiodic real input,
\[
 f_d(x)=x+d-\phi_\varepsilon(x)\pmod 1,\qquad
 \phi_\varepsilon(x)=\frac1\pi\operatorname{Arg}(1+\varepsilon e^{2\pi i x}),
 \quad 0<\varepsilon<1.
\]
For any bi-infinite sequence of inputs satisfying \(|d_n|\le q\), put
\[
 \delta=\frac{\arcsin\varepsilon}{\pi},\quad
 0<q<\delta,\quad
 v=\arcsin\left(\frac{\sin(\pi q)}{\varepsilon}\right),\quad
 p=\frac{\pi q+v}{2\pi},\quad
 r=\frac{\pi q+\pi-v}{2\pi}.
\]
The disjoint arcs \(I=[-p,p]\) and \(J=[r,1-r]\), understood modulo one, satisfy \(0<q<p<r<1/2\). Every permitted \(f_d\) maps \(I\) into itself, and its inverse maps \(J\) into itself. There exist unique entire sequences \(a_n\in I\) and \(b_n\in J\) with \(a_{n+1}=f_{d_n}(a_n)\) and \(b_{n+1}=f_{d_n}(b_n)\). In every fiber, every initial condition other than \(b_0\) converges exponentially in circular distance to \(a_n\) as \(n\to\infty\); the unique excluded forward trajectory is \(b_n\).

The common forward Lipschitz factor on \(I\), and inverse Lipschitz factor on \(J\), is the exact and sharp number
\[
 K(q,\varepsilon)=\exp\!\left[-2\operatorname{arcosh}\!\left(\frac{\cos(\pi q)}{\sqrt{1-\varepsilon^2}}\right)\right]<1.
\]
In particular, for \(x,y\in I\), \(|f_{d_{n-1}}\circ\cdots\circ f_{d_0}(x)-f_{d_{n-1}}\circ\cdots\circ f_{d_0}(y)|\le K^n|x-y|\), using the displayed lifts; the same inequality holds for backward dynamics on \(J\). The bound is optimal uniformly across all permitted input sequences.

For the cat-map skew product on \(\mathbb T^2\times\mathbb T^1\),
\[
 (t,s,x)\longmapsto\left(2t+s,t+s, f_{c+\mu\sin(2\pi t+\alpha)}(x)\right)\pmod1,
\]
\(|c|+|\mu|<\delta\) implies the existence of two disjoint *continuous invariant graphs* over the entire driving torus. The attracting graph has all remaining points of every fiber in its forward basin, and the repelling graph is the exact exceptional set. This is a sufficient, not a claimed necessary, parameter condition for the cat-forced map.

The strict inequality \(q<\delta\) is the maximal *uniform worst-case* bound over arbitrary input sequences: at \(q=\delta\), an admissible constant input has a parabolic fixed point and no attracting/repelling hyperbolic pair; for every \(q>\delta\), an admissible constant input is elliptic. The deterioration of the optimal bound at this edge is exactly
\[
 -\log K(q,\varepsilon)
 =2\sqrt{\frac{2\pi\varepsilon}{\sqrt{1-\varepsilon^2}}}\sqrt{\delta-q}
 +O_\varepsilon((\delta-q)^{3/2}).
\]
For \(q=0\), the analogous conclusions hold with singleton arcs \(I=\{0\}\), \(J=\{1/2\}\) and factor \((1-\varepsilon)/(1+\varepsilon)\).

## Assumptions and scope

All circle maps are orientation-preserving smooth diffeomorphisms; the principal argument in \(\phi_\varepsilon\) is unambiguous because \(1+\varepsilon\cos(2\pi x)>0\). The real input sequence can be arbitrarily chosen and correlated; no probability law, ergodicity or regularity in time is assumed. Exponential convergence means for each nonexceptional initial point there are finite constants \(C>0\) and \(\rho<1\), potentially depending on the initial point and driving sequence, such that the circular distance to \(a_n\) is bounded by \(C\rho^n\). The stronger sharp uniform factor \(K\) applies immediately on \(I\), or backward on \(J\), rather than as a single uniform bound for arbitrary initial points outside these arcs.

## Proof

**1. Exact fixed-point barriers.** The odd, one-periodic correction \(\phi_\varepsilon\) is positive on \((0,1/2)\), vanishes at its endpoints, and has a unique maximum \(\delta=\arcsin(\varepsilon)/\pi\). Differentiating gives
\[
 \phi_\varepsilon'(x)=\frac{2\varepsilon(\varepsilon+\cos 2\pi x)}{1+2\varepsilon\cos 2\pi x+\varepsilon^2},\qquad
 f_d'(x)=\frac{1-\varepsilon^2}{1+2\varepsilon\cos 2\pi x+\varepsilon^2}>0.
\]
Solving \(\phi_\varepsilon(x)=q\) by \(\varepsilon\sin(2\pi x-\pi q)=\sin(\pi q)\) gives exactly \(p,r\) displayed above. Since \(\phi_\varepsilon(x)<x\) for \(0<x\le1/2\) (the positive argument of \(1+\varepsilon e^{2\pi ix}\) is strictly below \(\pi x\)), \(p>q\). The two solutions lie strictly before and after the unique maximum, hence \(p<r\). Thus \(f_q(p)=p\), \(f_{-q}(-p)=-p\), \(f_q(r)=r\), and \(f_{-q}(1-r)=1-r\). Monotonicity in both \(d\) and \(x\) proves \(f_d(I)\subseteq I\) and, since \(f_d(r)\le r\) and \(f_d(1-r)\ge1-r\), also \(f_d^{-1}(J)\subseteq J\). These are inclusions of real lifts and so remain valid modulo one.

**2. Sharp metric estimates.** The derivative \(f_d'(x)\) is strictly increasing with \(|x|\) on \([0,1/2]\). Its maximum on \(I\) is \(f_d'(p)\), and its minimum on \(J\) is \(f_d'(r)\). Direct substitution of the two fixed-point solutions, or the trace of the associated real-normalized Möbius matrix, gives
\[
 f_d'(p)=K(q,\varepsilon),\qquad f_d'(r)=K(q,\varepsilon)^{-1}.
\]
The mean value theorem gives the two asserted contraction bounds. They are optimal: constant input \(d=q\) fixes both \(p\) and \(r\), attaining equality in the infinitesimal Lipschitz limits. Because \(K<1\), shrinking nested images \(f_{d_{-1}}\circ\cdots\circ f_{d_{-m}}(I)\) determine the unique entire attracting trajectory, and shrinking future inverse images \(f_{d_0}^{-1}\circ\cdots\circ f_{d_{m-1}}^{-1}(J)\) determine the unique entire repelling trajectory. Every orbit remaining in \(J\) for all positive times belongs to that singleton, by the same inverse contraction argument.

**3. Global basin.** On the open gap \((p,r)\), \(\phi_\varepsilon(x)>q\); on \((-r,-p)\), \(\phi_\varepsilon(x)<-q\). For a point in \((p,r)\), monotonicity and the barrier identities give \(-p\le f_{d_n}(x)\le r\). As long as it stays outside \(I\), its lift remains in \((p,r)\) and strictly decreases. If it never enters \(I\), it must tend to \(p\), because every compact subinterval of \((p,r)\) has a strictly positive lower bound on \(\phi_\varepsilon(x)-q\). The point \(a_n\) is always at most \(p\). Choose \(\eta>0\) such that \(f_d'(x)\le\rho<1\) for all \(x\in[-p,p+\eta]\) and all admissible \(d\), possible since \(f_d'(p)=K<1\). Once the descending orbit lies below \(p+\eta\), the mean value theorem gives \(|x_{n+1}-a_{n+1}|\le\rho|x_n-a_n|\). The negative gap is handled symmetrically and the other direction of the lift. Every orbit starting outside \(I\cup J\) is thus exponentially captured by the attracting sequence. Every orbit leaving \(J\) enters one of those gaps or \(I\), while exactly one orbit remains in \(J\). This proves the complete basin claim.

**4. Continuous graphs.** On any compact invertible driving space with continuous input \(d(z)\in[-q,q]\), the preceding finite pullback compositions of \(I\) converge uniformly, at geometric rate \(K\), to a continuous graph \(a(z)\) satisfying \(a(Az)=f_{d(z)}(a(z))\). Forward compositions of inverse maps on \(J\) give a second continuous invariant graph \(b(z)\). Apply this to the cat automorphism \(A(t,s)=(2t+s,t+s)\) and its continuous forcing. Their arcs are disjoint and Step 3 determines their exact fiberwise basins.

**5. Sharpness and critical scaling.** For a constant input \(d\), the fixed-point equation is \(\phi_\varepsilon(x)=d\) modulo one. The maximum amplitude is precisely \(\delta\). At \(d=\delta\), the fixed points coalesce to a parabolic point with derivative one; for \(\delta<d<1/2\), the Möbius transformation is elliptic (no real-circle fixed points). Thus no threshold \(q\ge\delta\) uniformly guarantees a separated hyperbolic graph pair for all admissible sequences. Finally, set \(\eta=\delta-q\). Then
\[
 \frac{\cos(\pi q)}{\sqrt{1-\varepsilon^2}}
 =1+\frac{\pi\varepsilon}{\sqrt{1-\varepsilon^2}}\eta+O_\varepsilon(\eta^2),
\]
and \(\operatorname{arcosh}(1+u)=\sqrt{2u}+O(u^{3/2})\) yields the claimed square-root law.

## Verification

The standalone `checker.py` checks the exact barrier roots, differentiation identities, sharp multipliers, forward and backward strip inequalities, square-root coefficient and iterated contraction for several independent positive parameter configurations. Run `python3 checker.py`; the script reports 39,042 finite consistency checks passed. The infinite-time theorem follows from the preceding analytical contraction/barrier proof, not from simulation. No computer algebra dependency is required.

## Relationship to prior work

Chigarev, Kazakov and Pikovsky introduce exactly the cat-driven Möbius family and numerically examine its attractor–repeller separation and collision. Their Appendix A also gives the known autonomous Möbius fixed-point/rotation conjugacy boundary; the constant-input value \(\delta\) is therefore **not claimed as a new autonomous threshold**. The distinct contribution here is an explicit, pathwise uniform trapping-and-expulsion theorem valid for *every* bounded (including adversarial) driving sequence, with a sharp worst-case metric factor, a complete fiberwise basin classification, and its quantitative collapse at the robustness edge. The authors' related 2021 paper concentrates on multifractal dimensions of overlapping attractor/repeller measures for related Anosov–Möbius and Chirikov–Möbius systems, not this all-input pathwise synchronization theorem. General invariant-graph contraction principles are established theory; the calculation of this model's exact common barriers and optimal constant is the claimed specialization.

## Limitations

The condition \(|c|+|\mu|<\delta\) is not asserted necessary for synchronization under cat forcing; correlations in the driving sequence can permit larger regions. The sharpness is only worst-case across arbitrary bounded inputs, using constant-input counterexamples. Transient entry into the attracting arc is not guaranteed for all nonexceptional points, although their exponential convergence is proved. No classification of the collision or heterodimensional dynamics outside the robust region is attempted. An unindexed equivalent special-purpose contraction result or unknown supplementary calculation could affect priority. Independent external validation is not included.

## References

1. V. Chigarev, A. Kazakov and A. Pikovsky, *Attractor-repeller collision and the heterodimensional dynamics*, arXiv:2305.18172v1 (first posted 2023-05-29), Sections II–IV and Appendix A, https://arxiv.org/html/2305.18172v1.
2. V. Chigarev, A. Kazakov and A. Pikovsky, *Mutual singularities of overlapping attractor and repeller*, Chaos **31** (2021), 083127, DOI:10.1063/5.0056891, https://www.hse.ru/data/2024/05/24/2124568536/3_ChigarevKazakovPikovsky_Chaos2021.pdf.
