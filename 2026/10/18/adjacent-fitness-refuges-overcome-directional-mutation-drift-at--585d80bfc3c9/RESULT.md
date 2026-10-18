# Adjacent fitness refuges overcome directional mutation drift at an exact threshold

## Finding
For the frequency-independent nearest-neighbor mutation–selection logistic system on all integer traits, two adjacent advantageous sites can support a unique positive summable equilibrium in a range of advantages for which a single advantageous site cannot support any such equilibrium, no matter how large the birth rate. The exact two-site and one-site thresholds, positive equilibrium, and an example are given below.

## Assumptions and scope
Let \(p,q>0\), \(p+q=1\), \(\mu>0\), \(0<\delta<\mu\), and \(\lambda>0\). Traits are \(i\in\mathbb Z\), densities are \(x_i\ge0\), and \(m=\sum_{i\in\mathbb Z}x_i\le1\). The evolution equation is
\[
\dot x_i=\lambda(1-m)(p x_{i-1}+q x_{i+1})-\mu_i x_i.
\]
For the **adjacent-refuge model**, \(\mu_0=\mu_1=\mu-\delta\) and every other \(\mu_i=\mu\). For the **single-refuge comparison**, only \(\mu_0=\mu-\delta\). Equilibria are nonnegative \(\ell^1(\mathbb Z)\) vectors, with strictly positive total mass. There is no spatial boundary or finite-trait truncation.

Set \(v=|p-q|\), \(w=2\sqrt{pq}=\sqrt{1-v^2}\), and
\[
\delta_2=\frac{\mu}{2}(1+v-w),\qquad \delta_1=\mu v.
\]
The adjacent-refuge system has a nonzero summable equilibrium if and only if
\[
\delta>\delta_2\quad\text{and}\quad\lambda>a_2,
\qquad a_2=\frac{\mu-2\delta+\sqrt{\mu^2+4\delta(\mu-\delta)}}{4\sqrt{pq}}.
\]
When it exists this equilibrium is unique. To give it explicitly put
\[
t=2\sqrt{pq}\,a_2,\quad z=\frac{\mu-\sqrt{\mu^2-t^2}}t,\quad
r=\sqrt{p/q}\,z,\quad s=\sqrt{q/p}\,z,\quad h=\sqrt{p/q}.
\]
Then \(0<r,s<1\), and with \(Z=(1-s)^{-1}+h(1-r)^{-1}\),
\[
x_i^*=\frac{1-a_2/\lambda}{Z}
\begin{cases}
s^{-i},&i\le0,\\
h r^{i-1},&i\ge1.
\end{cases}
\]
In the single-refuge system a nonzero summable equilibrium exists precisely if
\[
\delta>\delta_1\quad\text{and}\quad
\lambda>a_1=\frac{\sqrt{\mu^2-\delta^2}}{2\sqrt{pq}}.
\]
It is likewise unique. For \(p\ne q\), \(0<\delta_2<\delta_1\); hence every \(\delta_2<\delta\le\delta_1\) permits persistence with two adjacent refuges at sufficiently large birth rate, but forbids it with just one.

For an exact example take \(\mu=1\), \(p=3/4\), \(q=1/4\), \(\delta=2/5\), \(\lambda=1\). The two-site threshold is \((3-\sqrt3)/4\), the single-site threshold is \(1/2\), and \(a_2=8\sqrt3/15<1\). Thus the two-refuge system has positive mass \(1-8\sqrt3/15\), but the single-refuge system has no nonzero summable equilibrium for any birth rate.

## Proof
Let \(a=\lambda(1-m)\). At a nonzero nonnegative stationary \(\ell^1\) state, the stationarity equation implies \(a>0\) and strict positivity of every coordinate: a zero coordinate forces both neighboring coordinates to vanish, hence all coordinates vanish. Summation yields \(a=\sum_i\mu_i x_i/m\in(\mu-\delta,\mu)\). Outside the finitely many refuges,
\[
a(p x_{i-1}+q x_{i+1})=\mu x_i.
\]
Write \(\Delta=\sqrt{\mu^2-4a^2pq}>0\), which is real since \(a<\mu\) and \(2\sqrt{pq}\le1\). The unique decaying roots on the left and right half-lines are respectively
\[
s=\frac{\mu-\Delta}{2ap},\qquad r=\frac{\mu-\Delta}{2aq}.
\]
Every positive summable stationary profile is therefore uniquely determined by the two values \(C=x_0>0\), \(D=x_1>0\), and equals \(x_{-j}=Cs^j\) and \(x_{1+j}=Dr^j\) for all integers \(j\ge0\). Inserting these expressions at the two refuges gives
\[
BC=aqD,\qquad BD=apC,\qquad B=\frac{\mu+\Delta-2\delta}{2}.
\]
Their positivity implies \(B=a\sqrt{pq}\), \(D/C=\sqrt{p/q}\). Upon setting \(t=2a\sqrt{pq}\), this is the exact scalar condition \(\mu+\sqrt{\mu^2-t^2}-2\delta=t\). Since \(0<\delta<\mu\), its unique positive root is
\[
t=\frac{\mu-2\delta+\sqrt{\mu^2+4\delta(\mu-\delta)}}2.
\]
Indeed the original equation is strictly decreasing in \(t\in(0,\mu)\), and squaring it produces only this root in the admissible interval (the other quadratic root is negative). Summability holds exactly when both decaying roots are less than one. If \(p>q\), the restrictive root is \(r\), which reaches one exactly at \(a=\mu\); the analogous restrictive root is \(s\) when \(q>p\). For \(p=q\), both roots reach one at \(a=\mu\). In all cases the condition is \(a_2<\mu\). Substitution of \(a_2=\mu\) in the scalar matching condition (using \(\Delta=\mu v\)) yields \(\delta=\delta_2\); strict monotonicity yields \(a_2<\mu\) precisely for \(\delta>\delta_2\). The positive profile is then summable with the displayed \(Z\).

Finally, \(m=1-a_2/\lambda\) fixes the normalization. This is strictly positive exactly when \(\lambda>a_2\). The profile satisfies every recurrence and both matching conditions, so it is an equilibrium, and all earlier steps force uniqueness.

For a single refuge, the same tail recurrence and its central equation \(a(ps+qr)=\mu-\delta\) reduce exactly to \(\Delta=\delta\), giving \(a_1=\sqrt{\mu^2-\delta^2}/(2\sqrt{pq})\). Summability of both tails requires \(a_1<\mu\), equivalently \(\delta>\mu v\). Normalization again requires \(\lambda>a_1\) and yields uniqueness. If \(v>0\), then \(\delta_2<\delta_1\) follows from \(1-v<\sqrt{1-v^2}\), while \(\delta_2>0\). This proves the strict rescue window. All threshold equalities are excluded: the restrictive tail has root one at the localization boundary, and total mass vanishes at the birth boundary.

## Verification
The companion `verify.py` independently checks algebraic expressions with symbolic arithmetic and evaluates the exact infinite-shape recurrence at 41 integer sites for the example. It checks the strict rescue inequalities and verifies the analytic formulas across several rational parameter choices. The executable checks are finite diagnostics; the statements for all integer traits follow from the recurrence proof above. Run `python verify.py` after installing packages in `requirements.txt`.

## Relationship to prior work
Pollett (2026) gives the mutation–selection population equation and proves a principal-eigenvalue persistence criterion under mortality confinement, where mortality grows without bound. The constant-off-refuge mortality here is bounded, and the stated two-site localization and one-versus-two persistence classification are not consequences of those confinement assumptions. Hatano and Nelson (1996) study drift-induced non-Hermitian localization, and Liu et al. (2021) study a single impurity in nonreciprocal lattices; those related lattice mechanisms motivate careful comparison but are not claimed to be novel here. The present claim is limited to the explicit nonlinear ecological classification and its adjacent-refuge rescue interval.

## Limitations
The result classifies positive summable equilibria only. It does not prove global attraction, dynamics for non-summable initial data, or stochastic evolutionary persistence. The mathematical method uses classical one-dimensional recurrence matching. Prior general point-defect or non-Hermitian lattice theory may subsume some spectral formulas; a complete independent novelty audit has not been performed. The model assumes an infinite one-dimensional trait lattice, nearest-neighbor mutation, uniform mortality outside the refuges, and logistic suppression shared by all traits.

## References
- P. K. Pollett, *Mutation–selection balance on an infinite trait space: confinement, drift and equilibrium*, arXiv:2609.02086v1 (first publicly posted 2026-09-02), https://arxiv.org/html/2609.02086v1 .
- N. Hatano and D. R. Nelson, *Localization transitions in non-Hermitian quantum mechanics*, arXiv:cond-mat/9603165 (1996), https://arxiv.org/abs/cond-mat/9603165 .
- Y. Liu et al., *Exact solution of single impurity problem in non-reciprocal lattices*, arXiv:2106.03420 (2021), https://arxiv.org/abs/2106.03420 .
