# Characteristic-two index-three Rota–Baxter operators on square-zero local algebras

## Finding
Let \(k\) be any field, let \(d\geq1\), and put \(A_d(k)=k\oplus V\) with \(\dim_k V=d\), identity \(1\), and \(V^2=0\). A weight-zero Rota–Baxter operator is a \(k\)-linear endomorphism \(R\) satisfying \(R(x)R(y)=R(R(x)y+xR(y))\) for all \(x,y\in A_d(k)\).

Every such operator has a unique block matrix relative to \(k1\oplus V\):
\[
 R=\begin{pmatrix}0&0\\ u&B\end{pmatrix},\qquad B^2=0,\qquad 2Bu=0.
\]
In particular, in characteristic two \(u\) is unrestricted, \(R^3=0\), and \(R^2\ne0\) exactly when \(Bu\ne0\); for \(d\ge2\) this is a nonempty Zariski-open dense locus. In characteristics other than two, every such operator satisfies \(R^2=0\).

Put \(r=\lfloor d/2\rfloor\). Over any field of characteristic two, the **reduced** algebraic variety of these operators is geometrically irreducible and rational of dimension \(2r(d-r)+d\). In all other characteristics, its reduced variety is geometrically irreducible and rational of dimension \((d-r)(2r+1)\). Thus the dimension jumps upward by exactly \(r\) in characteristic two.

For a prime power \(q\), set
\[
 N_{d,j}(q)={d\brack j}_q{d-j\brack j}_q\prod_{i=0}^{j-1}(q^j-q^i),\qquad 0\le j\le r,
\]
where Gaussian coefficients count vector subspaces, and the empty product is one. The joint polynomial recording operator rank by \(z\) and the condition \(R^2\ne0\) by \(t\) is, for even \(q\),
\[
 F_d(q;z,t)=\sum_{j=0}^{r}N_{d,j}(q)\left[q^jz^j+(q^{d-j}-q^j)z^{j+1}+(q^d-q^{d-j})tz^{j+1}\right].
\]
The coefficient of \(z^s t^\epsilon\) counts operators with rank \(s\) and \(\epsilon=1\) precisely when their square is nonzero. For odd \(q\), the corresponding polynomial is
\[
 F_d(q;z,t)=\sum_{j=0}^{r}N_{d,j}(q)\left[q^jz^j+(q^{d-j}-q^j)z^{j+1}\right]
\]
(with no \(t\)-terms). In particular, total counts are \(q^d\sum_jN_{d,j}(q)\) for even \(q\) and \(\sum_jq^{d-j}N_{d,j}(q)\) for odd \(q\).

## Assumptions and scope
The algebra \(A_d(k)\) is unital, commutative, finite-dimensional, and split with radical \(V\) of square zero. All linear maps and Rota–Baxter operators are labelled, not modulo algebra automorphisms. The complete classification and geometric conclusions hold over arbitrary fields, including imperfect fields. The point counts hold over every finite field (including nonprime finite fields). Rank is the rank of \(R:A_d(k)\to A_d(k)\), not of its restriction \(B:V\to V\). Geometric assertions refer only to reduced varieties, not potentially nonreduced defining schemes.

## Proof
**1. Reduction to a square-zero matrix and a vector.** Write \(R(1)=a+u\) and \(R(v)=f(v)+Bv\), with \(a\in k\), \(u\in V\), a linear functional \(f:V\to k\), and \(B\in\operatorname{End}(V)\). For \(v,w\in V\), compare scalar terms in the Rota–Baxter identity: its left side is \(f(v)f(w)\), while its right side is \(2f(v)f(w)\). Hence \(f(v)f(w)=0\), and taking \(v=w\) shows \(f=0\), over every field. With \(f=0\), comparison at \((1,v)\) gives \(B^2v=0\). Finally, the scalar and radical parts at \((1,1)\) give \(a^2=2a^2\), so \(a=0\), and \(2Bu=0\). Conversely, under these conditions, for \(x=c+v\), \(y=e+w\), the left side is zero, and the right side equals \(cB^2w+eB^2v+2ceBu=0\). Thus the conditions are necessary and sufficient, with no assumption that two is invertible.

Direct matrix multiplication yields \(R^2(1)=Bu\), \(R^2(V)=0\), and \(R^3=0\). For characteristic two and \(d\ge2\), choose a nonzero square-zero rank-one \(B\), then choose \(u\notin\ker B\). Such operators have exact nilpotency index three. For example, with \(d=2\), \(B(e_1)=e_2\), \(B(e_2)=0\), and \(u=e_1\), the map has one Jordan block of size three on \(k1\oplus V\). The condition \(Bu\ne0\) is open. The irreducibility below proves it is dense; it is also compatible with the generic maximal rank \(r\).

**2. Geometric structure.** Put \(r=\lfloor d/2\rfloor\). For any \(B^2=0\), let \(j=\operatorname{rank}B\le r\). Then \(\operatorname{im}B\subseteq\ker B\), with dimensions \(j\) and \(d-j\). The square-zero matrix variety is irreducible: every rank-\(j\) matrix is a specialization of a rank-\(r\) square-zero matrix obtained by adding \(r-j\) independent two-by-two nilpotent blocks on the trivial-block complement. The rank-\(r\) locus is a single \(\mathrm{GL}_d\)-orbit, hence irreducible. Its dimension is \(2r(d-r)\), since the image/kernel incidence variety over \(\operatorname{Gr}(d-r,V)\) is generically birational: choose \(K\) of dimension \(d-r\), choose \(B\in\operatorname{Hom}(V/K,K)\) (a space of dimension \(r(d-r)\)), and at rank \(r\) the choice \(K=\ker B\) is unique. This incidence space is a vector bundle over a Grassmannian, hence rational. In characteristic two the Rota–Baxter variety is its product with \(V\), giving dimension \(2r(d-r)+d\).

In characteristic different from two, the reduced variety consists of \((B,u)\) with \(B^2=0\) and \(u\in\ker B\). Consider the incidence space of triples \((K,B,u)\), with \(K\in\operatorname{Gr}(d-r,V)\), \(B(K)=0\), \(\operatorname{im}B\subseteq K\), and \(u\in K\). Over \(K\) this is a vector bundle of rank \(r(d-r)+(d-r)\). The projection is surjective: for any pair \((B,u)\), a \((d-r)\)-plane can be chosen between \(\operatorname{im}B+ku\) and \(\ker B\). Indeed, for \(j<r\), the former has dimension at most \(j+1\le d-r\); at \(j=r\), the kernel has dimension \(d-r\), so take \(K=\ker B\). On the dense rank-\(r\) locus the only choice is \(K=\ker B\). Thus the reduced image is irreducible, rational, and of dimension \(r(d-r)+r(d-r)+(d-r)=(d-r)(2r+1)\). Subtraction gives the dimension jump \(r\).

**3. Finite-field distribution.** A square-zero \(d\)-by-\(d\) matrix \(B\) of rank \(j\) is determined by an image \(U\) (\({d\brack j}_q\) choices), a kernel \(K\supseteq U\) of dimension \(d-j\) (\({d-j\brack j}_q\) choices), and an isomorphism \(V/K\to U\) (\(\prod_{i=0}^{j-1}(q^j-q^i)\) choices). This gives \(N_{d,j}(q)\).

For fixed \(B\), \(\operatorname{rank}R=\dim(\operatorname{im}B+ku)\). There are exactly \(q^j\) vectors \(u\in\operatorname{im}B\), yielding rank \(j\). In characteristic two, another \(q^{d-j}-q^j\) vectors lie in \(\ker B\setminus\operatorname{im}B\), yielding rank \(j+1\) but \(R^2=0\). The remaining \(q^d-q^{d-j}\) vectors yield rank \(j+1\) and \(R^2\ne0\). For odd \(q\), only \(u\in\ker B\) is admissible; the first two quantities remain. Summing over \(j\) proves the formulas. There are no other cases.

## Verification
The standalone program `checker.py` contains independent multiplication-table tests of the defining Rota–Baxter identity, finite-field matrix arithmetic (including \(\mathbb F_4\)), rank computations, and a separate Gaussian-coefficient enumerator. It completely enumerates **all linear maps** of \(A_d(k)\) for \((d,q)=(1,2),(1,3),(2,2),(2,3),(2,4),(3,2)\), and exhausts all square-zero radical blocks and augmentation vectors for \((d,q)=(3,3),(4,2),(3,4)\). All nine configurations agree with the classification and the rank/index polynomial. The final marker is `ROTA_BAXTER_MODULAR_SQUARE_ZERO_OK`. Finite checks are corroboration, not substitutes for the proof of the universal assertions.

In particular, the rank/index distributions (the second index records whether the operator square is nonzero) are \((0,0):1,(1,0):9,(2,1):6\) for \((d,q)=(2,2)\); \((0,0):1,(1,0):75,(2,1):180\) for \((2,4)\); and \((0,0):1,(1,0):49,(2,0):42,(2,1):84\) for \((3,2)\).

## Relationship to prior work
Guo, Rosenkranz, and Zheng [1] classify weight-zero Rota–Baxter operators on semigroup algebras of orders two and three over characteristic-zero fields; their operator identity and low-dimensional motivation do not supply the present unrestricted characteristic-two family. Farooq [2, Theorem 3.4] proves the block condition \(B^2=0\), \(Bu=0\) for this same truncated local algebra in characteristic zero. That result and its immediate odd-characteristic extension are acknowledged, not represented as new. The new boundary is the disappearance of \(Bu=0\) in characteristic two, producing a dense index-three locus, a precisely \(\lfloor d/2\rfloor\)-dimensional moduli jump, and a joint finite-field rank/index census.

The space of arbitrary pairs \((u,B)\) with nilpotent \(B\), and its orbit geometry, is the enhanced nilpotent cone studied by Achar and Henderson [3]. The standard square-zero nilpotent-matrix orbit structure and Gaussian counts are used rather than claimed as inventions. The cited sources do not state the characteristic-two Rota–Baxter identification or its index-three consequences. This is a best-knowledge originality assessment rather than an exhaustive proof of publication priority.

## Limitations
Only weight-zero operators on split unital local algebras with square-zero radical are considered. The formulas count labelled operators and do not separately count automorphism-conjugacy classes. The geometric statements concern reduced algebraic varieties; no assertion about reducedness or singularity of the original operator equation schemes is made. Higher radical nilpotency, nonzero operator weights, and non-split base algebras are outside scope. Existing enhanced-nilpotent theory covers some constituent orbit geometry. Independent mathematical audit and exhaustive literature-priority verification have not been performed.

## References
[1] Li Guo, Markus Rosenkranz, Shanghua Zheng, *Classification of Rota-Baxter operators on semigroup algebras of order two and three*, arXiv:1402.3702, first posted 2014-02-15. https://arxiv.org/abs/1402.3702

[2] Azhar Farooq, *Rota Baxter Operators on Truncated Polynomial Algebras*, arXiv:2605.15670, first posted 2026-05-15. https://arxiv.org/abs/2605.15670

[3] Pramod N. Achar, Anthony Henderson, *Orbit closures in the enhanced nilpotent cone*, arXiv:0712.1079, first posted 2007-12-07. https://arxiv.org/abs/0712.1079 (consult the 2010 corrigendum arXiv:1008.1117 concerning an affine-paving argument, not the basic orbit parametrization).
