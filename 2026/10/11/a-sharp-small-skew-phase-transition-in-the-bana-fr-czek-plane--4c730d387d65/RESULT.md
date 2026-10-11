# A sharp small-skew phase transition in the Banaś–Frączek plane
## Finding
For the real Banaś–Frączek plane \(X_\lambda=(\mathbb R^2,N_\lambda)\), \(\lambda>1\), with
\[
N_\lambda(u,v)=\max\{\lambda|u|,\sqrt{u^2+v^2}\},
\]
let \(\mathcal S_\lambda(\tau)=\mathcal S_{X_\lambda,2}(\tau)\) denote the skew Schäffer type constant. Then the right derivative at the unskewed endpoint exists and
\[
\mathcal S_\lambda'(0+)=-c(\lambda),
\qquad
c(\lambda)=
\begin{cases}
\frac12\sqrt{\lambda^2-1},&1<\lambda\le\sqrt2,\\
1-\lambda^{-2},&\lambda\ge\sqrt2.
\end{cases}
\]
Equivalently,
\[
\mathcal S_\lambda(\tau)=1-c(\lambda)\tau+o(\tau)
\qquad(\tau\downarrow0).
\]
The two branches agree at \(\lambda=\sqrt2\), where \(c(\sqrt2)=1/2\). Thus the initial loss of the skew Schäffer constant has a sharp geometric phase transition at that parameter.

## Assumptions and scope
Everything is over the real scalars. Write
\[
h=\lambda^{-1},\qquad q=\sqrt{1-h^2},
\]
and set
\[
Q_s(u,v)=\lambda^2u^2,\qquad Q_e(u,v)=u^2+v^2,\qquad
\Phi_\lambda=\max\{Q_s,Q_e\}=N_\lambda^2.
\]
For unit vectors \(x,y\in S_{X_\lambda}\), define
\[
F_{x,y}(\tau)^2=\frac{\Phi_\lambda(x+\tau y)+\Phi_\lambda(y-\tau x)}2.
\]
By symmetry of the norm this is the square of the quadratic-mean expression in the definition of \(\mathcal S_\lambda(\tau)\), so
\[
\mathcal S_\lambda(\tau)^2=\inf_{x,y\in S_{X_\lambda}}F_{x,y}(\tau)^2.
\]
The statement concerns only the right derivative at \(\tau=0\). It does not claim an exact formula for \(\mathcal S_\lambda(\tau)\) on an interval to the right of zero.

## Proof
For each unit vector choose one active quadratic branch of \(\Phi_\lambda\), so that the chosen branch equals one at that vector. Consider first a mixed choice: the strip branch is active at \(x\) and the Euclidean branch is active at \(y\). Then
\[
|x_1|=h,\qquad |x_2|\le q,\qquad y_1^2+y_2^2=1,\qquad |y_1|\le h.
\]
Since \(\Phi_\lambda\) dominates each of its quadratic branches,
\[
\begin{aligned}
2F_{x,y}(\tau)^2
&\ge Q_s(x+\tau y)+Q_e(y-\tau x)\\
&=2+2\tau\bigl((\lambda^2-1)x_1y_1-x_2y_2\bigr)
 +\tau^2\bigl(\lambda^2y_1^2+\|x\|_2^2\bigr).
\end{aligned}
\]
Put \(a=\lambda-\lambda^{-1}\). If \(t=|y_1|\in[0,h]\), then
\[
(\lambda^2-1)x_1y_1-x_2y_2
\ge-\bigl(a t+q\sqrt{1-t^2}\bigr).
\]
The maximum of the expression in parentheses over \(0\le t\le h\) is
\[
C(\lambda)=
\begin{cases}
\lambda q,&q\le h,\\
2q^2,&q\ge h.
\end{cases}
\]
Indeed, on the unconstrained interval its maximizing point is \(t=q\), and \(q\le h\) is equivalent to \(\lambda\le\sqrt2\); if \(q\ge h\), the constrained maximum is attained at \(t=h\). The reversed mixed choice gives the same bound. If both chosen active branches are the same, the linear cross terms cancel exactly. Hence for every unit pair and every \(\tau\ge0\),
\[
F_{x,y}(\tau)^2\ge1-C(\lambda)\tau,
\]
and therefore
\[
\liminf_{\tau\downarrow0}
\frac{\mathcal S_\lambda(\tau)^2-1}{\tau}
\ge-C(\lambda).
\]

For the reverse inequality, use strict mixed-branch points approaching the boundary. Take \(x=(h,s)\) with \(0<s<q\), so the strip branch is uniquely active, and take
\[
y=(-t,\sqrt{1-t^2})
\]
with \(0<t<h\), so the Euclidean branch is uniquely active. For sufficiently small positive \(\tau\), these active branches persist and direct expansion gives
\[
F_{x,y}(\tau)^2
=1-\tau\bigl(a t+s\sqrt{1-t^2}\bigr)+O(\tau^2).
\]
If \(1<\lambda<\sqrt2\), first let \(s\uparrow q\) and take \(t=q<h\); the linear coefficient tends to \(\lambda q=C(\lambda)\). If \(\lambda>\sqrt2\), let \(s\uparrow q\) and \(t\uparrow h\); the coefficient tends to \(2q^2=C(\lambda)\). The same limiting argument covers \(\lambda=\sqrt2\). Thus
\[
\limsup_{\tau\downarrow0}
\frac{\mathcal S_\lambda(\tau)^2-1}{\tau}
\le-C(\lambda).
\]
Combining the two bounds,
\[
\mathcal S_\lambda(\tau)^2=1-C(\lambda)\tau+o(\tau).
\]
Since \(\mathcal S_\lambda(0)=1\), taking the square root yields
\[
\mathcal S_\lambda'(0+)=-\frac{C(\lambda)}2.
\]
Finally, \(q=\sqrt{1-\lambda^{-2}}\), so \(C(\lambda)/2=\frac12\sqrt{\lambda^2-1}\) below \(\sqrt2\) and \(C(\lambda)/2=1-\lambda^{-2}\) above it, as claimed.

## Verification
The proof uses exact quadratic identities and a one-variable maximization; no finite numerical sampling is used as proof. The boundary cases were checked explicitly: the two coefficient formulas coincide at \(\lambda=\sqrt2\), and \(c(\lambda)\to0\) as \(\lambda\downarrow1\), consistent with the Euclidean limit. The lower bound allows either active branch at a corner, so nonsmooth points of the max norm do not require differentiating the norm there. The upper bound instead uses strict single-branch points and only then takes a boundary limit.

## Relationship to prior work
Xu and Liu introduce the skew Schäffer type constants and, for this same Banaś–Frączek plane, prove the exact formula
\[
\mathcal S_{X_\lambda,2}(\tau)
=\left(\frac{(1+\tau^2)(1+\lambda^{-2})}2\right)^{1/2}
\]
for \(\sqrt{1-\lambda^{-2}}\le\tau\le1\). Their general theory also gives global Lipschitz control in the skew parameter. The present result addresses the complementary endpoint question \(\tau\downarrow0\) and identifies the exact first-order coefficient there.

The 2016 paper of C. Yang and X. Yang computes classical James-type quantities for Banaś–Frączek-type spaces, including the symmetric parameter value used in that theory. A 2025 paper of Wang and coauthors computes the supremal Euler–Lagrange constant for the Banaś–Frączek plane. Those are supremal or symmetric geometric invariants and do not imply the infimal small-skew derivative proved here.

## Limitations
The result is only a first-order endpoint asymptotic. It does not determine the exact profile of \(\mathcal S_\lambda(\tau)\) for \(0<\tau<\sqrt{1-\lambda^{-2}}\), does not classify minimizers for positive \(\tau\), and makes no claim about complex scalars or higher-dimensional analogues. Because one close 2025 comparison source was available only through its abstract during the literature comparison, an older equivalent formulation under different geometric-constant terminology remains a residual originality risk.

## References
1. Y. Xu and Q. Liu, *Skew Schäffer Type Constants*, arXiv:2610.03050v1, 2026.
2. C. Yang and X. Yang, *On the James type constant and von Neumann–Jordan constant for a class of Banaś–Frączek type spaces*, J. Math. Inequal. 10 (2016), 551–558, DOI:10.7153/jmi-10-43.
3. Y. Wang et al., *On the \(L_{\mathrm{YJ}}(\xi,\eta,X)\) constant for the Banaś–Frączek space*, Rend. Circ. Mat. Palermo (2025), DOI:10.1007/s12215-025-01277-7.
