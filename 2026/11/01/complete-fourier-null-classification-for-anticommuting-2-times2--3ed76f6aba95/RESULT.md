# Complete Fourier-null classification for anticommuting \(2\times2\) matrices over odd finite fields

## Finding
For every odd prime power \(q\ge5\), let \(F=\mathbb F_q\) and consider the anti-commuting variety
\[
\mathcal C_q=\{(X,Y)\in M_2(F)^2:XY+YX=0\}.
\]
For any fixed nontrivial additive character \(\psi\) of \(F\), put
\[
\mathscr F(A,B)=\sum_{(X,Y)\in\mathcal C_q}\psi\big(\operatorname{tr}(AX+BY)\big).
\]
For frequency matrices, write \(A=aI+P\), \(B=bI+R\), where \(P,R\) are traceless, and put \(Q(Z)=\tfrac12\operatorname{tr}(Z^2)\), \(\langle Z,W\rangle=\tfrac12\operatorname{tr}(ZW)\) on the traceless three-space, and \(c=\langle P,R\rangle\). Let \(\chi\) be the quadratic multiplicative character, with \(\chi(0)=0\). Then **the complete Fourier-zero set** consists exactly of the following disjoint families:

1. \(P\ne0\), \(Q(P)=0\), \(\chi(Q(R))=-1\), \(a\ne0\), and \(\chi(c^2+2abc+Q(R)a^2)=1\).
2. \(R\ne0\), \(Q(R)=0\), \(\chi(Q(P))=-1\), \(b\ne0\), and \(\chi(c^2+2abc+Q(P)b^2)=1\).

In either family \(c\ne0\) follows automatically. Consequently, unnormalized convolution by \(\mathbf1_{\mathcal C_q}\) on the additive group \(M_2(F)^2\) has
\[
\boxed{\dim\ker T_q=\frac{q(q^2-1)(q-1)^4}{2}},\qquad
\boxed{\operatorname{rank}T_q=q^8-\frac{q(q^2-1)(q-1)^4}{2}}.
\]
For \(q=5\), this is nullity \(15,360\) and rank \(375,265\); for \(q=7\), nullity \(217,728\) and rank \(5,547,073\). Thus the nullity proportion is asymptotic to \(1/(2q)\). The lower bound \(q\ge5\) is substantive: extra cancellations arise for \(q=3\), which is excluded.

## Assumptions and scope
Here \(q\) is an arbitrary odd prime power at least five, not necessarily prime, and the Fourier transform is the **unnormalized** additive transform with the trace pairing. All matrices and all characters are over \(F\). The operator \(T_q f=\mathbf1_{\mathcal C_q}*f\) acts on the complex space of dimension \(q^8\); its eigenvectors are the additive characters, so rank equals the number of nonzero Fourier coefficients. The statement is not about a complex-algebraic or characteristic-two version of the variety.

Identify the traceless space \(W\) with triples by
\[
(u,v,w)\longleftrightarrow\begin{pmatrix}u&v\\w&-u\end{pmatrix},
\quad Q(u,v,w)=u^2+vw,
\quad\langle U,V\rangle=\frac{Q(U+V)-Q(U)-Q(V)}2.
\]
This form is a split, nondegenerate three-dimensional quadratic form. The distinction between matrix frequencies \((A,B)\) and their scalar/traceless coordinates \((a,b,P,R)\) is bijective because the characteristic is odd.

## Proof
**1. Exact decomposition of the anti-commuting locus.** Write \(X=tI+U\), \(Y=sI+V\) with \(U,V\in W\). The matrix identity \(UV+VU=2\langle U,V\rangle I\) gives
\[
XY+YX=0\quad\Longleftrightarrow\quad
 tV+sU=0,\qquad ts+\langle U,V\rangle=0.
\]
Split into \(t=s=0\); \(t\ne0,s=0\); \(t=0,s\ne0\); and \(ts\ne0\). In the last stratum \(U=tZ,\ V=-sZ,\ Q(Z)=1\), or equivalently \(X=t(I+Z),Y=s(I-Z)\). In the middle two strata the free traceless variable has \(q^3\) choices. These strata are disjoint and exhaustive.

**2. An exact integer Fourier multiplier.** Let \(\Sigma=\{Z\in W:Q(Z)=1\}\); \(|\Sigma|=q^2+q\). Define
\[
N_1=\#\{Z\in\Sigma:\langle P,Z\rangle=-a\},\quad
N_2=\#\{Z\in\Sigma:\langle R,Z\rangle=b\},
\]
\[
N_{12}=\#\{Z\in\Sigma:\langle P,Z\rangle=-a,\ \langle R,Z\rangle=b\}.
\]
Fourier orthogonality in the first stratum (using a Lagrange multiplier for \(\langle U,V\rangle=0\)) gives \(q^5\mathbf1_{P=R=0}+q^3\mathbf1_{c=0}-q^2\). The two one-nonzero-scalar strata contribute \(q^3\mathbf1_{P=0}(q\mathbf1_{a=0}-1)\) and \(q^3\mathbf1_{R=0}(q\mathbf1_{b=0}-1)\). Summing over \(t,s\in F^\times\) in the last stratum gives \(q^2N_{12}-q(N_1+N_2)+q(q+1)\). Thus, *for all frequencies*,
\[
\begin{aligned}
\mathscr F(A,B)={}&q^5\mathbf1_{P=R=0}+q^3\mathbf1_{c=0}-q^2\\
&+q^3\mathbf1_{P=0}(q\mathbf1_{a=0}-1)
+q^3\mathbf1_{R=0}(q\mathbf1_{b=0}-1)\\
&+q^2N_{12}-q(N_1+N_2)+q(q+1).
\end{aligned}
\tag{1}
\]
The factor of two from the matrix trace pairing does not change any character-orthogonality constraint, since two is invertible in \(F\). Formula (1) also proves that every Fourier coefficient is an integer.

**3. Hyperplane sections of the unit quadric.** For \(H\in W\setminus\{0\}\), let \(N(H,d)=\#\{Z\in\Sigma:\langle H,Z\rangle=d\}\). A Witt-coordinate calculation gives the complete table
\[
N(H,d)=\begin{cases}
2q,&Q(H)=0,\ d=0,\\
q,&Q(H)=0,\ d\ne0,\\
2q-1,&Q(H)\text{ a nonzero square},\ d^2=Q(H),\\
q-1,&Q(H)\text{ a nonzero square},\ d^2\ne Q(H),\\
q+1,&\chi(Q(H))=-1.
\end{cases}
\tag{2}
\]
For clarity, when \(H\) is isotropic, choose Witt coordinates \(H=(0,1,0)\); the section equation fixes the complementary isotropic coordinate, leaving a product equation. For nonisotropic \(H\), decompose \(Z=(d/Q(H))H+Z_\perp\); the binary form on \(H^\perp\) is hyperbolic precisely when \(Q(H)\) is square. Counting solutions of its level equation yields the last three rows. In particular \(q-1\le N(H,d)\le2q\) for nonzero \(H\).

**4. Reduction to one geometric possibility.** If \(P=0\ne R\), direct substitution in (1) gives \(\mathscr F=q(1-N_2)\) when \(a\ne0\), and \(\mathscr F=q(q-1)(q^2-1+N_2)\) when \(a=0\). Both are nonzero by (2); the symmetric case is analogous. If \(P=R=0\), direct substitution shows the coefficient is positive in each of the four cases \((a=0\text{ or }\ne0,\ b=0\text{ or }\ne0)\).

Now take \(P,R\ne0\). If \(c=0\), (1) divided by \(q\) is at least \(q^2-4q+1>0\) for \(q\ge5\). For \(c\ne0\), it reduces to
\[
\mathscr F/q=qN_{12}-N_1-N_2+1.
\tag{3}
\]
If \(P,R\) are dependent, their two affine hyperplanes are identical or disjoint; hence \(N_{12}=N_1=N_2\) or \(N_{12}=0\), and (3) is respectively \((q-2)N_1+1>0\) or \(1-(N_1+N_2)<0\). If independent, their intersection is an affine line in \(W\), meeting \(Q=1\) in \(0,1,2\), or \(q\) points. By (2), for \(q\ge5\), (3) can vanish only for
\[
N_{12}=2,\qquad N_1+N_2=2q+1.
\tag{4}
\]
Inspection of the exact five possibilities (2) shows (4) requires one of \(N_1,N_2\) to be \(q\), and the other \(q+1\). The former is an isotropic nonzero normal with nonzero section value; the latter is a normal of nonsquare norm. This proves the two orientations asserted in the theorem, except for their final square-class condition.

**5. The discriminant condition.** Suppose \(Q(P)=0\), \(P\ne0\), \(\chi(Q(R))=-1\), and \(a\ne0\). Every vector in \(P^\perp\) has square norm; therefore \(c=\langle P,R\rangle\ne0\). The two affine equations of (4) specify an affine line \(Z_0+\lambda H\), with \(H\) spanning the orthogonal complement of \(\operatorname{span}(P,R)\) and \(Z_0\in\operatorname{span}(P,R)\). The Gram matrix has determinant \(-c^2\). Solving the two linear equations yields
\[
Q(Z_0)=\frac{-2abc-Q(R)a^2}{c^2}.
\]
The form on the orthogonal line has square norm, because \(Q\) is split of determinant \(-1/4\) and the plane has Gram determinant \(-c^2\). Consequently the line meets \(Q=1\) in exactly two points precisely when \(1-Q(Z_0)\) is a *nonzero square*; equivalently
\[
\chi\big(c^2+2abc+Q(R)a^2\big)=1.
\]
Interchanging the roles of \((P,a)\) and \((R,b)\) gives the other orientation. This proves the stated if-and-only-if Fourier-zero criterion.

**6. Counting all Fourier zeros.** The nonzero isotropic vectors of \(W\) number \(q^2-1\). There are \(q(q-1)^2/2\) vectors with nonsquare norm: for each nonsquare \(d\ne0\), the equation \(Q(Z)=d\) has \(q^2-q\) solutions. Choose one isotropic normal, then the nonsquare normal, then its associated nonzero scalar (\(q-1\) choices). The remaining scalar occurs linearly with nonzero slope in the discriminant, giving exactly \((q-1)/2\) nonzero-square discriminants. The two orientations are disjoint. Thus the number of vanishing frequencies is
\[
2(q^2-1)\frac{q(q-1)^2}{2}(q-1)\frac{q-1}{2}
=\frac{q(q^2-1)(q-1)^4}{2}.
\]
Fourier diagonalization of additive convolution proves the asserted rank and nullity.

## Verification
The standalone `check_antico_fourier.cpp` implements formula (1) using integer arithmetic over the prime fields with orders three, five and seven. It exhaustively checks the claimed zero criterion for all \(390625\) frequency pairs at \(q=5\) and all \(5764801\) frequency pairs at \(q=7\), including the predicted zero counts \(15360\) and \(217728\). For \(q=3\), it records \(384\) zero frequencies and thereby independently confirms why the theorem does not extend as stated. The checker additionally enumerates all actual anti-commuting matrix pairs, forms exact character-exponent histograms, and compares their Fourier coefficients with formula (1) for all \(6561\) frequencies at \(q=3\) and \(411\) deterministic frequencies at \(q=5\). Exact root-of-unity sums are tested via coefficient equality, not floating-point thresholds. A separate `check_gf9.py` constructs the degree-two extension field with exact arithmetic and verifies the criterion on \(2850\) deterministic test frequencies, including \(152\) positive zero-family cases. Output from the prime-field checker terminates `ANTICOMMUTING_FOURIER_NULLITY_ALL_CHECKS_OK`. Run with `c++ -O3 -std=c++17 check_antico_fourier.cpp -o check && ./check` and `python3 check_gf9.py`.

The analytic arguments above establish the theorem for **all** odd prime powers at least five. Finite prime-field tests neither prove an infinite assertion nor independently verify extension-field arithmetic.

## Relationship to prior work
Iosevich and Koh's 2008 analysis of finite-field quadratic-surface Fourier transforms supplies important context for the quadratic level-set counts used here, but not a Fourier-null classification of pairs of anti-commuting matrices. Britnell and Wildon's 2010 work studies commuting-matrix types, without the anti-commutator Fourier spectrum. Chen and Wang study anti-commuting matrix varieties and irreducible components in their 2018 preprint; their focus is algebraic geometry rather than the complete finite-field additive spectrum. Huang's 2021 paper explicitly counts \(AB=\zeta BA\) pairs, including \(\zeta=-1\), through a generating function; its Theorems 1.1–1.2 count total points and do not give the full frequency-dependent zero set. Browning, Sawin and Wang's later paper on *commuting* integer matrices studies related exponential sums but not this criterion. The present result classifies all Fourier zeros, not merely the zero-frequency point count, and thereby determines an exact convolution nullity. These comparisons do not exclude every possible alternate formulation in the older finite-field character-sum or matrix-association literature.

## Limitations
The classification is for \(q\ge5\) odd prime powers. Characteristic two, the three-element field, larger matrices, nonscalar anti-commutation parameters, and a full multiplicity classification of **nonzero** eigenvalues are not asserted. The formula (1) supplies every individual eigenvalue but no compressed distribution of its distinct nonzero values. The analytic proof is not an independent mathematical audit. Historical originality uncertainty remains for potentially equivalent general exponential-sum identities.

## References
- A. Iosevich and D. Koh, *Extension theorems for the Fourier transform associated with non-degenerate quadratic surfaces in vector spaces over finite fields*, arXiv:0804.4505v1, public 2008-04-28. https://arxiv.org/abs/0804.4505
- J. Britnell and M. Wildon, *On types and classes of commuting matrices over finite fields*, arXiv:1001.0811v1, 2010. https://arxiv.org/abs/1001.0811
- X. Chen and W. Wang, *Anti-commuting matrices*, arXiv:1805.00378, 2018. https://arxiv.org/abs/1805.00378
- Y. Huang, *Counting on the variety of modules over the quantum plane*, arXiv:2110.15570v1, 2021. https://arxiv.org/abs/2110.15570
- T. Browning, W. Sawin and J. Wang, *Pairs of commuting integer matrices*, arXiv:2409.01920v1, 2024. https://arxiv.org/abs/2409.01920
