# A sharp prey-survival threshold at critical constant harvest with group defense

## Finding
Consider the planar harvested predator–prey model
\[
\dot x=x(1-x/K)-P(x)y-K/4,\qquad
\dot y=\bigl(P(x)-P(K/2)\bigr)y,
\]
with positive initial prey \(x\) and predator \(y\). Let \(r=K/2\), \(P(r)>0\), and \(\alpha=-K P'(r)\). A positive solution is called *prey surviving* when it remains in \(x>0\) for all forward time; the model is followed only until first contact with \(x=0\), where constant prey harvesting would otherwise render the continuation biologically nonphysical.

**Sharp dichotomy.** If \(\alpha\le2\), every strictly positive predator initial condition causes prey to reach zero in finite time, regardless of initial prey abundance. If \(\alpha>2\), each \(c\) satisfying
\[
0<c<\frac{\alpha-2}{2K P(r)}
\]
admits an \(\varepsilon>0\) such that the open wedge
\[
0<x-r<\varepsilon,\qquad 0<y<c(x-r)^2
\]
is forward invariant and every trajectory in it is prey surviving, with \((x(t),y(t))\to(r,0)\). For **every** \(\alpha\), however, positive states with \(0<x(0)\le r\) suffer prey exhaustion in finite time. Thus \(\alpha=2\), including equality on the collapse side, is a sharp threshold for an interior prey-survival basin at maximum sustainable constant yield.

In the group-defense specialization
\[
P(x)=\frac{x^2}{a x^2+b x+1},\qquad a>0,\quad -2\sqrt a<b<0,
\]
the entire cutoff is explicit:
\[
\alpha=-\frac{4K^2(bK+4)}{(aK^2+2bK+4)^2}.
\]
For example, at \(K=4\), \(b=-5/4\), critical harvest \(h=1\), and predator mortality \(d=P(2)\), taking \(a=1\) gives \(\alpha=16/25<2\) (all positive-predator states exhaust prey), whereas \(a=1/2\) gives \(\alpha=16>2\) (an open survival wedge). At \(a=9/16\), \(b=-9/8\), \(K=4\), one has the sharp equality \(\alpha=2\), and again all positive-predator states exhaust prey. All three examples satisfy the stated group-defense admissibility conditions.

## Assumptions and scope
The structural theorem uses \(K>0\) and a positive, locally Lipschitz response \(P\) on \((0,\infty)\), continuously differentiable near \(r\) with a locally Lipschitz derivative (\(C^2\) there suffices). A positive classical trajectory exists uniquely until its first contact with \(x=0\). There is no claim of a positive-invariant quadrant under *constant* harvesting: at \(x=0\), the prey vector field equals \(-K/4\). The negative-\(b\) Holling response is smooth and strictly positive on positive \(x\) because \(b^2<4a\). The classification concerns prey survival; in the surviving wedge the predator ultimately goes extinct, and positive coexistence at equilibrium is not asserted. The strict derivative threshold is imposed only at the coalesced predator-free equilibrium, when harvesting is \(K/4\) and predator mortality is precisely \(P(r)\).

## Proof
Put \(u=x-r\), \(p(u)=P(r+u)\), \(p_0=P(r)\). Completing the logistic square gives the *exact*, not asymptotic, equations
\[
\dot u=-u^2/K-p(u)y,\qquad
\dot y=(p(u)-p_0)y.
\]
The predator remains positive while the solution remains biological, and \(u\) is strictly decreasing whenever \(y>0\). If \(u(0)<0\), then \(\dot u\le-u^2/K\), so \(u\) decreases from a negative number to \(-r\) (that is, \(x=0\)) in finite time; indeed, the Riccati comparison reaches \(-r\) no later than \(K(1/|u(0)|-1/r)\) when \(-r<u(0)<0\). When \(u(0)=0\), \(\dot u(0)=-p_0y(0)<0\), reducing immediately to the negative case. If a trajectory initially has \(u>0\), but crosses \(u=0\) at finite time while \(y>0\), it also reaches prey exhaustion in finite time. It therefore suffices to classify trajectories satisfying \(u(t)>0\) for all \(t\ge0\).

Suppose such an all-time trajectory exists. Since \(\dot u\le-u^2/K\), its decreasing limit is zero, and
\[
\int_0^\infty u(t)^2\,dt\le K u(0)<\infty.
\]
Necessarily \(\int_0^\infty u(t)\,dt=\infty\): otherwise, local differentiability of \(p\) near zero makes \(\int_0^\infty[p(u(t))-p_0]dt\) finite, and the second equation implies that \(y(t)\) approaches a strictly positive limit. Since \(p(u(t))\to p_0>0\), the first equation would then force \(u\) through zero, a contradiction.

For any all-time \(u>0\) trajectory define \(z=u^2/y>0\). Direct differentiation yields the key *exact linear identity*
\[
\dot z=-2p(u)u-A(u)z,\qquad
A(u)=\frac{2u}{K}+p(u)-p_0.
\]
As \(u\downarrow0\), Taylor's formula gives
\[
A(u)=\frac{2-\alpha}{K}u+O(u^2).
\]
When \(\alpha\le2\), there exist \(C>0\) and a late time \(T\) such that \(A(u(t))\ge-Cu(t)^2\) for \(t\ge T\). Thus the integrating factor \(E(t)=\exp(\int_T^t A(u(s))ds)\) satisfies \(E(t)\ge\exp(-CKu(T))>0\). The linear identity gives
\[
\frac{d}{dt}\{E(t)z(t)\}=-2E(t)p(u(t))u(t).
\]
The integral of the right-hand side is negative and divergent, since \(p(u(t))\to p_0>0\), the integrating factor is bounded below by a positive constant, and \(\int_T^\infty u(t)dt=\infty\). This forces \(E(t)z(t)<0\) eventually, contradicting positivity. Hence for \(\alpha\le2\) no positive-predator state can avoid finite-time prey exhaustion. The argument explicitly covers the equality case, where the first-order coefficient of \(A\) vanishes.

Conversely, take \(\alpha>2\), and choose \(0<c<(\alpha-2)/(2Kp_0)\). On the sloped boundary \(y=cu^2\) of the proposed wedge, the outward normal derivative of \(\Phi=y-cu^2\) is
\[
\dot\Phi=cu^3\left[\frac{p(u)-p_0}{u}+\frac2K+2cp(u)\right].
\]
Its bracket tends to \((2-\alpha)/K+2cp_0<0\) as \(u\downarrow0\). Choose \(\varepsilon>0\) so the bracket remains negative for \(0<u<\varepsilon\). The \(u=\varepsilon\) boundary is inward-pointing because \(\dot u<0\); the \(y=cu^2\) boundary is strictly inward-pointing as just shown; the \(y=0\) axis is invariant. Thus the region \(0<u<\varepsilon,\ 0<y<cu^2\) is positively invariant until any hypothetical contact with \(u=0\). Inside it,
\[
-\bigl(1/K+cM\bigr)u^2\le\dot u\le-u^2/K,
\]
where \(M=\max_{r\le x\le r+\varepsilon}P(x)<\infty\). Reciprocal comparison rules out finite-time contact with \(u=0\), while \(u(t)\to0\) and \(0<y(t)<cu(t)^2\to0\). This proves survival and shows the cutoff is sharp.

For the rational response, differentiation gives
\[
P'(x)=\frac{x(bx+2)}{(ax^2+bx+1)^2},
\]
which at \(x=r=K/2\) yields the stated \(\alpha\) formula. In the explicit surviving example \(a=1/2\), \(b=-5/4\), \(K=4\), one may take \(c=1/8\) and \(\varepsilon=1/10\): the bracket above simplifies to
\[
\frac{4u^2-13u-6}{2(2u^2+3u+2)}<0\quad(0<u<1/10).
\]
Indeed its numerator is at most \(1/25-6<0\) in that interval, and its denominator is positive. Therefore this concrete parameter example has a rigorously certified nonempty wedge without relying on an unspecified smallness constant.

## Verification
Run `python verify.py` from a directory containing the standalone artifact; it needs Python 3 and SymPy. The script reconstructs the key ratio identity, the wedge derivative, the rational slope formula, all three exact parameter witnesses, and the explicit inward boundary bracket. It performs algebraic checks, **not** an exhaustive enumeration or proof of the infinite-time statements. Those follow from the comparison and integrating-factor arguments above. All formulas use the unscaled physical positive variables of the displayed ODE.

## Relationship to prior work
El Khateeb, Akter, Kottegoda, and Abou Hasan introduced the negative-\(b\) harvested generalized Holling-III model and analyzed the local nilpotent saddle/elliptic coalescence at \(K=4h\), \(d=P(2h)\) (their Theorem 3.8). That local bifurcation classification, including sign distinctions in \(bh\), is distinct from the present physically constrained, *global* finite-time prey-collapse statement and the sharp \(-KP'(K/2)=2\) positive-state survival threshold. It does not state the ratio identity, the necessary all-time divergence condition, or the explicit positive wedge. These are the specific proposed additions, not a claim to discover the nilpotent coalescence itself.

Etoua and Rousseau previously treated generalized Gause dynamics with prey harvesting and Holling response in the \(b\ge0\) regime; that framework does not cover the negative-\(b\) survival wedge. Saputra, van Veen, and Quispel developed normal-form theory for the double-zero saddle-node/transcritical interaction in a Lotka–Volterra model with constant harvesting. Their local phase portraits provide relevant structural precedent, but their different response and local unfolding statements do not give this complete physical, finite-time Holling-III threshold. General nilpotent normal-form theory may imply some local sector information, and an unlocated prior general theorem might subsume the structural lemma; historical priority beyond the material inspected remains a risk.

## Limitations
The extinction statements mean *first finite-time contact* with the prey boundary, not biological trajectories continued through negative prey densities. The survival wedge is sufficient and open, not the entire survival basin. The theorem makes no claim about positive periodic orbits away from this critical harvest/mortality surface. It does not study demographic stochasticity, variable harvest feedback, or delay. The critical cutoff requires predator mortality exactly equal to \(P(K/2)\) and harvesting exactly at \(K/4\). The historical novelty assessment is based on inspected literature and searches, not a proof of universal priority. No independent validation is claimed.

## References
1. W. El Khateeb, F. Akter, C. Kottegoda, and M. M. Abou Hasan, *Dynamics of a Harvested Predator-Prey Model with a Generalized Holling Type III Response Capturing Group Defense*, arXiv:2610.32306v1, first public 23 October 2026, https://arxiv.org/html/2610.32306v1 .
2. M. A. Etoua and C. Rousseau, *Bifurcation analysis of a generalized Gause model with prey harvesting and a generalized Holling response function of type III*, available at https://dms.umontreal.ca/~rousseac/Etoua_Rousseau_eng.pdf .
3. K. V. I. Saputra, L. van Veen, and G. R. W. Quispel, *The saddle-node-transcritical bifurcation in a population model with constant rate harvesting*, Discrete and Continuous Dynamical Systems B **14** (2010), 233–250, doi:10.3934/dcdsb.2010.14.233, public preprint arXiv:1002.4150.
