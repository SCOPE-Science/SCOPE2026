# Kernel-wreath abelianization order and the exterior-square correction

## Statement

Let \(R\) be a finite group, let \(T\neq 1\) be a finite abelian group, and let \(\chi:R\twoheadrightarrow T\) be an epimorphism. Let \(T\) act regularly on the coordinates of \(R^T\), put
\[
W=R^T\rtimes T,
\]
and define
\[
\varepsilon((r_x)_{x\in T},u)=\left(\prod_{x\in T}\chi(r_x)\right)u.
\]
Write \(G=\ker\varepsilon\), the multiplicative group in the kernel-wreath construction of Damele.

Then
\[
\boxed{|G^{\mathrm{ab}}|=|R^{\mathrm{ab}}|\,|T|\,|\bigwedge^2 T|.}
\]
Equivalently, using \(|G|=|R|^{|T|}\),
\[
\boxed{|G'|=\frac{|R|^{|T|}}{|R^{\mathrm{ab}}|\,|T|\,|\bigwedge^2T|}.}
\]
Here \(\bigwedge^2T\) is the exterior square over \(\mathbb Z\). If
\[
T\cong\bigoplus_{i=1}^d C_{n_i},
\]
then
\[
|\bigwedge^2T|=\prod_{i<j}\gcd(n_i,n_j).
\]
In particular, for cyclic \(T\),
\[
|G^{\mathrm{ab}}|=|T|\,|R^{\mathrm{ab}}|,
\]
and for the prime-cyclic step \(T=C_p\), the abelianization order is multiplied exactly by \(p\).

Damele proves that \(G\) has order \(|R|^{|T|}\) and that every finite abelian quotient of \(R\) survives as a quotient of \(G\). The formula above determines the full order of the first derived quotient, and shows that a noncyclic target contributes an additional factor \(|\bigwedge^2T|\), the order of the Schur multiplier of the abelian group \(T\).

## Proof

### 1. Reduction to an abelian base

Let
\[
A=R^{\mathrm{ab}}=R/R'.
\]
Because \(T\) is abelian, \(\chi\) factors through an epimorphism \(\bar\chi:A\twoheadrightarrow T\). Coordinatewise abelianization induces an epimorphism
\[
q:G\twoheadrightarrow H,
\]
where
\[
H=\ker\!\left(A^T\rtimes T\longrightarrow T\right)
\]
for the corresponding kernel-wreath map, and
\[
\ker q=(R')^T.
\]
We claim that \((R')^T\leq G'\).

Fix a coordinate \(i\). If \(|T|\geq3\), choose two further distinct coordinates \(j,k\). For \(r,s\in R\), let \(x\in G\) have base entries \(r,r^{-1}\) at \(i,j\), respectively, and identity elsewhere, with trivial top component. Let \(y\in G\) have base entries \(s,s^{-1}\) at \(i,k\), respectively. Both lie in \(G\), and their commutator has entry \([r,s]\) at \(i\) and identity at every other coordinate. Hence every coordinate copy of every commutator of \(R\) lies in \(G'\).

If \(|T|=2\), then \(T=C_2\). Let \(c\) be its nontrivial element and choose \(t\in R\) with \(\chi(t)=c\). For \(r,s\in R\), write \(\chi(r)=c^\alpha\) and \(\chi(s)=c^\beta\), with \(\alpha,\beta\in\{0,1\}\). At the other coordinate, compensate \(r\) by \(t^{-\alpha}\) and \(s\) by \(t^{-\beta}\). The two compensating entries commute because they are powers of the same element \(t\), so again the commutator isolates \([r,s]\) in the chosen coordinate. Thus \((R')^T\leq G'\) also in this case.

Therefore
\[
G^{\mathrm{ab}}\cong H^{\mathrm{ab}}.
\]
It remains to compute the latter when the base group \(A\) is abelian.

### 2. The kernel as an extension

Use additive notation for \(A\) and \(T\), and put
\[
M=A^T.
\]
Let
\[
f:M\longrightarrow T,\qquad f((a_x))=\sum_{x\in T}\bar\chi(a_x).
\]
Then
\[
H=\{(m,u)\in M\rtimes T:f(m)+u=0\}.
\]
Set \(K=\ker f\). Projection to the top group gives an exact sequence
\[
1\longrightarrow K\longrightarrow H\longrightarrow T\longrightarrow1.
\]
Conjugation by a lift of \(u\in T\) acts on \(K\) by the regular coordinate permutation. Hence
\[
[H,K]=I_TK,
\]
where \(I_T\) is the augmentation ideal, and
\[
K_T:=K/I_TK
\]
is the group of coinvariants.

The short exact sequence of \(T\)-modules
\[
0\longrightarrow K\longrightarrow M\overset f\longrightarrow T\longrightarrow0
\]
has trivial action on the target \(T\). Since
\[
M\cong \mathbb Z[T]\otimes_{\mathbb Z}A
\]
is induced from the trivial subgroup, Shapiro's lemma gives \(H_1(T,M)=0\). The homology exact sequence therefore yields
\[
0\longrightarrow H_1(T,T)\overset\delta\longrightarrow K_T
\longrightarrow M_T\longrightarrow T\longrightarrow0.
\]
Here
\[
H_1(T,T)\cong T\otimes_{\mathbb Z}T,
\qquad M_T\cong A,
\]
and the map \(M_T\to T\) is \(\bar\chi\). Thus
\[
\boxed{0\longrightarrow T\otimes T\overset\delta\longrightarrow K_T
\longrightarrow\ker\bar\chi\longrightarrow0.}
\]
Consequently,
\[
|K_T|=|T\otimes T|\,|\ker\bar\chi|.
\]

### 3. The commutator correction

For \(u\in T\), choose \(m_u\in M\) with \(f(m_u)=-u\), and let \(\widetilde u=(m_u,u)\in H\). Modulo \([H,K]\), a direct semidirect-product commutator computation gives
\[
[\widetilde u,\widetilde v]
=\delta(v\otimes u-u\otimes v)
\quad\text{in }K_T,
\]
up to the harmless global sign determined by the commutator convention. Since \(K\) is abelian and \(H/K\cong T\) is abelian, these lift commutators generate \(H'/[H,K]\). Therefore
\[
H'/[H,K]=\delta(\operatorname{Alt}(T)),
\]
where \(\operatorname{Alt}(T)\) is generated in \(T\otimes T\) by all \(u\otimes v-v\otimes u\).

The map \(\delta\) is injective. If \(T\cong\bigoplus_iC_{n_i}\) with standard generators \(e_i\), then \(\operatorname{Alt}(T)\) is generated independently by
\[
e_i\otimes e_j-e_j\otimes e_i\qquad(i<j),
\]
and the corresponding generator has order \(\gcd(n_i,n_j)\). Hence
\[
|H'/[H,K]|=|\operatorname{Alt}(T)|
=\prod_{i<j}\gcd(n_i,n_j)
=|\bigwedge^2T|.
\]
It follows that
\[
|K/H'|=\frac{|K_T|}{|\bigwedge^2T|}.
\]
Because \(H'\leq K\) and \(H/K\cong T\),
\[
|H^{\mathrm{ab}}|
=|T|\,|K/H'|
=|T|\frac{|T\otimes T|\,|\ker\bar\chi|}{|\bigwedge^2T|}.
\]
Now \(|\ker\bar\chi|=|A|/|T|\), so
\[
|H^{\mathrm{ab}}|=|A|\frac{|T\otimes T|}{|\bigwedge^2T|}.
\]
For \(T\cong\bigoplus_iC_{n_i}\),
\[
|T\otimes T|
=\prod_i n_i\prod_{i<j}\gcd(n_i,n_j)^2
=|T|\,|\bigwedge^2T|^2.
\]
Therefore
\[
|H^{\mathrm{ab}}|=|A|\,|T|\,|\bigwedge^2T|,
\]
and since \(A=R^{\mathrm{ab}}\), the theorem follows.

## Consequences

### Exact size of the preserved-quotient kernel

Damele's preservation map, specialized to the quotient \(R\twoheadrightarrow R^{\mathrm{ab}}\), factors through an epimorphism
\[
\overline\Theta:G^{\mathrm{ab}}\twoheadrightarrow R^{\mathrm{ab}}.
\]
The theorem gives
\[
\boxed{|\ker\overline\Theta|=|T|\,|\bigwedge^2T|.}
\]
This is an order statement, not a splitting statement. For example, if \(R=T=C_2\) and \(\chi\) is the identity, then \(G\cong C_4\); the resulting extension of \(C_2\) by \(C_2\) is nonsplit.

### Iteration with a fixed target

The source construction preserves \(T\) itself as an abelian quotient, so the same target can be used repeatedly. If \(R_m\) denotes the multiplicative group after \(m\) steps using the same \(T\), then
\[
|R_m|=|R_0|^{|T|^m}
\]
and
\[
\boxed{|R_m^{\mathrm{ab}}|
=(|T|\,|\bigwedge^2T|)^m|R_0^{\mathrm{ab}}|.}
\]
Consequently,
\[
\boxed{|R_m'|
=\frac{|R_0|^{|T|^m}}
{(|T|\,|\bigwedge^2T|)^m|R_0^{\mathrm{ab}}|}.}
\]
For the prime-cyclic towers in the source, \(T=C_p\) and \(\bigwedge^2C_p=0\), so
\[
|R_m^{\mathrm{ab}}|=p^m|R_0^{\mathrm{ab}}|.
\]

### A noncyclic example

Take \(R=Q_8\) and let \(\chi:Q_8\twoheadrightarrow Q_8^{\mathrm{ab}}\cong C_2^2=T\). Then
\[
|R^{\mathrm{ab}}|=4,
\qquad |T|=4,
\qquad |\bigwedge^2T|=2,
\]
so the kernel-wreath multiplicative group has
\[
|G^{\mathrm{ab}}|=32.
\]
Thus preservation of the old quotient of order \(4\) accounts for only part of the new abelianization; the target's exterior square supplies an additional factor.

## Relation to prior work and originality boundary

Damele's arXiv:2609.20401v1 introduces the kernel-wreath group \(G\), proves \(|G|=|R|^{|T|}\), proves that arbitrary finite abelian quotients of \(R\) survive in \(G\), and derives iterable skew-brace towers. Those statements are prior work. The paper does not state an abelianization, derived-subgroup, commutator, or exterior-square formula.

The abelianization of a full regular wreath product with abelian base is standard: it is controlled by coordinate augmentation together with the abelianization of the top group. The present group is instead the index-\(|T|\) kernel cut out by the coupled augmentation/top relation, and abelianization does not commute with taking such a kernel. The extra \(|\bigwedge^2T|\) factor records precisely the commutator correction in that kernel.

To the best of our knowledge, searches for equivalent formulations using kernel/augmentation subgroups of regular wreath products, abelianization, derived subgroups, Schur multipliers, and exterior squares did not locate the formula above. Older wreath-product and group-extension literature was not exhaustively checked theorem-by-theorem, so an equivalent result under different terminology remains a residual originality risk.

## Limitations

The theorem determines the order of \(G^{\mathrm{ab}}\), not its full invariant-factor decomposition. In particular, the natural epimorphism \(G^{\mathrm{ab}}\twoheadrightarrow R^{\mathrm{ab}}\) need not split. No independent validation is asserted.

## References

1. M. Damele, *Kernel--wreath constructions and infinite families of finite simple skew braces*, arXiv:2609.20401v1 (2026).
2. H. Bradford and F. Fournier-Facio, *Hopfian wreath products and the stable finiteness conjecture*, arXiv:2211.01510 (for standard wreath-product morphisms and augmentation structure).
3. K. S. Brown, *Cohomology of Groups*, Graduate Texts in Mathematics 87, Springer (for Shapiro's lemma and the homology exact sequence used above).
