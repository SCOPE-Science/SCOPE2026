# Minimal failure of \(f\)-corner inheritance under binary DFA products

## Finding
Let \(\Sigma=\{a,b\}\), and let \(f:\Sigma^*\to\{-1,1\}\) assign \(+1\) to the empty word and to precisely the nonempty words beginning with \(a\). For a deterministic complete automaton \(M\), let \(d_f^+(p,q)\) be the shortest length of an \(f\)-positive word taking state \(p\) to state \(q\), with value \(\infty\) when no such word exists. A state \(z\) is an \(f\)-corner when \(d_f^+(q,z)<d_f^+(z,q)\) for every other state \(q\).

The property that two designated \(f\)-corners remain an \(f\)-corner in the synchronous product **fails** for two strongly connected binary automata with respectively two and three states. Their product is nonetheless synchronizable to the designated state. Moreover, **five is the minimum sum of factor-state counts for failure** among all pairs of complete binary automata with this fixed \(f\) (including automata not assumed strongly connected).

## Assumptions and scope
The state sets are \(Q_A=\{0,1\}\), \(Q_B=\{0,1,2\}\), with transition tables written as ordered images of states in increasing order:

| Automaton | \(a\) | \(b\) |
| --- | --- | --- |
| \(A\) | `00` | `10` |
| \(B\) | `002` | `120` |

For example, `120` means \(b(0)=1\), \(b(1)=2\), and \(b(2)=0\). The product \(P=A\times B\) uses simultaneous application of the same letter to both coordinates, with designated product state \(z=(0,0)\). Distances are lengths of arbitrary finite input words subject only to the stated positivity condition; no bound on word length is assumed.

## Proof
**1. The individual corners.** The \(b\)-transition is a two-cycle on \(A\) and a three-cycle on \(B\), so both automata are strongly connected. In \(A\), the shortest positive routes have
\[
d_f^+(1,0)=1\quad(\mathtt a),\qquad d_f^+(0,1)=2\quad(\mathtt{ab}).
\]
In \(B\), they have
\[
\begin{aligned}
d_f^+(1,0)&=1 &(\mathtt a),&\qquad d_f^+(0,1)=2 &(\mathtt{ab}),\\
d_f^+(2,0)&=2 &(\mathtt{ab}),&\qquad d_f^+(0,2)=3 &(\mathtt{abb}).
\end{aligned}
\]
The minima follow because a positive nonempty word must begin with \(a\): from state \(0\), the first \(a\) leaves both machines in state \(0\), while in \(B\) state \(2\) is fixed by \(a\). Thus state \(0\) is an \(f\)-corner in each factor.

**2. Failure in the product.** Put \(q=(0,2)\). Every positive word of length at most two is one of \(\mathtt a,\mathtt{aa},\mathtt{ab}\). Starting from \(z\), their respective endpoints are \((0,0),(0,0),(1,1)\); starting from \(q\), their respective endpoints are \((0,2),(0,2),(1,0)\). None carries \(z\) to \(q\), or \(q\) to \(z\). Yet
\[
z\xrightarrow{\mathtt{abb}}q,
\qquad q\xrightarrow{\mathtt{aba}}z.
\]
Consequently
\[
\boxed{d_f^+(z,q)=3=d_f^+(q,z),}
\]
contradicting the strict inequality required of a product \(f\)-corner. This obstruction is not failure of simultaneous synchronization: the word \(\mathtt{aba}\) sends **every** state of \(A\) to \(0\) and **every** state of \(B\) to \(0\), hence resets \(P\) to \(z\).

**3. Minimal total number of states.** A one-state factor changes none of the positive distances in the other factor; it cannot create a failure. It remains to exclude a pair of two-state factors. Rename the designated corner of each factor \(0\). If \(0\) is an \(f\)-corner, necessarily \(a(0)=0\), since otherwise \(d_f^+(0,1)=1\) while \(d_f^+(1,0)\ge1\). There are precisely two types of two-state binary automata with corner \(0\):

* **Type I:** \(a\) sends both states to \(0\), and \(b\) is any of the four possible maps. Indeed, \(d_f^+(1,0)=1<d_f^+(0,1)\), the latter distance being at least two or infinite.
* **Type II:** \(a\) is the identity and \(b\) sends both states to \(0\). Indeed, \(d_f^+(1,0)=2\) via \(\mathtt{ab}\), whereas \(d_f^+(0,1)=\infty\). To see that no other identity-\(a\) case qualifies, a positive path from \(1\) to \(0\) forces \(b(1)=0\); if \(b(0)=1\), both directed positive distances are two.

For two Type-I factors, \(a\) resets the product to \((0,0)\), and every positive route leaving that state must have length at least two: the product corner inequality holds. For two Type-II factors, both letters fix \((0,0)\), so it has no positive route to any other state; \(\mathtt{ab}\) resets every state to \((0,0)\). In a mixed pair, the Type-II coordinate cannot leave \(0\) when started at \(0\), while \(\mathtt{aba}\) resets the product to \((0,0)\). Every target-other state with Type-II coordinate \(1\) is therefore unreachable from \((0,0)\) and has a finite positive route back. The sole other state with Type-II coordinate \(0\) reaches the target in one step using \(a\), whereas the target cannot leave itself in one positive step. Thus the product is an \(f\)-corner in every two-by-two case. Together with the two-by-three witness above, this proves the sharp minimum sum of five states.

## Verification
The standalone Python 3 program `verify_corner.py` independently computes positive distances using breadth-first search with an explicit first-letter constraint. It tests all \(16\) labeled two-state binary automata, finds exactly \(5\) with corner \(0\), and checks all \(25\) ordered pairs of these against product corner inheritance. It also checks both factor transition graphs are strongly connected, both factor corners, the equality of product distances, and the joint reset word. Execute `python3 verify_corner.py`; the expected output begins `VERIFY_OK`. The proof above does not rely on extrapolation from those finite tests.

## Relationship to prior work
Bradshaw, Clow, and Stacho introduced \(f\)-corners and proved that the synchronous product of two automata with designated \(f\)-corners is synchronizable to the designated pair (Theorem 6.1 of [1]). Immediately before that theorem, they explicitly leave open whether the designated pair must itself be an \(f\)-corner. The construction here answers **that structural question negatively** for the simple regular positivity language of words beginning with \(a\), and establishes a minimum-size obstruction within that language. It neither contradicts their synchronization theorem nor settles their separate conjecture about synchronizing products of three or more factors.

## Limitations
The minimality statement fixes the alphabet \(\{a,b\}\) and this particular positivity function. It does not prove a minimum size over all possible positivity functions or all alphabet sizes. The construction shows loss of the corner property, not loss of synchronizability. The journal version of [1] has not been independently compared line by line with the inspected freely accessible preprint; related independently unpublished constructions cannot be excluded.

## References
[1] P. Bradshaw, A. Clow, and L. Stacho, *A cornering strategy for synchronizing a DFA*, arXiv:2405.00826v3 (initial public submission 2024-05-01; version 3, 2025-08-20), Sections 4.1, 6 and 7; https://arxiv.org/abs/2405.00826 . Journal record: *Theoretical Computer Science* 1073 (2026), 115864, DOI:10.1016/j.tcs.2026.115864.
