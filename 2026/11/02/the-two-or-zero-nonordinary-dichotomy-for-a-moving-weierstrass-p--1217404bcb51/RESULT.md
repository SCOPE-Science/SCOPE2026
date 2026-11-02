# The two-or-zero nonordinary dichotomy for a moving Weierstrass point in characteristic three

## Finding
Let \(k\) be an algebraically closed field of characteristic \(3\). For **every monic separable quintic**
\[
h(x)=x^5+a_4x^4+a_3x^3+a_2x^2+a_1x+a_0\in k[x],
\]
consider the genus-two hyperelliptic curves
\[
C_t:\quad y^2=(x-t)h(x),\qquad t\in k\setminus V(h),
\]
and the smooth member \(C_\infty:y^2=h(x)\) at the moving branch point \(t=\infty\).
Define
\[
\begin{split}
A&=a_2a_4-a_1,\\
B&=a_0-a_2a_3,\\
C&=a_1a_3-a_0a_4,\\
G(x)&=x^2+a_4x+a_3=D_x^{(3)}h(x),\\
\mathcal H(T,S)&=AT^2+BTS+CS^2.
\end{split}
\]
Here \(D_x^{(3)}\) is the third **Hasse derivative**, the coefficient of \(z^3\) in \(h(x+z)\). The polynomial \(\mathcal H\) is nonzero. Its zeros on \(\mathbb P^1_{[T:S]}\) are precisely the parameters with nonordinary smooth genus-two fibers, together with any formal Hasse zeros supported at the excluded branch-collision parameters \(t\in V(h)\). Its discriminant has the **exact resultant identity**
\[
\boxed{\operatorname{Disc}(\mathcal H)=B^2-4AC=\operatorname{Res}_x(h,G).}
\]
There are exactly two mutually exclusive possibilities, including the parameter at infinity:

1. If \(\operatorname{Res}(h,G)\ne0\), then \(\mathcal H\) has **two distinct roots**, both corresponding to **smooth nonordinary** genus-two curves. Each zero is reduced and each curve has \(a\)-number exactly \(1\). The Jacobian \(3\)-rank may be \(0\) or \(1\).
2. If \(\operatorname{Res}(h,G)=0\), then \(h\) and \(G\) have **exactly one common root** \(\alpha\), and \(\mathcal H(T,1)=A(T-\alpha)^2\) with \(A\ne0\). Thus its entire double zero lies at the **singular branch-collision fiber** \(t=\alpha\), and **every smooth member, including \(C_\infty\), is ordinary**.

Equivalently, the nonordinary parameter scheme **restricted to the smooth family is always reduced**, and the number of its geometric points is either **two or zero**. This is a statement about the marked moving-branch family and its parameter; no assertion is made that two distinct parameters always give nonisomorphic curves in coarse moduli.

## Assumptions and scope
The ground field is algebraically closed of characteristic \(3\); no genericity, automorphism-group, or special-position hypothesis on the five fixed branch points is imposed beyond separability of \(h\). For finite \(t\), the hyperelliptic double cover is smooth precisely when \(h(t)\ne0\). The fiber at infinity is understood in the chart \(s=1/t\) through the equation \(y^2=(1-sx)h(x)\), which differs from the finite equation by an invertible scalar twist away from \(s=0\) and has smooth fiber \(y^2=h(x)\) at \(s=0\). The zeros considered are zeros of the Cartier/Hasse--Witt determinant in these charts; they do not assert any particular scheme structure of a compactified moduli stack at the singular boundary.

## Proof
**Step 1: coefficient matrix.** For a hyperelliptic curve \(y^2=f(x)\) in characteristic \(3\) and genus \(2\), the Hasse--Witt matrix in the standard basis is formed from coefficients \(c_j=[x^j]f(x)\) as
\[
H(f)=\begin{pmatrix}c_2&c_1\\c_5&c_4\end{pmatrix}.
\]
This is the standard \(p=3\) specialization of the hyperelliptic Cartier--Manin coefficient formula; transposing the matrix under an alternate convention does not change the determinant, the \(a\)-number, or the ranks used below. For \(f_t=(x-t)h(x)\),
\[
H_t=\begin{pmatrix}
a_1-ta_2&a_0-ta_1\\
a_4-t&a_3-ta_4
\end{pmatrix},\qquad
\det(H_t)=At^2+Bt+C.
\]
Near infinity the smooth chart uses \(f_s=(1-sx)h(x)\). The same formula gives
\[
\det H(f_s)=A+Bs+Cs^2=s^2\det H_{1/s}.
\]
Hence these two expressions define the degree-two homogeneous determinant \(\mathcal H\) over the whole parameter line.

**Step 2: an exact Bezout identity.** In characteristic \(3\) one has
\[
\boxed{h'(x)G(x)-(2x+a_4)h(x)=Ax^2+Bx+C.}
\]
Indeed, direct expansion and cancellation of the degree-six through degree-three coefficients leaves the displayed quadratic. There is also the polynomial decomposition
\[
h(x)=x^3G(x)+a_2x^2+a_1x+a_0
      \equiv -Ax+B\pmod{G(x)}.
\]
Since \(G\) is monic quadratic,
\[
\begin{split}
\operatorname{Res}_x(h,G)&=\operatorname{Res}_x(-Ax+B,G)\\
&=A^2a_3+ABa_4+B^2.
\end{split}
\]
The relation \(C=-Aa_3-Ba_4\), verified directly from the definitions, makes this equal to \(B^2-AC=B^2-4AC\) because \(4=1\) in characteristic \(3\). This proves the exact resultant/discriminant identity, including the cases \(A=0\) or \(B=0\).

**Step 3: nonvanishing and boundary collisions.** If \(A=B=0\), then \(a_1=a_2a_4\) and \(a_0=a_2a_3\), giving
\[
h(x)=(x^3+a_2)(x^2+a_4x+a_3).
\]
Over an algebraically closed characteristic-three field the first factor is a cube, contradicting the separability of \(h\). Thus \((A,B)\ne(0,0)\), and \(\mathcal H\ne0\). In particular, if infinity is a root (\(A=0\)), its local vanishing order is one because \(B\ne0\).

If \(\alpha\) is a root of the separable \(h\), then \(h'(\alpha)\ne0\). The boxed Bezout identity gives
\[
\mathcal H(\alpha,1)=h'(\alpha)G(\alpha).
\]
Hence a fixed-branch collision is a Hasse zero precisely when \(G(\alpha)=0\). Such a shared root forces \(\operatorname{Res}(h,G)=0\) and thus the discriminant of \(\mathcal H\) to vanish. Since \((A,B)\ne(0,0)\) and \(A=0\) would force a nonzero discriminant \(B^2\), necessarily \(A\ne0\). The unique repeated root of \(AT^2+BT+C\) is \(\alpha=B/A\) (because \(-B/(2A)=B/A\) in characteristic \(3\)). It has multiplicity exactly two. Two distinct common roots of \(h\) and \(G\) would make \(-Ax+B\) vanish at two roots of \(G\), forcing \(A=B=0\), already excluded (the assertion also follows from the repeated quadratic root). Thus the common root is unique.

If \(\operatorname{Res}(h,G)\ne0\), the discriminant is nonzero and the homogeneous quadratic has two distinct zeros on \(\mathbb P^1(k)\). None lies among the roots of \(h\), for otherwise the Bezout identity would force a shared root with \(G\). Both therefore parametrize smooth curves. If the resultant vanishes, the entire quadratic divisor is twice the singular parameter \(\alpha\), and no smooth fiber is nonordinary. This proves the dichotomy and the reducedness statement.

**Step 4: exact \(a\)-number.** At a finite smooth parameter \(t\), translate \(x=t+z\) and write \(h(t+z)=b_0+b_1z+\cdots+z^5\). Then \(b_0=h(t)\ne0\), and in the translated standard differential basis the matrix is
\[
\begin{pmatrix}b_1&b_0\\b_4&b_3\end{pmatrix}.
\]
It is nonzero. At infinity the matrix \(\bigl(\begin{smallmatrix}a_2&a_1\\1&a_4\end{smallmatrix}\bigr)\) is also nonzero. Thus any smooth nonordinary matrix, which has determinant zero, has rank exactly one. As \(a(C)=2-\operatorname{rank}(H)\), the \(a\)-number is exactly one. It does not follow that the \(3\)-rank is one: that rank is the stable rank of semilinear Frobenius.

**Step 5: the two \(3\)-rank types really occur.** Take \(h(x)=x^5+x^4+x^3+x\in\mathbb F_3[x]\), which is separable. Then \(\mathcal H(T,1)=1-T^2\), and \(h(1)=h(-1)=1\). At \(t=1\) and \(t=-1=2\) the matrices are respectively
\[
H_1=\begin{pmatrix}1&2\\0&0\end{pmatrix},\qquad
H_{-1}=\begin{pmatrix}1&1\\2&2\end{pmatrix}.
\]
Both have rank one, but \(H_1^2=H_1\) while \(H_{-1}^2=0\). All coefficients lie in \(\mathbb F_3\), so these are the actual second Frobenius iterates. The smooth curves consequently have \(3\)-ranks one and zero, respectively. Direct point counts give \(\#C_1(\mathbb F_3)=6\) and \(\#C_{-1}(\mathbb F_3)=4\), consistent with the matrix classification (both smooth degree-six models have two rational points at infinity). For the other possibility, \(h(x)=x^5+x\) is separable and yields \(\mathcal H(T,1)=-T^2\); its only Hasse zero occurs at the excluded singular fiber \(t=0\). This completes the proof.

## Verification
Run the self-contained Python 3 checker \(\texttt{verify_linearized_g2.py}\). It recomputes the Hasse matrices from coefficients, verifies both polynomial Bezout and resultant/discriminant identities, computes the independent Sylvester determinant, and exhaustively tests all \(3^5=243\) monic quintics over \(\mathbb F_3\), including all 162 separable ones. The exact output is:

```text
LINEARIZED_GENUS2_CHAR3_RESULTANT_REDUCED_NONORDINARY_DIVISOR_PASS
Exhausted 162 separable monic quintics over F3; parameter strata={'two': 120, 'double': 42, 'infty': 42}
Explicit genus-two p-rank pair: (t=1,r=1,#F3=6), (t=-1,r=0,#F3=4).
```

These finite checks are independent reproducibility checks, **not** a proof for arbitrary algebraically closed characteristic-three fields. The unrestricted result is established by the displayed universal polynomial identities and the Hasse--Witt formula.

## Relationship to prior work
Cavalieri and Pries, *Mass formula for non-ordinary curves in one dimensional families*, arXiv:2308.14891 (first public version, August 28, 2023), introduce the linearized moving-branch hyperelliptic families and prove a mass formula. In Section 5, Remark 5.5, they state the general \(g(p-1)/2\) bound on nonordinary parameter values from the Cartier operator and explain that generic-curve information does not itself control vanishing multiplicities in the family. The result here is a characteristic-three, genus-two refinement: it computes the entire parameter divisor and gives a precise boundary-collision criterion, with no genericity condition on \(h\).

Yui, *On the Jacobian varieties of hyperelliptic curves over fields of characteristic \(p>2\)*, Journal of Algebra 52 (1978), 378–410, is a classical source for the coefficient method. The standard Cartier--Manin calculation itself is **not** claimed as new. The claimed additional content is the exact Bezout/resultant identity, the two-or-zero smooth-fiber dichotomy, universal simple zeros on the smooth family, and the explicit coexistence of both possible nonordinary \(3\)-ranks.

## Limitations
No assertion is made about arithmetic splitting over a non-algebraically-closed field; the two zero parameters may be defined only over an extension. Their isomorphism types and automorphism groups can vary. The divisor is computed on the **parameter line**; its orders must not automatically be identified with stack or coarse-moduli intersection multiplicities when the moduli map is ramified or has automorphisms. Singular branch-collision members are not assigned \(a\)-numbers or \(3\)-ranks. The result does not classify the full Newton polygon of all fibers, nor all higher-characteristic or higher-genus analogues. An equivalent identity could exist in classical or unindexed literature and must be checked independently before claims of publication priority.

## References
1. R. Cavalieri and R. Pries, *Mass formula for non-ordinary curves in one dimensional families*, arXiv:2308.14891, submitted August 28, 2023; full text: https://arxiv.org/html/2308.14891v3, especially Section 5 and Remark 5.5.
2. N. Yui, *On the Jacobian varieties of hyperelliptic curves over fields of characteristic \(p>2\)*, Journal of Algebra 52 (1978), 378–410, doi:10.1016/0021-8693(78)90247-8; standard Cartier--Manin coefficient formula.
