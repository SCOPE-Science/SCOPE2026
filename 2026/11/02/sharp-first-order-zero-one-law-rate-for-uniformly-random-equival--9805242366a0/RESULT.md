# Sharp first-order zero-one-law rate for uniformly random equivalence relations

## Finding

Let \(E_n\) be an equivalence relation sampled uniformly among all \(B_n\) equivalence relations on a labelled \(n\)-element set. Let \(E_\infty\) be a countable equivalence relation with infinitely many classes of each finite positive size, with no infinite classes. For every fixed integer \(r\ge2\), write \(E_n\equiv_r E_\infty\) if the two structures agree on **every** first-order sentence in the vocabulary \(\{E,=\}\) of quantifier rank at most \(r\). Define \(w_n>0\) by \(w_ne^{w_n}=n\). Then

\[
\Pr(E_n\not\equiv_r E_\infty)
\sim \frac{w_n^{r-1}}{(r-2)!\,n}.
\]

In particular the uniform Bell-partition model has a first-order zero-one law, and the displayed expression is the exact leading probability of *any disagreement at rank at most* \(r\), rather than the error for one selected sentence. The leading obstruction is the presence of fewer than \(r-1\) singleton equivalence classes.

## Assumptions and scope

The language has one binary equivalence predicate and equality, without added order, colors, constants, parameters, counting quantifiers, or second-order operators. The sampling law is uniform over all labelled partitions of \([n]\), not uniform over integer partitions or isomorphism types. Quantifier rank \(r\) is fixed while \(n\to\infty\). The limit structure \(E_\infty\) has exactly countably infinitely many classes of every positive finite cardinality; it is not asserted to be \(\omega\)-categorical. The symbol \(\equiv_r\) concerns agreement on sentences, not tuple types with parameters.

## Proof

**Step 1: an exact rank-\(r\) singleton obstruction.** Write \(N_j(E)\) for the number of classes of cardinality \(j\). The following sentence has quantifier rank exactly \(r\):

\[
\sigma_r:=\exists x_1\cdots\exists x_{r-1}\;\forall y\;\left[
\bigwedge_{1\le i<j\le r-1}\neg E(x_i,x_j)
\ \land\ \bigwedge_{i=1}^{r-1}(E(x_i,y)\to y=x_i)
\right].
\]

It asserts that there are at least \(r-1\) distinct singleton classes. Consequently \(N_1(E_n)<r-1\) forces \(E_n\not\equiv_r E_\infty\).

**Step 2: a sufficient small-class supply and the game argument.** Suppose a finite equivalence relation \(E\) satisfies \(N_1(E)\ge r-1\) and \(N_j(E)\ge r\) for every \(j=2,\ldots,r\). In the length-\(r\) Ehrenfeucht--Fraïssé game against \(E_\infty\), Duplicator maintains a bijection between already opened classes, preserves equality and whether two picked elements lie in the same class, and uses classes of the exact same size for opened classes of size below \(r\); classes with at least \(r\) elements can imitate one another for all \(r\) rounds. At most \(r\) classes are opened. There are \(r\) unused classes of each size \(2,\ldots,r\) initially, enough for any such requests. For singleton classes Duplicator uses exact singleton matches for the first \(r-1\) distinct singleton classes encountered. Only if a \(r\)-th new singleton class is opened from the infinite structure can such a match fail; that opening must be the final move, so a fresh nonsingleton class is an indistinguishable response at the end of the game. Within a previously paired class, always reply with a fresh element when Spoiler chooses a fresh one; until the final move, paired classes have adequate remaining capacity. Thus Duplicator wins, and \(E\equiv_r E_\infty\).

The phrase “first \(r-1\) distinct singleton classes” counts classes exposed by the game, from either side, not all singleton classes in either model. This is why \(r-1\), not \(r\), is the sharp requirement.

**Step 3: fixed small-block probabilities.** Let \(B_n\) denote the \(n\)-th Bell number, and put \(F(z)=\exp(e^z-1)\). Marking classes of size \(j\) gives the exact coefficient identity, for each fixed \(j\ge1\) and \(t\ge0\):

\[
\Pr(N_j(E_n)=t)=\frac{n!}{B_n}\,
\frac{1}{t!(j!)^t}\,[z^{n-jt}]
\exp(e^z-1-z^j/j!).
\]

The standard positive-saddle coefficient estimate for assemblies, with saddle radius \(w_n\) satisfying \(w_ne^{w_n}=n\), yields, for each *fixed* \(j,t\),

\[
\Pr(N_j(E_n)=t)
=(1+o(1))\,\frac{1}{t!}
\left(\frac{w_n^j}{j!}\right)^t
\exp(-w_n^j/j!).
\]

Here is the needed relative-error justification: in the Cauchy integral for \(F\), the central Gaussian arc has angular width of order \((n(1+w_n))^{-1/2}\); the logarithm of the factor \(\exp(-z^j/j!)\) changes by \(O(w_n^j/\sqrt{n(1+w_n)})=o(1)\) there. Standard outer-arc bounds for \(F\), whose exponential term is \(\exp(e^{w_ne^{i\theta}})\), make the complementary integral negligible **even relative to** the central factor \(\exp(-w_n^j/j!)\), since \(w_n^j=o(n^\delta)\) for every fixed \(\delta>0\). Finally the fixed degree shift \(jt\) contributes \(w_n^{jt}(1+o(1))\) to the coefficient ratio. This establishes the displayed estimate without treating the small-block counts as literally independent Poisson variables at finite \(n\).

**Step 4: the matching asymptotics.** Since \(w_n\to\infty\), the \(j=1\) estimate gives

\[
\Pr(N_1<r-1)
\sim\frac{e^{-w_n}w_n^{r-2}}{(r-2)!}
=\frac{w_n^{r-1}}{(r-2)!\,n}.
\]

For each fixed \(j\ge2\), the same estimate summed over \(t=0,\ldots,r-1\) proves
\[
\Pr(N_j<r)=O_r\bigl((1+w_n^{j(r-1)})\exp(-w_n^j/j!)\bigr)
=o\bigl(e^{-w_n}w_n^{r-2}\bigr).
\]

By Step 2 and a union bound, the probability of \(E_n\not\equiv_r E_\infty\) is at most \(\Pr(N_1<r-1)+\sum_{j=2}^{r}\Pr(N_j<r)\). Step 1 supplies the matching lower bound, proving the theorem.

## Verification

The included standard-library `checker.py` independently generates Bell numbers and the number of partitions avoiding singleton blocks using a block-of-one recurrence. It compares exact singleton-count distributions against independent enumeration by integer-partition profiles for every \(0\le n\le8\), verifies the relevant finite probability identities, and checks the asymptotic ratios at \(n=80,160,320\). It returns `ALL_CHECKS_OK`. These are finite consistency tests; the infinite asymptotic and logical implications rest on the preceding proofs, not on numerical extrapolation.

## Relationship to prior work

Koponen (2026) studies finite-model approximation and logical convergence laws, including random expansions of finite base structures; it does not give this Bell-partition rank-\(r\) failure probability. Haigh (1972) established foundational random-equivalence-relation block-size statistics; these and the Bell generating function are prior ingredients, not claimed as novel. Goh and Schmutz (1994) study largest blocks and their multiplicities, a different asymptotic question. Earlier set-partition singleton generating functions and saddle-point methods are likewise standard. The new conclusion combines a sharp finite-rank logical obstruction with a small-block tail estimate to identify the precise probability of failure of the entire first-order rank-\(r\) theory.

## Limitations

This is an asymptotic for every **fixed** rank \(r\ge2\), not a uniform estimate when rank grows with \(n\). The conclusion does not apply to the distribution uniform over unlabelled partitions, to signatures with additional relations, or to monadic-second-order properties. The argument uses classical Bell-function saddle estimates; it does not purport to introduce new asymptotics for the component counts themselves. A complete archival survey for equivalent older logical formulations has not been performed.

## References

- V. Koponen, “A characterization of the finite model property for \(\omega\)-categorical theories,” arXiv:2610.16163v1, first posted 12 October 2026. https://arxiv.org/html/2610.16163v1
- J. Haigh, “Random equivalence relations,” Journal of Combinatorial Theory A 13 (1972), 287–295. https://doi.org/10.1016/0097-3165(72)90032-5
- W. M. Y. Goh and E. Schmutz, “Random Set Partitions,” SIAM Journal on Discrete Mathematics 7 (1994), 419–436. https://doi.org/10.1137/S0895480190186974
- “The largest singletons of set partitions,” European Journal of Combinatorics (2011). https://doi.org/10.1016/j.ejc.2010.10.011
