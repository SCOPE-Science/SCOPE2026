# Exact autocorrelation and parity amplitudes in a neutral heterochaos baker map

## Finding
Let \(F\) be the critical two-dimensional heterochaos baker map specified below. For the centered vertical-coordinate observable \(\phi(x,y)=y-1/2\), define the stationary correlations
\[
C_n=\int_{[0,1]^2}\phi(x,y)\phi(F^n(x,y))\,dx\,dy \qquad (n\ge0).
\]
Put \(r(z)=(1-\sqrt{1-z^2})/z\), analytically continued by \(r(0)=0\). Then
\[
\boxed{\sum_{n=0}^{\infty} C_n z^n=\frac{r(z)}{6z(1-r(z)/2)^2},\qquad |z|<1.}
\]
The right side has a removable singularity at zero, with value \(1/12\). Its coefficients have the *parity-resolved* sharp asymptotic
\[
\boxed{C_n=\sqrt{\frac2\pi}\left(1+\frac{(-1)^n}{81}\right)n^{-3/2}+O(n^{-5/2}).}
\]
Thus the limiting constants along even and odd times are respectively \((82/81)\sqrt{2/\pi}\) and \((80/81)\sqrt{2/\pi}\). The decay exponent itself is established in previous work; the exact all-time generating function and distinct leading amplitudes are the present result.

## Assumptions and scope
Take Lebesgue measure on \([0,1]^2\) and the four-piece map (the final two pieces share the same first-coordinate formula):
\[
F(x,y)=\begin{cases}
(4x,y/2),&0\le x<1/4,\\
(4x-1,(y+1)/2),&1/4\le x<1/2,\\
(2x-1,2y),&1/2\le x\le1,\ 0\le y<1/2,\\
(2x-1,2y-1),&1/2\le x\le1,\ 1/2\le y\le1.
\end{cases}
\]
The formulas are understood almost everywhere; choices on the measure-zero partition boundaries do not change the integrals. The map is the \(m=2,a=1/4\) case of the two-dimensional heterochaos baker family, and it preserves planar Lebesgue measure. Only this map and this specific Lipschitz observable are claimed; there is no universal exact coefficient for arbitrary observables. The stationary centered observable has integral zero.

## Proof
**1. Independent base itinerary and fiber digits.** The first-coordinate map has three full branches, each onto \([0,1]\), with inverse widths \(1/4,1/4,1/2\). The branch symbols at successive times are independent with these probabilities under Lebesgue measure. The first two symbols prepend to the binary expansion of \(y\) the digits \(0\) and \(1\), respectively; the third deletes the leading digit. Conditional on a prepend occurring, the new digit is fair and independent of the prepend/delete sequence, of earlier prepended digits, and of the initial binary digits. The initial digits \(\xi_j\), \(j\ge1\), of \(y\) are independent fair bits. All these claims exclude only the null set with ambiguous binary expansions or a partition-boundary itinerary.

**2. Surviving initial bits.** Let \(S_0=0\), and let \(S_k\) be the simple symmetric nearest-neighbor random walk whose increment is \(+1\) at a prepend and \(-1\) at a deletion. Write \(m_n=\min_{0\le k\le n}S_k\). Initially, the \(j\)-th fiber digit has position \(j\). After \(n\) updates it remains present if and only if \(j>-m_n\), in which case its final position is \(j+S_n\). All other output bits come from independent prepended bits and are uncorrelated with initial digits. By the binary expansion \(y-1/2=\sum_{j\ge1}2^{-j}(\xi_j-1/2)\), absolute convergence and \(\mathbb E[(\xi_j-1/2)(\xi_k-1/2)]=\delta_{jk}/4\) give
\[
C_n=\frac14\,\mathbb E\sum_{j>-m_n}2^{-j}2^{-j-S_n}
=\frac1{12}\,\mathbb E[2^{2m_n-S_n}]. \tag{1}
\]
In the last equality, the geometric series begins at \(j=1-m_n\): \(\sum_{j=1-m_n}^\infty4^{-j}=4^{m_n}/3\). Equation (1) also gives positivity for every \(n\) and the initial value \(C_0=1/12\).

**3. Exact generating function.** Let \(r(z)=\sum_{n\ge1}\Pr(T_{-1}=n)z^n\), the generating function of the first hit of \(-1\) by a symmetric random walk begun at zero. The first-step recursion \(r=(z/2)(1+r^2)\) and \(r(0)=0\) give \(r(z)=(1-\sqrt{1-z^2})/z\). For \(j\ge0\), the generating function for a walk from zero to \(j\) without ever becoming negative is
\[
H_j(z)=\sum_{n\ge0}\Pr(S_n=j,\min_{0\le k\le n}S_k\ge0)z^n
=\frac{2}{z}r(z)^{j+1}. \tag{2}
\]
For completeness, reflection gives \(H_j(z)=[r(z)^j-r(z)^{j+2}]/\sqrt{1-z^2}\), and the identity \((1-r^2)/\sqrt{1-z^2}=2r/z\) yields (2). The generating function for paths whose overall minimum is exactly \(-h\) and terminal height \(-h+j\) factors into \(r(z)^h H_j(z)\): use the first hit of \(-h\) and the remaining walk constrained to stay at or above \(-h\). In (1), the weight of such a path is \(2^{-h-j}\). All terms are nonnegative for real \(0\le z<1\), so Tonelli's theorem legitimizes the sum:
\[
\begin{aligned}
\sum_{n\ge0}C_nz^n
&=\frac1{12}\sum_{h,j\ge0}2^{-h-j}r(z)^hH_j(z)\\
&=\frac{r(z)}{6z}\left(\sum_{h\ge0}(r(z)/2)^h\right)
\left(\sum_{j\ge0}(r(z)/2)^j\right)\\
&=\frac{r(z)}{6z(1-r(z)/2)^2}.
\end{aligned}
\]
Absolute convergence and analytic continuation extend this identity to all \(|z|<1\).

**4. Singularities and parity.** The first-passage series has nonnegative coefficients summing to one, hence \(|r(z)|\le1\) for \(|z|\le1\), so \(1-r(z)/2\) never vanishes there. The only singularities of the generating function on the circle of convergence are the square-root branch points \(z=1\) and \(z=-1\). With \(\delta_+=1-z\) and \(\delta_-=1+z\), direct expansion yields
\[
\begin{aligned}
\frac{r(z)}{6z(1-r(z)/2)^2}
&=\frac23-2\sqrt2\,\delta_+^{1/2}+O(\delta_+) \quad(z\to1),\\
&=\frac2{27}-\frac{2\sqrt2}{81}\,\delta_-^{1/2}+O(\delta_-)\quad(z\to-1).
\end{aligned}
\]
The analytic integer-power terms have no algebraic coefficient contribution at high orders. The next nonanalytic term at either point is of order \(\delta_\pm^{3/2}\). Singularity transfer using \([z^n](1-z)^{1/2}=-n^{-3/2}/(2\sqrt\pi)+O(n^{-5/2})\) and \([z^n](1+z)^{1/2}=(-1)^n[z^n](1-z)^{1/2}\) gives the asserted sharp expansion. The absence of other unit-circle singularities makes the remainder \(O(n^{-5/2})\). The distinct parity constants follow immediately.

## Verification
The standalone file `check.py` uses only Python's standard library. It independently (i) evolves the weighted symmetric walk by exact rational arithmetic, (ii) extracts the first thirteen generating-function coefficients from the Catalan expansion, and (iii) integrates the actual piecewise-affine planar map over exact rational rectangles for iterates zero through six. Every comparison passes. In particular
\[
(C_0,C_1,C_2,C_3,C_4,C_5,C_6)
=\left(\frac1{12},\frac1{24},\frac7{192},\frac5{192},\frac{73}{3072},\frac{115}{6144},\frac{859}{49152}\right).
\]
These finite checks confirm normalization and independent low-order consequences; the analytic generating-function and singularity arguments prove the infinite statements.

## Relationship to prior work
Takahasi (2023, arXiv:2307.08119) defined the generalized heterochaos baker family, demonstrated Lebesgue invariance, and established mixing and exponential correlation decay away from the neutral center. Takahasi and Tsujii (2024, arXiv:2408.16618) proved the **optimal** order \(n^{-3/2}\) for Hölder correlation decay in the neutral regime, using a reflected random-walk transfer-operator argument. That order, including its optimality, is not new here. The full mathematical statements and the reduced-operator proof in the 2024 preprint were compared: its upper/lower bounds do not specify the exact two-dimensional central-coordinate correlation generating function, the numerical leading amplitude, or the nonzero parity correction. The present result identifies those finer invariants for the natural affine observable. The walk first-passage and reflection identities are classical; the new computation is their exact combination with the binary-memory structure and the two boundary singularities of this dynamical observable.

## Limitations
The result concerns the critical parameter \(a=1/4\), binary center, planar Lebesgue measure and the specific centered-coordinate observable. It gives neither general observable-dependent asymptotic constants nor perturbation robustness, nor mixing rates for unrelated piecewise-affine systems. The manuscript does not assert independent peer verification or exhaustive priority coverage; mathematically equivalent formulas in unindexed sources remain a residual historical-priority risk. The first two coefficients alone do not certify the asymptotic; the infinite proof is independent of numerical or finite enumeration.

## References
1. H. Takahasi, *Exponential mixing for heterochaos baker maps and the Dyck system*, arXiv:2307.08119v1 (first public version 2023-07-16), Sections 1.1 and 3, https://arxiv.org/html/2307.08119v1.
2. H. Takahasi and M. Tsujii, *Polynomial rate of mixing for the heterochaos baker maps with mostly neutral center*, arXiv:2408.16618v1 (first public version 2024-08-29), especially Sections 1.2 and 2.2--2.6, https://arxiv.org/pdf/2408.16618.
3. Standard symmetric-walk reflection principle and first-passage/Catalan generating-function identities, derived explicitly in the proof above.
