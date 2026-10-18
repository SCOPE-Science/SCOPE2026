# Arithmetic spectral cycles and information loss for equal-bin expanding maps

## Finding

Fix integers \(b\ge 2\) and \(q\ge 2\). Let \(T_b:[0,1)\to[0,1)\) be \(T_b(x)=bx\bmod 1\), let \(X\) be uniformly distributed on \([0,1)\), and record the equal-bin observation \(Z_n=\lfloor qT_b^n(X)\rfloor\) for each integer \(n\ge 0\). Write
\[
B=b^n=qL_n+r_n,\qquad 0\le r_n<q.
\]
The exact two-time joint law is
\[
\Pr(Z_0=i,Z_n=j)=\frac{L_n+\mathbf 1_{\{(j-Bi)\bmod q<r_n\}}}{qB},
\qquad 0\le i,j<q.\tag{1}
\]
Consequently both marginals are uniform. In particular, exact independence occurs at lag \(n\) **if and only if** \(q\mid b^n\).

Let \(Q_{b,q}\) denote the corresponding one-step stochastic matrix with entry \(Q_{j,i}=\Pr(Z_1=j\mid Z_0=i)\). Define \(q_0\) to be the largest positive divisor of \(q\) relatively prime to \(b\). For each divisor \(d>1\) of \(q_0\), let \(\ell_d\) be the multiplicative order of \(b\) modulo \(d\). The **complete characteristic polynomial** is
\[
\boxed{\det(zI-Q_{b,q})=(z-1)z^{q-q_0}
\prod_{\substack{d\mid q_0\\d>1}}
\left(z^{\ell_d}-b^{-\ell_d}\right)^{\varphi(d)/\ell_d}.}\tag{2}
\]
The empty product is one. Thus every nontrivial nonzero eigenvalue has modulus precisely \(1/b\); the zero eigenvalue has algebraic multiplicity \(q-q_0\). This gives the exact spectral distinction between finite-time complete memory loss and persistent exponentially small dependence.

Writing \(I_n=I(Z_0;Z_n)\) for Shannon mutual information in natural logarithmic units, with the convention \(0\log 0=0\), one has
\[
\boxed{I_n=\frac{r_n(L_n+1)}{B}\log\frac{q(L_n+1)}{B}
+\frac{(q-r_n)L_n}{B}\log\frac{qL_n}{B}.}\tag{3}
\]
The joint law versus the product law has exact total variation and chi-square divergences
\[
\|\mathcal L(Z_0,Z_n)-\mathcal L(Z_0)\otimes\mathcal L(Z_n)\|_{\mathrm{TV}}
=\frac{r_n(q-r_n)}{qB},\qquad
\chi^2=\frac{r_n(q-r_n)}{B^2}.\tag{4}
\]
For fixed \(b,q\),
\[
I_n=\frac{r_n(q-r_n)}{2b^{2n}}+O_q(b^{-3n}).\tag{5}
\]
If \(q_0=1\), all dependence vanishes exactly at the first integer \(n_*\) for which \(q\mid b^{n_*}\), and never earlier. If \(q_0>1\), dependence never vanishes at a finite lag, \(r_n\) is eventually nonzero and periodic, and
\[
\lim_{n\to\infty}-\frac{\log I_n}{n}=2\log b.
\]
The scaled information can have genuinely different subsequential limits despite this common exponential rate. For \(b=2,q=7\), the three consecutive values of \(r_n\) are \(2,4,1\) periodically for \(n\ge1\), yielding successive limiting coefficients \(5,6,3\) in \(b^{2n}I_n\) along the three residue classes of \(n\bmod3\).

## Assumptions and scope

The source is Lebesgue measure, the transformation is integer multiplication modulo one, the observing partition comprises the \(q\) standard half-open intervals \([i/q,(i+1)/q)\), and the same partition is used at the two observation times. The formulas are exact for every integer \(b,q\ge2\) and every \(n\ge0\), with interval endpoints irrelevant because they form a null set. The matrix acts on probability column vectors; its transpose acts on observables. The polynomial in (2) includes algebraic multiplicity even when distinct divisor terms have common roots.

## Proof

**1. Exact interval counting.** On the initial bin \(i\), write \(x=(i+u)/q\) with \(0\le u<1\). Conditional on that bin, \(u\) is uniform. Multiplication by \(B=b^n\) gives
\[
qT_b^n(x)\equiv Bi+Bu\pmod q.
\]
As \(u\) increases from zero to one, the integer part of \(Bi+Bu\) runs once through each of the \(B\) consecutive integers \(Bi,Bi+1,\ldots,Bi+B-1\). A future bin equals the integer's residue modulo \(q\). Every complete block of \(q\) consecutive integers contributes once to every residue; the remaining \(r_n\) integers contribute to precisely the residues specified in (1). A single interval has unconditional mass \(1/q\), proving (1). Since integer multiplication preserves Lebesgue measure, the second marginal is also uniform. If \(r_n\ne0\), every row contains both a count \(L_n\) and a count \(L_n+1\), so the joint law differs from the product law; if \(r_n=0\), it equals the product law exactly.

**2. The finite-state transition powers.** The same count gives
\[
(Q_{b,q}^n)_{j,i}=\frac1{b^n}\#\{0\le a<b^n: j\equiv b^ni+a\pmod q\}.\tag{6}
\]
For \(n=1\) this is the definition of the one-step transition. The induction uses the bijection \((a,d)\mapsto ba+d\) from \(\{0,\ldots,b^n-1\}\times\{0,\ldots,b-1\}\) onto \(\{0,\ldots,b^{n+1}-1\}\). Thus the transition-matrix power in (6) agrees with the actual two-time conditional law, without assuming unverified probabilistic independence of successive observations.

**3. Fourier-cycle diagonal blocks.** Let \(\omega=e^{2\pi i/q}\), and for \(0\le m<q\) define the character \(e_m(j)=\omega^{mj}\). On these characters,
\[
Q_{b,q}^{\mathsf T}e_0=e_0,\qquad
Q_{b,q}^{\mathsf T}e_m=c_m e_{bm\bmod q},\quad
c_m=\frac1b\frac{1-\omega^{bm}}{1-\omega^m}\quad(m\ne0).\tag{7}
\]
If \(bm\equiv0\pmod q\), the corresponding coefficient \(c_m\) is zero, and the character is killed rather than mapped to the constant mode. For a nonzero residue of additive order \(d=q/\gcd(m,q)\), the multiplication-by-\(b\) graph has a nonzero directed cycle precisely when \(\gcd(d,b)=1\). For each such \(d\), the \(\varphi(d)\) residues split into exactly \(\varphi(d)/\ell_d\) cycles of length \(\ell_d\). On each cycle the product of the weights in (7) telescopes to \(b^{-\ell_d}\), because the numerator for one residue cancels the denominator for the next. The weighted cycle therefore contributes the characteristic factor \(z^{\ell_d}-b^{-\ell_d}\). The other characters form transient directed trees and contribute zero eigenvalues. The number of cycling nonconstant characters is \(\sum_{d\mid q_0,\,d>1}\varphi(d)=q_0-1\). Adding the one constant character proves (2) and its multiplicities.

**4. Quantified information loss.** The joint probability in (1) has \(qr_n\) entries of size \((L_n+1)/(qB)\) and \(q(q-r_n)\) entries of size \(L_n/(qB)\). Substituting into \(I_n=\sum_{i,j}p_{ij}\log(q^2p_{ij})\) proves (3). Relative to \(1/q^2\), the two entry deviations are respectively \((q-r_n)/(q^2B)\) and \(-r_n/(q^2B)\). Summing their absolute values and normalized squares proves (4). Taylor expansion of \((1+u)\log(1+u)\), using cancellation of the linear terms and \(|u|\le q/B\), proves (5), uniformly over the finitely many residues for fixed \(q\).

**5. Exact cutoff and arithmetic oscillation.** The condition \(q\mid b^n\) occurs for some \(n\) exactly when every prime divisor of \(q\) also divides \(b\), equivalently \(q_0=1\). Otherwise \(b^n\bmod q\) is never zero. Powers in a finite multiplicative semigroup are eventually periodic; their nonzero residue values have positive, finite coefficient \(r(q-r)/2\), so (5) gives the asserted exponential rate. For \(2^n\bmod7\), the cycle \(2,4,1\) gives coefficients \(5,6,3\). This completes the theorem.

## Verification

The included standalone `check_arithmetic_binning.py` calculates \(7100\) joint cells by exact rational intersection of preimage intervals, comparing them with (1). It verifies the two exact divergences, tests Fourier-cycle products, and checks \(44\) complete characteristic polynomials against both the cycle and divisor formulas over the rationals. It also checks the three limiting coefficients for the seven-bin example. Running `python check_arithmetic_binning.py` produced `VERIFY_OK direct_cells= 7100 ; exact_characteristic_polynomials= 44 ; Fourier_cycles=verified; periodic_limits=verified`. These finite checks support, but do not replace, the general proofs above.

## Relationship to prior work

Binder and Wissman (2010) established a transfer-matrix framework for time-delayed coarse-grained measurements, and considered Bernoulli shifts under four-bin and three-bin partitions. In particular, the finite-time loss for the four-bin binary shift and the eigenvalues of the three-bin example are antecedents, not new claims here. The contribution established by (1)–(5) is the *all-resolution arithmetic classification*: a closed divisor-order characteristic polynomial, an exact finite-independence criterion for arbitrary \(b,q\), and a nontrivial periodic prefactor for Shannon mutual information. The general transfer-matrix machinery motivates the calculation but does not itself state these formulas or the divisibility classification. The possibility of an equivalent prior formulation using Fourier or arithmetic language remains an originality risk.

## Limitations

The theorem concerns equal-width standard bins, integer expansion, Lebesgue initial data, and two-time information. It does not classify shifted or unequal partitions, noninteger beta maps, multi-time conditional mutual information, or arbitrary invariant measures. The theorem is a mathematical calculation, not an empirical claim about finite noisy samples. The full relevant 2010 source was inspected; unlocated equivalent results remain possible. No external independent audit has been carried out.

## References

1. P.-M. Binder and B. D. Wissman, “Geometry of repeated measurements in chaotic systems,” *Chaos* **20** (2010), 013106, published online 26 January 2010, DOI: 10.1063/1.3298244. Full text was available from the authors' university-hosted copy.
