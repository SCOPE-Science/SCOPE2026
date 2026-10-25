# Exact Fibonacci analytic mixing norm of the classical cat map

## Finding
For the classical Arnold cat automorphism \(T(x)=Ax\pmod{\mathbb Z^2}\), with
\[
A=\begin{pmatrix}2&1\\1&1\end{pmatrix},
\]
and every \(0<\theta<1\) and integer \(n\ge0\), the exact optimal mean-zero analytic correlation is
\[
\boxed{\sup_{\substack{f,g\in\mathcal H_\theta^0\\\|f\|_\theta=\|g\|_\theta=1}}
\left|\int_{\mathbb T^2}(f\circ T^n)\overline g\,d\mu\right|
=\|U^n\|_{\mathcal H_\theta^0\longrightarrow\mathcal H_{\theta^{-1}}^0}
=\theta^{F_{n+3}}.}
\]
Here \(U f=f\circ T\), \(\mu\) is Haar probability, and the Fibonacci numbers satisfy \(F_0=0,F_1=1,F_{j+2}=F_{j+1}+F_j\). The sharp norm is attained at precisely **four individual Fourier frequencies** at each time (and also by their normalized combinations):
\[
\operatorname*{argmin}_{k\in\mathbb Z^2\setminus\{0\}}
\bigl(|k|_1+|A^n k|_1\bigr)=
\begin{cases}
A^{-r}\{\pm e_1,\pm e_2\},&n=2r,\\
A^{-r}\{\pm e_2,\pm(e_1-e_2)\},&n=2r+1.
\end{cases}
\]
In particular, the decay is double exponential with an **exact all-time Fibonacci exponent**, not only an asymptotic rate or unspecified constants.

## Assumptions and scope
The torus is \(\mathbb T^2=\mathbb R^2/\mathbb Z^2\), with normalized Lebesgue measure. The analytic Hilbert norm and its dual are the specific Fourier-weighted norms
\[
\|f\|_\theta^2=\sum_{k\in\mathbb Z^2}|\widehat f(k)|^2\theta^{-2|k|_1},\qquad
\|h\|_{\theta^{-1}}^2=\sum_{k\in\mathbb Z^2}|\widehat h(k)|^2\theta^{2|k|_1},\qquad
|k|_1=|k_1|+|k_2|.
\]
The superscript \(0\) requires the zero-frequency Fourier coefficient to vanish. Both observables may be complex-valued, although a real cosine pair also attains the norm. The theorem concerns the symmetric unimodular matrix displayed above, not general Anosov maps, other Fourier norms, or perturbations.

## Proof
**1. Exact reduction to a lattice minimum.** For the character \(e_k(x)=\exp(2\pi i k\cdot x)\), composition obeys \(U^n e_k=e_{A^n k}\), because \(A=A^\mathsf T\). Distinct frequencies remain distinct because \(A\in\mathrm{GL}(2,\mathbb Z)\). Passing between weighted orthonormal Fourier bases, \(U^n:\mathcal H_\theta^0\to\mathcal H_{\theta^{-1}}^0\) becomes a permutation of coordinates times positive diagonal weights \(\theta^{|k|_1+|A^n k|_1}\). Hence its norm and the sharp bilinear correlation supremum are both
\[
\theta^{m_n},\qquad m_n:=\min_{0\ne k\in\mathbb Z^2}\bigl(|k|_1+|A^n k|_1\bigr).
\]
The minimum exists, since the first term tends to infinity with \(|k|_1\). Taking single characters with respective unit coefficients \(\theta^{|k|_1}\) and \(\theta^{|A^n k|_1}\) proves attainment. It remains to compute \(m_n\) and all its minimizing frequencies.

**2. Fibonacci matrix identities.** For \(r\ge1\), direct induction gives
\[
A^r=\begin{pmatrix}F_{2r+1}&F_{2r}\\F_{2r}&F_{2r-1}\end{pmatrix},\quad
A^{-r}=\begin{pmatrix}F_{2r-1}&-F_{2r}\\-F_{2r}&F_{2r+1}\end{pmatrix}.
\]
The same identities hold at \(r=0\) on setting \(F_{-1}=1\). In particular, all displayed Fibonacci coefficients are nonnegative. Since \(A^r\) is an integer unimodular bijection, set \(w=A^r k=(u,v)\) to minimize over arbitrary \(w\in\mathbb Z^2\setminus\{0\}\).

**3. Even times.** When \(n=2r\), the minimized sum is
\[
S_{2r}(w)=|A^{-r}w|_1+|A^r w|_1.
\]
For \(r=0\), this is \(2|w|_1\), minimized only at the four signed coordinate vectors, and \(m_0=2=F_3\). Assume \(r\ge1\). If both coordinates are nonzero with the same sign, the second summand alone equals \(F_{2r+2}|u|+F_{2r+1}|v|\ge F_{2r+3}\), and the first summand is strictly positive. If they have opposite signs, the first summand alone is \(F_{2r+1}|u|+F_{2r+2}|v|\ge F_{2r+3}\), and the second is strictly positive. On either coordinate axis the sum is exactly \(F_{2r+3}(|u|+|v|)\). Thus the only minimizers are \(w=\pm e_1,\pm e_2\), and \(m_{2r}=F_{2r+3}\).

**4. Odd times.** When \(n=2r+1\), minimize
\[
S_{2r+1}(w)=|A^{-r}w|_1+|A^{r+1}w|_1,\qquad C=F_{2r+4}.
\]
The four claimed points \(w=\pm e_2,\pm(e_1-e_2)\) have sum \(C\), as follows immediately from the matrix identities. We show every other \(w\) has larger sum. By simultaneous sign reversal, assume the nonzero coordinates have the stated signs when applicable. If \(u,v\) have the same sign, then \(|A^{r+1}w|_1=F_{2r+4}|u|+F_{2r+3}|v|\). This already exceeds or equals \(C\) whenever \(u\ne0\), with a strictly positive other summand; if \(u=0\), direct evaluation yields \(C|v|\), with equality exactly when \(|v|=1\). If \(v=0\), direct evaluation gives a strictly larger coefficient than \(C\).

For opposite signs take \(w=(u,-v)\), \(u,v\ge1\). Then
\[
|A^{-r}w|_1=F_{2r+1}u+F_{2r+2}v,
\qquad C=F_{2r+1}+2F_{2r+2}.
\]
If \(v\ge2\), this term alone is at least \(C\) and the second term is positive. If \(v=1\) and \(u\ge3\), this term again reaches at least \(C\), since \(2F_{2r+1}\ge F_{2r+2}\); again the other term is positive. At \((u,v)=(2,1)\), the first term is \(C-F_{2r}\), but the second coordinate of \(A^{r+1}(2,-1)\) is \(F_{2r+2}+F_{2r}>F_{2r}\), giving strict inequality. Only \((u,v)=(1,1)\) survives, and direct substitution gives exactly \(C\). This proves \(m_{2r+1}=C\) and the four stated minimizers. Both parity cases therefore yield \(m_n=F_{n+3}\) for all \(n\ge0\).

**5. Attainers and rate.** Each minimizing frequency gives unit Fourier characters achieving \(\theta^{m_n}\). Conversely, in a diagonal-weighted permutation between Hilbert spaces, equality in the operator norm requires the input be supported entirely on coordinates attaining the maximum weight. Therefore no other individual Fourier frequency can attain the bound. The relation \(F_{n+3}\sim\varphi^{n+3}/\sqrt5\), with \(\varphi=(1+\sqrt5)/2\), yields the sharp double-exponential time exponent \(\log\varphi=\tfrac12\log((3+\sqrt5)/2)\), with the exact finite-time norm already proved.

## Verification
A standalone exact-integer checker, `verify.py`, enumerates every nonzero lattice point satisfying \(|k|_1\le F_{n+3}\) at each \(0\le n\le12\). This is a logically exhaustive finite check: a hypothetical better or tied point outside that diamond would satisfy \(|k|_1>F_{n+3}\) and hence cost greater than \(F_{n+3}\). It checks the four predicted minimizers and the exact minimum, and also checks the four candidates' identities through time \(120\). The recorded result is `VERIFY_OK exhaustive_n=0..12 exact_integer_pairs= 1207324 minimizers_per_n=4 candidate_iterations=0..120`. The unrestricted-time theorem is established in the proof above, not inferred from enumeration.

## Relationship to prior work
Shchetka's 2026 study (arXiv:2610.19019v1), especially Definitions 2.1–2.2, Lemma 2.4 and Section 4.5, motivates analytic/Hilbert-dual correlation norms and identifies sharp *asymptotic* double-exponential exponents. Its explicitly studied linear matrix is \(\bigl(\begin{smallmatrix}5&2\\2&1\end{smallmatrix}\bigr)\), and it does not state the present all-time Fibonacci norm or the complete maximizing frequency set for the classical cat matrix. Axenides–Floratos–Nicolis discuss correlations and Fibonacci structures in cat-map lattices but do not furnish this finite-time analytic Hilbert-space extremal identity in the examined portions. Earlier work of Brini–Siboni and Fannjiang–Wołowski treats quantitative analytic or Fourier mixing bounds; equivalence under alternative norms or notation remains a priority risk. The standard Fibonacci-power identity for the cat matrix and the diagonal Fourier reduction are acknowledged as known ingredients; the assertion is their sharp all-time optimization and maximizer classification in the specified natural analytic norm.

## Limitations
The formula depends on the exact \(\ell_1\) Fourier weights and on the classical symmetric integer matrix. It neither computes nonlinear correlation norms nor implies exact formulas for arbitrary hyperbolic toral automorphisms. The optimal observables may depend on time; this is an operator-norm statement, not a fixed-pair lower bound valid at every time. Searching existing literature cannot establish absolute priority. Independent validation has not been performed.

## References
1. Ekaterina Shchetka, *Mixing Rates for Analytic Observables: Toral Endomorphisms and Anosov Blaschke Deformations*, arXiv:2610.19019v1, publicly posted 13 October 2026, Sections 2, 3, 4.5. https://arxiv.org/html/2610.19019v1
2. M. Axenides, E. Floratos and S. Nicolis, *Exponential mixing of all orders for Arnol'd cat map lattices*, preprint, https://arxiv.org/abs/2401.08521. Selected pages concerning Fourier correlations were examined.
3. F. Brini and G. Siboni, *Estimates of correlation decay in auto/endomorphisms of the n-torus* (2001), identified through Reference [4] of [1]; full text not inspected.
4. A. Fannjiang and P. Wołowski, *Noise induced dissipation in Lebesgue-measure preserving maps on d-dimensional torus* (2003), identified through Reference [6] of [1]; full text not inspected.
