# Universal 3-adic density for diagonal binary cubic quotient sets

## Finding

**Theorem.** For any two nonzero integers \(a,b\), put \(C_{a,b}(x,y)=ax^3+by^3\) and
\[
R_{\mathbb Z}(C_{a,b})=\left\{\frac{C_{a,b}(x,y)}{C_{a,b}(u,v)}:(x,y),(u,v)\in\mathbb Z^2,\ C_{a,b}(u,v)\ne0\right\}.
\]
Then \(R_{\mathbb Z}(C_{a,b})\) is dense in \(\mathbb Q_3\). More strongly, allowing variables in \(\mathbb Z_3\) gives the exact identity
\[
R_{\mathbb Z_3}(C_{a,b})=\mathbb Q_3.
\]
Consequently every integral diagonal cubic form in at least two variables, with at least two nonzero coefficients, has a quotient set dense in \(\mathbb Q_3\).

For example, the quotient sets associated with both \(x^3+3y^3\) and \(x^3+2y^3\) are dense in \(\mathbb Q_3\). These provide explicit boundary cases for the non-density alternatives asserted at the prime three in the cited 2021 and 2022 preprints.

## Assumptions and scope

All integer variables range over \(\mathbb Z\), not only strictly positive integers. Denominators must be nonzero. The prime is exactly \(3\); the theorem concerns diagonal cubic forms with two nonzero coefficients. The field \(\mathbb Q_3\), its integer ring \(\mathbb Z_3\), and its unit group \(U=\mathbb Z_3^{\times}\) have their usual meanings. An expression \(3^kU\) denotes elements of valuation exactly \(k\). No assertion is made about arbitrary binary cubics or other primes.

## Proof

**1. Cubic units and a surjection lemma.** A unit \(u\in U\) is a cube in \(U\) precisely when \(u\equiv1\) or \(-1\pmod9\). Necessity follows by cubing the six unit classes modulo nine. Conversely, if \(u\equiv1\pmod9\), write \(u=1+9w\). Expanding \((1+3t)^3=1+9(t+3t^2+3t^3)\), the polynomial \(t+3t^2+3t^3-w\) has derivative congruent to one modulo three and thus a root in \(\mathbb Z_3\) by Hensel's lemma. Apply a sign for \(u\equiv-1\pmod9\).

We shall repeatedly use the elementary consequence of Hensel's lemma: if \(f\in\mathbb Z_3[t]\) reduces modulo three to an affine function \(ct+d\), where \(c\) is a unit, then \(f(\mathbb Z_3)=\mathbb Z_3\). Indeed every target has a root in the appropriate residue class, and the derivative remains a unit there.

**2. Unequal coefficient valuations, reduced to a single factor of three.** Consider
\[
G(X,Y)=\alpha X^3+3\beta Y^3,\qquad\alpha,\beta\in U.
\]
We show that \(G(\mathbb Z_3^2)\) contains every unit. Fix \(w\in U\). Choose \(s\in\{1,-1\}\) with \(\alpha s\equiv w\pmod3\), and choose \(y\in\{0,1,-1\}\) with \(3\beta y^3\equiv w-\alpha s\pmod9\). Such a \(y\) exists since its three residues give all multiples of three modulo nine. Then
\[
\frac{w-3\beta y^3}{\alpha}\equiv s\pmod9,
\]
so the quotient is a unit cube by step 1. Some \(x\in U\) therefore satisfies \(G(x,y)=w\). Thus \(U\subseteq G(\mathbb Z_3^2)\). Also \(G(0,1)=3\beta\), so \(3U\subseteq R_{\mathbb Z_3}(G)\); because \(U\) consists of values, quotients of units give \(U\), while quotients of a unit by \(3\beta\) give \(3^{-1}U\). Homogeneity implies that if \(q\in R_{\mathbb Z_3}(G)\), then \(3^{3j}q\in R_{\mathbb Z_3}(G)\) for any integer \(j\): scale the numerator variables for positive \(j\), and the denominator variables for negative \(j\). The three valuation classes modulo three now give every nonzero \(3\)-adic number; zero is represented by the zero numerator. Hence \(R_{\mathbb Z_3}(G)=\mathbb Q_3\).

**3. Equal coefficient valuations.** Let
\[
H(X,Y)=\alpha X^3+\beta Y^3,\qquad\alpha,\beta\in U,
\]
and put \(\gamma=-\beta/\alpha\in U\).

If \(\gamma\) is a cube, take \(t\in U\) with \(t^3=\gamma\). Then \(H(t,1)=0\) and
\[
H(t+3s,1)=9\alpha t^2\left(s+3t^{-1}s^2+3t^{-2}s^3\right),\qquad s\in\mathbb Z_3.
\]
The parenthesized polynomial is \(s\) modulo three and has unit derivative; consequently \(9\mathbb Z_3\subseteq H(\mathbb Z_3^2)\). As \(H(3^k,0)=\alpha3^{3k}\), for any \(z\in\mathbb Q_3\) choose \(k\ge0\) large enough that \(z\alpha3^{3k}\in9\mathbb Z_3\). Represent this numerator by \(H\) and divide by \(H(3^k,0)\). This realizes \(z\) exactly as a quotient.

If \(\gamma\) is not a cube, take \(r\in\{1,-1\}\) with \(r\equiv\gamma\pmod3\). Then
\[
c_0=\frac{\alpha r^3+\beta}{3}\in U:
\]
if the numerator were divisible by nine, then \(\gamma\equiv r^3\equiv\pm1\pmod9\), contrary to step 1. Direct expansion gives
\[
\frac{H(r+3s,1)}3=c_0+3\alpha r^2s+9\alpha rs^2+9\alpha s^3.
\]
The polynomial divided by the leading factor three after subtracting \(c_0\) reduces to \(\alpha r^2s\pmod3\) and is therefore surjective on \(\mathbb Z_3\). Thus the values of \(H\) contain \(3(c_0+3\mathbb Z_3)\). As \(H\) is odd, they also contain \(3(-c_0+3\mathbb Z_3)\). The two sets together equal \(3U\), so \(3U\subseteq H(\mathbb Z_3^2)\). In addition, \(H(1,0)=\alpha\in U\), hence the ratio set contains \(3U\), \(U=(3U)/(3U)\), and \(3^{-1}U=\alpha/(3U)\). Cubic scaling as in step 2 yields every \(3^jU\), hence \(R_{\mathbb Z_3}(H)=\mathbb Q_3\).

**4. Arbitrary coefficients.** Interchange variables if necessary so that \(A=\nu_3(a)\le B=\nu_3(b)\). Write \(a=3^A\alpha\), \(b=3^B\beta\), \(\alpha,\beta\in U\), and \(B-A=3t+r\) with \(t\ge0\), \(r\in\{0,1,2\}\). For \(r=0\) or \(1\), restricting the original form to \(x=3^tX\) gives
\[
C_{a,b}(3^tX,Y)=3^{A+3t}\bigl(\alpha X^3+3^r\beta Y^3\bigr).
\]
The normalized form is handled by step 3 or step 2. For \(r=2\), instead restrict to \(x=3^{t+1}X\), obtaining
\[
C_{a,b}(3^{t+1}X,Y)=3^{A+3t+2}\bigl(3\alpha X^3+\beta Y^3\bigr),
\]
which is step 2 after swapping variables. A common nonzero scalar does not alter ratios, so the quotient set over \(\mathbb Z_3\) of the original form contains all of \(\mathbb Q_3\). The reverse containment is automatic.

**5. Passing from \(\mathbb Z_3\) to \(\mathbb Z\).** For any quotient of two \(\mathbb Z_3\)-valued inputs with nonzero denominator, approximate all four inputs by ordinary integers. Polynomial evaluation and division by a nonzero \(3\)-adic number are continuous. The corresponding integer-value quotients converge to the chosen quotient. Therefore \(R_{\mathbb Z}(C_{a,b})\) is dense in \(\mathbb Q_3\). Setting all but two variables to zero proves the asserted multivariable consequence. \(\square\)

## Verification

The standalone `verify.py` checks (i) the cube-unit residue criterion and surjective-unit construction modulo finite powers of three, (ii) both local equal-valuation alternatives, and (iii) the coefficient-normalization identities. These are consistency checks only. Steps 1--5 supply the infinite proof, including Hensel's lemma and continuity; finite rings by themselves cannot prove density.

## Relationship to prior work

Antony and Barman, *p-adic quotient sets: Cubic forms*, first publicly posted 11 October 2021, state in Theorem 1.2(3) that coefficient valuation differences nonzero modulo three force non-density; their Theorem 1.2(1) also gives a cubic-residue condition for unit coefficients. The explicit forms \(x^3+3y^3\) and \(x^3+2y^3\) respectively fall outside those asserted density cases, whereas the present proof establishes density for both and all other nonzero coefficient pairs. Antony, Barman, and Miska's subsequent diagonal-form preprint (12 January 2022) extends the stated conditions for general degrees. Miska, Murru, and Sanna's earlier unweighted sum-of-cubes density theorem does not supply the arbitrary-coefficient classification proved here. The comparison concerns the explicitly inspected preprints; journal-version changes or unindexed corrections cannot be ruled out.

## Limitations

This result addresses only \(p=3\), diagonal homogeneous cubics, and integer-coordinate quotient density. It does not claim that every element of \(\mathbb Q_3\) is exactly a quotient of *integer* values; exact surjectivity is proved only for \(\mathbb Z_3\) coordinates. The paper-priority comparison is bounded by accessible literature, especially the inspected preprint versions; independently checking final journal texts and any subsequent errata is advisable.

## References

1. D. Antony and R. Barman, *p-adic quotient sets: Cubic forms*, arXiv:2110.05420v2 (2021), Theorem 1.2, introduction and proof. https://arxiv.org/html/2110.05420v2
2. D. Antony, R. Barman and P. Miska, *p-adic quotient sets: diagonal forms*, arXiv:2201.04372v1 (2022), Theorem 1.1 and discussion of the cubic case. https://arxiv.org/abs/2201.04372
3. P. Miska, N. Murru and C. Sanna, *On the p-adic denseness of the quotient set of a polynomial image*, arXiv:1807.08947v2 (2018), section on sums of cubes. https://arxiv.org/html/1807.08947v2
4. D. Antony and R. Barman, *On p-adic denseness of quotients of values of integral forms*, arXiv:2308.08907 (2023), related subsequent investigation. https://arxiv.org/abs/2308.08907
