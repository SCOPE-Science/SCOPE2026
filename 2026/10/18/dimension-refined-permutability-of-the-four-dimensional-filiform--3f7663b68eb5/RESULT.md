# Dimension-refined permutability of the four-dimensional filiform Lie algebra

## Finding

Let \(q\) be any prime power, let \(F=\mathbb F_q\), and let \(L\) be the four-dimensional nilpotent Lie algebra with basis \(x,y,z,w\) and nonzero basic brackets
\[
[x,y]=z,\qquad [x,z]=w.
\]
Let \(\mathcal S(L)\) denote **all** Lie subalgebras, including \(0\) and \(L\). Two subalgebras \(A,B\) are *permutable* when their vector-space sum is again a subalgebra, equivalently \([A,B]\subseteq A+B\). Write
\[
D_{a,b}=\#\{(A,B)\in\mathcal S(L)^2:\dim A=a,\ \dim B=b,\ [A,B]\not\subseteq A+B\}.
\]
The complete dimension-refined failure profile is
\[
\begin{aligned}
D_{1,1}&=q^4(q+1)^2,\\
D_{1,2}&=D_{2,1}=q^4(2q+1),\\
D_{2,2}&=q^3(q+1),
\end{aligned}
\]
with \(D_{a,b}=0\) for all other pairs of dimensions \(0\le a,b\le4\). In particular, the bivariate failure enumerator is
\[
\sum_{a,b=0}^{4}D_{a,b}s^a t^b
=q^4(q+1)^2st+q^4(2q+1)(st^2+s^2t)+q^3(q+1)s^2t^2.
\]
The subalgebra lattice has exactly \(N=q^3+3q^2+3q+5\) elements. Therefore its subalgebra commutativity degree, with ordered pairs sampled uniformly from the full subalgebra lattice, is
\[
\boxed{\displaystyle
\mathrm{sd}(L)
=1-\frac{q^3(q^3+6q^2+4q+1)}{(q^3+3q^2+3q+5)^2}
=\frac{11q^4+27q^3+39q^2+30q+25}{(q^3+3q^2+3q+5)^2}.}
\]
For increasing prime powers \(q\), this gives \(\mathrm{sd}(L)\sim 11/q^2\). These are exact statements for *all* finite fields, including characteristic two.

## Assumptions and scope

The Lie bracket is alternating and bilinear, with all unspecified basic brackets zero and reverse brackets obtained by antisymmetry. This is a Lie algebra over every characteristic: its lower central series is \(L\supset [L,L]=\langle z,w\rangle\supset\langle w\rangle\supset0\). In characteristic two, alternating still implies \([a,a]=0\), and the same calculations apply. No restrictions on \(q\) other than being a prime power are imposed.

The probability \(\mathrm{sd}(L)\) is for **subalgebra permutability** \([A,B]\subseteq A+B\), not for elementwise commutativity \([A,B]=0\), not for modular pairs without permutability, and not for adjacency in the comaximal graph (where \(\langle A,B\rangle=L\)). All subalgebras, including \(0\) and \(L\), are counted. The dimensions \(a,b\) are dimensions over \(F\), and \(D_{a,b}\) counts ordered pairs.

## Proof

**1. Classification of subalgebras.** Put \(Z=Fw\), \(D=Fz+Fw\), and let \(\pi:L\longrightarrow L/Z\). The quotient is the three-dimensional Heisenberg Lie algebra \(\overline L\), with center \(F\bar z\). Its subalgebras are the zero space, its \(q^2+q+1\) lines, its \(q+1\) planes (exactly those containing \(F\bar z\)), and the whole space.

A subalgebra containing \(Z\) is the full preimage of a subalgebra of \(\overline L\). Thus there is one such line (\(Z\)), \(q^2+q+1\) such planes, \(q+1\) such hyperplanes, and the whole algebra.

Any line not containing \(Z\) is automatically a subalgebra. If a two-dimensional subalgebra \(U\) does not contain \(Z\), then \(\pi\) restricts injectively to \(U\), and \(\pi(U)\) is a plane of \(\overline L\), hence contains \(F\bar z\). Choosing lifts of \(\bar z\) and a second projective direction, closure of \(U\) forces that direction to have zero \(\bar x\)-coefficient, because \([x,z]=w\notin U\). Consequently \(\pi(U)=F\bar y+F\bar z\), and every such \(U\) has the unique graph description
\[
U=Y_{a,b}:=F(y+aw)+F(z+bw),\qquad a,b\in F.
\]
All \(q^2\) graphs are indeed abelian subalgebras. No three-dimensional subalgebra avoids \(Z\): otherwise its image would be all of \(\overline L\), and brackets of lifts of \(\bar x\) and \(\bar z\) would force \(w\in U\), a contradiction.

Therefore, the numbers of subalgebras in dimensions \(0,1,2,3,4\) are respectively
\[
1,\qquad P=q^3+q^2+q+1,\qquad B=2q^2+q+1,\qquad q+1,\qquad1.
\]
Their sum is \(N=q^3+3q^2+3q+5\). Every hyperplane is the inverse image of a Heisenberg plane; equivalently it contains \(D=[L,L]\), so it is an ideal. The special plane \(D\) itself is an ideal. Every other two-dimensional subalgebra meets \(D\) in a line, by the explicit classification.

**2. Which dimension pairs can fail?** A sum with \(0\) or \(L\) is always a subalgebra. If either subalgebra is a hyperplane, it is an ideal and its sum with any subalgebra is a subalgebra. Accordingly only pairs \((1,1),(1,2),(2,1),(2,2)\) can fail. For two subalgebras, their sum is a subalgebra exactly when their mutual brackets lie in it.

**3. Line–line failures.** Any two distinct lines span a unique vector-space plane, and their sum is a Lie subalgebra precisely when this plane is one of the \(B\) subalgebra planes. Each plane contains exactly \(q+1\) lines, giving \(q(q+1)\) ordered distinct line pairs. Such pairs belonging to different planes cannot overlap, because they determine their span. Hence
\[
D_{1,1}=P(P-1)-Bq(q+1)=q^4(q+1)^2.
\]
Equal lines always permute.

**4. Line–plane failures.** A line contained in a subalgebra plane permutes with it. Otherwise the sum is a three-space. A three-space is a subalgebra exactly when it contains \(D\). Every plane contains \(q+1\) lines, and every three-space contains \(q^2+q+1\) lines.

For the plane \(D\), all lines permute. For every other subalgebra plane \(U\), the sum \(D+U\) is the **unique** hyperplane containing it, because \(\dim(D\cap U)=1\). Of the lines outside \(U\), exactly \(q^2\) lie in this hyperplane; the remaining \(q^3\) produce a non-subalgebra sum. There are \(B-1=2q^2+q\) subalgebra planes distinct from \(D\). Thus
\[
D_{1,2}=q^3(B-1)=q^4(2q+1),\qquad D_{2,1}=D_{1,2}.
\]

**5. Plane–plane failures.** Every subalgebra plane containing \(Z\) is \(X_\ell=\pi^{-1}(\ell)\) for a projective line \(\ell\) in \(\overline L\); here \(X_{F\bar z}=D\), leaving \(q^2+q\) such planes \(X_\ell\ne D\). The remaining planes are the graphs \(Y_{a,b}\), all lying in the abelian hyperplane \(H_0=Fy+Fz+Fw\).

Two graph planes permute, as do a graph plane and any \(X_\ell\): when \(X_\ell\subseteq H_0\) the sum lies in the abelian algebra \(H_0\); otherwise \(X_\ell\cap Y_{a,b}=0\), so their sum is \(L\). The ideal \(D\) also permutes with every subalgebra.

For two distinct \(X_\ell\ne D\), their intersection is \(Z\) and their sum is a three-space. That three-space is a subalgebra exactly when the two corresponding points \(\ell\) of the projective plane \(\mathbb P(\overline L)\) lie on one of the \(q+1\) projective lines through its distinguished center point \(F\bar z\). Each of these projective lines contains exactly \(q\) noncentral points, so among the \(q^2+q\) noncentral points the ordered distinct pairs yielding subalgebras number \((q+1)q(q-1)\). Subtracting from all ordered distinct pairs gives
\[
D_{2,2}=(q^2+q)(q^2+q-1)-(q+1)q(q-1)=q^3(q+1).
\]

**6. Final sum.** Adding the four ordered dimension cells,
\[
\begin{aligned}
\#\{(A,B):[A,B]\not\subseteq A+B\}
&=q^4(q+1)^2+2q^4(2q+1)+q^3(q+1)\\
&=q^3(q^3+6q^2+4q+1).
\end{aligned}
\]
The number of permuting pairs is \(N^2\) minus this expression, namely \(11q^4+27q^3+39q^2+30q+25\). Dividing by \(N^2\) establishes all formulas. The asymptotic follows by comparing leading degrees. \(\square\)

## Verification

The standalone standard-library program `verify.py` enumerates **every vector subspace** of \(F^4\) in reduced row-echelon form, tests closure under the two defining brackets, then evaluates the condition \([A,B]\subseteq A+B\) independently for every ordered pair of resulting subalgebras. It checks all claimed dimension cells, lattice sizes, and numerator formulas, over \(\mathbb F_2\), \(\mathbb F_3\), \(\mathbb F_4\), and \(\mathbb F_5\). Field operations in the nonprime case use the explicit relation \(\alpha^2=\alpha+1\); addition, multiplication, inverses, associativity, and distributivity are checked before enumeration.

With `python3 verify.py`, the successful run reports the following tuples \((q,N,\text{nonpermuting pairs},\text{permuting pairs})\):
\[
(2,31,328,633),\quad(3,68,2538,2086),\quad(4,129,11328,5313),\quad(5,220,37000,11400).
\]
The terminal marker is `VERIFY_OK`. These are finite computational checks of the general argument above, not an induction from four field sizes.

## Relationship to prior work

Muhie, Otera, and Russo (arXiv:2609.19086v1, first posted September 16, 2026) define the same subalgebra-permutability probability and compute it for the three-dimensional Heisenberg algebra and, in odd characteristic, \(\mathfrak{sl}_2\). Their principal exact formulas do not address this four-dimensional class-three algebra or its dimension-pair profile.

Towers, Zuleta, and Gutierrez (arXiv:2608.16575, posted August 17, 2026), Proposition 4.4, enumerate the proper subalgebras of the **same** four-dimensional filiform Lie algebra and describe its comaximal graph. That existing enumeration is expressly credited; the lattice counts are not claimed as new. Comaximal adjacency means \(\langle A,B\rangle=L\), a different predicate from \([A,B]\subseteq A+B\). For example \(A=Fx\) and \(B=Fz\) do **not** permute, because \([x,z]=w\notin A+B\), yet their generated subalgebra is the proper three-space \(Fx+Fz+Fw\), so they are not adjacent in the comaximal graph. The new contribution is the **complete ordered permutability-failure profile and its probability**, not a new list of subalgebras or a recomputation of comaximal graph edges.

The Lie algebra can be related through the Lazard correspondence to exponent-prime group examples in sufficiently large odd characteristics. A possibly equivalent subgroup-permutability enumeration in older group-theoretic literature has not been excluded.

## Limitations

The claim concerns exactly the specified four-dimensional filiform Lie algebra as the field varies. It does not classify permutability degrees of arbitrary four-dimensional Lie algebras or filiform Lie algebras in larger dimensions. Literature searches cannot prove absence of equivalent older group-theoretic or Lie-theoretic formulas. The proofs are self-contained; computational examples only check small fields.

## References

1. S. K. Muhie, D. E. Otera, and F. G. Russo, *On the number of modular pairs in finite dimensional Lie algebras on finite fields*, arXiv:2609.19086v1, September 16, 2026. https://arxiv.org/html/2609.19086
2. D. A. Towers, Y. Zuleta, and I. Gutierrez, *Comaximal Graphs of finite-dimensional Lie algebras over finite fields: Triangle counts and structural invariants*, arXiv:2608.16575, August 17, 2026, Proposition 4.4. https://arxiv.org/abs/2608.16575
