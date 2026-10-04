# Three domination parameters of extraspecial noncommuting graphs

## Finding

Let \(G\) be an extraspecial \(p\)-group of order \(p^{1+2n}\), with \(n\ge1\), and let \(\Gamma_G\) be its noncommuting graph on \(G\setminus Z(G)\). Then the ordinary, total, and paired domination numbers all coincide with the symplectic rank: \[\gamma(\Gamma_G)=\gamma_t(\Gamma_G)=\gamma_{\mathrm{pr}}(\Gamma_G)=2n.\] The value is independent of the plus/minus type and, for odd \(p\), independent of whether \(G\) has exponent \(p\) or \(p^2\).

The proof identifies the lower bound with the dimension of the nondegenerate commutator space and shows that a symplectic basis simultaneously gives an ordinary dominating set, a total dominating set, and a paired dominating set.

## Assumptions and scope

An extraspecial \(p\)-group is a finite \(p\)-group \(G\) satisfying
\[
Z(G)=G'=\Phi(G)
\]
and
\[
|Z(G)|=p.
\]
Write
\[
|G|=p^{1+2n},
\qquad n\ge1.
\]
Then
\[
V=G/Z(G)
\]
is a vector space of dimension \(2n\) over \(\mathbb F_p\).

The noncommuting graph \(\Gamma_G\) has vertex set
\[
G\setminus Z(G),
\]
and distinct vertices are adjacent exactly when they do not commute.

A total dominating set requires every vertex, including each selected vertex, to have a selected neighbor. A paired dominating set is a dominating set whose induced subgraph has a perfect matching.

## Proof

Identify \(Z(G)\) additively with \(\mathbb F_p\). Since \(G\) has nilpotency class two, the commutator induces a well-defined alternating bilinear form
\[
B:V\times V\longrightarrow\mathbb F_p,
\qquad
B(xZ(G),yZ(G))=[x,y].
\]
It is nondegenerate: if \(B(xZ(G),v)=0\) for every \(v\in V\), then \(x\) commutes with all of \(G\), hence \(x\in Z(G)\).

Therefore
\[
x\sim y
\iff
B(\bar x,\bar y)\ne0,
\tag{1}
\]
where \(\bar x=xZ(G)\).

### Upper bounds

Choose a symplectic basis
\[
e_1,f_1,\ldots,e_n,f_n
\]
of \(V\), with
\[
B(e_i,f_i)=1
\]
and all other pairings between distinct basis vectors equal to zero. Choose group elements
\[
x_i,y_i\in G\setminus Z(G)
\]
mapping to \(e_i,f_i\).

Let
\[
D=\{x_1,y_1,\ldots,x_n,y_n\}.
\]
For any vertex \(g\), if \(\bar g\) were orthogonal to every basis vector then nondegeneracy would force
\[
\bar g=0,
\]
contrary to \(g\notin Z(G)\). Thus every vertex outside \(D\) is adjacent to some vertex of \(D\), so \(D\) dominates.

Moreover, \(x_i\) is adjacent to \(y_i\) for every \(i\). Hence every selected vertex has a selected neighbor, so \(D\) is total dominating. The edges
\[
x_iy_i,\qquad 1\le i\le n,
\]
form a perfect matching in the induced graph on \(D\). Thus \(D\) is paired dominating.

Consequently,
\[
\gamma(\Gamma_G),
\gamma_t(\Gamma_G),
\gamma_{\mathrm{pr}}(\Gamma_G)
\le 2n.
\tag{2}
\]

### Lower bound

Let \(D\) be any ordinary dominating set and let
\[
W=\operatorname{span}\{\bar d:d\in D\}\le V.
\]
If \(W=V\), then
\[
|D|\ge\dim V=2n.
\]

Assume instead that \(W\ne V\), and put
\[
U=W^\perp.
\]
Then
\[
m=\dim U\ge1.
\]
Every noncentral group element whose image lies in \(U\) commutes with every element of \(D\). Since \(D\) dominates, every such element must itself belong to \(D\).

For each nonzero vector \(u\in U\), its coset in \(G/Z(G)\) contains exactly \(p\) group elements. Hence \(D\) contains at least
\[
p(p^m-1)
\tag{3}
\]
vertices mapping into \(U\).

Because all of those vertices belong to \(D\), their images lie in \(W\), so
\[
U\subseteq W.
\]
Thus
\[
m\le n
\]
and
\[
\dim W=2n-m.
\]
The vectors from \(U\) span only \(m\) dimensions, so at least
\[
(2n-m)-m=2n-2m
\]
additional selected vertices are required to span \(W\). Therefore
\[
|D|
\ge
p(p^m-1)+2n-2m.
\tag{4}
\]
For \(p\ge2\) and \(m\ge1\),
\[
p(p^m-1)\ge 2(2^m-1)\ge 2m.
\]
Equation (4) now gives
\[
|D|\ge2n.
\]
Hence
\[
\gamma(\Gamma_G)\ge2n.
\tag{5}
\]

Since
\[
\gamma(\Gamma_G)\le\gamma_t(\Gamma_G)\le\gamma_{\mathrm{pr}}(\Gamma_G),
\]
the upper bounds in (2) and lower bound in (5) prove
\[
\gamma(\Gamma_G)
=
\gamma_t(\Gamma_G)
=
\gamma_{\mathrm{pr}}(\Gamma_G)
=
2n.
\]

The argument depends only on the nondegenerate alternating commutator form on \(G/Z(G)\). Therefore it is independent of extraspecial type and exponent.

## Verification

The accompanying `verify.py` constructs the exact symplectic blow-up model of the noncommuting graph: each nonzero vector of
\[
\mathbb F_p^{2n}
\]
has \(p\) group-element copies, and two vertices are adjacent exactly when their vectors have nonzero symplectic pairing.

It exhaustively searches ordinary, total, and paired dominating sets in the cases
\[
(p,n)=(2,1),(3,1),(2,2),
\]
whose graphs have \(6\), \(24\), and \(30\) vertices respectively. It also constructs the actual groups \(D_8\) and \(Q_8\) directly from their multiplication laws and checks the ordinary domination value there. Finally, it checks the elementary inequality used in the lower bound over a broad finite grid.

Exact output:

```text
VERIFY_OK
symplectic_model_p=2_n=1: vertices=6 gamma=2 gamma_t=2 gamma_pr=2
symplectic_model_p=3_n=1: vertices=24 gamma=2 gamma_t=2 gamma_pr=2
symplectic_model_p=2_n=2: vertices=30 gamma=4 gamma_t=4 gamma_pr=4
D8_and_Q8_actual_group_checks=gamma_2
lower_bound_inequality_grid=p2..17_m1..12_passed
```

The finite computations are corroborative only. The theorem for all extraspecial \(p\)-groups is proved by the symplectic argument above.

## Relationship to prior work

Chin studied maximal pairwise noncommuting subsets of extraspecial \(p\)-groups, so the same commutator geometry was already known to be useful for extremal questions on these groups. Later finite-\(p\)-group work continued that noncommuting-set program.

Abdollahi, Akbari, and Maimani developed the noncommuting graph of a group as a systematic graph-theoretic object. Vatandoost and Khalili later studied its domination number for finite groups and proved a general upper bound, together with several extremal characterizations. Their full text does not treat extraspecial groups or give the dimension formula above.

The present result is not a clique-number reformulation: maximal pairwise noncommuting sets concern complete subgraphs, whereas domination asks for a set meeting every symplectic orthogonal complement. The lower bound here uses the full orthogonal subspace \(W^\perp\), including the multiplicity of each nonzero quotient vector in the group.

Targeted searches for ordinary domination, total domination, paired domination, extraspecial groups, noncommuting graphs, and symplectic formulations did not locate the three-parameter equality above.

## Limitations

The result is specific to extraspecial groups. More general class-two \(p\)-groups can have degenerate commutator forms, larger centers, or quotient multiplicities that alter the domination problem.

A directly relevant 2005 paper on pairwise noncommuting subsets of extraspecial \(p\)-groups was available through its publisher abstract and bibliographic record, but not as complete readable full text in the inspected access path. The closest full-text domination paper was inspected in full and contains no extraspecial or \(p\)-group specialization.

No claim is made about locating, Roman, independent, or other domination variants.

## References

1. A. Y. M. Chin, “On non-commuting sets in an extraspecial \(p\)-group,” *Journal of Group Theory* 8 (2005), 189–194. DOI: 10.1515/jgth.2005.8.2.189.
2. A. Abdollahi, S. Akbari, and H. R. Maimani, “Non-commuting graph of a group,” *Journal of Algebra* 298 (2006), 468–492. DOI: 10.1016/j.jalgebra.2006.02.015.
3. M. R. Darafsheh, M. Ghorbani, and S. K. Prajapati, “On maximal subsets of pairwise noncommuting elements in finite \(p\)-groups,” *Bulletin of the Australian Mathematical Society* 92 (2015), 380–389. DOI: 10.1017/S0004972715000830.
4. E. Vatandoost and M. Khalili, “Domination number of the non-commuting graph of finite groups,” *Electronic Journal of Graph Theory and Applications* 6 (2018), 228–237. DOI: 10.5614/ejgta.2018.6.2.3.
5. T. W. Haynes and P. J. Slater, “Paired-domination in graphs,” *Networks* 32 (1998), 199–206.
