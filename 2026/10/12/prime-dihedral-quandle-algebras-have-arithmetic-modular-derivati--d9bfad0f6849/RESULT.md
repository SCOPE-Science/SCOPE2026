# Prime dihedral quandle algebras have arithmetic modular derivations

## Finding

Let \(p\) be an odd prime, let \(K\) be any field of characteristic \(p\), and let
\[
A_p(K)=K[R_p]
\]
be the quandle algebra of the dihedral quandle
\[
R_p=\mathbf F_p,
\qquad
i\triangleright j=2j-i.
\]
Thus
\[
e_i e_j=e_{2j-i}.
\]

Put
\[
h=\operatorname{ord}_p(2)
\]
and
\[
S_p=
\{t\in\{0,\ldots,p-2\}:t\text{ is odd and }2^{t+1}\equiv1\pmod p\}.
\]
Then
\[
\boxed{
\dim_K\operatorname{Der}(A_p(K))
=
2|S_p|
=
\frac{2(p-1)}{\operatorname{lcm}(h,2)}.
}
\]

For every \(t\in S_p\), define
\[
D_t^{(0)}(e_i)
=
\sum_{r\in\mathbf F_p^\times}r^t e_{i+r}
\]
and
\[
D_t^{(1)}(e_i)
=
i\sum_{r\in\mathbf F_p^\times}r^t e_{i+r}.
\]
Then
\[
\boxed{\{D_t^{(0)},D_t^{(1)}:t\in S_p\}}
\]
is a \(K\)-basis of the derivation algebra.

The dimension therefore depends arithmetically on the multiplicative order of \(2\) modulo \(p\). It is \(2\) for \(p=3,5,7\), \(4\) for \(p=17\), and \(6\) for \(p=31\).

## Assumptions and scope

The field \(K\) may be arbitrary of characteristic \(p\); it need not be finite or algebraically closed.

The theorem treats prime dihedral-quandle order equal to the coefficient characteristic. Composite quandle orders and cross-characteristic cases are not classified.

Indices are taken in \(\mathbf F_p\), and coefficients such as \(i\) and \(r^t\) are interpreted in the prime subfield of \(K\).

## Proof

Write
\[
D(e_i)=\sum_{u\in\mathbf F_p}c_i(u)e_u.
\]
Comparing the coefficient of \(e_u\) in the derivation identity for
\[
e_i e_j=e_{2j-i}
\]
gives
\[
c_{2j-i}(u)
=
c_i(2j-u)
+
c_j\!\left(\frac{u+i}{2}\right).
\]

Define
\[
F_i(r)=c_i(i+r).
\]
Putting \(j=i+d\) and \(u=i+2d+r\) yields
\[
F_{i+2d}(r)
=
F_i(-r)+F_{i+d}(r/2).
\tag{1}
\]
With \(d=0\),
\[
F_i(r)=F_i(-r)+F_i(r/2).
\tag{2}
\]
In particular \(F_i(0)=0\).

Fix \(r\) and put
\[
A_i=F_i(r),
\qquad
C_i=F_i(r/2).
\]
Subtracting equation (2) from equation (1) gives
\[
A_{i+2d}-A_i=C_{i+d}-C_i.
\]
At \(i=0\),
\[
C_d-C_0=A_{2d}-A_0.
\]
Substituting this relation back gives
\[
A_{2k-i}=A_i-A_{2i}+A_{2k}.
\]
Since \(2\) is invertible in \(\mathbf F_p\), for every increment the difference
\[
A_{x+h}-A_x
\]
is independent of \(x\). Hence \(A_i-A_0\) is additive as a function
\[
\mathbf F_p\to K.
\]
Every such additive map is scalar multiplication, so
\[
F_i(r)=\alpha(r)i+\beta(r)
\tag{3}
\]
for functions \(\alpha,\beta:\mathbf F_p\to K\). The equality \(F_i(0)=0\) gives
\[
\alpha(0)=\beta(0)=0.
\]

Substituting equation (3) into equation (1) and comparing coefficients gives
\[
\alpha(r/2)=2\alpha(r),
\qquad
\alpha(-r)=-\alpha(r),
\tag{4}
\]
and
\[
\beta(r)=\beta(-r)+\beta(r/2).
\tag{5}
\]

The functions
\[
r\longmapsto r^t,
\qquad
0\le t\le p-2,
\]
form a \(K\)-basis of all \(K\)-valued functions on \(\mathbf F_p^\times\), because their evaluation matrix is Vandermonde on the distinct nonzero prime-field elements.

For \(r^t\), equation (4) requires
\[
(-1)^t=-1
\]
and
\[
2^{-t}=2.
\]
Thus \(t\) is odd and
\[
2^{t+1}=1
\]
in \(\mathbf F_p\).

Equation (5) gives the same condition, since it becomes
\[
1=(-1)^t+2^{-t}.
\]
Even \(t\) is impossible; for odd \(t\) the equation is equivalent to
\[
2^{t+1}=1.
\]

Therefore both the \(\alpha\)-space and the \(\beta\)-space have basis
\[
\{r^t:t\in S_p\}.
\]
Equation (3) produces exactly the two displayed derivations per \(t\), proving the basis statement.

Finally, if
\[
h=\operatorname{ord}_p(2),
\]
then \(u=t+1\) is an even positive multiple of \(h\) not exceeding \(p-1\). Such \(u\) are precisely the positive multiples of
\[
\operatorname{lcm}(h,2)
\]
up to \(p-1\). Thus
\[
|S_p|
=
\frac{p-1}{\operatorname{lcm}(h,2)},
\]
which proves the dimension formula.

## Verification

The included checker constructs every displayed basis derivation for
\[
p\in\{3,5,7,11,13,17,19,23,31\}
\]
and verifies the derivation identity on all basis pairs.

For
\[
p\in\{3,5,7,11\},
\]
it independently builds the full linear system for arbitrary derivations and computes its nullity over \(\mathbf F_p\). The nullities agree with
\[
\frac{2(p-1)}{\operatorname{lcm}(\operatorname{ord}_p(2),2)}.
\]

The checker returns `VERIFY_OK`.

Finite computation is not used to prove the all-prime theorem.

## Relationship to prior work

Elhamdadi, Makhlouf, Silvestrov, and Zappala introduced the derivation problem for quandle algebras and completely characterized dihedral-quandle derivations in characteristic zero. Their Theorem 3.9 gives trivial derivation algebra when the dihedral quandle has odd order and the coefficient field has characteristic zero.

Their positive-characteristic treatment is explicitly computational: Section 4.2 gives matrices only for dihedral quandles of cardinality \(3\) through \(6\). The rows
\[
(n,\operatorname{char}K)=(3,3)
\]
and
\[
(5,5)
\]
both have two free parameters, agreeing with the first two prime instances of the theorem above.

The inspected source does not give an all-prime modular dimension formula, an explicit all-prime basis, or a connection with \(\operatorname{ord}_p(2)\). Focused searches did not locate such a result. The closest database result on \(K[R_3]\) concerns idempotents rather than derivations.

## Limitations

The theorem treats the diagonal modular regime: prime dihedral-quandle order \(p\) over characteristic \(p\).

It does not classify composite quandle orders or cross-characteristic cases.

An equivalent calculation may exist under different terminology in quandle-ring or nonassociative-algebra literature.

Failed searches do not prove novelty.

## References

1. M. Elhamdadi, A. Makhlouf, S. Silvestrov, and E. Zappala, “The derivation problem for quandle algebras,” arXiv:2106.08289v1, first public version 15 June 2021, DOI 10.48550/arXiv.2106.08289. MSC 2020: 17A60, 16D99.
