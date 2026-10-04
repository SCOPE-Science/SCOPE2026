# Domination polynomials of finite local unit graphs determine the residue-fiber geometry

## Finding

Let \(R\) be a finite commutative local ring with maximal ideal \(M\), \(q=|R/M|\), \(s=|M|\), and \(N=qs\). For its unit graph \(G(R)\), the ordinary and total domination polynomials have closed forms depending only on \((q,s)\) and whether \(\operatorname{char}(R/M)=2\). In particular, if \(\kappa=q\) in residue characteristic \(2\) and \(\kappa=1\) otherwise, then \[D(G(R),x)=(1+x)^N-q(1+x)^s+(q-1)+\kappa x^s.\] If the residue characteristic is \(2\), \[D_t(G(R),x)=(1+x)^N-q(1+x)^s+(q-1).\] If it is odd, writing \(A=(1+x)^s-1\), \[D_t(G(R),x)=(1+x)^N-q(1+x)^s+(q-1)-\frac{q-1}{2}\big(A^2-(A-sx)^2\big).\] Moreover, the ordinary domination polynomial alone recovers \(q\), \(s\), and the parity of the residue characteristic, and hence determines the unit-graph isomorphism type among finite commutative local rings.

The formulas classify every dominating set and every total dominating set, not only the minimum cardinalities.

## Assumptions and scope

Let \(R\) be a finite commutative local ring with identity, maximal ideal \(M\), residue field \(F=R/M\), \(q=|F|\), \(s=|M|\), and \(N=|R|=qs\). The unit graph \(G(R)\) has vertex set \(R\), with distinct \(x,y\) adjacent exactly when \(x+y\in U(R)\).

For each \(a\in F\), let
\[
C_a=\{x\in R:x+M=a\}.
\]
Every \(C_a\) has size \(s\). Since an element of a local ring is a unit exactly when its residue is nonzero,
\[
x\in C_a,\ y\in C_b
\quad\Longrightarrow\quad
x\sim y\iff a+b\ne0
\]
for distinct \(x,y\).

Write
\[
D(G,x)=\sum_k d_kx^k
\]
for the domination polynomial and
\[
D_t(G,x)=\sum_k t_kx^k
\]
for the total domination polynomial.

## Proof

### Ordinary domination

First suppose that \(\operatorname{char}(F)=2\). Then \(a=-a\) for every \(a\in F\). Hence each fiber \(C_a\) is independent, while every pair of distinct fibers is completely joined. Thus \(G(R)\) is the complete \(q\)-partite graph with all parts of size \(s\).

A nonempty set \(S\subseteq R\) dominates if and only if either it meets at least two fibers, or it is exactly one whole fiber. All subsets meeting at least two fibers contribute
\[
(1+x)^N-1-q\big((1+x)^s-1\big).
\]
Adding the \(q\) whole-fiber sets gives
\[
D(G(R),x)
=(1+x)^N-q(1+x)^s+(q-1)+q x^s.
\]

Now suppose that \(\operatorname{char}(F)\) is odd. The zero fiber \(C_0\) is independent. Each nonzero fiber \(C_a\) is a clique, there are no edges between \(C_a\) and \(C_{-a}\), and every other pair of distinct fibers is completely joined.

Any set meeting at least two distinct fibers dominates: no vertex can be nonadjacent to every selected fiber. A set supported in one nonzero fiber fails to dominate the opposite fiber. A set supported in \(C_0\) dominates exactly when it is the whole \(C_0\). Therefore
\[
D(G(R),x)
=(1+x)^N-q(1+x)^s+(q-1)+x^s.
\]

These two cases give the stated unified formula with
\[
\kappa=
\begin{cases}
q,&\operatorname{char}(F)=2,\\
1,&\operatorname{char}(F)\ne2.
\end{cases}
\]

### Total domination

In residue characteristic \(2\), a set is total dominating exactly when it meets at least two fibers. Hence
\[
D_t(G(R),x)
=(1+x)^N-q(1+x)^s+(q-1).
\]

Assume now that the residue characteristic is odd and put
\[
A=(1+x)^s-1.
\]
Start with all subsets meeting at least two fibers:
\[
B=(1+x)^N-q(1+x)^s+(q-1).
\]
The only such subsets that fail total domination are those supported on exactly one opposite pair
\[
C_a\cup C_{-a},
\qquad a\ne0,
\]
for which one of the two selected sides has cardinality one. For a fixed unordered opposite pair, all nonempty selections on both sides contribute \(A^2\), while the selections having at least two vertices on each side contribute
\[
(A-sx)^2.
\]
There are \((q-1)/2\) unordered opposite pairs. Therefore
\[
D_t(G(R),x)
=
B-\frac{q-1}{2}\big(A^2-(A-sx)^2\big).
\]

### Reconstruction from the ordinary domination polynomial

Let \(P(x)=D(G(R),x)\). Its degree is
\[
N=|R|.
\]

If \(s=1\), then \(R\) is a field. The coefficient of \(x\) is \(N\) in residue characteristic \(2\), because the unit graph is complete, and it is \(1\) in odd residue characteristic, because only \(0\) is a dominating singleton. Thus the field case is recovered immediately.

Assume \(s\ge2\). Compare the coefficients of \(P(x)\) with those of \((1+x)^N\), and let
\[
h=\max\{k<N:[x^k]P(x)\ne \binom Nk\}.
\]
In residue characteristic \(2\), the \(x^s\) correction cancels, so \(h=s-1\), and
\[
[x^h]P(x)-\binom Nh=-qs=-N.
\]
In odd residue characteristic, \(h=s\), and
\[
[x^h]P(x)-\binom Nh=-(q-1)\ne-N.
\]
Hence the polynomial itself decides the parity case. In the first case,
\[
s=h+1,\qquad q=N/s;
\]
in the second,
\[
s=h,\qquad q=N/s.
\]

Finally, the fiber description above shows that the unit graph of a finite local ring depends, up to graph isomorphism, only on \(q\), \(s\), and whether the residue characteristic is \(2\). Therefore \(D(G(R),x)\) determines the unit-graph isomorphism type within the class of finite commutative local rings.

## Verification

The symbolic proof is independent of computation. The accompanying `verify.py` constructs the residue-fiber graph directly, exhaustively enumerates all vertex subsets, and compares the resulting domination and total-domination polynomials with the formulas for seven representative parameter sets. It also independently constructs the actual modular unit graphs of \(\mathbb Z_4\), \(\mathbb Z_8\), and \(\mathbb Z_9\).

The exact output is:

```text
VERIFY_OK
model_cases=7
actual_modular_rings=Z4,Z8,Z9
largest_exhaustive_graph_order=16
reconstruction_from_domination_polynomial=verified
```

The largest exhaustive graph has \(16\) vertices, so all \(2^{16}\) subsets are checked. The script also reconstructs \((q,s)\) and the residue-characteristic parity from each computed ordinary domination polynomial.

## Relationship to prior work

Ashrafi, Maimani, Pournaki, and Yassemi introduced the arbitrary-ring unit graph and developed its basic structural properties. Kiani, Maimani, Pournaki, and Yassemi later classified finite rings whose unit graphs have domination number less than four; in particular, finite local nonfields have domination number \(2\).

The general total-domination polynomial was introduced independently in graph theory by Chaluvaraju and Chaitra. More recently, Du and Gan studied the domination number and total domination number of unit graphs of finite commutative rings and again obtained the local value \(2\), while a later dominant-metric study made the local residue-fiber geometry explicit.

The result here is finer: it enumerates dominating and total dominating sets in every cardinality, and shows that the ordinary domination polynomial reconstructs the residue-field size, maximal-ideal size, residue-characteristic parity, and therefore the entire unit-graph isomorphism type for finite local rings. Targeted searches for “domination polynomial,” “total domination polynomial,” “unit graph,” “local ring,” “residue field,” and equivalent generating-function language found no prior statement of these formulas or reconstruction property.

## Limitations

The theorem is restricted to finite commutative local rings. For nonlocal finite rings, several residue coordinates interact simultaneously and the one-fiber/opposite-pair classification used here no longer applies directly.

The polynomial determines the unit graph within the local class, not the ring isomorphism type: distinct local rings can have the same \(q\), \(s\), and residue-characteristic parity and hence isomorphic unit graphs.

No claim is made about domination roots beyond what follows formally from the displayed polynomials.

## References

1. N. Ashrafi, H. R. Maimani, M. R. Pournaki, and S. Yassemi, “Unit Graphs Associated with Rings,” *Communications in Algebra* 38 (2010), 2851–2871. DOI: 10.1080/00927870903095574. Published online 2010-08-18.
2. B. Chaluvaraju and V. Chaitra, “Total Domination Polynomial of A Graph,” *Journal of Informatics and Mathematical Sciences* 6 (2014), 87–92. DOI: 10.26713/jims.v6i2.256.
3. S. Kiani, H. R. Maimani, M. R. Pournaki, and S. Yassemi, “Classification of rings with unit graphs having domination number less than four,” *Rendiconti del Seminario Matematico della Università di Padova* 133 (2015), 173–195. DOI: 10.4171/RSMUP/133-9.
4. T. Du and A. Gan, “Domination Parameters of Unit Graphs of Rings,” *Axioms* 14 (2025), 399. DOI: 10.3390/axioms14060399.
5. “Dominant Metric Dimension of Unit Graphs of Finite Commutative Rings,” *Journal of Mathematics* (2026). DOI: 10.1155/jom/6300309.
