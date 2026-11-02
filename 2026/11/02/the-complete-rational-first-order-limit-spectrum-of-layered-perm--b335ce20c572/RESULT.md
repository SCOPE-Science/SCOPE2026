# The complete rational first-order limit spectrum of layered permutations

## Finding

Let \(\mathcal L_n=\operatorname{Av}_n(231,312)\), with a uniformly chosen permutation on \(n\) points, regarded as a structure with the position order \(<_1\) and value order \(<_2\). Let \(\operatorname{Lim}_{\rm FO}(\mathcal L)\) be the set of limits of probabilities of first-order sentences in this two-order language. Then

\[
\operatorname{Lim}_{\rm FO}(\mathcal L)=\mathbb Q\cap[0,1].
\]

This is an exact set equality, not merely density. More constructively, for every pair of integers \(0\le a\le b\), \(b\ge1\), an explicit first-order sentence \(\Phi_{a,b}\) satisfies, for every \(n\ge1\),

\[
\Pr_{\pi\in\mathcal L_n}(\pi\models\Phi_{a,b})=\frac ab\Pr(H_{b,n}),
\]

where \(H_{b,n}\) is an explicitly defined first-occurrence event, and

\[
0\le\frac ab-\Pr(\Phi_{a,b})\le
\left(1-2^{-N}\right)^{\lfloor(n-1)/N\rfloor},
\qquad N=2\max\{1,\lceil\log_2b\rceil\}+5.
\]

The witnessing binary patterns have length \(N=O(\log b)\). Taking the ordinary first-order quantifier rank, one can arrange \(\operatorname{qr}(\Phi_{a,b})\le N+3=2\max\{1,\lceil\log_2b\rceil\}+8\); a written-out sentence has length polynomial in \(b\).

## Assumptions and scope

The statement concerns **uniform** sampling from the \(2^{n-1}\) layered permutations of size \(n\), first-order TOTO sentences without counting or modular predicates, and their ordinary real probability limits. It does not concern all \(231\)-avoiding permutations, arbitrary distributions, or monadic second-order sentences.

Every \(\pi\in\mathcal L_n\) has a unique decomposition as a direct sum of decreasing blocks. The \(n-1\) binary cut symbols \(c_1,\ldots,c_{n-1}\) specify whether the successive positions lie in distinct blocks: \(c_i=1\) exactly when \(\pi_i<\pi_{i+1}\). Hence these bits are independent fair Bernoulli variables under uniform sampling. Adjoin the formal final bit \(c_n=0\). For distinct positions \(i<j\), the value comparison \(\pi_i<\pi_j\) holds exactly when one of \(c_i,\ldots,c_{j-1}\) is \(1\). Thus both orders are definable in the ordinary first-order language of a linearly ordered word whose unary predicate marks \(1\)-bits, and conversely the cut predicate is defined in TOTO by \(C(x)\iff\exists y\,[\operatorname{Succ}_1(x,y)\land x<_2y]\).

## Proof

**1. No irrational limit.** Let \(\varphi\) be any TOTO sentence. The preceding interpretation turns it into a first-order sentence over binary words, evaluated on words of length \(n\) whose last symbol is \(0\). By the Schützenberger–McNaughton–Papert theorem, its language has an aperiodic finite syntactic monoid and a complete deterministic automaton with aperiodic transition monoid. Write \(T_0,T_1\) for its \(0\)- and \(1\)-transition matrices on reachable states, \(v\) for the rational initial row vector and \(f\) for its accepting-state column vector. Then

\[
\Pr(\varphi)=v\big((T_0+T_1)/2\big)^{n-1}T_0f.
\]

Let \(P=(T_0+T_1)/2\). In every closed communicating class of this finite Markov chain, repeated \(0\)-transitions remain in the class. Since the transformation \(T_0\) is eventually idempotent, that class contains a state fixed by \(T_0\). This state has a positive self-loop under \(P\), so the communicating class has period one. Therefore \(P^m\) converges as \(m\to\infty\). Its limit is a rational matrix: the stationary distributions of rational irreducible stochastic blocks and the transient-to-recurrent absorption probabilities solve finite nonsingular linear systems over \(\mathbb Q\). Consequently every first-order limiting probability is rational. This direction is also implicit in the finite dyadic, aperiodic Markov-chain method of Braunfeld and Kukla (2022), which already proves convergence; it is not claimed to be a new general rationality principle.

**2. Cross-bifix-free words.** Fix \(a,b\). Put \(t=\max\{1,\lceil\log_2b\rceil\}\), \(L=t+3\), and choose distinct binary strings \(u_0,\ldots,u_{b-1}\) of length \(t\), for example the binary representations of \(0,\ldots,b-1\) padded to length \(t\). Set

\[
w_j=0^L1u_j1,\qquad N=2t+5.
\]

No proper suffix of any \(w_i\) is a prefix of any \(w_j\). Indeed, for an overlap of length at most \(L\) the suffix ends in \(1\), whereas the prefix consists of zeros. For overlap length greater than \(L\), the overlapping suffix starts at some positive shift \(s\le t+1\) inside the leading zero run and contains its subsequent \(1\) in one of the first \(L\) overlap positions, whereas the prefix contains only zeros there. Thus occurrences of these \(b\) words at distinct starting positions cannot overlap, even with different labels.

**3. Exact finite symmetry.** In a binary string of length \(n-1\), replace every occurrence of \(w_i\) by \(w_j\) and every occurrence of \(w_j\) by \(w_i\). The replacements are disjoint, and the cross-bifix-free property implies that they cannot create an occurrence at a previously unoccupied starting position. Replacing again restores the original string. Thus this operation is a length-preserving involution which preserves all occurrence starting positions and interchanges the labels \(i,j\). All \(b\) possible labels of the first occurrence therefore have equal counts for every length, conditional on there being at least one occurrence. Let \(H_{b,n}\) mean that a designated word occurs, and let \(\Phi_{a,b}\) mean that its earliest occurrence has label among \(0,\ldots,a-1\). Then exactly \(a/b\) of the strings in \(H_{b,n}\) satisfy \(\Phi_{a,b}\). For \(a=0\), take an impossible sentence; for \(a=b\), take the existence-of-occurrence sentence.

**4. First-order realization.** A position is a cut precisely when the definable predicate \(C\) holds. For a fixed binary word \(w\) of length \(N\), the assertion that \(w\) occurs beginning at \(x\) is first order: quantify \(N\) consecutive positions beginning at \(x\) and assert \(C\) or \(\neg C\) at each as prescribed. Because each \(w_j\) ends in \(1\) and the last position is always \(\neg C\), no designated occurrence uses that final position. The earliest start among the finite disjunction of patterns is first-order definable using \(<_1\). Hence \(\Phi_{a,b}\) is a genuine TOTO sentence, not a probabilistic or second-order event. With \(\operatorname{Succ}_1\) expressed using one nested quantifier, each cut test \(C\) has rank at most two, each length-\(N\) pattern-at-\(x\) test has rank at most \(N+1\), and the outer existential earliest-start witness plus universal no-earlier-start condition add two more levels. Thus the displayed rank bound \(N+3\) holds.

**5. Almost-sure occurrence.** Inspect disjoint blocks of \(N\) bits in the \(n-1\) freely sampled bits. Each such block equals \(w_0\) independently with probability \(2^{-N}\). Therefore

\[
\Pr(H_{b,n}^{\mathrm c})\le\left(1-2^{-N}\right)^{\lfloor(n-1)/N\rfloor}\longrightarrow0.
\]

The exact identity of Step 3 now implies \(\Pr(\Phi_{a,b})\to a/b\). Together with Step 1 this proves the asserted equality of spectra.

## Verification

The supplied standalone `checker.py` tests the exact cross-bifix-free property for denominators through \(16\), the finite-sample symmetry for explicit finite words, the involutions preserving occurrence positions, the exact finite identities for selected \(a,b,n\), and the direct layered-permutation encoding against all permutations up to seven points. Its successful status is `ALL_CHECKS_OK`. These finite tests are corroboration only. The all-denominator theorem rests on the symbolic arguments in Steps 1–5, particularly the aperiodic-automaton rationality theorem and the no-overlap proof. To reproduce: `python checker.py` with an ordinary Python 3 interpreter and no nonstandard packages.

## Relationship to prior work

Braunfeld and Kukla, *Logical limit laws for layered permutations and related structures* (2022), prove the first-order convergence law and the uniform interdefinability of layered permutations with convex linear orders (their Lemma 3.5 and Theorem 3.6); their finite fair-transition Markov chain also implies rationality of limits, but their theorem does not determine which rational values occur. Falgas-Ravry, Markström, Räty and Skerman, *On first-order limiting probabilities for small permutation classes* (arXiv:2610.34328, first public 2026-10-25), prove density of the limit spectrum for every small exponentially growing permutation class (Theorem 1.4), rather than exact attainment. The present result gives the full spectrum for the particular natural class \(\operatorname{Av}(231,312)\), by a uniform first-occurrence construction. Berthé, Goulet-Ouellet and Perrin (2025) provide much more general existence and formula results for densities of regular languages under stationary measures, and recall older rationality results for rational Bernoulli measures; these statements are also credited rather than claimed as new. The classical McNaughton–Papert–Schützenberger characterization and elementary rational Markov-chain facts are used, not claimed as new.

An existing related calculation establishes rational *attainment* for the narrower Fibonacci class \(\operatorname{Av}(231,312,321)\); it neither describes all its irrational exclusions nor implies rational attainment for the larger, differently distributed class treated here. The binary first-occurrence method is related, but the exact upper-and-lower classification and the uniform full layered class are distinct. Possible older results in aperiodic language density or random convex orders remain a historical-priority risk.

## Limitations

The result determines the set of limiting values, not an optimal quantifier-rank bound for a given denominator, not the distribution of first-order formulas, and not the corresponding spectra in more expressive logics. The numerical checks terminate at explicit finite parameters and do not certify infinite quantifiers. The historical novelty comparison is based on inspected literature and semantic indexing, not an independent exhaustive priority search. No independent mathematical audit has been performed.

## References

1. S. Braunfeld and M. Kukla, *Logical limit laws for layered permutations and related structures*, 2022, arXiv:2111.06307, especially §§2–3, Lemma 3.5 and Theorem 3.6.
2. V. Falgas-Ravry, K. Markström, E. Räty and F. Skerman, *On first-order limiting probabilities for small permutation classes*, 2026, arXiv:2610.34328, Theorem 1.4.
3. R. McNaughton and S. Papert, *Counter-Free Automata*, 1971; M.-P. Schützenberger, *On finite monoids having only trivial subgroups*, 1965 (first-order definability and aperiodicity).
4. V. Berthé, H. Goulet-Ouellet and D. Perrin, *Density of Rational Languages Under Shift Invariant Measures*, ICALP 2025, DOI:10.4230/LIPIcs.ICALP.2025.143, especially §§3.2 and 5.
5. M. Bojańczyk, *Nominal Monoids*, Theory of Computing Systems 53 (2013), introductory recollection of the Schützenberger–McNaughton–Papert theorem.
