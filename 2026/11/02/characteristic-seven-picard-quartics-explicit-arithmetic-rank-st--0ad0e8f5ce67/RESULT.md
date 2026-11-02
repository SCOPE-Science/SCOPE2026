# Characteristic-seven Picard quartics: explicit arithmetic-rank strata

## Finding
Let \(k\) be algebraically closed of characteristic \(7\). For the smooth projective model of
\[
 C_{a,b,c}:\qquad y^3=x^4+a x^2+b x+c,\qquad (a,b,c)\in k^3,
\]
put
\[
\Delta=2a^4c+3a^3b^2-2a^2c^2-3ab^2c+b^4-3c^3.
\]
Exactly the triples with \(\Delta\ne0\) give smooth genus-three curves. On this smooth locus the Jacobian \(7\)-rank \(f_7\) and \(a\)-number (the dimension of the kernel of Cartier on regular differentials) satisfy the **complete marked-coefficient classification**
\[
 (f_7,a\text{-number})=
 \begin{cases}
 (3,0),&a\ne0,\\
 (0,2),&a=0\ \text{and}\ (c=0\ \text{or}\ b^4=4c^3),\\
 (1,2),&a=0,\ c\ne0,\ b^4\ne4c^3.
 \end{cases}
\]
Here the condition \(\Delta\ne0\) is imposed in every case. In particular the rank-zero locus has two explicit components inside the nonordinary divisor; no smooth member has \(7\)-rank two or \(a\)-number one or three. **Over \(\mathbb F_7\)**, the \(294\) smooth ordered coefficient triples have distributions \(252\) of type \((3,0)\), \(30\) of type \((1,2)\), and \(12\) of type \((0,2)\). These are counts of coefficient triples, not abstract isomorphism classes.

## Assumptions and scope
All coefficient and polynomial equalities below are interpreted in characteristic \(7\), with \(k\) algebraically closed unless counting \(\mathbb F_7\)-triples. The curve is the nonsingular projective completion of the affine superelliptic equation, not an arbitrary ternary quartic. Because \(3\) is coprime to \(7\), \(\gcd(3,4)=1\), and the quartic is squarefree precisely when \(\Delta\ne0\), its smooth model has genus \((3-1)(4-1)/2=3\). The theorem does not classify unmarked isomorphism classes or assert supersingularity from \(7\)-rank zero.

## Proof
Write \(F(x)=x^4+a x^2+b x+c\). Regular differentials have basis \(dx/y,\ dx/y^2,\ x\,dx/y^2\). Applying Cartier using \(x^i dx/y^j=x^i F(x)^{2j}dx/y^{7j}\), extracting exponents congruent to \(6\pmod 7\), and taking seventh roots gives the Cartier-semilinear matrix with columns representing the images of the ordered input basis,
\[
 H^{(1/7)},\qquad H=
 \begin{pmatrix}2a&0&0\\0&U&V\\0&W&Z\end{pmatrix},\quad
 \begin{aligned}
 U&=[x^6]F^4, &V&=[x^5]F^4,\\
 W&=[x^{13}]F^4,&Z&=[x^{12}]F^4.
 \end{aligned}
\]
Here \(H^{(1/7)}\) means entrywise seventh roots and the operator is seventh-root-semilinear. Direct multinomial expansion and polynomial reduction establish the **identities in the polynomial ring**
\[
 UZ-VW=5a\Delta,\qquad\det H=3a^2\Delta.
\]
Thus for \(a\ne0\), Cartier is bijective on the smooth locus. Its kernel is zero, and the stable Frobenius (equivalently Cartier) rank is three, so the invariant pair is \((3,0)\).

On \(a=0\), the middle block becomes
\[
 \begin{pmatrix}U&V\\W&Z\end{pmatrix}
 =\begin{pmatrix}5b^2c&5bc^2\\4b&4c\end{pmatrix}
 =\binom{3bc}{1}\begin{pmatrix}4b&4c\end{pmatrix}.
\]
For smooth members, \(\Delta=b^4-3c^3\ne0\) ensures \((b,c)\ne(0,0)\), so this block has rank exactly one, while the scalar block vanishes. Consequently Cartier has rank one and its kernel has dimension two: the \(a\)-number is two throughout the nonordinary divisor.

For the rank-one block \(uv\), repeated seventh-root-semilinear Cartier has stable rank one if and only if \(v^{(7)}u\ne0\): if this contraction vanishes the second iterate already vanishes on the block; otherwise every iterate has rank one. Explicitly,
\[
 v^{(7)}u=5b^8c+4c^7
 =5c(b^4-3c^3)(b^4-4c^3).
\]
After imposing smoothness \(b^4-3c^3\ne0\), the contraction vanishes precisely when \(c=0\) or \(b^4=4c^3\). Hence those curves have stable rank zero, and every remaining nonordinary curve has stable rank one. Since \(a=0\) also gives one identically zero block, the displayed classification follows.

For the finite-field census, the number of squarefree monic quartics over \(\mathbb F_7\) is \(7^4-7^3\). Translation of the variable \(x\) acts freely on their cubic coefficients because \(4\) is invertible, and gives a unique depressed quartic in each translation orbit. Therefore exactly \(7^3-7^2=294\) depressed quartics are squarefree. Of the \(49\) triples with \(a=0\), seven have \(b^4=3c^3\) and are singular: the pair \((0,0)\) plus six nonzero pairs (fourth powers and cubes in \(\mathbb F_7^*\) give these six pairs). Thus \(42\) are smooth. The condition \(c=0\) contributes six smooth rank-zero triples, and \(b^4=4c^3\), with \(c\ne0\), contributes six more; they are disjoint. The remaining \(30\) nonordinary triples have rank one, and the other \(294-42=252\) smooth triples are ordinary.

## Verification
Run `python3 verify_symbolic.py` with Python 3 and SymPy: it directly expands the coefficient matrix and discriminant in \(\mathbb F_7[a,b,c]\), verifies the determinant and stable-rank identities symbolically, and enumerates all \(343\) coefficient triples by polynomial gcd. Its completed output is `SYMBOLIC_VERIFY_OK {'singular': 49, (1, 2): 30, (0, 2): 12, (3, 0): 252}`.

Run `python3 verify_counts.py` with Python 3 and no third-party packages: this separately implements arithmetic in the fields \(\mathbb F_7,\mathbb F_{49},\mathbb F_{343}\), checks smoothness by polynomial gcd, counts points on all \(294\) smooth curves, reconstructs initial zeta numerator coefficients with Newton identities, and checks the \(7\)-ranks by reduction modulo seven. Its completed output begins `POINT_COUNTS_OK {1: 30, 0: 12, 3: 252}`. Finite point counts corroborate only the \(\mathbb F_7\) census; the polynomial proof establishes the geometric theorem.

## Relationship to prior work
Bouw–Koutsianas–Sijsling–Wewers give the Picard-curve normal form and study its discriminant and arithmetic models (arXiv:1902.09624, first publicly posted 2019-02-25). Özman–Pries–Weir study the cyclic-cover \(p\)-rank strata and establish **existence and dimensions** of rank-zero and rank-one strata for genus-three signature \((2,1)\) in characteristic congruent to one modulo three (arXiv:1907.05684, especially Lemma 5.7). Accordingly, the possible ranks and dimensions are **not claimed as new**. The result here is the explicit characteristic-seven equations for each marked-parameter stratum, the uniform \(a\)-number, and the complete \(\mathbb F_7\) coefficient census. Estrada-Sarlabous (1991) also treated Hasse–Witt criteria for Picard curves, and Kazemifard–Tafazolian (2015) studied particular Picard examples; their potential overlap is acknowledged.

## Limitations
No claim is made about geometric isomorphism-class counts, the full Ekedahl–Oort type, Newton polygon slopes, or supersingularity of rank-zero curves. A 1991 article on Picard-curve Hasse–Witt matrices could not be inspected beyond its abstract, so some explicit formulas might already be known. The marked coefficient census is new only to the extent it is not implied by unindexed earlier tabulations. The classification is restricted to the smooth coefficient-marked family.

## References
- I. Bouw, A. Koutsianas, J. Sijsling, S. Wewers, *Conductor and discriminant of Picard curves*, arXiv:1902.09624 (2019); doi:10.1112/jlms.12323.
- E. Özman, R. Pries, C. Weir, *The boundary of the p-rank 0 stratum of moduli space of cyclic covers*, arXiv:1907.05684 (2019), Lemma 5.7.
- J. Estrada-Sarlabous, *On the Jacobian varieties of Picard curves defined over fields of characteristic p > 0*, Mathematische Nachrichten 152 (1991), 329–340, doi:10.1002/mana.19911520125.
- A. Kazemifard, S. Tafazolian, *A note on some Picard curves over finite fields*, Finite Fields and Their Applications (2015), doi:10.1016/j.ffa.2014.12.002.
