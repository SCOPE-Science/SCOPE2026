# Exact reciprocity budget for prescribed partner-choice equilibria

## Finding

Let \(n\ge 1\), let \(f:\{1,\ldots,n\}\to\{1,\ldots,n\}\) be any designated partner-choice map, and assign strictly positive incentive gaps \(\delta_1,\ldots,\delta_n\). For a positive payoff matrix \(U\), impose the strong row-optimality inequalities
\[
U_{i,f(i)}-U_{ij}\ge\delta_i\quad\text{for every }i\text{ and }j\ne f(i).
\]
Its reciprocity defect is \(\mathcal A(U)=\max_{i<j}|U_{ij}-U_{ji}|\), with the empty maximum equal to zero. Write \(\mathcal C_{\ge3}(f)\) for the directed cycles of \(f\) of length at least three. The exact minimum reciprocity defect needed to realize \(f\) is
\[
\boxed{\min_U\mathcal A(U)=
\max_{C\in\mathcal C_{\ge3}(f)}\frac{1}{|C|}\sum_{i\in C}\delta_i,}
\]
where the outer maximum is zero when there is no such cycle. The minimum is attained by a matrix with strictly positive entries and the prescribed strict best-response map.

In particular, with a common row gap \(\delta>0\), every one of the \(n^n\) partner-choice topologies is realizable at reciprocity budget \(\varepsilon\ge\delta\), while for \(0\le\varepsilon<\delta\) precisely the functional graphs whose directed cycles have length one or two are realizable. The cardinality of the latter already-classically-enumerated family is \(c_n\) with
\[
 c_n=\sum_{k=1}^n\binom nk I_k\,k\,n^{n-k-1},\qquad
 I_k=\sum_{j=0}^{\lfloor k/2\rfloor}\frac{k!}{2^j j!(k-2j)!},
\]
interpreting the \(k=n\) summand as \(I_n\). Its known generating function and asymptotic are
\[
\sum_{n\ge0}c_n\frac{z^n}{n!}=\exp(T(z)+T(z)^2/2),\quad
T(z)=ze^{T(z)},\qquad
c_n\sim 2e^{3/2}n^{n-1}.
\]
The enumeration and its asymptotic are pre-existing combinatorial facts (OEIS A209319), included solely to quantify the phase loss implied by the reciprocity-budget identity. The new claimed contribution is the exact heterogeneous-gap minimax reciprocity identity and its application to the nondegenerate partner-choice model.

## Assumptions and scope

The labeled set of types is finite, each type is permitted to choose itself, and positive real payoffs are unrestricted in magnitude. A type \(i\) chooses exactly one partner type \(f(i)\). A margin \(\delta_i>0\) is measured on the raw payoffs \(U_{ij}\); it is not an invariant of rescaling each row. Reciprocity refers specifically to numerical payoff equality \(U_{ij}=U_{ji}\), not to a two-player symmetric game in the usual game-theoretic sense. The latter may have unequal off-diagonal payoff entries.

The budget \(\varepsilon\ge0\) bounds the maximum absolute reciprocal payoff discrepancy over distinct types, without constraining diagonal entries. No stochastic steady-state, finite-rationality mixing or statistical identifiability result is claimed. All optimality inequalities ensure the unique maximizer in each payoff row.

## Proof

**Lower bound.** Consider a directed cycle \(v_0\to v_1\to\cdots\to v_{\ell-1}\to v_0\) of length \(\ell\ge3\), with indices modulo \(\ell\). Since the predecessor \(v_{t-1}\) differs from the successor \(v_{t+1}\), the row gap implies
\[
 U_{v_t,v_{t+1}}-U_{v_t,v_{t-1}}\ge\delta_{v_t}.
\]
Summing and reindexing the second terms gives
\[
\sum_{t=0}^{\ell-1}\delta_{v_t}
\le\sum_{t=0}^{\ell-1}(U_{v_t,v_{t+1}}-U_{v_{t+1},v_t})
\le\ell\,\mathcal A(U).
\]
Taking the largest cycle mean proves the universal lower bound. There is no analogous bound from a loop (no alternate predecessor), or a directed two-cycle (predecessor and successor coincide).

**Attaining the bound.** Let \(D=\max_i\delta_i\), choose \(L=(n+2)D+1\) and \(B=(n+3)L\), and initially set every matrix entry to \(1\). In each directed cycle of length one, set its diagonal entry to \(B\); in each directed cycle of length two, set both mutual entries to \(B\).

For each directed cycle \(C=(v_0,\ldots,v_{\ell-1})\) of length \(\ell\ge3\), put \(\mu_C=\ell^{-1}\sum_{i\in C}\delta_i\). Define \(a_0=0\) and recursively \(a_t-a_{t-1}=\delta_{v_t}-\mu_C\) for \(1\le t<\ell\). Set
\[
 U_{v_t,v_{t+1}}=B+a_t,\qquad
 U_{v_{t+1},v_t}=B+a_t-\mu_C
\]
for every cyclic \(t\). The telescoping sum guarantees the corresponding row gap at \(t=0\), while the recursion guarantees it for the other vertices. Each reciprocal pair in this cycle differs by precisely \(\mu_C\).

Every remaining vertex belongs to a unique in-tree directed toward a cyclic vertex. For a noncyclic vertex \(v\) at depth \(d\ge1\) from its cyclic root, set the two entries on its parent edge to \(B-dL\). This assignment is consistent because the noncyclic parent edges form an ordinary forest. All unmentioned entries remain \(1\), including unused diagonal and chord entries. The cycle offsets satisfy \(|a_t|\le nD\), and every parent edge is positive. Within an in-tree, the chosen parent is favored over any child by at least \(L>D\); at a cycle vertex the prescribed cyclic partner beats every attached tree child by at least \(L-nD>D\), and its other on-cycle competitor by its exact required gap. Because \(B\) is large, unmentioned entries \(1\) are inferior by more than \(D\) everywhere. Therefore the row inequalities hold for all \(i,j\), and all payoffs are positive. Only the length-at-least-three cycle edges exhibit nonzero reciprocal discrepancies, each of size \(\mu_C\). Thus the lower bound is attained.

**Budget transition and enumeration.** When all gaps equal \(\delta\), the minimum is \(0\) if all cycles have length one or two, and \(\delta\) otherwise. This proves the sharp threshold. For completeness, select the \(k\) cyclic vertices (\(\binom nk\) ways), arrange them into an involution (\(I_k\) ways), and attach all other labels in a forest rooted at those \(k\) specified roots (\(k n^{n-k-1}\) ways). This gives the stated known exact count. Equivalently, rooted labeled trees have exponential generating function \(T=ze^T\); replacing every cycle by a loop or transposition yields \(\exp(T+T^2/2)\).

For the recorded asymptotic, put \(F(u)=\exp(u+u^2/2)\), apply Lagrange inversion, and obtain
\[
\frac{c_n}{n^{n-1}}=\frac{[u^{n-1}]F'(u)e^{nu}}{[u^{n-1}]e^{nu}}.
\]
Writing \(F'(u)=\sum_{j\ge0}b_j u^j\) with \(b_j\ge0\), this ratio is \(\sum_{j=0}^{n-1} b_j\prod_{h=1}^j(1-h/n)\), which converges by dominated convergence to \(F'(1)=2e^{3/2}\). This rederives a previously recorded asymptotic; it is not asserted as new.

## Verification

Run `python check.py`. The standalone program uses exact rational arithmetic to construct and validate the attaining payoff matrix for all \(\sum_{n=1}^6 n^n=50{,}069\) labeled maps with the heterogeneous gaps \(\delta_i=i\), including all cycle topologies through six types. The restricted-map totals are \(1,4,25,218,2451,33832\) for one through six types and agree with the published OEIS A209319 values. As a separate numerical linear-programming formulation, SciPy HiGHS independently finds the same optimal reciprocity defect on every map with three or four types (\(283\) instances). This tests the construction and minimax sharpness for finite cases; the proof establishes the result for all finite orders.

## Relationship to prior work

Riedl and Smead (2026), *Strategic Origins of Network Structure*, define the game-graph equilibrium through row-wise partner preference and prove \(n^n\) nondegenerate labeled topologies in their Supplementary Information, Proposition 6. Their proof allows arbitrary payoff matrices; their phrase “symmetric game” describes a two-player interaction, not the stronger equation \(U_{ij}=U_{ji}\). The present theorem asks how much departure from reciprocal numerical payoffs is **necessary and sufficient** to realize any specified topological preference map with quantitative row gaps. The earlier unrestricted realizability theorem neither supplies nor contradicts the cycle-mean optimum.

The no-long-cycle observation at exact reciprocity is the classical two-cycle phenomenon for unique-neighbor choices on undirected weighted graphs. The entire enumerative sequence, its generating function, and its asymptotic already appear as OEIS A209319 (and in A246522, column two); they are explicitly not claimed as discoveries. The new assertion is the sharp minimax extension from exact reciprocity to arbitrary positive heterogeneous margins, together with the interpretation of its exact budget transition for partner-choice equilibria. Classical functional-digraph decomposition underlies its counting corollary.

## Limitations

The identity requires independently specifiable positive payoff entries and strictly positive row margins. It does not enforce a common normalized payoff scale, prescribed diagonal levels, equilibrium mixing at finite rationality, bidirectional acceptance, or network edge reciprocity. Row scaling changes both margins and the measured defect. The result does not imply empirical detectability of reciprocity or novelty of the underlying functional-graph counts. Independent scientific audit has not been performed. Unindexed work on approximate symmetric preference representation could conceivably contain the same quantitative minimax statement.

## References

1. Christoph Riedl and Rory Smead, *Strategic Origins of Network Structure*, arXiv:2610.24792v1, first publicly posted 2026-10-17. https://arxiv.org/html/2610.24792v1. Especially Materials and Methods and Supplementary Information S2, Proposition 6.
2. Geoffrey Critzer and contributors, OEIS A209319, *Number of functions whose cycle lengths are at most two*, first entered 2013. https://oeis.org/A209319. Includes exact generating function and the asymptotic constant.
3. OEIS A246522, *Number of endofunctions whose cycle lengths divide a prescribed integer*, especially column two. https://oeis.org/A246522.
4. Oscar Defrain, Antonio E. Porreca, and Ekaterina Timofeeva, *Polynomial-delay generation of functional digraphs up to isomorphism*, Discrete Applied Mathematics 357 (2024), 24–33. DOI:10.1016/j.dam.2024.05.030 (background on classical functional-digraph structure, not on reciprocity defects).
