# Sharp four-state tree synchronization over two ranked symbols

## Finding

Let \(Q=\{0,1,2,3\}\). A **full context** is a finite rooted term in which every leaf is a distinct, freely varying state variable and every interior node is a transition symbol of its specified rank. A term strongly synchronizes a deterministic bottom-up tree automaton if its root state is independent of all leaf assignments. The strong reset threshold is the least possible height of such a term.

**Theorem.** Among all complete four-state tree automata with precisely one unary symbol \(w\) and one binary symbol \(f\), the largest finite strong reset threshold is exactly
\[
\boxed{11=2^4-4-1}.
\]
The universal bound \(2^4-4-1\), valid with arbitrary finite ranked alphabets, is therefore attained already with two symbols and maximum rank two. Moreover, no four-state full-context automaton with only one transition symbol of *any* finite rank has threshold eleven. Thus two symbols are the minimum alphabet cardinality attaining this universal bound.

An attaining automaton has the unary action
\[
w(0)=1,\quad w(1)=3,\quad w(2)=0,\quad w(3)=2,
\]
and binary action \(f(x,y)\) given by the complete table

| \(x\backslash y\) | 0 | 1 | 2 | 3 |
| :---: | :---: | :---: | :---: | :---: |
| 0 | 0 | 2 | 2 | 3 |
| 1 | 2 | 2 | 2 | 3 |
| 2 | 2 | 3 | 3 | 0 |
| 3 | 3 | 3 | 2 | 3 |

## Assumptions and scope

All transitions are total, all states are allowed as independent leaf assignments, height counts internal nodes on a longest root-to-leaf path, and synchronization means the **strong** (full-context) notion rather than weak-context synchronization. The two chosen symbols have ranks one and two. Nullary letters are unnecessary because they cannot occur as leaves of a full context. For an input set \(A\subseteq Q\), put \(w(A)=\{w(a):a\in A\}\); for \(A,B\subseteq Q\), put \(f(A,B)=\{f(a,b):a\in A,b\in B\}\).

## Proof

**General upper bound.** Let \(\mathcal R_h\) be the collection of nonempty state sets realized by full contexts of height at most \(h\). We have \(\mathcal R_0=\{Q\}\), and \(\mathcal R_{h+1}\) is obtained by adding all operation images with arguments from \(\mathcal R_h\). If \(\mathcal R_{h+1}=\mathcal R_h\), no new set can ever appear. If a singleton first appears at height \(H\), therefore, each previous stage from height zero through height \(H-1\) introduces at least one fresh nonsingleton set. There are only \(2^4-4-1=11\) nonempty nonsingleton subsets of \(Q\); hence \(H\le11\) for any synchronizing four-state tree automaton, regardless of the transition ranks or alphabet size.

**Exact closure for the displayed automaton.** Specializing to the two operations, the exact recurrence is
\[
\mathcal R_{h+1}=\mathcal R_h\cup\{w(A):A\in\mathcal R_h\}
\cup\{f(A,B):A,B\in\mathcal R_h\}.
\]
Represent a subset by the sum of \(2^i\) over its states \(i\). Substituting the entire displayed operation table into this recurrence yields the following **exact** first-appearance certificate. Each row lists the only set newly reachable at that height, not merely one selected witness.

| Height | New mask | New state set |
| ---: | ---: | :--- |
| 0 | 15 | \(\{0,1,2,3\}\) |
| 1 | 13 | \(\{0,2,3\}\) |
| 2 | 7 | \(\{0,1,2\}\) |
| 3 | 11 | \(\{0,1,3\}\) |
| 4 | 14 | \(\{1,2,3\}\) |
| 5 | 12 | \(\{2,3\}\) |
| 6 | 5 | \(\{0,2\}\) |
| 7 | 3 | \(\{0,1\}\) |
| 8 | 10 | \(\{1,3\}\) |
| 9 | 9 | \(\{0,3\}\) |
| 10 | 6 | \(\{1,2\}\) |
| 11 | 4 | \(\{2\}\) |

The table verifies all possible unary and ordered binary combinations at every height, because the recurrence uses the whole of \(\mathcal R_h\). Hence no singleton occurs at heights zero through ten, while a singleton first occurs at height eleven. There are four distinct three-state masks and six distinct two-state masks in the ten intermediate rows, so all eleven nonsingleton subsets occur before synchronization.

**Explicit height-eleven full context.** Let \(T_0\) be a single variable. Build terms using fresh, pairwise disjoint renamings of the variables whenever an earlier term is copied:
\[
\begin{aligned}
T_1&=f(T_0,T_0),\\
T_j&=w(T_{j-1})\quad (j=2,3,4),\\
T_5&=f(T_4,T_2),\\
T_j&=w(T_{j-1})\quad (j=6,7,8),\\
T_9&=f(T_5,T_8),\\
T_{10}&=w(T_9),\\
T_{11}&=f(T_7,T_{10}).
\end{aligned}
\]
Each \(T_j\) has height exactly \(j\) and its output set is the corresponding set in the table. In particular, \(T_{11}\) has twelve distinct variable leaves and constant root value \(2\).

**One symbol cannot suffice.** With only a single positive-rank symbol \(g\), let \(I=g(Q^r)\) denote its complete operation image. If \(I=Q\), every context image is \(Q\), so no synchronization occurs. If \(|I|=1\), synchronization occurs at height one. Otherwise \(2\le|I|\le3\), and every non-variable context image lies inside \(I\). Before the first singleton, the only possible nonsingleton images are \(Q\) and at most \(2^{|I|}-|I|-1\le4\) subsets of \(I\). The same strict-growth argument bounds the reset threshold by five. A sole nullary symbol cannot form a full context. Thus a single ranked symbol cannot attain eleven, while the displayed two-symbol automaton does.

## Verification

The finite certificate is replayed using the Python standard library:

```bash
python3 verify.py
```

The program computes every reachable state-set image by complete Cartesian-product closure at each height and asserts **exactly one** new set per height with mask sequence `15,13,7,11,14,12,5,3,10,9,6,4`. A second min/max cost-relaxation calculation independently verifies the least height of every reachable mask. An explicit term evaluator constructs the eleven-stage witness, assigns distinct variable identities, and confirms its twelve leaves and singleton image. The expected output begins with `VERIFY_OK`. The machine-readable expected sequence is in `certificate.json`. These checks are finite, exhaustive over all subsets of four states, and support the exact finite statement; they are not a claim about larger state sets.

## Relationship to prior work

Blažej, Janoušek, and Plachý prove the universal bound \(2^n-n-1\) for strong tree synchronization and provide larger-alphabet constructions approaching it. Their full 2026 account also subsumes the 2023 conference version. The bound alone does not supply a two-symbol four-state extremizer. Herrmann and Mörbitz (2026) study the **same unary-plus-binary ranked alphabet** and give an infinite family with Landau-function reset thresholds for \(n\ge5\), but do not establish four-state tightness of the general upper bound. Their outlook motivates exploring further behavior enabled by genuinely binary operations. The present explicit four-state witness attains the general upper bound with the minimal possible number of ranked symbols, a statement not implied by these constructions.

## Limitations

The result is exact at four states only: it gives neither a sharp bound for five or more states nor a classification/count of all four-state extremizers. The witness automaton has no nullary symbol and therefore no ground terms; strong synchronization remains well defined for full contexts, exactly as in the motivating two-symbol setting. Adding a nullary letter does not alter the full-context threshold, but would enlarge the literal alphabet. Independent review and historical-priority determination beyond the inspected literature have not been carried out.

## References

1. L. Herrmann and R. Mörbitz, *On smallest synchronizing terms over constant alphabets*, arXiv:2609.01184, first posted 1 September 2026. https://arxiv.org/abs/2609.01184
2. V. Blažej, J. Janoušek, and Š. Plachý, *On the Smallest Synchronizing Terms of Finite Tree Automata*, International Journal of Foundations of Computer Science 37(1), 215–239 (2026), DOI: 10.1142/S0129054125410096. Lawful open version: https://wrap.warwick.ac.uk/id/eprint/193962/
3. V. Blažej, J. Janoušek, and Š. Plachý, *On the smallest synchronizing terms of finite tree automata*, CIAA 2023, Lecture Notes in Computer Science 14151, pp. 79–90, DOI: 10.1007/978-3-031-40247-0_5; earlier conference version of [2].
