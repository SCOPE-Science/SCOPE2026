# Prime-complement Frobenius groups with elementary abelian kernels are not psi-divisible

## Finding

Let \(p\) and \(q\) be distinct primes, let \(r\ge2\), and let
\[
G=V\rtimes C_q
\]
be a Frobenius group with
\[
V\cong C_p^r.
\]
For a finite group \(X\), write
\[
\psi(X)=\sum_{x\in X}o(x).
\]

Then
\[
\boxed{\psi(V)=p^{r+1}-p+1}
\]
and
\[
\boxed{\psi(G)=p^{r+1}-p+1+p^r q(q-1)}.
\]
Moreover,
\[
\boxed{
\gcd(\psi(V),\psi(G))
=
\gcd(p^{r+1}-p+1,q-1)
<
\psi(V).
}
\]
In particular,
\[
\psi(V)\nmid\psi(G),
\]
so \(G\) is not \(\psi\)-divisible.

Thus the open search for nonabelian \(\psi\)-divisible groups contains no Frobenius group with a noncyclic elementary abelian kernel and complement of prime order.

## Assumptions and scope

A finite group \(G\) is \(\psi\)-divisible if
\[
\psi(H)\mid\psi(G)
\]
for every subgroup \(H\le G\).

The theorem concerns Frobenius semidirect products
\[
G=V\rtimes C_q
\]
whose kernel \(V\) is elementary abelian of rank \(r\ge2\) and whose complement has prime order \(q\).

The Frobenius hypothesis means that every nonidentity element of the complement fixes no nonzero element of \(V\). Equivalently, the complement acts semiregularly on
\[
V\setminus\{0\}.
\]

The rank restriction \(r\ge2\) isolates the noncyclic-kernel case. Cyclic normal kernels belong to the previously studied ZM and cyclic-by-cyclic settings.

## Proof

Every nonidentity element of \(V\) has order \(p\). Therefore
\[
\psi(V)
=
1+(p^r-1)p
=
p^{r+1}-p+1.
\]
Put
\[
D=p^{r+1}-p+1.
\]

Let \(c\) generate the complement \(C_q\). For any
\[
v\in V
\]
and
\[
1\le j\le q-1,
\]
consider the element
\[
vc^j.
\]
In additive notation on \(V\),
\[
(vc^j)^q
=
\left(
v+c^jv+\cdots+c^{(q-1)j}v,\ 1
\right).
\]
Because \(c^j\) acts fixed-point-freely on \(V\), the linear map
\[
c^j-1
\]
is invertible. Since
\[
(1+c^j+\cdots+c^{(q-1)j})(c^j-1)=c^{jq}-1=0,
\]
the geometric-sum operator is zero. Hence
\[
(vc^j)^q=1.
\]
The element \(vc^j\) is not the identity, so it has order exactly \(q\).

Thus every one of the
\[
p^r(q-1)
\]
elements outside \(V\) has order \(q\), and therefore
\[
\psi(G)
=
D+p^r q(q-1).
\]

The fixed-point-free action of \(C_q\) on
\[
V\setminus\{0\}
\]
partitions its
\[
p^r-1
\]
elements into orbits of size \(q\). Hence
\[
q\mid p^r-1.
\]
Consequently
\[
D
=
p(p^r-1)+1
\equiv1\pmod q.
\]
Also
\[
D\equiv1\pmod p.
\]
Therefore
\[
\gcd(D,pq)=1.
\]

Now
\[
\begin{aligned}
\gcd(\psi(V),\psi(G))
&=
\gcd\!\left(D,D+p^rq(q-1)\right)\\
&=
\gcd\!\left(D,p^rq(q-1)\right)\\
&=
\gcd(D,q-1).
\end{aligned}
\]

Finally, since
\[
q\mid p^r-1,
\]
we have
\[
q\le p^r-1.
\]
Hence
\[
q-1<p^r<p^{r+1}-p+1=D,
\]
so
\[
\gcd(D,q-1)<D.
\]
Thus
\[
\psi(V)\nmid\psi(G),
\]
and the subgroup \(V\) itself witnesses failure of \(\psi\)-divisibility.

## Verification

The included replay constructs several Frobenius semidirect products with noncyclic elementary abelian kernels.

For each example it verifies directly that the chosen complement matrix has prime order and acts fixed-point-freely on every nonzero kernel vector. It then enumerates every group element, computes its order by repeated multiplication, evaluates the full sum of element orders, and checks
\[
\psi(G)
=
p^{r+1}-p+1+p^rq(q-1).
\]

It also independently checks
\[
\gcd(\psi(V),\psi(G))
=
\gcd(p^{r+1}-p+1,q-1)
<
\psi(V).
\]

The examples include both scalar and irreducible nonscalar actions, including the groups with parameters
\[
(p,r,q)=(2,2,3),\ (2,3,7),\ (3,2,2),\ (5,2,3),\ (7,2,3).
\]
The replay returns `VERIFY_OK`.

Finite enumeration is not used to prove the universal theorem.

## Relationship to prior work

Lazorec's 2020 paper develops the \(\psi\)-divisibility problem beyond the abelian case. Its introduction records that no nonabelian \(\psi\)-divisible group was known, and its second section studies ZM-groups as a natural test class. In the key square-free argument, the obstruction uses a subgroup with cyclic normal Sylow subgroup.

The 2022 preprint on the \(\psi\)-divisibility graph explicitly states that the existence of a nonabelian \(\psi\)-divisible group remains open. That paper studies the graph mainly for cyclic groups and does not treat Frobenius groups with elementary abelian kernels.

Published-result searches also locate obstructions for cyclic-by-cyclic semidirect products and for groups with a noncentral normal cyclic Sylow subgroup. Those results do not cover the present rank-\(r\) elementary abelian kernel with \(r\ge2\).

The new point is that the whole kernel
\[
V\cong C_p^r
\]
provides an exact divisibility obstruction. The Frobenius orbit condition forces
\[
q\mid p^r-1,
\]
which in turn makes the kernel sum \(p^{r+1}-p+1\) coprime to both \(p\) and \(q\). This reduces the required divisibility to an impossible divisor of \(q-1\).

## Limitations

The theorem does not rule out nonabelian \(\psi\)-divisible groups in general.

The complement is required to have prime order. For larger complements, the sum of element orders outside the kernel has additional order strata, so the same final size argument does not automatically apply.

The kernel is required to be elementary abelian. Other abelian or nonabelian Frobenius kernels have different element-order distributions.

The most relevant primary sources and statement-level searches were inspected, but an equivalent obstruction could exist under different Frobenius-group notation or in unindexed literature.

## References

1. M.-S. Lazorec, “On a divisibility property involving the sum of element orders,” arXiv:2003.01678v1, first public version 3 March 2020; later published in *Bulletin of the Malaysian Mathematical Sciences Society* 44 (2021), 941–951, DOI 10.1007/s40840-020-00987-8.
2. M.-S. Lazorec, “A graph related to the sum of element orders of a finite group,” arXiv:2203.00071v1, first public version 28 February 2022; later published in *Contributions to Discrete Mathematics* 18(2) (2023), 113–128, DOI 10.55016/ojs/cdm.v18i2.73182.
