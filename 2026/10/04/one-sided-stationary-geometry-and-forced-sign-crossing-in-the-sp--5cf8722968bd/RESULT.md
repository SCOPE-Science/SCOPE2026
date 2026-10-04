# One-sided stationary geometry and forced sign crossing in the Sprott E flow
## Finding
Consider the canonical Sprott E flow
\[
\dot x=yz,\qquad \dot y=x^2-y,\qquad \dot z=1-4x.
\]
For every compactly supported invariant probability measure \(\mu\),
\[
\mathbb E_\mu[yz\mid x]=0,\qquad
\mathbb E_\mu[x^2\mid y]=y,\qquad
\mathbb E_\mu[x\mid z]=\frac14.
\]
Moreover the support of \(\mu\) lies in the open half-space \(y>0\), and
\[
\mathbb E_\mu[y]=\frac1{16}+\operatorname{Var}_\mu(x)\ge \frac1{16}.
\]
Equality holds exactly for the point mass at the unique equilibrium
\[
p_* = \left(\frac14,\frac1{16},0\right).
\]
Every compact invariant measure other than \(\delta_{p_*}\) assigns positive mass to both \(z>0\) and \(z<0\). In particular, every nonconstant periodic orbit stays in \(y>0\), crosses \(z=0\) at least twice in each least period, and satisfies \(\langle y\rangle>1/16\).

## Assumptions and scope
An invariant probability measure means an invariant Borel probability measure for the Sprott E flow whose support is compact. Thus every trajectory in its support is a bounded complete trajectory. No ergodicity assumption is made. The statement concerns the unmodified Sprott E equations above; controlled, delayed, fractional-order, and parameter-extended variants are not included.

## Proof
Let \((x(t),y(t),z(t))\) be any bounded complete trajectory. Solving the scalar linear equation \(\dot y+y=x^2\) backward gives, for every \(T>0\),
\[
y(t)=e^{-T}y(t-T)+\int_0^T e^{-s}x(t-s)^2\,ds.
\]
Boundedness and \(T\to\infty\) yield
\[
y(t)=\int_0^\infty e^{-s}x(t-s)^2\,ds\ge0.
\]
The inequality is strict. Indeed, if \(y(t_0)=0\), then the integral forces \(x(t)=0\) for all \(t\le t_0\). The equation for \(y\) then forces \(y(t)=0\) on the same past half-line, while \(\dot z=1\), contradicting boundedness as \(t\to-\infty\). Hence every compact invariant support is contained in \(y>0\).

For a \(C^1\) function \(F\) of one variable, invariance gives \(\int L(F\circ x)\,d\mu=0\), where \(L\) is the flow generator. Since
\[
L(F(x))=F'(x)yz,
\]
and every continuous function on the compact \(x\)-projection is the derivative there of a \(C^1\) function, it follows that
\[
\mathbb E_\mu[yz\mid x]=0.
\]
The same argument applied to functions of \(y\) and \(z\) gives
\[
\mathbb E_\mu[x^2-y\mid y]=0,
\qquad
\mathbb E_\mu[1-4x\mid z]=0,
\]
which are the other two conditional laws.

Taking expectations gives
\[
\mathbb E_\mu[x]=\frac14,
\qquad
\mathbb E_\mu[y]=\mathbb E_\mu[x^2].
\]
Therefore
\[
\mathbb E_\mu[y]-\frac1{16}
=\mathbb E_\mu[x^2]-\mathbb E_\mu[x]^2
=\operatorname{Var}_\mu(x)\ge0.
\]
If equality holds, then \(x=1/4\) on the support. Invariance and \(y>0\) imply \(0=\dot x=yz\), hence \(z=0\). The remaining equation is \(\dot y=1/16-y\); its only bounded complete solution is \(y=1/16\). Thus equality holds exactly for \(\delta_{p_*}\).

Finally, stationarity of \(x\) gives \(\int yz\,d\mu=0\). Suppose a compact invariant measure is supported in \(z\ge0\). Since its support lies in \(y>0\), the integrand \(yz\) is nonnegative, so \(yz=0\) almost surely and therefore \(z=0\) on the support. Invariance then forces \(x=1/4\), and bounded completeness forces \(y=1/16\); hence the measure is \(\delta_{p_*}\). The same argument applies to \(z\le0\). Thus every non-equilibrium compact invariant measure has positive mass in both open \(z\)-half-spaces. A nonconstant periodic orbit carries such an invariant time-average measure, so its continuous periodic \(z(t)\) assumes both signs and consequently has at least two distinct zeros per least period.

## Verification
The vector-field equations and the identification of the unmodified Sprott E case were checked against a full-text same-object source. The exact equilibrium and the rational identities used in the mean-defect argument were replayed with the dependency-free standard-library checker `verify.py`; the recorded output is `VERIFY_OK`. The measure-theoretic steps are analytic: invariance of compact support justifies the generator identities, while the backward variation-of-constants formula proves the strict \(y>0\) support property.

## Relationship to prior work
Sprott's 1994 paper introduced the family of simple chaotic flows and is the earliest verified public source for this system. Wei and Wang later write the extended equations \(\dot x=yz+h(x)\), \(\dot y=x^2-y\), \(\dot z=1-4x\) and explicitly identify \(h=0\) with Sprott E. Their work studies chaotic attractors, period-doubling, Lyapunov exponents, and synchronization. Later Sprott E papers study degenerate Hopf bifurcations, hidden attractors, adaptive control, and distributed-delay chaos control. The inspected sources do not state the three conditional stationary laws, the strict one-sided \(y\)-geometry of compact complete dynamics, the sharp mean floor, its equality rigidity, or the forced two-sided \(z\)-recurrence theorem.

Structurally similar invariant-measure identities are known for other polynomial chaotic flows, but those depend on different vector fields and do not imply the Sprott E identities. The present result is specific to the triangular forcing \(\dot y+y=x^2\) together with \(\dot z=1-4x\) and \(\dot x=yz\).

## Limitations
The theorem does not prove existence, uniqueness, ergodicity, mixing, or physicality of a non-equilibrium invariant measure. It does not give a quantitative lower bound on the mass in either \(z\)-half-space or on the separation of consecutive crossings. The original 1994 publisher full text was not accessible during this review; its publication date and bibliographic record were verified at the publisher, while the exact equations were inspected in a later full-text paper that explicitly identifies the unmodified Sprott E case. Unindexed literature may use alternate terminology such as occupation measures or time averages.

## References
1. J. C. Sprott, *Some simple chaotic flows*, Physical Review E 50 (1994), R647-R650. DOI: 10.1103/PhysRevE.50.R647. Published 1 August 1994.
2. Z. Wei and Z. Wang, *Chaotic behavior and modified function projective synchronization of a simple system with one stable equilibrium*, Kybernetika 49 (2013), 359-374. DML-CZ 143372; MR 3085401.
3. Z. Wei, I. Moroz, and A. Liu, *Degenerate Hopf bifurcations, hidden attractors, and control in the extended Sprott E system with only one stable equilibrium*, Turkish Journal of Mathematics 38 (2014), 672-687. DOI: 10.3906/mat-1305-64.
4. C.-J. Xu and Y.-S. Wu, *Chaos Control and Bifurcation Behavior for a Sprott E System with Distributed Delay Feedback*, International Journal of Automation and Computing 12 (2015), 182-191. DOI: 10.1007/s11633-014-0852-z.
