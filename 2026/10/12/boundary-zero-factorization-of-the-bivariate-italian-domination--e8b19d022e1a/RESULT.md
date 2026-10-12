# Boundary-zero factorization of the bivariate Italian domination law of chain graphs

## Finding

**Theorem (full bivariate enumerator).** Let \(G\) be a connected chain graph with a canonical bipartite twin-class decomposition \(A_1,\ldots,A_p\) and \(B_1,\ldots,B_p\), where \(p\ge1\), all class sizes \(\alpha_i=|A_i|\) and \(\beta_j=|B_j|\) are positive, and \(A_i\) is complete to \(B_j\) precisely when \(j\le i\). An Italian dominating function is a map \(f:V(G)\to\{0,1,2\}\) such that each zero-labelled vertex has total weight at least two in its open neighborhood. Define
\[
\mathcal I_G(u,v)=\sum_{f\ \mathrm{Italian}}u^{n_1(f)}v^{n_2(f)},\qquad n_h(f)=|\{z\in V(G):f(z)=h\}|.
\]
This polynomial, including each individual coefficient, is given by the following explicit boundary-zero factorization.

Put \(P_m(u,v)=(u+v)^m\), \(Q_m(u,v)=(1+u+v)^m\), and \(R_m=Q_m-P_m\). For \(i\in\{1,\ldots,p+1\}\), put
\[
U_{i,t}=\begin{cases}P_{\alpha_t},&t<i,\\R_{\alpha_t},&t=i\le p,\\Q_{\alpha_t},&t>i;\end{cases}
\]
where \(i=p+1\) selects \(P\) in every class. For \(j\in\{0,\ldots,p\}\), put
\[
V_{j,t}=\begin{cases}Q_{\beta_t},&t<j,\\R_{\beta_t},&t=j\ge1,\\P_{\beta_t},&t>j;\end{cases}
\]
where \(j=0\) selects \(P\) everywhere. In each displayed polynomial the variables are \((u,v)\). Define the marked products
\[
F_{i,j}(u,v,y)=\prod_{t=1}^p
 U_{i,t}\bigl(u y^{\mathbf1_{j\ge1,\ t\ge j}},\ v y^{2\mathbf1_{j\ge1,\ t\ge j}}\bigr),
\]
\[
H_{j,i}(u,v,y)=\prod_{t=1}^p
 V_{j,t}\bigl(u y^{\mathbf1_{i\le p,\ t\le i}},\ v y^{2\mathbf1_{i\le p,\ t\le i}}\bigr).
\]
The linear operators \(\mathsf T_{\mathrm{all}}(F)=F(u,v,1)\) and
\(\mathsf T_{\ge2}(F)=F(u,v,1)-[y^0]F-[y^1]F\) retain, respectively, all assignments or only assignments with marked weight at least two. Then
\[
\boxed{\displaystyle
\mathcal I_G(u,v)=\sum_{i=1}^{p+1}\sum_{j=0}^p
\left(\begin{cases}\mathsf T_{\mathrm{all}}F_{i,j},&j=0,\\\mathsf T_{\ge2}F_{i,j},&j\ge1\end{cases}\right)
\left(\begin{cases}\mathsf T_{\mathrm{all}}H_{j,i},&i=p+1,\\\mathsf T_{\ge2}H_{j,i},&i\le p\end{cases}\right).}
\]
Every factor on the right is a finite explicit binomial polynomial. In particular, the ordinary Italian domination polynomial is exactly \(D_I(G,x)=\mathcal I_G(x,x^2)\), and all its coefficients can be obtained in polynomial time in \(|V(G)|\).

**Corollary (minimum weight and its multiplicity).** Suppose \(p\ge2\), so \(G\) is not complete bipartite. Write \(a=\sum_i\alpha_i\), \(b=\sum_j\beta_j\), and
\[
C_3=\mathbf1_{a=2}+\mathbf1_{a=3,\alpha_p\ge2}
+\mathbf1_{b=2}+\mathbf1_{b=3,\beta_1\ge2}
+\mathbf1_{a=2,\beta_p=1}+\mathbf1_{b=2,\alpha_1=1}.
\]
The number of weight-three Italian dominating functions is exactly \(C_3\); no weight-two function exists; a weight-four function always exists. Thus \(\gamma_I(G)=3\) if \(C_3>0\), and \(\gamma_I(G)=4\) otherwise. For example \(\alpha=(1,2)\), \(\beta=(2,1)\) has exactly two minimum functions, both of weight three, notwithstanding both bipartition shores having three vertices.

## Assumptions and scope

All graphs are finite, undirected, and simple. A connected chain graph means a nonempty bipartite graph with nested neighborhoods on each side; collapsing equal open-neighborhood classes gives the canonical indexed blocks above, with each class nonempty and edges \(A_iB_j\) iff \(j\le i\). Both shores are nonempty. The full enumerator holds even when \(p=1\) (a complete bipartite graph); the minimum-weight corollary deliberately assumes \(p\ge2\). Distinct vertex assignments are counted separately, even if their labels have equal totals. The independent binomial variables \(u,v\) count the numbers of labels one and two; weight uses the substitution \((u,v)=(x,x^2)\).

## Proof

**Boundary-zero decomposition.** Every labelling has a unique boundary \(i\): the smallest class index containing a zero on the \(A\)-shore, or \(p+1\) if none. Thus all earlier \(A\)-classes contain only ones and twos, class \(i\), when present, contains a zero, and all later classes are unrestricted; their exact generating factors are \(P,R,Q\). Similarly, let \(j\) be the largest \(B\)-index containing a zero, or zero when none. Earlier classes are unrestricted, class \(j\) contains a zero when present, and later classes contain no zero. These are precisely the \(U\)- and \(V\)-products, and different boundary pairs are disjoint.

For any zero-labelled vertex in \(A_t\), the entire open neighborhood is \(B_1\cup\cdots\cup B_t\), so its guarding weight is the sum on that prefix. If there is an \(A\)-zero, the hardest such constraint occurs at the least zero-index \(i\): all further zero-neighborhoods contain the prefix ending at \(i\). Therefore all \(A\)-zeros are guarded if and only if the total weight on \(B_1\cup\cdots\cup B_i\) is at least two. Symmetrically, a zero in \(B_t\) has neighborhood \(A_t\cup\cdots\cup A_p\), and the hardest \(B\)-zero lies in its greatest zero-index \(j\). All \(B\)-zeros are therefore guarded if and only if the weight on \(A_j\cup\cdots\cup A_p\) is at least two. A shore with no zero imposes no guarding condition.

Fix a boundary pair \((i,j)\). These two numerical conditions involve disjoint sets of labelling variables, one on each shore. Mark the relevant weight on \(A_j\cup\cdots\cup A_p\) in \(F_{i,j}\), and on \(B_1\cup\cdots\cup B_i\) in \(H_{j,i}\), with the variable \(y\); label one contributes one exponent and label two contributes two. Since all coefficients are nonnegative, \(\mathsf T_{\ge2}\) discards exactly the forbidden marked weights zero and one. The two sides multiply independently. Sum over the unique pairs \((i,j)\) to obtain the asserted formula without overcounting. Since only the three capped weight states zero, one, and at least two are needed in each marked product, its coefficients can be computed by ordinary polynomial multiplication using polynomially many arithmetic operations in the vertex count.

**Minimum-weight corollary.** For \(p\ge2\), both shores have at least two vertices and the least neighborhood on \(A_1\) is \(B_1\), while that on \(B_p\) is \(A_p\). No Italian assignment of weight two can guard all zeros: a lone label-two vertex leaves some zero on its own shore unguarded; two label-ones on separate shores leave zeros with opposing weight at most one; two label-ones on one shore either leave zeros on that shore or, if that shore has exactly two vertices, leave a zero on the other shore seeing only one of the two (the least-neighborhood boundary). Labelling one vertex of \(A_p\) and one vertex of \(B_1\) by two, with every other vertex zero, gives a valid weight-four assignment.

To obtain weight three, partition three guard units between the shores. A direct check of their zero constraints produces exactly six disjoint possibilities, each with one assignment when its indicator is true: (1) the \(A\)-shore has two vertices, with labels one in \(A_1\) and two in \(A_p\); (2) the \(A\)-shore has three vertices, all labelled one, with at least two in \(A_p\); (3) the symmetric \(B\)-shore two-vertex case, with two in \(B_1\) and one in \(B_p\); (4) the symmetric \(B\)-shore three-vertex all-one case with at least two in \(B_1\); (5) the \(A\)-shore has two vertices, both labelled one, and the unique vertex of \(B_p\) is labelled one; (6) the \(B\)-shore has two vertices, both labelled one, and the unique vertex of \(A_1\) is labelled one. Every unmentioned vertex receives zero. Conversely, any feasible weight-three labelling must fall in one of these forms: if a shore contains a zero, it requires at least two units in its neighbor shore; the distributions of the three available units and the extreme neighborhoods then force one of these six patterns. Each is readily checked by direct neighborhood sums. These possibilities yield exactly the six terms defining \(C_3\); together with the weight-two exclusion and weight-four construction they prove the corollary.

## Verification

Run `python3 verify_italian_chain_bivariate.py` from the same directory as this document; it has no nonstandard dependencies. The verifier constructs the stated generating function using capped-weight twin-class products, then independently exhausts all \(3^n\) vertex labellings against the original adjacency matrix. It checks 419 class profiles, including 383 proper chain-graph profiles, and tests 12,707,343 labellings. It also checks the exact weight-three coefficient and minimum-weight dichotomy for every proper profile. Representative coefficient distributions and the complete output appear in `verification_output.txt`. These finite tests corroborate the algebraic proof; they are not asserted to prove the infinite family.

## Relationship to prior work

Shao and Zhao, *Counting Weight-k Italian Dominating Sets on Trees and Cycles* (arXiv:2610.00108v1, first public September 9, 2026), define the Italian domination polynomial and provide complete counting algorithms for paths, trees, and cycles. Their inspected full text does not give the boundary-zero decomposition or the bivariate enumerator on connected chain graphs; chain graphs can contain arbitrarily large complete bipartite subgraphs and need not be trees or cycles. Padamutham and Palagiri, *Complexity of Roman {2}-domination and the double Roman domination in graphs* (2020), study the minimum Roman \(\{2\}\)-domination parameter on chain graphs, but not the complete function distribution. Roman domination, unlike Italian domination, requires a zero to have a neighbor explicitly labelled two; accordingly, previously described Roman-domination enumerators for chain graphs are not equivalent. Published Roman \(\{2\}\) enumerators for complete multipartite graphs include the complete-bipartite case but do not determine this result on arbitrary proper nested-neighborhood chain graphs.

## Limitations

The theorem concerns connected chain graphs with the stated canonical decomposition, not general bipartite graphs. The minimum formula is restricted to \(p\ge2\), and the full polynomial may be expensive to write explicitly because it has \(O(n^2)\) distinct bivariate monomials, although it is polynomial-time computable. Literature search cannot exclude unindexed equivalences; the published summaries of some related Roman and Roman \(\{2\}\) enumeration results were accessible without full manuscripts. No external independent mathematical audit has been performed.

## References

1. Pingping Shao and Chengye Zhao, *Counting Weight-k Italian Dominating Sets on Trees and Cycles*, arXiv:2610.00108v1 (September 9, 2026), https://arxiv.org/html/2610.00108v1.
2. N. Padamutham and K. Palagiri, *Complexity of Roman {2}-domination and the double Roman domination in graphs*, 2020, https://doi.org/10.1016/j.akcej.2020.01.005.
