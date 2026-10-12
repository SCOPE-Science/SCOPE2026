# Exact pair-moment bounds for three-of-four predictive success under infinite exchangeability

## Finding

Let \(X_1,X_2,\ldots\) be an infinitely exchangeable Bernoulli sequence, and suppose its one- and two-coordinate success probabilities are prescribed:
\[
\mu=\Pr(X_1=1),\qquad \nu=\Pr(X_1=X_2=1),\qquad 0\le\mu\le1,\quad \mu^2\le\nu\le\mu.
\]
Set \(R=\Pr(X_1+X_2+X_3+X_4\ge3)\). For every feasible pair the **entire sharp attainable interval** is \(L(\mu,\nu)\le R\le U(\mu,\nu)\), with
\[
U(\mu,\nu)=
\begin{cases}
\dfrac{4\nu+12\mu\nu-4\mu^2-9\nu^2}{3},&\nu\le\dfrac{2\mu}{3},\\[4pt]
\dfrac{\nu^2(4\mu-3\nu)}{\mu^2},&\nu\ge\dfrac{2\mu}{3},\quad\mu>0,
\end{cases}
\]
and, for \(0<\mu<1\),
\[
L(\mu,\nu)=
\begin{cases}
\dfrac{\nu^2(4\mu-3\nu)}{\mu^2}, & \nu\le\dfrac\mu6,\\[6pt]
\dfrac{1-\mu}{1-a}\,(4a^3-3a^4)+\dfrac{\mu-a}{1-a},
&\mu\ge\dfrac16,\ \nu\le\dfrac{7\mu-1}{6},\quad a=\dfrac{\mu-\nu}{1-\mu},\\[6pt]
\dfrac{13\nu-\mu}{12},&\nu\ge\max\!\left\{\dfrac\mu6,\dfrac{7\mu-1}{6}\right\}.
\end{cases}
\]
At \(\mu=0\) both endpoints equal zero; at \(\mu=1\) they equal one. All common boundary formulas agree. Both endpoints are attained by explicitly specified infinite exchangeable laws, and every intermediate value is attained. In particular, knowledge of the pairwise joint success probability induces three distinct sharp lower-bound phases; the central phase is supported on the universal mixing atom \(\theta=1/6\).

## Assumptions and scope

The Bernoulli observations are infinitely, not merely four-fold, exchangeable. By de Finetti's theorem there is a random \(\Theta\in[0,1]\) such that the observations are independent Bernoulli\((\Theta)\) conditionally on \(\Theta\). The known moments are \(\mathbb E\Theta=\mu\) and \(\mathbb E\Theta^2=\nu\). Feasibility \(\mu^2\le\nu\le\mu\) is both necessary and sufficient; for example a two-atom directing law on \(\{0,\nu/\mu\}\) realizes every interior pair \(\mu>0\). The event probability is
\[
R=\mathbb E f(\Theta),\qquad f(t)=4t^3-3t^4,\quad 0\le t\le1.
\]
The formulas also apply conditionally when \(\mu,\nu\) are posterior moments at a fixed conditioning event; no claim is made that they are known from an exchangeability assumption alone.

## Proof

**Quadratic moment duality.** A quadratic \(q(t)\ge f(t)\) on \([0,1]\) gives \(R\le\mathbb E q(\Theta)\); reverse the inequality for lower bounds. Because only the first two moments are prescribed, the expectation of \(q\) is fixed. In each regime construct a quadratic contact bound and a directing distribution concentrated on its contact points, thereby proving sharpness without invoking numerical optimization.

**Upper bound, low second moment.** Assume \(0<\mu<1\) and \(\nu\le2\mu/3\). Define
\[
s=\sqrt{\nu-2\mu/3+1/9},\quad a=1/3-s,\quad b=1/3+s.
\]
The inequalities \(\mu^2\le\nu\le2\mu/3\) imply \(s\ge|\mu-1/3|\) and \(s\le1/3\); hence \(0\le a\le\mu\le b\le2/3\). The polynomial
\[
q(t)=f(t)+3(t-a)^2(t-b)^2
\]
is quadratic because \(a+b=2/3\). Writing \(P=ab=2\mu/3-\nu\), it equals
\[
q(t)=3P^2-4Pt+(4/3+6P)t^2.
\]
Thus \(\mathbb E q(\Theta)=(4\nu+12\mu\nu-4\mu^2-9\nu^2)/3\). Take \(\Pr(\Theta=b)=(\mu-a)/(b-a)\) and \(\Pr(\Theta=a)=(b-\mu)/(b-a)\): its first two moments are \(\mu,\nu\), and the bound is attained. If \(a=b\), necessarily \(\Theta=1/3\) almost surely, and the same expression holds by continuity.

**Upper bound, high second moment.** For \(\nu\ge2\mu/3\) and \(\mu>0\), put \(b=\nu/\mu\in[2/3,1]\), \(c=4/3-2b\le0\). Then
\[
q(t)=f(t)+3t(t-b)^2(t-c)
\]
is quadratic, \(q\ge f\) for \(0\le t\le1\), and equality holds at \(0,b\). The law \(\Pr(\Theta=b)=\mu^2/\nu\), \(\Pr(\Theta=0)=1-\mu^2/\nu\) has the prescribed moments, so the sharp upper endpoint is \(\nu^2(4\mu-3\nu)/\mu^2\).

**Lower bound, low second moment.** If \(0<\mu<1\) and \(\nu\le\mu/6\), set \(b=\nu/\mu\le1/6\) and \(c=4/3-2b\ge1\). The quadratic
\[
q(t)=f(t)-3t(t-b)^2(c-t)
\]
satisfies \(q\le f\) on \([0,1]\) and contacts at \(0,b\). The same two-atom law on \(0,b\) attains \(L=\nu^2(4\mu-3\nu)/\mu^2\).

**Lower bound, endpoint atom.** Suppose \(\mu\ge1/6\), \(\nu\le(7\mu-1)/6\), and \(0<\mu<1\). Set \(a=(\mu-\nu)/(1-\mu)\ge1/6\) and \(c=1/3-2a\le0\). Feasibility gives \(0\le a\le\mu<1\). The quadratic
\[
q(t)=f(t)-3(t-a)^2(1-t)(t-c)
\]
satisfies \(q\le f\), with contact points \(a,1\). Assign mass \((1-\mu)/(1-a)\) to \(a\) and mass \((\mu-a)/(1-a)\) to \(1\). These masses reproduce the two prescribed moments and yield the stated middle branch.

**Lower bound, universal three-atom support.** In the remaining phase, \(\nu\ge\max\{\mu/6,(7\mu-1)/6\}\). We have the exact quadratic minorant
\[
q(t)=\frac{13t^2-t}{12},\qquad f(t)-q(t)=3t(1-t)(t-1/6)^2\ge0.
\]
Choose the directing distribution supported on \(\{0,1/6,1\}\), with respective probabilities
\[
w_0=1-7\mu+6\nu,\quad w_{1/6}=\frac{36}{5}(\mu-\nu),\quad w_1=\frac{6\nu-\mu}{5}.
\]
The phase conditions make all masses nonnegative. Their sum is one and the first two moments are exactly \(\mu,\nu\). Since the support consists of contact points, \(L=\mathbb E q(\Theta)=(13\nu-\mu)/12\).

The low and endpoint-atom lower-bound regions meet the three-atom region at their stated thresholds; the upper two regimes meet at \(\nu=2\mu/3\). Their values coincide because the adjacent extremizing laws and dual polynomials agree at the boundary. If \(\nu=\mu^2\), the directing law is \(\delta_\mu\) and the sharp interval collapses to \(\{f(\mu)\}\); if \(\nu=\mu\), it is supported on \(\{0,1\}\), and the interval collapses to \(\{\mu\}\). Convexly mixing the upper- and lower-extremizing *directing distributions* preserves both moments and attains every intermediate value of \(R\). This completes the proof.

## Verification

The supplementary `artifacts/verify_exact.py` reconstructs all four contact-polynomial factorizations using SymPy, checks moment-matching identities, and exactly checks 297 feasible interior rational moment pairs on a grid. It reports 2,988 symbolic/rational checks on the test environment. The grid is corroboration, not the proof of any infinite or continuous assertion. The rigorous argument is the displayed nonnegative polynomial factorization and moment-matching calculation on each full parameter phase.

A concrete interior example is \(\mu=2/5\) and \(\nu=19/100\), corresponding to pairwise Bernoulli correlation \(1/8\). The interval becomes
\[
\frac{7747}{40000}\le R\le\frac{2357}{10000}.
\]
For comparison, **merely four-fold exchangeable** (not necessarily infinitely extendible) laws with the same moments attain values \(17/200\) and \(19/50\): take laws on the sum \(S_4\) with weights \((57,0,126,0,17)/200\) and \((8,23,0,19,0)/50\), respectively, and conditionally distribute the successes uniformly over the chosen count. Both agree on \(\mathbb E X_1=2/5\), \(\mathbb E X_1X_2=19/100\), yet lie strictly outside the infinitely exchangeable interval.

## Relationship to prior work

Polson and Zantedeschi (2026) establish a hierarchy of moments needed for coherent exchangeable Bernoulli prediction; the distinction between first- and higher-order predictive information motivates the exact two-moment partial-identification problem, but their theorems do not evaluate this specific sharp feasible interval. Gottschling and Caprio (2026) give different concentration bounds for exchangeable sequences about de Finetti component means.

Zaigraev and Kaniovski (2010) optimize threshold events over arbitrary finite exchangeable Bernoulli vectors; Di Cecco (2011) studies finite exchangeable binary variables with pairwise correlation. Infinite extendibility is a stricter condition: the displayed exact finite-population counterexample shows the finite-exchangeable bounds do not imply these sharp narrower endpoints. The general moment duality is classical and is not claimed as new. A public prior result, *Exact Bernoulli tail envelopes under infinite exchangeability* (2026), fixes only the first marginal moment and optimizes thresholds at arbitrary sample sizes. That mean-only optimization neither imposes nor determines the fixed second-moment sharp interval derived here.

## Limitations

The claim is specific to the four-trial event requiring at least three successes, and to infinite exchangeability and exactly specified first two joint success moments. It does not supply a closed formula for all thresholds or all sample sizes, nor estimate the moments from finite data. These bounds are sharp for the stated population class, not for arbitrary finite exchangeable four-vectors. General truncated Hausdorff moment theory and historic correlation-constrained exchangeability papers may contain equivalent formulations not identified by the documented comparison. In particular, the complete 2011 paper by Di Cecco was not available in the accessible open sources at review time; an institutional retrieval required a manual connection unavailable then.

## References

1. Nicholas G. Polson and Daniel Zantedeschi (2026), *Martingale Posterior Predictive Coherence: Hausdorff Moment Hierarchy*, arXiv:2603.00661, first posted 28 February 2026, https://arxiv.org/abs/2603.00661 .
2. Nina Maria Gottschling and Michele Caprio (2026), *Hoeffding-Type Concentration Bounds for Exchangeable Random Variables*, arXiv:2603.10190, https://arxiv.org/abs/2603.10190 .
3. Alexander Zaigraev and Serguei Kaniovski (2010), *Exact bounds on the probability of at least k successes in n exchangeable Bernoulli trials as a function of correlation coefficients*, Statistics & Probability Letters 80, 1079–1084, https://serguei.kaniovski.wifo.ac.at/fileadmin/pdf/kn_reliability.pdf .
4. Davide Di Cecco (2011), *A geometric approach to a class of optimization problems concerning exchangeable binary variables*, Statistics & Probability Letters 81, 411–416, https://doi.org/10.1016/j.spl.2010.11.016 .
5. *Exact Bernoulli tail envelopes under infinite exchangeability* (2026), public mathematical research record, https://github.com/published-finding corpus/2026/tree/main/2026/9/17/SCOPE-sharp-extendible-bernoulli-tail-bounds--829140c11a96 .
6. B. de Finetti, classical representation theorem for infinite exchangeability of Bernoulli sequences.
