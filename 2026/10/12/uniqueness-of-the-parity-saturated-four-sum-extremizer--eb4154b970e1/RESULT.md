# Uniqueness of the parity-saturated four-sum extremizer
## Finding
For every integer \(n\ge 6\) and every three-element set \(E\subseteq\{2,4,\ldots,2n\}\), put
\[
A_E=\{1,3,\ldots,2n-1\}\cup E.
\]
Then \(A_E\) contains the six pairwise sums of four distinct positive integers if and only if \(E\neq\{2,2n-2,2n\}\). Equivalently, the unique three-even augmentation of the complete odd set that remains witness-free is
\[
E_0=\{2,2n-2,2n\}.
\]

This is a rigidity statement for the parity-saturated extremal class at the sharp value \(h_4(n)=4\): every set in this class has \(n+3\) elements, exactly the cardinality used by the sharp lower bound.

## Assumptions and scope
Throughout, \(n\) is an integer with \(n\ge6\), and \(E\) is a three-element subset of the even integers in \(\{1,\ldots,2n\}\). A *witness* means four distinct positive integers \(b_1,b_2,b_3,b_4\) such that all six sums \(b_i+b_j\), for \(i<j\), lie in \(A_E\).

The statement classifies only the natural parity-saturated extremal class containing all \(n\) odd integers and three evens. It does not classify all witness-free subsets of \(\{1,\ldots,2n\}\) of cardinality \(n+3\).

The primary classification is MSC2020 \(11B13\) (additive bases, including sumsets), matching the additive-set extremal problem.

## Proof
Assume first that \(E\) contains an even integer \(a\) with
\[
6\le a\le2n-4.
\]
We construct a witness directly.

If \(a\le n+1\), take
\[
(b_1,b_2,b_3,b_4)=(1,2,a-2,a-1).
\]
These are four distinct positive integers because \(a\ge6\). Their six pairwise sums are
\[
3,\quad a-1,\quad a,\quad a,\quad a+1,\quad 2a-3.
\]
Every displayed number except \(a\) is odd, and the inequalities \(3\le2a-3\le2n-1\) show that those odd sums belong to the complete odd part of \(A_E\). The two occurrences of \(a\) belong to \(E\).

If \(a\ge n+2\), take
\[
(b_1,b_2,b_3,b_4)=(a-n,n,a-n+1,n-1).
\]
The assumptions \(n+2\le a\le2n-4\) make these four positive and distinct. Their six pairwise sums are
\[
a,\quad 2a-2n+1,\quad a-1,\quad a+1,\quad 2n-1,\quad a.
\]
Again, every sum other than \(a\) is odd and lies in \(\{1,3,\ldots,2n-1\}\). Hence any witness-free \(E\) must avoid the whole middle interval \(\{6,8,\ldots,2n-4\}\), so necessarily
\[
E\subseteq\{2,4,2n-2,2n\}.
\]
Since \(E\) has three elements, only four boundary triples remain.

Three of them have explicit witnesses. For
\[
E=\{4,2n-2,2n\}\quad\text{or}\quad E=\{2,4,2n-2\},
\]
use
\[
(b_1,b_2,b_3,b_4)=(1,2,3,2n-4).
\]
The six sums are \(3,4,2n-3,5,2n-2,2n-1\), all of which lie in \(A_E\). For
\[
E=\{2,4,2n\},
\]
use
\[
(b_1,b_2,b_3,b_4)=(1,3,4,2n-4),
\]
whose sums are \(4,5,2n-3,7,2n-1,2n\). The assumption \(n\ge6\) guarantees distinctness in both constructions.

It remains to prove that \(E_0=\{2,2n-2,2n\}\) is witness-free. Suppose a witness existed. If three of the \(b_i\) had the same parity, their three mutual sums would be three distinct even integers. None can equal \(2\), while \(A_{E_0}\) has only the other two even values \(2n-2\) and \(2n\), a contradiction. Thus the four \(b_i\) split into two even and two odd integers. In each parity pair, the sum belongs to \(\{2n-2,2n\}\). The larger member of each pair is therefore at least \(n\). Those two larger members have opposite parity and hence are distinct, so their cross-sum is at least \(2n+1\), outside \(A_{E_0}\). This contradiction proves that \(E_0\) is witness-free and completes the classification.

## Verification
The proof is symbolic and covers every \(n\ge6\). The accompanying `verify.py` is only a finite consistency check: it exhaustively enumerates all three-even choices for \(6\le n\le12\), confirms that exactly one is witness-free in each case, and independently checks the displayed middle-interval and boundary witnesses over a larger finite range. Its output is stored in `verification_output.txt`.

The finite computation is not used to infer the infinite theorem. The infinite step is the explicit two-case witness construction plus the parity argument for \(E_0\).

## Relationship to prior work
Van Doorn and Erlbacher prove \(h_4(n)=4\) for every \(n\ge6\). Their Lemma 4.1 gives the witness-free set
\[
\{1,3,\ldots,2n-1\}\cup\{2,2n-2,2n\},
\]
and their Case I construction shows, in a more general setting, how a suitable middle even element forces a witness. They do not state a uniqueness theorem for the three-even parity-saturated extremal class. The present proof combines the middle-even mechanism with a complete analysis of the four boundary triples, showing that exactly one survives.

The earlier paper by van Doorn contains a related "optimal in a narrow sense" theorem for the five-integer problem under the assumption that all odd integers are present. That makes the same parity-saturated equality question natural here, but its theorem concerns five integers and a different even augmentation and does not imply the classification above.

MSC2020 \(11B13\) is the standard additive-bases/sumsets classification and is the primary classification used here.

## Limitations
No claim is made that the displayed set is the unique witness-free set of cardinality \(n+3\) without the assumption that all odd integers are present. The theorem is an equality-case classification inside the parity-saturated class only. It also does not address \(n<6\), where the sharp global value \(h_4(n)=4\) is not the same statement.

The originality search materially inspected the two directly relevant 2026 papers and searched for aliases such as extremal, parity-saturated, all-odd, and uniqueness formulations. An unindexed equivalent observation in older additive-combinatorics literature remains a residual historical risk.

## References
1. W. van Doorn and J. Erlbacher, *The cardinality of a set containing the pairwise sums of four positive integers*, arXiv:2609.39314v1, 2026. Lemma 4.1 and Section 5.1.
2. W. van Doorn, *The cardinality of a set containing the pairwise sums of a fixed number of integers*, arXiv:2605.00040v1, 2026. Theorem 6 and Section 4.
3. MSC2020 database, classification 11B13: Additive bases, including sumsets.
