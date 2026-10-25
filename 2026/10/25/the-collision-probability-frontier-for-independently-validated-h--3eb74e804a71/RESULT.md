# The collision-probability frontier for independently validated hypergradient steps on coordinate-sparse quadratics

## Finding
Fix an integer \(d\ge 2\), a curvature \(h>0\), and sampling probabilities \(p_i>0\) with \(\sum_{i=1}^d p_i=1\). Put \(c=\sum_{i=1}^d p_i^2\). For the separable sampled losses
\[
f_i(x)=\frac{h}{2p_i}x_i^2,\qquad f(x)=\sum_{i=1}^d p_if_i(x)=\frac h2\|x\|_2^2,
\]
use independent update and validation indices \(\xi,\zeta\) with common distribution \(p\). The expected normalized out-of-sample hypergradient feedback is strictly convex in the scalar trial step \(\alpha\) and has the unique minimizer
\[
\boxed{\alpha_*=\frac ch}. 
\]
Freeze the step at this *population feedback minimizer*. Both the raw sampled-gradient iteration and the version which retains a proposed iterate only when its independent validation loss does not exceed the old validation loss converge to \(0\) almost surely from **every** initial vector if and only if
\[
\boxed{\sum_{i=1}^d p_i^2<2\min_{1\le i\le d}p_i}.\tag{1}
\]
For the independently validated iteration, this equivalence holds for **every measurable rule for resolving equal validation losses**, including always accepting or always rejecting ties. When (1) fails, any initial point with nonzero component in a minimum-probability coordinate fails to approach the minimizer under every such rule.

For \(d=2\), writing \(p_1=p\), the stability band is exactly
\[
\boxed{1-\frac1{\sqrt2}<p<\frac1{\sqrt2}}.
\]
For \(d\ge2\), if only a uniform lower bound \(p_i\ge m\) is known, where \(0<m\le1/d\), **every** admissible probability vector has property (1) if and only if
\[
\boxed{m>\frac1{\sqrt d(\sqrt d+1)}}.\tag{2}
\]
At and below this universal threshold, an extremal distribution violates (1).

An explicit four-component, equally sampled finite-sum example has \(p=(1/4,3/4)\), \(h=1\), \(\alpha_*=5/8\). For the infrequently sampled coordinate, the unguarded squared-error factor is \(21/16\); under validation with ties always accepted, the factor is \(79/64\), both strictly greater than one, even though \(f(x)=\|x\|_2^2/2\) is strongly convex and every sampled loss shares its unique minimizer.

## Assumptions and scope
The state is \(x\in\mathbb R^d\); indices are sampled independently across iterations and independent of the past. The objective is an exact expectation over \(d\) component losses. A finite uniform-component realization is available whenever the probabilities are rational, by repeating each sampled loss in proportion to its probability. The normalized feedback is defined at states with \(x_i\ne0\) for every \(i\), which makes its sampled-gradient denominator positive; its expectation there is independent of the state. The frozen-step iterations are defined for all states, including zero components.

For a trial \(\alpha\in\mathbb R\), write \(y=x-\alpha\nabla f_\xi(x)\). When \(\nabla f_\xi(x)\ne0\), the feedback is
\[
H_{x,\xi,\zeta}(\alpha)=\frac{f_\zeta(y)-f_\zeta(x)}{\|\nabla f_\xi(x)\|_2^2}.
\]
The *unguarded* update always sets the next iterate to \(y\). The *validation-gated* update selects any minimizer of \(f_\zeta\) over the two-element set \(\{x,y\}\); either value may be selected on a tie. All convergence claims use the single scalar \(\alpha=\alpha_*\), not an evolving online-learned step. The theorem does **not** assert a property of the full time-varying online-feedback algorithm.

## Proof
**Population feedback.** Conditional on \(\xi=i\), \(\nabla f_i(x)=(h/p_i)x_ie_i\), so
\[
y_i=(1-\alpha h/p_i)x_i,\quad y_j=x_j\ (j\ne i).
\]
When \(\zeta\ne i\), the numerator of \(H\) is zero. When \(\zeta=i\), direct cancellation, valid for \(x_i\ne0\), gives
\[
H_{x,i,i}(\alpha)=-\alpha+\frac{h\alpha^2}{2p_i}.
\]
Multiplying by the independent-collision probabilities \(p_i^2\) and summing shows
\[
\mathbb E_{\xi,\zeta}H_{x,\xi,\zeta}(\alpha)=-c\alpha+\frac h2\alpha^2
=\frac h2(\alpha-c/h)^2-\frac{c^2}{2h}.
\]
This proves the asserted unique feedback minimizer.

**Uniform almost-sure convergence under arbitrary validation tie rules.** At \(\alpha=c/h\), any proposed update of coordinate \(i\) multiplies that coordinate by
\[
m_i=1-c/p_i.
\]
All other coordinates are unchanged. If \(c<2p_i\), then \(|m_i|<1\). Independently of the validation index and tie selection, any accepted update weakly decreases \(|x_i|\), and all rejections leave it unchanged. On the positive-probability event \(\xi=\zeta=i\), whose probability is \(p_i^2\), a nonzero \(x_i\) strictly reduces the sampled validation loss, so the update is accepted; if \(x_i=0\), it remains zero. The events occur infinitely often almost surely for every \(i\) by independence, hence \(|x_{k,i}|\to0\). This proves sufficiency for all states and all tie decisions. For the raw iteration, \(\xi=i\) infinitely often almost surely and likewise gives convergence.

Conversely, if \(c\ge2p_i\), then \(m_i\le-1\). Every possible accepted update of coordinate \(i\) weakly increases its absolute value, and a rejection leaves it unchanged. Consequently \(|x_{k,i}|\ge |x_{0,i}|\) pathwise, for all iterations, for every tie decision, whenever \(x_{0,i}\ne0\). The raw iteration is likewise nonconvergent. Since \(c<2p_i\) must hold for every coordinate, (1) is necessary and sufficient.

**Exact mean-square factor of the raw method.** Its coordinate multipliers are independent over iterations. Thus, for every initial point and integer \(k\ge0\),
\[
\mathbb E[x_{k,i}^2]=\left[(1-p_i)+p_i(1-c/p_i)^2\right]^k x_{0,i}^2
=\left(1-2c+\frac{c^2}{p_i}\right)^k x_{0,i}^2.
\]
The bracket is strictly below one precisely when \(c<2p_i\). If \(c>2p_i\), selecting proposals on all validation ties makes the validation-gated squared error obey the exact factor
\[
\mathbb E[x_{k,i}^2]=\left[1+p_i(1-p_i)\bigl((1-c/p_i)^2-1\bigr)\right]^k x_{0,i}^2,
\]
which exceeds one. This calculation relies on the fact that a worsening update of \(i\) is rejected on \(\zeta=i\), but is tied and accepted on \(\zeta\ne i\). For \(c=2p_i\), the absolute value is constant under all tie policies.

**Two-coordinate and universal probability frontiers.** In two dimensions \(c=p^2+(1-p)^2\); writing \(q=\min(p,1-p)\), the criterion \(c<2q\) reduces to \(q>1-1/\sqrt2\), giving the open interval stated above.

For a lower probability floor \(m\), the convex function \(\sum p_i^2\) on the simplex \(p_i\ge m\) is maximized at a vertex: up to permutation this is
\[
p=(1-(d-1)m,m,\ldots,m).
\]
Its collision mass is \(c_{\max}=(1-(d-1)m)^2+(d-1)m^2\). All vectors with the same floor converge if and only if \(c_{\max}<2m\), equivalent to
\[
d(d-1)m^2-2dm+1<0.
\]
Its smaller root is \(1/[\sqrt d(\sqrt d+1)]\), and its larger root exceeds \(1/d\). This proves (2), including the failed equality boundary.

**Four equally probable components.** Let the first sampled loss be \(f_1(x)=2x_1^2\), and let the other three identical sampled losses be \(f_2(x)=f_3(x)=f_4(x)=(2/3)x_2^2\). Their uniform average is \(\frac12(x_1^2+x_2^2)\), corresponding to \(p=(1/4,3/4)\). The collision mass is \(5/8\), so the rare-coordinate multiplier is \(-3/2\). Its unguarded one-step squared error multiplier is \((3/4)+(1/4)(9/4)=21/16\). With validation ties accepted, the only rare-coordinate changing events have probability \((1/4)(3/4)=3/16\), giving \(1+(3/16)(9/4-1)=79/64\), proving the asserted strict failure.

## Verification
The standalone `verify.py` uses only the Python standard library and exact `fractions.Fraction` arithmetic. Run `python3 verify.py` from the extracted package directory. It recomputes the independent-feedback expectation and the gated/raw one-step multipliers on 375 seeded rational test cases across dimensions two through six; tests exact finite-horizon distributions in the four-component example through four iterations; and checks the extremal collision inequality on 429 integer-rational grid cases. All tests passed in the originating review. The universal statements above follow from the complete algebraic proof, not from the finite checks.

## Relationship to prior work
Zhang, Gao, Ye and Udell (2026) introduce the independent out-of-sample normalized hypergradient feedback and its null-step safeguard in their Section 3.1, equation (4) and Algorithm 2. Their convergence theorem uses additional stochastic-gradient and oracle concentration conditions; the sparse coordinate model here is not claimed to satisfy those bounds at the levels required for the theorem, and the present result does not contradict it. The new distinction is the exact probability-collision bias of the *feedback-optimal frozen scalar step*, together with the sharp all-tie-policy failure of independent validation on orthogonal supports.

Qu and Richtárik (2015) study coordinate descent under arbitrary sampling, with convergence guarantees built around coordinatewise sampling information. Their update and analysis do not use an independent validation sample to select between a proposed iterate and its predecessor, nor do they optimize the normalized out-of-sample feedback above. Earlier scalar-random-curvature feedback analyses explicitly observe that their strictly positive independent evaluation curvature makes every accepted proposal a true contraction in absolute value; their null-step gate rejects expansive updates. That implication fails for the present rank-one coordinate losses: when the evaluation and update supports are disjoint, the evaluation loss is **unchanged** even if the updated coordinate expands. Thus the scalar stability conclusions do not imply the multidimensional all-tie-policy obstruction.

## Limitations
The result concerns a scalar step *frozen at the population feedback minimizer*, not the actual stochastic online-learning recursion for the step matrix, nor arbitrary candidate sets or matrix preconditioners. The normalized feedback is only defined when the sampled gradient is nonzero; its population expression uses states with all coordinates nonzero. The all-states convergence classification concerns the resulting frozen-step dynamics, which remains defined after any coordinate becomes zero. The probability floor (2) is for positive sampling probabilities; zero-probability coordinates obviously cannot be learned. Separate full-literature priority verification remains open, especially among randomized coordinate methods and hypergradient adaptations.

## References
1. W. Zhang, W. Gao, Y. Ye, and M. Udell, *Stochastic Gradient Methods with Online Scaling*, Optimization Online, first posted 2026-05-28. https://optimization-online.org/2026/05/stochastic-gradient-methods-with-online-scaling/ ; original full text https://optimization-online.org/wp-content/uploads/2026/05/Stochastic_OSGM-4.pdf .
2. Z. Qu and P. Richtárik, *Coordinate Descent with Arbitrary Sampling I: Algorithms and Complexity*, 2015, https://arxiv.org/abs/1412.8060 .
3. A. Rodomanov and D. Kropotov, *A Randomized Coordinate Descent Method with Volume Sampling*, SIAM Journal on Optimization 30 (2020), 1878–1904, https://doi.org/10.1137/19M125532X .
4. M. Dereziński and X. Dong, *Last-Iterate Convergence of Randomized Kaczmarz and SGD with Greedy Step Size*, COLT 2026, https://proceedings.mlr.press/v336/derezinski26b.html .
