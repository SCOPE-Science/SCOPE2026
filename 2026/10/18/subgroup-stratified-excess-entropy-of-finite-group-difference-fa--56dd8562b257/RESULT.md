# Subgroup-stratified excess entropy of finite-group difference factors

## Finding

Let \(G\) be any finite group, with identity \(e\), and let \(k\ge 1\) be an integer. Independently sample \(X_i\in G\), for every \(i\in\mathbb Z\), with common law \(\mu\). Consider the stationary difference process
\[
Y_i=X_i^{-1}X_{i+k}.
\]
Write \(\mathsf H(\mu)=-\sum_{x\in G}\mu(x)\log_2\mu(x)\), with \(0\log_2 0=0\), and let the **left-translation stabilizer** be
\[
K_\mu=\{g\in G:\mu(gx)=\mu(x)\text{ for every }x\in G\}.
\]
It is a subgroup, not necessarily normal. If \(\mathcal E_k(\mu)=I((Y_i)_{i<0};(Y_i)_{i\ge0})\), the exact identity is
\[
\boxed{\mathcal E_k(\mu)=k\bigl(\mathsf H(\mu)-\log_2|K_\mu|\bigr).}
\]
The output entropy rate is \(\mathsf H(\mu)\). In fact, all finite-block entropies are given by an explicit finite orientation-posterior formula below.

There is a complete classification of the singular dependence on the source law. The map \(\mu\mapsto\mathcal E_k(\mu)\) is continuous **exactly** where \(K_\mu=\{e\}\). For an arbitrary reference law \(\mu\), allowing approximating laws equal to \(\mu\), all possible limits along sequences \(\mu_n\to\mu\) are
\[
\boxed{\bigl\{k\bigl(\mathsf H(\mu)-\log_2|J|\bigr):J\le K_\mu\bigr\}.}
\]
Every subgroup \(J\le G\) can be realized as the exact stabilizer of a strictly positive law. Consequently, a generic small perturbation of a law with nontrivial stabilizer produces an excess-entropy jump of precisely \(k\log_2|K_\mu|\). This includes a hierarchy of intermediate jumps at proper, possibly nonnormal, subgroups.

## Assumptions and scope

All groups are finite but need not be abelian; their group operation is written multiplicatively. The source law may have zeros. The stationary law is the pushforward of the two-sided Bernoulli product under the coordinatewise difference map above. Entropies and mutual informations are Shannon quantities in **bits**, with natural sigma-algebras for infinite past and future. The parameter \(k\) is fixed when taking past and future to infinity. A convergence statement for laws means convergence of their finite-dimensional probability vectors on the fixed group.

## Proof

**1. A finite-word identity.** The map from the \(n+k\) source symbols \((X_0,\ldots,X_{n+k-1})\) to \((Y_0,\ldots,Y_{n-1})\) splits into \(k\) disjoint chains according to indices modulo \(k\). In each chain, the consecutive ratios \(x_r^{-1}x_{r+1}\) determine all source symbols from the first symbol: each output word has exactly \(|G|\) group-valued lifts. For \(L\ge1\), sample \(W=(W_1,\ldots,W_L)\sim\mu^{\otimes L}\) and define
\[
\pi_W(g)=\frac{\prod_{r=1}^L\mu(gW_r)}{\sum_{a\in G}\prod_{r=1}^L\mu(aW_r)},\qquad g\in G.
\]
The denominator is positive almost surely because the actual word has positive sampling probability. Let \(q_L(\mu)=\mathbb E[-\sum_g\pi_W(g)\log_2\pi_W(g)]\). This is the conditional entropy of a chain's initial source symbol given its \(L-1\) differences: the competing lifts are precisely the simultaneous left translates \(gW\), with their product-law weights. For \(0\le j<k\), put
\[
L_j=1+\#\{0\le i<n:i\equiv j\pmod k\}.
\]
Entropy conservation under a deterministic map and independence of the chains give the **exact identity for every \(n\ge1\)**:
\[
\mathsf H(Y_0,\ldots,Y_{n-1})
=(n+k)\mathsf H(\mu)-\sum_{j=0}^{k-1}q_{L_j}(\mu).
\]
Since each \(q_L\) lies between zero and \(\log_2|G|\), dividing by \(n\) proves that the factor's entropy rate equals \(\mathsf H(\mu)\).

**2. Recoverable information.** Let \(B=(X_0,\ldots,X_{k-1})\), and let \(C=(K_\mu X_0,\ldots,K_\mu X_{k-1})\) record the \(k\) **left cosets** of \(K_\mu\). Each half of the difference observations determines \(C\) almost surely. Indeed, on any residue chain, fixing a hypothetical initial letter reconstructs every source letter from the observed differences. Under the true initial letter these reconstructed letters are iid with law \(\mu\), and under another choice they are all translated on the left by one fixed group element. By the strong law of large numbers, their empirical frequencies identify exactly those hypotheses whose translated law equals \(\mu\); those initial letters form the single left coset \(K_\mu X_j\). The argument applies separately in either time direction and is valid even if \(\mu\) vanishes at some letters.

The past and future observations depend, respectively, on independent source families \((X_i)_{i<0}\) and \((X_i)_{i\ge k}\), together with \(B\). They are therefore conditionally independent given \(B\). Furthermore, translating one boundary symbol \(X_j\) by an element of \(K_\mu\), and simultaneously translating the corresponding unobserved source tail on that residue chain, preserves the product law and all differences. Thus the conditional law of each half given \(B\) depends only on \(C\). Consequently the two observed halves are conditionally independent given \(C\) as well. Since both determine \(C\), their mutual information is exactly \(\mathsf H(C)\).

The law \(\mu\) is constant on each left coset of \(K_\mu\). Conditional on a coset, its letter is uniform over \(|K_\mu|\) elements, so
\[
\mathsf H(K_\mu X_j)=\mathsf H(\mu)-\log_2|K_\mu|.
\]
The coset variables are independent across \(j\). Hence \(\mathsf H(C)=k(\mathsf H(\mu)-\log_2|K_\mu|)\), proving the excess-entropy identity without interchanging any questionable infinite sum.

**3. Full phase diagram.** The simplex of probability laws on \(G\) is finite dimensional. For each fixed \(g\in G\), the condition \(\mu(gx)=\mu(x)\) for all \(x\) is closed. Thus, if \(\mu_n\to\mu\), any subgroup occurring infinitely often as \(K_{\mu_n}\) must be a subgroup of \(K_\mu\). There are only finitely many subgroups. By continuity of finite-alphabet entropy, every convergent sequence of excess entropies has a limit of the stated subgroup form (pass to a constant-subgroup subsequence).

Conversely, fix any \(J\le K_\mu\). Choose a strictly positive law \(\nu_J\) with a distinct positive total mass on each left coset \(Jg\), uniformly distributed within that coset. Such a law has stabilizer **exactly** \(J\): every \(j\in J\) preserves each left coset, whereas an element \(h
otin J\) cannot preserve the law because \(
u_J(h)
e
u_J(e)\) by the distinct left-coset masses. For \(0<\varepsilon<1\), let \(\mu_\varepsilon=(1-\varepsilon)\mu+\varepsilon\nu_J\). Elements of \(J\) preserve both summands. Any element of \(K_\mu\setminus J\) fails to preserve the second summand, whereas an element outside \(K_\mu\) still fails to preserve the first for all sufficiently small \(\varepsilon\) (only finitely many inequalities are involved). Therefore \(K_{\mu_\varepsilon}=J\) for all sufficiently small positive \(\varepsilon\), and the subgroup value is attained as a limit. The choice \(J=K_\mu\) also follows by the constant sequence \(\mu_n=\mu\).

If \(K_\mu=\{e\}\), that trivial stabilizer persists under sufficiently small perturbations, so the formula is continuous. If \(|K_\mu|>1\), take \(J=\{e\}\) in the construction: the limit along generic perturbations exceeds the value at \(\mu\) by exactly \(k\log_2|K_\mu|\), proving discontinuity. For every subgroup \(J\le G\), the positive law \(\nu_J\) realizes that subgroup as claimed.

## Verification

The accompanying standalone `verify.py` builds the distribution of finite output words directly by enumerating independent source words, and separately evaluates the conditional orientation-posterior formula. It checks **38 independent finite-cylinder entropy identities** across cyclic groups of orders three and four and the nonabelian symmetric group on three letters, with \(k=1,2\). The test examples include trivial, order-two, and full stabilizers and source laws with unequal coset masses. These are finite checks only; the all-group result follows from the argument above, in particular the strong law of large numbers and the finite subgroup argument.

For illustration, let \(G=\mathbb Z/4\mathbb Z\) and \(\mu=(a,b,a,b)\), where \(a,b>0\), \(a+b=1/2\), and \(a\ne b\). Then \(K_\mu=\{0,2\}\) and \(\mathcal E_k(\mu)=k\,h_2(2a)\), with \(h_2\) the binary Shannon entropy. At the uniform law on this group, the attainable limiting excess entropies are exactly \(0\), \(k\), and \(2k\), corresponding to subgroup orders four, two, and one. For a nonnormal example, the group \(S_3\) with unequal left-coset masses and a two-element stabilizer has \(\mathcal E_k\) equal to \(k\) times the entropy of its three left-coset masses.

## Relationship to prior work

Lindgren and Nordahl (1988, Section 3, equations (3.10)–(3.17)) already calculated the effective measure complexity and its discontinuity for **binary** Rule 60 under a biased Bernoulli input, including a formula proportional to cellular-automaton time. That important binary result, and its consequences at binary XOR lags of powers of two, are **not** claimed here. Kari and Taati (2013, Example 6 and Example 7) likewise studied the binary XOR factor, its non-Gibbsian image, and its iterates. The present result instead classifies the complete information jump **for arbitrary finite groups**, including zero-probability source laws, nonnormal subgroups, every lag, and all subgroup-indexed limits at each parameter point. Neither inspected binary treatment gives a theorem for the full left-stabilizer lattice of nonabelian alphabet laws. Marzen and Crutchfield's work on renewal-process excess entropy concerns a different stationary-process family; Riechers and Crutchfield provide general hidden-Markov information formulae and an RRXOR example, but do not evaluate this group-stabilizer law.

## Limitations

The result applies to group differences from iid two-sided source sequences; it makes no corresponding assertion for correlated, nonstationary, or non-group alphabets. It determines limiting past–future mutual information but does **not** give optimal finite-observation convergence rates or explicit finite-sample statistical confidence bounds. The subgroup-limit classification allows constant approximating sequences; for isolated maximally symmetric laws, some values need not be approachable through *distinct* laws with the same stabilizer. The proof and numerical checks are internal mathematical validation, not independent audit or certification. Historical priority beyond the inspected sources remains a risk, particularly for specialized group-process literature that may not be indexed.

## References

1. K. Lindgren and M. G. Nordahl, *Complexity Measures and Cellular Automata*, Complex Systems **2** (1988), 409–440, especially Section 3, pp. 430–432. Public full text: https://wpmedia.wolfram.com/uploads/sites/13/2018/02/02-4-2.pdf.
2. J. Kari and S. Taati, *Statistical Mechanics of Surjective Cellular Automata*, arXiv:1311.2319, initially public 2013-11-10 UTC; subsequently Journal of Statistical Physics **160** (2015), 1198–1243, especially Examples 6–7. https://arxiv.org/abs/1311.2319.
3. K. Lindgren, *An Information-Theoretic Perspective on Coarse-Graining, Including the Transition from Micro to Macro*, Entropy **17** (2015), 3332–3351, especially Section 2.3, DOI:10.3390/e17053332.
4. S. Marzen and J. P. Crutchfield, *Informational and Causal Architecture of Discrete-Time Renewal Processes*, arXiv:1408.6876, initially public 2014-08-28 UTC.
5. P. M. Riechers and J. P. Crutchfield, *Spectral Simplicity of Apparent Complexity, Part II: Exact Complexities and Complexity Spectra*, arXiv:1706.00883, initially public 2017-06-03 UTC, especially Section VII.
