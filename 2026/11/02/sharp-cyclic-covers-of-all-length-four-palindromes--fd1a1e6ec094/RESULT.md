# Sharp cyclic covers of all length-four palindromes

## Finding

**Theorem.** Let \(\Sigma\) be a labeled alphabet of size \(q\ge2\). A *cyclic cover* is a nonempty circular word \(W\) in which each word \(abba\), for every ordered pair \((a,b)\in\Sigma^2\), appears as a contiguous length-four factor, with indices read cyclically. Repetitions of factors other than the required palindromes are allowed. The shortest possible length is

\[
L_4(q)=\begin{cases}\dfrac{5q^2+q}{2},&q\text{ odd},\\[3pt]\dfrac{5q^2+2q}{2},&q\text{ even}.\end{cases}
\]

Each shortest cover has a *rigid run signature*: for each symbol \(a\), exactly one maximal constant run has length four; for each ordered pair \(a\ne b\), exactly one maximal run of \(b\) has length two and is flanked immediately on both sides by runs of \(a\); every other maximal run has length one. If \(m_{ab}\) is the number of unordered adjacent transitions \(a\leftrightarrow b\) in the cyclic sequence of run symbols, then every optimum has

\[
m_{ab}=3\quad(a\ne b)\text{ for odd }q;
\]

for even \(q\), exactly the edges of a perfect matching have \(m_{ab}=4\), and all other distinct pairs have \(m_{ab}=3\). Every such perfect-matching profile is attained by an optimum; for odd \(q\) the indicated sole profile is attained. In particular the optimum lengths for \(q=2,3,4,5,6\) are \(12,24,44,65,96\).

## Assumptions and scope

Symbols are distinct labeled letters and the same symbol may appear many times. Circular words are considered up to choice of starting position, but the *length* and run multiplicities do not depend on that choice. A cyclic factor of length four may cross the chosen starting point. No assumption of exact-once coverage is made. The theorem holds for all integers \(q\ge2\); the one-symbol case is deliberately outside its statement. The term *run* means a maximal cyclic block of equal letters. Since every symbol is required, each admissible word has at least two distinct letters, and its cyclic run decomposition is well-defined.

## Proof

**1. Dedicated runs.** Write the runs in cyclic order as \(a_0^{\ell_0},a_1^{\ell_1},\ldots,a_{R-1}^{\ell_{R-1}}\), where consecutive run symbols differ and the last differs from the first. Every constant target \(aaaa\) requires some run of \(a\) to have length at least four. Thus at least \(q\) different runs are long and together contribute an excess of at least \(3q\) over unit-length runs.

If \(a\ne b\), an occurrence of \(abba\) must cross precisely a full run of \(b\) of **exactly length two**, with a run of \(a\) immediately on either side. Neither a longer run nor a shorter run can supply this factor. Distinct ordered pairs \((a,b)\) have distinct dedicated center runs. The \(q(q-1)\) necessary length-two runs are disjoint from the long ones and contribute at least \(q(q-1)\) additional positions over their unit lengths. Hence, for a cover of length \(N\) with \(R\) runs,

\[
N\ge R+q(q-1)+3q.\tag{1}
\]

**2. Skeleton-edge multiplicities.** Ignore the run lengths and retain only their cyclic symbol sequence \(a_0a_1\cdots a_{R-1}\). It is a closed walk on the loopless complete graph with vertex set \(\Sigma\). For each unordered distinct pair \(\{a,b\}\), both patterns \(aba\) and \(bab\) appear as consecutive run symbols, by Step 1.

When \(q\ge3\), the closed walk uses some third symbol. Two traversals of the edge \(\{a,b\}\) are insufficient to exhibit *both* opposing alternating triples: if they are consecutive, they form only one of the two triples; if they are separated, they form neither. The only apparent exception would be an entire two-run cyclic walk, excluded because all \(q\) symbols occur. Thus

\[
m_{ab}\ge3\quad\text{for all }a\ne b.\tag{2}
\]

For odd \(q\), summing (2) gives \(R=\sum_{a<b}m_{ab}\ge3\binom q2\). For even \(q\), the degree of each vertex in the skeleton multigraph is even because the walk is closed. The baseline degree \(3(q-1)\) is odd, so each of the \(q\) vertices needs at least one extra incident edge beyond (2). These additional traversals number at least \(q/2\), giving

\[
R\ge3\binom q2+\frac q2\quad(q\text{ even}).\tag{3}
\]

For \(q=2\), the skeleton alternates between the two symbols. It must have at least four runs because it contains two distinct length-two center runs and two distinct length-four runs. Thus \(R\ge4=3\binom22+1\), exactly the even-case bound. Substitution into (1) yields the stated lower bounds.

**3. Construction achieving equality.** When \(q\) is odd, take an Eulerian circuit through all edges of the loopless complete graph \(K_q\). When \(q\) is even, add one parallel copy of each edge of an arbitrary perfect matching and take an Eulerian circuit of that connected even-degree multigraph. These Eulerian circuits exist because every vertex has even degree.

Traverse the circuit cyclically. On the first use of each unordered edge \(\{u,v\}\), replace its step \(u\to v\) by the three-step alternating segment \(u\to v\to u\to v\). If a matching edge is traversed again, keep its single step. This produces a proper cyclic run-symbol skeleton with

\[
R=3\binom q2+\mathbf1_{2\mid q}\,q/2.
\]

The two internal vertices inserted in the first zigzag over \(\{u,v\}\) are respectively \(v\) flanked by \(u\), and \(u\) flanked by \(v\). Assign run length two to precisely these inserted vertices; this realizes each target \(abba\) with \(a\ne b\) exactly at its dedicated center. Every alphabet symbol occurs at an original Euler-circuit vertex, so choose one original occurrence per symbol and assign it run length four; assign every remaining original occurrence run length one. This supplies the constant targets \(aaaa\). The resulting word has exactly

\[
R+q(q-1)+3q=L_4(q)
\]

symbols and is therefore shortest.

**4. Equality rigidity.** In a shortest word, every inequality used in (1)–(3) is equality. Hence no additional positive run excess is possible: the necessary dedicated center runs have length exactly two, the \(q\) designated long runs have length exactly four, and all other runs have length one. Also every pair has its minimal transition multiplicity three when \(q\) is odd. When \(q\) is even, each vertex acquires exactly one extra degree in the skeleton, so the extra edges necessarily form a perfect matching. The construction works for any chosen perfect matching, proving realization of all stated profiles. The exceptional \(q=2\) case has four alternating runs and the same rigid run signature. \(\square\)

## Verification

The accompanying standalone standard-library Python program `verify.py` constructs the specified covers and checks **all** length-four palindromes for every alphabet size \(2\le q\le50\), all stated lengths, and each stated run-length count. It separately performs a shortest-path breadth-first search through the entire finite cyclic-factor state space for \(q=2\) and \(q=3\), obtaining the exact minima \(12\) and \(24\). These finite checks corroborate the constructive formula but are **not** substituted for the all-alphabet proof above. Reproduce with `python3 verify.py`.

For instance, the binary word `000011001111` is a length-12 cover, and `000022002222112211110011` is a length-24 ternary cover (both understood cyclically).

## Relationship to prior work

Universal-cycle literature develops Eulerian methods for exact-once or restricted-factor coverage. Gardner and Godbole (2017) study Eulerian constructions for selected restricted word families; Chen, Kitaev and Sun (2019) address probability and obstructions for *exact-once* universal cycles and words after deletion of target factors. The directly inspected statements do not give the *at-least-once* minimum cyclic cover of the \(q^2\) length-four palindromes, nor its forced run signature.

The OEIS entry A330022, originally recorded in 2019, lists the shortest **linear binary** superstring containing all length-four palindromes as having length 12. The present binary cyclic minimum agrees; that one numerical case is not claimed as new. A prior length-three cyclic-palindrome cover classification has the same underlying three-transition-per-unordered-pair and parity-matching obstruction. The new question requires and proves the exact-length-two internal runs and the length-four constant runs, yielding a distinct length-four optimal-word rigidity result, while reusing the natural Eulerian zigzag construction.

## Limitations

The result concerns full factor coverage of *ordinary* length-four palindromes, not reverse-complement palindromes, exact-once universal cycles, linear minimum lengths for \(q>2\), arbitrary palindromic lengths, or counts of labeled minimum words. The run signature and adjacency profiles are necessary for every optimum, and each stated pair profile occurs; this theorem does not enumerate every distinct optimum. Related unindexed shortest-superstring or graph-postman results could independently imply parts of the formula. Independent scientific audit has not been performed.

## References

- K. B. Gardner and A. P. Godbole, *Universal Cycles of Restricted Words*, arXiv:1711.07029 (first submitted 19 November 2017), https://arxiv.org/abs/1711.07029.
- H. Z. Q. Chen, S. Kitaev and B. Y. Sun, *On the probability of existence of a universal cycle or a universal word for a set of words*, arXiv:1908.01116 (first submitted 3 August 2019), https://arxiv.org/abs/1908.01116.
- OEIS A330022, *Length of shortest binary string containing all palindromes of length n as substrings*, authored 27 November 2019, https://oeis.org/A330022.
