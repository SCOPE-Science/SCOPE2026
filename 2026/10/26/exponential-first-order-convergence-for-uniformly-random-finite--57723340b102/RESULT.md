# Exponential first-order convergence for uniformly random finite total preorders

## Finding

Let \(W_n\) be uniformly distributed over all reflexive, transitive, total binary relations \(R\) on the labelled universe \([n]\), for every integer \(n\ge 1\). Put \(\rho=\log 2\). For **every** first-order sentence \(\varphi\) in the relational signature \(\{R\}\), there exist constants \(L_\varphi\in[0,1]\) and \(c_\varphi\in(0,1)\) such that

\[
\Pr(W_n\models\varphi)=L_\varphi+O_\varphi(c_\varphi^n).
\]

Moreover, \(L_\varphi\in\mathbb Q(\log 2)\), and \(L_\varphi\) is effectively calculable from \(\varphi\) through a finite, aperiodic word-type monoid and an associated stochastic matrix. This is a **first-order convergence law, not a zero-one law**: for example, the probability that the least equivalence class has one element converges to \(\log 2\). The distinct event that the least class is a singleton and the greatest class has two elements has limiting probability \((\log 2)^3/2\).

The claim is about labelled total preorders sampled uniformly, not uniformly sampled unlabelled ordered partitions and not the class of all S4 frames.

## Assumptions and scope

A total preorder is a relation \(R\) that is reflexive, transitive and total (for any \(x,y\), either \(xRy\) or \(yRx\)). Let \(x\sim y\) mean \(xRy\wedge yRx\). The \(\sim\)-classes are nonempty, linearly ordered by \(R\). Writing their sizes from least to greatest as \((s_1,\dots,s_k)\), all \(s_i\) are positive and sum to \(n\). There are exactly \(n!/\prod_i s_i!\) labelled total preorders having this list of sizes. No additional relation symbols, parameters, or uniformly random first-order interpretations are assumed.

The exponential rate \(c_\varphi\) may depend on the entire sentence. A mathematical decision procedure (potentially with very large complexity in sentence size) can compute the limiting expression, not necessarily a practical polynomial-time inference algorithm.

## Proof

**Step 1: from structures to finite words.** Fix \(q=\max(1,\operatorname{qr}(\varphi))\). Replace each positive block size \(s\) by the letter \(\tau_q(s)=\min(s,q)\) in the alphabet \(A_q=\{1,\ldots,q\}\); the final letter \(q\) represents *all* sizes at least \(q\). If two resulting words are equivalent in the \(q\)-round Ehrenfeucht--Fraïssé game for linearly ordered, \(A_q\)-coloured positions, then their expanded total preorders are \(q\)-equivalent. Indeed, a move on an element determines its block. Duplicator uses the word game to match that block and matches already chosen elements within each block by their equality pattern. Blocks of sizes below \(q\) have equal sizes, while two sizes at least \(q\) contain enough fresh elements for the at most \(q\) moves. The global order relation is exactly the block order, so this is a partial isomorphism. Consequently, truth of \(\varphi\) depends only on the word's \(q\)-type.

**Step 2: finite aperiodic type monoid.** Let \(M_q\) be the finite monoid of first-order quantifier-rank-\(q\) equivalence classes of \(A_q\)-coloured finite linear words, with concatenation product, identity the empty word, and \(E_\varphi\subseteq M_q\) the accepted types. Concatenation respects \(q\)-equivalence by the standard interval-game composition argument. For every word \(u\), sufficiently many successive copies of \(u\) become indistinguishable by \(q\)-round games: for example, any two powers \(u^m,u^{m+1}\) with \(m\ge2^q\) are \(q\)-equivalent. Thus \(M_q\) is aperiodic: every \(a\in M_q\) satisfies \(a^{2^q}=a^{2^q+1}\). Both the monoid and \(E_\varphi\) are effectively obtainable from finite-rank types and a representative model.

**Step 3: exact matrix exponential generating function.** For each letter \(a\in A_q\), define

\[
 B_a(z)=\sum_{s\ge1:\,\tau_q(s)=a}\frac{z^s}{s!}.
\]

Thus \(B_s(z)=z^s/s!\) if \(1\le s<q\), and \(B_q(z)=e^z-\sum_{s=0}^{q-1}z^s/s!\). Let \(T_a\) be the zero-one transition matrix of right multiplication by letter \(a\) on \(M_q\), and put \(K(z)=\sum_{a\in A_q} B_a(z)T_a\). Denote by \(e\) the row vector selecting the identity element, and by \(v\) the column indicator vector of \(E_\varphi\). The number \(N_\varphi(n)\) of labelled \(n\)-world total preorders satisfying \(\varphi\) has the *exact* exponential generating function

\[
 \sum_{n\ge0}\frac{N_\varphi(n)}{n!}z^n=e(I-K(z))^{-1}v.
\]

The sum over all finite block words is the matrix geometric series. Without the acceptance condition, the total enumerator is the ordered-Bell/Fubini generating function

\[
 \sum_{n\ge0}\frac{F_n}{n!}z^n=\frac1{1-\sum_a B_a(z)}=\frac1{2-e^z}.
\]

In each coefficient these identities are finite sums. The value assigned at \(n=0\) is immaterial to the claimed positive-size asymptotics.

**Step 4: the simple dominant pole.** Since \(e^\rho=2\), the matrix \(P=K(\rho)\) is stochastic. Every letter has strictly positive probability \(B_a(\rho)\). Each recurrent communicating class of the finite right-multiplication chain is aperiodic: for any letter \(a\), the element \(a^{2^q}\) is idempotently stable; starting from a recurrent state and repeatedly multiplying by \(a\) yields a state in the same recurrent class with a one-step \(a\)-self-loop. Thus the stochastic powers \(P^m\) converge to a projection \(H\), the projection onto the space of \(P\)-harmonic vectors.

For every harmonic vector \(h\), the value of \(h\) is constant on each recurrent class. Moreover, for a state inside that class, all letter transitions stay inside it and \(K'(\rho)h=2h\), since \(\sum_a B'_a(\rho)=e^\rho=2\). The harmonic projection is uniquely determined by its recurrent-class values, whence

\[
 HK'(\rho)H=2H.
\]

As eigenvalue \(1\) of a stochastic matrix is semisimple, analytic finite-dimensional spectral perturbation yields

\[
 (I-K(z))^{-1}=\frac{H}{2(\rho-z)}+\text{a function holomorphic near }\rho.
\]

There are no competing singularities on the circle \(|z|=\rho\). Indeed for \(|z|=\rho\), \(z\ne\rho\), the series \(B_q(z)\) includes two consecutive positive-degree monomials with distinct arguments, so \(|B_q(z)|<B_q(\rho)\), while \(|B_a(z)|\le B_a(\rho)\) for the remaining letters. Therefore every row of \(K(z)\) has absolute row sum strictly less than \(\sum_a B_a(\rho)=1\). On \(|z|<\rho\), the same conclusion follows from \(e^{|z|}-1<1\). Analyticity and compactness now give some \(R_\varphi>\rho\) such that the displayed pole is the only singularity in \(|z|<R_\varphi\). The same singularity statement holds for \(1/(2-e^z)\).

Taking coefficients and dividing the two generating functions gives

\[
 \Pr(W_n\models\varphi)=eHv+O_\varphi(c_\varphi^n)
\]

for some \(0<c_\varphi<1\). The zero or unit value of \(eHv\) does not affect the absolute exponential error.

**Step 5: value field, effectiveness and non-zero-one example.** The transition probabilities are \(B_s(\rho)=\rho^s/s!\) for \(s<q\) and \(B_q(\rho)=1-\sum_{s<q}\rho^s/s!\). Entries of \(P\) therefore lie in \(\mathbb Q(\rho)\). Finite recurrent-class stationary vectors and transient absorption probabilities solve finite linear systems over this field; hence \(H\), and thus \(eHv\), have entries in \(\mathbb Q(\rho)\). This also supplies an effective formula for the limit.

The number of total preorders whose least block is a singleton is \(nF_{n-1}\), while the number having a least singleton and a greatest block of size two is \(n\binom{n-1}{2}F_{n-3}\) for \(n\ge3\). Since \(F_n/n!\sim 1/(2\rho^{n+1})\), their limiting probabilities are respectively \(\rho\) and \(\rho^3/2\). Both conditions are first-order definable via \(R\), and \(0<\rho<1\), so a zero-one law fails.

## Verification

The standalone file `check.py` enumerates every surjective rank assignment of labelled elements to an ordered sequence of nonempty blocks for \(1\le n\le7\), independently enumerates all integer compositions weighted by their multinomial coefficients, and compares the full block-size histograms. It checks the ordered Bell counts \(1,3,13,75,541,4683,47293\), the exact first/last block counting formulas, and convergence numerics for the first-singleton probability. Run `python check.py` from the same directory; successful completion prints `TOTAL_PREORDER_BLOCK_WORD_CHECK_OK`.

The finite checker tests enumerative identities, not the infinite-rank game lemma or analytic pole argument. Those steps are justified mathematically above. The proof uses the familiar first-order word-type monoid and finite stochastic-chain facts, not an unverified computational extrapolation.

## Relationship to prior work

Tóth and collaborators' 2026 paper on weighted first-order model counting for ordered domains (arXiv:2608.10877, first public 11 August 2026) motivates the question of exact logical probabilities on finite ordered structures. Its Section 7 and Appendix E explicitly recover ordered Bell numbers through a different first-order counting encoding; their enumeration is **not new here**. The inspected paper treats model-counting complexity of restricted fragments, not the exponential all-first-order convergence law for uniformly sampled total preorders or the limit-value field above.

Koponen and Karlsson, *Convergence Laws for Expansions of Linear Preorders* (WoLLIC 2025), is a particularly close title but treats random **expansions of a fixed deterministic sequence of linear preorders** whose equivalence classes all grow faster than any logarithm while remaining subpolynomial. Its public full abstract explicitly establishes a zero-one law for sentences of the expansions in that regime. Here, by contrast, the base preorder itself is uniformly random, has typically many bounded-size blocks, and its underlying first-order sentence “the least block is a singleton” has a nonzero, nonunit limiting probability. Thus its hypotheses do not cover this sampling model; the full 2025 primary text was inaccessible, so this comparison rests on its official conference abstract and author institutional record.

The ordered Bell generating function is classical (OEIS A000670). The finite aperiodic-monoid characterization of first-order word languages is classical (Schützenberger--McNaughton--Papert; e.g. Bojańczyk, *Nominal Monoids*, introduction, 2013). The argument here combines these tools with a new, explicitly stated random-total-preorder limiting distribution and the analytic matrix pole calculation; it does not claim these ingredients independently as new. Logical limit-law techniques for other random structures (e.g. Mallows permutations and attachment graphs) are related but are different probability models.

## Limitations

The rate constant depends on the sentence and is not asserted uniform in quantifier rank. The proof assumes one binary total-preorder relation with **uniform labelled** sampling and standard first-order logic; no analogous claim is made for arbitrary preorders, additional random predicates, modulo-counting logic, or other sampling schemes. Although published sources and mathematical research records were searched, an older general weighted-word convergence theorem might imply this as a specialization; no absolute historical priority is claimed.

## References

- J. Tóth, Q. Kuang, K. Zou, V. Kůla, Y. Wang, Y. Wang, and O. Kuželka, *Weighted First-Order Model Counting over Ordered Domains*, arXiv:2608.10877v1 (11 August 2026), https://arxiv.org/abs/2608.10877.
- M. Bojańczyk, *Nominal Monoids*, Theory of Computing Systems 53 (2013), 194–222, https://doi.org/10.1007/s00224-013-9464-1. The introduction recalls the classical Schützenberger--McNaughton--Papert characterization.
- OEIS A000670, Fubini/ordered Bell numbers, https://oeis.org/A000670.
- T. Müller, F. Skerman and T. W. Verstraaten, *Logical limit laws for Mallows random permutations*, arXiv:2302.10148 (2023), https://arxiv.org/abs/2302.10148 (distinct random-structure comparison).
- V. Koponen and E. Karlsson, *Convergence Laws for Expansions of Linear Preorders*, WoLLIC 2025, LNCS 15942, pp. 101–118, https://doi.org/10.1007/978-3-031-99536-1_7 (published conference abstract and author university record examined; full text unavailable).
