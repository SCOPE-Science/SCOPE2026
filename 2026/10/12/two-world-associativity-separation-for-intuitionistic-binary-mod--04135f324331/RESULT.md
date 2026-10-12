# Two-world associativity separation for intuitionistic binary modalities

## Finding
For the two-world chain \(W=\{0<1\}\), precisely **67** labeled ternary relations \(R\subseteq W^3\) satisfy both intuitionistic frame persistence conditions of Kaminski [1]. All 67 induce an **associative existential binary modality** \(\circ\), whereas the universal binary modality \(\bullet\) is associative for 43 and nonassociative for 24. Among the 43 where both are associative, 32 ternary relations are associative and 11 are not. Thus on the smallest non-Boolean Heyting base there are two strict distinctions:
\[
\text{ternary relational associativity}\ \Longrightarrow\ 
\text{joint modal associativity}\ \Longrightarrow\ 
\text{existential modal associativity}.
\]
Each implication is strict within the 67 admissible frames. All counts refer to **labeled relations**, not distinct isomorphism classes or distinct induced operation pairs.

## Assumptions and scope
Use the fixed poset \(W=\{0,1\}\), with \(0<1\). A ternary relation \(R(u,v,w)\) is admissible if:

1. When \(R(u,v,w)\) and \(u\le u'\), there are \(v'\ge v\) and \(w'\ge w\) with \(R(u',v',w')\).
2. When \(R(u,v,w)\), \(v\le v'\), and \(w\le w'\), some \(u'\ge u\) satisfies \(R(u',v',w')\).

These are exactly the two monotonicity clauses of [1, Definition 2]. For upward-closed truth sets \(A,B\subseteq W\), define
\[
A\circ B=\{u:\exists v\in A\,\exists w\in B\ R(u,v,w)\},
\]
\[
A\bullet B=\{u:\forall u'\ge u\;\forall v,w\in W\;(R(u',v,w)\Rightarrow (v\in A\lor w\in B))\}.
\]
The possible truth sets are \(\emptyset\), \(U=\{1\}\), and \(W\). Associativity of an operation means \((A\star B)\star C=A\star(B\star C)\) for **all** of these triples, equivalently validity of both directions of the appropriate modal associativity schema for every persistent valuation. Ternary relational associativity means, for all \(u,v,w,x\in W\),
\[
(\exists y\;R(y,v,w)\land R(u,y,x))\ \Longleftrightarrow\
(\exists z\;R(z,w,x)\land R(u,v,z)).
\]

## Proof
Write \(R_i=\{(v,w):R(i,v,w)\}\) for \(i\in\{0,1\}\), and order \(W^2\) coordinatewise. By persistence (2) at \(u=1\), \(R_1\) must be an upper set of \(W^2\). If \(R_1=\emptyset\), persistence (1) forces \(R_0=\emptyset\). If \(R_1\ne\emptyset\), it contains \((1,1)\); persistence (1) is then automatic. Persistence (2) at \(u=0\) says exactly that \(R_0\cup R_1\) is an upper set of \(W^2\). Hence these conditions are **necessary and sufficient** for admissibility.

There are six upper sets \(R_1\) of the four-point square. Fixing a nonempty \(R_1\), each permitted upper superset \(S\supseteq R_1\) gives \(2^{|R_1|}\) choices for \(R_0=(S\setminus R_1)\cup T\), \(T\subseteq R_1\). The choices of \(S\) number \(5,3,3,2,1\) for the five nonempty \(R_1\), respectively. Thus the admissible total is
\[
1+2\cdot5+4\cdot3+4\cdot3+8\cdot2+16\cdot1=67.
\]

The following exact six-case table results by evaluating the two operations on the three upward-closed sets and testing all 27 triples \((A,B,C)\), as well as testing the 16 choices \((u,v,w,x)\) in the ternary associativity condition. The `verify.py` program gives the exhaustive, dependency-free case expansion. Its eight-bit convention is bit \(4u+2v+w\) for \(R(u,v,w)\); thus **every one** of the 256 possible relations is considered, not a sample.

| Upper-coordinate row \(R_1\) | Admissible | Relation and both associative | Both modalities, relation not associative | \(\circ\) only |
|---|---:|---:|---:|---:|
| \(\emptyset\) | 1 | 1 | 0 | 0 |
| \(\{(1,1)\}\) | 10 | 10 | 0 | 0 |
| \(\{(0,1),(1,1)\}\) | 12 | 3 | 1 | 8 |
| \(\{(1,0),(1,1)\}\) | 12 | 3 | 1 | 8 |
| \(\{(0,1),(1,0),(1,1)\}\) | 16 | 8 | 0 | 8 |
| \(W^2\) | 16 | 7 | 9 | 0 |
| **Total** | **67** | **32** | **11** | **24** |

There are no other outcomes. In particular, \(\circ\) is associative in every row. To see a strict difference **without relying on the census**, let
\[
R=\{(1,0,1),(1,1,1)\}.
\]
This relation satisfies both persistence clauses. Directly from the definitions, \(A\circ B=U\) if both arguments are nonempty and \(\emptyset\) otherwise, so \(\circ\) is associative. Also, \(A\bullet B=W\) exactly when \(B\ne\emptyset\) or \(A=W\), and is \(\emptyset\) otherwise. Taking \((A,B,C)=(\emptyset,U,\emptyset)\),
\[
(A\bullet B)\bullet C=W\ne\emptyset=A\bullet(B\bullet C).
\]
For the other strict difference take
\[
R=\{(0,0,0),(0,1,0),(0,1,1),(1,0,1),(1,1,1)\}.
\]
The three-element upper-set tables of both modalities are associative (reproduced by the checker), but relational associativity fails at \((u,v,w,x)=(0,1,0,1)\): the left existential is false and the right existential true. The checker evaluates all cases rather than inferring modal associativity from this relational discrepancy.

For minimality, with one world there are only the empty and full ternary relations, and all three associativity conditions agree. On the two-world **discrete** order, there are 50 relationally associative and 206 nonassociative relations, and in each case both modal associativity tests agree with relational associativity. Indeed on any discrete base, \(A\bullet B\) is the Boolean complement of \((W\setminus A)\circ(W\setminus B)\), while testing \(\circ\) on singleton sets recovers relational associativity. Thus a two-world non-discrete order is the first possible separating base.

## Verification
Run `python3 verify.py` using the Python standard library. The program enumerates all 256 ternary relations on the two-world chain, checks the two persistence conditions verbatim, constructs each operation on all upward-closed subsets, verifies associativity for all 27 triples, verifies relational associativity on all 16 quadruples, and checks the six structural categories. It separately exhausts one-world and discrete two-world bases. The verified output begins with `VERIFY_OK`. The six-row table and two explicit witness masks (160 and 173) are asserted independently within the program.

## Relationship to prior work
Kaminski [1] defines the joint intuitionistic binary-modal semantics, proves soundness and strong completeness for the nonassociative logic, and identifies completeness for its associative extension as unresolved. In particular the paper states relational associativity suffices for soundness of the four associativity axioms, but does not classify the smallest non-Boolean frame nor give these exact counts. Kaminski [2] studies associative single-binary-modality logics and classical ternary frames; it does not supply the joint \(\circ\)/\(\bullet\) two-world intuitionistic census. The present result is a **finite semantic boundary** for the proposed associative fragment, not a decision procedure for the full logic and not a resolution of its strong-completeness problem.

## Limitations
The exact counts concern labeled ternary relations on the fixed two-element chain; they do not generalize automatically to all finite posets or infinite frames. The existence of frames validating both modal associativity schemes without satisfying the strict ternary associativity condition does **not** refute a possible completeness theorem for the relationally associative class. A semantic-equivalence or differently indexed finite-algebra classification may independently give these numbers; no uniqueness beyond the explicit comparisons is claimed. Independent validation has not been performed.

## References
[1] Michael Kaminski, *Intuitionistic logic of a binary modality*, Archive for Mathematical Logic, publicly available 2026-09-09. DOI: https://doi.org/10.1007/s00153-026-01025-3. Full text: https://link.springer.com/article/10.1007/s00153-026-01025-3.

[2] Michael Kaminski, *On undecidability of the propositional logic of an associative binary modality*, Archive for Mathematical Logic 63 (2024), 837–857. DOI: https://doi.org/10.1007/s00153-024-00921-w. Full text: https://link.springer.com/article/10.1007/s00153-024-00921-w.
