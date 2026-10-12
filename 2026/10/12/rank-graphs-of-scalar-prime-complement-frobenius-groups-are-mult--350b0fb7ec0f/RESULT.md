# Rank graphs of scalar prime-complement Frobenius groups are multipartite joins

## Finding

Let \(\ell\ge3\) be prime, let \(p\ne\ell\) be prime, put
\[
e=\operatorname{ord}_{\ell}(p),
\qquad
q=p^e,
\]
and choose \(\alpha\in\mathbf F_q^\times\) of order \(\ell\). Let
\[
V=\mathbf F_q^t,
\qquad
t\ge2,
\]
and
\[
G=V\rtimes\langle h\rangle,
\qquad
|h|=\ell,
\]
where \(h\) acts as scalar multiplication by \(\alpha\).

Then
\[
\boxed{d(G)=t+1.}
\]

Let \(\Gamma_{t+1}(G)\) be the fixed-size independence graph whose vertices are the elements of \(G\), with two distinct elements adjacent exactly when they occur together in a generating set of cardinality \(t+1\). The identity is isolated. After deleting it,
\[
\boxed{
\Delta_{t+1}(G)
\cong
K_{\underbrace{q-1,\ldots,q-1}_{(q^t-1)/(q-1)}}
\vee
K_{\underbrace{\ell-1,\ldots,\ell-1}_{q^t}}.
}
\]

The first complete multipartite factor is carried by \(V\setminus\{0\}\): two nonzero kernel elements are adjacent exactly when they are linearly independent over \(\mathbf F_q\). Its parts are the nonzero points of the one-dimensional \(\mathbf F_q\)-subspaces.

The second complete multipartite factor is carried by \(G\setminus V\): two outside elements are adjacent exactly when they lie in distinct conjugates of \(\langle h\rangle\). The \(q^t\) parts are the sets
\[
H^u\setminus\{1\},
\qquad
H=\langle h\rangle,\quad u\in V,
\]
each of size \(\ell-1\).

Every nonzero element of \(V\) is adjacent to every element of \(G\setminus V\). Therefore
\[
\boxed{
\deg(g)=
\begin{cases}
0,&g=1,\\[4pt]
\ell q^t-q,&g\in V\setminus\{0\},\\[4pt]
\ell(q^t-1),&g\in G\setminus V.
\end{cases}
}
\]

Since nonzero kernel elements have order \(p\) and outside elements have order \(\ell\),
\[
\boxed{
|g|\mid\deg_{\Gamma_{d(G)}(G)}(g)
}
\]
for every \(g\in G\). Thus Lucchini's degree-divisibility question has an affirmative answer on a nonnilpotent family with unbounded
\[
d(G)=t+1.
\]

## Assumptions and scope

The graph convention is Lucchini's fixed-size graph: for \(u\ge d(G)\), two distinct elements are adjacent in \(\Gamma_u(G)\) when some generating set of cardinality \(u\) contains both.

The complement order \(\ell\) is an odd prime. The boundary \(\ell=2\) is excluded.

The condition
\[
e=\operatorname{ord}_{\ell}(p)
\]
implies
\[
\mathbf F_p(\alpha)=\mathbf F_q.
\]
Thus one copy of \(\mathbf F_q\), viewed as an \(\mathbf F_p\langle h\rangle\)-module, is irreducible, and \(V\) is the direct sum of \(t\) isomorphic irreducible copies.

## Proof

Write elements as
\[
(v,h^a),
\qquad
v\in V,\quad a\in\mathbb Z/\ell\mathbb Z,
\]
with multiplication
\[
(v,h^a)(w,h^b)
=
(v+\alpha^a w,h^{a+b}).
\]

Take a set
\[
S=\{x_0,x_1,\ldots,x_r\}
\]
containing an element
\[
x_0=(v_0,h^a)
\]
with \(a\ne0\). Since \(1-\alpha^a\ne0\), there is a unique \(u\in V\) such that conjugation by \(u\) sends \(x_0\) to \((0,h^a)\). After applying the same conjugation to the remaining elements, write
\[
x_i=(v_i,h^{b_i}).
\]
Because \(\ell\) is prime, \(a\) is invertible modulo \(\ell\). Choosing
\[
r_i\equiv b_i a^{-1}\pmod\ell
\]
gives
\[
x_i x_0^{-r_i}=(v_i,1).
\]

Hence \(S\) generates \(G\) exactly when the associated vectors \(v_1,\ldots,v_r\) generate \(V\) as an \(\mathbf F_p\langle h\rangle\)-module. Since
\[
\mathbf F_p(\alpha^a)=\mathbf F_q,
\]
this is equivalent to
\[
\operatorname{span}_{\mathbf F_q}\{v_1,\ldots,v_r\}=V.
\]

One generator is needed outside \(V\), and then at least \(t\) associated kernel vectors are needed. Conversely,
\[
h,e_1,\ldots,e_t
\]
generates \(G\) for every \(\mathbf F_q\)-basis \(e_1,\ldots,e_t\) of \(V\). Therefore
\[
d(G)=t+1.
\]

Now let \(0\ne v,w\in V\). They occur together in a minimum generating set exactly when they can be completed to an \(\mathbf F_q\)-basis, which happens exactly when they are linearly independent. Thus the kernel part is complete multipartite with one part for each one-dimensional subspace and part size \(q-1\).

Next take \(0\ne v\in V\) and \(x\in G\setminus V\). Normalize \(x\) into the complement. The vector \(v\) can be extended to a basis with \(t-1\) further vectors, so every such pair is adjacent.

Finally take \(x,y\in G\setminus V\). Normalize \(x\) to
\[
(0,h^a),
\qquad a\ne0,
\]
and write the transformed \(y\) as
\[
(w,h^b).
\]
Cancelling the quotient exponent by a power of \(x\) leaves the kernel vector \(w\). The pair \(x,y\) can be completed to a generating set of size \(t+1\) exactly when \(w\ne0\). The equality \(w=0\) is precisely the condition that \(x\) and \(y\) lie in the same conjugate of \(H\). Frobenius complements intersect trivially, so the \(q^t\) conjugates partition \(G\setminus V\) into parts of size \(\ell-1\).

For \(0\ne v\in V\), the kernel contributes \(q^t-q\) neighbors and the outside part contributes \(q^t(\ell-1)\), giving
\[
\deg(v)=\ell q^t-q.
\]
For \(x\notin V\), all \(q^t-1\) nonzero kernel elements are neighbors, and among outside vertices exactly the \(\ell-1\) elements in its own complement part are nonneighbors. Hence
\[
\deg(x)=\ell(q^t-1).
\]

Finally \(p\mid q\), so
\[
p\mid \ell q^t-q,
\]
and the outside degree is visibly divisible by \(\ell\). This proves the order-divisibility assertion.

## Verification

The included checker reconstructs
\[
G=\mathbf F_4^2\rtimes C_3
\]
directly. It enumerates every three-element subset of the \(48\)-element group, computes the subgroup generated by that triple using the multiplication table, and marks the three pairs occurring in each generating triple. This independently reconstructs \(\Gamma_3(G)\) from its definition.

The resulting degree histogram is
\[
0^1,\qquad
44^{15},\qquad
45^{32},
\]
exactly as predicted by
\[
3\cdot4^2-4=44
\]
and
\[
3(4^2-1)=45.
\]

The checker also verifies the five kernel projective-line parts of size \(3\), the sixteen complement parts of size \(2\), and the predicted adjacency criterion for every unordered pair.

The checker returns `VERIFY_OK`.

Finite computation is not used to prove the infinite family.

## Relationship to prior work

Lucchini introduced the independence graph of a finite group and the fixed-size graphs \(\Gamma_u(G)\). His paper asks whether, for every finite group,
\[
|g|
\]
divides the degree of \(g\) in
\[
\Gamma_{d(G)}(G).
\]
Immediately before that question, the paper notes that the answer is already known when \(d(G)=2\). The family proved here has
\[
d(G)=t+1,
\]
which is unbounded.

Lucchini and Nemmi later introduced the rank graph notation \(\Delta_{d(G)}(G)\) and proved that it is connected whenever \(d(G)\ge3\). Their general theorem does not give a Frobenius specialization or vertex-degree formula.

Related database searches locate a complement-order-two generalized-dihedral theorem and a theorem for nilpotent groups. Neither covers the odd-prime-complement nonnilpotent family here.

The new content is the exact generation criterion, the full multipartite-join graph, and the resulting closed degree formulas.

## Limitations

The complement is assumed to have prime order. For composite cyclic complements, quotient projections can generate collectively without either element alone generating the quotient, so additional arithmetic strata appear.

The kernel module is homogeneous: it is a direct sum of copies of one irreducible scalar module. More general Frobenius modules can have several nonisomorphic constituents.

The theorem resolves the degree-divisibility question only for this family.

Failed searches do not prove novelty.

## References

1. A. Lucchini, “The independence graph of a finite group,” arXiv:2004.14651v1, first public version 30 April 2020; *Monatshefte für Mathematik* 193 (2020), 845–856, DOI 10.1007/s00605-020-01445-0. Primary MSC 20D60.
2. A. Lucchini and D. Nemmi, “On the connectivity of the generating and rank graphs of finite groups,” arXiv:2405.16427v1, first public version 26 May 2024; *Journal of Algebra* 665 (2025), 131–144, DOI 10.1016/j.jalgebra.2024.10.030.
