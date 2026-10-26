# Sharp observation thresholds for elementary cellular automata on bounded-run shifts

## Finding
For each integer \(k\geq3\), let \(X_k\subset\{0,1\}^{\mathbb Z}\) be the subshift forbidding the word \(1^k\). A centered radius-one binary cellular automaton \(F_r\) has Wolfram code \(r\in\{0,\ldots,255\}\), with output \((F_rx)_i=(r\mathbin{\mathrm{div}}2^{4x_{i-1}+2x_i+x_{i+1}})\bmod2\).

The number of Wolfram codes satisfying \(F_r(X_k)\subseteq X_k\) is 62 when \(k=3\), and 70 for every \(k\geq4\). For \(k=3\), the forbidden neighborhood 111 is unused, so these codes describe 31 distinct restricted maps. For \(k\geq4\), all eight three-bit neighborhoods occur and the 70 codes give 70 distinct maps. **Every surjective such map is a shift**: the three distinct coordinate shifts are represented by codes 170, 204 and 240. For \(k=3\) these shifts have six code representatives, since the unused 111 bit can be changed.

For a preserving code \(r\), let \(d_k(r)=0\) if \(F_r(X_k)=X_k\), and otherwise let \(d_k(r)\) be the least positive \(n\) for which a word of length \(n\) admitted by \(X_k\) does not occur in \(F_r(X_k)\). The maximum of \(d_k(r)\) over nonsurjective preserving codes is exactly

\[
\begin{array}{c|cccccc}
k&3&4&5&6&7&\geq8\\\hline
\max d_k(r)&7&8&5&5&6&6.
\end{array}
\]

The global eight-symbol bound is sharp, attained **only** for \(k=4\) at rules 26 and 82, with respective shortest missing words `10100111` and `11100101`. Thus the required observation length is nonmonotone as the forbidden-run length increases; it peaks at \(k=4\) despite stabilization of the permitted local-rule family. The complete code-by-code classification and shortest witnesses are in `classification.csv`.

## Assumptions and scope
Configurations are bi-infinite, with no boundary conditions; the shift convention is \((\sigma x)_i=x_{i+1}\). A finite word is admitted by \(X_k\) precisely when it contains no \(1^k\); every such word extends bi-infinitely by inserting zeros. Only centered three-site rules are classified. The shortest missing-word length concerns spatial output after one application of \(F_r\), not a temporal trace or an eventual limit set. All parameters \(k\) are integers at least three; a separate argument handles the unbounded tail \(k\geq9\).

## Proof
**1. The preserving local rules.** For a binary input word \(w\) of length \(k+2\), define \(E(w)\subseteq\{0,\ldots,7\}\) to consist of the integers represented by its consecutive three-bit windows. The image of the middle \(k\) sites is \(1^k\) if and only if every bit of the rule indexed by \(E(w)\) equals one. Hence \(F_r\) preserves \(X_k\) precisely if none of the supports \(E(w)\) of admissible \(w\) is contained in the set of one-output neighborhoods of \(r\).

For \(k=4\), exact enumeration of the 64 candidate six-bit inputs (discarding those with 1111) gives the following **complete inclusion-minimal violating supports**:

```
{0}
{1,2,4}
{2,5}
{1,3,4,6}
{3,5,6}
{1,3,4,7}
{1,3,6,7}
{1,4,6,7}
{3,4,6,7}
```

Here 0 denotes 000, 1 denotes 001, and so forth. The nine supports have witnesses for **every** \(k\geq4\): respectively, length-\(k+2\) prefixes of periodic `0`, `001`, `01`, `0011`, `011`, followed by the four words `100`+`1` repeated \(k-1\) times, `00`+`1` repeated \(k-1\) times+`0`, `1` repeated \(k-1\) times+`001`, and `0`+`1` repeated \(k-1\) times+`00`. Each avoids \(1^k\) and uses only triple types from the corresponding support. Therefore a rule violating \(X_4\) violates every \(X_k\) for \(k\geq4\).

Conversely, inspect the four-vertex binary de Bruijn graph whose edges are the one-output triples of any rule preserving \(X_4\). The verifier checks all 70 possibilities: after removing the 111 self-loop, each remaining graph is acyclic. If the 111 loop occurs, every loop-free path through vertex 11, with \(e\) edges and associated input word \(w\), has \(e\leq c(w)\), where \(c(w)\) is the longest consecutive run of ones in \(w\). A path of output ones avoiding the loop therefore has at most three edges. A path using the loop \(L\) times has output length \(e+L\) and its input contains a one-run of length at least \(c(w)+L\), hence of length at least \(e+L\). Such an output cannot contain \(1^k\) when the input is in \(X_k\). This proves that the 70 rules preserve **all** \(X_k\) for \(k\geq4\). Counting the 256 eight-bit rule masks avoiding the nine supports gives 70. For \(k=3\), direct examination of admissible five-bit inputs gives 62 codes (31 distinct maps).

**2. Exact detection automata.** Fix \(3\leq k\leq8\) and a preserving rule. Use the \(2^{k-1}\) possible input words of length \(k-1\) as graph states. An edge appends a bit, except when this would form \(1^k\), and is labeled by the rule applied to the last two bits of the state together with the new bit. The labels of paths are exactly the finite output words of \(F_r(X_k)\): all admissible finite input words can be extended on both sides with zeros.

Determinize this labeled graph by reachable subsets, starting at the full state set. In parallel record \(j\in\{0,\ldots,k-1\}\), the run of terminal ones in the proposed output, omitting a transition to 1 if \(j=k-1\). A candidate word is admitted by \(X_k\) exactly when this latter automaton permits it. Therefore the **first** transition to an empty predecessor subset among admissible words, found by breadth-first search, gives the exact shortest missing-word length. If complete finite-state closure has no such transition, the image language equals that of \(X_k\) and the map is surjective. The code independently enumerates finite input blocks for every output length up to the claimed shortest witness and compares the resulting languages. Its exact distribution of lengths is:

| \(k\) | \(d=0\) | \(d=1\) | \(d=2\) | \(d=3\) | \(d=4\) | \(d=5\) | \(d=6\) | \(d=7\) | \(d=8\) |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 3 | 6 | 2 | 24 | 6 | 8 | 6 | 8 | 2 | 0 |
| 4 | 3 | 1 | 19 | 33 | 6 | 4 | 2 | 0 | 2 |
| 5 | 3 | 1 | 12 | 34 | 18 | 2 | 0 | 0 | 0 |
| 6 | 3 | 1 | 12 | 24 | 24 | 6 | 0 | 0 | 0 |
| 7 | 3 | 1 | 12 | 24 | 19 | 9 | 2 | 0 | 0 |
| 8 | 3 | 1 | 12 | 24 | 19 | 8 | 3 | 0 | 0 |

**3. Infinite tail.** Every input word of length at most eight is admitted by \(X_k\) for \(k\geq9\). Accordingly, every spatial output word of length at most six appears in \(F_r(X_k)\) precisely when it appears in the full-shift image of \(F_r\). Exact enumeration of all 70 preserving rules' full-shift images through length six shows that only rules 170, 204 and 240 contain **every** binary six-word. Each of the other 67 codes omits a word of length at most six. These omissions are admitted by every \(X_k\) for \(k\geq9\). The three surviving rules are shifts and are onto. Their complement's exact shortest missing-word distribution agrees with that for \(k=8\), as separately checked by finite-state closure; hence the last column \(k\geq8\) is uniform. This proves the theorem for infinitely many \(k\), not merely sampled instances.

## Verification
Run `python3 verify.py` from the directory containing `classification.csv`. The verifier uses only the Python standard library. It independently reconstructs the nine inclusion-minimal four-step violation supports; checks the explicit all-\(k\) witness families at test values; checks the acyclicity and loop-run inequality for every preserving rule; exhaustively builds the exact predecessor-subset graphs for \(k=3,4,5,6,7,8\); independently enumerates finite input blocks through each shortest witness; checks the full-shift six-word argument for \(k\geq9\); and compares the regenerated CSV to the embedded one. The analytical de Bruijn proof and explicit template families supply the universal quantifiers, while the code supplies reproducible finite certificates.

## Relationship to prior work
The classical theory of \(S\)-gap shifts supplies the shift-of-finite-type context; after exchanging symbols, the present \(X_k\) is a bounded-gap finite-type example. Baker and Ghenciu (arXiv:1411.7167, first posted 2014-11-26) study entropy, balance and specification for such shifts, but do not give a finite-neighborhood endomorphism census. Dastjerdi and Jangjoo (arXiv:1108.3242) study structural shift properties and sliding block codes, but not the present restricted-rule obstruction profile; their arXiv record warns of a withdrawn flawed theorem, which is not invoked here. Kari and Taati's work on statistical mechanics of surjective cellular automata gives broad pre-injectivity/entropy principles for mixing finite-type shifts, but does not imply the reported code-by-code minimal forbidden lengths without the present exact comparison. No stronger covering theorem was identified among the inspected materials; unindexed enumerations remain a genuine priority risk.

## Limitations
The method proves only the stated radius-one classification and first-step image-obstruction lengths. It does not classify arbitrary-radius endomorphisms, distinguish all proper images up to conjugacy, determine their entropy, or assert that historical literature is exhaustively indexed. The numerical masks and shortest witnesses are exact finite computations replayable with the attached script, not claims about earlier authorship or independent certification.

## References
1. S. Baker and A. E. Ghenciu, *Dynamical properties of S-gap shifts and other shift spaces*, arXiv:1411.7167 (first posted 2014-11-26), https://arxiv.org/abs/1411.7167 .
2. D. Ahmadi Dastjerdi and S. Jangjoo, *Dynamics and Topology of S-gap Shifts*, arXiv:1108.3242 (first posted 2011-08-16), https://arxiv.org/html/1108.3242v4 ; withdrawal notice at the arXiv record; no disputed theorem is used.
3. J. Kari and S. Taati, *Statistical Mechanics of Surjective Cellular Automata*, Journal of Statistical Physics (2015), https://doi.org/10.1007/s10955-015-1281-2 .
4. J. Kopra, *Dynamics of cellular automata on beta-shifts and direct topological factorizations*, arXiv:2001.09699 (2020); relevant to general beta-shift automorphism behavior, not a directly inspected radius-one census.
