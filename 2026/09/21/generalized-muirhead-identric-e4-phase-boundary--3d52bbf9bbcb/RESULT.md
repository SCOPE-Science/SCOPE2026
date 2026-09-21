# A sharp phase boundary in the unresolved Muirhead–identric \(E_4\) region

## Context

For \(x,y>0\) and real \(a,b\) with \(a+b\ne0\), define the two-parameter generalized Muirhead mean
\[
M(a,b;x,y)=
\left(\frac{x^a y^b+x^b y^a}{2}\right)^{1/(a+b)}
\]
and the identric mean
\[
I(x,y)=
\begin{cases}
e^{-1}\left(y^y/x^x\right)^{1/(y-x)},&x\ne y,\\
x,&x=y.
\end{cases}
\]

Wang, Chu and Qiu (2010) classified three parameter regions \(E_1,E_2,E_3\) for the comparison of \(M\) with \(I\), and in Remark 3.1 explicitly left the complementary region
\[
E_4=\left\{(a,b):
ab<0,\quad
3(a-b)^2-2(a+b)>0,\quad
2(a-b)^2-3(a+b)+1<0
\right\}
\]
as an open problem.

This record gives an exact one-dimensional phase boundary for all of \(E_4\). The boundary is variational rather than elementary, but it yields necessary and sufficient conditions for the global comparison and shows that the unresolved region contains both globally positive and genuinely sign-changing subregions.

## Theorem

Put
\[
s=a+b,\qquad d=|a-b|,
\]
and define
\[
d_0=\sqrt{\frac25},\qquad
L(d)=\frac{2d^2+1}{3},\qquad
U(d)=\min\left\{d,\frac{3d^2}{2}\right\}.
\]
Then
\[
(a,b)\in E_4
\quad\Longleftrightarrow\quad
d_0<d<1,\qquad L(d)<s<U(d).
\]

For \(d>0\) and \(z>0\), set
\[
R_d(z)=
\frac{\log\cosh(dz)}{z\coth z-1},
\qquad
C(d)=\inf_{z>0}R_d(z).
\]

The following statements hold.

1. \(C(d)\) extends continuously to \(d=d_0\), is strictly increasing on
   \([d_0,1)\), and
   \[
   C(d_0)=\frac35.
   \]

2. For every
   \[
   d_0<d<\log2,
   \]
   the sharp threshold lies strictly inside the unresolved cross-section:
   \[
   \boxed{L(d)<C(d)<U(d)}.
   \]
   The infimum is attained at at least one finite \(z_d>0\).

3. For
   \[
   \log2\le d<1,
   \]
   one has the exact identity
   \[
   \boxed{C(d)=d}.
   \]
   In this range \(U(d)=d\).

4. Consequently, if \((a,b)\in E_4\), then:

   - if \(d\ge\log2\), then
     \[
     \boxed{M(a,b;x,y)>I(x,y)}
     \]
     for every \(x\ne y>0\);

   - if \(d_0<d<\log2\) and \(L(d)<s<C(d)\), the same strict global inequality holds;

   - if \(d_0<d<\log2\) and \(s=C(d)\), then
     \[
     M(a,b;x,y)\ge I(x,y)
     \]
     for all \(x,y>0\), with equality for at least one unequal pair;

   - if \(d_0<d<\log2\) and \(C(d)<s<U(d)\), then both signs occur: there are unequal positive pairs with \(M>I\) and others with \(M<I\). In fact the logarithmic deficit is positive both near \(x=y\) and for sufficiently large ratios, so any negative value forces at least two nontrivial equality ratios.

Thus the 2010 \(E_4\) problem has a sharp continuous phase curve \(s=C(d)\): above it (where allowed) the comparison is mixed, below it the generalized Muirhead mean dominates the identric mean globally, and for \(d\ge\log2\) the entire \(E_4\) cross-section is globally positive.

## Proof

### 1. Hyperbolic normal form

By homogeneity and symmetry, for an unequal pair write
\[
x=g e^{-z},\qquad y=g e^z,\qquad g=\sqrt{xy},\qquad z>0.
\]
Then
\[
M(a,b;x,y)
=
g\,\cosh(dz)^{1/s},
\]
whereas direct substitution in the identric mean gives
\[
I(x,y)=g\,e^{z\coth z-1}.
\]
Hence
\[
\log\frac{M}{I}
=
\frac{\log\cosh(dz)}{s}-(z\coth z-1).
\]
Since \(z\coth z-1>0\) for \(z>0\),
\[
\operatorname{sgn}\log\frac{M}{I}
=
\operatorname{sgn}\bigl(R_d(z)-s\bigr).
\tag{1}
\]

The \(E_4\) inequalities imply
\[
s>\frac{2d^2+1}{3}>0.
\]
Also
\[
ab=\frac{s^2-d^2}{4}<0
\]
gives \(s<d\), while \(3d^2-2s>0\) gives \(s<3d^2/2\). Thus \(E_4\) is exactly
\[
L(d)<s<U(d).
\]
The interval is nonempty exactly when
\[
d_0<d<1.
\]

### 2. Endpoint behavior of \(R_d\)

At the diagonal,
\[
\log\cosh(dz)
=\frac{d^2z^2}{2}-\frac{d^4z^4}{12}+O(z^6),
\]
and
\[
z\coth z-1
=\frac{z^2}{3}-\frac{z^4}{45}+O(z^6).
\]
Therefore
\[
R_d(z)
=
\frac{3d^2}{2}
+
\frac{d^2(2-5d^2)}{20}z^2
+O(z^4).
\tag{2}
\]
In particular,
\[
R_d(0):=\lim_{z\downarrow0}R_d(z)=\frac{3d^2}{2}.
\]

At the opposite endpoint,
\[
\log\cosh(dz)
=
dz-\log2+\log(1+e^{-2dz}),
\]
and
\[
z\coth z-1
=
z-1+\frac{2z}{e^{2z}-1}.
\]
Hence
\[
R_d(\infty):=\lim_{z\to\infty}R_d(z)=d,
\tag{3}
\]
and, more precisely,
\[
R_d(z)-d
=
\frac{
d-\log2+\log(1+e^{-2dz})
-\dfrac{2dz}{e^{2z}-1}
}{
z\coth z-1
}.
\tag{4}
\]
Thus if \(d<\log2\), then \(R_d(z)<d\) for all sufficiently large \(z\).

### 3. The lower algebraic boundary is strictly below \(C(d)\)

Fix \(d_0<d<1\) and take \(s=L(d)\). Then
\[
2d^2-3s+1=0
\]
and
\[
3d^2-2s=\frac{5d^2-2}{3}>0.
\]
Also \(L(d)<d\) for \(1/2<d<1\), so the corresponding parameters have \(ab<0\). Therefore this boundary point lies in the \(E_1\) region of Wang–Chu–Qiu, whose Theorem 1.1 gives
\[
M>I
\]
for every unequal pair. By (1),
\[
R_d(z)>L(d)\qquad(z>0).
\tag{5}
\]

The two endpoint limits are also strictly above \(L(d)\):
\[
\frac{3d^2}{2}-L(d)=\frac{5d^2-2}{6}>0,
\]
and
\[
d-L(d)=\frac{(2d-1)(1-d)}{3}>0.
\]
Combining these endpoint gaps with (5) and continuity yields
\[
C(d)>L(d).
\tag{6}
\]

At \(d=d_0\), the same \(E_1\) boundary argument gives \(R_{d_0}(z)>3/5\) for every finite \(z>0\), while (2) gives \(R_{d_0}(0)=3/5\). Hence
\[
C(d_0)=\frac35.
\tag{7}
\]

### 4. The upper algebraic boundary is strictly above \(C(d)\) below \(\log2\)

If \(d_0<d\le2/3\), then \(U(d)=3d^2/2\). Since \(d>d_0\), the quadratic coefficient in (2) is negative, so
\[
R_d(z)<\frac{3d^2}{2}=U(d)
\]
for all sufficiently small positive \(z\). Therefore \(C(d)<U(d)\).

If \(2/3\le d<\log2\), then \(U(d)=d\). Equation (4) gives
\[
R_d(z)<d=U(d)
\]
for all sufficiently large \(z\). Again \(C(d)<U(d)\).

Together with (6),
\[
L(d)<C(d)<U(d),
\qquad d_0<d<\log2.
\tag{8}
\]
Since both endpoint limits exceed \(C(d)\), the infimum is attained at a finite positive \(z_d\).

### 5. Exact collapse at \(d=\log2\)

For the power mean \(P_r=M(r,0;\cdot,\cdot)\), Pittenger's sharp bound quoted in Wang–Chu–Qiu is
\[
I(x,y)<P_{\log2}(x,y)
\qquad(x\ne y).
\]
Power means increase with their order, so for every \(d\ge\log2\),
\[
P_d>I.
\]
In the hyperbolic normalization,
\[
\log\frac{P_d}{I}
=
\frac{\log\cosh(dz)}{d}-(z\coth z-1),
\]
and therefore
\[
R_d(z)>d
\qquad(z>0,\ d\ge\log2).
\]
Together with the limit \(R_d(\infty)=d\), this proves
\[
C(d)=d
\qquad(d\ge\log2).
\tag{9}
\]

### 6. Continuity and strict monotonicity of the phase curve

Compactify \(z\in(0,\infty)\) by \(u=z/(1+z)\in(0,1)\) and use the endpoint values in (2)–(3). On every compact positive \(d\)-interval, the extended function
\[
(d,u)\longmapsto R_d\!\left(\frac{u}{1-u}\right)
\]
is jointly continuous on the closed rectangle, with values \(3d^2/2\) at \(u=0\) and \(d\) at \(u=1\). Therefore its minimum \(C(d)\) depends continuously on \(d\).

For finite \(z>0\),
\[
\frac{\partial R_d(z)}{\partial d}
=
\frac{z\tanh(dz)}{z\coth z-1}>0.
\]
The two endpoint values are also strictly increasing in \(d\). Hence for \(d_2>d_1>0\), the continuous difference \(R_{d_2}-R_{d_1}\) is positive on the compactified \(z\)-interval and has a positive minimum. It follows that
\[
C(d_2)>C(d_1).
\]
Thus \(C\) is continuous and strictly increasing.

### 7. Classification

Equation (1) says that the entire comparison is controlled by whether \(s\) lies below, on, or above \(\inf R_d\).

For \(d\ge\log2\), (9) and \(s<U(d)=d\) immediately give \(R_d(z)>s\) for all \(z>0\), hence \(M>I\).

For \(d_0<d<\log2\), (8) shows that all three positions relative to \(C(d)\) are genuinely possible inside \(E_4\). If \(s<C(d)\), then \(R_d(z)>s\) for every \(z\), giving strict \(M>I\). If \(s=C(d)\), then \(R_d\ge s\) and an interior minimizer supplies an unequal equality pair. If \(s>C(d)\), some \(z\) has \(R_d(z)<s\), hence \(M<I\) there. But \(s<U(d)\) is below both endpoint limits \(3d^2/2\) and \(d\), so \(M>I\) for \(z\) sufficiently near \(0\) and for \(z\) sufficiently large. This proves the mixed-sign statement and forces at least two nontrivial zeros by continuity.

## Two explicit \(E_4\) examples

### A globally positive point

Take
\[
d=\frac34,\qquad s=\frac{18}{25},
\qquad
(a,b)=\left(\frac{147}{200},-\frac{3}{200}\right).
\]
Then
\[
3d^2-2s=\frac{99}{400}>0,
\qquad
2d^2-3s+1=-\frac7{200}<0,
\]
and \(ab<0\), so this is an interior \(E_4\) point. Since \(d=3/4>\log2\), the theorem gives
\[
M(a,b;x,y)>I(x,y)
\]
for every unequal positive pair.

### A mixed-sign point with an exact certificate

Take
\[
d=\frac23,\qquad s=\frac{33}{50},
\qquad
(a,b)=\left(\frac{199}{300},-\frac1{300}\right).
\]
Then
\[
3d^2-2s=\frac1{75}>0,
\qquad
2d^2-3s+1=-\frac{41}{450}<0,
\]
so this is also in \(E_4\). Near \(x=y\),
\[
\log\frac{M}{I}
=
\frac{3d^2-2s}{6s}z^2+O(z^4)>0.
\]
At the ratio \(y/x=64\), equivalently \(z=3\log2\),
\[
\log\frac{M}{I}
=
1+\frac{50}{33}\log\frac{17}{8}
-\frac{65}{21}\log2.
\tag{10}
\]
For \(0<q<1\),
\[
2\left(q+\frac{q^3}{3}+\frac{q^5}{5}\right)
<
\log\frac{1+q}{1-q}
<
2\left(q+\frac{q^3}{3}+\frac{q^5}{5}\right)
+\frac{2q^7}{7(1-q^2)}.
\]
Using \(q=9/25\) for \(\log(17/8)\) and \(q=1/3\) for \(\log2\), the right-hand side of (10) is rigorously bounded above by
\[
-\frac{43568079809}{14910328125000}<0.
\]
Thus \(M<I\) at \((x,y)=(1,64)\), while \(M>I\) for sufficiently close arguments and again for sufficiently large ratios. This supplies a completely explicit interior mixed-sign example.

## Reproducibility

`artifacts/verify_muirhead_identric_e4.py` checks the exact rational sign certificate above, the two \(E_4\) parameter examples, the hyperbolic normal form numerically, and gives illustrative numerical values of \(C(d)\). The theorem itself does not depend on numerical optimization.

## Limitations

- The sharp curve \(C(d)\) is characterized variationally; no elementary closed form is established for \(d_0<d<\log2\).
- Existence of an interior minimizer is proved there, but uniqueness is not claimed.
- This record addresses precisely the previously unclassified \(E_4\) region; the already classified \(E_1,E_2,E_3\) regions are not re-proved.
- The originality assessment is to the best of our knowledge. Equivalent prior coverage under substantially different notation, in unindexed literature, or in a source not retrieved by the documented searches remains possible.


## References

1. M.-K. Wang, Y.-M. Chu, and Y.-F. Qiu, “Some Comparison Inequalities for Generalized Muirhead and Identric Means,” *Journal of Inequalities and Applications* 2010, Article ID 295620. DOI: https://doi.org/10.1155/2010/295620
2. A. O. Pittenger, “Inequalities between arithmetic and logarithmic means,” *Publikacije Elektrotehničkog Fakulteta. Serija Matematika i Fizika* 678–715 (1981), 15–18. The sharp identric power-mean bound used above is quoted as equation (1.8) in reference 1.
3. Y.-M. Chu, M.-Y. Shi, and Y.-P. Jiang, “Exact inequalities involving power mean, arithmetic mean and identric mean,” *Rev. Anal. Numér. Théor. Approx.* 40(2) (2011), 120–127. DOI: https://doi.org/10.33993/jnaat402-1042
4. T. Zhao and Y.-M. Chu, “Comparison between the logarithmic and two-parameter generalized Muirhead means,” *Scientia Sinica Mathematica* 45(3) (2015), 233–244. DOI: https://doi.org/10.1360/N012013-00175
