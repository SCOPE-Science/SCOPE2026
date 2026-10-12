# Weighted cycle evolution algebras over finite fields are doubling-orbit classified

## Finding

Let \(q\) be a prime power and let \(n\ge2\). For
\[
\mathbf c=(c_0,\ldots,c_{n-1})\in(\mathbf F_q^\times)^n,
\]
define the \(n\)-dimensional evolution algebra \(A(\mathbf c)\) with natural basis
\[
e_0,\ldots,e_{n-1}
\]
by
\[
e_i e_j=0\qquad(i\ne j)
\]
and
\[
e_i^2=c_i e_{i+1},
\]
where indices are read modulo \(n\).

Put
\[
m=2^n-1,
\qquad
d=\gcd(m,q-1),
\]
and define the weighted cycle invariant
\[
\Delta(\mathbf c)
=
c_0^{2^{n-1}}
c_1^{2^{n-2}}
\cdots
c_{n-2}^{2}
c_{n-1}.
\]
Let
\[
Q_{n,q}
=
\mathbf F_q^\times/(\mathbf F_q^\times)^m.
\]
Since \(\mathbf F_q^\times\) is cyclic,
\[
Q_{n,q}\cong C_d.
\]
Squaring induces an automorphism
\[
s:Q_{n,q}\to Q_{n,q},
\qquad
s([u])=[u^2],
\]
and
\[
s^n=1
\]
because \(2^n\equiv1\pmod d\).

Then the complete isomorphism classification is
\[
\boxed{
A(\mathbf c)\cong A(\mathbf b)
\iff
[\Delta(\mathbf c)]
=
[\Delta(\mathbf b)]^{2^r}
\text{ for some }0\le r<n.
}
\]

Thus the isomorphism classes are exactly the \(C_n\)-orbits of the doubling action on \(C_d\). Their number is
\[
\boxed{
N_{n,q}
=
\frac1n
\sum_{r=0}^{n-1}
\gcd(d,2^r-1).
}
\]

Every class has a representative
\[
A_a:
\qquad
e_i^2=e_{i+1}\quad(0\le i<n-1),
\qquad
e_{n-1}^2=a e_0,
\]
and the isomorphism class depends exactly on the doubling orbit of
\[
[a]\in Q_{n,q}.
\]

The automorphism group is controlled by the same orbit. There is an exact sequence
\[
\boxed{
1\longrightarrow
\mu_d(\mathbf F_q)
\longrightarrow
\operatorname{Aut}(A(\mathbf c))
\longrightarrow
\operatorname{Stab}_{C_n}([\Delta(\mathbf c)])
\longrightarrow1,
}
\]
where
\[
\mu_d(\mathbf F_q)
=
\{u\in\mathbf F_q^\times:u^d=1\}.
\]
Consequently
\[
\boxed{
|\operatorname{Aut}(A(\mathbf c))|
=
d\,
|\operatorname{Stab}_{C_n}([\Delta(\mathbf c)])|.
}
\]

Finally, the same invariant completely controls idempotents:
\[
\boxed{
|\operatorname{Idem}(A(\mathbf c))|
=
\begin{cases}
d+1,&[\Delta(\mathbf c)]=1,\\
1,&[\Delta(\mathbf c)]\ne1.
\end{cases}
}
\]
Thus exactly one isomorphism class has a nonzero idempotent: the class of the unweighted directed cycle
\[
e_i^2=e_{i+1}.
\]

For example, when
\[
(q,n)=(16,4),
\]
one has
\[
d=\gcd(15,15)=15.
\]
The doubling orbits in \(C_{15}\) are
\[
\{0\},
\quad
\{1,2,4,8\},
\quad
\{3,6,9,12\},
\quad
\{5,10\},
\quad
\{7,11,13,14\}.
\]
Hence there are exactly five isomorphism classes. Their automorphism-group orders are respectively
\[
60,\ 15,\ 15,\ 30,\ 15.
\]
Only the first class has nonzero idempotents, and it has exactly \(16\) idempotents.

## Assumptions and scope

The coefficients \(c_i\) are required to be nonzero, so the structure matrix is a weighted permutation matrix and
\[
A(\mathbf c)^2=A(\mathbf c).
\]
This perfectness condition is what forces isomorphisms to be monomial with respect to natural bases.

The classification concerns one connected directed cycle. A permutation evolution algebra with several disjoint cycles decomposes into cycle components, but isomorphic cycle lengths can also be permuted, so the multi-cycle classification has an additional wreath-product layer and is not claimed here.

The field is finite. The proof uses cyclicity of
\[
\mathbf F_q^\times
\]
to turn the coefficient obstruction into the finite cyclic quotient \(C_d\).

## Proof

Because the structure matrix of \(A(\mathbf c)\) is invertible, \(A(\mathbf c)\) is a perfect evolution algebra. A standard natural-basis rigidity theorem for perfect evolution algebras says that every algebra isomorphism between two such algebras sends each natural basis element to a nonzero scalar multiple of a natural basis element.

Suppose
\[
\varphi:A(\mathbf c)\to A(\mathbf b)
\]
is an isomorphism. Write
\[
\varphi(e_i)=\lambda_i f_{\sigma(i)}
\]
with
\[
\lambda_i\in\mathbf F_q^\times
\]
and
\[
\sigma\in S_n.
\]
Comparing
\[
\varphi(e_i^2)
=
c_i\lambda_{i+1}f_{\sigma(i+1)}
\]
with
\[
\varphi(e_i)^2
=
\lambda_i^2 b_{\sigma(i)}f_{\sigma(i)+1}
\]
shows first that
\[
\sigma(i+1)=\sigma(i)+1
\]
for every \(i\). Hence
\[
\sigma(i)=i+r
\]
for one rotation
\[
r\in\mathbf Z/n\mathbf Z.
\]

The scalar equations are
\[
c_i\lambda_{i+1}
=
\lambda_i^2 b_{i+r}.
\]
Starting from \(\lambda_0\) and iterating gives
\[
\lambda_n
=
\lambda_0^{2^n}
\prod_{i=0}^{n-1}
\left(\frac{b_{i+r}}{c_i}\right)^{2^{n-1-i}}.
\]
The cyclic condition
\[
\lambda_n=\lambda_0
\]
is therefore equivalent to
\[
\lambda_0^m
=
\frac{\Delta(\mathbf c)}
{\Delta_r(\mathbf b)},
\]
where
\[
\Delta_r(\mathbf b)
=
\prod_{i=0}^{n-1}
b_{i+r}^{2^{n-1-i}}.
\]

Modulo \(m\)-th powers,
\[
[\Delta_r(\mathbf b)]
=
[\Delta(\mathbf b)]^{2^r}.
\]
Indeed, for one rotation,
\[
\Delta_1(\mathbf b)
=
\frac{\Delta(\mathbf b)^2}{b_0^m},
\]
and iteration gives the general formula.

Thus an isomorphism with rotation \(r\) exists exactly when
\[
[\Delta(\mathbf c)]
=
[\Delta(\mathbf b)]^{2^r}
\]
in \(Q_{n,q}\). This proves the classification.

Since
\[
Q_{n,q}\cong C_d,
\]
the number of classes follows from Burnside's lemma. The number of points fixed by the \(r\)-th power of the doubling map is the number of solutions to
\[
(2^r-1)x=0
\]
in \(C_d\), namely
\[
\gcd(d,2^r-1).
\]
Therefore
\[
N_{n,q}
=
\frac1n
\sum_{r=0}^{n-1}
\gcd(d,2^r-1).
\]

For automorphisms, take \(\mathbf b=\mathbf c\). A rotation \(r\) lifts to an automorphism exactly when it stabilizes
\[
[\Delta(\mathbf c)].
\]
Whenever it lifts, the equation for \(\lambda_0\) is an \(m\)-th power equation with exactly
\[
d
\]
solutions, because the kernel of
\[
u\longmapsto u^m
\]
on \(\mathbf F_q^\times\) has order \(d\). The rotation-zero lifts are exactly the diagonal automorphisms and form
\[
\mu_d(\mathbf F_q).
\]
This yields the exact sequence and the automorphism-order formula.

It remains to determine idempotents. Let
\[
x=\sum_{i=0}^{n-1}x_i e_i.
\]
The equation
\[
x^2=x
\]
is equivalent to
\[
x_{i+1}=c_i x_i^2
\]
for every \(i\). If one coordinate is zero, all coordinates are zero. Otherwise the entire idempotent is determined by \(x_0\), and one circuit around the cycle gives
\[
x_0
=
\Delta(\mathbf c)x_0^{2^n}.
\]
Hence
\[
x_0^m
=
\Delta(\mathbf c)^{-1}.
\]
This equation has a solution exactly when
\[
[\Delta(\mathbf c)]=1
\]
in \(Q_{n,q}\), and then it has exactly \(d\) nonzero solutions. Adding the zero idempotent gives the stated formula.

Finally,
\[
[\Delta(\mathbf c)]=1
\]
is exactly the orbit of the trivial class, so the idempotent-rich algebras form one isomorphism class, represented by the unweighted directed cycle.

## Verification

The included checker uses only the cyclic multiplicative group of a finite field, so it applies equally to prime fields and extension fields.

For the complete coefficient spaces in
\[
(q,n)=(4,3),\ (7,2),\ (8,3),\ (5,4),
\]
it compares every pair of weighted cycles. It independently solves the scalar recurrence for each possible rotation and verifies that an isomorphism exists exactly when the two \(\Delta\)-classes lie in the same doubling orbit.

For
\[
(q,n)=(7,2),\ (8,3),\ (16,4),\ (9,3),
\]
it enumerates every coefficient tuple and verifies:

- the exact number of nonzero idempotents from the cyclic congruence
  \[
  (2^n-1)x\equiv-\delta\pmod{q-1};
  \]
- the automorphism count by solving the scalar recurrence for every rotation;
- the stabilizer formula
  \[
  |\operatorname{Aut}|=d|\operatorname{Stab}|;
  \]
- the Burnside class count.

The nontrivial class counts include
\[
N_{2,7}=2,\qquad
N_{3,8}=3,\qquad
N_{4,16}=5.
\]

The checker returns `VERIFY_OK`.

The finite computations are consistency checks; the classification is proved symbolically.

## Relationship to prior work

Elduque and Labra develop the graph-theoretic automorphism framework for perfect evolution algebras. Their work supplies a general exact sequence separating diagonal automorphisms from graph permutations, but does not in the inspected material classify coefficient systems on a directed cycle up to isomorphism over finite fields.

Narkuziyev studies evolution algebras associated with permutations, decomposes them into cycle components, and gives isomorphism criteria and idempotent-coordinate formulas. A public dissertation abstract records sufficient isomorphism criteria and an explicit idempotent formula for cycle components. Those results motivate the present finite-field question, but they do not state the necessary-and-sufficient quotient-orbit classification, the Burnside class count, or the automorphism stabilizer formula above.

A later open-access paper on permutation representations and automorphisms of evolution algebras restates the monomial rigidity of natural bases and cites the graph-theoretic description of the diagonal kernel. Exact-term inspection of that paper found no directed-cycle classification.

The new point is that all coefficient data on one weighted cycle collapse to one class
\[
[\Delta]\in
\mathbf F_q^\times/(\mathbf F_q^\times)^{2^n-1},
\]
with rotation acting by doubling. This simultaneously gives the complete finite-field isomorphism census, every automorphism-group order, and the exact idempotent boundary.

## Limitations

The theorem treats a single directed cycle with every edge weight nonzero. Several-cycle permutation algebras require accounting for permutations among isomorphic cycle components.

The general monomial-rigidity and graph-automorphism machinery is prior work; the claimed contribution is the explicit finite-field orbit reduction, Burnside enumeration, automorphism stabilizers, and idempotent dichotomy for the weighted cycle family.

The public source most directly devoted to permutation evolution algebras was only partially inspectable through its abstract and a public dissertation summary. An unindexed equivalent finite-field classification in its full article or older literature remains a residual bibliographic risk.

Failed searches do not prove novelty.

## References

1. A. Elduque and A. Labra, “Evolution algebras, automorphisms, and graphs,” arXiv:1902.02191v1, first public version 6 February 2019; *Linear and Multilinear Algebra* 69 (2021), 331–342, DOI 10.1080/03081087.2019.1598931. Primary MSC 17A36.
2. B. A. Narkuziyev, “Some remarks on evolution algebras corresponding to permutations,” arXiv:2005.05793v1, first public version 9 May 2020; *Journal of Algebra and Its Applications* 21 (2022), 2250112, DOI 10.1142/S0219498822501122. AMSC 17D92, 17D99.
3. C. Costoya, P. Mayorga, and A. Viruel, “Permutation representations and automorphisms of evolution algebras,” arXiv:2401.05924v1, first public version 11 January 2024; *Mediterranean Journal of Mathematics* 22 (2025), 149, DOI 10.1007/s00009-025-02924-0.
