# Sharp lag-one covariance freedom under a fixed invariant density

## Finding

Consider two half-branch quadratic interval maps, defined for \(0<b_1<2<b_2<4\). Put
\[
 f_i(u)=(4-2b_i)u^2+b_i u,\qquad 0\le u\le\tfrac12,
\]
and extend each to \([0,1)\) by \(\tau_i(u+j/2)=f_i(u)\), where \(j\in\{0,1\}\) and \(0\le u<1/2\). At a point \(x\), independently of previous random choices conditional on the current state, apply \(\tau_1\) with probability \(p(x)\), otherwise \(\tau_2\). All weighting functions \(p:[0,1)\to[0,1]\) in this note are Lebesgue measurable.

Define
\[
 \kappa=\frac{b_2-2}{2(b_2-b_1)},\qquad
 S(u)=2\kappa f_1'(u),\qquad
 \Delta(u)=f_2(u)-f_1(u)=(b_2-b_1)u(1-2u).
\]
The random transition kernel preserves Lebesgue probability on \([0,1)\) **if and only if**
\[
 \boxed{p(u)+p(u+\tfrac12)=S(u)\quad\text{for Lebesgue-a.e. }u\in(0,\tfrac12).}
\]
Consequently, this is an entire infinite-dimensional family of invariant-density-preserving randomizations, parameterized by an arbitrary measurable function \(h(u)=p(u+1/2)\) satisfying
\[
 \boxed{h_-(u):=\max(0,S(u)-1)\ \le h(u)\le\ h_+(u):=\min(1,S(u)).}
\]
Its complementary weight is \(p(u)=S(u)-h(u)\). Throughout this family, if the initial state is Lebesgue-uniform, the selected map labels are independent and identically distributed with probabilities \(2\kappa\) and \(1-2\kappa\). This invariance of the switching law does **not** force the temporal correlations of the state to agree.

In fact, let \(C(p)=\operatorname{Cov}(X_0,X_1)\) under this stationary initialization and define
\[
 C_0=\int_0^{1/2}\!\left[(2u+\tfrac12)f_2(u)-uS(u)\Delta(u)\right]du-\tfrac14.
\]
Then the exact **sharp attainable interval**, with both endpoints attained, is
\[
 \boxed{C_{\min}\le C(p)\le C_{\max}},\qquad
 C_{\min}=C_0-\tfrac12\int_0^{1/2}\!h_+(u)\Delta(u)\,du,
 \quad C_{\max}=C_0-\tfrac12\int_0^{1/2}\!h_-(u)\Delta(u)\,du.
\]
Every value in this interval is attained by a valid measurable probability function. Its width is strictly positive for every allowed parameter pair:
\[
 \boxed{C_{\max}-C_{\min}=\frac{b_2-b_1}{2}\int_0^{1/2}\!u(1-2u)\min\{S(u),2-S(u)\}\,du>0.}
\]
For the parameter values \(b_1=1/2\), \(b_2=7/2\) featured in the motivating article, the sharp endpoints simplify to
\[
 \boxed{\frac{223}{15360}\ \le\ \operatorname{Cov}(X_0,X_1)\ \le\ \frac{913}{15360},}
\]
with width exactly \(23/512\). The previously exhibited half-symmetric randomization lies strictly between them and has covariance \(71/1920\). Thus a fixed uniform one-time law and fixed independent map-selection law leave a nontrivial, completely quantified freedom in a two-time observable.

## Assumptions and scope

All intervals and equalities are understood up to boundary sets of Lebesgue measure zero. On each step the auxiliary selection randomness is fresh, and the next state is determined by the chosen map. Stationarity refers specifically to the Lebesgue probability law: no uniqueness of invariant probability for every admissible measurable control is assumed. Both the control classification and the covariance bounds hold for all real \(0<b_1<2<b_2<4\), without any continuity, smoothness or half-periodicity condition on the selection probability.

## Proof

**Full branches and the known balanced solution.** The functions \(f_i\) map \([0,1/2]\) increasingly onto \([0,1]\), because \(f_i(0)=0\), \(f_i(1/2)=1\), and \(f_i'>0\) in the stated parameter region. Moreover \(f_1(u)<f_2(u)\) for \(0<u<1/2\). Set
\[
 \kappa_2=\frac{2-b_1}{2(b_2-b_1)}.
\]
Direct coefficient comparison gives \(\kappa+\kappa_2=1/2\) and
\[
 \kappa f_1'(u)+\kappa_2 f_2'(u)=1\quad (0\le u\le1/2).
\]
Therefore \(0<S(u)<2\) in the open half interval. For the symmetric choice \(p(u)=p(u+1/2)=\kappa f_1'(u)\), each of the two inverse half branches contributes \(\kappa\) for the first map and \(\kappa_2\) for the second to the Perron--Frobenius density, so Lebesgue probability is invariant. This symmetric construction is prior work.

**Necessity for every measurable control.** Write \(p_j(u)=p(u+j/2)\), let \(w(u)=p_0(u)+p_1(u)\), and let \(W(u)=\int_0^u w(t)\,dt\). For \(0\le z\le1\), the cumulative distribution of the next state from a uniform starting state is, exactly,
\[
 W(f_1^{-1}(z))+2f_2^{-1}(z)-W(f_2^{-1}(z)).
\]
Hence uniform stationarity is equivalent to the identity of this expression with \(z\). The balanced control has \(w_*(u)=S(u)\), primitive \(W_*(u)=2\kappa f_1(u)\), and satisfies that identity. Subtract the two cumulative identities and put \(H=W-W_*\). On replacing \(z\) by \(f_1(u)\), one obtains
\[
 H(u)=H(t(u)),\qquad t(u)=f_2^{-1}(f_1(u)).
\]
For every \(u\in(0,1/2)\), strict inequality \(f_1(u)<f_2(u)\) implies \(0<t(u)<u\). Continuity, monotonicity and the absence of an interior fixed point imply \(t^n(u)\to0\). Because \(H\) is continuous and \(H(0)=0\), iteration gives \(H(u)=0\). This holds at the endpoints by continuity as well, so \(W=W_*\). Differentiating these absolutely continuous primitives yields \(w=S\) almost everywhere.

**Sufficiency and exact parameterization.** Conversely, if \(p_0+p_1=S\), the Perron--Frobenius density at every interior \(z\) is
\[
 \frac{S(f_1^{-1}(z))}{f_1'(f_1^{-1}(z))}
 +\frac{2-S(f_2^{-1}(z))}{f_2'(f_2^{-1}(z))}
 =2\kappa+2\kappa_2=1.
\]
The two probability constraints \(0\le p_0,p_1\le1\) are exactly \(h_-\le h=p_1\le h_+\); both bounds are admissible because \(0<S<2\).

**Sharp covariance envelope.** Since both consecutive stationary coordinates have mean \(1/2\), their covariance equals \(\mathbb E[X_0X_1]-1/4\). Conditioning on the starting half and the chosen map, and using \(p_0=S-h\), yields
\[
 C(p)=\int_0^{1/2}\!\left[(2u+\tfrac12)f_2(u)-(uS(u)+\tfrac12h(u))\Delta(u)\right]du-\tfrac14
 =C_0-\tfrac12\int_0^{1/2}h(u)\Delta(u)\,du.
\]
The kernel \(\Delta(u)>0\) in the open half interval. Consequently, this linear functional is minimized by \(h=h_+\) and maximized by \(h=h_-\), proving both optimal endpoints. For \(0\le\theta\le1\), the admissible interpolation \(h=(1-\theta)h_+ +\theta h_-\) attains every intermediate covariance. Because \(h_+-h_-=\min(S,2-S)\) and this is positive inside the interval, the stated sharp positive width follows.

For \((b_1,b_2)=(1/2,7/2)\), the exact polynomials are
\[
 f_1(u)=3u^2+u/2,\quad f_2(u)=-3u^2+7u/2,\quad S(u)=1/4+3u.
\]
Thus \(h_-=0\) for \(u\le1/4\), and \(h_-=S-1\) for \(u\ge1/4\); similarly \(h_+=S\) and \(h_+=1\) on those subintervals, respectively. Integrating the degree-at-most-four rational polynomials gives the exact covariance endpoints \(223/15360\) and \(913/15360\), and the halfway control \(h=S/2\) gives \(71/1920\).

**Identical map-selection statistics.** For any stationary allowed control, the joint density of the event that map one is selected and the next coordinate equals \(z\) is
\[
 \frac{p_0(f_1^{-1}(z))+p_1(f_1^{-1}(z))}{f_1'(f_1^{-1}(z))}
 =2\kappa.
\]
For map two it is \(2\kappa_2\). Hence the selected map at a given step is independent of the following coordinate and has probabilities \((2\kappa,2\kappa_2)\). Fresh selection randomness and the Markov property then inductively show that the entire sequence of selected-map labels is independent and identically distributed, for every one of the asymmetric admissible controls.

## Verification

Run `python3 verify.py` with Python 3's standard library. Its exact fraction-polynomial integrator independently checks the canonical rational covariance endpoints and width, the symmetric intermediate covariance, admissibility of the two extremal controls, and the transfer-balance identities at rational test points for six parameter pairs. The observed output is `SHARP_COVARIANCE_INTERVAL 223/15360 913/15360` followed by `VERIFY_OK`. These finite evaluations test arithmetic and formulas; the all-real-parameter if-and-only-if classification, the optimality proof, and the independence statement are analytical.

## Relationship to prior work

Góra, Li, Boyarsky and Proppe introduced these half-shifted quadratic boundary maps, showed that neither deterministic map need have an absolutely continuous invariant measure, and constructed a symmetric state-dependent randomization preserving Lebesgue measure. Their Section 5 derives the inverse-branch balance equation, then **restricts** the sought probability to be equal on the two half intervals. The novelty here is classification without that restriction and the exact range of a temporal covariance over every stationary control. The paper's existence theorem, symmetric example and general functional-equation technique remain prior art. Góra and Boyarsky (2006) analyze attainable densities and related inverse-branch representations, particularly in semi-Markov settings; the current claim is a sharp two-time observable range for a fixed nonlinear boundary pair and fixed invariant density. No generic novelty or uniqueness theorem for unrelated random maps is asserted.

## Limitations

The covariance bounds are specific to the coordinate observable and lag one, not to every time-lagged statistic or every observable. The conclusion that selected-map labels are independent is not a claim that the full coordinate process is independent or that arbitrary half-branch/choice pairs are independent. Measurable controls need not generate an ergodic stationary coordinate process; no pathwise Lyapunov exponent or uniqueness of stationary state is inferred. A publication-priority claim is limited by the scope of inspected sources and searches.

## References

1. P. Góra, Z. Li, A. Boyarsky and H. Proppe, *Toward A Mathematical Holographic Principle*, arXiv:1404.7455v1, first publicly submitted 2014-04-29; especially Sections 4, 5 and 8. https://arxiv.org/abs/1404.7455
2. P. Góra and A. Boyarsky, *Attainable densities for random maps*, Journal of Mathematical Analysis and Applications 317 (2006), 257--270, DOI:10.1016/j.jmaa.2005.11.061. https://doi.org/10.1016/j.jmaa.2005.11.061
3. P. Góra and A. Boyarsky, *Absolutely continuous invariant measures for position dependent random maps*, Journal of Mathematical Analysis and Applications 278 (2003), 225--242, cited for the general random-map framework. https://doi.org/10.1016/S0022-247X(02)00579-2
