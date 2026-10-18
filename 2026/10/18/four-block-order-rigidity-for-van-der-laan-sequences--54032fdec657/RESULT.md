# Four-block order rigidity for Van der Laan sequences

## Finding

For a sequence \(a_1,a_2,\ldots\) of nonnegative integers, call it a **Van der Laan sequence** when, for every integer \(n\ge1\), the largest of \(a_n,a_{n+1},a_{n+2},a_{n+3}\) equals the sum of its two smallest entries, counting repeated entries with multiplicity.

Fix a permutation \(\pi\) of \((1,2,3,4)\). Call the sequence **weakly four-block \(\pi\)-ordered** if each block \(B_k=(a_{4k+1},a_{4k+2},a_{4k+3},a_{4k+4})\) satisfies
\[
\pi(i)<\pi(j)\Longrightarrow a_{4k+i}\le a_{4k+j}\qquad(1\le i,j\le4),
\]
and every entry of \(B_k\) is at most every entry of \(B_{k+1}\), for all \(k\ge0\). Ties are permitted.

**Theorem (complete four-block classification).** If \(\pi\ne(1,2,3,4)\), the identically zero sequence is the only nonnegative integer Van der Laan sequence that is weakly four-block \(\pi\)-ordered. If \(\pi=(1,2,3,4)\), all such sequences, and only those sequences, arise from integer triples
\[
0\le u\le v\le w\le u+v,
\]
by setting \(a_1=u,\ a_2=v,\ a_3=w\) and \(a_n=a_{n-2}+a_{n-3}\) for every \(n\ge4\).

Thus the nonmonotone permutation patterns that occur for three-term blocks in the published classification disappear completely at block length four.

## Assumptions and scope

All terms are nonnegative integers and the condition must hold on **every** consecutive four-term window, not merely on windows aligned with block boundaries. Block ordering is weak, including possible ties. The permutation \(\pi\) is fixed for every block. The conclusion covers every one of the \(24\) permutations and all infinite sequences satisfying these hypotheses; it makes no claim for changing permutations, other block lengths, or sequences lacking inter-block ordering.

## Proof

**1. A two-block inequality.** Fix a nonidentity permutation \(\pi\) and write the first two blocks as \((x_0,x_1,x_2,x_3)\) and \((x_4,x_5,x_6,x_7)\). We construct five linear forms \(E_s\), for \(0\le s\le4\), and fifteen linear forms \(I_j\), for \(0\le j\le14\). All forms are explicitly determined from \(\pi\):

* To define \(E_s\), order the four indices \(s,s+1,s+2,s+3\) by the pair \((\lfloor i/4\rfloor,\pi(1+(i\bmod4)))\), obtaining \(j_1,j_2,j_3,j_4\), and set \(E_s=x_{j_4}-x_{j_1}-x_{j_2}\).
* For each of the two blocks, order its four positions by ascending \(\pi\)-rank. Define three consecutive-rank differences \(\text{lower}-\text{higher}\), in block order. These are \(I_0,\ldots,I_5\).
* Let \(I_6\) be the first block's rank-four entry minus the second block's rank-one entry. Set \(I_{7+i}=-x_i\), for \(0\le i\le7\).

By the hypotheses, \(E_s=0\) for all five windows and \(I_j\le0\) for all fifteen inequalities. The use of ranked positions remains valid with ties because a tied value can occupy either of its tied ranks without changing the minimum or maximum.

For **each** of the \(23\) nonidentity permutations, the attached file `certificates.json` gives nonnegative rational numbers \(\lambda_0,\ldots,\lambda_{14}\) and arbitrary rational numbers \(\mu_0,\ldots,\mu_4\) such that the following identity holds **coefficientwise**, as a linear form in eight unrestricted real variables:
\[
\boxed{\ x_0+x_1+x_2+x_3
=\sum_{j=0}^{14}\lambda_j I_j+\sum_{s=0}^{4}\mu_s E_s.\ }
\]
Only nonzero coefficients are listed. Their indices are zero-based, and an integer or reduced rational string is interpreted exactly. For example, the row for \(\pi=(1,2,4,3)\) is
\[
x_0+x_1+x_2+x_3=I_2-E_0-3E_2+3E_3-3E_4.
\]
The standalone standard-library program `verify.py` reconstructs the fifteen inequalities and five equalities directly from each permutation, exhausts all nonidentity permutations, and checks every displayed linear identity using exact rational arithmetic. Hence the right side is nonpositive, so \(x_0+x_1+x_2+x_3\le0\). Since these entries are nonnegative, the first block is zero.

**2. Propagation of zero.** If four consecutive nonnegative terms are zero, the Van der Laan condition on the next window, comprising three zeros and one further term, forces that further term to be zero. Induction proves \(a_n=0\) for every \(n\ge1\).

**3. The identity permutation.** For \(\pi=(1,2,3,4)\), the block conditions say precisely that \((a_n)\) is nondecreasing. Each consecutive four-term window then has its first two terms as the two smallest and its fourth as the largest. Thus the Van der Laan equation is equivalent to \(a_{n+3}=a_n+a_{n+1}\), or \(a_n=a_{n-2}+a_{n-3}\) for \(n\ge4\). Writing the initial terms as \(u,v,w\), monotonicity first gives \(0\le u\le v\le w\le u+v\).

Conversely, take any such triple and generate the recurrence. The next term \(a_4=u+v\) is at least \(w\); also \(a_5=v+w\ge a_4\) and \(a_6=w+a_4\ge a_5\). For \(n\ge6\), the difference \(a_{n+1}-a_n=a_{n-1}-a_{n-3}\ge0\) follows inductively. Thus the sequence remains nondecreasing, and each four-term window satisfies the required equation. This proves both directions. \(\square\)

## Verification

Extract the two accompanying standalone files `certificates.json` and `verify.py` in the same directory and run `python3 verify.py`. An actual execution returned `EXACT_CERTIFICATES_OK=23; INDEPENDENT_CONSTRUCTIONS_OK=50`. The first check verifies all \(23\) unrestricted linear-form identities with rational arithmetic and proves the required finite case disjunction; the second directly tests \(50\) distinct allowed initial triples for \(100\) terms each. Unlike finite simulation of a sequence, the certificate identities are a complete finite proof of the nonidentity branch for **all** nonnegative integer sequences.

## Relationship to prior work

David Nacin, *Van der Laan Sequences and a Conjecture on Padovan Numbers*, Journal of Integer Sequences 26 (2023), Article 23.1.2, develops the same four-consecutive-term condition. Its Proposition 3 classifies globally nondecreasing sequences; Propositions 5–7 and the concluding paragraph classify fixed permutation-ordered blocks of sizes at most three, with nonzero nonmonotone three-block examples. The present result instead determines the **next block size, four**, including all \(24\) permutations, and establishes that no nonidentity pattern persists. It does not simply assert an instance of the earlier increasing-sequence theorem: the exclusion of all other rank patterns is the new assertion.

OEIS A000931 identifies the Padovan sequence and records the four-consecutive-term property and examples of other sequences with this property. Those examples do not imply the present uniform fixed four-block ordering dichotomy. Searching for equivalent formulations in the accessible published literature and mathematical-result index located no covering statement, but this does not establish exhaustive uniqueness.

## Limitations

The classification assumes the same weak rank ordering in **every** block and complete ordering between consecutive blocks. It does not classify arbitrary Van der Laan sequences, variable block permutations, or block lengths greater than four. The proof of the nonidentity branch is a finite, exactly checkable set of algebraic certificates rather than a case-free inequality. No independent mathematical audit or external certification has been performed.

## References

1. D. Nacin, "Van der Laan Sequences and a Conjecture on Padovan Numbers," *Journal of Integer Sequences* **26** (2023), Article 23.1.2, https://cs.uwaterloo.ca/journals/JIS/VOL26/Nacin/nacin5.pdf . First publicly posted by the journal December 30, 2022 (per article abstract page).
2. OEIS Foundation, A000931, "Padovan sequence," https://oeis.org/A000931 . Relevant comments describe the four-term property and counterexamples to an early conjecture.
