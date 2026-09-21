# The exponent of an abelian p-group from its modular zero-divisor graph

## Statement

Let \(K=\mathbf F_q\) be a finite field of characteristic \(p\), let \(G\) be a
nontrivial finite abelian \(p\)-group, and write
\[
N=|G|,\qquad e=\exp(G).
\]
Let \(\Gamma(KG)\) be the zero-divisor graph of the group algebra: its vertices
are the nonzero zero divisors, with distinct vertices adjacent when their
product is zero. Denote its minimum vertex degree by \(\delta(\Gamma(KG))\).

**Theorem.**
\[
\boxed{
\delta(\Gamma(KG))=
\begin{cases}
q^{N/2}-2,&e=2,\\[2mm]
q^{N/e}-1,&e>2.
\end{cases}}
\tag{1}
\]

Consequently, if \(K,L\) are finite fields, \(G\) is a finite abelian
\(p\)-group with \(\operatorname{char}K=p\), \(H\) is a finite group, and
\[
\Gamma(KG)\cong\Gamma(LH),
\]
then
\[
K\cong L,\qquad |G|=|H|,\qquad H\text{ is an abelian }p\text{-group},
\qquad \boxed{\exp(G)=\exp(H)}.
\tag{2}
\]

For the prime field this gives a concrete isomorphism consequence. If \(G\) is
a finite abelian \(p\)-group of rank at most \(2\), then
\[
\Gamma(\mathbf F_pG)\cong\Gamma(\mathbf F_pH)
\]
for a finite group \(H\) implies \(G\cong H\). Thus the modular
zero-divisor-graph isomorphism question is affirmative for all two-generated
finite abelian \(p\)-groups.

## Proof

Let \(J=\Delta(G)\) be the augmentation ideal. Since \(G\) is a finite
\(p\)-group and \(K\) has characteristic \(p\), \(KG\) is local with maximal
ideal \(J\). Hence the vertices of \(\Gamma(KG)\) are exactly \(J\setminus
\{0\}\).

### 1. A sharp lower bound for annihilators

Write \(e=p^a\). For
\[
x=\sum_{g\in G}\alpha_g g\in J
\]
we have \(\sum_g\alpha_g=0\). Because \(KG\) is commutative, the
\(p^a\)-power Frobenius identity gives
\[
x^e
 =\sum_{g\in G}\alpha_g^e g^e
 =\left(\sum_{g\in G}\alpha_g\right)^e1
 =0.
\tag{3}
\]

Let \(M_x:KG\to KG\) be multiplication by \(x\). Then \(M_x^e=0\).
Every Jordan block of the nilpotent operator \(M_x\) has size at most \(e\).
Since \(\dim_K KG=N\), the number of Jordan blocks is at least \(N/e\).
Therefore
\[
\dim_K\operatorname{Ann}(x)
 =\dim_K\ker M_x
 \ge \frac Ne .
\tag{4}
\]

This bound is attained. Choose \(g\in G\) of order \(e\) and put \(x=g-1\).
Left multiplication by \(g\) permutes the standard basis \(G\) in exactly
\(N/e\) cycles, each of length \(e\). On each cycle the kernel of
\(M_g-I=M_{g-1}\) consists of the vectors with constant coefficients.
Consequently
\[
\dim_K\operatorname{Ann}(g-1)=\frac Ne.
\tag{5}
\]
Thus
\[
\min_{0\ne x\in J}|\operatorname{Ann}(x)|=q^{N/e}.
\tag{6}
\]

### 2. From annihilator size to graph degree

For a vertex \(x\),
\[
\deg(x)=
\begin{cases}
|\operatorname{Ann}(x)|-2,&x^2=0,\\
|\operatorname{Ann}(x)|-1,&x^2\ne0,
\end{cases}
\tag{7}
\]
because \(0\) is never a vertex and \(x\) itself must also be removed from
its annihilator exactly when \(x^2=0\).

If \(e=2\), equation (3) gives \(x^2=0\) for every \(x\in J\).
Equations (6) and (7) therefore yield
\[
\delta(\Gamma(KG))=q^{N/2}-2.
\]

Now suppose \(e>2\). For an element \(g\) of order \(e\),
\((g-1)^2\ne0\): in characteristic \(2\) this would force \(g^2=1\), and in
odd characteristic the three basis elements \(g^2,g,1\) cannot cancel.
Hence (5) gives a vertex of degree
\[
q^{N/e}-1.
\tag{8}
\]

Conversely, if \(x^2\ne0\), then (4) and (7) give
\[
\deg(x)\ge q^{N/e}-1.
\]
If \(x^2=0\), then \(M_x^2=0\), so
\(\dim_K\ker M_x\ge N/2>N/e\). Since the kernel dimension is integral, it is
at least \(N/e+1\), and hence
\[
\deg(x)\ge q^{N/e+1}-2>q^{N/e}-1.
\]
Together with (8), this proves (1).

### 3. The exponent is a graph invariant in the modular abelian case

Aliniaeifard and Li, using earlier results of Akbari and Mohammadian, proved
that an isomorphism
\[
\Gamma(KG)\cong\Gamma(LH)
\]
between finite group-algebra zero-divisor graphs determines the coefficient
field and group order, and that abelianness of \(G\) forces abelianness of
\(H\). Thus in the situation of (2), \(K\cong L\), \(|G|=|H|=N\), and \(H\)
is again an abelian \(p\)-group.

The two graphs have the same minimum degree. If one exponent were \(2\) and
the other were \(>2\), (1) would give
\[
q^{N/2}-2=q^{N/e'}-1
\]
for some \(e'>2\), so two positive powers of \(q\) would differ by \(1\),
which is impossible because both are divisible by \(q\). Hence either both
exponents are \(2\), or both exceed \(2\). In the latter case, (1) gives
\[
q^{N/\exp(G)}=q^{N/\exp(H)},
\]
and therefore \(\exp(G)=\exp(H)\). This proves (2).

Finally, over \(K=\mathbf F_p\), Aliniaeifard and Li also proved that the rank
of a finite abelian \(p\)-group is determined by its modular zero-divisor
graph. A rank-two group has the form
\[
C_{p^a}\times C_{p^b},\qquad a\ge b\ge1.
\]
Its order determines \(a+b\), while its exponent determines \(a\); hence both
\(a\) and \(b\) are determined. Rank one is the cyclic case, already covered
by the earlier isomorphism theorem. This proves the final assertion.

## Relation to prior work

Aliniaeifard and Li proved in 2014 that the zero-divisor graph of a modular
group ring determines the order and, over the prime field, the rank of a
finite abelian \(p\)-group. Their Section 3 reduces a substantial part of the
group-ring zero-divisor-graph isomorphism problem to the modular \(p\)-group
case. They do not state an exponent formula or the rank-two classification
above.

The degree identity (7) is standard for finite commutative zero-divisor
graphs. The new point is the sharp annihilator estimate (4)--(6), obtained
from the exponent bound \(x^e=0\), and its conversion into the exact
minimum-degree formula (1).

Later papers located during the literature check concern different graph
constructions (annihilator graphs of group rings) or semisimple group rings,
where the characteristic does not divide the relevant group order. No
statement recovering the exponent of an abelian \(p\)-group from the
ordinary modular zero-divisor graph was located.

## Limitations

Originality is asserted only to the best of our knowledge. The argument is
short and uses standard facts about modular group algebras and nilpotent
linear maps, so an implicit or differently phrased antecedent remains
possible.

The exponent formula requires \(G\) to be abelian; equation (3) uses
commutativity of \(KG\). The rank-two isomorphism corollary is stated over
the prime field because the cited rank-determination theorem is stated in
that setting. The result does not classify all finite abelian \(p\)-groups
from their zero-divisor graphs: order, rank, and exponent do not determine
an abelian \(p\)-group of arbitrary rank.

## References

1. F. Aliniaeifard and Y. Li, *Zero-Divisor Graphs for Group Rings*,
   Communications in Algebra 42 (2014), 4790--4800.
   https://doi.org/10.1080/00927872.2013.827689

2. S. Akbari and A. Mohammadian, *On zero-divisor graphs of finite rings*,
   Journal of Algebra 314 (2007), 168--184.
   https://doi.org/10.1016/j.jalgebra.2007.02.051

3. P. K. Prasobha and G. Suresh Singh, *Annihilator graphs derived from group
   rings*, Gulf Journal of Mathematics 15 (2023), 109--116.
   https://doi.org/10.56947/gjom.v15i2.1602

4. K. Paramasivam and K. Muhammed Sabeel, *Zero-divisor graph of semisimple
   group-rings*, Journal of Algebra and Its Applications 21 (2022), 2250028.
   https://doi.org/10.1142/S0219498822500281
