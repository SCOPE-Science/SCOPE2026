# Exact recurrence balances and a strict period floor for the Moore--Spiegel oscillator

Consider the Moore--Spiegel oscillator
\[
\dot x=y,\qquad
\dot y=z,\qquad
\dot z=-z-(T-R+Rx^2)y-Tx,
\tag{1}
\]
with real parameters \(T,R\). Equivalently,
\[
x'''+x''+(T-R+Rx^2)x'+Tx=0.
\tag{2}
\]

The results below give exact constraints on every compact recurrent statistical state, a global recurrence obstruction for \(T\le 0\), and a sharp parameter-only lower bound for the period of every nonconstant cycle.

## Theorem

Define
\[
\mathcal F
=xz+xy-\frac12y^2+\frac{T-R}{2}x^2+\frac R4x^4
\]
and
\[
\mathcal G
=yz+\frac12y^2+\frac T2x^2.
\]
Along every classical solution of (1),
\[
\boxed{\dot{\mathcal F}=y^2-Tx^2}
\tag{3}
\]
and
\[
\boxed{\dot{\mathcal G}
=z^2+(R-T)y^2-Rx^2y^2}.
\tag{4}
\]

Consequently:

1. **Invariant-measure balance.** For every compactly supported invariant probability measure \(\mu\),
   \[
   \boxed{\int y^2\,d\mu=T\int x^2\,d\mu},
   \tag{5}
   \]
   and
   \[
   \boxed{\int z^2\,d\mu+(R-T)\int y^2\,d\mu
   =R\int x^2y^2\,d\mu}.
   \tag{6}
   \]
   When \(T\ne0\), one also has
   \[
   \int x\,d\mu=\int y\,d\mu=\int z\,d\mu=0.
   \tag{7}
   \]

2. **Complete compact-recurrence obstruction for \(T\le0\).**
   If \(T<0\), the only compactly supported invariant probability measure is
   \(\delta_{(0,0,0)}\). Every bounded forward solution converges to the origin.
   If \(T=0\), every compactly supported invariant probability measure is supported
   on the equilibrium line
   \[
   \mathcal E_0=\{(x,0,0):x\in\mathbb R\},
   \tag{8}
   \]
   and every bounded forward solution converges to a single point of \(\mathcal E_0\).
   Hence no bounded non-equilibrium recurrent dynamics exists for \(T\le0\).

3. **Nonlinear-damping excursion forced by recurrence.**
   Suppose \(R>T>0\), and let \(\mu\) be any compactly supported invariant
   probability measure not concentrated at the origin. Then
   \[
   \frac{\int x^2y^2\,d\mu}{\int y^2\,d\mu}
   =
   1-\frac TR+
   \frac{\int z^2\,d\mu}{R\int y^2\,d\mu}
   >1-\frac TR.
   \tag{9}
   \]
   Therefore the support of \(\mu\) intersects
   \[
   \boxed{|x|>\sqrt{1-T/R}}.
   \tag{10}
   \]
   The threshold is exactly where the effective damping coefficient
   \(T-R+Rx^2\) changes sign.

4. **Sharp period floor.**
   Every nonconstant periodic solution has \(T>0\). If \(P\) is its minimal period,
   \[
   \boxed{P\ge\frac{2\pi}{\sqrt T}}.
   \tag{11}
   \]
   If \(R\ne0\), the inequality is strict:
   \[
   \boxed{P>\frac{2\pi}{\sqrt T}}.
   \tag{12}
   \]
   For \(R=0\), equality is attained by the harmonic family
   \(x(t)=A\cos(\sqrt T\,t)+B\sin(\sqrt T\,t)\), so the constant in (11)
   is sharp in the Moore--Spiegel parameter family.

## Proof

### Exact balances

Differentiate \(\mathcal F\), substitute (1), and collect terms:
\[
\begin{aligned}
\dot{\mathcal F}
&=yz+x\dot z+y^2+xz-yz
 +(T-R)xy+Rx^3y\\
&=y^2+x[-z-(T-R+Rx^2)y-Tx]+xz+(T-R)xy+Rx^3y\\
&=y^2-Tx^2.
\end{aligned}
\]
Likewise,
\[
\begin{aligned}
\dot{\mathcal G}
&=z^2+y\dot z+yz+Txy\\
&=z^2-(T-R+Rx^2)y^2\\
&=z^2+(R-T)y^2-Rx^2y^2.
\end{aligned}
\]
A standalone symbolic check is included in `artifacts/verify_identities.py`.

### Invariant measures

For a compactly supported invariant probability measure, the integral of the
Lie derivative of any smooth function is zero. Applying this to
\(\mathcal F\) and \(\mathcal G\) gives (5) and (6).

Also,
\[
Lx=y,\qquad Ly=z,\qquad L(x^3/3)=x^2y.
\]
Hence their invariant averages vanish. Averaging the third equation of (1) then gives
\[
0=-T\int x\,d\mu
\]
because the averages of \(z\), \(y\), and \(x^2y\) vanish. This proves (7).

If \(T<0\), (5) reads
\[
\int y^2\,d\mu+|T|\int x^2\,d\mu=0,
\]
so \(x=y=0\) almost everywhere and invariance forces \(z=0\). Thus
\(\mu=\delta_0\).

If \(T=0\), (5) gives \(y=0\) almost everywhere. Invariance then forces
\(z=0\), so the invariant measure is supported on the equilibrium line (8).

### Bounded forward dynamics for \(T\le0\)

For \(T<0\), (3) gives
\[
\dot{\mathcal F}=y^2+|T|x^2\ge0.
\]
On a bounded forward solution, \(\mathcal F\) is bounded. Therefore
\[
\int_0^\infty (y^2+|T|x^2)\,dt<\infty.
\]
The vector field and the state are bounded on that trajectory, so the relevant
derivatives are uniformly continuous. Standard Barbalat-type reasoning gives
\(x(t),y(t)\to0\). Since \(y'=z\), \(y(t)\to0\), and \(z'\) is bounded,
one also obtains \(z(t)\to0\).

For \(T=0\), (3) yields \(\int_0^\infty y^2dt<\infty\), hence \(y(t)\to0\).
Equation (4) becomes
\[
\dot{\mathcal G}=z^2+R(1-x^2)y^2.
\]
Boundedness of \(x\) and \(\mathcal G\), together with \(y\in L^2\), implies
\(z\in L^2\); uniform continuity then gives \(z(t)\to0\).

At \(T=0\) there is additionally the exact first integral
\[
\boxed{K=z+y-R\left(x-\frac{x^3}{3}\right)}.
\tag{13}
\]
For \(R\ne0\), since \(y,z\to0\), the cubic
\(x-x^3/3\) has a limit. A bounded continuous trajectory can then eventually
remain near only one root of the corresponding cubic level set, hence \(x(t)\)
converges. For \(R=0\), \(z'=-z\) and boundedness of \(x\) directly implies
that \(y\to0\) with integrable tail and \(x\) converges. The limit is a point
of (8).

### Forced excursion for \(R>T>0\)

For a nontrivial invariant measure, \(\int y^2d\mu>0\); otherwise invariance
would force the measure to be \(\delta_0\). Similarly \(\int z^2d\mu>0\).
Rearranging (6) gives (9). The left side is the \(y^2d\mu\)-weighted average
of \(x^2\), so it cannot exceed the essential supremum of \(x^2\) on the
support. The strict inequality in (9) therefore implies (10).

### Period floor

Let \(x(t)\) be a nonconstant periodic solution of minimal period \(P\).
Integrating (3) over one period gives
\[
\int_0^P y^2dt=T\int_0^P x^2dt.
\tag{14}
\]
Thus \(T>0\). Periodicity gives
\[
\overline y=\overline z=0,\qquad
\overline{x^2y}=\frac1{3P}[x^3]_0^P=0.
\]
Averaging the third equation of (1), and using \(T>0\), yields
\[
\overline x=0.
\]
The sharp Wirtinger inequality for the mean-zero \(P\)-periodic function \(x\)
therefore gives
\[
\int_0^P y^2dt
\ge\left(\frac{2\pi}P\right)^2\int_0^P x^2dt.
\]
Together with (14), this proves (11).

Equality in Wirtinger's inequality requires
\[
x(t)=A\cos(\sqrt T\,t)+B\sin(\sqrt T\,t).
\]
Substitution into (2) leaves
\[
R(x^2-1)x'=0.
\]
For \(R\ne0\), no nonconstant harmonic function satisfies this identity, so
equality is impossible and (12) follows. If \(R=0\), (2) factors as
\[
(D+1)(D^2+T)x=0,
\]
and the displayed harmonic family attains equality.

## Context and originality

Moore and Spiegel introduced the oscillator in 1966 in a model of overstable
convection and reported periodic and aperiodic behavior. Baker, Moore and
Spiegel (1971) developed analytical and numerical approximations for periodic
solutions and their stability. Marzec and Spiegel (1980) connected the
aperiodicity to strange attractors and averaging. Balmforth and Craster (1997)
mapped period-doubling, saddle-node and homoclinic bifurcations and used
explicit unstable periodic-orbit expansions; their published period tables are
consistent with (11)--(12). Later work treated generalized Moore--Spiegel
equations, multistability, topology, and control.

The inspected literature did not yield the exact balances (3)--(6), the
classification of compact recurrence for \(T\le0\), the support threshold (10),
or the global strict period floor (12). This originality assessment is to the
best of our knowledge, not a claim of exhaustive literature coverage.
The full text of Baker--Moore--Spiegel (1971), a particularly relevant source
for periodic solutions, was not inspected and remains the principal coverage
risk. The full text of Letellier--Malasoma (2014) was also not inspected; its
available abstract concerns topology and parity in generalized equations.

## Limitations

- The invariant-measure statements assume compact support.
- The convergence theorem for \(T\le0\) is conditional on forward boundedness;
  it does not claim all initial data are bounded. For \(T<0\), the origin can be
  unstable even though every bounded forward orbit converges to it.
- The excursion threshold (10) requires \(R>T>0\).
- The period theorem constrains existing cycles; it does not assert their
  existence for \(R\ne0\).
- Originality is to the best of our knowledge, with the inaccessible-source
  risks stated above.

## References

1. D. W. Moore and E. A. Spiegel, "A thermally excited non-linear oscillator,"
   *Astrophysical Journal* 143 (1966), 871--887.
   https://doi.org/10.1086/148562
2. N. H. Baker, D. W. Moore and E. A. Spiegel, "Aperiodic behaviour of a
   nonlinear oscillator," *Quarterly Journal of Mechanics and Applied
   Mathematics* 24 (1971), 391--422.
   https://ui.adsabs.harvard.edu/abs/1971QJMAM..24..391B/abstract
3. C. J. Marzec and E. A. Spiegel, "Ordinary Differential Equations with
   Strange Attractors," *SIAM Journal on Applied Mathematics* 38 (1980),
   403--421. https://doi.org/10.1137/0138034
4. N. J. Balmforth and R. V. Craster, "Synchronizing Moore and Spiegel,"
   *Chaos* 7 (1997), 738--752. https://doi.org/10.1063/1.166271
5. C. Letellier and J.-M. Malasoma, "Universalities in the chaotic generalized
   Moore & Spiegel equations," *Chaos, Solitons & Fractals* 69 (2014), 40--49.
   https://doi.org/10.1016/j.chaos.2014.09.002
6. E. Igra, "Removable dynamics in the Nose-Hoover and Moore-Spiegel
   Oscillators," arXiv:2409.16624 (2024).
   https://arxiv.org/abs/2409.16624
