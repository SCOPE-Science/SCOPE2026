# Subgroup-stratified excess entropy of finite-group difference factors

## Finding

Let \(G\) be any finite group with identity \(e\). Let \((X_i)_{i\in\mathbb Z}\) be iid with law \(\mu\) on \(G\), and set \(Y_i=X_i^{-1}X_{i+k}\) at fixed integer lag \(k\ge 1\). Write \(H(\mu)=-\sum_x\mu(x)\log_2\mu(x)\) and let
\[
K_\mu=\{g\in G:\mu(gx)=\mu(x)\text{ for every }x\in G\}
\]
be the left-translation stabilizer. This is a subgroup, not necessarily normal. The excess entropy and output entropy rate satisfy
\[
\mathcal E_k(\mu)=I((Y_i)_{i<0};(Y_i)_{i\ge0})=k\bigl(H(\mu)-\log_2|K_\mu|\bigr),\qquad h(Y)=H(\mu).
\]
The exact finite-block formula is given below. As a function of the source law, \(\mathcal E_k\) is continuous exactly where \(K_\mu=\{e\}\). At any \(\mu\) the set of limits of \(\mathcal E_k(\mu_n)\) along sequences \(\mu_n\to\mu\), allowing constant sequences, is exactly
\[
\{k(H(\mu)-\log_2 |J|):J\le K_\mu\}.
\]
Every subgroup of \(G\) is the exact stabilizer of a strictly positive law. In particular a perturbation to a law with trivial stabilizer, which is an open dense condition in the simplex, gives the limiting upward jump \(k\log_2|K_\mu|\).

## Assumptions and scope

The group need not be abelian and the law may have zeros, with \(0\log_2 0=0\). All entropy quantities are in bits. Infinite past and future are taken in the natural sigma-algebras of the stationary factor of the two-sided product source. Convergence of source laws is on the simplex of a fixed finite group.

## Proof

**Finite blocks.** For a block of \(n\ge1\) output symbols, the source indices \(0,\ldots,n+k-1\) split into \(k\) disjoint paths by residue modulo \(k\), with lengths \(L_j=1+\#\{0\le i<n:i\equiv j\pmod k\}\). On each path, given its differences, all source letters are determined from the initial one by multiplication on the right. In particular, for any realized word \(W\) on that path, every lift is uniquely a simultaneous left translate \(g W\). For \(W\sim\mu^{\otimes L}\) write
\[
\pi_W(g)=\frac{\prod_{r=1}^L\mu(gW_r)}{\sum_{a\in G}\prod_{r=1}^L\mu(aW_r)},\qquad q_L(\mu)=\mathbb E\bigl[H(\pi_W)\bigr].
\]
The denominator is positive almost surely because the true sampled word has positive probability. The lift probabilities conditional on the output are the displayed weights; changing the reference lift only permutes them. Consequently \(q_L\) is the conditional source entropy of one path. The paths involve independent source variables, so
\[
H(Y_0,\ldots,Y_{n-1})=(n+k)H(\mu)-\sum_{j=0}^{k-1}q_{L_j}(\mu).
\]
Since \(0\le q_L\le\log_2 |G|\), division by \(n\) yields the stated entropy rate. Paths with one source letter require no differences and are included in the formula.

**Information in the two halves.** Write \(B=(X_0,\ldots,X_{k-1})\) and \(C=(K_\mu X_0,\ldots,K_\mu X_{k-1})\). The sets \(K_\mu x\) are the orbits of left multiplication by \(K_\mu\) (right cosets in standard terminology). On either half of a residue path, each possible boundary letter determines a reconstructed source tail using the observed differences, by multiplying on the right by the differences in forward time or by their inverses in reverse time. Starting from the true letter gives empirical frequencies tending to \(\mu\) by the strong law. Starting from \(gX_j\) left-translates every reconstructed letter by \(g\), so empirical frequencies tend to \(x\mapsto\mu(g^{-1}x)\). There are finitely many hypotheses; exactly the boundary letters in \(K_\mu X_j\) have limiting frequencies \(\mu\). Hence each observed half determines \(C\) almost surely, also for laws with zeros.

Conditionally on \(B\) the observed halves involve disjoint independent source tails and are independent. Changing \(B_j\) by a left translation from \(K_\mu\), and applying that translation to the corresponding residue tail, preserves every difference and the law of the unobserved tail. The conditional laws of each observed half thus depend on \(B\) only through \(C\). Averaging their product over \(B\) conditional on \(C\) gives their conditional independence given \(C\). As both halves determine \(C\), their mutual information is \(H(C)\) by the chain rule. Within any orbit of positive mass, the boundary law is uniform over \(|K_\mu|\) letters. The independence of the boundary letters now gives \(H(C)=k(H(\mu)-\log_2|K_\mu|)\).

**Limits and realizability.** For each \(g\), the equalities \(\mu(gx)=\mu(x)\) are closed conditions. If \(\mu_n\to\mu\), each subgroup appearing infinitely often as \(K_{\mu_n}\) is contained in \(K_\mu\). There are finitely many subgroups, and Shannon entropy is continuous on the closed simplex. Thus any sequence with convergent excess entropies has a subsequence with constant stabilizer giving one of the claimed limits.

Conversely, for any subgroup \(J\le G\), choose a law \(\nu_J\) assigning distinct strictly positive total masses to the sets \(Jg\), uniformly within each set. Every element of \(J\) preserves this law. If \(h\notin J\), then \(Jh\ne J\) and \(\nu_J(h)\ne\nu_J(e)\), so \(h\) does not preserve it. Therefore \(K_{\nu_J}=J\). For \(J\le K_\mu\), set \(\mu_\varepsilon=(1-\varepsilon)\mu+\varepsilon\nu_J\) with \(0<\varepsilon<1\). Every \(g\in J\) preserves both summands. Every \(g\in K_\mu\setminus J\) fails to preserve the second summand and cannot preserve the mixture. For each \(g\notin K_\mu\), select one failed equality of \(\mu\); by continuity it still fails for all sufficiently small \(\varepsilon\). There are finitely many such \(g\), so \(K_{\mu_\varepsilon}=J\) for sufficiently small positive \(\varepsilon\), proving attainment. The value for \(J=K_\mu\) may also be attained by a constant sequence. Trivial stabilizer is open by the finitely many closed symmetry constraints, and dense by taking \(J=\{e\}\) in the mixture. The formula is continuous at those laws and has the claimed jump from generic perturbations at all other laws.

## Verification and examples

The unchanged `verify.py` enumerates finite output-word probabilities and independently compares the posterior formula on 38 finite examples for cyclic groups of orders three and four and for \(S_3\) at lags one or two. The comparison uses numerical entropies; these are finite checks, not the proof of the infinite theorem.

For \(G=\mathbb Z/4\mathbb Z\) and \(\mu=(a,b,a,b)\) with \(a,b>0\), \(a+b=1/2\), and \(a\ne b\), one has stabilizer \(\{0,2\}\) and excess entropy \(k h_2(2a)\), where \(h_2\) is binary entropy. At the uniform law on this group the three limiting values are \(0,k,2k\). For a nonnormal example use \(G=S_3\) and \(J=\langle(12)\rangle\) with masses \(1/2,1/3,1/6\) distributed uniformly within the three orbits \(Jg\). The stabilizer is exactly \(J\), and the excess entropy is \(k H(1/2,1/3,1/6)\).

## Relationship to prior work and limitations

Lindgren and Nordahl, *Complexity Measures and Cellular Automata* (1988), [§3, Eqs. (3.10)–(3.17)](https://wpmedia.wolfram.com/uploads/sites/13/2018/02/02-4-2.pdf), already give the Rule 60 biased-binary effective measure complexity and its discontinuity at the fair source. Dyadic times there include the corresponding two-point XOR lags. Kari and Taati, *Statistical Mechanics of Surjective Cellular Automata* ([arXiv:1311.2319](https://arxiv.org/abs/1311.2319), Examples 33 and 35 in the inspected preprint), study the binary XOR factor and its iterates, including non-Gibbsian images. An [indexed result on Bayesian reconstruction](https://github.com/Resultary/2026/tree/main/2026/10/26/SCOPE-sharp-bayesian-reconstruction-exponents-and-kernel-density-extre--6a92d67fc135) gives invertibility and finite-window decoding exponents for biased binary additive factors, including the lag-one XOR map. The claim here is the finite-group excess-entropy formula and the full subgroup-indexed phase diagram, including nonnormal stabilizers and laws with zeros, not binary reconstruction or the binary discontinuity. This comparison does not establish historical priority.

The proof concerns iid source variables. It gives no finite-observation rate or confidence bound, or extension to correlated sources or non-group alphabets. Different subgroups of the same order give the same limiting value. Allowing constant approximating sequences matters, for example if no distinct nearby law can keep the same maximal stabilizer.
