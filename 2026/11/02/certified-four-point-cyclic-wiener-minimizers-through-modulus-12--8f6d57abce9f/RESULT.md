# Certified four-point cyclic Wiener minimizers through modulus 128

## Finding
For each integer \(8\le N\le128\), let \(G_N=\mathbb Z/N\mathbb Z\) and let \(A\subset G_N\) have exactly four elements. Define the unnormalized nonconstant-frequency Wiener mass
\[
D_N(A)=\sum_{k=1}^{N-1}\left|\sum_{a\in A}\exp(-2\pi i k a/N)\right|.
\]
The following is a **complete, rigorously certified finite-modulus classification** of every global minimizer.

1. When \(4\mid N\), \(A\) minimizes \(D_N\) exactly when \(A\) is a coset of the subgroup of order four. The minimum is \(N-4\).
2. When \(N=2q\) with \(q\) odd, \(A\) minimizes \(D_N\) exactly when it is a translate of \(\{0,d,q,q+d\}\) for an integer \(1\le d<q\) with \(\gcd(d,q)=1\). Its minimum is
\[
4\left(\csc\frac{\pi}{2q}-1\right).
\]
3. When \(N\) is odd, \(A\) minimizes \(D_N\) exactly when it is an invertible affine image of \(\{0,1,2,3\}\): namely \(A=\{a,a+d,a+2d,a+3d\}\), \(\gcd(d,N)=1\). Its minimum is
\[
\sum_{k=1}^{N-1}\left|\frac{\sin(4\pi k/N)}{\sin(\pi k/N)}\right|.
\]

The first family also follows from a previously known subgroup-coset theorem. The **new finite classifications** are the second and third families across all eligible moduli through 128. The assertions for moduli exceeding 128 are **not claimed**. Among the \(10{,}667{,}965\) anchored four-element sets examined, \(7{,}481\) are classified minimizers, and every one of the other \(10{,}660{,}484\) is separated from the minimum by a rigorously positive gap; a uniform certified bound over all moduli is greater than \(0.10997296\) in the normalization above.

## Assumptions and scope
The group has its ordinary cyclic addition and the characters \(a\mapsto\exp(-2\pi i ka/N)\). Zero frequency is excluded from \(D_N\); including it would add exactly four to every objective, leaving the minimizing sets unchanged. All sets have four **distinct** elements. The endpoint \(N=128\) is included; the claim is finite and does not depend on extrapolation.

Translation multiplies every Fourier coefficient by a unimodular factor and therefore leaves \(D_N\) invariant. Multiplication of all elements by a unit modulo \(N\) permutes the nonzero Fourier frequencies, again preserving \(D_N\). In particular, it suffices to certify four-subsets containing zero and to compare each with one canonical candidate for its residue class.

## Proof
**Candidate symmetry and values.** If \(4\mid N\), the unique four-element subgroup consists of \(0,N/4,N/2,3N/4\). Its nonzero-frequency transform takes value four at exactly \(N/4-1\) frequencies and zero elsewhere, giving \(D_N=N-4\). This case is also implied by the general subgroup-coset equality criterion in the references.

If \(N=2q\) with \(q\) odd, put \(B=\{0,1,q,q+1\}\). For odd frequencies the two terms separated by \(q\) cancel, while for \(k=2j\) the Fourier transform is \(2(1+\exp(-2\pi i j/q))\). Thus its norm is \(4\sum_{j=1}^{q-1}|\cos(\pi j/q)|=4(\csc(\pi/(2q))-1)\). Every \(\{0,d,q,q+d\}\) with \(\gcd(d,q)=1\) is the image of \(B\) under a multiplication by an odd unit modulo \(2q\) (choose the odd representative of \(d\bmod q\)); its translations share the same norm.

If \(N\) is odd, all invertible affine images of \(\{0,1,2,3\}\) have the same mass, with the stated geometric-series formula.

**Rational-enclosure lemma.** Put \(Q=10^8\). For each \(N\le128\) and \(j\in\{0,\ldots,N-1\}\), the supplied program `CHECK.py` constructs integers \(c_j,s_j\) satisfying
\[
\left|c_j/Q-\cos(2\pi j/N)\right|<1/Q,\qquad
\left|s_j/Q-\sin(2\pi j/N)\right|<1/Q.
\]
To justify this *without floating-point assumptions*, use Machin's exact identity \(\pi=16\arctan(1/5)-4\arctan(1/239)\); truncate each alternating arctangent series at twenty terms, bounding the total error by
\[
\varepsilon_\pi=\frac{16}{41\cdot5^{41}}+\frac4{41\cdot239^{41}}.
\]
For arguments in \([0,4]\), Taylor polynomials through degrees 38 (cosine) and 39 (sine) have error at most \(4^{40}/40!\) by Taylor's theorem. The argument error induced by \(\pi\)'s approximation is less than \(2\varepsilon_\pi\). The exact rational assertion
\[
2\varepsilon_\pi+\frac{4^{40}}{40!}<\frac1{2Q}
\]
is satisfied. Rational nearest-integer rounding adds at most \(1/(2Q)\). Reflection around the full circle and exact values at zero and the half-turn complete the table. Every bound here can be checked by rational arithmetic alone.

For \(A=\{a_1,a_2,a_3,a_4\}\) and \(1\le k<N\), form the integers
\[
X_{A,k}=\sum_{a\in A}c_{ka\bmod N},\quad
Y_{A,k}=\sum_{a\in A}s_{ka\bmod N},\quad
w_{A,k}=\left\lfloor\sqrt{X_{A,k}^2+Y_{A,k}^2}\right\rfloor,
\]
and \(W_N(A)=\sum_{k=1}^{N-1}w_{A,k}\). Each complex Fourier coefficient differs from \((X_{A,k}-iY_{A,k})/Q\) by less than \(4\sqrt2/Q<6/Q\), and integer-square-root flooring costs less than \(1/Q\). Consequently,
\[
\frac{W_N(A)-6(N-1)}{Q}<D_N(A)<\frac{W_N(A)+7(N-1)}{Q}.
\]
The integer roots are certified by the *exact* inequalities \(w^2\le X^2+Y^2<(w+1)^2\). Floating-point square root is used solely as a guess and is adjusted until both integer inequalities hold. All intermediate squared coordinate sums are below \(32Q^2<2^{63}\), so signed 64-bit arithmetic is exact. Table construction and bounds are part of the standalone program.

**Exhaustive separation certificate.** Each translated four-set contains zero, so enumerate every \(A=\{0,a,b,c\}\) with \(1\le a<b<c<N\). The program constructs the exact predicted candidate set \(\mathcal C_N\) for each modulus, computes \(W_N(C_N)\) for one canonical candidate, and verifies by integer arithmetic that
\[
W_N(A)-W_N(C_N)>13(N-1)
\]
for **every** anchored \(A\notin\mathcal C_N\). This inequality, together with the two rigorous enclosures, gives \(D_N(A)>D_N(C_N)\). For candidate sets, the translation/unit symmetries prove equal real objectives, irrespective of rounding of individual table entries.

The four attached certificates cover the disjoint exhaustive ranges \([8,96]\), \([97,112]\), \([113,120]\), and \([121,128]\). They report \(121\) distinct moduli, \(10{,}667{,}965\) anchored sets, \(7{,}481\) predicted minimizers and \(10{,}660{,}484\) rejected competitors. Every noncandidate passes the strict integer inequality. The smallest certified mass-gap bound, calculated before decimal display as an exact rational, is \(0.10997296\), at \(N=123\). This establishes the claimed finite range and exactly the prescribed equality families. \(\square\)

## Verification
The package contains standalone `CHECK.py`, four machine-readable `CERT_*.json` files recording each modulus and its closest competing configuration, and a `requirements.txt` specifying NumPy. Run the checker separately on the four nonoverlapping intervals with commands of the form `python CHECK.py 8 96 CERT_8_96.json` (similarly for `97 112`, `113 120`, and `121 128`). Each command regenerates its certificate from the mathematical definitions. Outputs are strict integer comparisons and exact-rational inequalities; reported decimal gaps are for display only. All four commands were executed successfully on the exact included program, with independent finite-range coverage confirmed. Source-code audit should examine `trig_table`, `certified_root_floor`, `expected_sets` and `verify_N` as critical routines.

## Relationship to prior work
Gupta and Iosevich (arXiv:2606.15475, first posted June 13, 2026) developed the graph Fourier-ratio framework motivating small-part Fourier minimization. Gupta et al. (arXiv:2610.31807, first posted October 22, 2026) developed energy and graph-Fourier complexity comparisons, but did not classify four-point cyclic \(\ell^1\) minimizers. Ferguson et al. (arXiv:2610.36276, first posted October 26, 2026) proved the subgroup-coset equality case and complete two-/three-point statements, explicitly posed the general four-point problem in Question 9.1, and certified a local obstruction for four-point sets at modulus 17. Its subgroup result already covers our \(4\mid N\) subcase; the *finite exact global classification* of all odd and twice-odd moduli through 128 is the additional result recorded here.

The result is not a proof of the conjectured eventual progression minimizers for arbitrary odd modulus, nor a new graph-energy lower bound. Prior works on endpoint norms of **fixed** four-character Fourier projections concern different optimization objectives and do not imply classification over every four-element support.

## Limitations
The numerical cutoff 128 is a verified finite range, not a threshold for all larger integers. The exhaustive certificate requires NumPy integer arrays and the stated arithmetic bounds, and does not constitute an independent formal verification. An unindexed earlier exhaustive enumeration or a stronger infinite-modulus result could cover some of these cases. The finite classification does not determine a quantitative separation uniform in *all* moduli, nor cover arbitrary four-term complex coefficients. No independent scientific audit has been performed.

## References
1. V. Gupta and A. Iosevich, *Fourier Ratios of Graph Kernels: Energy Bounds, Optimal Labelings, and Recovery*, arXiv:2606.15475, first posted 2026-06-13, https://arxiv.org/abs/2606.15475.
2. V. Gupta, S. Ferguson, A. Iosevich, J. Iosevich, H. Tian and B. Song, *Additive Energy and Fourier Complexity of Graphs*, arXiv:2610.31807, first posted 2026-10-22, https://arxiv.org/abs/2610.31807.
3. S. Ferguson, V. Gupta, A. Iosevich, J. Iosevich, C. Kelly, G. Smith and S. Yang, *Edge Complexity of Complete Bipartite and Complete Multipartite Graphs*, arXiv:2610.36276, first posted 2026-10-26, particularly Theorem 2.3, Section 4, Question 9.1 and Appendix A, https://arxiv.org/abs/2610.36276.
4. The present package, `CHECK.py` and `CERT_*.json`, exact-integer exhaustive verification of the above finite statement.
