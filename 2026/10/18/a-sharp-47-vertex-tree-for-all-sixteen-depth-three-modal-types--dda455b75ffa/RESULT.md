# A sharp 47-vertex tree for all sixteen depth-three modal types

## Finding

**Theorem.** In the one-modality propositional modal language with **no propositional atoms**, consider finite, nonempty rooted directed trees with accessibility precisely along edges from each parent to its children. A tree is **depth-three type-complete** if among its vertices it realizes every possible pointed modal theory up to modal depth three, equivalently every depth-three bisimulation type. The smallest such tree has exactly **47 vertices**.

There are exactly **16** depth-three types. The lower bound is proved for every finite rooted directed tree, without restrictions on degrees or total height. A complete explicit 47-vertex parent–child certificate attains the bound.

## Assumptions and scope

A rooted directed tree is a finite arborescence whose root has no incoming edge, whose other vertices have exactly one incoming edge, and in which every vertex is reached from the root. The only accessibility relation is the directed **immediate-child** relation, not reflexive reachability, strict-descendant accessibility, an undirected graph relation, or a relation permitting cycles. There are no propositional letters, node labels, edge labels, or counting modalities. The modal language has Boolean connectives, constants true and false, and one existential modality \(\Diamond\); the universal modality \(\Box\) is its Boolean dual. The depth of a formula is its maximum nesting depth of modalities.

For a vertex \(v\), define recursively the integer code
\[
\tau_0(v)=0,\qquad
\tau_{j+1}(v)=\sum_{b\in\{\tau_j(u):\,v\to u\}}2^b .
\]
The set in the sum, rather than a multiset, is essential: modal logic without counting does not distinguish one child from several identical children. Induction shows that the possible values of \(\tau_1\) are \(0,1\), those of \(\tau_2\) are \(0,1,2,3\), and those of \(\tau_3\) are precisely \(0,1,\ldots,15\). Each is realized by some finite rooted tree: attach, to a new root, one representative for every code in the desired subset of the previous level.

These codes are exactly the depth-bounded modal equivalence classes. In particular, a modal characteristic formula for a code \(t\) at positive depth \(j\) asserts the existence of a child of every previous-depth type indexed by a set bit of \(t\), and asserts that every child has one of those types. The empty set gives the formula \(\Box\bot\). This proves both soundness and separation of the displayed codes.

## Proof

**Step 1: reducing a depth-three code to depth two.** For \(t\in\{0,\ldots,15\}\) let \(\beta(t)\) be the depth-two code of any vertex of depth-three code \(t\). It is determined by \(t\), since a child with depth-two code zero has depth-one code zero, whereas a child with depth-two code \(1,2,\) or \(3\) has depth-one code one. Consequently
\[
\beta(0)=0,\quad \beta(1)=1,\quad
\beta(t)=\begin{cases}2,&t\ge2\text{ even},\\3,&t\ge3\text{ odd}.\end{cases}
\]
This identity also follows by deleting one layer from the characteristic formula of \(t\).

**Step 2: a weighted child-demand inequality.** Set \(\lambda_0=1\), \(\lambda_1=2\), \(\lambda_2=3\), and \(\lambda_3=4\). For each code \(t\), put
\[
D(t)=\sum_{b\in\{0,1,2,3\}:\,\text{bit }b\text{ of }t\text{ is }1}\lambda_b,
\qquad h(t)=1+D(t)-\lambda_{\beta(t)}.
\]
A vertex with code \(t\) must have at least one child of depth-two type \(b\) for each set bit \(b\). Since the four requirements concern distinct child types, their witnesses must be different children. With positive weights,
\[
D(\tau_3(v))\le\sum_{v\to u}\lambda_{\tau_2(u)}
=\sum_{v\to u}\lambda_{\beta(\tau_3(u))}.
\]
Sum this inequality over all vertices of any finite rooted directed tree \(T\), with root \(r\). Every nonroot vertex is counted once on the right, so
\[
\sum_{v\in V(T)}D(\tau_3(v))
\le \sum_{v\in V(T)}\lambda_{\beta(\tau_3(v))}
      -\lambda_{\beta(\tau_3(r))}.
\]
Rearranging gives the **global conservation bound**
\[
|V(T)|\ge \sum_{v\in V(T)}h(\tau_3(v))
          +\lambda_{\beta(\tau_3(r))}. \tag{1}
\]
The complete potential table, in order of code \(0,1,\ldots,15\), is
\[
\big(h(0),h(1),\ldots,h(15)\big)
=(0,0,0,0,1,1,3,3,2,2,4,4,5,5,7,7).
\]
Thus every potential is nonnegative, and the sum of the potentials over the **sixteen distinct types** is exactly \(44\). A type-complete tree therefore has
\[
\sum_{v\in V(T)}h(\tau_3(v))\ge44,
\]
since each of the sixteen codes occurs and extra vertices contribute nonnegative potential.

**Step 3: paying for the root.** A vertex of depth-three code \(4\) has a child of depth-two code \(2\), which has a child of depth-one code \(1\), which has a child. Thus this vertex lies above a directed path of length three. A tree containing type \(4\) has a root with a path of length at least three below it. In particular its root's depth-three code cannot be \(0,1,2,\) or \(3\), which only occur at vertices with no path of length three. The reduction formula from Step 1 then implies
\[
\lambda_{\beta(\tau_3(r))}\ge3.
\]
Combining this with (1) yields \(|V(T)|\ge44+3=47\).

**Step 4: attaining equality.** The file `witness.json` gives a rooted tree on vertices \(0,\ldots,46\), with 46 directed child edges. Its root is vertex \(0\) and has depth-three code \(4\). Bottom-up evaluation by the defining recurrence gives exactly the vertex codes listed in the witness. The 16 codes all occur. There are 19 vertices of code zero, 11 of code one, three of code two, two of code three, and one of each code from four through fifteen. Therefore \(\sum_vh(\tau_3(v))=44\), the root contributes \(\lambda_2=3\), and the certificate has the forced minimum 47 vertices. This establishes the theorem. \(\square\)

## Verification

The supplied `verify.py` reads `witness.json` in the same directory using only Python's standard library. It checks that the 47 vertices form a genuine rooted arborescence, with 46 edges, exactly one incoming edge per nonroot vertex, root reachability, and no cycles. It then computes all four levels of modal codes independently from the edge list, checking the 16 represented depth-three codes against the explicit witness annotation. It independently evaluates the reduction, potential table, conservation inequality, exact 44-unit potential sum, and the root's 3-unit contribution. Run `python3 verify.py` from the directory containing both bundled files. No exhaustive search over all smaller trees is claimed or needed: the analytic inequality proves the lower bound for arbitrary finite sizes.

## Relationship to prior work

Papacchini and Schmidt (2011), *A Tableau Calculus for Minimal Modal Model Generation*, develop sound and complete generation of minimal **modal Herbrand models for supplied input formulae**; their minimality is inclusion-minimality of Herbrand interpretations, not the smallest number of vertices in a single tree simultaneously representing every depth-bounded modal type. Their full paper's model definitions and tableaux results were compared with the present cardinality objective. Their 2011 work fixes the pre-2016 logical and model-minimization setting in which this finite question arises.

Bolander and Burigana (2024), *Better Bounded Bisimulation Contractions*, show that rooted bounded-bisimulation contractions minimize a **pointed model** while preserving its depth-bounded theory, over general Kripke frames. Their Definitions 3.10 and Theorems 4.4 and 5.6 concern a different minimization constraint from simultaneous realization of all sixteen pointed types **at every vertex of one tree**. In particular, their Section 6 uses labelled multi-modal binary-tree examples, not the unlabelled one-modality type-complete tree here. The general finite-depth type recursion is standard; the claim here is the exact constrained simultaneous-coverage optimum and its weighted dual proof, not the enumeration of sixteen types by itself.

The distinction between tree and shared-state directed-acyclic representations is material: a directed acyclic graph can realize all sixteen types with only sixteen vertices by letting each vertex coded \(t\) point to vertices coded \(b\in\{0,1,2,3\}\) for the set bits of \(t\). The vertices of codes \(0,1,2,3\) have the respective reductions \(0,1,2,3\), and the resulting edges always descend in the code order, so this construction is acyclic. A rooted **tree** forbids the shared child witnesses that make the smaller graph possible. This comparison motivates the 47-vertex tree cost; it is not a second optimality claim in the theorem.

## Limitations

The result concerns the specified **finite**, **atom-free**, **single-modal**, **immediate-child** rooted trees and modal depth **exactly three**. It does not assert a general formula for larger depths, or bounds with propositional labels, counting modalities, backward modalities, descendant accessibility, or arbitrary Kripke graphs. Its explicit upper bound uses 47 vertices and its exact lower bound uses a verified finite 16-entry potential table. The literature search cannot establish absolute priority over unindexed publications or unpublished enumerations; independent assessment has not been performed.

## References

1. Fabio Papacchini and Renate A. Schmidt. *A Tableau Calculus for Minimal Modal Model Generation*. Electronic Notes in Theoretical Computer Science 278 (2011), 159–172. DOI: 10.1016/j.entcs.2011.10.013. Author full text: https://www.csc.liv.ac.uk/~papacchf/papers/PapacchiniSchmidt11a.pdf. First public online: 2011-10-29 (university bibliographic record).
2. Thomas Bolander and Alessandro Burigana. *Better Bounded Bisimulation Contractions*. Advances in Modal Logic 15 (2024), 249–268. arXiv:2405.00480, https://arxiv.org/abs/2405.00480.
