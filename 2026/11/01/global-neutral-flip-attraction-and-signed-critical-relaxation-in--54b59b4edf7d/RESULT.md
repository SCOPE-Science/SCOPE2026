# Global neutral-flip attraction and signed critical relaxation in an entropic congestion map

## Finding

Let \(b\in(0,1)\), let \(s=b(1-b)\), and consider the two-strategy multiplicative-weights interval map
\[
f_{a,b}(x)=\frac{x}{x+(1-x)e^{a(x-b)}}\quad(0\le x\le1),
\qquad a>0.
\]
Its critical fixed-point flip parameter is \(a_c=2/s\). The following statements hold.

**Exact global flip boundary.** Every trajectory starting in \((0,1)\) converges to \(b\) whenever \(0<a\le a_c\). For \(a>a_c\) there is exactly one primitive period-two orbit, and therefore \(b\) is not globally attracting. The cycle has points \(b-d,b+d\), where \(d\in(0,\min\{b,1-b\})\) is the unique solution of
\[
a=\frac{\operatorname{logit}(b+d)-\operatorname{logit}(b-d)}{d},\qquad
\operatorname{logit}(x)=\log\frac{x}{1-x}.
\]
As \(a\downarrow a_c\) from above, its amplitude satisfies
\[
\frac{d^2}{a-a_c}\longrightarrow\frac{3s^3}{2(1-3s)}.
\]

**Critical relaxation, including asymmetry.** Fix \(a=a_c\), set \(x_n=f_{a_c,b}^n(x_0)\), and put
\[
E_b=\{x_0\in(0,1):x_n=b\text{ for at least one }n\ge0\}.
\]
The set \(E_b\) is countable. For each \(x_0\notin E_b\), the signs of \(x_n-b\) eventually alternate and
\[
\boxed{\lim_{n\to\infty}n(x_n-b)^2=\frac{3s^2}{4(1-3s)}.}
\]
More sharply, put \(u_n=\operatorname{logit}(x_n)-\operatorname{logit}(b)\), \(\gamma=\frac43(1-3s)\), and \(\delta=\frac23(2b-1)(1-3s)\). For each \(x_0\notin E_b\), the sign \(\epsilon=\operatorname{sgn}(u_{2m})\) is eventually constant and
\[
\boxed{\frac1{u_{2m}^{2}}=2\gamma m-\frac{4\delta\epsilon}{\sqrt{2\gamma}}\sqrt m+O(\log m).}
\]
At the symmetric parameter \(b=1/2\), where the square-root correction vanishes, the stronger exact logarithmic law holds:
\[
\boxed{\frac1{u_{2m}^{2}}=\frac23m+\frac3{20}\log m+O(1).}
\]
All asymptotics are for \(m\to\infty\), with constants in the remainder allowed to depend on \(b\) and the initial condition. Points of \(E_b\) reach \(b\) in finitely many steps and then stay there.

## Assumptions and scope

The parameters are real, \(a>0\) and \(0<b<1\); initial conditions lie strictly inside \((0,1)\). The value of the map at either endpoint is fixed and no endpoint is claimed to converge to the interior equilibrium. The two-cycle assertion counts distinct unordered **primitive** period-two orbits and does not claim stability for every \(a>a_c\). There is no assumption of global monotonicity of the map. Asymptotic signs and inverse squares exclude precisely those orbits that hit the fixed point in finite time.

## Proof

**1. Cycle equation and the sharp threshold.** The exact log-odds identity is
\[
\operatorname{logit}(f_{a,b}(x))=\operatorname{logit}(x)-a(x-b).
\]
For a primitive two-cycle \(x_-\ne x_+\), summing both increments gives \(x_-+x_+=2b\). Thus \(x_-=b-d\), \(x_+=b+d\), for \(0<d<\min\{b,1-b\}\), and one of the log-odds increments gives the displayed equation for \(a\). Conversely that equation verifies both legs of the orbit.

Writing \(L(x)=\operatorname{logit}(x)\), its parameter function is
\[
Q_b(d)=\int_{-1}^{1}L'(b+td)\,dt.
\]
We have \(L'(x)=1/[x(1-x)]\) and \(L'''(x)=2/x^3+2/(1-x)^3>0\). Consequently,
\[
Q_b'(d)=\int_0^1 t\,[L''(b+td)-L''(b-td)]\,dt>0.
\]
Also \(Q_b(0+)=2L'(b)=2/s=a_c\), and \(Q_b(d)\to+\infty\) as \(d\uparrow\min\{b,1-b\}\). This proves nonexistence of primitive two-cycles at or below \(a_c\), and existence and uniqueness above it. Expanding the same symmetric difference yields
\[
Q_b(d)=\frac2s+\frac{2(1-3s)}{3s^3}d^2+O(d^4),
\]
which gives the stated amplitude limit; \(1-3s\ge1/4>0\).

**2. Global convergence at and below the flip.** The continuous self-map \(f_{a,b}:[0,1]\to[0,1]\) has no nontrivial period-two orbit when \(a\le a_c\). The classical Coppel convergence theorem for continuous interval maps without a primitive two-cycle states that each forward orbit converges to a fixed point. The only fixed points are \(0,b,1\), by the strict log-odds identity in the interior. For \(0<x<b\) one has \(f_{a,b}(x)>x\), and for \(b<x<1\) one has \(f_{a,b}(x)<x\). Therefore an interior orbit cannot converge to either boundary fixed point: an eventually-near-zero positive orbit would have to increase at every subsequent step, and analogously near one. The limit is \(b\), also at \(a=a_c\). For \(a>a_c\) the primitive two-cycle prevents global attraction.

**3. Critical coordinate and exact local coefficients.** Fix \(a=a_c\) and let \(u=L(x)-L(b)\). By the exponential-odds identity and \(s=b(1-b)\), its exact induced map is
\[
T_b(u)=u-\frac{2(e^u-1)}{1+b(e^u-1)}.
\]
Its Taylor expansion at zero is
\[
T_b(u)=-u+A u^2+B u^3+C u^4+D u^5+O(u^6),
\]
where
\[
A=2b-1,\quad B=-\frac{1-6s}{3},\quad
C=\frac{(2b-1)(1-12s)}{12},
\]
\[
D=-\frac{120b^4-240b^3+150b^2-30b+1}{60}.
\]
Composition gives the two-step normal form
\[
G_b(u)=T_b^2(u)=u-\gamma u^3+\delta u^4+\eta u^5+O(u^6),
\]
\[
\gamma=\frac43(1-3s)>0,\qquad
\delta=\frac23(2b-1)(1-3s),\qquad
\eta=\frac{3-5s}{15}.
\]
These coefficients are consequences of an identity of analytic functions, rather than polynomial fitting; a standalone exact-series verifier is included.

**4. Universal rate and signed correction.** By step 2, \(u_n\to0\) for every interior start. Unless \(u_n=0\) at some finite step, it remains nonzero. Near zero, \(T_b\) reverses sign and \(G_b\) preserves sign; hence for all sufficiently large \(m\), \(u_{2m}\) has a fixed sign \(\epsilon\). Put \(v_m=u_{2m}^{-2}\). The normal form gives
\[
v_{m+1}-v_m=2\gamma-2\delta u_{2m}+(3\gamma^2-2\eta)u_{2m}^2+O(u_{2m}^3).
\]
Since \(u_{2m}\to0\), the difference tends to \(2\gamma\); summation yields \(v_m/m\to2\gamma\). Consequently \(u_{2m}=\epsilon(2\gamma m)^{-1/2}(1+o(1))\). The displayed increment now gives first \(v_m=2\gamma m+O(\sqrt m)\), and therefore
\[
u_{2m}=\frac{\epsilon}{\sqrt{2\gamma m}}+O(m^{-1}).
\]
Substituting this sharper estimate back into the increments and using \(\sum_{k\le m}k^{-1/2}=2\sqrt m+O(1)\) yields
\[
v_m=2\gamma m-\frac{4\delta\epsilon}{\sqrt{2\gamma}}\sqrt m+O(\log m).
\]
The one-step map reverses the leading sign without changing its square, so \(n u_n^2\to1/\gamma\) for both parities. Since \(x-b=s u+O(u^2)\), the asserted \(n(x_n-b)^2\) limit follows.

At \(b=1/2\) the map \(T_b\) is odd, so the two-step map is odd and the next error in the increment is \(O(u_{2m}^4)\), rather than merely cubic. Here \(\gamma=1/3\), \(\delta=0\), and \(\eta=7/60\). Thus
\[
v_{m+1}-v_m=\frac23+\frac{1}{10v_m}+O(v_m^{-2}).
\]
As \(v_m\sim2m/3\), summing gives \(v_m=\frac23m+\frac3{20}\log m+O(1)\); the bounded remainder follows because \(v_m=\frac23m+O(\log m)\) makes the error in replacing \(1/v_m\) by \(3/(2m)\) summable.

**5. Exceptional starts.** For each fixed \(k\ge0\), \(f_{a_c,b}^k\) is real analytic on \((0,1)\) and continuously extends to \(0\) with value \(0\). Hence \(f_{a_c,b}^k-b\) is not identically zero, so its zeros form a countable subset of \((0,1)\). The union over \(k\) is countable, proving the assertion about \(E_b\).

## Verification

Run `python verification.py` with Python and SymPy. The included code independently expands the exact logit map to fifth order using truncated exponential/geometric polynomials, composes the jets, and verifies the rational formulas for \(\gamma,\delta,\eta\) and the symmetric logarithmic coefficient. It also checks 20 representative cycle equations, 10 near-birth amplitude scalings, and 15 critical trajectories of 160000 iterates each. All checks passed before packaging. These finite tests are not substitutes for the all-parameter proof above.

## Relationship to prior work

Chotibut–Falniowski–Misiurewicz–Piliouras introduced this map and proved the entire symmetric global convergence regime \(b=1/2\), including its neutral endpoint, in Theorem 3.9; their Conjecture 3.10 asked for convergence for arbitrary \(b\) up to the critical line. Bielawski and collaborators proved global convergence in the strictly attracting region through a negative-third-derivative criterion (Theorem 6.2, 2021). The claims here are **not** that either the strict region or the symmetric endpoint were unknown: the added conclusions are the asymmetric neutral equality case, a global all-parameter two-cycle count, and explicit physical-iteration critical relaxation including the signed correction and symmetric logarithm. The all-parameter absence of two-cycles follows by strengthening the same secant-derivative idea used in the 2021 work; the originality assessment relies on the newly quantified critical asymptotics and on their combination with the exact global endpoint.

## Limitations

The critical-rate assertions concern the diagonal one-dimensional MWU reduction and do not establish convergence of arbitrary off-diagonal states in a two-agent game. The one-dimensional Coppel theorem and the general mechanism of a parabolic flip are classical ingredients; neither is claimed as new. No stability or global basin classification is claimed for the newly born cycle at parameter values far above the threshold. Literature and research-record search reduces but does not remove the risk that an unindexed paper already states the same exact endpoint correction formulas. No independent mathematical audit has been performed.

## References

1. T. Chotibut, F. Falniowski, M. Misiurewicz and G. Piliouras, *Family of chaotic maps from game theory*, arXiv:1807.06831v1, first posted 2018-07-18. See Theorems 3.8–3.9 and Conjecture 3.10. https://arxiv.org/abs/1807.06831
2. J. Bielawski, T. Chotibut, F. Falniowski, G. Kosiorowski, M. Misiurewicz and G. Piliouras, *Follow-the-Regularized-Leader Routes to Chaos in Routing Games*, arXiv:2102.07974v1, first posted 2021-02-16. See Lemma 6.1, Theorem 6.2 and Corollary 6.3. https://arxiv.org/abs/2102.07974
3. F. Falniowski et al., *The route to chaos in routing games: When is Price of Anarchy too optimistic?*, arXiv:1906.02486, 2019. https://arxiv.org/abs/1906.02486
4. W. A. Coppel, *The solution of equations by iteration*, Proceedings of the Cambridge Philosophical Society **51** (1955), 41–43, for the classical interval-map convergence principle.
