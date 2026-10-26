# An exact quadratic interaction threshold and nine-equilibrium phase diagram for two reinforced urns

## Finding

For the two-urn, two-colour model with quadratic reinforcement, the critical probability of drawing from the combined composition has the exact value
\[
 p_2=1-\frac{1}{\sqrt 2}=0.292893218813\ldots.
\]
The equilibrium set of the limiting mean-field vector field has **exactly nine points** for \(0<p<p_2\), **exactly five** for \(p_2\le p<1/2\), and **exactly three** for \(1/2\le p\le1\). For \(0<p<p_2\) two noncentral anti-diagonal points are linearly asymptotically stable; for \(p_2<p<1/2\), they are linearly unstable. These yield the sharp stochastic consequence that the probability of domination is strictly below one when \(0<p<p_2\), and equals one when \(p>p_2\), via the cited stochastic-approximation theorem. The behavior exactly at \(p=p_2\) is not determined here.

The four additional, non-anti-diagonal points exist only below \(p_2\). They merge, in two pairs, into the two anti-diagonal points as \(p\uparrow p_2\). The count and parameterization below are exact over the full invariant square.

## Assumptions and scope

Fix \(p\in(0,1]\). Each of two urns receives one new ball at each discrete time, with black probability, independently conditional on the current counts,
\[
 (1-p)\frac{B_i^2}{B_i^2+R_i^2}
 +p\frac{(B_1+B_2)^2}{(B_1+B_2)^2+(R_1+R_2)^2},
\]
with the usual requirement that both colours occur initially somewhere in the system and with denominators defined. Write \(x,y\in[0,1]\) for the limiting scaled local black proportions. The associated ODE is
\[
\dot x=-x+(1-p)h(x)+ph((x+y)/2),\qquad
\dot y=-y+(1-p)h(y)+ph((x+y)/2),
\]
where \(h(u)=u^2/(u^2+(1-u)^2)\). For urns with unequal finite initial totals, the mean-field ODE remains this one; exact finite-time conditional probabilities use the actual total ball counts. This result classifies equilibria for every \(p\) in the stated range and invokes published stochastic-approximation results for positive-probability attraction and nonconvergence to linearly unstable equilibria. No statement about the distribution at the critical value is assumed.

## Proof

**1. Location of every equilibrium.** Because \(h(u)-u\) has the same sign as \(2u-1\) for \(0<u<1\), if both coordinates lie strictly below \(1/2\) their drift sum is negative; if both lie strictly above \(1/2\) it is positive. The same monotonicity handles a coordinate equal to \(1/2\). For \(p>0\), a boundary equilibrium with one coordinate \(0\) or \(1\) forces the other coordinate to agree. On the diagonal, \(h(x)=x\) has only \(0,1/2,1\). Thus every other equilibrium has, after swapping coordinates, \(0<x<1/2<y<1\).

**2. Anti-diagonal solutions and their stability.** Put \(a=2x-1\), \(b=2y-1\). Then
\[
 h((1+a)/2)=\frac12+\frac{a}{1+a^2}.
\]
On the anti-diagonal \(a=-b=-z\) with \(z>0\), the two equilibrium equations reduce to \(z^2=1-2p\). They give two noncentral points exactly for \(0<p<1/2\):
\[
(x,y)=\left(\frac{1-z}{2},\frac{1+z}{2}\right),\quad
\left(\frac{1+z}{2},\frac{1-z}{2}\right),\qquad z=\sqrt{1-2p}.
\]
The Jacobian at either has eigenvalues
\[
\lambda_-=-\frac{2z^2}{1+z^2},\qquad
\lambda_+=\frac{1-2z^2-z^4}{1+z^2}.
\]
The first is strictly negative. The second is negative iff \(z^2>\sqrt2-1\), equivalently \(p<1-1/\sqrt2\), and is positive iff \(p>1-1/\sqrt2\) (within \(p<1/2\)). At equality its value is zero and linear stability is inconclusive. The central equilibrium is linearly unstable for every \(p\), since its diagonal-direction eigenvalue is one. Both corners are stable.

**3. Polynomial elimination for the off-anti-diagonal branch.** Let \(s=a+b\) and \(t=ab\). We know \(t\in(-1,0)\). Since
\[
h((x+y)/2)=\frac12+\frac{2s}{4+s^2},
\]
the equilibrium equations, after division by positive factors, are
\[
\frac{a(a^2+2p-1)}{1+a^2}=\frac{4ps}{4+s^2},\qquad
\frac{b(b^2+2p-1)}{1+b^2}=\frac{4ps}{4+s^2}.
\]
For \(s\ne0\) and \(a\ne b\), subtracting gives
\[
D=s^2+t^2-2pt+2p-1=0.
\]
Clearing denominators in the sum gives \(sK=0\), with
\[
K=s^4+(3-3t-2p)s^2+(8p-12)t-4.
\]
Solving \(D=0\) for \(p\) and substituting in \(K\) yields the exact factorization
\[
 p=\frac{1-s^2-t^2}{2(1-t)},\quad
 K=\frac{(s^2-2t+2)\big(s^2(t-2)-2t^2+4t+2\big)}{t-1}.
\]
Because \(s^2-2t+2>0\), it follows that
\[
 s^2=\frac{2(t^2-2t-1)}{t-2},\qquad
 p=\frac{t(t^2-5)}{2(t-2)(t-1)}=:P(t).
\]
The constraints \(s^2>0\), \(-1<t<0\) force \(1-\sqrt2<t<0\). Conversely for each \(t\) in precisely that interval, both signs \(s=\pm\sqrt{2(t^2-2t-1)/(t-2)}\) are admissible: the identity
\[
 (1+t)^2-s^2=\frac{t(t-1)^2}{t-2}>0
\]
guarantees that the two roots \(a,b\) of \(u^2-su+t=0\) lie strictly between \(-1\) and \(1\) and have opposite signs. All substitutions are reversible because the cleared denominators are strictly positive. Each choice of \(s\) produces two solutions via coordinate swap, hence four off-anti-diagonal equilibria whenever the parameter equation has a solution.

The derivative
\[
 P'(t)=\frac{t^4-6t^3+11t^2-10}{2(t-2)^2(t-1)^2}<0
\]
on \(1-\sqrt2<t<0\). To check the last sign, use \(-1/2<t<0\) to bound its numerator above by \(1/16+6/8+11/4-10<0\). Finally
\[
 P(1-\sqrt2)=1-\frac1{\sqrt2},\qquad P(0)=0.
\]
Thus there are exactly four off-anti-diagonal equilibria for \(0<p<p_2\), none for \(p\ge p_2\). They approach the two noncentral anti-diagonal equilibria as \(t\downarrow1-\sqrt2\) and \(s\to0\). This completes the count: three diagonal points, plus two anti-diagonal points for \(p<1/2\), plus four additional points only for \(p<p_2\).

**4. Probability-one domination boundary.** The cited stochastic-approximation results of Qin, as used in Xia's Proposition 2.1, give almost-sure convergence of the urn proportions to an equilibrium, positive probability of convergence to an asymptotically stable equilibrium, and zero probability of convergence to an equilibrium with a positive Jacobian eigenvalue. For every \(0<p<p_2\), the noncentral anti-diagonal points are asymptotically stable, so the probability of non-domination is positive. For every \(p>p_2\), every nondominating equilibrium is either absent or has a positive eigenvalue (the anti-diagonal pair for \(p<1/2\), or the center for all \(p\)), hence the probability of domination is one. The definitions of the two sharp thresholds therefore give \(p_2=1-1/\sqrt2\), regardless of the still-unresolved status of equality at \(p=p_2\).

## Verification

The standalone `verify_quadratic_urn.py` checks symbolic elimination identities, positivity/admissibility formulas, the derivative and endpoint threshold, the Jacobian eigenvalues, and substitutions of four rational \(t\)-values into both original equilibrium equations. Its run recorded 27 successful checks. The proof of the continuum classification is the displayed monotonicity and sign argument; finite samples are not offered as exhaustive proof. Execute with `python verify_quadratic_urn.py` using Python 3 and SymPy. The included `verification_output.txt` records one replay output.

## Relationship to prior work

Xia (2026), *The phase transition for domination in two interacting urns with power reinforcement*, arXiv:2607.22438, introduces the same model and proves that an implicit deterministic threshold equals the two probabilistic transition parameters for all reinforcement exponents greater than one. Its Section 3 establishes the generic anti-diagonal branch and abstract stability threshold; Sections 4–9 develop an analytic scalar reduction; Section 10 discusses exponent dependence. The exact quadratic value and nine/five/three equilibrium census derived above are special, additional algebraic evaluations, **not** a claim to have independently proved Xia's general stochastic threshold theorem. Qin (2023/2024), arXiv:2311.13480, provides the prior stochastic approximation and lower-bound framework. Launay (2011), arXiv:1101.1410, introduced related interacting urns, rather than this quadratic exact census.

## Limitations

The result treats two urns with exponent exactly two. It does not prove domination or non-domination at the critical parameter itself, classify the stability type of each off-anti-diagonal equilibrium, generalize to more urns or other exponents, or replace the published stochastic approximation hypotheses. Independent mathematical validation has not been performed. Historical coverage by a specialized quadratic-urn analysis using different terminology remains a priority risk, despite the targeted literature comparisons.

## References

1. Jiaming Xia, *The phase transition for domination in two interacting urns with power reinforcement*, arXiv:2607.22438, first public July 24, 2026, https://arxiv.org/abs/2607.22438 (especially Proposition 2.1, Lemma 3.1, Theorem 2.2, and Sections 4–10).
2. Shuo Qin, *Interacting urn models with strong reinforcement*, arXiv:2311.13480, first public November 22, 2023, https://arxiv.org/abs/2311.13480.
3. Mickaël Launay, *Interacting Urn Models*, arXiv:1101.1410, first public 2011, https://arxiv.org/abs/1101.1410.
