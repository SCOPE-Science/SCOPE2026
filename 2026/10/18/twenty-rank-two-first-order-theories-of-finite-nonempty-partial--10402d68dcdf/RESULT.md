# Twenty rank-two first-order theories of finite nonempty partial orders, with a sharp six-point cutoff

## Finding
For finite **nonempty** strict partial orders \(P=(V,<)\) in the pure order language, exactly **20** distinct theories of first-order sentences of quantifier rank at most two occur. Every theory has a representative on at most **six** elements; the bound is sharp, and precisely one of the 20 theories first occurs on six elements.

## Assumptions and scope
The signature contains only a strict transitive irreflexive relation \(<\) and equality. The universe \(V\) is finite and nonempty. In a point \(x\in V\), define the three bits \(L_x,R_x,I_x\) for the existence, respectively, of a point strictly below \(x\), strictly above \(x\), or incomparable with \(x\). Write \(t(x)=(L_x,R_x,I_x)\) and \(S(P)=\{t(x):x\in V\}\). A three-bit word is interpreted as the integer \(4L+2R+I\); the mask \(m(P)=\sum_{(L,R,I)\in S(P)}2^{4L+2R+I}\) is only an enumeration label, not a new invariant beyond \(S(P)\).

## Proof
**Rank-two characterization.** In a two-round Ehrenfeucht–Fraïssé game, after the first pair of pebbles \(x,y\), the second pebble can only observe equality, a smaller point, a larger point, or an incomparable point. Hence Duplicator can respond to both choices of side in the second round precisely when \(t(x)=t(y)\). She has a two-round winning strategy on \(P,Q\) exactly when \(S(P)=S(Q)\). Conversely, the rank-two sentence \(\exists x\,\theta_t(x)\) detects realization of each signature \(t\), where \(\theta_t\) is a conjunction of the positive or negative rank-one existence formulas for the three possibilities. Distinct sets \(S(P)\) are therefore distinct rank-two theories.

**Structural classification.** Form the undirected incomparability graph of \(P\). Its connected components are totally ordered: across distinct components all pairs are comparable, and transitivity forces a consistent orientation along every incomparability path. Consequently \(P\) is the ordinal sum of its incomparability-connected components.

If \(P\) has one vertex, \(S(P)=\{000\}\). If it is an antichain of size at least two, \(S(P)=\{001\}\). If the incomparability graph is connected and \(P\) has a comparable pair, every point has an incomparable partner. A minimal point below another point realizes \(011\), and a maximal point above another realizes \(101\). The only optional signatures are \(001\) and \(111\): precisely four possibilities \(\{011,101\}\cup T\), for \(T\subseteq\{001,111\}\).

If there are at least two incomparability components, each point in the first component has an upper point in a later component and each in the last has a lower point from an earlier component. A singleton first component realizes \(010\), while a nonsingleton first component realizes \(011\); similarly, the last component contributes \(100\) or \(101\). Any further types must be \(110\) or \(111\). Thus \(S(P)=\{a,b\}\cup T\), where \(a\in\{010,011\}\), \(b\in\{100,101\}\), and \(T\subseteq\{110,111\}\). There are at most \(2+4+2\cdot2\cdot4=22\) displayed possibilities, but the one-component and multiple-component families share exactly the two signatures \(\{011,101\}\) and \(\{011,101,111\}\). All other displayed combinations are distinct. Thus the **upper bound is \(22-2=20\)**. The table below realizes every one of these possibilities, proving the bound sharp.

**Exhaustive finite classification and witnesses.** The following table gives all attainable masks, their least orders, and explicit downset encodings. For a row of size \(n\), the tuple `D=[d_0,...,d_{n-1}]` denotes the strict lower set of vertex \(j\) by the set bits of integer `d_j`. Each tuple defines a poset (closure is immediately checked), and directly realizes the listed mask.

| Mask | Least \(n\) | Downset tuple |
| ---: | ---: | :--- |
| `1` | 1 | `[0]` |
| `2` | 2 | `[0, 0]` |
| `20` | 2 | `[0, 1]` |
| `24` | 3 | `[0, 0, 3]` |
| `36` | 3 | `[0, 1, 1]` |
| `40` | 4 | `[0, 0, 3, 1]` |
| `42` | 3 | `[0, 1, 0]` |
| `84` | 3 | `[0, 1, 3]` |
| `88` | 4 | `[0, 0, 3, 7]` |
| `100` | 4 | `[0, 1, 3, 3]` |
| `104` | 5 | `[0, 0, 3, 7, 7]` |
| `148` | 4 | `[0, 1, 1, 7]` |
| `152` | 4 | `[0, 0, 1, 7]` |
| `164` | 4 | `[0, 1, 1, 3]` |
| `168` | 5 | `[0, 1, 1, 0, 11]` |
| `170` | 4 | `[0, 1, 3, 0]` |
| `212` | 5 | `[0, 1, 1, 7, 15]` |
| `216` | 5 | `[0, 0, 1, 7, 15]` |
| `228` | 5 | `[0, 1, 3, 3, 7]` |
| `232` | 6 | `[0, 0, 3, 7, 7, 23]` |

The table is a direct constructive lower bound on the number of theories and provides representatives of size at most six. Its **completeness** follows from the structural upper bound of 20 signatures and these 20 distinct realized signatures. The independent verifier enumerates naturally labelled posets through six vertices and confirms every minimum in the table; this finite check is not substituted for the structural upper bound on all sizes.

**Sharpness.** The signature mask `232` is \(\{011,101,110,111\}\). It occurs for the six-element strict poset given by the downsets `(0,0,3,7,7,23)`: its incomparability components have sizes three, one, and two. Any poset with that signature has a nonsingleton first and last component (at least four elements) and a singleton internal component to realize \(110\) (at least one more). A point realizing \(111\) requires either an additional element inside an endpoint component or a nonsingleton internal component. Hence at least six vertices are necessary. The table shows all other masks have representatives on at most five vertices.

## Verification
Run `python3 verify.py` with standard Python 3. The program generates all naturally labelled posets through order six (per-order counts `1,2,7,40,357,4824`), computes each point's observed order-relations, obtains the same 20 masks with the minimum sizes in the table, and independently compares every two representatives by explicit two-round pebble responses. The finite census checks the presented witnesses and minimal sizes through six; the structural argument is necessary for the assertion that no larger poset can produce further rank-two theories.

## Relationship to prior work
Two-variable first-order logic over structures with a transitive relation is a classical research subject. Szwast and Tendera (2013) study the much broader *satisfiability decision problem*, not the exact count of rank-two theories of unlabelled finite nonempty partial orders; its general decidability theorem does not directly give this 20-type classification or its least-representative sizes. The present result evaluates a particularly small finite-model invariant through an explicit decomposition and exhaustive witness list.

## Limitations
The result is restricted to the **pure** strict order language, nonempty finite structures, and **quantifier rank at most two**. No assertion is made about counting quantifiers, extra predicates, ranks three or higher, or isomorphism classification. Computation through size six alone cannot exclude unseen larger-model profiles; the decomposition is indispensable. No independent audit has been performed.

## References
1. W. Szwast and L. Tendera, “FO² with one transitive relation is decidable,” *STACS 2013*, LIPIcs 20, pp. 317–328, DOI: 10.4230/LIPIcs.STACS.2013.317. Public release 2013-02-26. https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.STACS.2013.317
2. R. Fraïssé, “Sur une nouvelle classification des systèmes de relations,” *Comptes Rendus* 230 (1950), 1022–1024 (background on finite-rank back-and-forth equivalence).
