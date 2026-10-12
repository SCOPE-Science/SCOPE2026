# Zero forcing polynomials recognize mixed finite-field zero-divisor graphs

## Finding

Let \(R\cong\prod_{i=1}^{r}\mathbb F_{q_i}\), where \(r\ge2\), at least one \(q_i=2\), and at least one \(q_i>2\). For every nonempty proper \(S\subset[r]\), put \(w_S=\prod_{i\in S}(q_i-1)\), \(h=2^r-2\), and \(N=\prod_i q_i-\prod_i(q_i-1)-1\). Then the standard zero-divisor graph satisfies \[\mathcal Z(\Gamma(R);u)=u^{N-h}\prod_{\varnothing\ne S\subsetneq[r]}(u+w_S).\] Consequently \(Z(\Gamma(R))=M(\Gamma(R))=N-h\), the real symmetric minimum rank is \(h=2^r-2\), and the minimum zero forcing sets are exactly the complements of one vertex from every nonempty proper support class. Moreover the polynomial recovers the complete unordered multiset \(\{q_1,\ldots,q_r\}\), so within this mixed binary/nonbinary reduced class it determines both the zero-divisor graph and the finite ring up to isomorphism.

The number of minimum zero forcing sets is
\[
\left(\prod_{i=1}^{r}(q_i-1)\right)^{2^{r-1}-1}.
\]

## Assumptions and scope

Let
\[
R\cong\mathbb F_{q_1}\times\cdots\times\mathbb F_{q_r},
\qquad r\ge2,
\]
where at least one factor is \(\mathbb F_2\) and at least one factor has order greater than \(2\).

The standard zero-divisor graph \(\Gamma(R)\) has the nonzero zero-divisors of \(R\) as vertices; distinct vertices are adjacent exactly when their product is zero.

For a vertex \(x=(x_1,\ldots,x_r)\), write
\[
\operatorname{supp}(x)=\{i:x_i\ne0\}.
\]
For each nonempty proper \(S\subset[r]\), let
\[
T_S=\{x:\operatorname{supp}(x)=S\}.
\]

## Proof

Put
\[
a_i=q_i-1.
\]
The support class \(T_S\) has size
\[
w_S=|T_S|=\prod_{i\in S}a_i.
\tag{1}
\]
Every nonzero zero-divisor has a nonempty proper support, and two vertices are adjacent exactly when their supports are disjoint:
\[
x\sim y
\quad\Longleftrightarrow\quad
\operatorname{supp}(x)\cap\operatorname{supp}(y)=\varnothing.
\tag{2}
\]
Thus the graph is a weighted blow-up of the Boolean disjointness graph on the
\[
h=2^r-2
\]
nonempty proper subsets. Its order is
\[
N=\sum_{\varnothing\ne S\subsetneq[r]}w_S
=
\prod_i q_i-\prod_i(q_i-1)-1.
\tag{3}
\]

Each \(T_S\) is an independent false-twin class. Hence a zero forcing set can leave at most one white vertex in each class with \(w_S\ge2\); a singleton class automatically satisfies the same bound.

It remains to prove that every coloring leaving at most one white vertex in every support class is forcing, despite the singleton classes created by binary field factors.

Let
\[
B=\{i:q_i=2\}.
\]
A class \(T_S\) is a singleton exactly when
\[
S\subseteq B.
\]
Because the product is mixed, \(B\ne[r]\).

First suppose some white vertex lies in a singleton class. Choose such a white support \(S\subseteq B\) minimal by inclusion. The complementary support
\[
S^c=[r]\setminus S
\]
contains every nonbinary coordinate, so
\[
w_{S^c}\ge2.
\]
Therefore \(T_{S^c}\) contains a blue vertex even if it also contains its one allowed white representative.

A white support \(U\) is adjacent to \(S^c\) precisely when
\[
U\cap S^c=\varnothing,
\]
equivalently
\[
U\subseteq S.
\]
Minimality of \(S\) makes its white representative the unique white neighbor of a blue vertex in \(T_{S^c}\), so it is forced. Repeating removes all white singleton classes.

Now suppose white vertices remain only in classes of size at least \(2\). Choose an inclusion-minimal white support \(T\). The complementary class \(T_{T^c}\) supplies a blue vertex: if it has size at least \(2\), one representative remains blue; if it is a singleton, its possible white representative was removed in the first stage. Again, the white neighbors of a vertex in \(T_{T^c}\) are exactly the white supports contained in \(T\), so minimality leaves only \(T\). Hence the white representative of \(T_T\) is forced. Iteration finishes the process.

Therefore the zero forcing sets are exactly the sets that contain all but at most one vertex from every support class. A class of size \(w_S\) contributes
\[
u^{w_S}+w_Su^{w_S-1}
=
u^{w_S-1}(u+w_S).
\]
Multiplying over all support classes gives
\[
\mathcal Z(\Gamma(R);u)
=
u^{N-h}
\prod_{\varnothing\ne S\subsetneq[r]}(u+w_S).
\tag{4}
\]
The least exponent is
\[
Z(\Gamma(R))=N-h.
\tag{5}
\]
A minimum set omits one vertex from every class, giving
\[
\prod_{\varnothing\ne S\subsetneq[r]}w_S
=
\left(\prod_i(q_i-1)\right)^{2^{r-1}-1}.
\tag{6}
\]

For minimum rank, let \(A_r\) be the \(h\times h\) adjacency matrix of the Boolean disjointness graph on nonempty proper subsets. The full disjointness matrix on all subsets is
\[
D_r=
\begin{pmatrix}
1&1\\
1&0
\end{pmatrix}^{\otimes r}.
\]
Its determinant is \(1\). Ordering the subsets as the empty set, then all nonempty proper subsets, then \([r]\), expansion first along the row indexed by \([r]\) and then along the resulting last column gives
\[
\det D_r=-\det A_r.
\]
Thus
\[
\det A_r=-1.
\tag{7}
\]

Let \(X\) be the vertex-by-support incidence matrix. Then
\[
XA_rX^{\mathsf T}
\]
has exactly the off-diagonal zero pattern of \(\Gamma(R)\). Every support class is nonempty, so \(X\) has full column rank, and (7) gives a rank-\(h\) symmetric graph-pattern matrix. Hence
\[
\operatorname{mr}(\Gamma(R))\le h.
\]
The standard inequality
\[
M(G)\le Z(G)
\]
and (5) imply
\[
\operatorname{mr}(\Gamma(R))
=
N-M(\Gamma(R))
\ge
N-Z(\Gamma(R))
=
h.
\]
Therefore
\[
\operatorname{mr}(\Gamma(R))=h,
\qquad
M(\Gamma(R))=Z(\Gamma(R))=N-h.
\tag{8}
\]

Finally, the nonzero root magnitudes of (4) are the multiset
\[
\mathcal P=
\left\{
\prod_{i\in S}(q_i-1):
\varnothing\ne S\subsetneq[r]
\right\}.
\tag{9}
\]
The number of roots with multiplicity is \(2^r-2\), so \(r\) is recovered.

Put
\[
P=\prod_i(q_i-1).
\]
Each factor \(q_i-1\) occurs in exactly \(2^{r-1}-1\) proper nonempty subset products, hence
\[
\prod_{x\in\mathcal P}x
=
P^{2^{r-1}-1}.
\tag{10}
\]
Thus \(P\) is recovered exactly. Add one copy of \(1\) and one copy of \(P\) to (9); the resulting multiset consists of all \(2^r\) subset products of the integers \(q_i-1\).

If exactly \(t\) field factors have order \(2\), then exactly \(t\) of these integers equal \(1\), and the subset product \(1\) occurs with multiplicity
\[
2^t.
\]
Thus \(t\) is recovered. Dividing every subset-product multiplicity by \(2^t\) leaves the complete subset-product multiset of the factors greater than \(1\).

Those remaining factors are recovered greedily, with multiplicity. After some factors have been recovered, remove all subset products generated by them. The smallest unexplained product is the next smallest unrecovered factor, since every product involving an unrecovered factor is at least that factor and the factor itself occurs. Induction reconstructs all \(q_i-1\), hence all \(q_i\).

A finite field is determined up to isomorphism by its order, so the polynomial determines \(R\), and therefore \(\Gamma(R)\), up to isomorphism within this mixed class.

## Verification

The accompanying `verify.py` was read from its packaged path before replay.

It exhausts every at-most-one-white support profile for
\[
(2,3),\ (2,2,3),\ (2,3,3),\ (2,2,2,3),\ (2,2,3,5),
\]
including all \(16384\) profiles in each tested four-factor case.

The Boolean disjointness quotient rank is checked exactly over the rationals through six field factors.

The entire zero forcing polynomial is exhaustively enumerated at the vertex level for
\[
(2,3),\quad(2,2,3),\quad(2,3,3),\quad(2,2,5),
\]
and agrees with (4).

Direct multiplication in products of prime fields checks the support adjacency rule independently for
\[
(2,3),\quad(2,2,3),\quad(2,3,5).
\]
The polynomial-root reconstruction is replayed on repeated and unequal field orders, including a factor of order \(4\).

The checker also verifies the sharp pure-binary boundary:
\[
\Gamma(\mathbb F_2\times\mathbb F_2)=K_2,
\]
whose polynomial is
\[
2u+u^2,
\]
not the product predicted by (4).

Exact replay output:

```text
profile theorem (2, 3): 4 profiles
profile theorem (2, 2, 3): 64 profiles
profile theorem (2, 3, 3): 64 profiles
profile theorem (2, 2, 2, 3): 16384 profiles
profile theorem (2, 2, 3, 5): 16384 profiles
quotient rank r=2: 2
quotient rank r=3: 6
quotient rank r=4: 14
quotient rank r=5: 30
quotient rank r=6: 62
full polynomial (2, 3): N=3, Z=1, coeff_min=2
full polynomial (2, 2, 3): N=9, Z=3, coeff_min=8
full polynomial (2, 3, 3): N=13, Z=7, coeff_min=64
full polynomial (2, 2, 5): N=15, Z=9, coeff_min=64
direct product (2, 3): vertices=3
direct product (2, 2, 3): vertices=9
direct product (2, 3, 5): vertices=21
recover (2, 3): r=2, binary=1, unit_product=2, fields=(2, 3)
recover (2, 2, 3): r=3, binary=2, unit_product=2, fields=(2, 2, 3)
recover (2, 3, 5): r=3, binary=1, unit_product=8, fields=(2, 3, 5)
recover (2, 2, 3, 4): r=4, binary=2, unit_product=6, fields=(2, 2, 3, 4)
recover (2, 2, 2, 3, 5): r=5, binary=3, unit_product=8, fields=(2, 2, 2, 3, 5)
pure binary boundary F2xF2: {1: 2, 2: 1}
VERIFY_OK
```

The finite checks corroborate the arbitrary-\(r\) proof but do not replace the two-stage support forcing argument, unimodularity proof, or multiset reconstruction.

## Relationship to prior work

Anderson and Livingston introduced the standard zero-divisor graph on nonzero zero-divisors. Anderson and Badawi later studied its ring-theoretic structure; their article lists \(13A15\) as primary Mathematics Subject Classification.

Anderson, Levy, and Shapiro studied zero-divisor graphs of von Neumann regular rings and Boolean algebras, providing foundational reduced-ring context.

Gaded and Narayana study exactly the zero-divisor graphs of direct products of finite fields. Their full article determines order, girth, diameter, planarity, total domination, and connected domination. It explicitly gives
\[
|V(\Gamma(R))|
=
\prod_i|F_i|-\prod_i(|F_i|-1)-1
\]
and the complete-bipartite two-factor description. A full-text search found no occurrence of “zero forcing.”

General zero forcing polynomial theory provides the counting invariant, and general minimum-rank theory provides \(M(G)\le Z(G)\). Neither supplies the mixed singleton-class support forcing theorem or the inverse recovery of all field orders from the polynomial.

The mixed hypothesis is essential. When every factor is binary, support classes are all singletons and the factorization can fail already for \(\mathbb F_2\times\mathbb F_2\). When no factor is binary, there are no singleton support classes; the present result isolates and resolves the intermediate regime in which both kinds occur.

## Limitations

The theorem is restricted to finite direct products of fields having at least one binary and at least one nonbinary factor.

The all-binary case requires a different forcing analysis and is explicitly excluded.

The all-nonbinary case has no singleton support classes and is not the new boundary addressed here.

Minimum rank is over real symmetric graph-pattern matrices.

The polynomial determines the ring only within the stated finite reduced product-of-fields class.

## References

1. D. F. Anderson and P. S. Livingston, “The Zero-Divisor Graph of a Commutative Ring,” *Journal of Algebra* 217 (1999), 434–447. DOI: 10.1006/jabr.1998.7840.
2. D. F. Anderson and A. Badawi, “On the Zero-Divisor Graph of a Ring,” *Communications in Algebra* 36 (2008), 3073–3092. DOI: 10.1080/00927870802110888. Published online 22 August 2008.
3. D. F. Anderson, R. Levy, and J. Shapiro, “Zero-Divisor Graphs, von Neumann Regular Rings, and Boolean Algebras,” *Journal of Pure and Applied Algebra* 180 (2003), 221–241. DOI: 10.1016/S0022-4049(02)00250-5.
4. S. M. Gaded and N. S. Narayana, “On zero divisors graphs of direct product of finite fields,” *Journal of Computational Mathematica* 7 (2023), 100–109. DOI: 10.26524/cm165. Published online 19 June 2023.
5. K. Boyer, B. Brimkov, S. English, D. Ferrero, A. Keller, R. Kirsch, M. Phillips, and C. Reinhart, “The zero forcing polynomial of a graph,” *Discrete Applied Mathematics* 258 (2019), 35–48. arXiv:1801.08910.
6. AIM Minimum Rank — Special Graphs Work Group, “Zero forcing sets and the minimum rank of graphs,” *Linear Algebra and its Applications* 428 (2008), 1628–1648. DOI: 10.1016/j.laa.2007.10.009.
