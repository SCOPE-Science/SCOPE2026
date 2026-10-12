# Resolving and determining sets in extraspecial noncommuting graphs

## Finding

Let \(G\) be an extraspecial \(p\)-group of order \(p^{1+2n}\), with \(p\) prime and \(n\ge1\). Put
\[
v=\frac{p^{2n}-1}{p-1},
\qquad
s=p(p-1),
\]
and let \(\Gamma_G\) be the noncommuting graph on \(G\setminus Z(G)\).

The \(v\) sets of elements whose images in \(G/Z(G)\) span the same projective point are exactly the maximal false-twin classes of \(\Gamma_G\), and every class has size \(s\).

A set of vertices is resolving if and only if it is determining if and only if it contains at least \(s-1\) vertices from every one of these classes. Hence
\[
\beta(\Gamma_G)
=
\operatorname{Det}(\Gamma_G)
=
v(s-1)
=
\frac{p^{2n}-1}{p-1}\bigl(p(p-1)-1\bigr).
\]

If
\[
\mathcal R_{\Gamma_G}(x)=\sum_{S\text{ resolving}}x^{|S|}
\]
is the resolving polynomial, and
\[
\mathcal D_{\Gamma_G}(x)=\sum_{S\text{ determining}}x^{|S|}
\]
is the analogous determining-set size enumerator, then
\[
\mathcal R_{\Gamma_G}(x)
=
\mathcal D_{\Gamma_G}(x)
=
(sx^{s-1}+x^s)^v
=
x^{v(s-1)}(s+x)^v.
\]
In particular, the metric bases and the minimum determining sets are the same family, and there are exactly
\[
s^v
\]
of them.

## Assumptions and scope

An extraspecial \(p\)-group satisfies
\[
Z(G)=G'=\Phi(G),
\qquad |Z(G)|=p.
\]
Thus
\[
V=G/Z(G)
\]
is a \(2n\)-dimensional vector space over \(\mathbb F_p\). After identifying the cyclic center with the additive group of \(\mathbb F_p\), the commutator induces a nondegenerate alternating bilinear form
\[
B:V\times V\longrightarrow\mathbb F_p.
\]
For noncentral \(x,y\in G\),
\[
xy=yx
\quad\Longleftrightarrow\quad
B(xZ(G),yZ(G))=0.
\]

The statement covers both extraspecial types when two types exist. It depends only on the commutator geometry, not on the exponent or plus/minus type.

## Proof

For each projective point \(P\) of \(\operatorname{PG}(V)\), define
\[
C_P=\{x\in G\setminus Z(G):xZ(G)\in P\setminus\{0\}\}.
\]
There are
\[
v=\frac{p^{2n}-1}{p-1}
\]
projective points. Each contains \(p-1\) nonzero quotient vectors, and every quotient vector has exactly \(p\) lifts in \(G\), so
\[
|C_P|=p(p-1)=s.
\]

If \(x,y\in C_P\), then their quotient vectors are scalar multiples. Alternation of \(B\) gives
\[
B(xZ(G),yZ(G))=0,
\]
so \(C_P\) is an independent set. For a vertex outside \(C_P\), adjacency to any element of \(C_P\) depends only on whether its quotient point is nonorthogonal to \(P\). Hence all vertices in \(C_P\) have the same open neighborhood.

These false-twin classes are maximal. If \(P\ne Q\), then nondegeneracy gives distinct hyperplanes
\[
P^\perp\ne Q^\perp.
\]
Choose a projective point \(R\) in their symmetric difference. Every vertex of \(C_R\) is adjacent to all vertices in exactly one of \(C_P,C_Q\). Thus vertices from different classes do not have identical neighborhoods.

The graph has diameter two. If two vertices are not adjacent and lie over points \(P,Q\), choose a vector outside
\[
P^\perp\cup Q^\perp.
\]
Such a vector exists because one or two proper hyperplanes do not cover a finite vector space; if \(P=Q\), one proper hyperplane already suffices. A nonzero lift is adjacent to both vertices.

Now let \(S\) be a resolving set. If two vertices of one class \(C_P\) were omitted, they would have identical distances to every vertex of \(S\), because they are false twins. Therefore
\[
|S\cap C_P|\ge s-1
\]
for every \(P\).

Conversely, suppose \(S\) contains at least \(s-1\) vertices from every class. The only vertices needing comparison are the at most one omitted vertex from each class. Let \(u_P,u_Q\) be omitted vertices from distinct classes.

If \(P\) and \(Q\) are nonorthogonal, take a selected vertex \(z\in C_P\). Then
\[
d(u_P,z)=2,
\qquad
d(u_Q,z)=1.
\]
If \(P\) and \(Q\) are orthogonal, choose \(R\) in the symmetric difference of \(P^\perp\) and \(Q^\perp\), and take a selected vertex \(z\in C_R\). Again the two distances are \(1\) and \(2\). Thus \(S\) resolves \(\Gamma_G\).

For determining sets, the same lower bound is forced by symmetry: if two vertices of one \(C_P\) are omitted, their transposition is a nonidentity graph automorphism fixing \(S\) pointwise.

Conversely, if \(S\) contains at least \(s-1\) vertices from each class, then it contains at least one vertex from each class because \(s\ge2\). Any automorphism fixing \(S\) pointwise preserves the maximal twin equivalence relation. A fixed selected vertex in \(C_P\) forces \(C_P\) itself to be preserved setwise, and then the possible unique omitted vertex in that class is also fixed. Thus every vertex is fixed, so \(S\) is determining.

Therefore resolving sets and determining sets coincide exactly. For one twin class the permitted choices contribute
\[
sx^{s-1}+x^s,
\]
because one may omit exactly one of its \(s\) vertices or omit none. The choices are independent over all \(v\) classes, which gives
\[
\mathcal R_{\Gamma_G}(x)
=
\mathcal D_{\Gamma_G}(x)
=(sx^{s-1}+x^s)^v.
\]
The minimum degree is \(v(s-1)\), and its coefficient is \(s^v\), proving all stated formulas.

## Verification

The accompanying `verify.py` was inspected at its packaged path and replayed.

It constructs the projective symplectic quotient for
\[
(p,n)=(2,1),(3,1),(2,2),(3,2),(5,2),
\]
checks the number and size of projective fibers, and verifies the separation property used in the proof.

It also constructs the Heisenberg extraspecial group directly for \(p=2,3,5\), forms its noncommuting graph from the group law, recovers the predicted maximal false-twin partition, and verifies a canonical minimum resolving set. For the six-vertex case \(p=2,n=1\), it exhaustively tests all vertex subsets and obtains
\[
8x^3+12x^4+6x^5+x^6=(2x+x^2)^3.
\]

Exact replay output:

```text
p=2, n=1: projective classes=3, class_size=2, vertices=6, beta=Det=3, bases=8
p=3, n=1: projective classes=4, class_size=6, vertices=24, beta=Det=20, bases=1296
p=2, n=2: projective classes=15, class_size=2, vertices=30, beta=Det=15, bases=32768
p=3, n=2: projective classes=40, class_size=6, vertices=240, beta=Det=200, bases=13367494538843734067838845976576
p=5, n=2: projective classes=156, class_size=20, vertices=3120, beta=Det=2964, bases=91343852333181432387730302044767688728495783936000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
Heisenberg p=2: actual group twin partition and resolving basis OK
Heisenberg p=3: actual group twin partition and resolving basis OK
Heisenberg p=5: actual group twin partition and resolving basis OK
p=2, n=1 exhaustive resolving polynomial: {3: 8, 4: 12, 5: 6, 6: 1}
VERIFY_OK
```

The finite checks corroborate the proof. The arbitrary-rank theorem follows from the nondegenerate symplectic commutator form and the twin-class argument, not from enumeration.

## Relationship to prior work

Chin studied maximum pairwise noncommuting sets in extraspecial \(p\)-groups. That work concerns clique-type extremal subsets rather than resolving or determining sets.

Abdollahi, Akbari, and Maimani introduced the modern noncommuting graph and developed structural questions about how the graph reflects the group. Abdollahi, Akbari, Dorbidi, and Shahverdi later proved order recognition for finite nonabelian \(p\)-groups and placed this graph explicitly in finite-group theory.

Tolue introduced the twin noncommuting graph and studied metric dimension. The inspected metric-dimension section proves, among other results, that metric dimension three occurs exactly for \(S_3,D_8,Q_8\), and gives general bounds and special cases. The present theorem agrees at the boundary \(D_8,Q_8\), where it gives \(3\), but supplies an exact all-rank extraspecial formula, a characterization of every resolving set, an exact resolving polynomial, and the parallel determining-set theorem.

Searches under extraspecial, symplectic, twin, resolving, metric-dimension, determining-set, and resolving-polynomial formulations did not locate this all-rank statement. Closest same-family results concern domination, pairwise noncommuting sets, or cyclic-subgroup commutativity rather than distance resolution or pointwise graph bases.

## Limitations

The theorem is for extraspecial groups, not arbitrary special or generalized extraspecial groups. The argument uses the fact that the center has order \(p\) and that the commutator form on \(G/Z(G)\) is nondegenerate.

The polynomial enumerates resolving sets by cardinality; it does not enumerate ordered resolving sequences.

The determining-set enumerator is defined here explicitly as the cardinality generating function of determining sets; no claim is made about competing terminology for that enumerator.

## References

1. A. Y. M. Chin, “On non-commuting sets in an extraspecial p-group,” *Journal of Group Theory* 8 (2005), 189–194. DOI: 10.1515/jgth.2005.8.2.189.
2. A. Abdollahi, S. Akbari, and H. R. Maimani, “Non-commuting graph of a group,” *Journal of Algebra* 298 (2006), 468–492. DOI: 10.1016/j.jalgebra.2006.02.015.
3. A. Abdollahi, S. Akbari, H. Dorbidi, and H. Shahverdi, “Commutativity pattern of finite non-abelian p-groups determine their orders,” arXiv:1109.5007, first submitted 23 September 2011; DOI: 10.1080/00927872.2011.627075.
4. B. Tolue, “The twin non-commuting graph of a group,” *Rendiconti del Circolo Matematico di Palermo* 69 (2020), 591–599. DOI: 10.1007/s12215-019-00421-4.
