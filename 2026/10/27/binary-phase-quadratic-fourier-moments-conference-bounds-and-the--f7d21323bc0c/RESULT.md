# Binary-phase quadratic Fourier moments: conference bounds and the first seven-vertex obstruction

## Finding
For an integer \(n\ge4\), choose signs \(\varepsilon_{ij}\in\{-1,1\}\) for \(1\le i<j\le n\), and define
\[
P_{\varepsilon}(z)=\sum_{1\le i<j\le n}\varepsilon_{ij}z_i z_j,\qquad z\in\mathbb T^n.
\]
All integrals below use normalized Haar measure. Put \(m_n=\min_{\varepsilon}\int_{\mathbb T^n}|P_{\varepsilon}|^4\). The exact first seven values are
\[
\begin{array}{c|rrrrrrr}n&4&5&6&7&8&9&10\\\hline
m_n&58&150&315&741&1300&2124&3285\end{array}.
\]
More generally, let \(S\) be the symmetric sign matrix with \(S_{ii}=0\) and \(S_{ij}=\varepsilon_{ij}\) for \(i\ne j\). Then the following **exact nonnegative deficit identity** holds:
\[
\int_{\mathbb T^n}|P_{\varepsilon}|^4
=\binom n2+6\binom n3+12\binom n4+
\sum_{i\ne j}\bigl((S^2)_{ij}\bigr)^2.
\tag{1}
\]
Consequently every sign pattern obeys the lower bound given by the first three terms in (1), with equality if and only if \(S\) is a symmetric conference matrix, \(S^2=(n-1)I\). For odd \(n\), the right side improves by \(n(n-1)\), and equality holds if and only if all off-diagonal entries of \(S^2\) have modulus one. Both parity bounds are sharp for infinitely many dimensions: for each prime power \(q\equiv1\pmod4\), equality holds at \(n=q+1\) and \(n=q\), respectively.

Equivalently, if \(b(\varepsilon)\) counts four-vertex sets \(\{i,j,k,l\}\) whose three matching products \(\varepsilon_{ij}\varepsilon_{kl},\varepsilon_{ik}\varepsilon_{jl},\varepsilon_{il}\varepsilon_{jk}\) agree, then
\[
\int|P_{\varepsilon}|^4=\binom n2+12\binom n3+4\binom n4+32b(\varepsilon).
\tag{2}
\]
The exact minimum of \(b\) is zero for \(4\le n\le6\), while for \(7\le n\le10\) it is \(\binom n4/7\). Thus seven is the first dimension where these four-vertex phase collisions cannot all be frustrated.

## Assumptions and scope
The coefficients are restricted **exactly** to real signs \(\{-1,1\}\), not arbitrary complex unimodular phases and not arbitrary magnitudes. The Fourier frequencies are all distinct square-free monomials of degree two, on the continuous torus \(\mathbb T^n\) with independent coordinate characters. No discrete sign-cube substitution or additional frequency aliasing is assumed. The sharp finite list concerns dimensions \(4\) through \(10\); the universal matrix identity and the two lower bounds apply to all dimensions \(n\ge4\), with the stated infinite equality families.

## Proof
**Fourier expansion.** Expand \(P_{\varepsilon}^2\) and use orthogonality of monomials. The terms from a repeated edge contribute \(\binom n2\). Two distinct edges sharing one vertex contribute \(4\) per unordered pair, for a total \(12\binom n3\). For four distinct vertices, the three perfect matchings have equal output Fourier monomial and their combined coefficient is twice the sum of their signed products. Its squared magnitude is \(36\) when the three signs agree and \(4\) otherwise. Summing proves (2).

**Seidel trace identity.** Each four-vertex set has three unoriented four-cycles. The indicator that all three matching products agree is one fourth of one plus the three four-cycle products. Each unoriented four-cycle contributes eight ordered closed walks to \(\operatorname{tr}S^4\); the remaining closed walks have total weight \(n(n-1)(2n-3)\). Therefore
\[
32b=8\binom n4+\operatorname{tr}S^4-n(n-1)(2n-3).
\]
Since \((S^2)_{ii}=n-1\), expanding \(\operatorname{tr}S^4=\sum_{i,j}(S^2)_{ij}^2\) proves (1). The zero-deficit equivalence follows immediately. If \(n\) is odd, each off-diagonal entry of \(S^2\) is a sum of \(n-2\) signs, hence is an odd integer, proving the stronger bound and its equality criterion.

**Paley equality examples.** For each prime power \(q\equiv1\pmod4\), index a \((q+1)\)-by-\((q+1)\) matrix by \(\{\infty\}\cup\mathbb F_q\). Set its diagonal to zero, its \(\infty\)-row and column to one, and \(S_{xy}=\chi(x-y)\) for distinct field elements, where \(\chi\) is the quadratic multiplicative character. As \(\chi(-1)=1\), the matrix is symmetric. The character sums \(\sum_y\chi(x-y)=0\) and \(\sum_y\chi(x-y)\chi(z-y)=-1\) for \(x\ne z\) give \(S^2=qI\). Deleting the \(\infty\)-row and column yields a matrix \(T\) with \(T^2=qI-\mathbf1\mathbf1^\top\), so all off-diagonal entries of \(T^2\) equal \(-1\). This proves the claimed infinite equality families.

**First forced collisions and exact finite values.** Switching signs by \(\varepsilon_{ij}\mapsto u_i u_j\varepsilon_{ij}\), with each \(u_i\in\{-1,1\}\), does not change (2). Every switching class has exactly one representative with all edges from vertex \(1\) positive. At \(n=7\), only \(\binom62=15\) edge signs remain, giving exactly \(2^{15}=32768\) cases. The supplied exhaustive integer checker constructs two independent four-cycle parity masks for each of the \(35\) four-sets and checks all cases; the smallest \(b\) is exactly \(5\), attained by \(3024\) normalized assignments. This is an exhaustive finite proof of the single base-case bound, not a sampled experiment.

For any \(n\ge7\), count the incidence of four-sets inside seven-sets: every seven-set contains at least five agreeing-matching four-sets, and every four-set lies in \(\binom{n-4}{3}\) seven-sets. Hence \(b\ge\binom n4/7\). At \(n=10\) the Paley construction over \(\mathbb F_9\) has \(b=30=\binom{10}{4}/7\). Every seven-set of its ten indices must therefore attain the seven-vertex bound, and the same incidence identity shows that each of its induced \(n\)-vertex submatrices, \(7\le n\le10\), attains \(\binom n4/7\). For \(4\le n\le6\), the Paley matrix over \(\mathbb F_5\) has \(b=0\), and so do all its principal submatrices. Substitute these exact collision counts into (2) to obtain the displayed list.

## Verification
Run `python3 checker.py` beside this file. It enumerates all normalized sign patterns for \(4\le n\le7\) (including all \(32768\) cases at seven vertices), checks the Paley conference identities over \(\mathbb F_5\) and \(\mathbb F_9\) in exact integer arithmetic, independently counts matching-product collisions on all indicated principal submatrices, and checks the seven resulting exact moments. The recorded output in `CHECKS.txt` ends with `ALL_CHECKS_PASSED`. The infinite-prime-power character identity and the general torus Fourier identity are established algebraically above and are **not** inferred from finite computation.

## Relationship to prior work
Symmetric conference matrices, Paley constructions and Seidel switching are classical. Haemers–Parsaei Majd (2021) discuss their spectra, principal submatrices, and the Paley construction; those facts are used rather than presented as new. Previously recorded sharp **upper** fourth-moment bounds for unrestricted complex coefficients of the same complete degree-two Fourier layer do not imply the binary-phase **minimum** or the seven-vertex obstruction. Work on binary fourth moments of a full hypercube Fourier aperture treats a different character support; it does not establish the matching-collision count for all quadratic square-free modes on a continuous torus. The combination here is the exact torus-to-Seidel deficit, sharp binary minima through the first obstruction and their conference-matrix equality mechanism. No mathematical priority beyond the inspected sources is claimed.

## Limitations
This does not identify all equality signings in each dimension, classify conference matrices, or solve the unrestricted complex-phase minimization. Outside the displayed finite dimensions and the specified equality families, the universal bounds need not be sharp. The seven-vertex base is an exhaustive computer-assisted finite result; it is not replaced by a closed-form hand classification. Equivalent results in unindexed work on Seidel fourth moments or two-graphs remain a literature risk.

## References
1. W. H. Haemers and L. Parsaei Majd, *Spectral symmetry in conference matrices*, Designs, Codes and Cryptography 90 (2022), 1983–1990; first publicly available online 18 March 2021. DOI: 10.1007/s10623-021-00858-8.
2. K. Gunderson and J. Semeraro, *Turán numbers and switching*, arXiv:2204.10775, first publicly available 22 April 2022 (background on switching; no claim of identical extremal invariant).
3. Previously reported sharp upper fourth-moment theorem for the complete quadratic torus layer, item `bbffed0a-87b1-4413-ab31-580c2a2c2667` (different extremal direction).
