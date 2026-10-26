# A doubled Hasse divisor and an intermediate-slope genus-four stratum in characteristic seven

## Finding
For the smooth, marked genus-four family
\[
C_{a,b}:\quad y^3=x^5+ax+b,\qquad a^5\ne b^4,
\]
over characteristic \(7\), the Cartier/Hasse determinant in its natural basis is \(2a^2(a^5-b^4)\). Consequently the Hasse determinant vanishes to order **two**, not one, along the reduced nonordinary divisor \(a=0\) on the smooth parameter locus. The Jacobian has rank \(4\), \(a\)-number \(0\) for \(a\ne0\), and rank \(0\), \(a\)-number \(2\) for \(a=0,b\ne0\). There are no intermediate ranks.

Every geometric exceptional member is isomorphic to \(C_{0,1}:y^3=x^5+1\), whose zeta numerator and Newton polygon are
\[
L_{C_{0,1}}(T)=1-77T^4+2401T^8,\qquad
\operatorname{NP}=\{(1/4)^4,(3/4)^4\}.
\]
Thus this unique exceptional geometric isomorphism class is \(7\)-rank zero but is **not supersingular**.

For every \(q=7^n\) with \(n\ge1\), the exact count of smooth **marked coefficient pairs**, rather than isomorphism classes, is
\[
\#U_0(\mathbb F_q)=q-1,\qquad
\#U_4(\mathbb F_q)=(q-1)^2,\qquad
\#U(\mathbb F_q)=q(q-1).
\]
The corresponding Grothendieck-ring classes are \([U_0]=\mathbb L-1\) and \([U_4]=(\mathbb L-1)^2\).

## Assumptions and scope
Let \(k\) be an algebraic closure of a perfect field of characteristic \(7\). The model is the smooth projective normalization of the affine superelliptic equation, with the distinguished coordinate form and coefficients \((a,b)\). The polynomial \(f=x^5+ax+b\) is separable precisely when \(a^5-b^4\ne0\): solving \(f=f'=0\) gives the equality, and conversely a root exists over \(k\). Since \(\gcd(3,5)=1\), such curves have genus \((3-1)(5-1)/2=4\) and a unique point at infinity. Throughout, \(7\)-rank refers to the geometric \(7\)-rank of the Jacobian, \(a\)-number to the kernel dimension of the Cartier operator on regular differentials, and ordinary means \(7\)-rank \(4\). Counting formulas apply to **ordered normalized coefficient pairs**, not moduli-isomorphism classes.

## Proof
The following four regular differentials form a complete basis:
\[
\omega_0=dx/y,\quad \omega_1=dx/y^2,\quad
\omega_2=x\,dx/y^2,\quad\omega_3=x^2\,dx/y^2.
\]
This is the standard superelliptic regular-differential basis (the pole-order test at the unique point at infinity gives the same four). Write the Cartier map in source-to-target convention and temporarily omit the inverse-Frobenius roots from its coefficients. Since \(y^{-j}=(y^{-j})^7f^{2j}\), the coefficient of \(x^k dx/y^j\) in the image of \(x^i dx/y^j\) is the seventh root of the coefficient of \(x^{7(k+1)-1-i}\) in \(f^{2j}\). No mixing occurs between the two \(j\)-blocks.

Expanding \(f^2\) and \(f^4\) exactly modulo \(7\) yields
\[
H_1=(2a),\qquad
H_2=\begin{pmatrix}
5ab^2&0&1\\
4b^3&6a^2&0\\
a^4&5ab&0
\end{pmatrix}.
\]
A direct determinant expansion gives
\[
\det H_2=a(a^5-b^4),\qquad
\det H=2a^2(a^5-b^4).
\]
On \(U=\operatorname{Spec}k[a,b,(a^5-b^4)^{-1}]\), the discriminant factor is a unit, so the *scheme-theoretic* zero divisor of this chosen Hasse determinant is exactly \(2\{a=0\}\). Taking seventh roots of matrix entries changes the presentation of the Cartier map but not its invertibility or rank; the polynomial matrix \(H\) is the Hasse–Witt-transpose coefficient matrix defining the determinant section, so its divisor order is computed in the polynomial presentation.

For \(a\ne0\), \(H\) is invertible and the curve is ordinary. For \(a=0,b\ne0\), its one-dimensional block vanishes and the other block specializes to
\[
H_2\big|_{a=0}=\begin{pmatrix}0&0&1\4b^3&0&0\0&0&0\end{pmatrix}.
\]
Cartier is semilinear, but this nonzero-entry pattern is a chain of length three, so Cartier has rank \(2\), its square remains nonzero, and its cube is zero. Since the stable Cartier image has dimension equal to the \(7\)-rank, the latter vanishes; the \(a\)-number is \(4-2=2\). For any \(b\ne0\) over \(k\), scaling \(x=\lambda X\), \(y=\mu Y\) with \(\lambda^5=\mu^3=b\) produces an isomorphism \(C_{0,b}\simeq C_{0,1}\).

For the latter curve, exact point counts (with the unique point at infinity included) over the first four extensions are
\[
(\#C(\mathbb F_7),\#C(\mathbb F_{49}),\#C(\mathbb F_{343}),\#C(\mathbb F_{2401}))
=(8,50,344,2094).
\]
Writing \(S_n=7^n+1-\#C(\mathbb F_{7^n})\), Newton identities give the first four coefficients of the degree-eight Weil polynomial \(L(T)\) as \((1,0,0,0,-77)\). The genus-four functional equation determines the remaining coefficients, giving \(L(T)=1-77T^4+2401T^8\). Its \(7\)-adic Newton polygon is the lower convex hull of \((0,0),(4,1),(8,4)\), with four slopes \(1/4\) and four slopes \(3/4\). This Newton polygon is geometric, so it holds for every exceptional member over \(k\).

Finally, the excluded discriminant curve \(a^5=b^4\) is parametrized over **every** field \(\mathbb F_q\) of characteristic \(7\) by \((a,b)=(t^4,t^5)\), including \((0,0)\): for nonzero \((a,b)\) recover \(t=b/a\). It has precisely \(q\) rational points and Grothendieck class \(\mathbb L\) (it is the bijective monomial cusp, with a piecewise algebraic isomorphism to \(\mathbb A^1\)). The exceptional smooth locus \(a=0,b\ne0\) is \(\mathbb G_m\). Subtracting the cusp and this line from \(\mathbb A^2\) gives the claimed two strata and classes.

## Verification
Run `python3 verify.py` using Python's standard library. The checker expands \(f^2,f^4\) modulo \(7\), reproduces the matrix entries and determinant, tests the exceptional nilpotent chain, exhaustively checks the \(\mathbb F_7\) parameter partition, constructs irreducible presentations of all \(\mathbb F_{7^n}\) for \(1\le n\le4\), and exhaustively counts the points needed for the exceptional Weil polynomial. The observed success marker is `VERIFY_OK`. Universal parameter counts and Cartier classification follow from the symbolic proof, not the finite enumerations.

## Relationship to prior work
Baldwin–Eilbeck–Gibbons–Ônishi analyze the general cyclic trigonal genus-four model from the standpoint of complex Abelian functions. Elkin gives the general Cartier formalism and rank bounds for cyclic covers; the coefficient-extraction identity used here is standard. Kudo–Harashita show that superspecial genus-four curves do not exist in characteristic seven, consistent with the exceptional \(a\)-number \(2\) and its non-supersingular Newton polygon. The contribution examined here is the **exact nonreduced Hasse divisor with complete geometric rank dichotomy, exceptional Newton polygon, and all-extension marked-parameter census for this specific two-parameter family**. General methods may imply pieces of it; no global claim of novelty for the Cartier method or model is made.

## Limitations
The classification uses a distinguished normalized parameterization; it does not enumerate isomorphism classes over finite fields. The calculation of a unique exceptional geometric isomorphism type refers only to the nonordinary locus *inside this family*. The exact Newton polygon is proved for the exceptional class; other ordinary members need no separate Newton calculation. Relevant newer work on \(a\)-numbers of genus-four superelliptic curves was not fully inspectable and could contain partial or stronger overlap. No independent external audit has yet been performed.

## References
1. S. Baldwin, J. C. Eilbeck, J. Gibbons, and Y. Ônishi, *Abelian Functions for Cyclic Trigonal Curves of Genus Four*, arXiv:math/0612654 (initial public version 2006-12-21), https://arxiv.org/abs/math/0612654.
2. A. Elkin, *The Rank of the Cartier operator on cyclic covers of the projective line*, arXiv:0708.0431 (initial public version 2007-08-02), https://arxiv.org/abs/0708.0431.
3. M. Kudo and S. Harashita, *Superspecial curves of genus 4 in small characteristic*, arXiv:1607.01114 (initial public version 2016-07-05), https://arxiv.org/abs/1607.01114.
4. Y. Sohn, *The a-number of superelliptic curves of genus four*, Journal of Applied and Pure Mathematics (2025), DOI:10.23091/japm.2025.059; incomplete full-text access, potential overlapping \(a\)-number treatment.
