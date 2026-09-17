# Exact subalgebra commutativity degree of the five-dimensional Heisenberg algebra

## Result

Let \(q\) be a prime power and let
\[
H_2=\mathfrak h(2,\mathbb F_q)
 =\langle x_1,y_1,x_2,y_2,z\mid [x_1,y_1]=[x_2,y_2]=z\rangle,
\]
with all other basic brackets zero. For the subalgebra commutativity degree
\[
\operatorname{sd}(L)=
\frac{|\{(A,B)\in\mathcal L(L)^2:[A,B]\subseteq A+B\}|}
{|\mathcal L(L)|^2},
\]
one has
\[
|\mathcal L(H_2)|
=q^5+3q^4+5q^3+6q^2+4q+6
\]
and
\[
\boxed{
\operatorname{sd}(H_2)=
\frac{
3q^9+12q^8+34q^7+62q^6+91q^5+111q^4+108q^3+88q^2+48q+36
}{
(q^5+3q^4+5q^3+6q^2+4q+6)^2
}.}
\]
Equivalently, the number of nonpermutable ordered pairs of subalgebras is
\[
q^{10}+3q^9+7q^8+8q^7+7q^6+5q^5+q^4.
\]
In particular,
\[
\operatorname{sd}(H_2)\sim \frac{3}{q}
\qquad(q\to\infty).
\]

This gives the next Heisenberg rank after the rank-one computation in Muhie--Otera--Russo, arXiv:2609.19086v1. Their introduction asks for the values of \(\operatorname{sd}(\mathfrak h(m))\), while Theorem 1.2 gives the explicit rank-one case. No rank-two formula appears in that version.

## Symplectic description of all subalgebras

Write
\[
H_2=V\oplus Z,
\qquad V=\langle x_1,y_1,x_2,y_2\rangle,
\qquad Z=\mathbb F_qz,
\]
and encode the bracket by the nondegenerate alternating form
\[
[v,w]=\omega(v,w)z,
\]
where, in coordinates \((a,b,c,d)\),
\[
\omega((a,b,c,d),(a',b',c',d'))
=ab'-ba'+cd'-dc'.
\]
The following elementary description is useful more generally for \(\mathfrak h(m)\).

1. If a subalgebra \(A\) contains \(Z\), then
   \[
   A=U\oplus Z
   \]
   for a unique arbitrary subspace \(U\le V\).

2. If \(A\cap Z=0\), projection to \(V\) identifies \(A\) with a totally isotropic subspace \(U\le V\). Relative to the fixed splitting \(H_2=V\oplus Z\), there is a unique functional \(f\in U^*\) such that
   \[
   A=\Gamma_f(U):=\{u+f(u)z:u\in U\}.
   \]
   Conversely every such graph over an isotropic \(U\) is a subalgebra.

For two graph subalgebras \(A=\Gamma_f(U)\) and \(B=\Gamma_g(W)\), put \(T=U\cap W\). Then
\[
z\in A+B
\quad\Longleftrightarrow\quad
f|_T\ne g|_T.
\]
Since every bracket lies in \(Z\), it follows that
\[
A,B\text{ are nonpermutable}
\quad\Longleftrightarrow\quad
f|_T=g|_T\ \text{ and }\ \omega(U,W)\ne0.
\tag{1}
\]
For fixed \(U,W\), with \(r=\dim U\), \(s=\dim W\), and \(t=\dim(U\cap W)\), the number of functional pairs satisfying the first condition in (1) is
\[
q^{r+s-t}.
\tag{2}
\]

For context, in a \(2m\)-dimensional symplectic space the number of totally isotropic \(r\)-subspaces is
\[
I_{m,r}(q)
=\prod_{i=0}^{r-1}\frac{q^{2m-2i}-1}{q^{r-i}-1}
={m\brack r}_q\prod_{j=m-r+1}^{m}(q^j+1).
\]
Consequently the same classification gives the general subalgebra count
\[
|\mathcal L(\mathfrak h(m,\mathbb F_q))|
=\sum_{r=0}^{2m}{2m\brack r}_q
 +\sum_{r=0}^{m}q^r I_{m,r}(q).
\tag{3}
\]
Equation (1) reduces the commutativity-degree problem for every rank to a finite symplectic incidence count.

## Proof of the rank-two formula

Let
\[
n=(q+1)(q^2+1)=q^3+q^2+q+1.
\]
There are \(n\) lines in \(V\), and every line is isotropic. There are also \(n\) Lagrangian planes in the four-dimensional symplectic space \(V\).

### Number of subalgebras

Subalgebras containing \(Z\) are in bijection with all subspaces of \(V\). Hence their number is
\[
C=2+2{4\brack1}_q+{4\brack2}_q
=q^4+3q^3+4q^2+3q+5.
\]
The noncentral graph subalgebras arise from isotropic subspaces of dimensions \(0,1,2\). Each \(r\)-space supports \(q^r\) linear functionals, so their number is
\[
S=1+nq+nq^2
=q^5+2q^4+2q^3+2q^2+q+1.
\]
Thus
\[
N:=|\mathcal L(H_2)|=C+S
=q^5+3q^4+5q^3+6q^2+4q+6.
\tag{4}
\]
Any ordered pair in which at least one subalgebra contains \(Z\) is permutable, because \([A,B]\subseteq Z\subseteq A+B\). It remains to count nonpermutable pairs of graph subalgebras using (1)--(2).

### Line--line pairs

Fix a line \(U\). Its symplectic orthogonal \(U^\perp\) is three-dimensional and contains \(q^2+q+1\) lines. Therefore exactly
\[
n-(q^2+q+1)=q^3
\]
lines \(W\) are nonorthogonal to \(U\). Such lines are distinct from \(U\), so \(t=0\), and (2) contributes \(q^2\) choices of \((f,g)\). Hence
\[
E_{11}=nq^5.
\tag{5}
\]

### Line--Lagrangian pairs

A fixed line \(U\) lies in exactly \(q+1\) Lagrangian planes. Since a Lagrangian plane \(W\) satisfies \(W^\perp=W\), the pair \((U,W)\) is nonorthogonal exactly when \(U\not\subset W\). Thus there are
\[
n-(q+1)=q^2(q+1)
\]
such \(W\). Here \(t=0\), so the functional weight is \(q^3\). In one orientation,
\[
E_{12}=nq^5(q+1),
\tag{6}
\]
and the reverse orientation contributes the same amount.

### Lagrangian--Lagrangian pairs

Fix a Lagrangian plane \(U\). A distinct Lagrangian \(W\) meeting \(U\) in a line is automatically nonorthogonal to \(U\). For each of the \(q+1\) lines in \(U\), there are \(q\) other Lagrangians containing it, so there are \(q(q+1)\) such \(W\). Here \(t=1\), and the functional weight is \(q^3\), giving
\[
nq(q+1)q^3=nq^4(q+1).
\tag{7}
\]
The remaining Lagrangians transverse to \(U\) number
\[
n-1-q(q+1)=q^3.
\]
They are also nonorthogonal to \(U\), now with \(t=0\) and functional weight \(q^4\), giving
\[
nq^3q^4=nq^7.
\tag{8}
\]

Combining (5)--(8), the number of nonpermutable ordered pairs is
\[
\begin{aligned}
E
&=nq^5+2nq^5(q+1)+nq^4(q+1)+nq^7\\
&=nq^4(q^3+2q^2+4q+1)\\
&=q^{10}+3q^9+7q^8+8q^7+7q^6+5q^5+q^4.
\end{aligned}
\tag{9}
\]
Therefore \(\operatorname{sd}(H_2)=1-E/N^2\). Expanding \(N^2-E\) gives the displayed numerator.

The argument uses only finite-field linear algebra and nondegeneracy of an alternating form, so it includes characteristic two and arbitrary prime-power \(q\).

## Computational checks

The standalone script `artifacts/verify_h2.py` exhaustively enumerates vector subspaces of \(\mathbb F_q^5\) in reduced row-echelon form for the prime fields \(q=2,3\), filters the Lie subalgebras, and tests permutability directly. It was executed with the following outputs:

```text
q=2: subalgebras=158, permutable_ordered_pairs=18964
q=3: subalgebras=693, permutable_ordered_pairs=292329
```

These agree exactly with (4) and with \(N^2-E\). The computation is a finite check for two fields; the general theorem rests on the proof above.

## Relation to the rank-one case

Applying the same graph criterion to a two-dimensional symplectic quotient gives
\[
|\mathcal L(\mathfrak h(1,\mathbb F_q))|=q^2+2q+4
\]
and \(q^3(q+1)\) nonpermutable ordered pairs, hence
\[
\operatorname{sd}(\mathfrak h(1,\mathbb F_q))
=\frac{3q^3+12q^2+16q+16}{(q^2+2q+4)^2}.
\]
For prime \(q=p\), this recovers Muhie--Otera--Russo, Theorem 1.2, while also showing that the same expression holds over every finite field \(\mathbb F_q\).

## Originality scope and limitations

The classification of Heisenberg subalgebras through symplectic geometry is standard in spirit, and Gaussian-binomial counts of isotropic subspaces are classical. The originality claim is limited to the exact subalgebra commutativity degree above, the explicit nonpermutability criterion (1) as applied to this invariant, and the resulting rank-two enumeration, to the best of our knowledge.

The motivating preprint is extremely recent. Searches for the exact invariant together with rank-two/five-dimensional Heisenberg terminology, synonymous permutability language, and adjacent subgroup-commutativity literature found no prior formula for this case. This does not prove exhaustive absence. A specialized group-theoretic computation for the corresponding class-two group could in principle imply the odd-prime case through Lazard correspondence, although no such matching formula was located.

## References

1. S. K. Muhie, D. E. Otera, F. G. Russo, *On the number of modular pairs in finite dimensional Lie algebras on finite fields*, arXiv:2609.19086v1 (2026). https://arxiv.org/abs/2609.19086
2. M. Tărnăuceanu, *The subgroup commutativity degree of finite P-groups*, Bull. Aust. Math. Soc. 93 (2016), 37--41. https://doi.org/10.1017/S0004972715000702
