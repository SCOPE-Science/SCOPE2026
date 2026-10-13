# The eight Rota–Baxter operators on \(S_3\)

## Finding

Let
\[
S_3=\langle r,s\mid r^3=s^2=e,\ srs=r^{-1}\rangle.
\]

A group Rota–Baxter operator of weight \(1\) is a set map
\[
B:S_3\to S_3
\]
satisfying
\[
B(g)B(h)
=
B\!\left(gB(g)hB(g)^{-1}\right)
\]
for every \(g,h\in S_3\).

There are exactly
\[
\boxed{8}
\]
such operators.

Two are the elementary operators
\[
\boxed{B_0(g)=e}
\]
and
\[
\boxed{B_{-1}(g)=g^{-1}}.
\]

The other six are proper splitting Rota–Baxter operators.

For each transposition \(t\), there is exactly one operator with
\[
\ker B=A_3,
\qquad
\operatorname{Im}B=\langle t\rangle.
\]
It is the parity homomorphism with values in \(\langle t\rangle\):
\[
B(g)=
\begin{cases}
e,&g\in A_3,\\
t,&g\notin A_3.
\end{cases}
\]
This gives three operators.

For each transposition \(t\), there is exactly one operator with
\[
\ker B=\langle t\rangle,
\qquad
\operatorname{Im}B=A_3.
\]
For the representative \(t=s\), every element has a unique expression
\[
g=s^j r^i,
\qquad
j\in\{0,1\},
\qquad
i\in\{0,1,2\},
\]
and the operator is
\[
\boxed{
B(s^j r^i)=r^{-i}.
}
\]
This gives three further operators.

Hence the eight operators split by kernel and image sizes as
\[
\boxed{
\begin{array}{c|cccc}
(|\ker B|,|\operatorname{Im}B|)
&(6,1)&(1,6)&(3,2)&(2,3)\\ \hline
\#B&1&1&3&3.
\end{array}}
\]

Since
\[
\operatorname{Aut}(S_3)=\operatorname{Inn}(S_3),
\]
conjugation by automorphisms gives exactly four operator classes, with orbit sizes
\[
\boxed{1,\ 1,\ 3,\ 3.}
\]

The standard Rota–Baxter involution
\[
\widetilde B(g)=g^{-1}B(g^{-1})
\]
interchanges
\[
B_0\longleftrightarrow B_{-1}
\]
and interchanges the two non-elementary automorphism orbits. Therefore, under the equivalence generated jointly by group automorphisms and this involution, there are exactly
\[
\boxed{2}
\]
classes: one elementary class and one non-elementary class.

For every non-elementary operator,
\[
S_3=\ker(B)\operatorname{Im}(B)
\]
is an exact factorization, and the associated descendant group satisfies
\[
\boxed{
S_{3,B}\cong C_6.
}
\]

## Assumptions and scope

The Rota–Baxter identity is the group identity introduced by Guo, Lang, and Sheng and used by Bardakov and Gubarev:
\[
B(g)B(h)
=
B\!\left(gB(g)hB(g)^{-1}\right).
\]

The claim concerns all set maps \(S_3\to S_3\), not only homomorphisms.

The automorphism quotient uses the standard conjugation action
\[
B\longmapsto \phi^{-1}B\phi,
\qquad
\phi\in\operatorname{Aut}(S_3).
\]

The additional two-class quotient uses the involution
\[
B\longmapsto \widetilde B,
\qquad
\widetilde B(g)=g^{-1}B(g^{-1}).
\]

No statement is made here about Rota–Baxter operators on larger symmetric groups.

## Proof

For any group Rota–Baxter operator \(B\), the sets
\[
\ker B
\quad\text{and}\quad
\operatorname{Im}B
\]
are subgroups.

The Rota–Baxter identity also defines the descendant product
\[
g\circ h
=
gB(g)hB(g)^{-1}.
\]
With this product, \(S_{3,B}=(S_3,\circ)\) is a group and
\[
B:S_{3,B}\to S_3
\]
is a group homomorphism. Consequently,
\[
|\ker B|\,|\operatorname{Im}B|=6.
\]

Thus only four kernel-image size pairs are possible:
\[
(6,1),\qquad
(3,2),\qquad
(2,3),\qquad
(1,6).
\]

If
\[
|\ker B|=6,
\]
then
\[
B=B_0
\]
is the constant identity map.

Suppose
\[
|\ker B|=3.
\]
The kernel must be the unique subgroup
\[
A_3=\langle r\rangle.
\]
For a Rota–Baxter operator, values are constant on left cosets of the kernel. Hence \(B\) is \(e\) on \(A_3\) and is constant on the other coset. Since the image has order \(2\), the nonidentity value is a transposition \(t\). Therefore
\[
B(g)=
\begin{cases}
e,&g\in A_3,\\
t,&g\notin A_3.
\end{cases}
\]
There are exactly three choices of \(t\). Each map is a homomorphism into the abelian subgroup \(\langle t\rangle\), hence is Rota–Baxter.

Now suppose
\[
|\ker B|=2.
\]
Choose
\[
\ker B=\langle s\rangle.
\]
The image must be
\[
A_3=\langle r\rangle.
\]
Since \(B\) is constant on the three left cosets
\[
\langle s\rangle,
\qquad
\langle s\rangle r,
\qquad
\langle s\rangle r^2,
\]
surjectivity onto \(A_3\) leaves only two possible assignments:
\[
B(r)=r^\varepsilon,
\qquad
B(r^2)=r^{-\varepsilon},
\qquad
\varepsilon\in\{1,-1\}.
\]

Use the Rota–Baxter identity on
\[
(g,h)=(r,s).
\]
Since
\[
r^\varepsilon s r^{-\varepsilon}
=
s r^{-2\varepsilon},
\]
the argument on the right is
\[
r r^\varepsilon s r^{-\varepsilon}
=
s r^{-1-2\varepsilon}.
\]

If
\[
\varepsilon=1,
\]
this lies in
\[
\langle s\rangle,
\]
so the right side is \(e\), while the left side is \(r\). This is impossible.

Thus
\[
\varepsilon=-1.
\]
The surviving map is
\[
B(s^j r^i)=r^{-i}.
\]
It is Rota–Baxter because it is precisely the splitting operator associated with the exact factorization
\[
S_3=\langle s\rangle A_3.
\]
There are three possible transposition kernels, so this case contributes exactly three operators.

It remains to treat
\[
|\ker B|=1.
\]
Then \(B\) is bijective.

Put
\[
F=B^{-1}.
\]
For an invertible group Rota–Baxter operator, \(F\) is a crossed homomorphism for conjugation:
\[
F(uv)=F(u)\,uF(v)u^{-1}.
\]
Define
\[
\theta(u)=F(u)u.
\]
Then
\[
\theta(uv)
=
F(u)uF(v)v
=
\theta(u)\theta(v),
\]
so \(\theta:S_3\to S_3\) is an endomorphism, and
\[
F(u)=\theta(u)u^{-1}.
\]

If \(\theta\) is trivial, then
\[
F(u)=u^{-1},
\]
and therefore
\[
B=B_{-1}.
\]

No other endomorphism yields a bijective \(F\).

If \(\theta\) is an automorphism, it is inner:
\[
\theta(u)=aua^{-1}
\]
for some \(a\in S_3\). Then
\[
F(a)=e=F(e),
\]
unless \(a=e\); for \(a=e\), \(F\) is the constant identity map. In either case \(F\) is not bijective.

If \(\theta\) has image of order \(2\), its kernel is \(A_3\). If \(t\) generates its image, then
\[
\theta(t)=t,
\]
so again
\[
F(t)=e=F(e).
\]
There is no endomorphism of \(S_3\) with image of order \(3\), since that would require a normal subgroup of order \(2\).

Hence inversion is the unique bijective Rota–Baxter operator.

This proves the count
\[
1+3+3+1=8.
\]

For the automorphism quotient, the two elementary operators are fixed by every automorphism. The three operators with kernel \(A_3\) are permuted transitively according to their image transposition subgroup. The three operators with image \(A_3\) are permuted transitively according to their kernel transposition subgroup. Therefore the four orbit sizes are
\[
1,\ 1,\ 3,\ 3.
\]

For the chosen representatives
\[
B_2(r^i s^j)=s^j
\]
and
\[
B_3(s^j r^i)=r^{-i},
\]
direct substitution gives
\[
\widetilde{B_2}=B_3
\]
and
\[
\widetilde{B_3}=B_2.
\]
Also
\[
\widetilde{B_0}=B_{-1}.
\]
Thus automorphisms together with the involution leave exactly two equivalence classes.

Finally, each non-elementary operator is splitting from an exact factorization by subgroups of orders \(2\) and \(3\). For a splitting operator arising from
\[
G=HL,
\]
the descendant group is
\[
G_B\cong H\times L.
\]
Therefore here
\[
S_{3,B}\cong C_2\times C_3\cong C_6.
\]

## Verification

The included program `artifacts/verify.py` represents \(S_3\) as all permutations of three letters.

It enumerates all
\[
6^6=46656
\]
set maps
\[
B:S_3\to S_3
\]
and checks the Rota–Baxter identity on all \(36\) ordered pairs.

Exactly
\[
8
\]
maps pass.

The checker independently records the kernel-image size distribution:
\[
(6,1):1,\qquad
(3,2):3,\qquad
(2,3):3,\qquad
(1,6):1.
\]

It verifies that the four automorphism-conjugacy orbits have sizes
\[
1,\ 1,\ 3,\ 3.
\]

It also verifies that the involution
\[
\widetilde B(g)=g^{-1}B(g^{-1})
\]
swaps the two singleton elementary orbits and swaps the two size-three non-elementary orbits.

Finally, for every non-elementary operator the checker reconstructs the descendant multiplication and verifies that its element-order multiset is
\[
\{1,2,3,3,6,6\},
\]
hence the descendant group is cyclic of order \(6\).

The program returns `VERIFY_OK`.

The exhaustive enumeration is not used as a substitute for the structural proof.

## Relationship to prior work

Bardakov and Gubarev develop the general theory of Rota–Baxter operators on groups, including the facts that kernels and images are subgroups, values are constant on kernel cosets, splitting operators arise from exact factorizations, and classification is naturally considered modulo automorphisms and the standard involution.

Their paper uses \(S_3\) as an example in the map-extension problem and explicitly exhibits the inversion operator, but does not give a complete \(S_3\) operator census.

In a second paper, Bardakov and Gubarev exhibit two non-elementary Rota–Baxter operators on \(S_3\): one splitting operator
\[
S_3\to A_3
\]
coming from
\[
S_3=\langle s\rangle A_3,
\]
and one homomorphism
\[
S_3\to\langle s\rangle.
\]
They observe that both yield a cyclic descendant group of order \(6\), while being different operators. Those two examples represent the two non-elementary automorphism orbits classified above, but that paper does not state that they exhaust all non-elementary operators.

Focused searches for a complete \(S_3\) Rota–Baxter census, an eight-operator count, automorphism normal forms, and the combined automorphism-plus-involution quotient did not locate the classification above.

## Limitations

The theorem is specific to \(S_3\).

The result concerns the weight-\(1\) group Rota–Baxter identity, not linear Rota–Baxter operators on the group algebra.

The descendant-group statement distinguishes the elementary and non-elementary cases only at this order; it does not classify descendant groups for larger symmetric groups.

A specialized or unindexed calculation may already contain the same finite classification. Failed searches do not prove novelty.

## References

1. V. G. Bardakov and V. Gubarev, “Rota-Baxter operators on groups,” arXiv:2103.01848v1, first public 2 March 2021; *Proceedings of the Indian Academy of Sciences - Mathematical Sciences* 133 (2023), article 4, DOI `10.1007/s12044-023-00723-9`.
2. V. G. Bardakov and V. Gubarev, “Rota-Baxter groups, skew left braces, and the Yang-Baxter equation,” arXiv:2105.00428v1, first public 2 May 2021; *Journal of Algebra* 596 (2022), 328–351, DOI `10.1016/j.jalgebra.2021.12.036`.
