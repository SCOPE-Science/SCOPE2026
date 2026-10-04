# Principal nonsingularity of the order-\(154\) Fourier matrix
## Finding
Every principal minor of the complex Fourier matrix \(\mathcal F_{154}=(\omega_{154}^{jk})_{0\le j,k<154}\) is nonzero.

## Assumptions and scope
The Fourier matrix is indexed by \(\mathbb Z/154\mathbb Z\), with \(\omega_{154}\) any primitive \(154\)-th root of unity. Multiplying the exponent by a unit or replacing \(\omega_{154}\) by its inverse does not affect the nonvanishing conclusion. The proof uses the square-free lifting theorem of Caragea, Lee, Malikiosis, and Pfander with \(154=11\cdot14\).

## Proof
Caragea--Lee--Malikiosis--Pfander prove the following lifting statement: if \(N=pN'\) is square-free and all principal minors of \(\mathcal F_{N'}\) are nonzero in characteristic \(p\), then every \(N'\)-principal minor, hence every ordinary principal minor, of \(\mathcal F_N\) is nonzero.

It therefore suffices to verify the characteristic-
\(11\) hypothesis for \(N'=14\). Work in
\[
K=\mathbb F_{11}[a]/(a^3+a+4).
\]
The cubic \(X^3+X+4\) has no root in \(\mathbb F_{11}\), hence is irreducible. The class \(a\) has multiplicative order \(1330=11^3-1\): the exact checker verifies \(a^{1330}=1\) and, for the prime divisors \(2,5,7,19\) of \(1330\), verifies \(a^{1330/q}\ne1\). Thus \(\zeta=a^{95}\) has order \(14\).

There are two Frobenius orbits of primitive \(14\)-th roots in \(K\), represented by \(\zeta\) and \(\zeta^3\): multiplication of exponents by \(11\) gives the orbits \(\{1,11,9\}\) and \(\{3,5,13\}\) modulo \(14\). For each representative, the checker forms \(\overline{\mathcal F}_{14}=(\zeta^{ij})_{0\le i,j<14}\) and evaluates all \(2^{14}-1=16383\) nonempty principal determinants by exact finite-field Gaussian elimination. All determinants are nonzero for both orbit representatives. Frobenius preserves zero versus nonzero, so every primitive \(14\)-th-root realization is covered.

The lifting theorem now applies with \(p=11\) and \(N'=14\), proving that every principal minor of \(\mathcal F_{154}\) is nonzero.

## Verification
Run `python3 verify_154.py`. The verifier uses only Python's standard library and integer arithmetic modulo \(11\). It reconstructs the field, checks irreducibility and the orders of \(a\) and \(\zeta\), checks representatives of both Frobenius orbits of primitive \(14\)-th roots, and exhaustively evaluates \(32766\) nonempty principal determinants in total. The replay packaged with this finding returned `VERIFY_OK`, with zero determinants in every size \(1,\ldots,14\) for both orbit representatives.

## Relationship to prior work
Tao's prime-order uncertainty principle is an early source for the Fourier-minor viewpoint. Caragea and Lee later proved square-free equivalences for principal minors of sizes two and three and conjectured full principal nonsingularity for square-free order. Caragea--Lee--Malikiosis--Pfander supplied the finite-characteristic lifting theorem used here. Their explicit sufficient-growth theorem does not cover \(154=2\cdot7\cdot11\): at the second extension it would require \(11>7^{21}\). Gu--Zhou--Wang used the lifting method to settle orders \(70\) and \(143\) by separate finite-field certificates. Targeted searches of the inspected literature and public result indexes did not locate the order-
\(154\) statement or the needed characteristic-
\(11\), order-
\(14\) certificate. This is evidence for originality, not an absolute priority guarantee.

## Limitations
The argument depends on the published square-free lifting theorem and on a finite exhaustive computation, not on a new general symbolic criterion for all square-free orders. The computation checks principal minors only, exactly as required by the lifting hypothesis; it does not claim that all non-principal minors of \(\mathcal F_{154}\) are nonzero. The full text of arXiv:2608.17746 was not inspected here; its title and abstract state results for orders \(70\) and \(143\), and no implication to order \(154\) was found.

## References
1. T. Tao, *An uncertainty principle for cyclic groups of prime order*, arXiv:math/0308286, first posted 2003-08-29.
2. A. Caragea and D. G. Lee, *On the principal minors of Fourier matrices*, arXiv:2409.09793.
3. A. Caragea, D. G. Lee, R. Malikiosis, and G. E. Pfander, *Principal minors of Fourier matrices of square-free order*, arXiv:2505.24326.
4. J. Gu, L. Zhou, and Y. Wang, *Principal nonsingularity of the Fourier matrices of orders \(70\) and \(143\)*, arXiv:2608.17746.
