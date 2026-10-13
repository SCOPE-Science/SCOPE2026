# Exact repair of a detailed-balance adaptation example: species 2 adapts and species 3 tracks the signal
## Finding
Consider the reversible network used in Example 3.8 of Franco and Velázquez,
\[
X_1 \rightleftarrows X_2+X_3,\qquad X_3\rightleftarrows X_1,
\]
with the rate constants printed in that example. Prescribe the signal species \(X_1\) as a positive function \(u(t)\), and write \(x(t)=n_2(t)\), \(y(t)=n_3(t)\),
\[
a=K_1>0,\qquad b=K_2>0,\qquad c=e^{E_2+E_3-E_1},\qquad r=e^{E_1-E_3}.
\]
Then the nonsignal subsystem is
\[
\dot x=a(u-cxy),\qquad
\dot y=a(u-cxy)+b(ru-y).
\]
The adapting product is species \(X_2\), not species \(X_3\). More strongly, under the source's admissible-signal assumptions, species \(X_2\) adapts for every positive parameter choice: its limiting value is always \(e^{-E_2}\), and its transient response is necessarily nontrivial. Species \(X_3\) instead tracks the limiting signal proportionally.

## Assumptions and scope
The signal is assumed to satisfy the hypotheses used for admissible signaling in the motivating work: \(u\in C^1([0,\infty))\), \(u(t)>0\), \(u(0)=e^{-E_1}\),
\[
u(t)-u(0)\sim t\quad(t\downarrow0),
\]
\[
\left|\frac{d}{dt}\log u(t)\right|\le e^{-\rho t}
\]
for some \(\rho>0\), and \(u(t)\to\bar u>0\). Initial nonsignal concentrations are the detailed-balance values \(x(0)=e^{-E_2}\) and \(y(0)=e^{-E_3}\). All kinetic constants are positive.

The claim concerns this explicit two-reaction network with an externally prescribed signal. It does not assert that every detailed-balance network has an all-parameter adaptation coordinate.

## Proof
Use reaction vectors
\[
\nu_1=(-1,1,1)^\top,\qquad \nu_2=(1,0,-1)^\top.
\]
A conservation law \(m=(m_1,m_2,m_3)^\top\) obeys \(m^\top\nu_1=m^\top\nu_2=0\). The second equation gives \(m_1=m_3\), and the first then gives \(m_2=0\). Therefore
\[
\mathcal M=\operatorname{span}\{(1,0,1)^\top\}.
\]
In particular, coordinate 2, not coordinate 3, vanishes on every conservation law.

For a constant signal \(u=s>0\), a positive steady state \((X,Y)\) satisfies
\[
0=a(s-cXY),\qquad 0=a(s-cXY)+b(rs-Y).
\]
The first equation gives \(cXY=s\), and then the second gives \(Y=rs\). Hence
\[
X=\frac1{cr}=e^{-E_2},\qquad Y=rs=e^{E_1-E_3}s.
\]
This positive steady state is unique. Thus the species-2 set point is independent of the signal level, whereas the species-3 steady value is proportional to it.

It remains to verify convergence for a time-dependent admissible signal without importing a generic convergence theorem. Set
\[
x_*=\frac1{cr}=e^{-E_2},\qquad X=\frac{x}{x_*},\qquad Y=\frac{y}{ru},
\]
and let \(h(z)=z\log z-z+1\). Define
\[
V(t)=x_*h(X(t))+ru(t)h(Y(t)).
\]
A direct differentiation gives the exact identity
\[
\dot V=-a u(XY-1)\log(XY)-b r u(Y-1)\log Y+r\dot u(1-Y).
\]
The first two terms are nonpositive. Put \(q(t)=|\dot u(t)|/u(t)\). The signal hypothesis makes \(q\) integrable. It also implies that \(u\) stays between two positive constants. Since entropy coercivity gives \(y\le C(1+V)\) for a fixed \(C\),
\[
|r\dot u(1-Y)|\le q(t)(ru+y)\le Cq(t)(1+V).
\]
Gronwall's inequality therefore bounds \(V\), hence \(x\) and \(y\), for all positive time. With \(u\) bounded below, the differential inequalities
\[
\dot x\ge a u_{\min}-ac y_{\max}x,
\]
and
\[
\dot y\ge (a+br)u_{\min}-(ac x_{\max}+b)y
\]
show that both \(x\) and \(y\) are eventually bounded away from zero. Thus \(X\) and \(Y\) eventually remain in a compact subset of \((0,\infty)\).

Because the last term in \(\dot V\) is absolutely integrable, integration of the identity for \(\dot V\) yields
\[
\int_0^\infty au(XY-1)\log(XY)\,dt<\infty,
\]
\[
\int_0^\infty bru(Y-1)\log Y\,dt<\infty.
\]
On the eventual compact positive range these dissipation terms are uniformly continuous; the signal hypothesis also gives \(\dot u(t)\to0\). The elementary Barbalat argument therefore forces both dissipations to tend to zero. Since \((z-1)\log z=0\) only at \(z=1\), first \(Y\to1\), then \(XY\to1\), and hence \(X\to1\). Consequently
\[
n_2(t)\to e^{-E_2},\qquad n_3(t)\to r\bar u.
\]

Finally, at the initial detailed-balance state, \(x'(0)=y'(0)=0\). The normalization \(u(t)-u(0)\sim t\) and \(u\in C^1\) imply \(u'(0)=1\). Differentiating \(x'=a(u-cxy)\) gives
\[
x''(0)=a=K_1>0.
\]
Therefore
\[
n_2(t)=e^{-E_2}+\frac{K_1}2t^2+o(t^2),
\]
so the product response is nontrivial for every positive rate choice.

## Verification
The stoichiometric calculation and steady-state formulas are exact algebra. The bundled `verify.py` performs an independent exact-arithmetic check of the reaction-vector conservation law and of the fixed-signal residual identities after the exponential combinations are represented by arbitrary positive rational parameters \(c\) and \(r\). It also checks the sign of the forced second-order response coefficient in representative exact rational instances. The convergence argument is analytic; finite computation is not used as a substitute for it.

## Relationship to prior work
The motivating article itself gives the same reaction network earlier and states its conservation-law space as \(\operatorname{span}\{(1,0,1)^\top\}\). Its later Example 3.8 nevertheless identifies coordinate 3 as vanishing on all conservation laws and concludes that species 3 adapts. The two statements are incompatible. Solving the printed equations resolves the incompatibility: coordinate 2 is the invariant output, and coordinate 3 is signal dependent.

The article's general proposition for nonconservative detailed-balance networks guarantees an adapting coordinate under a structural conservation-law condition, subject to a possible exceptional transient-response case. The calculation above specializes the printed example, identifies the correct coordinate, and removes that genericity caveat for this network by proving \(n_2''(0)=K_1>0\) for every positive parameter choice.

Earlier absolute-concentration-robustness results, including Shinar and Feinberg's structural theory and later dynamic ACR work, concern different structural hypotheses and do not state this correction or the all-parameter transient law for the present chemostatted reversible network.

## Limitations
The result is a correction and exact strengthening for one explicit network. It does not invalidate the motivating article's general structural propositions, and it does not classify all detailed-balance adaptation networks. The convergence proof uses the source's exponentially decaying logarithmic signal-rate assumption and a positive limiting signal. Literature and repository searches found no published correction of this example, but poorly indexed commentary or later errata could still exist.

## References
1. D. Franco and J. J. L. Velázquez, “The adaptation property in non-equilibrium chemical systems,” *Journal of Mathematical Biology* 92 (2026), article 32. arXiv:2502.17375. DOI: 10.1007/s00285-026-02344-y.
2. D. Franco and J. J. L. Velázquez, “The Detailed Balance Property and Chemical Systems out of Equilibrium,” *Bulletin of Mathematical Biology* (2025). DOI: 10.1007/s11538-025-01487-1.
3. G. Shinar and M. Feinberg, “Structural Sources of Robustness in Biochemical Reaction Networks,” *Science* 327 (2010), 1389–1391. DOI: 10.1126/science.1183372.
4. D. Cappelletti, A. Gupta, and M. Khammash, “A hidden integral structure endows absolute concentration robust systems with resilience to dynamical concentration disturbances.” arXiv:1910.05531.
