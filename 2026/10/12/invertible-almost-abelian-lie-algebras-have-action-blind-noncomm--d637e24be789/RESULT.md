# Invertible almost-abelian Lie algebras have action-blind noncommuting graphs

## Finding

Let
\[
L_A=\mathbf F_q t\ltimes_A V
\]
be a nonabelian almost-abelian Lie algebra over the finite field \(\mathbf F_q\), where
\[
\dim_{\mathbf F_q}V=n\ge1,
\qquad
A\in\operatorname{GL}(V),
\]
and
\[
[t,v]=A(v),
\qquad
[V,V]=0.
\]
Put
\[
Q=q^n.
\]

Then
\[
Z(L_A)=0
\]
and the element-level noncommuting graph is
\[
\boxed{
\mathcal N(L_A)
\cong
K_{Q-1,\underbrace{q-1,\ldots,q-1}_{Q\text{ parts}}}.
}
\]

Thus the graph is completely independent of the similarity class of the invertible defining operator \(A\).

The unique large part is
\[
V\setminus\{0\},
\]
of size
\[
Q-1.
\]
The remaining \(Q\) parts are the nonzero points of the projective lines in \(L_A\) not contained in \(V\), each of size
\[
q-1.
\]

Consequently,
\[
\boxed{
\alpha(\mathcal N(L_A))=Q-1
}
\]
and
\[
\boxed{
\omega(\mathcal N(L_A))
=
\chi(\mathcal N(L_A))
=
Q+1.
}
\]

The degree distribution is
\[
\boxed{
\deg(x)=
\begin{cases}
Q(q-1),&x\in V\setminus\{0\},\\[4pt]
q(Q-1),&x\in L_A\setminus V.
\end{cases}
}
\]

The graph determines the field size and dimension inside this family:
\[
\boxed{
\mathcal N(L_A)\cong\mathcal N(L_B)
\iff
q_A=q_B
\text{ and }
n_A=n_B.
}
\]

However, it does not determine the Lie algebra. For fixed \(q,n\),
\[
\boxed{
L_A\cong L_B
\iff
A\text{ is similar to }cB
\text{ for some }c\in\mathbf F_q^\times.
}
\]
All invertible \(A\) have the same graph. Hence, for every \(n\ge2\),
\[
L_{I_n}
\not\cong
L_{I_n+E_{12}},
\]
while
\[
\mathcal N(L_{I_n})
\cong
\mathcal N(L_{I_n+E_{12}}).
\]

Finally,
\[
\boxed{
\operatorname{Aut}(\mathcal N(L_A))
\cong
\begin{cases}
S_{q-1}\wr S_{q+1},&n=1,\\[4pt]
S_{Q-1}\times\left(S_{q-1}\wr S_Q\right),&n\ge2.
\end{cases}
}
\]

Thus the graph has a sharp rigidity/blindness split: it recovers \(q\) and \(n\), but forgets the entire projective-similarity class of the invertible almost-abelian action.

## Assumptions and scope

The element-level noncommuting graph has vertex set
\[
L_A\setminus Z(L_A)
\]
and joins two distinct vertices exactly when their Lie bracket is nonzero.

The theorem assumes that the defining endomorphism \(A\) is invertible. Singular almost-abelian actions have nontrivial center and additional commuting fibers.

The graph-isomorphism statement is internal to the invertible almost-abelian family.

## Proof

Every element has a unique form
\[
x=\alpha t+u,
\qquad
\alpha\in\mathbf F_q,\quad u\in V.
\]
For
\[
y=\beta t+v,
\]
the bracket is
\[
[x,y]
=
\alpha A(v)-\beta A(u)
=
A(\alpha v-\beta u).
\]
Since \(A\) is invertible,
\[
[x,y]=0
\iff
\alpha v=\beta u.
\]

If \(x\) is central, commuting with every \(v\in V\) forces \(\alpha=0\), and then commuting with \(t\) forces \(u=0\). Thus
\[
Z(L_A)=0.
\]

If \(\alpha=\beta=0\), then both elements lie in the abelian ideal \(V\), so all of
\[
V\setminus\{0\}
\]
forms one independent part of size
\[
Q-1.
\]

If at least one of \(\alpha,\beta\) is nonzero and the vertices commute, then both are nonzero and
\[
\alpha v=\beta u
\]
says exactly that
\[
(\beta,v)
=
\frac{\beta}{\alpha}(\alpha,u).
\]
Hence two elements outside \(V\) commute exactly when they are nonzero scalar multiples of one another. There are
\[
\frac{q^{n+1}-1}{q-1}
-
\frac{q^n-1}{q-1}
=
Q
\]
projective lines not contained in \(V\), each contributing \(q-1\) vertices. Different parts are pairwise adjacent, proving the graph formula.

The independence number is the largest part size \(Q-1\), and a complete multipartite graph has clique and chromatic number equal to its number of parts, namely \(Q+1\).

A vertex in the large part has degree
\[
(q^{n+1}-1)-(Q-1)=Q(q-1),
\]
while a vertex in a small part has degree
\[
(q^{n+1}-1)-(q-1)=q(Q-1).
\]

The complement graph is
\[
K_{Q-1}\sqcup QK_{q-1}.
\]
For \(n=1\), all \(q+1\) components have size \(q-1\), which determines \(q\). For \(n\ge2\), the unique largest component has size \(Q-1\) and the repeated smaller components have size \(q-1\); hence the graph recovers \(q\), \(Q\), and the unique \(n\) with \(Q=q^n\).

Because \(A\) is invertible,
\[
L_A^2=A(V)=V.
\]
Thus \(V\) is characteristic. Any isomorphism
\[
\phi:L_A\to L_B
\]
restricts to some
\[
P\in\operatorname{GL}(V)
\]
and has
\[
\phi(t)=ct+w
\]
modulo the target \(V\), with \(c\ne0\). Bracket preservation gives
\[
PA=cBP.
\]
Conversely, such a relation defines an isomorphism. Hence
\[
L_A\cong L_B
\iff
A\sim cB.
\]

For \(n\ge2\), \(I_n+E_{12}\) is invertible and nonscalar. No scalar multiple of it is similar to the scalar matrix \(I_n\), giving the displayed nonisomorphic collision.

Automorphisms of a complete multipartite graph are arbitrary permutations within parts together with permutations among equal-sized parts. This gives the stated wreath-product formulas.

## Verification

The included checker constructs the Lie algebra directly over
\[
\mathbf F_2,\quad
\mathbf F_3,\quad
\mathbf F_5
\]
for scalar, Jordan, and nonscalar diagonal invertible actions.

The tested parameter pairs are
\[
(q,n)=(2,1),(2,2),(2,3),(3,2),(5,2).
\]
For every pair of nonzero elements it computes
\[
[x,y]=A(\alpha v-\beta u)
\]
and verifies the claimed multipartite adjacency and degree formulas.

For
\[
(q,n)=(2,2)
\quad\text{and}\quad
(3,2),
\]
the checker exhaustively searches invertible change-of-basis matrices and nonzero scalars and confirms that
\[
I_2
\]
is not proportionally similar to
\[
I_2+E_{12}.
\]

The checker returns `VERIFY_OK`.

Finite computation is not used to prove the theorem.

## Relationship to prior work

Chareh Khah Moghaddam, Erfanian, and Shamsaki introduced the element-level noncommuting graph of a finite-dimensional Lie algebra over a finite field and studied degree, connectivity, diameter, girth, Hamiltonicity, Eulerian behavior, planarity, and graph-isomorphism questions. Their full searchable preprint contains no almost-abelian or complete-multipartite family theorem.

Avetisyan gives a systematic structure and isomorphism theory for almost-abelian Lie algebras over arbitrary fields, representing them through one defining linear operator. That work does not study finite noncommuting graphs.

A later projective noncommuting-graph paper proves that, for centerless commutative-transitive Lie algebras, the projective graph is complete multipartite. This is compatible with the theorem above but does not give the element-level part sizes, the action-independence for every invertible almost-abelian operator, the graph automorphism group, or the exact rigidity/projective-similarity collision statement.

A previous almost-abelian commutativity calculation determines adjoint-rank and centralizer-size distributions from the rank of the defining operator. Equal degree distributions do not determine adjacency, so that calculation does not imply the complete graph decomposition here.

## Limitations

Invertibility is essential. If \(A\) is singular, the center contains \(\ker A\), and the commuting relation has additional fibers.

The graph recovers the field size and dimension only within the stated invertible almost-abelian family.

The later projective complete-multipartite criterion overlaps the qualitative mechanism, but not the element-level classification and action-blind collision theorem.

Failed searches do not prove novelty.

## References

1. Z. Avetisyan, “The structure of almost Abelian Lie algebras,” arXiv:1610.05365v1, first public version 17 October 2016; *International Journal of Mathematics* 33 (2022), article 2250057, DOI 10.1142/S0129167X22500574.
2. A. Chareh Khah Moghaddam, A. Erfanian, and A. Shamsaki, “On the non-commuting graph associated to a finite-dimensional Lie algebra,” arXiv:2406.15902v1, first public version 22 June 2024; later published in *Journal of the Indonesian Mathematical Society* 32 (2026), DOI 10.22342/jims.v32i1.1643. Primary MSC: 17B60.
3. S. Sriwongsa, “Non-commuting graphs of projective spaces over central quotients of Lie algebras,” arXiv:2505.00726v1, first public version 27 April 2025.
