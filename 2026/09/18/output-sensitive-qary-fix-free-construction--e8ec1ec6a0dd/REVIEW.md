# Review: output-sensitive q-ary fix-free construction

**Same-model review: passed. Cross-model review: not yet performed.**

## Correctness

**PASS.**

The middle-layer improvement was checked directly against the exact increment formula of Gao--Shan. If
\[
r_\ell(S)=|\{x\in S:i(x)=\ell\}|,\qquad
c_\ell(S)=|\{x\in S:j(x)=\ell\}|,
\]
then
\[
\delta_S(x)=b_x-r_{j(x)}(S)-c_{i(x)}(S).
\]
Selecting \(x=(i,j)\) therefore decrements exactly the candidates with \(i(\cdot)=j\) and those with \(j(\cdot)=i\). Under \((U_c)\), the latter set contains at most one candidate whenever it can be affected; under \((U_r)\), the symmetric statement holds. Labels outside the intersection of the two index sets cannot trigger the corresponding dynamic update, so the one-sided uniqueness condition is sufficient without any unstated global uniqueness assumption.

A two-level priority structure consequently returns an actual minimum of the current \(\delta_S\) values at every step. Using the numerical word index as the secondary heap key gives deterministic tie-breaking and still satisfies the interpolation theorem.

For the longest layer, the proof was checked in both geometric cases. If \(\lambda_3\ge2\lambda_2\), admissible words are exactly the Cartesian product of an admissible length-\(\lambda_2\) prefix, a free middle word, and an admissible length-\(\lambda_2\) suffix. If \(\lambda_2<\lambda_3<2\lambda_2\), the first and last \(\lambda_2\) symbols overlap in exactly \(\beta=2\lambda_2-\lambda_3\) symbols, so the disjoint union
\[
\bigsqcup_a P_a\times S_a
\]
is a bijection, not merely a counting bound. Hence direct enumeration neither misses nor duplicates admissible words.

Finite verification compares the structured greedy updates with naïve recomputation and compares direct longest-layer generation with exhaustive word enumeration on small binary and ternary examples. These checks are supportive only; the general result is proved algebraically.

## Originality

**PASS, to the best of our knowledge.**

The primary source inspected was Gao--Shan, arXiv:2609.18237. Its Section IV gives the exact greedy increment and one-sided uniqueness hypotheses; Section VI, Remark 30 states the direct implementation cost \(O(N_2^2+N_3\lambda_3)\), obtained by rescanning the remaining packet at every greedy step and scanning all length-\(\lambda_3\) words. The paper does not state a grouped priority implementation or an output-sensitive final-layer enumeration.

Searches around fix-free/bifix construction complexity, priority-queue implementations, output-sensitive construction, the exact source title, and the three-length \(3/4\) theorem did not locate the bound
\[
O(N_2\log N_2+\mu_3\lambda_3)
\]
or the two structural implementation lemmas recorded here. Older literature does contain many constructive fix-free algorithms, so no claim is made that lazy heaps, overlap grouping, or Cartesian-product generation are individually new data-structural ideas.

The closest older theorem is Congero--Zeger, IEEE Transactions on Information Theory 69(3), 1452--1485 (2023), DOI 10.1109/TIT.2022.3218212, for the binary three-length result. Bibliographic and abstract-level information was inspected here, but its full text was not inspected. It is a residual originality risk for related binary implementation ideas, though it cannot literally contain the optimization of Gao--Shan's later q-ary matrix interpolation theorem. The novelty claim is therefore restricted to the stated implementation theorem for the Gao--Shan q-ary construction and its resulting complexity bound.

The source preprint is recent, so an unindexed revision, independent note, or near-simultaneous observation remains a material residual risk.

## Value

**PASS.**

The source construction is deterministic but its stated implementation rescans an \(N_2\)-sized search space up to \(N_2\) times and then scans all \(N_3\) longest words. The new implementation removes both exhaustive factors:
\[
O(N_2^2+N_3\lambda_3)
\quad\longrightarrow\quad
O(N_2\log N_2+\mu_3\lambda_3).
\]
This is a qualitative algorithmic improvement in the natural search-space parameters, and the final stage becomes output-sensitive.

The result does not change the existence theorem, Kraft threshold, or number of supported codeword lengths. Its value is algorithmic rather than combinatorial.

## Verification state

- review_type: `same_model_review`
- independent: `false`
- same_model_review_status: `passed`
- cross_model_review_status: `not_performed`
