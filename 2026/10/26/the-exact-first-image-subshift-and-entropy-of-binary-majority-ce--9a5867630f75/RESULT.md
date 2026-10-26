# The exact first-image subshift and entropy of binary majority cellular automaton

## Finding

Let \(\Phi:\{0,1\}^{\mathbb Z}\to\{0,1\}^{\mathbb Z}\) be the three-neighbor majority cellular automaton
\[
(\Phi x)_i=\mathbf 1\{x_{i-1}+x_i+x_{i+1}\ge 2\}.
\]
Its **one-step spatial image** \(Y=\Phi(\{0,1\}^{\mathbb Z})\), equipped with the spatial shift, is exactly the shift of finite type avoiding the following six binary words:

```text
01001  01101  10010  10110  0100010  1011101
```

These six words are **all** the minimal forbidden words of \(Y\). In particular, a window of length seven suffices to recognize its language, and no window of length at most six does.

For \(n\ge0\), let \(a_n\) be the number of length-\(n\) spatial words occurring in \(Y\), with \(a_0=1\). Then the complete length distribution is
\[
\sum_{n\ge0}a_n z^n
 =\frac{1+z^3+2z^4-z^5}{1-2z+z^3-z^5}.
\]
Thus \(a_0,\ldots,a_5=(1,2,4,8,16,28)\), and
\[
a_{n+5}=2a_{n+4}-a_{n+2}+a_n\qquad(n\ge1).
\]
The spatial topological entropy of the **image shift** is
\[
h_{\rm top}(Y,\sigma)=\log\lambda=0.579193702797223\ldots,
\quad \lambda=1.78459893336865\ldots,
\]
where \(\lambda\) is the unique real root larger than \(1\) of
\[
\lambda^5-2\lambda^4+\lambda^2-1=0.
\]
The entropy is in natural logarithm units; it equals approximately \(0.83559988274\) bits per spatial symbol.

## Assumptions and scope

The input consists of **all** bilateral binary configurations with no probabilistic or boundary restriction. The map is applied **exactly once**, not iterated indefinitely. The output shift \(Y\) is compact and spatially shift-invariant. The enumeration counts the allowed spatial blocks in \(Y\), not the number of preimages of a block, not the entropy of the cellular automaton as a time-evolution map, and not the entropy of its eventual attractor.

## Proof

**1. Exact labeled two-bit automaton.** Represent the possible two-bit states \(00,01,10,11\) by masks \(1,2,4,8\). A nonempty subset of pair states is represented by the sum of its masks; mask \(15\) is the full starting set. If \(q\) is such a subset, let \(\delta(q,b)\) be the subset of terminal pair states obtained by appending a binary input bit to a pair in \(q\) whose three-bit majority is \(b\). The empty subset is state \(0\). All reachable states and their transitions are:

| State \(q\) | \(\delta(q,0)\) | \(\delta(q,1)\) |
|---:|---:|---:|
| 0 | 0 | 0 |
| 1 | 3 | 0 |
| 2 | 4 | 8 |
| 3 | 7 | 8 |
| 4 | 1 | 2 |
| 5 | 3 | 2 |
| 7 | 7 | 10 |
| 8 | 0 | 12 |
| 10 | 4 | 12 |
| 12 | 1 | 14 |
| 14 | 5 | 14 |
| 15 | 7 | 14 |

Every entry follows directly from the eight three-bit majority values. A finite output word \(w\) occurs if and only if \(\delta(15,w)\ne0\). Indeed, an accepting automaton path is precisely a finite input word with those output labels, and any finite input word extends bilaterally.

**2. A six-letter state-reset lemma.** Let \(Q\) be the eleven nonzero states in the table. Start with all \(110\) ordered pairs \((q,r)\) of distinct states of \(Q\). For a pair, simultaneously follow the same label \(b\in\{0,1\}\); discard a transition if either destination is empty or the destinations agree. The numbers of distinct surviving ordered pairs after \(j=0,1,\ldots,6\) steps are, respectively,
\[
110,\ 40,\ 24,\ 12,\ 8,\ 4,\ 0.
\]
This is an exhaustive finite computation from the displayed twelve-row table, using the two-line set update in `verify.py`. Consequently, after any six-letter output word, **all nonempty image states coincide**, regardless of the nonempty starting state in \(Q\).

For every accepted word \(w\) of length at least six, the automaton state after reading \(w\) equals the state obtained by reading its final six letters from state \(15\): both computations are nonempty, and the reset lemma forces equality. It follows inductively that an arbitrary output word is accepted if and only if every one of its contiguous length-seven factors is accepted, provided its length is at least seven.

**3. All minimal forbidden words.** Directly evaluate the displayed transition table on every binary word of length at most seven. All words of lengths at most four occur; at length five the four minimal exclusions are `01001`, `01101`, `10010`, `10110`; there are no new minimal exclusions at length six; at length seven the two new minimal exclusions are `0100010` and `1011101`. The six-letter reset lemma excludes every additional minimal forbidden word of length at least eight. Hence the six-word list is exact at **all** lengths. The two length-seven words have admissible proper subwords, so no forbidden presentation with maximum word length six is possible.

**4. Rational generating function.** List the eleven nonempty states in increasing order and let \(M\) be the corresponding adjacency-count matrix: \(M_{q,r}\) is the number of output labels leading from \(q\) to \(r\), with transitions to state \(0\) omitted. Write \(\mathbf1\) for the column of eleven ones and \(e_{15}\) for the coordinate vector of starting state \(15\). Then
\[
a_n=e_{15}^{\mathsf T}M^n\mathbf1.
\]
Exact multiplication of this finite integer matrix gives the identity
\[
\bigl(M^5-2M^4+M^2-I\bigr)\mathbf1=-e_{15}.
\]
No nonempty transition ends at state \(15\), hence \(e_{15}^{\mathsf T}M^n e_{15}=0\) for \(n\ge1\). Multiplying the matrix identity by \(e_{15}^{\mathsf T}M^n\) proves the displayed order-five recurrence for every \(n\ge1\). For \(n=0\), the same expression equals \(-1\). The first six block counts then yield exactly the rational generating function in the finding (including the \(n=0\) exception).

**5. Entropy.** The characteristic polynomial of the explicit \(11\)-state matrix factors as
\[
\det(tI-M)=t(t^5+t^2-1)(t^5-2t^4+t^2-1).
\]
The Perron spectral radius is at least \(1\) because the table contains nonempty loops. The first quintic has no real root at or above \(1\). The second has precisely one real root larger than \(1\): after setting \(t=1+u\), its polynomial is \(u^5+3u^4+2u^3-u^2-u-1\), with exactly one positive root by Descartes' rule and opposite endpoint signs. Thus the Perron radius is \(\lambda\). Every nonempty state is accessible from \(15\) and is an accepting state, so the growth rate of \(e_{15}^{\mathsf T}M^n\mathbf1\) equals the logarithm of the Perron radius. The standard language-growth definition of subshift entropy gives \(h_{\rm top}=\log\lambda\).

## Verification

Run `python3 verify.py` with Python 3 (standard library only). It independently reconstructs the majority transitions, the twelve reachable deterministic states, the six-step ordered-pair reset table, all minimal forbidden words through seven symbols, and block languages through thirteen symbols from two separate methods. It verifies the unrestricted recurrence's finite integer-matrix identity, the exact characteristic-polynomial factorization, and numerical root brackets. Expected terminal line begins with `VERIFY_OK` and reports \(\lambda=1.78459893336865\ldots\). The proof's infinite-length deductions use the reset lemma and matrix identity; finite enumeration alone would not establish them.

## Relationship to prior work

Kůrka's *Topological Dynamics of Cellular Automata* (2009), especially its majority-rule example and the section on attractors, describes the rule's **maximal long-time attractor**, signal subshifts, and column subshifts. The attractor is an intersection of successive images, not the first spatial image analyzed here; its forbidding conditions and zero temporal/column entropy therefore do not imply the six-word first-image presentation or the positive **spatial** image entropy. Kari and Taati's *Statistical Mechanics of Surjective Cellular Automata* (public preprint 10 November 2013) establishes the entropy and Garden-of-Eden framework and inequalities for factor images, but gives no evaluated rule-232 first-image polynomial. The rule table itself is standard. The contribution here is the exact first-image forbidden-language classification and its evaluated block-growth invariant, not the underlying majority rule or general finite-state methodology.

## Limitations

No claim is made about the entropy of iterating the cellular automaton in time, its limit set, stationary Bernoulli-image entropy rate, or arbitrary neighborhoods/alphabets. General finite-state factor constructions were already available; historical priority of this **specific evaluated** classification has not been independently certified. A prior explicit rule-232 one-step image computation in an unindexed automata catalogue remains possible.

## References

1. P. Kůrka, *Topological Dynamics of Cellular Automata*, in *Encyclopedia of Complexity and Systems Science* (2009), DOI `10.1007/978-0-387-30440-3_556`. Accessible author's manuscript: `https://www.cts.cuni.cz/~kurka/cantor.pdf`, example 7, PDF pages 18–19.
2. J. Kari and S. Taati, *Statistical Mechanics of Surjective Cellular Automata*, arXiv:`1311.2319` (first posted 2013-11-10), later *Journal of Statistical Physics* 160 (2015), DOI `10.1007/s10955-015-1281-2`, especially §3.1.
3. Wolfram Atlas, *Elementary Cellular Automaton Rule 232*, `https://atlas.wolfram.com/01/01/232/01_01_1_232.html`, for the standard local-rule identification.
