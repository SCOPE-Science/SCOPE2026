# Relative subgroup commutativity for \(C_{p^a}\rtimes C_q\) Frobenius groups

## Finding

Let \(p,q\) be distinct primes with
\[
q\mid p-1,
\]
let \(a\ge2\), and let
\[
G=C_{p^a}\rtimes C_q
\]
be the faithful nonabelian semidirect product.

Let
\[
P=C_{p^a}
\]
be the normal kernel, and for
\[
0\le i\le a
\]
let \(P_i\) be its unique subgroup of order \(p^i\). Put
\[
S_i=1+p+\cdots+p^i
=
\frac{p^{i+1}-1}{p-1}
\]
and
\[
L=a+1+S_a.
\]

Then
\[
\boxed{|L(G)|=L.}
\]

Every subgroup of \(G\) is exactly one of the following:

- a kernel subgroup \(P_i\);
- one of the \(p^{a-i}\) conjugates
  \[
  H_{i,t}\cong C_{p^i}\rtimes C_q,
  \qquad 0\le i<a;
  \]
- the whole group
  \[
  H_{a,t}=G.
  \]

For every kernel subgroup,
\[
\boxed{sd(P_i,G)=1.}
\]

For every subgroup \(H_{i,t}\) containing a \(q\)-element,
\[
\boxed{
sd(H_{i,t},G)
=
\frac{
(i+1)L+
\displaystyle\sum_{j=0}^{i}
p^{i-j}\bigl(2a-j+1+S_j\bigr)
}{
(i+1+S_i)L
}.
}
\]

The decisive structural statement is:

\[
\boxed{
H_{j,u}H_{k,v}=H_{k,v}H_{j,u}
\quad\Longleftrightarrow\quad
H_{j,u}\subseteq H_{k,v}
\text{ or }
H_{k,v}\subseteq H_{j,u}.
}
\]

Thus the full relative subgroup commutativity function of this infinite metacyclic Frobenius family is explicit.

## Assumptions and scope

Because \(q\mid p-1\), the cyclic group
\[
\operatorname{Aut}(C_{p^a})
\]
contains an element of order \(q\). In a faithful action, the corresponding multiplier is nontrivial modulo \(p\), so its difference from \(1\) is a unit modulo \(p^a\). Hence the complement acts fixed-point-freely on the nonidentity elements of the kernel, and \(G\) is a Frobenius group.

The invariant
\[
sd(H,G)
\]
is the relative subgroup commutativity degree:
\[
sd(H,G)
=
\frac{
|\{(A,B)\in L(H)\times L(G):AB=BA\}|
}{
|L(H)|\,|L(G)|
}.
\]

The theorem concerns ordinary subgroup permutability, not the cyclic-subgroup-only variant.

The restriction \(a\ge2\) removes the order-\(pq\) boundary case and isolates the prime-power-kernel family not treated by the prime-kernel semidirect calculations in the motivating literature.

## Proof

Choose generators
\[
P=\langle x\rangle,
\qquad
Q=\langle y\rangle,
\]
with
\[
|x|=p^a,\qquad |y|=q,
\]
and
\[
y^{-1}xy=x^\lambda,
\]
where \(\lambda\) has order \(q\) modulo \(p^a\).

For each \(i\), let
\[
P_i=\langle x^{p^{a-i}}\rangle.
\]
These are all the subgroups of \(P\), and each is normal in \(G\).

Let \(K\le G\) with \(K\nleq P\). Since \(G/P\cong C_q\) has prime order, the image of \(K\) in \(G/P\) is all of \(C_q\). Therefore
\[
K\cap P=P_i
\]
for some \(i\), and \(K\) contains an element projecting to a generator of \(G/P\). Hence
\[
K=P_i\langle x^t y\rangle
\]
after replacing the projected generator if necessary.

Two such subgroups with the same \(i\) are equal exactly when their parameters differ by an element of \(P_i\). Thus there are
\[
|P:P_i|=p^{a-i}
\]
subgroups of type \(H_{i,t}\). Summing over \(i\), and adding the \(a+1\) kernel subgroups, gives
\[
|L(G)|
=
(a+1)+\sum_{i=0}^{a}p^{a-i}
=
a+1+S_a
=
L.
\]

We next determine subgroup permutability.

Take two subgroups containing \(q\)-elements,
\[
A=H_{j,u},
\qquad
B=H_{k,v}.
\]
If one contains the other, then they certainly permute.

Suppose neither contains the other. Their intersection contains no \(q\)-subgroup. Indeed, a common \(q\)-subgroup would force the parameter cosets in the cyclic kernel to meet, and because the kernel subgroups form a chain, this would make one of \(A,B\) contain the other. Hence
\[
A\cap B=P_{\min(j,k)}.
\]
If \(AB=BA\), then \(AB\) would be a subgroup and
\[
|AB|
=
\frac{|A||B|}{|A\cap B|}
=
p^{\max(j,k)}q^2.
\]
But every subgroup of \(G\) has order either \(p^r\) or \(p^r q\), by the classification above. This is impossible. Therefore two \(q\)-containing subgroups permute exactly when they are comparable.

Fix \(H_{j,u}\). It permutes with all \(a+1\) kernel subgroups.

The \(q\)-containing subgroups contained in \(H_{j,u}\) are counted by
\[
\sum_{h=0}^{j}p^{j-h}
=
S_j.
\]
For every level
\[
k=j+1,\ldots,a,
\]
there is a unique \(q\)-containing supergroup of \(H_{j,u}\), giving \(a-j\) further partners. Hence
\[
|C(H_{j,u})|
=
(a+1)+S_j+(a-j)
=
2a-j+1+S_j.
\]

Now let \(H=H_{i,t}\). Its subgroup lattice consists of the \(i+1\) kernel subgroups
\[
P_0,\ldots,P_i
\]
and, for every \(0\le j\le i\), exactly
\[
p^{i-j}
\]
subgroups of type \(H_{j,u}\). Therefore
\[
|L(H)|
=
i+1+S_i.
\]

Every kernel subgroup is normal in \(G\), hence has all \(L\) subgroups of \(G\) as permuting partners. Summing partner counts over \(L(H)\) gives
\[
(i+1)L+
\sum_{j=0}^{i}
p^{i-j}(2a-j+1+S_j).
\]
Dividing by
\[
(i+1+S_i)L
\]
proves the stated formula.

Finally, if \(H=P_i\), every subgroup of \(H\) is one of the normal subgroups \(P_j\). Hence every subgroup of \(H\) permutes with every subgroup of \(G\), so
\[
sd(P_i,G)=1.
\]

## Verification

The included replay constructs the semidirect products directly from modular multiplication for
\[
(p,a,q)=(3,2,2),\quad(3,3,2),\quad(5,2,2),\quad(7,2,3).
\]

For each case it:

- constructs every predicted kernel subgroup and every predicted \(q\)-containing subgroup;
- checks subgroup closure and the exact total lattice count
  \[
  a+1+S_a;
  \]
- tests every ordered pair of listed subgroups by comparing the set products \(AB\) and \(BA\);
- verifies the exact partner count
  \[
  2a-j+1+S_j
  \]
  for every \(H_{j,t}\);
- computes \(sd(H,G)\) directly from the definition for every listed subgroup;
- compares every value with the closed formula.

For the case
\[
(p,a,q)=(3,2,2),
\]
the replay additionally exhausts all one- and two-generator subgroups and verifies that the predicted list is the complete subgroup lattice.

The replay returns `VERIFY_OK`.

Finite enumeration is not used to prove the universal theorem.

## Relationship to prior work

The 2018 paper *Finite groups with two relative subgroup commutativity degrees* studies the function
\[
H\longmapsto sd(H,G)
\]
and computes it on several explicit semidirect-product families. In particular, its prime-kernel Frobenius family has the form
\[
C_p\rtimes C_{q^n}.
\]
The subgroup lattice there has a single conjugacy class of nonnormal subgroups.

The family treated here reverses the growth direction:
\[
C_{p^a}\rtimes C_q,
\qquad a\ge2.
\]
It has nonnormal \(q\)-containing subgroups at every kernel level. Their permutability is controlled by comparability in the subgroup lattice, producing the weighted sum in the formula above.

The later relative cyclic-subgroup paper studies the restriction of the same probability to cyclic subgroups. That invariant is different: the present theorem counts all subgroups of each \(H_{i,t}\), including its noncyclic Frobenius subgroups.

Targeted searches using relative subgroup commutativity, metacyclic Frobenius groups, cyclic prime-power kernels, ZM terminology, and the exact \(C_{p^a}\rtimes C_q\) family did not locate the formula above.

## Limitations

The complement is required to have prime order. Composite cyclic complements introduce intermediate projected subgroups and additional comparability strata.

The kernel is cyclic of prime-power order. More general ZM-groups have several coprime kernel and complement divisors and require a higher-dimensional divisor-poset count.

The theorem does not classify when the displayed values for different \(i\) coincide; it supplies the complete relative function itself.

An equivalent formula could exist under ZM-group or subgroup-permutability terminology not located by the searches.

## References

1. M.-S. Lazorec and M. Tărnăuceanu, “Finite groups with two relative subgroup commutativity degrees,” arXiv:1801.09133v1, first public version 27 January 2018; *Publicationes Mathematicae Debrecen* 94 (2019), 157–169, DOI 10.5486/PMD.2019.8290.
2. M.-S. Lazorec, “Relative cyclic subgroup commutativity degrees of finite groups,” arXiv:1803.01149v1, first public version 3 March 2018; *Filomat* 33 (2019), 4021–4032, DOI 10.2298/FIL1913021L.
