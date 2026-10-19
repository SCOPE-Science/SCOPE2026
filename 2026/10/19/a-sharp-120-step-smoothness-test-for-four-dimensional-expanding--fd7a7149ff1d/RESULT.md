# A sharp 120-step smoothness test for four-dimensional expanding tori

## Finding

For an expanding integer matrix \(A\in M_4(\mathbb Z)\), define its **integer-spectrum exponent** by
\[
 n(A)=\min\{j\geq1:\text{every eigenvalue of }A^j\text{ is an integer}\},
\]
when this set is nonempty. Repeated eigenvalues and nondiagonalizable matrices are allowed in this definition. Then the complete set of attainable indices is
\[
 \boxed{\mathcal H_4=\{1,2,3,4,5,6,8,10,12\}.}
\]
Each index is attained by an expanding **diagonalizable** integer matrix of size four. In particular, \(n(A)\) exists precisely when all eigenvalues of \(A^{120}\) are integers. The number \(120\) is the **least** positive integer with this universal property.

Combining the result with the smooth Markov-partition criterion of Hughes and de Jong [1, Theorem 1.2] gives an effective, sharp single-power test:

> An expanding endomorphism of \(\mathbb T^4\) induced by \(A\in M_4(\mathbb Z)\) has a Markov partition with finitely piecewise-\(C^1\) boundary if and only if \(A^{120}\) is diagonalizable over \(\mathbb C\) and every eigenvalue of \(A^{120}\) belongs to \(\mathbb Z\).

For every smaller positive universal exponent there is an expanding diagonalizable counterexample. In particular, the exponent \(120\) cannot be decreased by assuming diagonalizability.

## Assumptions and scope

Throughout, *expanding* means that the complex eigenvalues of the integer matrix have modulus strictly greater than one. An integer-spectrum power need not be diagonalizable. Integer-spectrum exponents are defined only when at least one such power exists. A matrix has a smooth Markov partition in the precise finite-cover and finite-piecewise-\(C^1\)-hypersurface sense of [1]; that external criterion is used only for the stated dynamical equivalence, not in the arithmetic classification.

For a nonzero algebraic integer \(\alpha\) with a positive power in \(\mathbb Z\), define \(e(\alpha)\) as the least such exponent. The set of all exponents with \(\alpha^j\in\mathbb Z\) is exactly \(e(\alpha)\mathbb N\). Indeed, if \(\alpha^j\) and \(\alpha^k\) are nonzero rational integers, Bézout's identity makes \(\alpha^{\gcd(j,k)}\) rational; as an algebraic integer it must be in \(\mathbb Z\). Consequently, for a characteristic polynomial split into distinct monic irreducible factors, \(n(A)\) is the least common multiple of their respective \(e\)-values; repetitions do not matter.

## Proof

**1. Conjugate moduli and the low-degree cases.** If \(\alpha^j=m\in\mathbb Z\setminus\{0\}\), every Galois conjugate \(\alpha'\) satisfies \((\alpha')^j=m\). Thus all conjugates have one common modulus, \(r=|m|^{1/j}\), and their ratios are roots of unity.

An irreducible linear factor contributes exponent \(1\). For an irreducible cubic, there is exactly one real conjugate \(\pm r\): three distinct real conjugates could take only the two values \(\pm r\). The nonreal pair has product \(r^2\), so the integer norm of the cubic root equals \(\pm r^3\). Consequently the real root has integral cube, and conjugacy makes every root's cube the same integer. Its minimal exponent is exactly \(3\), since an irreducible cubic cannot contain an algebraic number with a rational first or second power.

For an irreducible quadratic the possible exponents are \(2,3,4,6\). One way to establish this is to write a nonreal root as \(\sqrt q\,\zeta_m\), with \(q\in\mathbb N\) the norm and \(\zeta_m\) a primitive root of unity. If \(q\) is a square, then \(\varphi(m)=2\), so \(m\in\{3,4,6\}\). If \(q\) is nonsquare, its compositum with \(\mathbb Q(\zeta_m)\) has degree \(\varphi(m)\) or \(2\varphi(m)\), and the stabilizer of \(\sqrt q\,\zeta_m\) has size at most two. Degree two therefore forces \(\varphi(m)\leq4\). In the degree-four cyclotomic cases, the necessary nontrivial stabilizer occurs only for \(m=8\) or \(m=12\), and produces exponents \(4\) and \(6\); the degree-two cyclotomic cases contribute \(2\) or \(3\). Real quadratic conjugates must be \(\pm r\), giving exponent \(2\). This also agrees with the complete dimension-two index classification proved in [1, Section 5.2].

**2. Quartics with an even minimal polynomial.** Let \(f\in\mathbb Z[X]\) be an irreducible quartic whose roots have integral powers. Set \(q=r^2\). Since complex conjugation takes each root \(\alpha\) to \(q/\alpha\), the root set is invariant under the involution \(\alpha\mapsto q/\alpha\). Comparing coefficients in the reciprocal polynomial shows that if the cubic coefficient of \(f\) vanishes, then its linear coefficient also vanishes. Hence \(f(X)=X^4+bX^2+d\) is even. (If \(f\) has a real root, its four distinct roots of modulus \(r\) must contain both \(r\) and \(-r\), making \(f\) even by irreducibility.)

Write \(\beta=\alpha^2\). Because \(f\) is irreducible of degree four, \(\beta\) has degree two. Also every exponent making \(\alpha\) an integer must be even: the conjugate \(-\alpha\) would give opposite integers for an odd exponent, contrary to Galois invariance of rational integers. Therefore \(e(\alpha)=2e(\beta)\), giving
\[
 \boxed{e(\alpha)\in\{4,6,8,12\}}\qquad(f\text{ even}).
\]

**3. Quartics whose cubic coefficient is nonzero.** Such a quartic has no real roots, so its roots form two complex-conjugate pairs. Let its coefficients be
\[
 f(X)=X^4+aX^3+bX^2+cX+d,\qquad a\neq0.
\]
All four roots have modulus \(r\); hence \(d=r^4=q^2\), and reciprocal symmetry yields \(c=qa\). Thus \(q=c/a\) is rational. Since \(q>0\) and \(q^2=d\in\mathbb Z\), it follows that \(q\in\mathbb N\). Each root is therefore \(\alpha=\sqrt q\,\zeta_m\) for a root of unity of some primitive order \(m\): indeed \((\alpha/\sqrt q)^j=\pm1\) whenever \(\alpha^j\in\mathbb Z\).

Put \(F=\mathbb Q(\zeta_m)\), \(K=\mathbb Q(\sqrt q)\), and \(E=FK\). The Galois stabilizer of \(\alpha\) in \(E/\mathbb Q\) has size at most two. To fix \(\sqrt q\,\zeta_m\), the root of unity must be sent to either \(\zeta_m\) or \(-\zeta_m\); there is at most one automorphism inducing each option. Since \([\mathbb Q(\alpha):\mathbb Q]=4\) and \([E:\mathbb Q]\) is \(\varphi(m)\) or \(2\varphi(m)\), necessarily
\[
 \varphi(m)\in\{2,4,8\}.
\]
Using \(\varphi(p^j)=p^{j-1}(p-1)\) and multiplicativity (so the following are complete finite lists), the respective lists of orders are
\[
 \begin{split}
 \varphi(m)=2 &: m\in\{3,4,6\},\\
 \varphi(m)=4 &: m\in\{5,8,10,12\},\\
 \varphi(m)=8 &: m\in\{15,16,20,24,30\}.
 \end{split}
\]
If \(q\) is a square, the minimal exponent is \(m/\gcd(2,m)\); if \(q\) is nonsquare, it is \(\operatorname{lcm}(2,m/\gcd(2,m))\). For the first two lists the possible values are therefore contained in \(\{2,3,4,5,6,10\}\).

The \(\varphi(m)=8\) case needs care: degree four forces \(K\subseteq F\) and a nontrivial stabilizer. The latter must send \(\zeta_m\mapsto-\zeta_m\) and \(\sqrt q\mapsto-\sqrt q\). It exists only when \(m\) is divisible by four, leaving \(m=16,20,24\). For \(m=16\), its candidate action \(\zeta_{16}\mapsto\zeta_{16}^{9}\) fixes the unique real quadratic subfield \(\mathbb Q(\sqrt2)\). For \(m=20\), \(\zeta_{20}\mapsto\zeta_{20}^{11}\) fixes the unique real quadratic subfield \(\mathbb Q(\sqrt5)\). Neither can flip \(\sqrt q\). For \(m=24\), the candidate \(\zeta_{24}\mapsto\zeta_{24}^{13}\) can flip \(\sqrt2\) or \(\sqrt6\); its only possible exponent is
\[
 \operatorname{lcm}(2,24/2)=12.
\]
Thus every irreducible quartic contributes an exponent belonging to
\[
 \boxed{\{2,3,4,5,6,8,10,12\}}.
\]
The slightly larger displayed superset does not affect the final classification; the witnesses below establish which indices actually occur.

**4. Assemble dimensions at most four.** A factorization of a monic degree-four polynomial into irreducibles has partitions \(4\), \(3+1\), \(2+2\), \(2+1+1\), or \(1+1+1+1\). Cubic factors supply only exponent \(3\), quadratic factors only \(\{2,3,4,6\}\), and two quadratics can have least common multiple at most among \(\{2,3,4,6,12\}\). Combining with step 3 and the linear factors gives
\[
 n(A)\in\{1,2,3,4,5,6,8,10,12\}.
\]

**5. Sharp witnesses.** Denote by \(C(f)\) the integer companion matrix of a monic integer polynomial \(f\). For indices \(2,3,4,6\), use \(C(f_j)\oplus 2I_2\), with
\[
 \begin{array}{ll}
 f_2=X^2-2,& f_3=X^2-2X+4,\\
 f_4=X^2-2X+2,& f_6=X^2-3X+3.
 \end{array}
\]
For index \(1\), use \(2I_4\). For indices \(5,8,10,12\), use the companion matrices of
\[
 \begin{aligned}
 f_5&=X^4+2X^3+4X^2+8X+16,\\
 f_8&=X^4+2X^2+2,\\
 f_{10}&=X^4-5X^3+15X^2-25X+25,\\
 f_{12}&=X^4-3X^2+3.
 \end{aligned}
\]
The roots of \(f_5\) are \(2\) times primitive fifth roots of unity. The roots of \(f_8\) satisfy \(\alpha^8=-4\), while \(\alpha^4\notin\mathbb Z\); the polynomial is irreducible by Eisenstein's criterion at \(2\). The polynomial \(f_{10}\) is the irreducible minimal polynomial of \(\sqrt5\,e^{2\pi i/5}\); its root's tenth power is \(3125\), while the fifth power is \(25\sqrt5\notin\mathbb Z\). Irreducibility follows because the four Galois conjugates are distinct: fixing \(\sqrt5\,\zeta_5\) would require an automorphism to send \(\zeta_5\) to itself or its negative, but \(-\zeta_5\) is not a fifth root. The polynomial \(f_{12}\) is irreducible by Eisenstein at \(3\); its roots satisfy \(\alpha^{12}=-27\), and their sixth powers are nonreal. In every example, all eigenvalues have modulus greater than one and all companion blocks are separable, hence the matrices are expanding and diagonalizable. Direct exact polynomial-remainder calculations for all the displayed witnesses are supplied in `verify.py`.

These examples complete the equality for \(\mathcal H_4\). Their indices have least common multiple
\[
 \operatorname{lcm}(1,2,3,4,5,6,8,10,12)=120.
\]
By the exponent-divisibility lemma, every integer-spectrum matrix has integer eigenvalues at exponent \(120\), and every smaller positive candidate universal exponent fails for at least one of the displayed expanding examples. Since a nonzero-eigenvalue Jordan block remains nondiagonalizable under every positive power, the same \(120\) is the sharp single-power exponent for the smooth-Markov criterion in [1]. \(\square\)

## Verification

Run `python3 verify.py` with Python 3.8 or later. The script performs exact integer-polynomial remainders, tests the minimal integer-spectrum exponent of every displayed witness, checks that each divides \(120\), and enumerates small Euler-totient preimages needed in the cyclotomic case distinction. The script has no third-party dependencies. It is a finite consistency check; the unbounded classification relies on the preceding proof, not on finite enumeration.

## Relationship to prior work

Hughes and de Jong [1] prove the smooth-Markov-partition criterion, establish finiteness of the set of integer-spectrum indices in each dimension, and compute the complete two-dimensional set \(\{1,2,3,4,6\}\), with universal exponent \(12\). Their relevant Section 5.2 stops at dimension two; neither the four-dimensional index set nor the sharp \(120\)-power criterion is stated there. The present claim starts with their criterion and adds an exact four-dimensional arithmetic classification and optimal finite test.

Classical cyclotomic and binomial-irreducibility theory supplies background for root-of-unity and field-degree arguments; these general tools are not asserted as new. Dilcher–Noble–Smyth [2, Theorem 3 and Corollary 6] characterize irreducible polynomials with a root of rational complex modulus and derive reciprocal-root symmetry; their Lemma 2 records the well-known even-polynomial consequence of opposite conjugates. These structural precursor facts are acknowledged. They do not state the present root-of-an-integer-power restriction, complete degree-four index set, or optimal Markov single-power test. Koley–Reddy [3] gives an elementary proof of Capelli's binomial irreducibility criterion, which is background to the witness constructions rather than an independent computation of this spectrum.

## Limitations

This theorem does not classify the geometry, size, or number of Markov rectangles; it tests existence under the smoothness criterion in [1]. It applies to dimension four and expanding integer matrices. Replacing the semisimplicity hypothesis by integer eigenvalues alone would be false for nondiagonalizable matrices. The theorem is analytically proved subject to the correctness of the external smoothness criterion; no independent refereeing or exhaustive priority certification is claimed. A general higher-dimensional exact exponent formula is not established.

## References

[1] C. Hughes and H. de Jong, *Smoothness of Markov Partitions for Expanding Toral Endomorphisms*, arXiv:2604.00257v2 (2026), especially Theorem 1.2 and Section 5.2. Earliest public version: 31 March 2026. https://arxiv.org/html/2604.00257v2

[2] K. Dilcher, R. Noble, and C. Smyth, *Minimal polynomials of algebraic numbers with rational parameters*, Acta Arithmetica 148 (2011), 281–308. DOI:10.4064/aa148-3-5.

[3] B. Koley and A. S. Reddy, *Irreducibility of \(X^n-a\)*, arXiv:2006.03787 (2020), general binomial-irreducibility context.
