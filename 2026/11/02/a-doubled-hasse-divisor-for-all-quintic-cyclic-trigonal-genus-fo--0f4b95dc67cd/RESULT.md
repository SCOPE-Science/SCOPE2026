# A doubled Hasse divisor for all quintic cyclic trigonal genus-four curves in characteristic seven

## Finding
Let \(k\) be an algebraically closed field of characteristic \(7\). Write
\[
F(x)=x^5+c_4x^4+c_3x^3+c_2x^2+c_1x+c_0,
\qquad \Delta(F)=\operatorname{disc}_x F,
\]
and let \(U\subset\mathbb A_k^5\) be the open subscheme \(\Delta(F)\ne0\). For every coefficient-marked point of \(U\), the smooth projective model of \(C_F:y^3=F(x)\) has genus four. Set
\[
h(F)=c_3^2+2c_4c_2+2c_1.
\]
With the Hasse–Witt normalization specified below, the determinant has the **universal polynomial identity**
\[
\boxed{\det H_F=h(F)^2\Delta(F)\quad\text{in }\mathbb F_7[c_0,c_1,c_2,c_3,c_4].}
\]
Consequently the scheme-theoretic nonordinary Hasse divisor on \(U\), in this coefficient trivialization, is \(2V(h)\). Its reduced support is a smooth, geometrically irreducible hypersurface, and all its fibers have Jacobian \(a\)-number **at least two** and \(7\)-rank **at most two**. Every smooth fiber off \(V(h)\) is ordinary. In particular, no smooth curve in this five-parameter cyclic trigonal family has Jacobian \(a\)-number one or \(7\)-rank three.

## Assumptions and scope
The field is algebraically closed of characteristic \(7\), the defining quintic is monic and separable, the curve means its smooth projective model, and the parameters remain coefficient-marked rather than being identified by changes of coordinates. The divisor assertion is about the coefficient parameter space \(U\), not a claimed equality of divisor classes on a moduli stack. We claim neither a complete Ekedahl–Oort classification nor that all nonordinary fibers have \(a\)-number exactly two.

## Proof
1. Since \(\gcd(3,5)=1\) and \(F\) is separable, the cyclic cover of \(\mathbb P^1\) defined by \(y^3=F(x)\) is smooth after projective completion and has genus \((3-1)(5-1)/2=4\). Its regular differentials have basis
\[
\omega_0=dx/y,\quad \omega_1=dx/y^2,\quad
\omega_2=x\,dx/y^2,\quad \omega_3=x^2\,dx/y^2.
\]
The pole-order test at the unique point above infinity gives precisely this basis.

2. In characteristic \(7\), the Cartier operator preserves the two displayed character subspaces because \(7\equiv1\pmod3\). Let \(A_r=[x^r]F(x)^2\) and \(B_r=[x^r]F(x)^4\). Cartier's identity \(y^{-j}=y^{-7j}F(x)^{2j}\) and the rule that it retains exponents congruent to \(6\pmod7\) give the untwisted coefficient matrix
\[
H_F=\operatorname{diag}(h,B),\qquad
B_{ij}=[x^{7(i+1)-(j+1)}]F(x)^4\quad(0\le i,j\le2).
\]
Here the actual Cartier matrix is obtained by taking entrywise seventh roots; the dual Hasse–Witt matrix is the transpose of the coefficient matrix in the compatible dual convention. Therefore their determinants have the same zero scheme after the stipulated coefficient normalization. The scalar coefficient is \([x^6]F^2=c_3^2+2c_4c_2+2c_1=h\).

3. The nonstandard polynomial step is the identity
\[
\det B=h\,\operatorname{Res}_x(F,F')=h\Delta(F)
\quad\text{in }\mathbb F_7[c_0,c_1,c_2,c_3,c_4].
\]
The sign is positive because the degree-five discriminant is \((-1)^{5\cdot4/2}\operatorname{Res}(F,F')=\operatorname{Res}(F,F')\). This identity is verified **as a polynomial in five indeterminates**, not by specializing them: `verify_symbolic.py` expands the nine specified coefficient expressions of \(F^4\), computes their determinant in the finite-field polynomial ring, independently computes the quintic discriminant by the symbolic resultant, and checks equality of all coefficients. There are 107 monomials in the determinant polynomial and 55 in the discriminant polynomial in the chosen monomial basis. The complete executable coefficient check is an exact finite algebraic identity certificate; it entails the identity over every characteristic-seven field. Multiplying by the scalar block proves \(\det H_F=h^2\Delta(F)\).

4. On the smooth locus \(\Delta\ne0\), the determinant is invertible exactly where \(h\ne0\), so those fibers are ordinary. On \(h=0\), the scalar block vanishes and the \(3\)-by-\(3\) block has determinant zero; consequently Cartier rank is at most two, \(a=4-\operatorname{rank}(\mathcal C)\ge2\), and the stable Frobenius rank is at most two. Invertibility and these rank inequalities are geometric statements over \(k\), not just rational-point computations.

5. The polynomial \(h=c_3^2+2c_4c_2+2c_1\) is linear in \(c_1\) with nonzero coefficient. Thus \(V(h)\) is an affine four-space as a scheme over \(k\); its intersection with \(U\) is smooth and irreducible. It is nonempty: \(F=x^5+1\) has \(h=0\) and \(\Delta=3\ne0\) in characteristic seven. Since \(\Delta\) is a unit on \(U\), the determinant cuts out exactly the doubled effective Cartier divisor \(2V(h)|_U\).

## Verification
Run `python3 verify_symbolic.py` with SymPy. It must print `UNIVERSAL_SYMBOLIC_IDENTITY_OK`. This checks the coefficient extraction, genus-four block determinant identity and a nonempty smooth nonordinary witness over the complete polynomial ring.

Run `python3 verify_primefield.py` with Python 3. It must print `EXHAUSTIVE_F7_INDEPENDENT_OK`. This second implementation performs its own modular polynomial multiplication and a Sylvester-matrix resultant, and tests all \(7^5=16807\) monic quintics over \(\mathbb F_7\). It finds 12,390 smooth ordinary, 2,016 smooth nonordinary and 2,401 singular coefficient tuples. This finite enumeration independently checks the algebra, but is not used as a proof for the algebraic closure or for parameter values in extension fields; the polynomial identity supplies that proof.

## Relationship to prior work
Kudo and Harashita's 2017 work (initially available on arXiv February 17, 2017) develops genus-four Hasse–Witt calculations and enumerates superspecial curves over small prime fields. Its stated results include restrictions on characteristic-seven superspecial curves, but do not supply the universal identity \(\det H_F=h(F)^2\Delta(F)\) for all separable monic quintics or the resulting doubled divisor. Achter and Howe explain the important distinction between Hasse–Witt and Cartier–Manin matrices; the proof fixes a specific coefficient convention and uses no unverified semilinear-power ordering.

Earlier calculations for selected one- and two-parameter quintic subfamilies display special instances of a squared Hasse factor. Such results do not imply the present identity throughout the full five-dimensional coefficient space. No uniqueness or priority theorem is deduced merely from database-search absence.

## Limitations
The nonordinary locus can contain subloci with further rank drop, which are not classified here. The coefficient scheme is not the coarse moduli space; the precise multiplicity statement refers to the specified family and Hasse–Witt determinant frame. This calculation does not determine full Newton polygons, geometrically distinct isomorphism classes, or isogeny decompositions. A specialized earlier treatment not recovered by available search remains a priority risk. No independent external audit has been performed.

## References
1. M. Kudo and S. Harashita, *Enumerating superspecial curves of genus 4 over prime fields*, arXiv:1702.05313, first posted 17 February 2017. https://arxiv.org/abs/1702.05313
2. J. D. Achter and E. W. Howe, *Hasse–Witt and Cartier–Manin matrices: A warning and a request*, arXiv:1710.10726, first posted 30 October 2017. https://arxiv.org/abs/1710.10726
3. M. Kudo and S. Harashita, *Superspecial curves of genus 4 in small characteristic*, arXiv:1607.01114, first posted 5 July 2016 (background on general genus-four Hasse–Witt computation). https://arxiv.org/abs/1607.01114
