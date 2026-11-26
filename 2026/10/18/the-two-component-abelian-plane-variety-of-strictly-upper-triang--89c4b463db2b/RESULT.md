# Four components of the elementary two-plane variety in the four-by-four triangular Lie algebra in characteristic three

## Finding

Let \(k\) have characteristic three and let \(L=\mathfrak u_4(k)\) be the Lie algebra of strictly upper-triangular four-by-four matrices with the restricted operation given by ordinary matrix cubing. The reduced variety \(\mathbb E(2,L)_{\mathrm{red}}\) of two-dimensional elementary subalgebras has exactly four geometrically irreducible components: a five-dimensional component of planes in a Heisenberg subalgebra and three four-dimensional components described below. Over every finite field of characteristic three its point count is
\[
\#\mathbb E(2,L)(\mathbb F_q)=q^5+4q^4+3q^3+q^2+q+1.
\]
In characteristic at least five the restricted condition instead imposes no cut on the abelian-plane variety; the ordinary two-component geometry is the baseline, not a new claim here.

## Assumptions and scope

An elementary two-plane is an abelian two-dimensional linear subspace of \(L\) all of whose elements have zero restricted power. All component and closure statements concern reduced geometric support, not a nonreduced defining scheme. Write
\[
a=E_{12},\quad b=E_{23},\quad c=E_{34},\quad d=E_{13},\quad e=E_{24},\quad f=E_{14}.
\]
Set \(D=[L,L]=\langle d,e,f\rangle\), \(V=L/D\), \(H=\langle a,c,d,e,f\rangle\), and let \(\pi:L\to V\) be the quotient. When used for projective coordinates in \(V\), \(a,b,c\) denote their classes there.

## Proof

For vectors \(x,y\) spanning a plane \(W\), let \(p_{ij}=x_i y_j-x_j y_i\). Matrix multiplication gives
\[
[x,y]=p_{ab}d+p_{bc}e+(p_{ae}-p_{cd})f,
\qquad x^3=x_a x_b x_c f.
\]
For an abelian plane with \(\dim\pi(W)=2\), the equations \(p_{ab}=p_{bc}=0\) force \(p_{ac}\ne0\). The vector of two \(b\)-coordinates is then proportional to the vectors of both \(a\)- and \(c\)-coordinates, so it is zero. Thus \(W\subset H\) and its cube condition is automatic. Rank-zero planes lie in \(D\subset H\).

**Planes in \(H\).** The bracket on \(H/kf\) is a nondegenerate alternating form, with pairings between \(a,e\) and \(d,c\). Abelian planes in \(H\) not containing \(kf\) are lifts of Lagrangians in that four-space, forming a rank-two vector bundle over the irreducible three-dimensional Lagrangian Grassmannian. Every abelian \(\langle f,w\rangle\) belongs to its closure: choose a vector \(z\) commuting with \(w\) and independent of \(w\) modulo \(kf\), and use \(\langle w,f+t z\rangle\). All of these planes are elementary because their \(b\)-coordinates are zero. This gives an irreducible closed locus of dimension five.

**Rank-one incidence.** Such a plane determines \(ku=\pi(W)\) and \(kv=W\cap D\), both lines. The necessary and sufficient equations are
\[
u_a v_e-u_c v_d=0,\qquad u_a u_b u_c=0.
\]
The first is the bracket of a lift of \(u\) with \(v\). The second follows from the cube formula, since the image of every element of \(W\) is a multiple of \(u\). Using the fixed splitting \(L=\langle a,b,c\rangle\oplus D\), the choices for \(W\) over \(([u],[v])\) are precisely graphs of linear maps \(ku\to D/kv\) in \(\pi^{-1}(ku)/kv\), lifted to \(L\). These form a rank-two vector bundle over each incidence base.

If \(u_b=0\), the plane is already in \(H\). The remaining rank-one planes belong to the three families whose bases and rank-one equations are
\[
\begin{array}{c|c}
\text{projection direction} & \text{line in }D\\ \hline
[u]=[b]&[v]\in\mathbb P(D)\\
u_a=0&v_d=0\\
u_c=0&v_e=0.
\end{array}
\]
Indeed on the line \(u_a=0\) away from \([b]\), one has \(u_c\ne0\) and hence \(v_d=0\); the line \(u_c=0\) gives the symmetric alternative. The last two bases are each \(\mathbb P^1\times\mathbb P^1\) including their indicated fiber at \([b]\), and the first base is \(\mathbb P^2\). Thus the closures of their bundles are irreducible of dimension four. Each rank-zero plane lies in each of these closures: choose \(v\ne0\) in \(W\cap\langle e,f\rangle\) or \(W\cap\langle d,f\rangle\) for the last two families, or any \(v\in W\setminus0\) for the first, complete to a basis \((v,w)\), and specialize \(\langle v,w+t u\rangle\) using any allowed projection direction for that family.

These closures and the planes in \(H\) exhaust the elementary variety. None is contained in another. On the rank-one stratum the displayed base conditions are closed and thus remain necessary there upon taking closures. In particular \(\langle b,d+e\rangle\), \(\langle b+c,e\rangle\), and \(\langle b+a,d\rangle\) are witnesses for the three fourfolds respectively, all outside \(H\) and outside the other two families. The plane \(\langle a,c\rangle\) has rank-two projection and cannot be in any of those closures. The proof works over an algebraic closure, so these are the asserted geometric components.

**Counting over \(\mathbb F_q\).** Rank zero contributes \(q^2+q+1\). At rank one there are \(3(q+1)-3=3q\) projective directions satisfying the cube condition, since the three coordinate lines meet at three distinct points. The direction \([b]\) allows \(q^2+q+1\) lines in \(D\); each of the other \(3q-1\) directions allows \(q+1\). The incidence base therefore has \(4q^2+3q\) points, each admitting \(q^2\) lifts. At rank two there are six lift coordinates over \(\langle a,c\rangle\) and one independent linear bracket equation, so there are \(q^5\) elementary planes. These three disjoint contributions give the polynomial in the Finding.

## Relationship to prior work

Goodwin and Röhrle [1, Theorem 1.1 and §3.3] give the two nine-dimensional commuting-pair components in type \(A_3\) in characteristic zero. The all-characteristic pair case is also covered by [2,3]. Restricting to independent pairs gives the \(\mathrm{GL}_2\) frame bundle of the ordinary abelian-plane variety. Dependent pairs have dimension at most seven, so restriction and passage to the base give two five-dimensional plane components. Likewise [3]'s pair count gives the plain abelian-plane point count after subtracting dependent pairs and dividing by \(|\mathrm{GL}_2(\mathbb F_q)|\); in odd characteristic the branching matrix of [4, Theorem 6.1] already gives the pair count. The ordinary component count and plane polynomial are not claimed as new. For restricted powers in characteristic at least five, \(x^4=0\) makes the restricted cut vacuous. The present computation describes the characteristic-three cut, its component geometry and its own point polynomial. Carlson, Friedlander and Pevtsova [5] give the general elementary-variety setup and the smaller \(\mathfrak u_3\) example. No conclusion about characteristic-two elementary planes or nonreduced schemes is made.

## Verification

The proof is by explicit rank stratification, incidence bundles and limits, so the finite-field expression applies over all extensions of characteristic three. The bundled `verify.py` can be inspected for a finite RREF comparison: in \(\mathbb F_3\) there are 13, 405 and 243 elementary planes in projection ranks zero, one and two, respectively. The finite check does not establish geometric irreducibility or the extension formula.

## References

1. S. Goodwin and G. Röhrle, *On commuting varieties of nilradicals of Borel subalgebras of reductive Lie algebras*, [arXiv:1209.1289](https://arxiv.org/abs/1209.1289).
2. *Irreducible components of commuting tuples in the four-strand unitriangular group*, [Resultary 40c40428c8f0](https://github.com/Resultary/2026/blob/main/2026/10/13/SCOPE-irreducible-components-of-commuting-tuples-in-the-four-strand-un--40c40428c8f0/RESULT.md).
3. *A three-component transition for commuting tuples in the four-by-four triangular nilradical*, [Resultary 0700d390a0aa](https://github.com/Resultary/2026/blob/main/2026/11/2/SCOPE-a-three-component-transition-for-commuting-tuples-in-the-four-by--0700d390a0aa/RESULT.md).
4. U. Kaur, U. Sharma, A. Singh, *Branching Rules and Commuting Probabilities for Triangular and Unitriangular Matrices*, [arXiv:2006.01493](https://arxiv.org/abs/2006.01493).
5. J. F. Carlson, E. M. Friedlander, J. Pevtsova, *Elementary subalgebras of Lie algebras*, [arXiv:1207.5898](https://arxiv.org/abs/1207.5898).
