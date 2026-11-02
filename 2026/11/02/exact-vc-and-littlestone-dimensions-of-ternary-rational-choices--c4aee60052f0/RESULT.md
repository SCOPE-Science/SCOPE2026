# Exact VC and Littlestone dimensions of ternary rational choices on seven alternatives

## Finding

A strict ranking of seven alternatives determines a Boolean choice concept on ordered pairs of a designated winner and an unordered pair of competing alternatives: the concept labels a query positively if the designated alternative wins the corresponding three-element menu. This natural finite rational-choice class has **exactly** \(2520\) distinct concepts and
\[
\operatorname{VCdim}(\mathcal H_7)=5,\qquad \operatorname{Ldim}(\mathcal H_7)=10.
\]
For \(t\ge1\) independent seven-alternative decision contexts, with queries restricted to one context at a time, the product class has \(\operatorname{VCdim}=5t\) and \(\operatorname{Ldim}=10t\). Its exact adaptive-minus-static dimension gap is therefore \(5t\), and its dimension ratio is two.

## Assumptions and scope

Write \(U=\{0,1,\ldots,6\}\). A strict ranking is a bijection \(r:U\to\{0,1,\ldots,6\}\), with larger values denoting higher preference. A query is \(q=(x,\{a,b\})\), where \(x,a,b\) are distinct. The Boolean concept induced by \(r\) is
\[
h_r(x,\{a,b\})=\mathbf1\{r(x)>r(a)\text{ and }r(x)>r(b)\}.
\]
There are \(3\binom73=105\) queries. Two rankings determine identical concepts precisely when they have the same first five alternatives in best-to-worst order: the two lowest-ranked alternatives can be exchanged. Hence the exact number of distinct concepts is \(7!/2=2520\).

VC dimension means the largest number of *fixed, distinct* membership queries whose all Boolean traces occur. Littlestone dimension means the maximum complete binary depth of a (possibly adaptive) membership-query tree that admits a distinct compatible concept at every terminal leaf. In a product of \(t\) copies the alternatives and query domains are disjoint; a query never mixes alternatives from different copies.

## Proof

**Static lower bound.** Fix two anchor alternatives, labeled \(0\) and \(1\). Consider the five queries \((x,\{0,1\})\) for \(x\in\{2,3,4,5,6\}\). Every prescribed five-bit labeling is realized: place exactly its positive-labeled alternatives above both anchors and its negative-labeled alternatives below both anchors, breaking all ties arbitrarily. Thus \(\operatorname{VCdim}\ge5\).

**Static upper bound (finite exhaustive proof).** All queries are isomorphic under permutations of the seven alternatives. A six-element shattered support, if one existed, could therefore be relabeled to contain the fixed query \(q_0=(0,\{1,2\})\). Enumerate the \(2520\) distinct concepts as rank permutations satisfying \(r^{-1}(0)<r^{-1}(1)\). For each of the \(105\) queries, form the exact \(2520\)-bit positive-concept mask. Starting with the two nonempty trace blocks defined by \(q_0\), recursively add query indices in increasing order, retaining a branch only when the new mask splits **every** trace block into nonempty zero- and one-trace blocks. This is exhaustive for all potentially shattered supports containing \(q_0\), without enumerating unshattered supports. The verifier `verify_top_choice.py` checks all \(286503\) surviving partial shattered supports; its depth counts for support sizes one through six are \(1,94,3561,57484,225363,0\). Thus none has size six. The independent verifier `independent_top_choice.py` re-enumerates rankings in a distinct representation and reproduces the complete obstruction. Hence \(\operatorname{VCdim}\le5\).

**Adaptive lower bound (complete constructive certificate).** The file `top_choice_depth10_certificate.json` contains an actual full depth-ten binary query tree. Each internal node specifies a three-element menu and a distinguished potential winner; each leaf specifies a strict ranking of all seven alternatives. Its \(1023\) internal nodes, \(1024\) leaves, and \(1024\) distinct compatible terminal ranking witnesses are verified independently of certificate construction by `verify_top_choice.py`. Every root-to-leaf prescribed answer agrees with the displayed ranking at that leaf. Consequently \(\operatorname{Ldim}\ge10\).

**Adaptive upper bound (all possible first queries).** Every query has precisely \(7!/6=840\) positive *distinct* concepts. Indeed, exactly one third of the strict rankings put the designated choice above both opponents, and each Boolean concept is represented by exactly two strict rankings. A complete depth-eleven decision tree would require at least \(2^{10}=1024\) distinct positive concepts on the positive branch of its root, a contradiction. Therefore \(\operatorname{Ldim}\le10\).

**Products.** On disjoint query domains, a fixed query set is shattered by a product precisely when the query subset on each component is shattered. Thus VC dimension is additive. For online dimension, the exact finite version-space recursion
\[
L(V)=\max_q\bigl(1+\min\{L(V_{q=0}),L(V_{q=1})\}\bigr)
\]
(with a maximum of zero for unsplittable families) shows additivity \(L(V\times W)=L(V)+L(W)\) for independent query domains: every split acts on precisely one factor, and induction on the sum of finite version-space sizes proves the upper bound while concatenating optimal trees proves the lower bound. Iterating proves the claimed \(5t\) and \(10t\) dimensions for every positive integer \(t\).

## Verification

Run with Python 3 (standard library only):

```sh
python3 verify_top_choice.py top_choice_depth10_certificate.json
python3 independent_top_choice.py
```

The first program checks the exact concept count and two-to-one ranking equivalence, all masks, the complete six-query obstruction, the five-query shattered witness, every edge-to-leaf prediction of the depth-ten certificate, uniqueness of all \(1024\) leaves, and the depth-eleven root-branch upper bound. The second independently re-enumerates the choice class and replays the static obstruction; it also checks the smaller sizes \(3\le n\le6\) using a distinct finite-depth recurrence. These calculations use exact integers and exhaustive searches, not floating-point or random samples. Successful run markers are `TERNARY_CHOICE_ALL_CHECKS_PASS` and `INDEPENDENT_PASS` for all five sizes.

## Relationship to prior work

Cantone, Giarlotta and Watson (2020) analyze rationalizable choice resolutions and provide the broader axiomatic setting of deterministic maximum-of-order choice; their inspected full-text sections do not provide the exact ternary-menu static/adaptive dimensions. Basu and Echenique (2020) analyze learnability and VC/P dimension for decision theories; they explicitly restrict the discussion of choice functions to binary menus, not the three-alternative Boolean winner predicates here. Kalai (2003) treats learnability and rationality of choice more generally; available abstract-level material does not state these exact finite invariants, but a conclusive complete-text comparison could not be made and remains a priority risk.

The three-way winner predicate is distinct from the three-way *betweenness* predicate: a query asks whether a specified alternative is **highest**, not whether it lies between the other two. Coincident values of adaptive dimension for some small sizes cannot establish equivalence or broader coverage. The independent-context product uses standard online-dimension additivity; only the exact base dimensions and their application to this ternary choice class are offered as new.

## Limitations

The exact non-product classification here is for **seven** alternatives. It does not determine the asymptotic dimension of a single rational-choice class as the alternative set itself grows. The product separation uses disjoint menu contexts; it is not a claimed separation for one unrestricted total order over all \(7t\) alternatives. The VC upper bound and online lower bound have executable finite certificates rather than short closed-form proofs. Historical priority is uncertain, especially under alternate rational-choice learning notions, and there has been no independent scientific audit.

## References

- D. Cantone, A. Giarlotta and S. Watson, *Choice resolutions*, Social Choice and Welfare (first online 2020-11-03), https://doi.org/10.1007/s00355-020-01285-9.
- P. Basu and F. Echenique, *On the falsifiability and learnability of decision theories*, Theoretical Economics (first online 2020-11-20), https://doi.org/10.3982/TE3438.
- G. Kalai, *Learnability and Rationality of Choice*, Journal of Economic Theory (2003), https://doi.org/10.1016/S0022-0531(03)00083-8. Full text not materially inspected.
