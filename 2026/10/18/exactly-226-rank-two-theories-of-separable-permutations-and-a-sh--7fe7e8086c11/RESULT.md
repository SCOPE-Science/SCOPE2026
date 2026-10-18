# Exactly 226 rank-two theories of separable permutations and a sharp ten-point bound

## Finding

Let a finite, nonempty permutation be interpreted as a structure with **two strict linear orders**, the position order and the value order. Among all separable permutations, there are **exactly 226** different complete first-order sentence theories of quantifier rank at most two. Every one of these theories has a separable representative of length at most **10**. The bound is sharp: exactly two theories have shortest separable representatives of length 10.

The exact distribution of the **minimum representative length** over these 226 theories is

\[
\begin{array}{c|rrrrrrrrrr}
\text{minimum length}&1&2&3&4&5&6&7&8&9&10\\\hline
\text{number of theories}&1&2&6&19&46&60&50&29&11&2.
\end{array}
\]

The two length-ten witness permutations, in one-line notation, are \(8,9,10,5,6,7,4,1,2,3\) and \(3,2,1,6,5,4,7,10,9,8\).

The rank-two theory of the nonseparable five-point permutation \(2,5,3,1,4\) is **not** realized by any separable permutation. This exclusion follows from the same complete signature classification; it is not a claim that rank-two logic defines separability in general.

## Assumptions and scope

A permutation \(\pi\) of positive length \(n\) is represented on \(\{1,\ldots,n\}\) by the relations \(i<_{P}j\) precisely when \(i<j\), and \(i<_{V}j\) precisely when \(\pi(i)<\pi(j)\). Equality is the usual logical equality; no successor predicates, counting quantifiers, unary colours, constants, or additional relations are present. Quantifier rank means nesting depth of ordinary first-order quantifiers, and the equivalence relation concerns all sentences of rank at most two.

A permutation is **separable** when it is built from the one-element permutation by finitely many direct sums and skew sums. Equivalently, separable permutations avoid the patterns \(2413\) and \(3142\). The empty permutation is excluded. A *representative* means another separable permutation with the same complete rank-two sentence theory, not necessarily an isomorphic structure.

For each position \(i\), let \(q_{\pi}(i)\) be a four-bit mask whose bits respectively indicate the existence of a point to its right and above it, right and below it, left and above it, or left and below it. These quadrants are strict in both orders, and the mask is an integer in \(\{0,\ldots,15\}\). Let

\[
\Sigma(\pi)=\{q_{\pi}(i):1\leq i\leq n\}\subseteq\{0,\ldots,15\}.
\]

The 16-bit machine encoding of the signature is \(s(\pi)=\sum_{m\in\Sigma(\pi)}2^m\). This is an encoding, not an additional mathematical assumption.

## Proof

**Rank-two invariant.** For a chosen point \(x\), every quantifier-free formula in two variables \(x,y\) is determined by whether \(x=y\), and otherwise by which one of the four strict quadrants contains \(y\). Consequently, a formula with one free variable and quantifier rank at most one is determined by the mask \(q_{\pi}(x)\). A sentence with quantifier rank at most two can test only which of these pointed rank-one types occur. Conversely, each mask is definable by a conjunction of four existential or negated existential quadrant tests, and the set of realized masks is definable by rank-two sentences. Thus, for all finite nonempty permutations,

\[
\pi\equiv_{2}\rho\quad\Longleftrightarrow\quad\Sigma(\pi)=\Sigma(\rho).
\]

The same equivalence follows directly from the two-move Ehrenfeucht–Fraïssé game: the first move selects a point, and the second tests availability of each quadrant relative to it. This proves both directions without any finite-size cutoff.

**Composition.** Write \(U_j(A)=\{m\mathbin{\mathrm{OR}}2^j:m\in A\}\), where \(\mathrm{OR}\) is bitwise union and the quadrant bits \(j=0,1,2,3\) are, in order, right-above, right-below, left-above, left-below. Every point in the first block of a direct sum acquires a right-above witness and every point in the second block acquires a left-below witness. For a skew sum these are respectively right-below and left-above. Hence

\[
\begin{aligned}
\Sigma(\alpha\oplus\beta)&=U_0(\Sigma(\alpha))\cup U_3(\Sigma(\beta)),\\
\Sigma(\alpha\ominus\beta)&=U_1(\Sigma(\alpha))\cup U_2(\Sigma(\beta)).
\end{aligned}
\]

These identities hold for every nonempty pair of permutations, not only for separable permutations. By the generating definition of separability, the set of signatures realized by separable permutations is **exactly** the smallest set containing the singleton signature \(\{0\}\) and closed under these two binary operations.

**Exact finite closure and optimality certificate.** The accompanying file `permutation_rank2_certificate.json` lists 226 different reachable signatures, each with an explicit separable derivation, an actual permutation witness and its claimed minimum length. The accompanying verifier checks each witness directly from all ordered point pairs, checks every listed derivation, and checks the following two universally quantified finite facts for **every ordered pair** of listed states and **both** composition operations: the resulting state is listed, and its recorded minimum length is at most the sum of the two operand lengths. There are \(226^2\) ordered pairs and two operators.

Reachability of each listed state, closure of the complete list, and the generating definition show that the list is precisely the set of all separable signatures, not a bounded-length sample. The displayed inequality, initialized by minimum length one for the singleton, proves inductively that any separable expression realizing a state has length at least the recorded value. The explicit witness for each state has exactly that value, proving equality. The verifier therefore establishes the exact count, the full histogram, and sharpness at length ten. A separate enumeration of every separable permutation through length ten, using permutations rather than state transitions, reproduces every minimum and the counts of separable permutations at each length.

**A nonseparable rank-two signature.** For \(\pi=(2,5,3,1,4)\), direct pair comparison gives the machine signature \(s(\pi)=37928\). The same finite closure certificate checks that this integer is absent from the exhaustive 226-state set. Therefore no separable permutation is rank-two equivalent to \(\pi\). The nonseparable four-point forbidden patterns \(2413\) and \(3142\) both have signature \(5160\), which occurs among separable signatures; thus the five-point example is the first possible size of this obstruction.

## Verification

Run `python3 verify_permutation_rank2.py` in the directory containing `permutation_rank2_certificate.json`. Only Python's standard library is required. The checker verifies all 226 witnesses and their decomposition trees; all \(226^2\) ordered state pairs under both operations; the exact minimum-length inequalities; the two extremal signatures; and the missing five-point signature. It also independently generates every separable permutation of lengths 1 through 10, computing the quadrant masks from the permutations themselves. The enumerated totals for lengths 1 through 10 are

\[
1,\ 2,\ 6,\ 22,\ 90,\ 394,\ 1806,\ 8558,\ 41586,\ 206098.
\]

The complete checker output is embedded in `verification_output.txt`. The proof of the all-size statement depends on verified closure of the finite state set, **not** on extrapolation from this bounded enumeration.

## Relationship to prior work

Albert, Atkinson and Vatter (arXiv:1007.1014, first public version July 6, 2010, especially Propositions 1.1–1.4) establish the direct/skew decomposition framework and the large-Schröder enumeration of separable permutations. The present theorem uses that framework but counts **rank-two logical equivalence classes**, not permutations or pattern classes. Its 226-state invariant and optimal representative bound are not numerical consequences of the Schröder counts alone.

Albert, Bouvel and Féray (arXiv:1808.05459, 2018) describe permutations as structures with two linear orders and analyze Ehrenfeucht–Fraïssé games and first-order expressibility in that language. Their general logical framework explains the relevance of bounded-depth equivalence, but the exact 226-state separable spectrum, its minimum-length histogram, and the five-point obstruction were not found in the portions and searches of the full primary text inspected. Earlier unindexed enumerations or implications from stronger results remain a priority risk.

## Limitations

The 226 count and length-ten bound are for **nonempty separable permutations** and ordinary first-order rank-two sentences in the exact two-order signature specified above. They are not asserted for all permutations, for the language of permutation-as-bijection, for higher quantifier rank, or for logic with counting or successor. This result does not give a complete classification of all unrestricted-permutation rank-two signatures; only one concrete signature outside the separable class is exhibited. The finite certificate has been checked computationally and by its mathematical invariants, but no independent external audit or priority certification has been performed.

## References

1. M. H. Albert, M. D. Atkinson, V. Vatter, *Subclasses of the separable permutations*, first public arXiv version July 6, 2010, arXiv:1007.1014; published in *Bulletin of the London Mathematical Society* 43 (2011), 859–870. https://arxiv.org/abs/1007.1014
2. M. Albert, M. Bouvel, V. Féray, *Two first-order logics of permutations*, first public arXiv version August 16, 2018, arXiv:1808.05459; *Journal of Combinatorial Theory, Series A* 171 (2020), 105158. https://arxiv.org/abs/1808.05459
