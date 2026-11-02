# Sharp double-logarithmic cusp profiles for a critically intermittent random map

## Finding

A stationary measure for a randomly switched expanding/superattracting interval map has an exact **discrete-scale cusp profile**, including a positive periodic amplitude and an exponentially small second term. In contrast to a generic logarithmic upper bound, the result fixes the exact singularity exponent and a positive pointwise density envelope.

Let \(\epsilon(t)=2^{-t-1}\), \(m(t)=\mu((\tfrac12-\epsilon(t),\tfrac12))\), and \(\alpha=\log_\ell(1/q)\). Then there are positive, continuous, one-periodic functions \(\Phi\) and \(\mathcal B\), with \(\Phi\in C^1\), for which
\[
m(t)=t^{-\alpha}\Phi(\log_\ell t)-\frac{J}{4q}2^{-\ell t}+O(2^{-2\ell t}+2^{-\ell^2t}),
\]
\[
h(\tfrac12-2^{-t-1})=\frac{2^{t+1}}{\log 2}t^{-\alpha-1}\mathcal B(\log_\ell t)+O(2^{-(\ell-1)t}),
\]
where \(J=p h(1/4)+h(3/4)>0\). Both periodic functions are bounded above and away from zero. The result does **not** assert that either periodic function is nonconstant.

## Assumptions and scope

Fix real \(\ell>1\) and probability \(0<q<1/\ell\), with \(p=1-q\). At each step choose independently between the maps
\[
G(x)=\begin{cases}2x,&0\le x<\tfrac12,\\2x-1,&\tfrac12\le x\le1,\end{cases}
\qquad
B(x)=\begin{cases}\tfrac12-\tfrac12(1-2x)^\ell,&0\le x<\tfrac12,\\2x-1,&\tfrac12\le x\le1.\end{cases}
\]
Endpoint conventions affect null sets only. These are the good-map \(r_g=1\) and bad-map \(\ell_b=\ell\) specializations of Kalle--Zeegers [1]. Their theorems imply a unique absolutely continuous stationary probability \(\mu\) because \(q\ell<1\). Its density has a representative \(h\) that is positive and locally Lipschitz separately on \((0,1/2)\) and \([1/2,1)\) [1, Theorems 1.2 and Remark 4.1]. Density values at \(1/4\) and \(3/4\) mean the locally continuous representative.

## Proof

**1. An exact one-step interval identity.** For \(t>0\) set \(\epsilon(t)=2^{-t-1}\) and \(I_t=(\tfrac12-\epsilon(t),\tfrac12)\). The inverse image of \(I_t\) under the good lower branch is \((\tfrac14-\epsilon(t)/2,\tfrac14)\); under the bad lower branch it is exactly \(I_{t/\ell}\), because \(\tfrac12-B(x)=\tfrac12(1-2x)^\ell\). The common right branch contributes \((\tfrac34-\epsilon(t)/2,\tfrac34)\). Stationarity therefore gives
\[
m(t)=q\,m(t/\ell)+j(t),\quad j(t)=p\mu((\tfrac14-\epsilon(t)/2,\tfrac14))+\mu((\tfrac34-\epsilon(t)/2,\tfrac34)).
\]
All terms are strictly positive. Notice that the common right-branch contribution has total probability \(p+q=1\), not \(p\) or \(q\).

**2. Regularity and renormalization.** Local Lipschitz regularity of \(h\) near \(1/4\) and \(3/4\) gives \(j(t)=O(2^{-t})\) and \(j'(t)=O(2^{-t})\) as \(t\to\infty\). Both \(m\) and \(j\) are \(C^1\) for positive arguments, with \(m'(t)<0\), \(j'(t)<0\). Consequently
\[
F(t)=m(t)+\sum_{k=1}^{\infty}q^{-k}j(\ell^k t)
\]
converges with its derivative uniformly on every compact subinterval of \((0,\infty)\). Substitution of the exact recurrence at \(\ell t\) telescopes to \(F(\ell t)=qF(t)\). Since \(\alpha=\log_\ell(1/q)\), the function \(\Phi(v)=\ell^{\alpha v}F(\ell^v)\) is positive, \(C^1\) and period one. Differentiating yields
\[
-F'(t)=t^{-\alpha-1}\mathcal B(\log_\ell t),\qquad
\mathcal B(v)=\alpha\Phi(v)-\frac{\Phi'(v)}{\log\ell}.
\]
The same scaling shows that \(\mathcal B\) is period one. It is strictly positive because \(F'<0\). Compactness of the circle supplies strictly positive minima and finite maxima of both functions. Since \(q\ell<1\), \(\alpha>1\).

**3. Two-term tail and density.** By local Lipschitz regularity near the two injection points,
\[
j(t)=\frac J4 2^{-t}+O(2^{-2t}),\qquad
j'(t)=-\frac{J\log2}{4}2^{-t}+O(2^{-2t}),\quad J=p h(1/4)+h(3/4)>0.
\]
Thus the omitted tail \(R(t)=F(t)-m(t)\) satisfies
\[
R(t)=\frac{J}{4q}2^{-\ell t}+O(2^{-2\ell t}+2^{-\ell^2t}),\qquad
R'(t)=O(2^{-\ell t}).
\]
The estimates follow by isolating the first term in the series and comparing the remaining superexponentially decaying terms; constants may depend on \(\ell,q\). This proves the displayed mass expansion. Finally the fundamental theorem of calculus at the continuous density representative gives \(m'(t)=-(\log2)2^{-t-1}h(\tfrac12-2^{-t-1})\). Substituting \(m'=F'-R'\) proves the density expansion with error \(O(2^{-(\ell-1)t})\). No differentiation of an unproved error expansion is used.

## Verification

The accompanying standalone `checker.py` executes exact-rational preimage-mass comparisons for three polynomial reference densities, three integer bad-map exponents and three admissible probabilities, and separately checks finite-scale telescoping identities. The checker verifies the local branch algebra; it does not compute the invariant density or substitute for the infinite-series convergence proof. That convergence, positive periodicity and the stated asymptotics are established analytically above.

## Relationship to prior work

Kalle--Zeegers [1] define this random family and prove its finite-versus-infinite stationary-measure threshold and mixing/correlation results. Their Remark 4.1 supplies the regularity essential here, but the inspected relevant portions do not state the stationary cusp's sharp periodic envelope or two-term expansion. Homburg--Kalle--Ruziboev--Verbitskiy--Zeegers [2] prove general bounds of logarithmic order for a related critical-intermittency family and its non-\(L^s\) density, neither of which is claimed as new. Their theorem bounds do not imply the present positive periodic coefficient, exact sharp exponent and exponentially accurate correction as a stated conclusion. The source family and regularity results are explicitly reused, rather than independently reproved.

## Limitations

The finding treats one good doubling map and one bad map with \(0<q<1/\ell\), and the approach to the central point from the left. It does not classify arbitrary good-map exponents, multiple bad maps, the infinite-measure parameter range or correlation decay. The periodic amplitudes may conceivably be constant; no nonconstant oscillation is asserted. Formulae depend on the stationary law, and full publication-priority verification against unindexed specializations of renewal theory remains a risk. Independent scientific audit has not been performed.

## References

[1] Charlene Kalle and Benthen Zeegers, *Decay of correlations for critically intermittent systems*, arXiv:2206.07601v1, first submitted 2022-06-15. https://arxiv.org/abs/2206.07601

[2] Ale Jan Homburg, Charlene Kalle, Marks Ruziboev, Evgeny Verbitskiy, and Benthen Zeegers, *Critical intermittency in random interval maps*, arXiv:2107.02556v1, first submitted 2021-07-06. https://arxiv.org/abs/2107.02556
