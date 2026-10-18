# Sharp sixth moment and two phase orbits for four unimodular Fourier modes

## Finding
Let \(P(z)=c_0+c_1z+c_2z^2+c_3z^3\) with \(|c_j|=1\), and let \(m\) be normalized Haar probability measure on the unit circle. The exact sharp phase-only sixth moment is
\[
\boxed{\int_{|z|=1}|P(z)|^6\,dm(z)\ge 616-\frac{148}{3}\sqrt{111}=96.24108152593158\ldots.}
\]
Equality holds if and only if there are \(\lambda,\mu,u\in\mathbb S^1\) such that
\[
(c_0,c_1,c_2,c_3)=\lambda(1,\mu,\mu^2u,\mu^3u^3),\qquad
\operatorname{Re}u=\frac{\sqrt{111}-12}{6}.
\]
Modulo common phase and linear-phase modulation, precisely two extremal coefficient patterns exist, corresponding to the two conjugate values of \(u\).

For the normalized uniform average over the \(N\)-th roots of unity, exactly the same sharp constant and complete equality family hold for **every integer \(N\ge10\)**. This sharp stability threshold cannot be lowered to \(N=9\): a four-mode unimodular polynomial has an order-nine sampled sixth moment exactly \(48499/512\), strictly less than the continuous sharp constant.

## Assumptions and scope
All four frequencies \(0,1,2,3\) are distinct integral frequencies on the continuous circle, and all four coefficients have modulus exactly one. The integral and each root-of-unity sample average are probability normalized. The finite-grid result uses the exact characters \(z^j\) at \(N\)-th roots for \(N\ge10\); no conjecture is made for optimal sampled sixth moments at smaller orders. The result is a phase-only **minimum**, not an unrestricted-coefficient maximum or a fourth-moment result.

## Proof
**1. Remove phase symmetries and calculate the exact sixth moment.** Multiplication of \(P\) by a common unimodular scalar and substitution \(z\mapsto\nu z\) for \(|\nu|=1\) preserve the moment. These operations normalize \(c_0=c_1=1\). Write \(c_2=e^{i\alpha}\), \(c_3=e^{i\beta}\). Parseval applied to \(P^3\), whose frequencies range from \(0\) through \(9\), yields by convolution the exact trigonometric polynomial
\[
I(\alpha,\beta)=256+84\cos\alpha+84\cos(\beta-2\alpha)
+144\cos(\beta-\alpha)+6\cos\beta+6\cos(2\beta-3\alpha).
\tag{1}
\]
This identity follows from enumerating all \(4^3=64\) ordered triples in \(P^3\), grouping equal frequency sums, and expanding the squared absolute values. The supplied reproducible checker independently constructs every Laurent monomial from these triples and compares the exact coefficients against (1).

**2. Reduce globally to one real variable.** Set
\[
\phi=\frac{\beta-\alpha}{2},\qquad
\eta=\frac{\beta-3\alpha}{2},\qquad t=\cos\phi.
\]
Using \(\alpha=\phi-\eta\) and \(\beta=3\phi-\eta\), equation (1) becomes
\[
I=112+288t^2+12t(11+4t^2)\cos\eta.
\]
Since \(-1\le\cos\eta\le1\), writing \(s=|t|\in[0,1]\) gives the universal estimate
\[
I\ge H(s):=112-132s+288s^2-48s^3.
\tag{2}
\]
Every \(s\in[0,1]\) can attain the minimization in \(\eta\), so (2) is a sharp one-variable reduction, not just a relaxation.

**3. Minimize the cubic exactly.** Its derivative factors as
\[
H'(s)=-12(11-48s+12s^2).
\]
The only critical point in \([0,1]\) is
\[
s_*=2-\frac{\sqrt{111}}6\in(0,1).
\]
The other critical point exceeds one. The derivative changes from negative to positive at \(s_*\); hence \(s_*\) is the unique global minimum of \(H\). Exact substitution into (2) gives
\[
H(s_*)=616-\frac{148}{3}\sqrt{111}.
\]

**4. Classify all equality phases.** Equality in (2) forces \(|\cos\phi|=s_*\) and \(\cos\eta=-\operatorname{sgn}(\cos\phi)\). In the case \(\cos\phi>0\), \(\eta\equiv\pi\) modulo \(2\pi\), so \(\beta\equiv3\alpha\pmod{2\pi}\) and \(\cos\alpha=-s_*\). When \(\cos\phi<0\), \(\eta\equiv0\) and the same two conclusions follow. Conversely these two congruences attain (2). Removing the normalization \(c_0=c_1=1\) gives precisely the displayed coefficient vectors. The two solutions \(u=e^{\pm i\arccos(-s_*)}\) are inequivalent because the second-difference phase \(c_0c_2/c_1^2=u\) is invariant under both allowed symmetries.

**5. Exact finite-grid stability and its sharp boundary.** Since \(P^3\) has frequencies \(0\) through \(9\), its squared modulus has frequency differences of absolute value at most \(9\). The uniform root-of-unity average agrees term by term with the circle integral whenever \(N\ge10\). This proves the same sharp value and equality classification on every such finite grid.

At \(N=9\), set \(u=-1/4+i\sqrt{15}/4\) and \(P(z)=1+z+uz^2+u^3z^3\). Its continuous sixth moment from (2) is \(H(1/4)=385/4\). The only new alias terms in the nine-grid average are its two Fourier coefficients at \(\pm9\), whose combined contribution is \(2\operatorname{Re}(u^9)=2T_9(-1/4)=-781/512\), using the ninth Chebyshev polynomial. Thus the nine-grid moment equals \(48499/512\), which is strictly below the continuous optimum. This establishes sharpness of the universal nonaliasing threshold.

## Verification
The standalone Python program `artifacts/verify.py` independently expands all ordered triple products in \(P^3\), groups their frequency classes, and checks the eleven nonzero Laurent coefficients of (1) with integers. It independently evaluates the radical substitution with exact rational-pair arithmetic in \(\mathbb Q(\sqrt{111})\), verifies the Chebyshev order-nine witness exactly, and numerically compares circle Parseval with finite-grid sixth moments for seven grid orders at least ten. It prints a deterministic machine-readable PASS record in `artifacts/verify_output.json`. Finite numerical checks corroborate, but do not replace, the analytical global minimization and exact nonaliasing proof.

## Relationship to prior work
The classical theory of unimodular and Littlewood polynomials asks how close trigonometric polynomials with prescribed coefficient magnitudes can come to flat modulus. Schmidt's study of Littlewood's question develops fourth-moment and asymptotic flatness phenomena; the 2019 construction of flat Littlewood polynomials studies a large-degree, binary-coefficient, sup-norm question. Neither establishes the four-term **sixth**-moment global minimizer described here.

A published four-frequency unimodular phase-range theorem gives the different **fourth**-moment minimum \(19\) with extremal phase cosine \(-1/4\), whereas the present sixth-moment minimizer has the distinct phase cosine \((\sqrt{111}-12)/6\). A separate four-consecutive-frequency sixth-moment theorem maximizes the ratio of the sixth moment to the cube of the coefficient \(\ell^2\)-norm **over unrestricted coefficients**, using positive affine phases. That upper extremum does not imply a lower extremum subject to exactly unit coefficient magnitudes; the optimization directions and extremizer phases are different. No equal statement or stronger implication was located in the cited primary comparisons.

## Limitations
This does not solve sixth-moment phase minima for five or more terms, general frequency supports, arbitrary coefficient magnitudes, nor smaller sampling moduli. The published-source comparison cannot exclude an older unindexed length-four polyphase moment table or equivalent theorem. The radical bound is a complete mathematical proof under its stated assumptions, but novelty remains a best-knowledge bibliographic assessment, not an independent certification.

## References
1. K.-U. Schmidt, *On a problem due to Littlewood concerning polynomials with unimodular coefficients*, arXiv:1302.2766 (2013), https://arxiv.org/abs/1302.2766.
2. P. Balister, B. Bollobás, R. Morris, J. Sahasrabudhe, and M. Tiba, *Flat Littlewood Polynomials Exist*, arXiv:1907.09464 (first publicly posted 2019-07-22), https://arxiv.org/abs/1907.09464.
3. *Sharp fourth-moment phase range for four-frequency unimodular trigonometric polynomials*, published mathematical result, 2026, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-sharp-fourth-moment-phase-range-for-four-frequency-unimodular-tr--2e72429a4d8d.
4. *Sharp sixth-moment Fourier norm via four-term even-moment symmetrization*, published mathematical result, 2026, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-sharp-sixth-moment-fourier-norm-via-four-term-even-moment-symmet--f3e238ebf219.
