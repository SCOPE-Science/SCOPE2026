# Three balloon-radius classes in an edge-incentric 8-simplex and a four-class obstruction
## Finding
For an edge-incentric Euclidean simplex whose incenter coincides with its centroid, four distinct balloon radii are impossible, while three distinct balloon radii do occur. In particular, there exists a nonregular edge-incentric \(8\)-simplex with nine reciprocal balloon radii
\[
1,\quad b,b,b,\quad c,c,c,c,c,
\]
where \(b\) is the unique zero in
\[
\frac{247953648}{10^9}<b<\frac{247953649}{10^9}
\]
of
\[
P(t)=136t^4+816t^3-5901t^2-18250t+4875,
\]
and
\[
c=\frac{-10744b^3-47192b^2+692955b+332475}{372560}.
\]
Numerically, \(b\approx0.24795364834026344\) and \(c\approx1.3453685908429687\). Thus the corresponding balloon radii are \(1\), \(1/b\) with multiplicity three, and \(1/c\) with multiplicity five.

## Assumptions and scope
An edge-incentric \(d\)-simplex has positive balloon radii \(\beta_1,\ldots,\beta_{d+1}\) characterized by \(\lVert A_i-A_j\rVert=\beta_i+\beta_j\). Put \(x_i=1/\beta_i\), \(M=\sum_i x_i\), and \(N=\sum_i x_i^2\). Hajja's existence criterion says that prescribed positive balloon radii occur precisely when
\[
M^2-(d-1)N>0.
\]
For such a simplex, coincidence of the incenter and centroid is equivalent to equiareality. Hajja's facet-volume formula makes this equivalent to constancy, over \(i\), of
\[
Q_i=x_i^2\bigl(M^2-(d-2)N+(d-1)x_i^2-2Mx_i\bigr).
\]
The result resolves the existence part of Hajja's stated open question for the cases of three and four distinct balloon-radius values. It does not classify all three-value examples and does not assert that dimension \(8\) is minimal.

## Proof
Let the common value of the \(Q_i\) be \(K\), and set
\[
C=M^2-(d-2)N.
\]
Every distinct reciprocal balloon radius is then a positive zero of
\[
F(z)=(d-1)z^4-2Mz^3+Cz^2-K.
\]
The coefficient of \(z\) is zero. If four distinct positive values occurred, they would be the four roots of \(F\). Vieta's formula would then give
\[
0=-(d-1)e_3,
\]
where \(e_3\) is the sum of the four triple products of the roots. This is impossible because all four roots are positive. Hence four distinct balloon radii never occur.

For existence with three values, take \(d=8\) and seek reciprocal balloon radii with multiplicities \(1,3,5\):
\[
1,\quad b,b,b,\quad c,c,c,c,c.
\]
Thus
\[
M=1+3b+5c,\qquad N=1+3b^2+5c^2.
\]
Introduce a fourth auxiliary root
\[
s=-\frac{bc}{b+c+bc}.
\]
Then the cubic elementary symmetric function of \(1,b,c,s\) vanishes identically. Consequently
\[
G(z)=7(z-1)(z-b)(z-c)(z-s)
\]
has no \(z\)-term. Matching the \(z^3\) and \(z^2\) coefficients of \(G\) with those of
\[
7z^4-2Mz^3+(M^2-6N)z^2-K
\]
is equivalent, after multiplication by \(b+c+bc\), to
\[
\begin{aligned}
H_1={}&-b^2c-b^2+3bc^2+4bc-5b+3c^2-5c=0,\\
H_2={}&-9b^3c-9b^3+23b^2c^2+20b^2c-b^2-5bc^3\\
&+28bc^2+4bc-5b-5c^3+3c^2-5c=0.
\end{aligned}
\]
With
\[
c=\frac{-10744b^3-47192b^2+692955b+332475}{372560},
\]
direct polynomial division gives the exact factorizations
\[
H_1=\frac{P(b)A(b)}{138800953600},
\]
where
\[
A(b)=2546328b^3+9637368b^2-174872335b-59018575,
\]
and
\[
H_2=\frac{P(b)B(b)}{10342336654643200},
\]
where
\[
\begin{aligned}
B(b)={}&9119249344b^6+74570064256b^5+286367804048b^4\\
&+479231239776b^3-48108539657769b^2\\
&-53690303071570b-11936394528025.
\end{aligned}
\]
Therefore every zero \(b\) of \(P\) for which the displayed expression for \(c\) is defined satisfies both coefficient conditions.

At the rational endpoints of the asserted interval, exact evaluation gives
\[
P\!\left(\frac{247953648}{10^9}\right)>0,
\qquad
P\!\left(\frac{247953649}{10^9}\right)<0.
\]
Moreover, for \(0<t<1\),
\[
P'(t)=544t^3+2448t^2-11802t-18250<-15258<0,
\]
so this zero \(b\) is unique in the interval. In particular \(0<b<1/4\). The formula for \(c\) gives \(c>1\): using \(b>6/25\) and \(b<1/4\), the numerator of \(c-1\) is larger than
\[
-\frac{10744}{64}-\frac{47192}{16}+692955\frac{6}{25}-40085
=\frac{4924273}{40}>0.
\]
Thus \(1,b,c\) are positive and pairwise distinct, while \(s<0\).

It remains to verify that these radii actually define an edge-incentric simplex. Reducing \(M^2-7N\) modulo \(P(b)=0\) after the substitution for \(c\) gives
\[
M^2-7N=\frac{1224b^3-3584b^2-82717b+22782}{18628}.
\]
For \(0<b<1/4\), its numerator exceeds
\[
-\frac{3584}{16}-\frac{82717}{4}+22782=\frac{7515}{4}>0.
\]
Hence Hajja's existence criterion holds.

Finally, the two coefficient identities imply that \(G\) is precisely of the form
\[
7z^4-2Mz^3+(M^2-6N)z^2-K
\]
for some constant \(K\). Since \(1,b,c\) are roots of \(G\), the corresponding values of \(Q_i\) are equal. The resulting edge-incentric \(8\)-simplex is therefore equiareal, so its incenter equals its centroid. It has exactly three distinct balloon radii.

## Verification
The accompanying checker uses exact rational polynomial arithmetic. It verifies the two displayed polynomial factorizations, the reduction of \(M^2-7N\), the signs of \(P\) at the rational isolating endpoints, and the algebraic coefficient identities used in the construction. It also evaluates the isolated algebraic root at high precision as a diagnostic only. The impossibility of four positive classes is the Vieta argument above and does not depend on numerical experimentation.

## Relationship to prior work
Hajja introduced the balloon-radius parametrization and, for the incenter-centroid coincidence, proved that the reciprocal balloon radii satisfy a quartic whose missing linear term bounds the number of distinct values by four. He completely characterized the two-value case, then explicitly left the existence of the three- and four-value cases open. The present argument uses the missing linear coefficient twice: first as the immediate Vieta obstruction to four positive roots, and second to construct a three-positive-root quartic with one negative auxiliary root. Wu and Zhang later studied the circumradius of the same class of edge-incentric simplices; their result does not address equiareality or the number of balloon-radius classes.

## Limitations
The construction supplies one exact three-value family member and rules out the four-value case globally. It does not classify all multiplicity patterns or all algebraic solutions in the three-value case, and it does not establish the least dimension in which three values can occur. The originality search covered the source paper, later same-object circumradius work, exact phrase and polynomial searches, and the available published-finding index; an older or differently worded resolution outside those sources remains a residual bibliographic risk.

## References
1. M. Hajja, *Coincidences of Centers of Edge-Incentric, or Balloon, Simplices*, Results in Mathematics 49 (2006), 237–263, DOI 10.1007/s00025-006-0222-4.
2. Y.-D. Wu and Z.-H. Zhang, *On the Circumradius of a Special Class of n-Simplices*, arXiv:1007.1602.
