# Complete Zbăganu extremizers of the affine-regular hexagonal plane
## Finding
Let \(X=(\mathbb R^2,N)\), where
\[
N(s,t)=\max\{|s|,|t|,|s-t|\}.
\]
Then
\[
C_Z(X)=\frac54.
\]
Moreover, a nonzero pair \((x,y)\) attains \(C_Z(X)\) if and only if, after possibly exchanging \(x\) and \(y\), there exist \(r>0\), signs \(\varepsilon,\delta\in\{-1,1\}\), and a linear isometry \(T\) of \(X\) such that
\[
x=\varepsilon r\,T(0,1),
\qquad
y=\delta r\,T\!\left(-\frac12,-\frac14\right).
\]
Equivalently, in every maximizing pair the larger vector has twice the norm of the smaller one; after normalization the larger vector points to a vertex of the affine-regular hexagonal unit ball and the smaller vector points to the midpoint of the corresponding opposite-adjacent side orbit. Thus the classical counterexample value \(C_Z=5/4\) has a single maximizing orbit modulo the natural dihedral symmetries, independent vector signs, exchange, and common scaling.

## Assumptions and scope
The scalar field is real. The norm is
\[
N(s,t)=\max\{|s|,|t|,|s-t|\},
\]
whose unit ball is an affine-regular centrally symmetric hexagon. The Zbăganu constant is
\[
C_Z(X)=
\sup_{\substack{x,y\in X\\(x,y)\ne(0,0)}}
\frac{N(x+y)N(x-y)}{N(x)^2+N(y)^2}.
\]
The quotient is unchanged by common nonzero scaling, by changing either vector sign, by exchanging the vectors, and by applying a common linear isometry of \(X\).

## Proof
Let
\[
\phi_1(s,t)=s,\qquad
\phi_2(s,t)=t,\qquad
\phi_3(s,t)=s-t.
\]
Then
\[
N(z)=\max_{1\le i\le3}|\phi_i(z)|.
\]
Fix nonzero \(x,y\), and choose active functionals \(f,g\) from this set so that
\[
N(x+y)=|f(x+y)|,\qquad
N(x-y)=|g(x-y)|.
\]

If \(f=g\), then
\[
|f(x+y)g(x-y)|
=
|f(x)^2-f(y)^2|
\le
N(x)^2+N(y)^2,
\]
so this branch cannot attain a value larger than \(1\).

Assume that \(f\ne g\). By changing the signs of \(f\) and \(g\), which does not change their absolute values, the third defining functional can be written as \(f+g\). Put
\[
r=N(x),\qquad s=N(y),\qquad u=\frac{x}{r},\qquad v=\frac{y}{s}.
\]
Set
\[
a=f(u),\qquad b=g(u),\qquad c=f(v),\qquad d=g(v).
\]
Because \(N(u)=N(v)=1\),
\[
|a|,\ |b|,\ |a+b|\le1,
\qquad
|c|,\ |d|,\ |c+d|\le1.
\]
The selected branch of the numerator is
\[
|(ra+sc)(rb-sd)|
=
\left|
\begin{pmatrix}r&s\end{pmatrix}
M
\begin{pmatrix}r\\s\end{pmatrix}
\right|,
\]
where
\[
M=
\begin{pmatrix}
ab&(cb-ad)/2\\
(cb-ad)/2&-cd
\end{pmatrix}.
\]
Its determinant and discriminant are
\[
\det M=-\frac{(ad+bc)^2}{4},
\]
and
\[
(\operatorname{tr}M)^2-4\det M
=
(a^2+c^2)(b^2+d^2).
\]
Hence the spectral radius of \(M\) is
\[
\rho(M)
=
\frac{|ab-cd|+\sqrt{(a^2+c^2)(b^2+d^2)}}{2}.
\]

Suppose first that \(ab\ge cd\). By the arithmetic--geometric mean inequality,
\[
\rho(M)
\le
\frac14\left((a+b)^2+(c-d)^2\right)
\le
\frac14(1+4)
=
\frac54.
\]
If \(cd\ge ab\), the same calculation gives
\[
\rho(M)
\le
\frac14\left((a-b)^2+(c+d)^2\right)
\le
\frac54.
\]
Therefore
\[
N(x+y)N(x-y)
\le
\frac54\bigl(N(x)^2+N(y)^2\bigr),
\]
so
\[
C_Z(X)\le\frac54.
\]

For
\[
x=(0,1),\qquad
y=\left(-\frac12,-\frac14\right),
\]
one has
\[
N(x)=1,\qquad N(y)=\frac12,
\]
and
\[
N(x+y)=N(x-y)=\frac54.
\]
Thus the quotient is
\[
\frac{(5/4)^2}{1+(1/2)^2}
=
\frac54,
\]
which proves the value.

It remains to trace equality. In the case \(ab\ge cd\), equality in the preceding upper bound requires
\[
a^2+c^2=b^2+d^2,\qquad |a+b|=1,\qquad |c-d|=2.
\]
The last condition forces
\[
c=-d=\pm1.
\]
Then equality of the two quadratic sums gives \(|a|=|b|\), and \(|a+b|=1\) forces
\[
a=b=\pm\frac12.
\]
Thus one normalized direction is a side midpoint and the other is a vertex. In the case \(cd\ge ab\), the roles are reversed:
\[
a=-b=\pm1,\qquad c=d=\pm\frac12.
\]

The final equality condition comes from the quadratic-form estimate
\[
|z^TMz|\le\rho(M)\|z\|_2^2.
\]
For the vertex--midpoint configuration, \(M\) has rank one and its nonzero eigenvalue has absolute value \(5/4\). Its corresponding positive eigenvector has coordinate ratio \(2:1\). Consequently the vertex-directed vector has twice the norm of the midpoint-directed vector.

Finally,
\[
R(s,t)=(s-t,s),\qquad S(s,t)=(t,s)
\]
are linear isometries of \(N\). They generate the dihedral action on the six vertices and six side midpoints. Applying these isometries, together with independent vector signs and exchange, reduces every equality configuration to
\[
x=r(0,1),\qquad
y=r\left(-\frac12,-\frac14\right).
\]
Conversely every pair in this orbit attains the displayed quotient, completing the classification.

## Verification
The proof treats every possible active-functional branch. A branch using the same functional twice is bounded by \(1\), while every distinct-functional branch is controlled by the exact \(2\times2\) symmetric matrix above.

The algebraic identities used in the spectral calculation are
\[
\det M=-\frac{(ad+bc)^2}{4}
\]
and
\[
(\operatorname{tr}M)^2-4\det M
=
(a^2+c^2)(b^2+d^2).
\]
They were independently expanded symbolically. The representative pair was also substituted directly into the original norm, yielding the exact four values
\[
1,\quad \frac12,\quad \frac54,\quad \frac54.
\]
Random numerical sampling was used only as a stress test before the proof and is not evidence for the theorem.

## Relationship to prior work
Alonso and Martín introduced this hexagonal plane as the canonical counterexample to the conjecture that the Zbăganu and von Neumann--Jordan constants always coincide. Later sources record
\[
C_Z(X)=\frac54
<
\frac{3+\sqrt5}{4}
=
C_{\mathrm{NJ}}(X).
\]

Llorens-Fuster, Mazcuñán-Navarro, and Reich study both the Ptolemy and Zbăganu constants and identify the hexagon space among their concrete examples. Mizuguchi and Saito's complete 2012 exposition states the same piecewise Day--James norm and the exact value \(5/4\). Their complete 2011 article gives general necessary and sufficient conditions for several absolute-normalized Zbăganu identities, but does not state a complete maximizing-pair classification for this nonabsolute hexagonal counterexample.

Targeted searches under the named hexagon space, Day--James \(\ell_\infty-\ell_1\) notation, the value \(5/4\), maximizing-pair terminology, and Zbăganu equality language located the scalar value and related restricted constants, but no statement equivalent to the single-orbit classification proved here.

## Limitations
The theorem concerns one two-dimensional real polyhedral norm. It does not classify Zbăganu maximizers for arbitrary centrally symmetric hexagons or higher-dimensional Day--James constructions.

The original 2006 counterexample article and the complete body of the 2010 Ptolemy--Zbăganu article were not available through the checked lawful full-text routes. Their bibliographic and publisher materials were inspected, and this access limitation remains the principal originality risk. The exact date field uses the earliest checked source in this literature for which a day-level publication date was verified.

## References
1. J. Alonso and P. Martín, “A counterexample to a conjecture of G. Zbăganu about the Neumann--Jordan constant,” *Revue Roumaine de Mathématiques Pures et Appliquées* 51 (2006), 135--141.
2. E. Llorens-Fuster, E. M. Mazcuñán-Navarro, and S. Reich, “The Ptolemy and Zbăganu constants of normed spaces,” *Nonlinear Analysis* 72 (2010), 3984--3993, DOI 10.1016/j.na.2010.01.030; published 2010-06-01; primary MSC 46B20.
3. H. Mizuguchi and K.-S. Saito, “Some geometric constants of absolute normalized norms on \(\mathbb R^2\),” *Annals of Functional Analysis* 2 (2011), 22--33; received 2011-03-31 and accepted 2011-06-14; primary MSC 46B20.
4. H. Mizuguchi and K.-S. Saito, “The Zbăganu constant of absolute normalized spaces,” *RIMS Kôkyûroku* 1819 (2012), 103--110.
