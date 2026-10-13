# Unique maximum obstruction at the exceptional point \(n=5\) for the positive four-sum problem
## Finding
Let \(h_4(n)\) be the least integer \(h\) such that every set \(A\subseteq\{1,\ldots,2n\}\) with \(|A|\ge n+h\) contains all six pairwise sums of four distinct positive integers.

At the exceptional point \(n=5\), the maximum witness-free sets have size nine, and there is exactly one:
\[
A_0=\{1,2,3,4,6,7,8,9,10\}=\{1,\ldots,10\}\setminus\{5\}.
\]
Equivalently, if \(A\subseteq\{1,\ldots,10\}\) and \(|A|=9\), then \(A\) fails to contain the six pairwise sums of four distinct positive integers if and only if \(A=A_0\).

Consequently, combining this classification with the recent theorem \(h_4(n)=4\) for every \(n\ge6\), the complete function is
\[
h_4(1)=2,\qquad h_4(2)=3,\qquad h_4(3)=4,\qquad h_4(4)=4,\qquad h_4(5)=5,
\]
and \(h_4(n)=4\) for every \(n\ge6\).

## Assumptions and scope
A witness for \(A\subseteq\{1,\ldots,2n\}\) is a strictly increasing quadruple \(b_1<b_2<b_3<b_4\) of positive integers such that \(b_i+b_j\in A\) for all \(1\le i<j\le4\). The uniqueness assertion concerns all nine-element subsets of \(\{1,\ldots,10\}\), without a parity or structural restriction.

The classification is finite but natural: \(n=5\) is the sole exceptional point immediately below the sharp range \(n\ge6\), where the recent source proves the stable value \(h_4(n)=4\). MSC2020 \(11B13\) covers additive bases and sumsets, matching the pairwise-sum extremal problem.

## Proof
Every nine-element subset of \(\{1,\ldots,10\}\) is \(A_m=\{1,\ldots,10\}\setminus\{m\}\) for a unique \(m\in\{1,\ldots,10\}\).

First consider \(m=5\). Suppose a witness \(b_1<b_2<b_3<b_4\) existed in \(A_5\). Since every pairwise sum belongs to \(\{1,\ldots,10\}\), we have \(b_3+b_4\le10\). We show that such a quadruple must have a pair summing to \(5\).

If \(b_4=4\), then necessarily \(\{b_1,b_2,b_3,b_4\}=\{1,2,3,4\}\), and \(1+4=5\). If \(b_4\in\{5,6\}\), then \(b_3\le4\), so \(\{b_1,b_2,b_3\}\) is a three-element subset of \(\{1,2,3,4\}\). Every such subset contains either \(\{1,4\}\) or \(\{2,3\}\), hence contains a pair summing to \(5\). Finally, if \(b_4\ge7\), then \(b_3\le10-b_4\le3\). Thus \(\{b_1,b_2,b_3\}=\{1,2,3\}\), and again \(2+3=5\). In all cases a pairwise sum equals the missing element \(5\), a contradiction. Hence \(A_5\) is witness-free.

For every other missing element, an explicit witness exists. The following table lists one; all displayed pairwise sums lie in \(A_m\).

| Missing \(m\) | Witness \((b_1,b_2,b_3,b_4)\) | Distinct pairwise sums |
|---:|---|---|
| \(1,2,8,9,10\) | \((1,2,3,4)\) | \(\{3,4,5,6,7\}\) |
| \(3\) | \((1,3,4,5)\) | \(\{4,5,6,7,8,9\}\) |
| \(4\) | \((1,2,4,5)\) | \(\{3,5,6,7,9\}\) |
| \(6\) | \((1,2,3,6)\) | \(\{3,4,5,7,8,9\}\) |
| \(7\) | \((1,2,3,7)\) | \(\{3,4,5,8,9,10\}\) |

Therefore \(A_5\) is the unique witness-free nine-element set.

For completeness, the small values of \(h_4\) follow as follows. For \(n\le3\), the two largest members of four distinct positive integers have sum at least \(3+4=7>2n\), so no witness exists even in the full interval; the first true threshold is vacuous, giving \(h_4(n)=n+1\). For \(n=4\), the set \(\{1,\ldots,8\}\setminus\{5\}\) is witness-free by the same missing-\(5\) argument, while the full interval contains the witness \((1,2,3,4)\); hence \(h_4(4)=4\). The uniqueness result gives a nine-element obstruction for \(n=5\), while the full interval again contains \((1,2,3,4)\), so \(h_4(5)=5\). The value \(h_4(n)=4\) for \(n\ge6\) is the cited recent theorem.

## Verification
The proof above is symbolic and already exhausts all ten possible complements. The accompanying `verify_h4_n5.py` independently enumerates all four-element positive-integer candidates whose pairwise sums can lie in \(\{1,\ldots,10\}\), confirms that missing \(5\) is the unique nine-element obstruction, verifies every displayed witness, and exhaustively recomputes \(h_4(n)\) for \(1\le n\le5\). It uses exact integer set containment only.

The verifier is supplementary: no infinite statement is inferred from finite computation. The only infinite component, \(h_4(n)=4\) for \(n\ge6\), is imported explicitly from the recent source.

## Relationship to prior work
Van Doorn and Erlbacher, arXiv:2609.39314v1, define this positive variant and prove \(h_4(n)=4\) for all \(n\ge6\). In their final remarks they note \(h_4(5)=5\) using exactly the example \(\{1,2,3,4,6,7,8,9,10\}\). That establishes existence of an extremal obstruction, but does not classify all nine-element sets or state that the displayed obstruction is unique.

An earlier paper by van Doorn, arXiv:2605.00040v1, develops the distinction between the unrestricted and positive variants and gives general bounds for \(h_4\), but does not supply the \(n=5\) extremizer classification. The classical work of Choi, Erdős and Szemerédi introduces the pairwise-sum problem at a much broader asymptotic level and does not imply this finite boundary classification.

A separate current result for the same recent source classifies, for \(n\ge6\), witness-free sets inside the restricted parity-saturated family consisting of all odd integers and three evens. Its hypotheses require \(n\ge6\) and its sets have cardinality \(n+3\); it neither specializes to nor implies the present classification of all nine-element subsets at \(n=5\).

## Limitations
The new part is exactly the uniqueness classification at \(n=5\) and its elementary small-\(n\) consequences. It does not classify all lower-cardinality witness-free sets, and it does not classify unrestricted extremizers for \(n\ge6\). The stable range \(n\ge6\) is cited rather than reproved here.

## References
1. W. van Doorn and J. Erlbacher, *The cardinality of a set containing the pairwise sums of four positive integers*, arXiv:2609.39314v1, first posted 2026-09-30.
2. W. van Doorn, *The cardinality of a set containing the pairwise sums of a fixed number of integers*, arXiv:2605.00040v1, 2026.
3. S. L. G. Choi, P. Erdős, and E. Szemerédi, *Some additive and multiplicative problems in number theory*, Acta Arithmetica 27 (1975), 37–50.
4. Mathematics Subject Classification 2020, \(11B13\): additive bases, including sumsets.
