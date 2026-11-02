# Seven alternatives are the sharp Copeland-refinement failure for DSR scoring

## Finding

Consider the original 2024 dominating-set-relaxed scoring (DSR-scoring) voting rule of Hou, applied to a **strict tournament** (exactly one winner in each pair, with no ties). Let \(DSR(T)\) be the candidates with maximum DSR score and let \(C(T)\) be the candidates with maximum Copeland score (number of pairwise victories).

**Theorem (sharp first failure and full first-obstruction class).** For every strict tournament \(T\) on \(2\le n\le6\) alternatives,
\[
DSR(T)\subseteq C(T).
\]
At order \(n=7\) this inclusion fails. Of the exactly \(2^{21}=2,097,152\) tournaments on seven labeled alternatives, exactly \(5,040\) fail the inclusion, and they are precisely the relabelings of **one** tournament. Its automorphism group is trivial.

In the explicit witness below, \(DSR(T)=\{5,6\}\), whereas \(C(T)=\{5\}\). This answers negatively the arbitrary-order refinement conjecture appearing in the 2024 source, and locates the sharp finite boundary.

## Assumptions and scope

The alternatives are \(V=\{0,1,\ldots,n-1\}\), and \(a\to b\) means that \(a\) beats \(b\). Let \(U_z=\{u:u\to z\}\) be the predecessors of \(z\), and \(B_z=\{b:z\to b\}\) its successors. The strict-tournament restriction is essential: no pairwise ties are allowed. The DSR rule is exactly the **home-plus-away comparison-score rule** defined by equations (5)–(9) of Hou's 2024 preprint, not a different tournament rule that merely shares the same partition terminology.

For reproducibility, its tournament specialization is defined explicitly here. If \(B_z=\varnothing\), the iteration at \(z\) assigns one point to each \(u\in U_z\). If \(B_z\neq\varnothing\), call \(z\) active precisely when
\[
 \bigl(\forall u\in U_z\;\exists b\in B_z: u\to b\bigr)
 \quad\text{or}\quad
 \bigl(\exists u\in U_z\;\forall b\in B_z: u\to b\bigr).
\]
The first alternative holds vacuously if \(U_z=\varnothing\). An active \(z\) assigns \(|B_z|\) points to \(z\) and \(1+|\{b\in B_z:u\to b\}|\) points to each \(u\in U_z\); every other candidate receives zero from that iteration. An inactive \(z\) contributes no scores. Sum all \(n\) iterations to obtain \(\psi_T(x)\); \(DSR(T)=\operatorname*{argmax}_x\psi_T(x)\). The Copeland score is \(c_T(x)=|\{y:x\to y\}|\).

This definition is exactly the original rule for strict tournaments: the three permitted nontrivial partitions at a fixed \(z\) have conditions \(A_z\succeq B_z\), \(\gamma(A_z,B_z)>0\), or \(\beta(U_z,B_z)>0\), with \(A_z=U_z\cup\{z\}\). Since \(z\) beats all members of \(B_z\), the first condition implies the first disjunct above, the second is precisely that first disjunct, and the third is the second disjunct. For \(B_z=\varnothing\), the single-bottom-block convention gives the stated one-point assignment. A source worked example is reproduced by the checker.

## Proof

**1. Exact witness.** Define the seven-alternative tournament by listing every candidate's outgoing neighbors:

| Candidate | Candidates defeated |
| --- | --- |
| 0 | 3, 4, 6 |
| 1 | 0, 4, 6 |
| 2 | 0, 1 |
| 3 | 1, 2 |
| 4 | 2, 3 |
| 5 | 0, 1, 2, 3, 4 |
| 6 | 2, 3, 4, 5 |

Each unordered pair appears in exactly one row, so this specifies a strict tournament. Its seven iterations are inactive at candidates \(0,1\) and active at \(2,3,4,5,6\). Directly applying the definition produces, in candidate order \(0,1,\ldots,6\),
\[
 (\psi_T(0),\ldots,\psi_T(6))=(6,3,2,4,5,14,14),
 \qquad(c_T(0),\ldots,c_T(6))=(3,3,2,2,2,5,4).
\]
Therefore candidate \(6\) ties for the DSR maximum but not for the Copeland maximum. This alone disproves the general inclusion.

**2. Complete lower-order check.** For each \(n\in\{2,3,4,5,6,7\}\), place the unordered pairs \((i,j)\), \(i<j\), in lexicographic order. An integer \(m\) in \(0\le m<2^{\binom n2}\) specifies the complete labeled tournament by declaring \(i\to j\) when the associated bit of \(m\) equals \(1\), and \(j\to i\) otherwise. This parametrization is bijective, without an isomorphism-filtering assumption. The included standalone C99 source enumerates **every** such integer, computes both score vectors by their defining finite loops, and tests the failure predicate
\[
\exists x\in V:\ \psi_T(x)=\max_{y\in V}\psi_T(y)
\ \land\ c_T(x)<\max_{y\in V}c_T(y).
\]
It returns the exact failure counts
\[
\begin{array}{c|rrrrrr}
n&2&3&4&5&6&7\\ \hline
\text{labeled tournaments}&2&8&64&1024&32768&2097152\\
\text{failures}&0&0&0&0&0&5040
\end{array}.
\]
The enumerator's outer bounds cover every bit string; there are no pruning, random trials, cutoffs or time-limited branches. Every arithmetic operation uses bounded nonnegative integers, with scores at most \(n^2\), so C integer overflow cannot affect these sizes. Thus this is an exhaustive finite verification for the claimed orders, not an inference from samples.

**3. Classification by relabeling.** The checker takes the explicit seven-candidate witness (integer code \(1324\) under the preceding convention) and generates its images under all \(7!=5040\) permutations. Exactly \(5040\) *distinct* bit strings result. It then verifies that every one of the \(5040\) failures from the exhaustive census occurs in this orbit. Consequently the failures comprise a single isomorphism class. Since the orbit has full cardinality \(7!\), its stabilizer—and hence the tournament's automorphism group—is trivial. This proves the classification and completes the theorem.

## Verification

Compile with a conforming C99 compiler, for example:

```sh
cc -O2 -std=c99 -Wall -Wextra -Werror dsr_verify.c -o dsr_verify
./dsr_verify
```

The executable has no external dependencies. It independently checks that its implementation reproduces the original paper's four-candidate Table 7 score vector \((3,4,1,0)\), before the complete tournament census. The verified output is:

```text
orbit_size=5040
n=2 total=2 exceptions=0
n=3 total=8 exceptions=0
n=4 total=64 exceptions=0
n=5 total=1024 exceptions=0
n=6 total=32768 exceptions=0
n=7 total=2097152 exceptions=5040
witness=1324
DSR: 6 3 2 4 5 14 14
Copeland: 3 3 2 2 2 5 4
```

A separate implementation using a matrix-based scoring routine and independently compiled enumeration found the same seven-candidate first witness and \(5040\) failures. The proof's finite scope is fully covered by the exhaustive loops; no conclusion is drawn about detailed failure counts for larger orders.

## Relationship to prior work

Hou's 2024 preprint [1], Section 6.3, Proposition 7, proves \(DSR(T)\subseteq C(T)\) for at most four alternatives, reports that the statement can be checked for five, and conjectures the generalization. The exact seven-alternative counterexample, the exhaustive sharp six-alternative boundary, and the single-isomorphism-class census are not stated in the inspected preprint. The later 2025 journal version [2] repeats the up-to-four guarantee in its publicly accessible abstract. A separate later tournament-solution paper by Hou [3] discusses different placement-indicator scoring; the publicly accessible abstract states non-equality with Copeland in general, but does not establish the present *subset* counterexample or its minimality for the 2024 comparison-score formula. Its full text was not available for detailed verification, leaving a documented bibliographic risk.

Other previously published finite-tournament classifications (e.g., Banks, minimal covering, and uncovered-set comparisons) use different solution correspondences and do not imply the present score-specific classification. An exhaustive census is mathematical evidence of the first failure for this exact rule, not proof of publication priority.

## Limitations

The theorem concerns only strict tournaments, the **2024** DSR home-plus-away scoring definition, and the exact first boundary through seven candidates. It makes no claim that every larger tournament fails, nor any claim about tournaments with ties, strategic voting profiles, or the scoring formula of a later distinct DSR-based tournament solution. Independent audit and replication outside the reported implementations have not been performed. Relevant recent journal full text could not be fully inspected; originality should be reassessed if it becomes available.

## References

1. F. Hou, *A new social welfare function with a number of desirable properties*, arXiv:2403.16373v1, posted 2024-03-25, Sections 3–4 and 6.3, equations (5)–(9), Proposition 7, Conclusion. https://arxiv.org/html/2403.16373
2. F. Hou, *A social welfare function based on dominating set relaxations*, International Journal of General Systems, DOI:10.1080/03081079.2025.2493189, published online 2025-04-21. https://doi.org/10.1080/03081079.2025.2493189
3. F. Hou, *A tournament solution based on dominating-set-relaxed partitions*, Expert Systems with Applications 306 (2026), 130835, DOI:10.1016/j.eswa.2025.130835. https://doi.org/10.1016/j.eswa.2025.130835
