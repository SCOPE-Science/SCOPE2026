# Leaf vertices determine connected automorphisms of graph-associahedral toric varieties

## Finding

Let \(G=(V,E)\) be a finite connected simple graph with \(n=|V|\geq3\), and let \(X_G\) be the smooth projective complex toric variety of the graph-associahedral fan. Write \(L(G)=\{i\in V:\deg_G(i)=1\}\), \(\ell(G)=|L(G)|\), and \(p(i)\) for the unique neighbor of a leaf \(i\). Then the **complete Demazure-root set** of \(X_G\) is
\[
\mathcal R(X_G)=\{\varepsilon_{p(i)}-\varepsilon_i:i\in L(G)\}
\subseteq\{a\in\mathbb Z^V:\sum_{v\in V}a_v=0\}.
\]
All these roots are unipotent and their root subgroups commute. Consequently the full **identity component** of the algebraic automorphism group is
\[
\boxed{\operatorname{Aut}(X_G)^{\circ}\simeq
(\mathbb G_a)^{\ell(G)}\rtimes(\mathbb G_m)^{n-1}},
\qquad
\boxed{\dim\operatorname{Aut}(X_G)^{\circ}=n-1+\ell(G)}.
\]
The torus acts on the additive factors through the Demazure-root characters displayed above (with the root-sign convention below). In particular, the connected automorphism group is a torus, equivalently is reductive, **if and only if** \(G\) has no leaves. This describes the entire connected group, not only automorphisms preserving the toric fan.

## Assumptions and scope

All varieties and algebraic groups are over \(\mathbb C\). The graph is connected, undirected, loopless, simple, and has at least three vertices. Let
\[
N=\mathbb Z^V/\mathbb Z\mathbf1,
\qquad M=\operatorname{Hom}(N,\mathbb Z)
=\{a\in\mathbb Z^V:\sum_{v\in V}a_v=0\}.
\]
For a nonempty proper subset \(I\subsetneq V\), set \(v_I=\sum_{i\in I}\overline\varepsilon_i\in N\). A *tube* is a nonempty vertex subset whose induced graph is connected. By the graph-associahedral stellar-subdivision construction [1], the fan rays are exactly \(\mathbb R_{\geq0}v_I\) for **proper tubes** \(I\), and each \(v_I\) is primitive. The singleton tubes supply all \(v_{\{i\}}\). The fan is smooth and complete.

We use the Demazure convention of [2]: a character \(a\in M\) is a root if there is exactly one distinguished ray \(v_J\) with \(\langle a,v_J\rangle=-1\), while \(\langle a,v_I\rangle\geq0\) for every other ray. Equivalently, \(\langle a,v_I\rangle=\sum_{i\in I}a_i\). The groups here are the complex algebraic automorphism groups of the complete toric varieties, rather than automorphism groups of abstract graphs or polytopes.

## Proof

**Step 1: a negative ray must be a singleton.** Suppose \(a\in M\) is a Demazure root and its distinguished tube is \(J\). If \(J\) were not a singleton, all singleton rays would be nondistinguished, hence \(a_i=\langle a,v_{\{i\}}\rangle\geq0\) for every \(i\in V\). But \(\sum_i a_i=0\), so \(a=0\), contradicting \(\langle a,v_J\rangle=-1\). Thus \(J=\{i\}\) for a unique \(i\in V\).

**Step 2: all possible characters.** The singleton-ray inequalities now say \(a_i=-1\), \(a_k\geq0\) for every \(k\neq i\), and \(\sum_k a_k=0\). Integrality forces a unique \(j\neq i\) with \(a_j=1\), all other entries zero. Thus
\[
a=\varepsilon_j-\varepsilon_i.
\]
For any tube \(I\), its pairing is \(-1\) exactly when \(i\in I\) and \(j\notin I\); it is \(+1\) exactly when \(j\in I\) and \(i\notin I\), and is otherwise zero. For \(\{i\}\) to be the *only* negative tube, every proper connected tube containing \(i\) with more than one vertex must contain \(j\).

**Step 3: translate that condition into graph leaves.** If \(k\) is any neighbor of \(i\), the two-element subset \(\{i,k\}\) is a proper connected tube because \(n\geq3\). The condition of Step 2 therefore requires \(k=j\). Since \(G\) is connected, \(i\) has at least one neighbor, so \(\deg_G(i)=1\) and \(p(i)=j\).

Conversely, if \(i\) is a leaf with unique neighbor \(j=p(i)\), every connected induced vertex subset containing \(i\) and another vertex necessarily contains \(j\): otherwise \(i\) is isolated in its induced subgraph. Consequently \(\varepsilon_j-\varepsilon_i\) pairs to \(-1\) only with the singleton tube \(\{i\}\), and to a nonnegative integer with every other proper tube. It is therefore a root. This proves the asserted exact root classification, with no hidden candidate classes.

**Step 4: commute the root subgroups.** A connected graph on at least three vertices has no edge joining two leaves: such an edge would be an isolated two-vertex connected component. Thus the neighbor \(p(i)\) of any leaf is not another leaf. For the Cox ring with one variable \(z_I\) per proper tube, the Demazure locally nilpotent derivation for the root corresponding to \(i\) fixes all variables except \(z_{\{i\}}\), and sends that variable to
\[
\partial_i(z_{\{i\}})=
\prod_{\substack{I\text{ a proper tube}\\p(i)\in I,\ i\notin I}}z_I.
\]
This monomial does not involve the singleton variable of *any* leaf, because its factors \(z_{\{h\}}\) can occur only for \(h=p(i)\), which is not a leaf. Therefore for distinct leaves \(i,h\) the derivations \(\partial_i\) and \(\partial_h\) commute on every Cox variable. Their induced additive root subgroups commute on \(X_G\). Equivalently, the roots are pairwise orthogonal in the sense of [2, Definition 2.3].

**Step 5: identify the whole connected automorphism group.** The general Demazure--Cox structure theorem for a complete toric variety [2, Section 2; 3] says that the connected automorphism group is generated by its dense torus and the root one-parameter subgroups. Its reductive part is generated by the torus and *semisimple roots* \(a\) for which \(-a\) is also a root. Here no opposite pair is possible: an opposite root would have its negative entry at \(p(i)\), which is not a leaf, contrary to Step 3. Hence the reductive part is precisely \(T\cong(\mathbb G_m)^{n-1}\). The commuting additive subgroups are all unipotent, generate \(U\cong(\mathbb G_a)^{\ell(G)}\), and are normalized by \(T\). Thus \(\operatorname{Aut}(X_G)^\circ=U\rtimes T\), and its dimension is \(\ell(G)+(n-1)\). If no leaf exists then \(U\) is trivial; if a leaf exists then \(U\) is a nontrivial unipotent radical, proving the reductivity criterion.

## Verification

The self-contained Python program `checks/check_roots.py` constructs all connected labeled simple graphs with \(n\in\{3,4,5\}\) and all proper-tube rays. It compares exact integer Demazure inequalities against the leaf-neighbor formula and checks the pairwise vanishing of the corresponding Cox commutator tests. It finds \(4\), \(38\), and \(728\) connected graphs at these orders, respectively: \(770\) complete finite graph tests. The numbers with at least one root are \(3\), \(28\), and \(475\). Execute it with a standard-library Python 3 interpreter:

```sh
python checks/check_roots.py
```

The proof above establishes the statement for every finite connected graph with \(n\geq3\); the bounded enumeration is a regression test only, not a proof of the infinite assertion.

## Relationship to prior work

Ferreira da Rosa--Jensen--Ranganathan [1] construct graph-associahedral fans and toric blowups. Demazure's root-to-automorphism framework, including its dimension and reductive/unipotent decomposition, appears in Nill [2] and Liendo--Lucchini Arteche [3]. Those are the machinery used here and are not claimed as new. Eur--Huh--Larson [4] explicitly construct a full-dimensional additive action for the *star graph* specialization (the stellahedral variety), which is likewise existing coverage of that special family. The claim here is the graph-theoretic determination of **all** roots, their mutual commutativity and the full connected group **for every connected simple graph**. The star specialization, the toric character criterion, and general finite graph automorphism groups are not presented as novel.

## Limitations

The theorem concerns \(\operatorname{Aut}(X_G)^\circ\) only; it does not classify disconnected components or possible isomorphisms between toric varieties attached to nonisomorphic graphs. Graphs with two or fewer vertices are excluded: at two vertices the two endpoints are adjacent and opposite roots occur, invalidating the displayed formula. The base field is \(\mathbb C\); no assertion is made about arbitrary characteristic or non-split forms. The result is proved from the fan and standard root-automorphism theorems. The literature comparison does not establish global priority against unpublished or unindexed work.

## References

[1] R. Ferreira da Rosa, D. Jensen, D. Ranganathan, *Toric graph associahedra and compactifications of \(M_{0,n}\)*, arXiv:1411.0537 (v1 submitted 2014-11-03), Construction 1 and Definitions 5--7; https://arxiv.org/abs/1411.0537 .

[2] B. Nill, *Complete toric varieties with reductive automorphism group*, arXiv:math/0407491 (v1 submitted 2004-07-28), Section 2, Definition 2.1 and Proposition 2.2; https://arxiv.org/abs/math/0407491 .

[3] A. Liendo, G. Lucchini Arteche, *Automorphisms of products of toric varieties*, Math. Res. Lett. 29 (2022), DOI:10.4310/MRL.2022.v29.n2.a9; https://arxiv.org/abs/2101.03600 .

[4] C. Eur, J. Huh, M. Larson, *Stellahedral geometry of matroids*, Forum Math. Pi 11 (2023), e24, Section 3.2; https://arxiv.org/abs/2207.10605 .
