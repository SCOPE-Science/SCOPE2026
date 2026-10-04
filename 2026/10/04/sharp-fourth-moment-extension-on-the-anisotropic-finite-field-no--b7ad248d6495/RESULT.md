# Sharp fourth-moment extension on the anisotropic finite-field norm-one conic
## Finding
Let \(F=\mathbb F_q\) have odd order \(q\), let \(K=\mathbb F_{q^2}\), and let \(T=\{z\in K:N_{K/F}(z)=1\}\), viewed as a subset of the two-dimensional additive \(F\)-space \(K\). Give \(T\) normalized counting measure, give \(K\) counting measure, fix a nontrivial additive character \(\psi:F\to\mathbb C^\times\), and define
\[
Eg(x)=\frac1{q+1}\sum_{z\in T}g(z)\psi(\operatorname{Tr}_{K/F}(xz)).
\]
Then the exact sharp extension norm is
\[
R_T^*(2\to4)^4=\frac{3q^3}{(q+1)^3}.
\]
Every nonzero extremizer, and only every nonzero extremizer, has constant modulus on \(T\) and has all antipodal products \(g(z)g(-z)\) with one common argument. Equivalently, for some \(r>0\) and \(\phi\in\mathbb R\), \(|g(z)|=r\) and \(g(-z)=e^{i\phi}\overline{g(z)}\) for every \(z\in T\).

## Assumptions and scope
The field \(F=\mathbb F_q\) has odd order. The quadratic extension is \(K=\mathbb F_{q^2}\), with conjugation \(z\mapsto \bar z=z^q\), trace \(\operatorname{Tr}(z)=z+\bar z\), and norm \(N(z)=z\bar z\). The norm-one set \(T=\{z:N(z)=1\}\) has \(q+1\) elements and no zero. The Fourier pairing is the nondegenerate trace pairing \((x,z)\mapsto \psi(\operatorname{Tr}(xz))\). The ambient \(L^4\) norm uses counting measure on \(K\), while the input \(L^2\) norm uses normalized counting measure on \(T\).

## Proof
Put \(n=q+1\), \(S=\sum_{z\in T}|g(z)|^2\), and
\[
\mathcal Q(g)=\sum_{a+b=c+d}g(a)g(b)\overline{g(c)g(d)},
\]
where all four variables lie in \(T\). Orthogonality gives
\[
\|Eg\|_4^4=\frac{q^2}{n^4}\mathcal Q(g).
\]

The key collision fact is exact. Let \(Q(z)=N(z)\) and let \(B(u,v)=Q(u+v)-Q(u)-Q(v)\). If \(a,b\in T\) and \(a+b=s\), then \(Q(a)=Q(s-a)=1\), hence \(B(s,a)=Q(s)\). For fixed \(s\ne0\), this is an affine \(F\)-line, whose intersection with the nonsingular conic \(Q(a)=1\) has at most two points. Since \(a\) and \(b=s-a\) are both such points, every nonzero pair-sum fiber consists only of one diagonal pair or one swapped pair. For \(s=0\), all \(n\) ordered antipodal pairs \((z,-z)\) occur.

Therefore, with
\[
P_4=\sum_{z\in T}|g(z)|^4,\qquad
R=\sum_{z\in T}|g(z)|^2|g(-z)|^2,\qquad
B_0=\sum_{z\in T}g(z)g(-z),
\]
one has the exact identity
\[
\mathcal Q(g)=2S^2-P_4-2R+|B_0|^2.
\]
Partition \(T\) into \(m=n/2\) antipodal pairs. For the \(j\)-th pair set \(x_j=|g(z_j)|^2\), \(y_j=|g(-z_j)|^2\), \(s_j=x_j+y_j\), and \(p_j=\sqrt{x_jy_j}\). Phase alignment gives \(|B_0|\le2\sum_jp_j\). Thus
\[
\mathcal Q(g)\le2S^2-\sum_js_j^2-2\sum_jp_j^2+4\left(\sum_jp_j\right)^2.
\]
For fixed \((s_j)\), the right-hand side is strictly increasing in each \(p_j\) on \(0\le p_j\le s_j/2\), so it is maximized at \(p_j=s_j/2\), equivalently \(x_j=y_j\). This yields
\[
\mathcal Q(g)\le3S^2-\frac32\sum_js_j^2\le3S^2-\frac32\frac{S^2}m
=\frac{3(n-1)}nS^2.
\]
The last equality condition is \(s_1=\cdots=s_m\). Hence equality throughout holds exactly when all \(|g(z)|\) are equal and the products \(g(z)g(-z)\) have one common argument. Since \(\|g\|_{L^2(T)}^2=S/n\), substitution gives
\[
R_T^*(2\to4)^4=\frac{q^2}{n^2}\frac{3(n-1)}n=\frac{3q^3}{(q+1)^3}.
\]

## Verification
The accompanying `verify.py` exhaustively constructs anisotropic norm-one conics over every odd prime field through \(101\). It checks \(|T|=q+1\), the exact pair-sum fiber structure, and the constant-function collision energy \(3(q+1)q\). These finite checks corroborate, but do not replace, the all-prime-power proof above.

## Relationship to prior work
Iosevich and Koh prove uniform \(L^2\to L^4\) extension bounds for nondegenerate quadratic surfaces over finite fields and, in dimension two, reduce the problem to controlling two-point sums. Their argument records an upper bound of two representations for each nonzero sum but is deliberately nonsharp: it treats the origin separately by inequalities and concludes only a field-size-independent bound. The present result resolves the exceptional zero-sum fiber exactly and determines both the best constant and every equality case for the anisotropic norm-one conic.

The later sharp finite-field extension program of González-Riquelme and Oliveira e Silva computes best constants and maximizers for several paraboloid, hyperbolic-paraboloid, and cone models. Its stated sharp surfaces do not include the two-dimensional anisotropic norm-one conic. The 2018 sphere paper of Iosevich, Koh, Lee, Pham, and Shen establishes sharp exponent ranges and additive-energy bounds for nonzero-radius spheres, rather than an exact best constant and equality classification for this planar anisotropic conic.

## Limitations
The theorem is restricted to odd characteristic and to the quadratic norm-one conic in a two-dimensional additive space. It does not claim a sharp constant for higher-dimensional quadratic surfaces, for the zero-radius cone, or for other extension exponents. The computational verifier covers prime fields only; prime-power generality is supplied by the algebraic proof.

## References
1. A. Iosevich and D. Koh, *Extension theorems for the Fourier transform associated with non-degenerate quadratic surfaces in vector spaces over finite fields*, arXiv:0804.4505v1, first public 2008-04-28.
2. A. Iosevich, D. Koh, S. Lee, T. Pham, and C.-Y. Shen, *On restriction estimates for the zero radius sphere over finite fields*, arXiv:1806.11387v3.
3. C. González-Riquelme and D. Oliveira e Silva, *Sharp extension inequalities on finite fields*, arXiv:2405.16647v2.
