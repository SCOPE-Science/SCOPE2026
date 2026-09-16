# Dual stability of (n+1)-fold strictly-singular product compactness in X^n_{0,1}

## Context
The reflexive Banach spaces X^n_{0,1} (n >= 1) were constructed by Argyros, Beanland, and Motakis in "Strictly singular operators in Tsirelson like spaces" (arXiv:1309.4516; Illinois J. Math. 57 (2013), 1173-1217). Each X^n_{0,1} has a 1-unconditional basis, is reflexive (Corollary 3.19), and satisfies Theorem 0.1(ii): on every infinite-dimensional closed subspace Y, the product of any n+1 bounded strictly singular operators is compact, and n does not suffice. The paper left the dual question as Problem 2(iii): if S_1,...,S_{n+1} are bounded strictly singular operators on the dual X^{n*}_{0,1}, is S_1...S_{n+1} compact? Problems 2(i)-(ii) concern spreading models of the dual. This record resolves Problem 2(iii) affirmatively for every n >= 1.

## Definitions
An operator T in L(X,Y) is strictly singular if its restriction to no infinite-dimensional subspace is an isomorphic embedding (bounded below). An operator K is compact if it maps the unit ball to a relatively norm-compact set. X = X^n_{0,1} denotes the ABM space for fixed n; X* = X^{n*}_{0,1} is its dual. Adjoints satisfy (AB)* = B*A* and Schauder's theorem: K compact iff K* compact.

## Result
Theorem: For every n >= 1, let X = X^n_{0,1} with dual X*. If S_1,...,S_{n+1} in L(X*) are each bounded and strictly singular, then the product S_1...S_{n+1} is compact on X*.

## Proof / Evidence
Reflexivity gives that every S in L(X*) equals T* for a unique T in L(X) with equal norm. The primal ABM Theorem 0.1(ii) is used as a black box. It remains to show the duality lemma: if X is reflexive with unconditional basis and T* is strictly singular, then T is strictly singular. Proved contrapositively. If T|_E is bounded below (constant c) on infinite-dimensional E, extract a normalized weakly-null basic sequence (x_m) in E (reflexivity plus Bessaga-Pelczynski), perturb by gliding hump to a complemented block subspace E' on which T stays bounded below. Put y_m = Tx_m; bounded-belowness rules out any norm-Cauchy subsequence, so after differencing x'_m = x_{2m}-x_{2m+1}, both (x'_m) and (y'_m = Tx'_m) are seminormalized weakly-null basic sequences with T bounded below on [x'_m]. Simultaneous blocking gives complemented E'' = [x_m], F'' = [y_m] and a bounded projection Q onto F'' such that A_0 = QT|_{E''}: E'' -> F'' is an isomorphism (bounded below with range in F'' hence onto). Dualizing, A_0* = i*_{E''} T* Q* is an isomorphism, so T* is bounded below on the infinite-dimensional complemented subspace Z = Q*(F''*) of X*; hence T* is not strictly singular. Applying the lemma to each S_i = T_i* makes each T_i strictly singular; K = T_{n+1}...T_1 is compact by the primal theorem; then S_1...S_{n+1} = K* is compact by Schauder, with the order check (T_{n+1}...T_1)* = T_1*...T_{n+1}* = S_1...S_{n+1}. Full details in output/artifacts/DRAFT.md.

## Limitations
Uses ABM Theorem 0.1(ii) and Corollary 3.19 (reflexivity) plus standard facts (Bessaga-Pelczynski extraction, small-perturbation stability, complemented block subspaces, Schauder duality) as black boxes. Does not classify spreading models of X* (Problems 2(i)-(ii) untouched) and does not address dual sharpness (whether n factors can fail to be compact on X*).

## Reproducibility
Fix n, take ABM space X^n_{0,1}; verify reflexivity and unconditional basis; given strictly singular S_i on X*, write S_i = T_i*, apply the lemma, the primal theorem, and Schauder as above. No computation beyond functional-analytic proof.

## References
[1] S. A. Argyros, K. Beanland, P. Motakis, Strictly singular operators in Tsirelson like spaces, arXiv:1309.4516, Illinois J. Math. 57 (2013), 1173-1217 (Theorem 0.1(ii), Corollary 3.19, Problem 2(iii)).
[2] D. Kutzarova, P. Motakis, Asymptotically symmetric spaces with hereditarily non-unique spreading models, Proc. Amer. Math. Soc. (arXiv:1902.10098) — variant background, no dual product result.
