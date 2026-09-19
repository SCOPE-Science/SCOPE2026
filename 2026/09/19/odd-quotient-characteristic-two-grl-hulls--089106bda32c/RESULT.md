# Odd-quotient characteristic-two hull universality for generalized Roth--Lempel codes

## Statement

Let
\[
q=2^e,\qquad 1\le \ell\le e-1,\qquad d=\gcd(e,\ell),
\]
and assume that
\[
\frac{e}{d}\quad\text{is odd}.
\]
Put \(r=2^\ell\). Let \(a=(a_1,\ldots,a_n)\) be any vector of pairwise distinct elements of \(\mathbb F_q\), let
\[
u_i=\prod_{j\ne i}(a_i-a_j)^{-1},
\]
and let \(A_s\in\operatorname{GL}_s(\mathbb F_q)\) be arbitrary.

**Theorem 1 (arbitrary-skeleton prescribed hulls).** For every
\[
s<k\le \left\lfloor\frac{n+r-1}{r+1}\right\rfloor
\]
and every
\[
0\le h\le k-s,
\]
there exists a multiplier vector \(v\in(\mathbb F_q^*)^n\) such that
\[
C=\operatorname{GRL}_k(a,v,A_s)
\]
has
\[
\dim \operatorname{Hull}_\ell(C)=h.
\]

Thus, in this characteristic-two regime, prescribed \(\ell\)-Galois hull dimension requires no special evaluation-set structure, no subfield condition on the Lagrange coefficients, and no restriction on the nonsingular extension matrix.

**Corollary 2 (distance-neutral hull tuning).** Fix \((a,A_s,k)\) in the range of Theorem 1. All choices of nonzero multipliers are related by a diagonal Hamming isometry on the first \(n\) coordinates. Consequently, every classical Hamming weight distribution obtainable from this fixed GRL skeleton is preserved while the \(\ell\)-Galois hull dimension is tuned to any value \(0,1,\ldots,k-s\). In particular, any MDS, AMDS, or NMDS skeleton satisfying the hypotheses admits all these hull dimensions without changing its classical distance profile.

The theorem includes parameter regimes excluded by the condition \(2\ell\mid e\) used in Wu--Liu--Chen--Zhou. For example:

- over \(\mathbb F_{32}\), \(e=5,\ell=2\), the full evaluation set \(n=32\) and \(s=2\) permit every \(h\in[0,k-2]\) for \(3\le k\le7\);
- over \(\mathbb F_{64}\), \(e=6,\ell=2\), the full evaluation set \(n=64\) and \(s=2\) permit every \(h\in[0,k-2]\) for \(3\le k\le13\).

The first example also has \(\ell\nmid e\).

## Finite-field lemma

The mechanism is the following elementary power-map fact.

**Lemma 3.** Under the hypotheses of Theorem 1,
\[
\gcd(2^\ell+1,2^e-1)=1.
\]
Hence
\[
\varphi:\mathbb F_q^*\to\mathbb F_q^*,\qquad x\mapsto x^{r+1},
\]
is a bijection.

**Proof.** Write \(e=db\) and \(\ell=da\), with \(\gcd(a,b)=1\) and \(b\) odd. Let \(D\) divide both \(2^\ell+1\) and \(2^e-1\), and put \(x=2^d\). Then
\[
x^a\equiv-1\pmod D,\qquad x^b\equiv1\pmod D.
\]
Raising the first congruence to the odd power \(b\) and the second to the power \(a\) gives
\[
x^{ab}\equiv-1\pmod D,\qquad x^{ab}\equiv1\pmod D.
\]
Thus \(D\mid2\). Both original integers are odd, so \(D=1\). The multiplicative group \(\mathbb F_q^*\) is cyclic of order \(q-1\), so exponentiation by \(r+1\) is bijective. \(\square\)

This odd-quotient characteristic-two field regime is not itself claimed as new. Wan--Zhu explicitly treat the corresponding case \(m/\gcd(m,e)\) odd with \(p=2\) for GRS/EGRS Galois self-orthogonality and obtain arbitrary-hull MDS codes by propagation. The new point here is its consequence for the generalized Roth--Lempel dual equations, where it removes all evaluation-set restrictions in the low-degree prescribed-hull range.

## Proof of Theorem 1

Let \(t\) be the inverse of \(r+1\) modulo \(q-1\). By Lemma 3, for every Lagrange coefficient \(u_i\) there is a unique
\[
w_i=u_i^t\in\mathbb F_q^*
\]
with
\[
w_i^{r+1}=u_i.
\]
Choose any \(\beta\in\mathbb F_q^*\setminus\{1\}\), and put
\[
\gamma=\beta^{r+1}.
\]
Bijectivity of the same power map gives \(\gamma\ne1\).

For a requested hull dimension \(h\), set
\[
z=k-s-h
\]
and define
\[
v_i=\begin{cases}
\beta w_i,&1\le i\le z,\\
w_i,&z<i\le n.
\end{cases}
\]

We use the polynomial characterization of the Galois dual of a GRL code from Proposition II.8 of Wu--Liu--Chen--Zhou. Let \(c_f\) be the codeword associated with \(f\in\mathbb F_q[x]\), \(\deg f<k\). Then \(c_f\in C^{\perp_\ell}\) if and only if there is a polynomial \(g\) with
\[
\deg g\le n-k+s-1
\]
such that
\[
v_i^{r+1}f^r(a_i)=u_i g(a_i)\qquad(1\le i\le n)
\]
and the final \(s\) coefficient coordinates satisfy the GRL extension equation.

Suppose first that \(c_f\in\operatorname{Hull}_\ell(C)\). For \(i>z\), the multiplier choice gives
\[
u_i f^r(a_i)=u_i g(a_i),
\]
so
\[
f^r(a_i)=g(a_i).
\]
The bound on \(k\) implies
\[
(r+1)k\le n+r-1,
\]
hence
\[
r(k-1)\le n-k-1.
\]
Therefore
\[
\deg(f^r)\le n-k-1,
\]
while \(\deg g\le n-k+s-1\). The polynomial \(g-f^r\) vanishes at
\[
n-z=n-k+s+h\ge n-k+s
\]
distinct evaluation points, more than its possible degree. Thus
\[
g=f^r.
\]

Because \(\deg g\le n-k-1\), the last \(s\) coefficients appearing on the right side of the GRL extension equation vanish. Since \(A_s^{(r)}\) is nonsingular, the left side then forces
\[
f_{k-s}=\cdots=f_{k-1}=0,
\]
so
\[
\deg f\le k-s-1.
\]
For \(i\le z\), comparison of the scaled and unscaled equations now gives
\[
(\gamma-1)f^r(a_i)=0.
\]
Since \(\gamma\ne1\),
\[
f(a_i)=0\qquad(1\le i\le z).
\]
Consequently
\[
f(x)=c(x)\prod_{i=1}^z(x-a_i),
\qquad \deg c\le h-1.
\]
This proves that the hull has dimension at most \(h\).

Conversely, take any polynomial of the displayed form with \(\deg c\le h-1\), and put \(g=f^r\). Then \(\deg f\le k-s-1\) and, by the same degree estimate,
\[
\deg g\le n-k-1.
\]
For \(i>z\), the dual equation holds because \(v_i^{r+1}=u_i\). For \(i\le z\), both sides vanish because \(f(a_i)=0\). The final extension equation has both sides zero. Hence every such \(f\) gives a hull codeword. These polynomials form an \(h\)-dimensional space, so
\[
\dim\operatorname{Hull}_\ell(C)=h.
\]
\(\square\)

## Proof of Corollary 2

For two multiplier vectors \(v,v'\in(\mathbb F_q^*)^n\), the coordinate map
\[
(x_1,\ldots,x_n,y_1,\ldots,y_s)
\mapsto
\left(\frac{v_1'}{v_1}x_1,\ldots,\frac{v_n'}{v_n}x_n,y_1,\ldots,y_s\right)
\]
sends \(\operatorname{GRL}_k(a,v,A_s)\) onto \(\operatorname{GRL}_k(a,v',A_s)\). It is a monomial Hamming isometry. Thus the complete weight distribution and minimum distance are unchanged; the same holds for the dual distance. Theorem 1 supplies a multiplier choice for each desired hull dimension. \(\square\)

## Relation to prior work

Wu--Liu--Chen--Zhou study prescribed Galois hulls of GRL codes over \(q=p^e\) under the standing assumption \(2\ell\mid e\). Their Proposition II.8 gives the GRL dual characterization used above. Their Lemma II.9 notes a special characteristic-two root phenomenon when \(\ell\mid e\), but the paper explicitly retains \(2\ell\mid e\) for the subsequent constructions. Their common Proposition III.2 obtains \(0\le h\le k-s\) after requiring normalized Lagrange coefficients to lie in \(\mathbb F_{p^\ell}^*\).

Wan--Zhu treat GRS and extended GRS codes for all Galois exponents. In particular, their classification includes the characteristic-two case where the extension degree divided by the relevant gcd is odd, and they obtain MDS codes with arbitrary Galois hull dimensions by propagation. This establishes important prior art for the finite-field regime and for GRS hull control. It does not, in the inspected material, give the arbitrary-evaluation, arbitrary-extension-matrix GRL statement above.

Earlier GRL work includes Hermitian self-orthogonality and MDS/NMDS criteria, but Hermitian duality corresponds to an even quotient and does not cover the odd-quotient regime of Theorem 1.

The originality claim is therefore restricted to the GRL consequence: in characteristic two with \(e/\gcd(e,\ell)\) odd, every GRL evaluation/extension skeleton in the stated dimension range admits every hull dimension \(0,\ldots,k-s\), with hull tuning that is neutral to the classical distance profile. The power-map lemma and the analogous GRS regime are not claimed as new.

## Verification

`artifacts/verify.py` performs two finite checks. First, it verifies the power-map gcd identity for a range of exponents. Second, it constructs GRL generator matrices over representative binary extension fields, using arbitrary sampled evaluation sets and arbitrary invertible extension matrices, and computes
\[
\dim\operatorname{Hull}_\ell(C)
=k-\operatorname{rank}\bigl(G(G^{(2^\ell)})^{\mathsf T}\bigr)
\]
directly. The cases include \((e,\ell)=(5,2)\), where \(\ell\nmid e\). The recorded output is in `artifacts/verification.txt`.

The finite computation is a sanity check; the general result is proved algebraically above.

## Limitations

The result retains the low-degree range
\[
k\le\left\lfloor\frac{n+2^\ell-1}{2^\ell+1}\right\rfloor.
\]
It does not extend the larger-dimension self-orthogonality constructions known for some GRS families, does not classify which GRL skeletons are MDS/AMDS/NMDS, and does not address odd characteristic. It also does not assert novelty for the underlying characteristic-two power-map bijection. Because the motivating GRL hull preprint is very recent, a near-simultaneous observation or later revision remains a material originality risk.

## References

1. X. Wu, Q. Liu, Y. Chen, and H. Zhou, *Galois Hulls of Generalized Roth-Lempel Codes and Their Applications to EAQECCs*, arXiv:2609.20453, 2026. https://arxiv.org/abs/2609.20453
2. R. Wan and S. Zhu, *Galois self-orthogonal MDS codes with large dimensions*, arXiv:2412.05011, 2024. https://arxiv.org/abs/2412.05011
3. Q. Liu, X. Wu, and H. Zhou, *Generalized Roth--Lempel Codes: NMDS Characterization, Hermitian Self-Orthogonality, and Quantum Constructions*, arXiv:2604.11350, 2026. https://arxiv.org/abs/2604.11350
