# All singular three-by-three minors of prime-square Fourier matrices
## Finding
For every odd prime \(p\), set \(N=p^2\) and write the order-\(N\) Fourier matrix as
\[
F_N=(\zeta^{{rc}})_{{r,c\in\mathbb Z_N}},\qquad \zeta=e^{{2\pi i/N}}.
\]
For a three-element subset of \(\mathbb Z_N\), record how many elements lie in each residue class modulo \(p\). Call the subset type A, B, or C according as the nonzero occupancy pattern is \(1+1+1\), \(2+1\), or \(3\).

For every three-element row set \(R\) and every three-element column set \(C\),
\[
\det F_N[R,C]=0
\]
if and only if one of \(R,C\) is type C and the other is type B or C. More precisely, the rank is \(1\) exactly for type pair \((C,C)\), rank \(2\) exactly for \((C,B)\) and \((B,C)\), and rank \(3\) for all remaining type pairs.

Let
\[
B=\frac{{p^3(p-1)^2}}2,\qquad C_3=\frac{{p^2(p-1)(p-2)}}6
\]
be the numbers of type-B and type-C three-subsets. Hence the total number of singular three-by-three minors, indexed by an unordered row set and an unordered column set, is
\[
2BC_3+C_3^2=\frac{{p^4(p-1)^2(p-2)(6p^2-5p-2)}}{{36}}.
\]
The rank-one and rank-two counts are respectively
\[
C_3^2=\frac{{p^4(p-1)^2(p-2)^2}}{{36}},\qquad
2BC_3=\frac{{p^5(p-1)^3(p-2)}}6.
\]

## Assumptions and scope
The claim concerns the ordinary complex Fourier matrix of the cyclic group \(\mathbb Z_{{p^2}}\), with \(p\) an odd prime. Row and column index sets contain three distinct elements. The classification is invariant under translating either index set, and under multiplying row or column indices by a unit modulo \(p^2\).

The statement is about all three-by-three minors, not only principal minors and not merely whether a chosen three-row harmonic frame is full spark.

## Proof
If a three-set is type A, then it meets each residue class modulo \(p\) in at most one point. For a three-set this is exactly the uniform-distribution condition over the divisors of \(p^2\) appearing in Alexeev--Cahill--Mixon, Theorem 9. Their prime-power full-spark criterion therefore implies that every three-by-three minor using a type-A row set is nonsingular. Since the Fourier matrix is symmetric, the same holds if the column set is type A.

It remains to analyze type B and type C. Suppose first that the column set is type B. Translating columns and multiplying rows by nonzero phases do not change rank, so write
\[
C=\{0,pa,b\},
\]
where \(p\nmid a\) and \(p\nmid b\). For a row index \(t\), put
\[
u_t=\zeta^{{pat}},\qquad v_t=\zeta^{{bt}}.
\]
The row of the selected minor indexed by \(t\) is \((1,u_t,v_t)\).

If the row set is also type B, label its elements so that \(t_1\equiv t_2\pmod p\) and \(t_3\not\equiv t_1\pmod p\). Then \(u_1=u_2\), while \(v_1\ne v_2\) because \(b\) is a unit modulo \(p\) and \(t_2-t_1\) is a nonzero multiple of \(p\) modulo \(p^2\). Also \(u_3\ne u_1\). Subtracting the first selected row from the second gives, up to sign,
\[
\det F_N[R,C]=(v_2-v_1)(u_3-u_1),
\]
which is nonzero. Thus type \((B,B)\) has rank \(3\).

If the row set is type C, all three row indices are congruent modulo \(p\), so all three values \(u_t\) are equal. The first two columns are therefore proportional and the determinant vanishes. The three values \(v_t\) are distinct because \(b\) is a unit modulo \(p^2\) on the differences between the three distinct lifts in one residue class. Hence the rank is exactly \(2\). By symmetry the same conclusion holds for type \((B,C)\).

Finally suppose both sets are type C. Write
\[
R=\{r_0+pb_j:1\le j\le3\},\qquad C=\{c_0+pa_i:1\le i\le3\}.
\]
Then
\[
\zeta^{{(r_0+pb_j)(c_0+pa_i)}}
=\zeta^{{r_0c_0}}(\zeta^p)^{{r_0a_i}}(\zeta^p)^{{c_0b_j}},
\]
because the remaining factor is \(\zeta^{{p^2a_ib_j}}=1\). Thus the selected matrix is an outer product after a common scalar, and its rank is exactly \(1\).

The only remaining type pairs contain type A and are nonsingular by the full-spark criterion. This proves the rank classification.

For the count, a type-C set is obtained by choosing one residue class modulo \(p\) and then three of its \(p\) lifts, giving
\[
C_3=p\binom p3=\frac{{p^2(p-1)(p-2)}}6.
\]
A type-B set is obtained by choosing the repeated residue, two lifts there, a different singleton residue, and one lift there, giving
\[
B=p\binom p2(p-1)p=\frac{{p^3(p-1)^2}}2.
\]
The singular ordered pairs of unordered row and column sets are exactly \((C,B)\), \((B,C)\), and \((C,C)\), which gives the stated formulas.

## Verification
The proof is symbolic and applies to every odd prime. The accompanying verifier independently performs exact cyclotomic determinant calculations for every translation-normalized three-row and three-column pair for \(p=3\) and \(p=5\). A translation-normalized set contains \(0\); every translation orbit has such a representative, and zero/nonzero determinant and rank are translation invariant.

The verifier reduces powers of a primitive \(p^2\)-th root using
\[
\Phi_{{p^2}}(X)=1+X^p+X^{{2p}}+\cdots+X^{{(p-1)p}},
\]
uses no floating-point tolerances, checks the predicted rank for every tested pair, and separately checks the closed-form counts of type-B and type-C subsets. Its successful terminal marker is `VERIFY_OK`.

## Relationship to prior work
Alexeev, Cahill, and Mixon prove that, for prime-power order, a selected set of Fourier rows is full spark exactly when the row indices are uniformly distributed over the divisors. For three rows at order \(p^2\), this settles the type-A case, because type A is uniformly distributed, but it does not classify which individual minors vanish when the chosen row set is not full spark. The present result resolves that missing local question for every pair of three-row and three-column sets and additionally gives the exact ranks and counts of all singular minors.

Krahmer, Pfander, and Rashkov develop finite-Abelian uncertainty principles and use Fourier-minor information in support-size questions; Meshulam gives a general divisor-interpolation uncertainty bound. Those results provide the surrounding uncertainty framework but do not imply the residue-pattern rank census above.

## Limitations
The theorem is restricted to three-by-three minors and modulus equal to the square of an odd prime. It does not classify larger minors, higher prime powers, or arbitrary composite moduli. The literature search did not locate an equivalent rank-and-count theorem, but older generalized-Vandermonde or harmonic-frame literature could contain a differently phrased equivalent statement; this is the main residual originality risk.

## References
1. Boris Alexeev, Jameson Cahill, Dustin G. Mixon, *Full Spark Frames*, arXiv:1110.3548, first submitted 2011-10-17. Theorem 9 gives the prime-power full-spark criterion.
2. Felix Krahmer, Götz E. Pfander, Peter Rashkov, *Uncertainty in time--frequency representations on finite Abelian groups and applications*, arXiv:math/0611493, first submitted 2006-11-16.
3. Roy Meshulam, *An uncertainty inequality for finite abelian groups*, arXiv:math/0312407, first submitted 2003-12-22.
