# Exact speed-slope balance and an outer-scroll recurrence barrier in Chua’s double scroll
## Finding
Consider the classical piecewise-linear Chua system
\[
\dot x=\alpha(y-h(x)),\qquad
\dot y=x-y+z,\qquad
\dot z=-\beta y,
\]
with
\[
\alpha>0,\qquad \beta>0,
\]
and the odd three-segment characteristic
\[
h(x)=
\begin{cases}
m_1x+(m_0-m_1),&x\ge1,\\
m_0x,&|x|\le1,\\
m_1x-(m_0-m_1),&x\le-1,
\end{cases}
\]
where
\[
m_0<0<m_1.
\]

Every compactly supported invariant Borel probability measure \(\mu\) satisfies the three exact conditional laws
\[
\boxed{\mathbb E_\mu[y\mid x]=h(x)},
\]
\[
\boxed{\mathbb E_\mu[x+z\mid y]=y},
\]
and
\[
\boxed{\mathbb E_\mu[y\mid z]=0}.
\]

The first two are exact fluctuation decompositions:
\[
\boxed{
\operatorname{Var}_\mu(y)-\operatorname{Var}_\mu(h(x))
=
\frac1{\alpha^2}\mathbb E_\mu[\dot x^2]
},
\]
\[
\boxed{
\operatorname{Var}_\mu(x+z)-\operatorname{Var}_\mu(y)
=
\mathbb E_\mu[\dot y^2]
}.
\]

The two fast coordinate speeds also satisfy the exact slope-weighted balance
\[
\boxed{
\mathbb E_\mu[\dot y^2]
=
\mathbb E_\mu[h'(x)\dot x^2]
}.
\]
Here \(h'\) is the branch slope away from \(x=\pm1\). Its value at the two breakpoints is irrelevant because an invariant measure carries no \(\dot x^2\)-weighted mass there.

A separate sector-energy identity is
\[
\boxed{
\mathbb E_\mu[xh(x)]
=
\mathbb E_\mu[y^2]
=
\frac1{\beta^2}\mathbb E_\mu[\dot z^2]
}.
\]

Each of
\[
\mathbb E_\mu[\dot x^2],\qquad
\mathbb E_\mu[\dot y^2],\qquad
\mathbb E_\mu[\dot z^2]
\]
vanishes exactly for probability measures supported on the equilibrium set.

Define
\[
r=\frac{m_1-m_0}{m_1}>1.
\]
The equilibria are
\[
(0,0,0),\qquad
(r,0,-r),\qquad
(-r,0,r).
\]
Every compact stationary state not supported on those equilibria satisfies
\[
\boxed{\mu\{|x|>r\}>0}.
\]
Thus every genuinely recurrent stationary state reaches beyond the magnitude of the two nonzero equilibrium voltages.

There is also a quantitative outer-branch requirement. Set
\[
K_{\rm in}
=
\mathbb E_\mu[\dot x^2\mathbf 1_{\{|x|<1\}}],
\qquad
K_{\rm out}
=
\mathbb E_\mu[\dot x^2\mathbf 1_{\{|x|>1\}}].
\]
For every non-equilibrium stationary state,
\[
\boxed{
\frac{K_{\rm out}}{K_{\rm in}+K_{\rm out}}
>
\frac{-m_0}{m_1-m_0}
}.
\]

For the classical double-scroll slopes
\[
m_0=-\frac17,
\qquad
m_1=\frac27,
\]
one obtains
\[
r=\frac32
\]
and
\[
\boxed{
\frac{K_{\rm out}}
{\mathbb E_\mu[\dot x^2]}
>
\frac13
}.
\]
Hence every non-equilibrium compact stationary state gives positive mass to \(|x|>3/2\) and accumulates more than one third of its \(x\)-speed energy on the outer linear branches \(|x|>1\).

## Assumptions and scope
The measure \(\mu\) is invariant under the autonomous Chua flow and supported on a compact subset of \(\mathbb R^3\). The vector field is globally Lipschitz, so complete solutions are unique.

The characteristic \(h\) is continuous and piecewise affine. The branch derivative \(h'\) exists away from \(x=\pm1\), with values
\[
h'(x)=m_0\quad\text{for }|x|<1,
\qquad
h'(x)=m_1\quad\text{for }|x|>1.
\]
The slope balance is interpreted through the almost-everywhere chain rule for the Lipschitz function \(h\).

The double-scroll sign regime
\[
m_0<0<m_1
\]
is used only for the equilibrium-amplitude and outer-branch consequences. The three conditional laws and their variance defects hold for arbitrary continuous piecewise-linear \(h\) in this normalization.

The first verified public source date for the chaotic Chua attractor is 17 April 1984, from the Berkeley memorandum “A Chaotic Attractor From Chua’s Circuit.” A complete 1985 Berkeley report gives the normalized equations above, the three-segment nonlinearity, and the classical slopes \(m_0=-1/7\), \(m_1=2/7\). Same-object mathematical literature classifies Chua dynamics under MSC \(34C28\); this finding is placed there.

## Proof
Let \(L\) be the generator of the flow.

For a continuous test function \(\phi\) on the compact \(x\)-range, choose a continuously differentiable antiderivative \(H\) with
\[
H'(x)=\phi(x).
\]
Then
\[
LH
=
\alpha\phi(x)(y-h(x)).
\]
Invariance gives
\[
\mathbb E_\mu[\phi(x)(y-h(x))]=0
\]
for every such \(\phi\), hence
\[
\mathbb E_\mu[y\mid x]=h(x).
\]

Repeating the same argument with an antiderivative in \(y\) gives
\[
\mathbb E_\mu[x-y+z\mid y]=0,
\]
therefore
\[
\mathbb E_\mu[x+z\mid y]=y.
\]
An antiderivative in \(z\) gives
\[
\mathbb E_\mu[-\beta y\mid z]=0,
\]
so
\[
\mathbb E_\mu[y\mid z]=0.
\]

Because conditional expectation is an orthogonal projection in \(L^2\),
\[
\mathbb E[(y-h(x))^2]
=
\operatorname{Var}(y)-\operatorname{Var}(h(x)).
\]
Using
\[
y-h(x)=\frac{\dot x}{\alpha}
\]
gives the first variance defect. Likewise,
\[
x+z-y=\dot y
\]
and
\[
\mathbb E[x+z\mid y]=y
\]
give the second.

We next derive the slope balance. Put
\[
g=y-h(x)=\frac{\dot x}{\alpha}.
\]
The function \(h\) is Lipschitz, so \(g(t)\) is absolutely continuous along every trajectory and
\[
\frac{d}{dt}\frac{g^2}{2}
=
g(\dot y-h'(x)\dot x)
\]
for almost every time. Invariance and compact support imply that its stationary mean derivative is zero. Therefore
\[
\mathbb E[\dot x\dot y]
=
\mathbb E[h'(x)\dot x^2].
\]

Now let
\[
q=x-y+z=\dot y.
\]
Stationarity of \(q^2/2\) gives
\[
0
=
\mathbb E[q(\dot x-\dot y+\dot z)].
\]
Since
\[
\dot z=-\beta y
\]
and stationarity of \(y^2/2\) gives
\[
\mathbb E[y\dot y]=0,
\]
we have
\[
\mathbb E[q\dot z]=0.
\]
Thus
\[
\mathbb E[\dot x\dot y]
=
\mathbb E[\dot y^2].
\]
Combining the last two identities proves
\[
\mathbb E[\dot y^2]
=
\mathbb E[h'(x)\dot x^2].
\]

For completeness, an invariant probability measure has no \(\dot x^2\)-weighted mass on the two breakplanes. Indeed, on a subset of \(x=1\) or \(x=-1\) where \(|\dot x|\) is bounded away from zero, sufficiently small distinct time translates are locally disjoint; invariance would otherwise give infinitely many disjoint sets of the same positive measure. The remaining breakpoint points have \(\dot x=0\). Hence the assigned value of \(h'\) at \(x=\pm1\) is immaterial.

To obtain the sector-energy identity, first note from
\[
\mathbb E[y\mid z]=0
\]
that
\[
\mathbb E[y]=0,
\qquad
\mathbb E[yz]=0.
\]
Stationarity of \(y^2/2\) yields
\[
0
=
\mathbb E[y(x-y+z)],
\]
so
\[
\mathbb E[xy]=\mathbb E[y^2].
\]
But the first conditional law gives
\[
\mathbb E[xy]
=
\mathbb E[xh(x)].
\]
Finally,
\[
\dot z=-\beta y
\]
gives
\[
\mathbb E[y^2]
=
\frac1{\beta^2}\mathbb E[\dot z^2].
\]

We classify equality. If \(\mathbb E[\dot x^2]=0\), continuity makes \(\dot x=0\) on the invariant support. Along every support trajectory, \(x\) and therefore \(y=h(x)\) are constant. Bounded completeness of \(\dot z=-\beta y\) forces \(y=0\), so \(h(x)=0\); the \(y\)-equation then gives \(z=-x\), which is an equilibrium. If \(\mathbb E[\dot y^2]=0\), then \(y\) is constant and bounded completeness of \(\dot z=-\beta y\) again forces \(y=0\); the remaining equations force an equilibrium. If \(\mathbb E[\dot z^2]=0\), then \(y=0\) on support, invariance forces \(x+z=0\), and then \(x\) is constant with \(h(x)=0\). The converse is immediate.

In the sign regime \(m_0<0<m_1\), the positive zero of the outer branch is
\[
r=\frac{m_1-m_0}{m_1}.
\]
Directly from the piecewise formula,
\[
xh(x)\le0
\quad\text{for }|x|\le r,
\]
and
\[
xh(x)>0
\quad\text{for }|x|>r.
\]
A non-equilibrium stationary state has
\[
\mathbb E[y^2]>0,
\]
so the identity
\[
\mathbb E[xh(x)]=\mathbb E[y^2]
\]
forces positive mass on \(|x|>r\).

Finally, the slope balance becomes
\[
\mathbb E[\dot y^2]
=
m_0K_{\rm in}+m_1K_{\rm out}.
\]
The left-hand side is strictly positive off equilibrium support. Therefore
\[
m_1K_{\rm out}>-m_0K_{\rm in},
\]
which is equivalent to
\[
\frac{K_{\rm out}}{K_{\rm in}+K_{\rm out}}
>
\frac{-m_0}{m_1-m_0}.
\]
For \(m_0=-1/7\), \(m_1=2/7\), this is the strict one-third bound.

## Verification
The accompanying checker uses only the Python standard library and exact rational arithmetic.

It verifies the conditional-regression variance algebra
\[
\mathbb E[(A-B)^2]
=
\operatorname{Var}(A)-\operatorname{Var}(B)
\]
from the moment relations implied by \(\mathbb E[A\mid\mathcal G]=B\).

It verifies the algebraic chain behind the slope balance: stationarity of the fast residual gives
\[
\mathbb E[\dot x\dot y]
=
\mathbb E[h'(x)\dot x^2],
\]
while stationarity of \(\dot y^2/2\), together with \(\dot z=-\beta y\), gives
\[
\mathbb E[\dot x\dot y]
=
\mathbb E[\dot y^2].
\]

For the classical exact slopes
\[
m_0=-\frac17,
\qquad
m_1=\frac27,
\]
the checker confirms
\[
r=\frac{m_1-m_0}{m_1}=\frac32
\]
and
\[
\frac{-m_0}{m_1-m_0}=\frac13.
\]
It also verifies branchwise that \(xh(x)>0\) exactly for \(|x|>3/2\) in that case.

The stored output in `verification_output.txt` is `VERIFY_OK`.

The invariant-measure disintegrations, breakpoint zero-weight argument, and equality classification are analytic proofs in this document, not consequences of finite simulation.

## Relationship to prior work
Matsumoto’s 1984 Berkeley memorandum introduced the chaotic attractor from Chua’s circuit. The earliest verified public date used here is 17 April 1984.

Chua, Komuro, and Matsumoto’s complete 1985 Berkeley report develops a rigorous proof of chaos and bifurcation analysis for the double-scroll family. It writes the same normalized equations and the same three-segment characteristic used here, including the classical slopes \(m_0=-1/7\) and \(m_1=2/7\). The report studies Poincaré maps, homoclinic geometry, conjugacy, and bifurcations. Targeted full-document searches did not locate invariant-measure, conditional-expectation, moment, average, or variance statements matching the accepted theorem.

Later work rigorously studies localization of compact invariant sets in Chua systems. A 2016 same-object localization article writes the original Chua equations and develops localizing sets and global sections. Its accessible text does not expose the conditional regressions or weighted-speed identity proved here. A complete copy was not available through the inspected lawful routes, so possible overlap with the standalone amplitude-crossing corollary is retained as a residual risk rather than dismissed. The originality claim rests on the exact all-invariant-measures regression and speed-slope identities, which are not implied by the accessible localization statements.

Smooth-Chua hidden-attractor literature and the classic double-scroll papers study attractor existence, hidden versus self-excited localization, equilibria, and bifurcations. They provide same-object differential-dynamics context but do not implication-wise supply the identities
\[
\mathbb E[y\mid x]=h(x)
\]
or
\[
\mathbb E[\dot y^2]=\mathbb E[h'(x)\dot x^2].
\]

Published semantic searches covered direct conditional formulations, variance defects, the sector identity \(\mathbb E[xh(x)]=\mathbb E[y^2]\), the derivative-energy slope law, the equilibrium-voltage crossing, and the classical one-third outer-speed fraction. No same-object published record was found that implies the accepted theorem.

## Limitations
The theorem concerns compactly supported invariant probability measures. It does not prove existence of the double-scroll attractor for a given parameter set.

The amplitude condition \(\mu\{|x|>r\}>0\) is necessary for non-equilibrium compact recurrence in the sign regime \(m_0<0<m_1\); it is not sufficient for chaos or a periodic orbit.

The one-third classical bound concerns \(x\)-speed energy, not ordinary residence time on the outer branches.

The full 2016 localization article was not retrievable through the inspected lawful routes. Its accessible material was compared, and the residual overlap risk is confined primarily to the amplitude-crossing corollary; the exact regression and speed-slope identities remain the originality target.

The theorem does not determine Lyapunov exponents, entropy, symbolic dynamics, return maps, or basin geometry.

## References
1. T. Matsumoto, “A Chaotic Attractor From Chua’s Circuit,” Memorandum UCB/ERL M84/36, University of California, Berkeley, 17 April 1984.
2. L. O. Chua, M. Komuro, and T. Matsumoto, “The Double Scroll Family: Part I — Rigorous Proof of Chaos; Part II — Rigorous Analysis of Bifurcation Phenomena,” Memorandum UCB/ERL M85/102, University of California, Berkeley, 4 December 1985.
3. T. Matsumoto, L. O. Chua, and M. Komuro, “The double scroll,” IEEE Transactions on Circuits and Systems 32 (1985), DOI 10.1109/TCS.1985.1085791.
4. L. O. Chua, M. Komuro, and T. Matsumoto, “The double scroll family,” IEEE Transactions on Circuits and Systems 33 (1986), DOI 10.1109/TCS.1986.1085869.
5. E. Gribov, A. Kanatnikov, A. Krishchenko, and D. Razhev, “Localization Method of Compact Invariant Sets with Application to the Chua System,” International Journal of Bifurcation and Chaos 26 (2016), DOI 10.1142/S0218127416500735.
6. N. V. Kuznetsov, G. A. Leonov, and V. I. Vagaitsev, “Hidden attractor in smooth Chua systems,” Physica D 241 (2012), DOI 10.1016/j.physd.2012.05.016.
