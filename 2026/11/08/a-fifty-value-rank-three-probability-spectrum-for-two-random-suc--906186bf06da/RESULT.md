# A fifty-value rank-three probability spectrum for two random successor orders

## Finding
Let \(S\) and \(T\) be the successor relations of two independent, uniformly chosen linear orders on the same \(n\)-element domain. The orders themselves are *not* in the vocabulary. Define the aligned- and reversed-overlap counts
\[
A_n=|\{(u,v):S(u,v)\land T(u,v)\}|,\qquad
B_n=|\{(u,v):S(u,v)\land T(v,u)\}|.
\]
Then \((A_n,B_n)\) converges in distribution to a pair of independent mean-one Poisson variables. Every sentence in the two-variable first-order language \(\{S,T,=\}\) of quantifier rank at most three has a limiting satisfaction probability. Its truth, outside an event of probability tending to zero, is determined by the nine-state pair
\[
\bigl(\min(A_n,2),\min(B_n,2)\bigr)\in\{0,1,2\}^2.
\]
Conversely every Boolean function of this pair is realized by a sentence of rank at most three. Consequently the complete rank-three limiting-probability spectrum is exactly
\[
\mathcal P_3=\bigl\{u z^2+v z(1-2z)+w(1-2z)^2:
0\le u,v\le4,\;w\in\{0,1\}\bigr\},\quad z=e^{-1}.
\]
It has **exactly fifty distinct members**. At quantifier rank at most two the corresponding spectrum is exactly
\[
\mathcal P_2=\bigl\{u z^2+v z(1-z)+w(1-z)^2:
 u,w\in\{0,1\},\;0\le v\le2\bigr\},
\]
with exactly twelve distinct members. These claims concern fixed formulas as \(n\to\infty\), without counting quantifiers or additional predicates.

## Assumptions and scope
The domain is \([n]\), where \(n\ge2\), and both orders are independent uniform permutations. A directed successor edge runs from a position's element to the next element. A formula may use only the two variable symbols \(x,y\), recycled under quantification; its *quantifier rank* is maximum nesting depth of ordinary quantifiers. The strict underlying linear orders, constants, counting quantifiers, functions, and third variables are unavailable. A value \(2\) in the nine-state statistic means **at least two**, not exactly two. Limits are taken for one fixed sentence at a time.

## Proof

### 1. Joint Poisson law
By simultaneous relabeling, fix the first order as \(1,2,\ldots,n\) and take the second as a uniform permutation of the same labels. For each \(i\in\{1,\ldots,n-1\}\), the potential aligned edge is \(i\to i+1\) and the potential reversed edge is \(i+1\to i\). Fix nonnegative integers \(r,s\) and put \(t=r+s\). In the mixed factorial moment \(\mathbb E[(A_n)_r(B_n)_s]\), an ordered selection of \(r\) distinct aligned candidates and \(s\) distinct reversed candidates specifies \(t\) directed edges. All but \(O_{r,s}(n^{t-1})\) selections have pairwise disjoint endpoints; there are \(n^t+O_{r,s}(n^{t-1})\) such selections. A set of \(t\) directed edges lying on disjoint directed paths is contained in a uniform linear order with probability
\[
\frac{(n-t)!}{n!}=\frac1{(n)_t}.
\]
Every non-disjoint selection contributes either zero (inconsistent successor requirements) or that same probability (compatible directed paths). In particular, its total contribution is \(O_{r,s}(n^{-1})\). Thus
\[
\mathbb E[(A_n)_r(B_n)_s]=1+O_{r,s}(n^{-1})\longrightarrow1.
\]
These are precisely all mixed factorial moments of independent \(\operatorname{Poisson}(1)\) variables. Their exponential generating function is finite in a neighborhood of the origin, so the multivariate factorial-moment theorem gives joint convergence. In particular the overlap counts are tight.

### 2. A normal-form observation for two variables
For a structure \(M\) in a binary relational vocabulary, define \(c_0(u)\) to be the truth values of all atomic formulas with the one argument \(u\) (here all successor loops are false). For \(j\ge0\), put
\[
c_{j+1}(u)=\left(c_j(u),\;\bigl\{(\operatorname{atp}(u,v),c_j(v)):v\in M\bigr\}\right),
\]
where \(\operatorname{atp}(u,v)\) records equality and all directed atomic \(S,T\) relations between the two arguments. Types are compared by the displayed recursively defined data, not by arbitrary integer labels. Structural induction on two-variable formulas shows that every unary formula of rank at most \(j\) is determined by \(c_j(u)\). Indeed a formula whose two symbols are free is a Boolean combination of binary atomic formulas and subformulas in which one symbol has been rebound; the latter depend on the unary type of the remaining free element. Consequently every two-variable *sentence* of rank at most \(j+1\) is determined by the set of realized \(c_j\)-types. The converse direction used below needs only explicit sentences, not an abstract definability claim for all types.

### 3. The high-probability isolated-defect property
Call a vertex *special* if it is an endpoint of either successor path or an endpoint of an aligned or reversed overlap edge. In a typical realization, the four path endpoints are distinct, and no special vertices from different endpoint or overlap configurations have distance at most four in the undirected union of the two paths. In addition, within distance two of each configuration, all neighbors have the four prescribed successor half-edge slots, except the one missing slot at a path endpoint or the two merged slots at the shared edge. No other neighbor identifications occur in these bounded neighborhoods.

This property has probability tending to one. Here is a counting justification rather than an independence assumption: after fixing \(K\) candidate overlaps, every specified additional accidental identification among a bounded number of successor steps, or an encounter of a prescribed endpoint, forces one extra equality involving a fresh location of a uniform random order. The number of choices for that location loses a factor of \(n\), whereas the number of permitted local patterns is bounded in terms of \(K\). Hence each prohibited finite pattern has expected count \(O_K(n^{-1})\). The analogous statement for endpoint configurations is immediate by uniform permutation exposure. As \(A_n+B_n\) is tight by Step 1, first restrict to \(A_n+B_n\le K\), apply the bound, and then let \(K\to\infty\). Isolated short cycles elsewhere in the union of the paths are **not** excluded or needed: they have no effect on the rank-one types and on the rank-two recurrence below unless they meet a special neighborhood.

### 4. Why the rank-three theory only sees nine states
Every vertex has four directed *slots*: \(S\)-predecessor, \(S\)-successor, \(T\)-predecessor, and \(T\)-successor. Its \(c_1\)-type records which slots are missing or represent the same neighbor, together with the always-available completely nonadjacent pair type. On the isolated-defect event there are exactly these role types: an ordinary vertex with four distinct neighbors; one of four endpoint roles (one missing slot); an aligned-overlap source or target (respectively a merged outgoing or incoming pair); and a reversed-overlap source or target (a merged outgoing-incoming pair). The ordinary role occurs \(n-O(A_n+B_n+1)\) times; each endpoint role once; each aligned role \(A_n\) times; and each reversed role \(B_n\) times. Each role is distinguished by its directed atomic masks.

Now consider \(c_2(u)\). Its nonempty-neighbor-mask entries depend on the \(c_1\)-roles of at most four adjacent vertices. They are fixed by the local isolated configurations. For an empty-mask entry and a particular \(c_1\)-role \(\tau\), the entry occurs exactly when some \(\tau\)-vertex is neither \(u\) itself nor adjacent to \(u\). On the isolated-defect event, at most one vertex of any *special* role is excluded in this way: distinct configurations are separated, and the two endpoints of an overlap have different roles. Thus this test depends on whether the total multiplicity of \(\tau\) is zero, one, or at least two. The ordinary role is abundant and always supplies such an entry.

The possible \(c_2\)-types themselves occur either at ordinary vertices outside the immediate special neighborhoods, at a special vertex, or at an immediate neighbor of a special vertex. For each fixed endpoint or overlap configuration its local list of types is deterministic, subject only to the aforementioned zero/one/at-least-two multiplicity tests. Every present configuration contributes its list; an ordinary vertex away from all configurations exists for sufficiently large \(n\). Therefore the **set** of realized \(c_2\)-types is fixed by \((\min(A_n,2),\min(B_n,2))\). Step 2 proves the upper bound for all sentences of rank at most three. Repeating the argument one level lower, the set of \(c_1\)-types is determined merely by whether \(A_n\) and \(B_n\) are zero, giving the rank-two upper bound.

### 5. Realization of every state and exact cardinalities
Let
\[
\alpha(x):=\exists y\,[S(x,y)\land T(x,y)],\qquad
\beta(x):=\exists y\,[S(x,y)\land T(y,x)].
\]
Their numbers of satisfying vertices are exactly \(A_n\) and \(B_n\): no vertex has two outgoing \(S\)-edges. The formula \(\exists x\,\alpha(x)\) expresses \(A_n\ge1\) at rank two, and
\[
\exists x\exists y\,[x\ne y\land\alpha(x)\land\alpha(y)]
\]
expresses \(A_n\ge2\) at rank three, with inner rebindings of \(x\) and \(y\) understood in their own subformulas. The corresponding formulas with \(\beta\) express the two reversed thresholds. Negation and Boolean combinations therefore define all nine states and all their unions with rank at most three. At rank two, their presence/absence events realize all four coarse states.

Write \(z=e^{-1}\). A mean-one Poisson variable equals zero or one with probability \(z\) each, and is at least two with probability \(1-2z\). By Step 1, the nine cells have four masses \(z^2\), four masses \(z(1-2z)\), and one mass \((1-2z)^2\); hence precisely the asserted coefficient ranges occur as subset sums. Since \(z=e^{-1}\) is transcendental, the three polynomials \(z^2\), \(z(1-2z)\), and \((1-2z)^2\) are rationally linearly independent as polynomial functions of \(z\); the fifty coefficient triples give fifty distinct numbers. Likewise the four rank-two coarse cells have masses \(z^2\), \(z(1-z)\), \(z(1-z)\), and \((1-z)^2\), yielding twelve distinct subset sums. This proves both exact spectra.

## Verification
Run `python checker.py` with a standard Python 3 interpreter. It enumerates every second order through size seven, checks the exact mixed factorial-moment identity against compatible directed-edge selections, checks symmetry under reversal, symbolically enumerates the fifty distinct spectrum polynomials, and compares recursive rank-two unary type sets in fifty-four sampled locally isolated models across all nine states. Its expected completion text is `TWO_SUCCESSOR_FINITE_CHECKS_OK`. None of these finite tests proves the asymptotic isolation lemma or the logical rank-three classification; those are established in Steps 3–4. The checker does not claim to certify historical novelty.

## Relationship to prior work
Jeż, Michaliszyn, and Witkowski (2026, arXiv:2610.19943) establish decidability and size bounds for finite satisfiability in the larger language with arbitrarily many freely interacting successor relations. Their primary results are algorithmic rather than random-model limit spectra. Michaliszyn and Witkowski (2026, arXiv:2610.09758) study satisfiability and a bounded-disagreement finite fragment, not these uniform independent-order probabilities. Diaconis, Evans, and Graham (2013) give an exact distributional correspondence for aligned neighboring pairs in a random permutation and Poisson approximations. Their one-count distribution is an acknowledged antecedent, whereas the joint aligned/reversed collision law and the complete rank-two/rank-three logical readout classification are the objects proved here. This is not a result about arbitrary first-order formulas, and no new claim is made for the classical marginal Poisson approximation.

## Limitations
The exact spectrum is restricted to **ordinary two-variable first-order sentences of quantifier rank at most three** and two independent uniform linear orders observed only through successors. No assertion is made about sentences of higher rank, counting quantifiers, distinguished constants, visible order relations, or dependent/nonuniform orders. The clean-neighborhood argument is asymptotic for each fixed rank, not a finite-size equality. The spectral cardinalities use the classical transcendence of \(e\). Earlier general limit-law theorems may still imply part of the statement; the priority comparison is limited to specifically inspected literature and search results. No independent audit has been performed.

## References
1. A. Jeż, J. Michaliszyn, P. Witkowski, *Finite Satisfiability of Two-Variable Logic with Arbitrarily Many Successors*, arXiv:2610.19943, first posted 2026-10-14, https://arxiv.org/abs/2610.19943.
2. J. Michaliszyn, P. Witkowski, *Two-Variable Logic with Arbitrarily Many Successor Relations*, arXiv:2610.09758, first posted 2026-10-07, https://arxiv.org/abs/2610.09758.
3. P. Diaconis, S. N. Evans, R. Graham, *Unseparated pairs and fixed points in random permutations*, Berkeley Technical Report 822 (2013), https://statistics.berkeley.edu/sites/default/files/tech-reports/unseparated_pairs.pdf.
4. D. Figueira, *Satisfiability for two-variable logic with two successor relations on finite linear orders*, arXiv:1204.2495 (2012), https://arxiv.org/abs/1204.2495.
