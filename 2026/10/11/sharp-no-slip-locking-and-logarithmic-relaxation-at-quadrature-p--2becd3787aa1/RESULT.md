# Sharp no-slip locking and logarithmic relaxation at quadrature phase lag

## Finding

**Theorem (two-cluster no-slip threshold).** Consider the discrete-time mean-field phase map
\[
\theta_i^{(n+1)}=\theta_i^{(n)}+\omega+\frac{K}{N}\sum_{j=1}^{N}\sin\!\big(\theta_j^{(n)}-\theta_i^{(n)}-\beta\big)\pmod{2\pi},
\]
where \(N\ge3\), \(K>0\), all natural frequencies equal the same \(\omega\), and \(\beta=\pi/2\). Fix a nontrivial two-cluster partition with \(p>q\ge1\) and \(p+q=N\), and write the phase difference from the majority cluster to the minority cluster as \(\delta\in(0,2\pi)\). Put
\[
B=K\frac{p-q}{N}>0,\qquad
F_B(\delta)=\delta+B(1-\cos\delta).
\]
Let \(t_*\in(\pi/2,\pi)\) be the unique positive solution of \(\tan(t_*/2)=t_*\), and define
\[
B_* = \frac{t_*}{1-\cos t_*}=1.380050139689300948\ldots.
\]
Then **every** nonsynchronous two-cluster state has a lifted phase difference that advances without crossing \(2\pi\) on the first step, and hence on every subsequent step, **if and only if** \(0<B\le B_*\). In this range every such orbit eventually synchronizes in phase difference: \(\delta_n\to2\pi\), with possible finite-time synchronization only at \(B=B_*\). More precisely, for every orbit that does not synchronize in finite time, there is a finite initial-condition-dependent constant \(C\) such that
\[
\boxed{\quad
\frac{1}{2\pi-\delta_n}
=\frac{B}{2}n+\frac{B}{2}\log n+C+o(1)
\quad(n\to\infty).\quad}
\]
At \(B=B_*\), the initial lifted phase difference \(\delta_*=2\pi-t_*\) reaches synchrony in one step. For every \(B>B_*\), some lifted phase differences strictly overshoot \(2\pi\) in one step; **no conclusion is asserted about their eventual dynamics**.

The phenomenon is intrinsically discrete: in the corresponding continuous-time two-cluster equation \(\dot\delta=B(1-\cos\delta)\), a trajectory approached from below has \((2\pi-\delta(t))^{-1}=(B/2)t+C+o(1)\), *without* a logarithmic term. The results concern the invariant two-cluster family; they do not assert attraction of general multicluster configurations to this family.

## Assumptions and scope

All oscillator phases are considered modulo \(2\pi\), although a distinguished representative \(\delta\in[0,2\pi]\) is used to measure ordered phase separation. Every initial configuration considered has exactly two phase values, assigned to the same groups at all iterations; identical natural frequencies make this family invariant. The group of size \(p\) is named the majority group, so \(p>q\), and hence \(B>0\). With equal cluster sizes, \(B=0\) and the relative phase is constant at \(\beta=\pi/2\); this case is excluded. Interchanging cluster names reverses the oriented coordinate and reduces the unequal-size case to the displayed convention.

The **no-slip property** means the real lift \(F_B\) sends every point of \((0,2\pi)\) into \((0,2\pi]\); it is stronger than convergence modulo \(2\pi\). When \(B=B_*\), all but the union of finite-preimage sets of the synchronizing configuration obey the stated asymptotic; initial configurations hitting synchrony in finite time are explicitly excluded from the reciprocal asymptotic.

The relevant primary classification is MSC2020 \(37E10\), maps of the circle. The motivating model was first publicly available on 2026-09-19 (arXiv:2609.22715v1).

## Proof

**1. Exact invariant reduction.** Let \(u\) and \(v\) be the majority and minority cluster phases, with \(\delta=v-u\). Because the within-cluster and cross-cluster contributions are identical for every member of a cluster, each group remains exactly synchronized internally. Subtracting its two update equations cancels the common frequency and the self-interaction phase lag:
\[
\delta'=\delta-K\cos\beta\sin\delta
+K\frac{p-q}{N}\sin\beta\,(1-\cos\delta)
\pmod{2\pi}.
\]
At \(\beta=\pi/2\), the real lift is exactly \(F_B\) above. No continuum limit, linearization, or small-coupling approximation is used.

**2. Sharp no-overshoot boundary.** For \(0<\delta<2\pi\), the strict inequality \(F_B(\delta)>\delta\) holds. The inequality \(F_B(\delta)\le2\pi\) is equivalent, after putting \(t=2\pi-\delta\), to
\[
B\le H(t):=\frac{t}{1-\cos t},\qquad 0<t<2\pi.
\]
The function \(H\) diverges at both endpoints. Its stationary points satisfy \(1-\cos t=t\sin t\). On \((\pi,2\pi)\) the left side is positive and the right side negative, so there are none. On \((0,\pi)\), division by \(2\sin(t/2)\) yields \(\tan(t/2)=t\). The function \(\tan(t/2)-t\) is negative just to the right of zero; its derivative \(\tfrac12\sec^2(t/2)-1\) changes sign exactly once at \(t=\pi/2\), and the function diverges to positive infinity at \(\pi\). Consequently there is exactly one positive zero \(t_*\), a strict global minimum \(B_*=H(t_*)\). This proves the iff statement and exhibits the equality point \(\delta_*\). For \(B>B_*\), continuity gives an open interval of \(\delta\)'s with \(F_B(\delta)>2\pi\).

**3. Convergence on the no-slip side.** When \(0<B\le B_*\), \(\delta_{n+1}\in(\delta_n,2\pi]\). Unless the orbit reaches \(2\pi\), the lifted sequence is strictly increasing, bounded, and converges to some \(L\le2\pi\). Continuity and \(F_B(L)=L\) force \(1-\cos L=0\). Since \(L>\delta_0>0\), necessarily \(L=2\pi\). For \(B<B_*\) every strict initial gap remains strict after each finite step. At \(B=B_*\), \(\delta_*\) is the only point in \((0,2\pi)\) mapping directly to \(2\pi\). Therefore every finite-hitting point is an iterated preimage of this one point; those not finite-hitting converge asymptotically.

**4. Sharp reciprocal asymptotics.** On a non-finite-hitting trajectory let \(x_n=2\pi-\delta_n>0\). Then \(x_n\downarrow0\) and the *exact* recurrence is
\[
x_{n+1}=x_n-B(1-\cos x_n).
\]
Taylor's formula with a uniform local remainder yields
\[
1-\cos x=\frac{x^2}{2}-\frac{x^4}{24}+O(x^6),
\quad
x_{n+1}=x_n\left(1-\frac{B}{2}x_n+\frac{B}{24}x_n^3+O(x_n^5)\right).
\]
For \(y_n=1/x_n\), expansion of the reciprocal gives
\[
y_{n+1}-y_n=\frac{B}{2}+\frac{B^2}{4y_n}+O(y_n^{-2}).
\]
Because the increment tends to \(B/2>0\), Stolz--Cesàro (or summing the difference equation) gives \(y_n/n\to B/2\). Substitution then yields \(y_n=Bn/2+O(\log n)\), whence
\[
\frac{1}{y_n}=\frac{2}{Bn}+O\!\left(\frac{\log n}{n^2}\right).
\]
Thus the increments of \(y_n-(B/2)n-(B/2)\log n\) are absolutely summable: the leading harmonic term from \(B^2/(4y_n)\) cancels the logarithmic increment, and all remaining terms are \(O((\log n)/n^2)\). The claimed finite limit \(C\) follows, including the \(o(1)\) error. This argument is an infinite-orbit proof, not extrapolation of finite numerical data.

**5. Contrast with the flow.** For \(\dot x=-B(1-\cos x)\), direct differentiation shows \(\frac{d}{dt}\cot(x/2)=B\). Therefore \(\cot(x(t)/2)=Bt+\cot(x(0)/2)\). The expansion \(\cot(x/2)=2/x+O(x)\) gives the stated flow asymptotic and demonstrates that the discrete logarithmic term is not a continuous-time coefficient.

## Verification

Run `python3 verify.py` from the extracted package directory. The verifier uses only the Python standard library. It independently evaluates the original finite-oscillator update for several unequal cluster partitions and phases, checks the exact one-variable reduction, computes the unique threshold root by bisection, tests the no-overshoot boundary on a dense deterministic sample, and checks numerical stabilization of the logarithm-subtracted asymptotic. It reports **4,148 passing finite diagnostics**. These finite tests are sanity checks only. The proof above, including the global minimum and summable remainder, supplies the universal quantifiers.

## Relationship to prior work

Gade and Gupta (2026, arXiv:2609.22715v1) define the exact discrete-time phase-lag mean-field map and analyze instability of the incoherent state in the Lorentzian-frequency continuum limit; their explicit formulas and numerical studies do not provide this unequal two-cluster no-slip threshold or discrete logarithmic law. Gong, Zheng, Toenjes and Pikovsky (2018/2019, arXiv:1812.05883v2, especially Sec. III.2) derive the **continuous-time** two-cluster phase-difference drift and investigate noise and transverse cluster stability; the continuous drift is prior work, not a new derivation claimed here. The standard sine-circle-map literature already provides the general class of maps to which the reduction belongs, and classical parabolic iteration theory explains the *type* of algebraic decay. The contribution assessed here is the exact sharp non-winding boundary and full-orbit second-order discrete relaxation formula along the particular physically parametrized quadrature two-cluster subfamily. No inspected primary result was found to imply this combined specialization; priority remains subject to the explicitly stated literature risk.

## Limitations

The proof is restricted to identical frequencies, equal global coupling, the quadrature phase lag \(\beta=\pi/2\), and the invariant family of two unequal clusters. It does not show transverse attraction of that family in the full phase space, and it does **not** classify orbit behavior after an overshoot when \(B>B_*\). The sharpness refers exclusively to the stated no-slip property, not to a supposed global synchronization threshold. A classical sine-circle-map source might contain an equivalent specialization not detected in the searches.

## References

1. P. M. Gade and S. Gupta, *Discrete-time Kuramoto model with phase lag: Linear stability analysis and onset of synchronization*, arXiv:2609.22715v1 (first public version 2026-09-19), https://arxiv.org/html/2609.22715.
2. C. C. Gong, C. Zheng, R. Toenjes, and A. Pikovsky, *Repulsively Coupled Kuramoto-Sakaguchi Phase Oscillators Ensemble Subject to Common Noise*, arXiv:1812.05883v2, https://arxiv.org/html/1812.05883v2, especially Sec. III.2.
3. E. W. Weisstein, *Circle Map*, MathWorld, https://mathworld.wolfram.com/CircleMap.html (standard family definition; background only).
4. J. C. Canille Martins, L. R. Domínguez and J. Raissy, *Parametrization of unstable manifolds and Fatou disks for parabolic skew-products*, Complex Analysis and its Synergies (2018), https://link.springer.com/article/10.1186/s40627-018-0011-3 (general parabolic background; not a source for the finite-population threshold).
