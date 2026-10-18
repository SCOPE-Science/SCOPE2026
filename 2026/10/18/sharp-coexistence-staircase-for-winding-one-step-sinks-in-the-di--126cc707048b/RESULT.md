# Sharp coexistence staircase for winding-one-step sinks in the dissipative standard map

## Finding
Consider the dissipative kicked-rotor map \(F_{b,K}:\mathbb T\times\mathbb R\to\mathbb T\times\mathbb R\), where \(\mathbb T=\mathbb R/(2\pi\mathbb Z)\), defined by
\[
p'=bp+K\sin\theta,\qquad F_{b,K}(\theta,p)=(\theta+p'\pmod{2\pi},\,p').
\]
Assume \(0<b<1\) and \(K>0\). A *winding-\(m\) period-one orbit* is a fixed point on the cylinder whose angular lift increases by \(2\pi m\), where \(m\in\mathbb Z\). Let \(N_b(K)\) denote the number of **hyperbolic attracting** period-one orbits, counted as distinct points on the cylinder, irrespective of their winding.

**Exact individual mode criterion.** For each \(m\in\mathbb Z\), there is exactly one hyperbolic attracting fixed point of winding \(m\) if and only if
\[
4\pi^2(1-b)^2m^2<K^2<4\pi^2(1-b)^2m^2+4(1+b)^2.
\]
Outside this strict interval, there is no hyperbolic attracting fixed point of that winding. The attracting point, when present, satisfies \(p=2\pi m\), \(\sin\theta=2\pi(1-b)m/K\), and \(\cos\theta<0\).

**Exact coexistence staircase.** Define \(t=K^2/[4\pi^2(1-b)^2]\) and \(W=(1+b)^2/[\pi^2(1-b)^2]\). Then
\[
N_b(K)=\sum_{m\in\mathbb Z}\mathbf1_{\{m^2<t<m^2+W\}}.
\]
Consequently the sharp maximum over all positive forcing strengths is
\[
\boxed{\sup_{K>0}N_b(K)=\max\left\{2\bigl(\lceil\sqrt{W+1}\rceil-1\bigr),\quad2\lceil\sqrt W\rceil-1\right\}.}
\]
The supremum is an **attained integer maximum**. For every positive integer \(q\), at least \(2q\) simultaneous sinks are attainable exactly when \(W>q^2-1\), and at least \(2q+1\) are attainable exactly when \(W>q^2\). Equality in either positive threshold does **not** suffice. The maximal count diverges as \(b\uparrow1\), with
\[
\max_{K>0}N_b(K)\sim\frac{2(1+b)}{\pi(1-b)}\sim\frac4{\pi(1-b)}.
\]

## Assumptions and scope
The angular coordinate is taken modulo \(2\pi\), but momentum \(p\) is not reduced modulo \(2\pi\). Thus different integer winding numbers label genuinely different cylinder fixed points. The sinusoidal forcing has zero added constant torque, the dissipation multiplier lies strictly between zero and one, and the statement concerns **hyperbolic attracting fixed points only**, not higher-period sinks, neutral fixed points, chaotic attractors, basin areas, or all invariant measures. At a stability equality the relevant multiplier is \(+1\) or \(-1\), and the point is not included in \(N_b(K)\), regardless of possible nonlinear one-sided stability.

## Proof
Write \(p'=bp+K\sin\theta\). A fixed point on the cylinder with angular lift increment \(2\pi m\) must have \(p'=p=2\pi m\). Hence
\[
K\sin\theta=2\pi(1-b)m.
\]
Set \(d_m=2\pi(1-b)m\). If \(K<|d_m|\), there is no such point; if \(K=|d_m|\), the angular solution has zero cosine; if \(K>|d_m|\), there are exactly two angular solutions, distinguished by the sign of cosine.

The derivative at any such point, with \(c=K\cos\theta\), is
\[
J=\begin{pmatrix}1+c&b\\c&b\end{pmatrix},\qquad
\det J=b,\qquad\operatorname{tr}J=1+b+c.
\]
The characteristic polynomial is \(\lambda^2-(1+b+c)\lambda+b\). The second-order strict Schur inequalities are \(1-b>0\), \(1-\operatorname{tr}J+b=-c>0\), and \(1+\operatorname{tr}J+b=2(1+b)+c>0\). Thus both multipliers have modulus strictly less than one exactly when
\[
-2(1+b)<c<0.
\]
The positive-cosine solution never satisfies this inequality. For the negative-cosine solution \(c=-\sqrt{K^2-d_m^2}\), and the inequality is exactly \(0<K^2-d_m^2<4(1+b)^2\). This proves the mode criterion and uniqueness. At the lower boundary the characteristic polynomial has root \(+1\); at the upper boundary it has root \(-1\). Because the determinant is \(b\in(0,1)\), the strict Schur conditions characterize all hyperbolic attracting fixed points.

Dividing the mode criterion by \(4\pi^2(1-b)^2\) gives \(m^2<t<m^2+W\). Only finitely many \(m\) satisfy this at any fixed \(t>0\). For each \(q\ge1\), simultaneously including both windings \(\pm1,\ldots,\pm q\), but not requiring zero, means choosing \(t\) in the nonempty open interval
\[
(q^2,1+W),
\]
which is possible exactly when \(q^2-1<W\). More generally, any \(q\) distinct positive winding integers have their largest and smallest squares separated by at least \(q^2-1\); therefore this threshold is also **necessary** for any collection of \(2q\) nonzero winding sinks.

Including zero and the \(2q\) nonzero windings \(\pm1,\ldots,\pm q\) requires \(q^2<t<W\). Thus \(2q+1\) sinks including the zero mode are possible exactly when \(q^2<W\). If an odd count \(2q+1\) is obtained without zero, the count is in fact even by winding symmetry, hence at least \(2q+2\), which forces \(W>(q+1)^2-1>q^2\) by the preceding necessity bound. Consequently \(W>q^2\) is necessary and sufficient for **at least** \(2q+1\) sinks, even if the selected forcing does not include zero.

Define the largest integers \(P=\max\{q\ge1:q^2-1<W\}\) and \(Z=\max\{q\ge0:q^2<W\}\); these exist and satisfy
\[
P=\lceil\sqrt{W+1}\rceil-1,\qquad Z=\lceil\sqrt W\rceil-1.
\]
Here \(P\ge1\) since \(W>0\), and the zero-only option corresponds to \(Z=0\). Since all nonzero winding modes occur in symmetric pairs, every possible sink count is bounded by \(\max\{2P,2Z+1\}\). The two constructive open intervals above attain \(2P\) and \(2Z+1\), respectively, except that the latter with \(Z=0\) is achieved by any \(0<t<\min\{W,1\}\). Hence the maximum formula is exact and attained. The asymptotic follows from \(P=\sqrt W+O(1)\), \(Z=\sqrt W+O(1)\), and \(\sqrt W=(1+b)/[\pi(1-b)]\).

## Verification
The standalone `verify.py` checks the Jacobian trace and determinant algebra, the two strict Schur factors, all equality boundaries, and the exact integer-window maximum against complete interval-endpoint enumeration for a set of rational widths (including exact-square thresholds), plus independent floating-point spot checks in the original map. Running `python3 verify.py` produces `VERIFY_OK`. The proof above—not the finite checks—establishes the assertions for all real \(b\in(0,1)\) and \(K>0\).

## Relationship to prior work
Zaslavsky's 1978 paper derives a dissipative kicked map and analyzes strange-attractor formation; it does not state the simultaneous attracting-winding count. Schmidt and Wang (1985), Wenzel, Biham and Jayaprakash (1991), and Celletti and Di Ruzza (2011) study the dissipative standard map, periodic orbits, and mode-locking tongues. Wenzel and collaborators emphasize numerical periodic-orbit diagrams and Arnold-tongue scaling. Celletti and Di Ruzza construct periodic orbits and parametrize drift intervals for a given period. Those topics are closely related, but the **newly compared statement** here is the exact *zero-torque, all-winding, simultaneous hyperbolic fixed-point census*, sharp maximization over kick strength at fixed dissipation, and its interlaced even/odd staircase thresholds. The original full texts of the two latter studies could not be obtained in this comparison; these remain specifically identified overlap risks, and no claim of bibliographic exhaustiveness is made.

A related published analysis of the classical Zaslavsky map derives a sharp interval for mean lift transport of invariant probabilities and characterizes extremal winding fixed points. Its transport bound is a statement about invariant measures and **does not imply** the simultaneous number, strict local sink stability, or maximizing staircase proved here. The kicked-rotor model in Wells, Kath and Motter's 2015 supplement is conjugate to this map under the change of coordinates \((x,y)\mapsto(x+y,y)\) and exhibits more than one hundred numerical attractors at weak damping; their numerical discussion does not provide the exact all-parameter period-one capacity formula.

## Limitations
The optimization varies \(K>0\) while holding dissipation \(b\) fixed. Neither higher-period sink counts nor global attractor multiplicity are bounded by this formula. Positive and negative winding sinks are counted separately because momentum is unwrapped. Classical Arnold-tongue literature may contain equivalent period-one stability calculations, and unavailable full texts from 1991 and 2011 could imply some or all of the count; those are explicit remaining bibliographic risks. No independent audit has been performed.

## References
1. G. M. Zaslavsky, “The simplest case of a strange attractor,” *Physics Letters A* 69 (1978), 145–147. DOI: 10.1016/0375-9601(78)90195-0.
2. G. Schmidt and B. W. Wang, “Dissipative standard map,” *Physical Review A* 32 (1985), 2994–2999. DOI: 10.1103/PhysRevA.32.2994.
3. W. Wenzel, O. Biham and C. Jayaprakash, “Periodic orbits in the dissipative standard map,” *Physical Review A* 43 (1991), 6550–6557. DOI: 10.1103/PhysRevA.43.6550.
4. A. Celletti and S. Di Ruzza, “Periodic and quasi-periodic orbits of the dissipative standard map,” *Discrete and Continuous Dynamical Systems B* 16 (2011), 151–171. DOI: 10.3934/dcdsb.2011.16.151.
5. D. K. Wells, W. L. Kath and A. E. Motter, “Control of stochastic and induced switching in biophysical networks,” *Physical Review X* 5 (2015), 031036, §S4 of supplement. DOI: 10.1103/PhysRevX.5.031036.
6. G. M. Zaslavsky, “Zaslavsky map,” *Scholarpedia* 2(5):2662 (2007). DOI: 10.4249/scholarpedia.2662.
7. “Sharp stationary transport strip for the Zaslavsky map,” publicly available result, 2026-10-11, published source inspected in full for statement-level comparison.
