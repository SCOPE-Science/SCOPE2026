# Zero forcing polynomial and minimum rank of proper power graphs of \(C_p^d\times C_q\)

## Finding

Let \(p\ne q\) be odd primes, \(d\ge2\), and \(G=C_p^d\times C_q\). Put \(t=(p^d-1)/(p-1)\). For the proper power graph \(\mathcal P^*(G)\), \[\mathcal Z(\mathcal P^*(G);u)=u^{p^d q-t-3}(u+q-1)(u+q(p-1))^{t-1}\big(u(u+q(p-1))+t(p-1)^2(q-1)\big).\] Consequently \(Z(\mathcal P^*(G))=M(\mathcal P^*(G))=p^d q-t-3\) and the real symmetric minimum rank is \(\operatorname{mr}(\mathcal P^*(G))=t+2\). The minimum zero forcing sets are exactly the complements of white profiles having one white \(q\)-element, one distinguished \(p\)-line with one white order-\(p\) element and one white order-\(pq\) generator, and exactly one white vertex from the order-\(p\)/order-\(pq\) pair of classes on every other \(p\)-line.

The number of minimum zero forcing sets is
\[
t(p-1)^2(q-1)^2\big(q(p-1)\big)^{t-1}.
\]

## Assumptions and scope

Let \(p\ne q\) be odd primes and \(d\ge2\). Write
\[
G=C_p^d\times C_q,
\qquad
t=\frac{p^d-1}{p-1}.
\]
The proper power graph \(\mathcal P^*(G)\) has the nonidentity elements of \(G\) as vertices; two distinct vertices are adjacent exactly when one is a positive power of the other.

The \(t\) one-dimensional subspaces of \(C_p^d\) are denoted \(L_1,\ldots,L_t\). For each \(i\), let \(A_i=L_i\setminus\{0\}\), let \(H_i\) consist of elements whose \(p\)-component is nonzero in \(L_i\) and whose \(q\)-component is nonzero, and let \(C\) be the nonidentity elements of the \(C_q\) factor. Their sizes are
\[
|A_i|=p-1,\qquad |H_i|=(p-1)(q-1),\qquad |C|=q-1.
\tag{1}
\]

## Proof

Every element in \(H_i\) has order \(pq\) and generates the same cyclic subgroup \(L_i\times C_q\). Hence \(A_i\), \(H_i\), and \(C\) are cliques. The only edges between distinct classes are all edges between \(A_i\) and \(H_i\), and all edges between \(H_i\) and \(C\). There are no edges between different \(i\)-branches.

Thus \(C,A_1,H_1,\ldots,A_t,H_t\) are true-twin clique classes. Because both primes are odd, every class has at least two vertices. A zero forcing set can leave at most one white vertex in any such class: two white true twins cannot be separated by a first force.

Assume each class has at most one white vertex. Call branch \(i\) double-white when both \(A_i\) and \(H_i\) contain a white vertex. Every branch with exactly one white class clears immediately using a blue vertex of \(A_i\). After these forces, only double-white branches and a possible white vertex of \(C\) remain.

If no branch is double-white, forcing finishes. If exactly one branch is double-white and \(C\) is blue, a blue vertex of \(C\) forces its white \(H_i\)-vertex and then the white \(A_i\)-vertex is forced. If \(C\) has one white vertex, some other branch is entirely blue because \(t\ge2\); a blue \(H_j\)-vertex first forces the white vertex of \(C\), reducing to the preceding case. If at least two branches are double-white, every blue vertex of \(C\) sees at least two white \(H_i\)-vertices and every blue vertex in a double-white branch sees its two local white vertices, so the process stalls. Therefore
\[
\text{a set is zero forcing exactly when every twin class has at most one white vertex and at most one branch is double-white.}
\tag{2}
\]

Put
\[
a=p-1,\qquad c=q-1,\qquad h=(p-1)(q-1),\qquad s=q(p-1).
\]
The core class contributes \(u^{c-1}(u+c)\). A branch that is not double-white contributes \(u^{s-1}(u+s)\), while a double-white branch contributes \(ah\,u^{s-2}\). By (2),
\[
\begin{aligned}
\mathcal Z(\mathcal P^*(G);u)
&=u^{c-1}(u+c)\left((u^{s-1}(u+s))^t+tah\,u^{s-2}(u^{s-1}(u+s))^{t-1}\right)\\
&=u^{p^d q-t-3}(u+q-1)(u+q(p-1))^{t-1}\\
&\qquad\cdot\big(u(u+q(p-1))+t(p-1)^2(q-1)\big).
\end{aligned}
\tag{3}
\]
Hence
\[
Z(\mathcal P^*(G))=p^d q-t-3,
\tag{4}
\]
and the lowest coefficient is
\[
t(p-1)^2(q-1)^2\big(q(p-1)\big)^{t-1}.
\]
This coefficient counts exactly the white profiles stated in the finding.

For the real symmetric minimum rank, take a real vector space with basis \(e_1,\ldots,e_t,f,g\) and bilinear form with diagonal matrix \(\operatorname{diag}(1,\ldots,1,1,-1)\). Put \(w=f+g\), so \(\langle w,w\rangle=0\) and \(\langle w,f\rangle=1\). Assign \(e_i\) to every vertex of \(A_i\), \(e_i+w\) to every vertex of \(H_i\), and \(f\) to every vertex of \(C\). The resulting Gram matrix has a nonzero off-diagonal entry exactly on the graph edges and rank exactly \(t+2\). Thus
\[
\operatorname{mr}(\mathcal P^*(G))\le t+2.
\]
Since the graph has \(p^d q-1\) vertices, this gives \(M\ge p^d q-t-3\). The standard inequality \(M\le Z\), together with (4), yields
\[
M=Z=p^d q-t-3,
\qquad
\operatorname{mr}=t+2.
\]

## Verification

The accompanying `verify.py` was read from its actual packaged path before replay. For \((p,q,d)=(3,5,2)\) and \((5,3,2)\), it constructs the full class graph and exhausts every representative white profile having at most one white vertex per true-twin class: respectively \(512\) and \(8192\) profiles. Every actual zero forcing closure agrees with criterion (2).

It independently reconstructs the proper power graphs directly from \(C_3^2\times C_5\) and \(C_5^2\times C_3\) by generating every cyclic subgroup and checking power containment for every vertex pair. Every edge agrees with the class decomposition. It also expands the weighted counting formula, checks the minimum coefficient, verifies the complete bilinear-pairing table of the rank witness, and performs a symbolic \(d=3\) check at \((p,q)=(3,5)\).

Exact replay output:

```text
p=3, q=5, d=2: profiles=512, vertices=44, Z=38, min_sets=256000, rank_witness=6, direct_group_graph=OK
p=5, q=3, d=2: profiles=8192, vertices=74, Z=66, min_sets=95551488, rank_witness=8, direct_group_graph=OK
p=3, q=5, d=3: symbolic polynomial and rank witness OK; t=13, Z=119
VERIFY_OK
```

The finite computations corroborate the proof. The arbitrary-parameter statement follows from the cyclic-subgroup decomposition, criterion (2), and the explicit rank witness.

## Relationship to prior work

Tóth gives exact formulas for cyclic subgroups and elements of prescribed order in finite abelian groups. Applied to \(C_p^d\), this supplies the standard count \(t=(p^d-1)/(p-1)\) of order-\(p\) subgroups and the algebraic counting framework used here.

Jafari and Chattopadhyay study structure and spectrum of proper power graphs of direct products when one or both factors are EPO groups. Their public abstract covers the same broad direct-product regime, so the clique decomposition is treated as structural background rather than as the originality claim.

Boyer and coauthors introduce the zero forcing polynomial and derive formulas for several standard graph families. The inspected full text contains no occurrence of “power graph,” “windmill,” or “corona,” and no formula covering this proper-power family was located.

A same-family published comparison computes domination, total domination, and paired domination for \(C_p^d\times C_q\). Those domination parameters do not imply criterion (2), the complete zero forcing polynomial, or the rank-\(t+2\) matrix witness.

## Limitations

Both primes are assumed odd. When \(p=2\) or \(q=2\), some twin classes become singletons and the forcing classification changes.

The theorem concerns the proper power graph, with the identity deleted. No statement is made for higher \(p\)-power exponents.

The public full text of the most directly relevant structure-and-spectrum paper was not available in the inspected sources; its abstract does not advertise zero forcing or minimum rank. A non-advertised incidental forcing computation there remains a residual literature risk.

## References

1. L. Tóth, “On the number of cyclic subgroups of a finite Abelian group,” arXiv:1203.6201, first submitted 28 March 2012; *Bulletin Mathématique de la Société des Sciences Mathématiques de Roumanie* 55(103) (2012), 423–428.
2. S. H. Jafari and S. Chattopadhyay, “Spectrum of proper power graphs of the direct product of certain finite groups,” *Linear and Multilinear Algebra* 70 (2022), 5460–5481. DOI: 10.1080/03081087.2021.1918051.
3. K. Boyer, B. Brimkov, S. English, D. Ferrero, A. Keller, R. Kirsch, M. Phillips, and C. Reinhart, “The zero forcing polynomial of a graph,” arXiv:1801.08910; *Discrete Applied Mathematics* 258 (2019), 35–48.
4. AIM Minimum Rank — Special Graphs Work Group, “Zero forcing sets and the minimum rank of graphs,” *Linear Algebra and its Applications* 428 (2008), 1628–1648.
