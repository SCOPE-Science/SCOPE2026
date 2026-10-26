# A Fejér certificate for the slope-two Hartogs diagonal

## Finding
For every integer \(n\ge1\), let \(m=2n+1\), and let \(Q_{m,n}(s)=s^{1-2n}P_{m,n}(s,s)\) be the degree-\(2(m-n)\) diagonal Bergman-numerator polynomial, normalized exactly as in Edholm and Mathew, Theorem 1.3 and Section 3.3. The polynomial \(Q_{2n+1,n}\) has precisely \(n+1\) zeros in the punctured unit disk and precisely \(n+1\) zeros outside the closed disk, counted with multiplicity. More quantitatively, for every real \(\theta\),
\[
 e^{-i(n+1)\theta}Q_{2n+1,n}(e^{i\theta})\ge 2n+1-\frac1n>0.
\]
The minimum of this positive centered trigonometric polynomial lies between \(2n+1-1/n\) and \(2n+1\). Every interior zero gives a genuine Bergman-kernel zero on the diagonal \(s=t\) of the Hartogs domain with exponent \(2+1/n\).

## Assumptions and scope
Fix an integer \(n\ge1\). Define \(m=2n+1\) and \(k=m-n=n+1\); then \(\gcd(m,n)=1\). The generalized Hartogs triangle is \(\mathbb H_{m/n}=\{(z_1,z_2)\in\mathbb C^2:|z_1|^{m/n}<|z_2|<1\}\). The 2025 Edholm--Mathew numerator is \(P_{m,n}(s,t)\), as in their equation (1.4). Their normalized polynomial \(Q_{m,n}(s)=s^{1-2n}P_{m,n}(s,s)\) is palindromic. In this result \(s\) is a complex variable; the symbols \(n,m,k\) denote integers as above. The assertion is about the diagonal polynomial and the associated diagonal kernel zeros, not about every zero of the full bivariate numerator.

## Proof
**1. Exact coefficients.** Edholm and Mathew's five-part numerator formula gives
\[
Q_{m,n}(s)=q_0(s)+q_1(s)+q_2(s)+q_3(s)+q_4(s),\qquad q_0(s)=m^2s^k.
\]
For \(0\le j\le 2n-1\), write \(j=2r\) or \(j=2r+1\), where \(0\le r\le n-1\). In equation (1.4h) their arithmetic parameters specialize to
\[
 L(2r)=L(2r+1)=r+1,\quad
 \kappa(2r)=n-1-r,\quad \kappa(2r+1)=2n-1-r.
\]
Put \(B(s)=q_1(s)+q_2(s)=\sum_{j=0}^{n+1}b_js^j\). Direct substitution in their equations (3.21b,c) gives \(b_0=n\), \(b_{n+1}=2n^2\), and, for every integer \(1\le j\le n\),
\[
\begin{aligned}
b_j={}&(2j+1)(n-j)+2j(2n-j+1)\\
&+(2j-1)(n+j)+2(j-1)^2\\
={}&(8n-4)j+2.
\end{aligned}
\]
At the endpoint \(j=n\), the first summand vanishes and represents no out-of-range contribution; at \(j=1\), the fourth summand vanishes likewise. Their reciprocal identities (3.23b,c) yield \(q_3(s)+q_4(s)=s^{2k}B(s^{-1})\). Thus, writing \(Q_{m,n}(s)=\sum_{j=0}^{2k}a_js^j\),
\[
 a_0=a_{2k}=n,\quad a_j=a_{2k-j}=(8n-4)j+2\ (1\le j\le n),\quad
 a_k=(2n+1)^2+4n^2=8n^2+4n+1.
\]
In particular the constant and leading coefficients are both positive.

**2. Positive-circle certificate.** Write \(s=e^{i\theta}\) and \(F_{n+1}(\theta)=|\sum_{j=0}^{n}e^{ij\theta}|^2\). The preceding coefficients imply the exact Fejér decomposition
\[
\begin{aligned}
T_n(\theta)&:=e^{-ik\theta}Q_{2n+1,n}(e^{i\theta})\\
&=(8n-4)F_{n+1}(\theta)+5
 +4\sum_{j=1}^{n}\cos(j\theta)+2n\cos((n+1)\theta).
\end{aligned}
\]
For \(\theta\not\equiv0\pmod{2\pi}\), set \(u=\theta/2\), \(v=(n+1)\theta\), and \(s_0=\sin^2u\in(0,1]\). The geometric-sum identity and Dirichlet-kernel identity give
\[
 F_{n+1}(\theta)=\frac{1-\cos v}{2s_0},\qquad
1+2\sum_{j=1}^{n}\cos(j\theta)=\cot u\,\sin v-\cos v.
\]
Consequently,
\[
T_n(\theta)=2n+1+H(1-\cos v)+2\cot u\,\sin v,
\qquad H=\frac{4n-2}{s_0}-(2n-2)\ge\frac{2n}{s_0}>0.
\]
With \(y=\sqrt{1-\cos v}\), the elementary estimate \(|\sin v|\le\sqrt2\,y\) and completion of the square show
\[
\begin{aligned}
T_n(\theta)&\ge 2n+1+Hy^2-2\sqrt2|\cot u|y\\
&\ge2n+1-\frac{2\cot^2u}{H}\\
&\ge2n+1-\frac{1-s_0}{n}\ge2n+1-\frac1n.
\end{aligned}
\]
At \(\theta\equiv0\pmod{2\pi}\), the exact coefficient formula makes \(Q_{2n+1,n}(1)>2n+1\), proving the same inequality there. For \(\theta=2\pi/(n+1)\), the Fejér kernel vanishes, the cosine sum is \(-1\), and \(T_n(\theta)=2n+1\); this establishes the stated upper bound on the minimum.

**3. Root count and kernel interpretation.** The strict positivity above excludes roots of \(Q_{m,n}\) on the unit circle. Its degree is \(2k\), its constant coefficient is nonzero, and it is reciprocal: \(Q_{m,n}(s)=s^{2k}Q_{m,n}(1/s)\). Every zero of modulus below one has a zero of reciprocal modulus above one with the same multiplicity. Therefore exactly \(k=n+1\) zeros lie in \(0<|s|<1\) and exactly \(k\) in \(|s|>1\). For an interior zero \(s\), the point \((s,s)\) belongs to \(\mathbb H_{m/n}\); the denominator \((1-s)^2(s^n-s^m)^2\) in the Bergman-kernel formula is nonzero there. Hence the vanishing of \(Q_{m,n}(s)\) gives a genuine Bergman-kernel zero. By the Reinhardt power-domain property, such a product point is realized by a pair of points of the domain.

## Verification
The standalone Python 3 file `verify_slope_two.py` independently constructs the polynomial from all five summands of Edholm--Mathew equation (1.4), and compares it coefficient-by-coefficient against the formula above for every integer \(1\le n\le500\). It passed. This finite check corroborates the parity computation but is not a proof for arbitrary \(n\); the parameter-uniform argument is the displayed algebra and trigonometric estimate. No external numerical data or other files are required.

## Relationship to prior work
Edholm and Mathew (initial arXiv posting May 26, 2025; Math. Z., 2026), Conjecture 4.20, ask for circle nonvanishing of \(Q_{m,n}\) for all coprime \(m>n\). Their Theorem 1.7 handles differences \(m-n=1,2\), and Section 4.3 reports proofs for fixed differences \(3,4,6\) plus unpublished further fixed-difference work. Here \(m-n=n+1\) grows without bound, while the exponents \(m/n=2+1/n\) tend to \(2\); this is a distinct arithmetic family with an explicit quantitative certificate. Edholm and McNeal (2017), Theorem 3.8, prove that kernels for all exponents at least \(2\) have zeros, by restricting the kernel to \(s=0\). That result does not determine the number of zeros of the nontrivial diagonal polynomial nor the positive circle margin proved here.

## Limitations
The full Conjecture 4.20 for arbitrary coprime \(m,n\) remains open. The result proves no assertion about the number of zeros of the full bivariate numerator away from the diagonal. Root multiplicities are counted algebraically; they are not claimed to be simple. Equivalence to unindexed or later work cannot be ruled out by database searches alone. The proof is a self-review mathematical argument, not an independent external validation.

## References
1. L. D. Edholm and V. T. Mathew, *Arithmetic properties and zeros of the Bergman kernel on a class of quotient domains*, arXiv:2505.20489 (first posted 2025-05-26); *Mathematische Zeitschrift* 313 (2026), article 43. https://doi.org/10.1007/s00209-026-04059-8
2. L. D. Edholm and J. D. McNeal, *Bergman Subspaces and Subkernels: Degenerate L-p Mapping and Zeroes*, *Journal of Geometric Analysis* 27 (2017), 2658--2683. https://doi.org/10.1007/s12220-017-9777-4
