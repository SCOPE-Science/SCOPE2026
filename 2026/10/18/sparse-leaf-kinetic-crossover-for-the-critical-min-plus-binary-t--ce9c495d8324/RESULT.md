# Sparse-leaf kinetic crossover for the critical min-plus binary tree

## Finding

Let the independent leaves of a depth-\(N\) full binary tree be \(1\) with probability \(r_N\in(0,1]\), and \(0\) otherwise. Every internal node independently chooses the sum or the minimum of its two child values, each with probability \(1/2\). Let \(X_{N,r_N}\) be the root value. Assume \(r_N\to0\), and write \(\mathcal L_{N,r_N}=\operatorname{Law}(X_{N,r_N}\mid X_{N,r_N}>0)\).

There is a unique continuous family of probability measures \((\nu_t)_{t\ge0}\) on the positive integers, with \(\nu_0=\delta_1\), solving in \(\ell^1\)
\[
\frac{d\nu_t}{dt}=\frac12\bigl(\nu_t*\nu_t-\operatorname{Max}_2(\nu_t)\bigr),
\]
where \(*\) means the law of a sum of independent draws and \(\operatorname{Max}_2\) means the law of their maximum. The following complete three-regime conclusion holds for every sequence \(r_N\to0\):

1. If \(Nr_N\to0\), then \(\mathcal L_{N,r_N}\to\delta_1\) in total variation.
2. If \(Nr_N\to\lambda\in(0,\infty)\), then \(\mathcal L_{N,r_N}\to\nu_\lambda\) in total variation.
3. If \(Nr_N\to\infty\), then for every fixed integer \(K\ge1\), \(\mathcal L_{N,r_N}([1,K])\to0\).

The middle law is nontrivial for every \(\lambda>0\):
\[
\nu_\lambda(\{1\})=\frac2{2+\lambda}.
\]
For a fixed density \(r\), the intermediate evolution after \(m\) generations obeys the quantitative estimate
\[
\bigl\|\operatorname{Law}(X_{m,r}\mid X_{m,r}>0)-\nu_{mr}\bigr\|_{\mathrm{TV}}
\le\frac r4\bigl(e^{2mr}-1\bigr).
\]
This estimate applies whenever \(0<r\le1\) and \(m\ge0\), and makes the finite-clock convergence uniform on compact ranges of \(mr\).

## Assumptions and scope

At each node the two descendant subtrees are independent and identically distributed; the choice between addition and minimum is an independent fair coin. Leaves are independent Bernoulli variables, with \(\Pr\{X_0=1\}=r\). Tree depth \(m\) counts internal levels from the leaves to the root. The law conditional on a positive root is well-defined because \(r>0\). \(\ell^1\) denotes absolutely summable sequences indexed by positive integers and \(\|\cdot\|_{\mathrm{TV}}\) is half their \(\ell^1\) distance. In the three-regime theorem \(N\) tends to infinity and \(r_N\) can depend arbitrarily on \(N\) subject to the stated limits. No claim about the unconditioned distribution's nonzero mass at a fixed positive level is made beyond the exact identities below.

## Proof

**1. Exact separation of the zero mass.** Let \(r\in(0,1]\). If the probability of a positive descendant is \(r\), the probability that the sum is positive equals \(2r-r^2\), while the probability that the minimum is positive equals \(r^2\). Their fair mixture therefore has positive probability exactly \(r\). Inductively, \(\Pr(X_{m,r}>0)=r\) at every depth.

Put \(\mu_m=\operatorname{Law}(X_{m,r}\mid X_{m,r}>0)\), and let \(Y,Y'\) be independent with law \(\mu_m\). Conditioning the two-branch update on a positive result gives the **exact** equality of probability measures
\[
\mu_{m+1}=(1-r)\mu_m+\frac r2\Bigl(\operatorname{Law}(Y+Y')+\operatorname{Law}(\min(Y,Y'))\Bigr).
\]
Indeed, a sum is positive with exactly one positive descendant with total probability \(2r(1-r)\), and with two positive descendants with probability \(r^2\); a minimum is positive only with two positive descendants. The identity
\[
\operatorname{Law}(\min(Y,Y'))+\operatorname{Law}(\max(Y,Y'))=2\mu_m
\]
follows by evaluating arbitrary test functions on the unordered pair. Therefore
\[
\mu_{m+1}=\mu_m+r\Phi(\mu_m),\qquad
\Phi(\mu)=\tfrac12\bigl(\mu*\mu-\operatorname{Max}_2(\mu)\bigr),\qquad \mu_0=\delta_1.
\]
Thus the entire conditional law, not merely one atom, is an explicit forward Euler scheme with step \(r\).

**2. Global kinetic flow and quantitative convergence.** For probability measures \(\alpha,\beta\) on the positive integers, the convolution and maximum operations obey, separately,
\[
\|T(\alpha,\alpha)-T(\beta,\beta)\|_1\le2\|\alpha-\beta\|_1
\]
by adding and subtracting \(T(\alpha,\beta)\), for either pushforward \(T\) of the product. Consequently \(\|\Phi(\alpha)-\Phi(\beta)\|_1\le2\|\alpha-\beta\|_1\), and \(\|\Phi(\alpha)\|_1\le1\). Standard Euler polygonal convergence in the Banach space \(\ell^1\), applied on the probability simplex, constructs a unique globally defined solution. Positivity and unit total mass follow because every approximating Euler step of size \(h\le1\) equals the explicit convex combination from Step 1. Uniqueness follows from the Lipschitz inequality and Gronwall's lemma.

The local Euler truncation error at step \(h\) has \(\ell^1\) norm at most \(h^2\): on that interval \(\|\nu_{t+s}-\nu_t\|_1\le s\), and integration of the Lipschitz bound gives \(\int_0^h2s\,ds=h^2\). If \(E_m\) is the accumulated \(\ell^1\) error, then \(E_{m+1}\le(1+2h)E_m+h^2\), whence
\[
E_m\le\tfrac h2\bigl((1+2h)^m-1\bigr)\le\tfrac h2\bigl(e^{2mh}-1\bigr).
\]
Taking \(h=r\) and dividing by two yields the asserted total-variation estimate. Continuity of \(t\mapsto\nu_t\) now proves the first two regimes.

**3. Monotonicity and the large-clock regime.** The update map
\[
\mathcal T_r(\mu)=(1-r)\mu+\tfrac r2\bigl(\mu*\mu+\operatorname{Min}_2(\mu)\bigr)
\]
preserves first-order stochastic domination: monotone couplings of two copies preserve the orders of both sum and minimum. Also \(\mathcal T_r(\delta_1)=(1-r/2)\delta_1+(r/2)\delta_2\) stochastically dominates \(\delta_1\). Hence \(\mathcal T_r^{m+1}(\delta_1)\) dominates \(\mathcal T_r^m(\delta_1)\) for all \(m\). Passing to the finite-clock limit proves that \(\nu_t\) is stochastically nondecreasing in \(t\).

Write \(U_k(t)=\nu_t([1,k])\) and \(U_0(t)=0\). The nonlinear equation yields
\[
U_k'(t)=\frac12\left[\Pr\{Y_t+Y'_t\le k\}-U_k(t)^2\right],
\]
where the independent draws have law \(\nu_t\). For \(k=1\), no two positive integers sum to one, so \(U_1(t)=2/(t+2)\to0\). Inductively, \(\Pr(Y_t+Y'_t\le k)\le U_{k-1}(t)^2\to0\). The nonincreasing function \(U_k\) has a limit \(b\ge0\). If \(b>0\), then for all sufficiently large \(t\), \(U'_k(t)\le-b^2/4\), contradicting nonnegativity. Therefore \(U_k(t)\to0\) for every fixed \(k\).

For \(Nr_N\to\infty\), fix \(T>0\), let \(m_N=\lfloor T/r_N\rfloor\), and note \(m_N\le N\) eventually. Stochastic monotonicity implies
\[
\mathcal L_{N,r_N}([1,K])\le\operatorname{Law}(X_{m_N,r_N}\mid X_{m_N,r_N}>0)([1,K]).
\]
By Step 2, the right side converges to \(U_K(T)\). Letting \(T\to\infty\) completes the third regime.

**4. Nontriviality.** The scalar equation for \(U_1\) above provides the explicit \(\nu_\lambda(\{1\})\) and strictly separates the finite-clock law from both \(\delta_1\) and escape to infinity. Thus the parameter \(Nr_N\) defines a genuine crossover window, rather than only a proof-specific normalization.

## Verification

A standalone standard-library Python checker (`verify.py`) independently propagates the complete finite-depth sum/min probability distribution with exact rational arithmetic and separately propagates the conditional-law update. It compares the two constructions for five rational positive-leaf densities over six levels, checks the exact CDF recurrences, and checks stochastic monotonicity. It also tests the nontrivial kinetic CDF of values at most two against its closed-form Riccati solution for four finite clocks. Running `python verify.py` produces `PASS: 804 exact/finite-check assertions and kinetic diagnostics`. These finite checks do not replace the infinite-time or infinite-state analytical arguments.

## Relationship to prior work

Mendonça (2026, arXiv:2608.12295, Sections 4 and A.1) establishes that the zero atom is invariant at fair operator mixing, and gives the full finite-depth marginal recursion; it documents a pronounced positive-conditional dependence on the leaf-zero density. It does not identify the sparse-density scaling \(r_N\to0\), the total-variation kinetic flow, the \(Nr_N\) clock, or its three-regime phase classification.

Auffinger and Cable (2017, arXiv:1709.07849, particularly Sections 2 and 3) analyze the critical model with every leaf initially equal to one, including comparison sequences for fixed small-value probabilities and a large-value distributional limit. Their leaf density is fixed at one, whereas here it vanishes and the result conditions on an increasingly rare positive root. The present claim does not assert novelty of their fixed-level constants.

General Euler convergence for Lipschitz measure-valued equations underlies one proof step, but does not by itself identify the exact conditional recursion or the sparse-leaf clock and escape regime for this tree model. Searches of published research records and relevant earlier literature did not identify an equivalent complete three-regime statement. A broad earlier general theorem on recursive distributions could still imply it.

## Limitations

The theorem requires the fair sum/min mixture, iid Bernoulli \(0\)/\(1\) leaves, and a vanishing positive-leaf density. The finite-clock limit is in total variation **conditional on positivity**; unconditioned laws tend to \(\delta_0\) throughout the sparse regime. In the diverging-clock case the conclusion is escape from each fixed finite set, not a specified rescaled growth rate. No uniform error estimate is claimed for unbounded \(Nr_N\), and no universality over arbitrary positive-leaf size distributions is asserted. Priority against unpublished or unindexed general kinetic-limit results is not independently certified.

## References

1. J. R. G. Mendonça, *Finite-depth scaling and an exact Bernoulli-leaf identity for the min-plus process on the binary tree*, arXiv:2608.12295 (initial public submission August 12, 2026), https://arxiv.org/abs/2608.12295.
2. A. Auffinger and D. Cable, *Pemantle's min-plus binary tree*, arXiv:1709.07849 (2017), https://arxiv.org/abs/1709.07849; lawful full text also at https://sites.math.northwestern.edu/~auffing/09_20_Tree.pdf.
3. Y. Hu, B. Mallein, and M. Pain, *An exactly solvable continuous-time Derrida--Retaux model*, arXiv:1811.08749 (2019), https://arxiv.org/abs/1811.08749 (related but different continuous-time recursive model).
