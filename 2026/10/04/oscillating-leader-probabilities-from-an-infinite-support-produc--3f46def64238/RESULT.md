# Oscillating leader probabilities from an infinite-support product law
## Finding
Let \(\mu\) be the probability law on \(\mathbb N_0\) whose upper tails are
\[
T_k:=\Pr_\mu\{X>k\}=2^{-4^k},\qquad k=0,1,2,\ldots.
\]
Equivalently, \(\Pr\{X=0\}=1/2\), and for \(k\ge1\),
\[
p_k:=\Pr\{X=k\}=T_{k-1}-T_k.
\]
Let \(Z_i=(X_i,Y_i)\), \(i\ge1\), be i.i.d. with law \(\mu\otimes\mu\). For each sample size \(n\), let \(a_n\) denote the probability that the sample contains a leader, meaning an observed vector that is coordinatewise at least every other observed vector.

Then
\[
\liminf_{n\to\infty}a_n=0,
\qquad
\limsup_{n\to\infty}a_n\ge e^{-2}.
\]
In particular, the leader probability need not converge even when the two coordinates are independent and both marginal supports are infinite.

More explicitly, put
\[
N_k=T_k^{-1}=2^{4^k}
\]
and, for \(k\ge2\),
\[
M_k=T_{k-1}^{-3/2}=2^{3\cdot 4^{k-1}/2}.
\]
Then
\[
\liminf_{k\to\infty}a_{N_k}\ge e^{-2},
\qquad
a_{M_k}\longrightarrow0.
\]

## Assumptions and scope
The construction is two-dimensional and uses independent, identically distributed coordinates. The marginal law is purely discrete, supported on every nonnegative integer, and has deliberately lacunary upper tails. No moment assumption is needed.

The conclusion is a nonconvergence statement. It does **not** disprove the conjecture of Răducan, Rădulescu, Rădulescu, and Zbăganu that a product of two infinite-support marginals cannot have the leader property, because the present example has \(\liminf a_n=0\). Instead, it shows that the stronger conclusion \(a_n\to0\), proved in their Proposition 4 under a bounded adjacent-mass-ratio hypothesis, fails without such regularity.

## Proof
Fix \(k\ge1\) and abbreviate
\[
q:=T_{k-1}.
\]
The construction gives \(T_k=q^4\) and \(p_k=q-q^4\).

First consider the peak sample size
\[
n=N_k=q^{-4}.
\]
For one coordinate sample, the probability that no observation exceeds \(k\) is
\[
(1-q^4)^n=(1-1/n)^n\longrightarrow e^{-1}.
\]
Conditional on this event, the number \(R_k\) of observations equal to \(k\) is binomial with success probability
\[
\theta_k=\frac{q-q^4}{1-q^4}\sim q,
\]
so its conditional mean is asymptotic to \(q^{-3}\). Since
\[
n^{2/3}=q^{-8/3}=o(q^{-3}),
\]
a standard binomial lower-tail bound gives
\[
\Pr\{R_k\ge n^{2/3}\mid \max X_i\le k\}\longrightarrow1.
\]
Hence the event \(E_X\) that the coordinate maximum equals \(k\) and is attained at least \(n^{2/3}\) times satisfies
\[
\Pr(E_X)\longrightarrow e^{-1}.
\]
The same statement holds independently for the \(Y\)-sample.

Conditional on respective maximum multiplicities \(r\) and \(s\), exchangeability makes the two maximizing-index sets independent uniform subsets of \(\{1,\ldots,n\}\) of sizes \(r\) and \(s\). Their disjointness probability is at most
\[
\left(1-\frac r n\right)^s\le \exp\!\left(-\frac{rs}{n}\right).
\]
On \(E_X\cap E_Y\), one has \(r,s\ge n^{2/3}\), so this is at most \(e^{-n^{1/3}}\). A common maximizing index is a leader. Therefore
\[
a_{N_k}\ge \Pr(E_X)\Pr(E_Y)\bigl(1-e^{-N_k^{1/3}}\bigr),
\]
and consequently
\[
\liminf_{k\to\infty}a_{N_k}\ge e^{-2}.
\]

Now take \(k\ge2\) and the trough sample size
\[
m=M_k=q^{-3/2}.
\]
For a single coordinate, the probability of seeing any value above \(k\) is at most
\[
mT_k=mq^4=q^{5/2}.
\]
The probability of seeing no value equal to \(k\) is at most
\[
(1-p_k)^m\le e^{-mp_k},
\]
and \(mp_k\sim q^{-1/2}\to\infty\). Thus the coordinate maximum equals \(k\) with probability tending to one.

If both coordinate maxima equal \(k\), then a leader can exist only if some sample index has both coordinates equal to \(k\). By the union bound and coordinate independence,
\[
\Pr\{\exists i:X_i=Y_i=k\}\le mp_k^2\sim q^{1/2}\longrightarrow0.
\]
Therefore
\[
a_{M_k}
\le
2\left(mq^4+e^{-mp_k}\right)+mp_k^2
\longrightarrow0.
\]
This proves both the zero liminf and the positive limsup bound.

## Verification
Every asymptotic step follows from the explicit identities \(T_k=T_{k-1}^4\), \(p_k=T_{k-1}-T_k\), and the two displayed sample-size choices. At the peak scale, the only probabilistic input beyond elementary conditioning is a binomial lower-tail estimate in a regime where the target \(n^{2/3}\) is a vanishing fraction of a mean asymptotic to \(n^{3/4}\). At the trough scale, Markov's union bound and \((1-u)^m\le e^{-mu}\) suffice.

As finite stress checks, at \(k=2\) the peak size is \(N_2=65536\), the mean number of level-\(2\) observations is \(4095\), and \(\sqrt{N_2}=256\); at \(k=3\) the separation is already much larger. These numerical checks are illustrative only and are not used to prove the limiting claim.

## Relationship to prior work
Răducan, Rădulescu, Rădulescu, and Zbăganu introduced the leader probability and explicitly asked whether independent coordinates with infinite supports can have the leader property. Their Proposition 4 proves the stronger convergence \(a_n\to0\) when at least one discrete marginal has bounded adjacent atom ratios. The present law lies deliberately outside that regular regime and shows that convergence itself can fail: the same infinite-support product law has troughs tending to zero and peaks bounded away from zero.

A later paper by Răducan and Zbăganu studies quasi-unidimensional, dependent-coordinate vectors of the form \(f(X)\), not the independent product construction here. Jacobovic and Zuk study the probability that a fixed sample vector is Pareto maximal; that is a different event from the existence of a single vector dominating the whole sample and does not imply the present oscillation statement.

A previous structural result for product samples reduces leader existence to intersection of the two marginal maximizing-index sets. The current construction is not contained in that criterion: it supplies an explicit infinite-support law and proves two incompatible asymptotic regimes for its maximum multiplicities. The proof above is self-contained and does not require that earlier criterion.

## Limitations
The construction is intentionally lacunary. It proves nonconvergence and a quantitative positive limsup, but it does not determine the exact value of \(\limsup a_n\), nor does it settle the infinite-support no-leader conjecture because \(\liminf a_n=0\).

A residual originality risk remains that a similar lacunary example may exist under different terminology for common sample maxima or tied extreme order statistics. Targeted searches of the motivating paper, its same-author follow-up, the Pareto-maxima literature cited there, and semantic databases did not locate such an example or the stated oscillation.

## References
1. A. M. Răducan, C. Z. Rădulescu, M. Rădulescu, and G. Zbăganu, “On the Probability of Finding Extremes in a Random Set,” *Mathematics* 10 (2022), 1623. DOI: 10.3390/math10101623. Published 10 May 2022.
2. A. M. Răducan and G. Zbăganu, “The Leader Property in Quasi Unidimensional Cases,” *Mathematics* 10 (2022), 4199. DOI: 10.3390/math10224199. Published 9 November 2022.
3. R. Jacobovic and O. Zuk, “A phase transition for the probability of being a maximum among random vectors with general iid coordinates,” arXiv:2112.15534, first submitted 31 December 2021; later published in *Statistics & Probability Letters*.
