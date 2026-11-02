# A harmonic staircase of sharp finite Cesàro norms on mixed endpoint sequence spaces

## Finding

For every integer \(n\ge2\), \(0\le t\le1\), and \(0<\varepsilon\le1\), define the finite generalized Cesàro matrix by
\[
(C_t x)_i=\frac1i\sum_{j=1}^{i}t^{i-j}x_j\qquad(1\le i\le n)
\]
and equip \(\mathbb R^n\) with the mixed endpoint norm
\[
N_\varepsilon(x)=(1-\varepsilon)\|x\|_\infty+\varepsilon\|x\|_1.
\]
Set \(c_j(t)=\sum_{i=j}^{n}t^{i-j}/i\). Then the exact norm is
\[
\boxed{\|C_t\|_{N_\varepsilon\to N_\varepsilon}=\max_{1\le k\le n}\frac{1-\varepsilon+\varepsilon\sum_{j=1}^{k}c_j(t)}{1+\varepsilon(k-1)}.}
\]
Each quotient is the ratio for the positive indicator of coordinates \(1,\ldots,k\); at least one such indicator is a norming vector.

At the classical Cesàro endpoint \(t=1\), writing \(H_0=0\), \(H_j=\sum_{i=1}^j1/i\), this becomes
\[
\boxed{\|C_1\|=1+\varepsilon\max_{1\le k\le n}\frac{k(H_n-H_k)}{1+\varepsilon(k-1)}.}
\]
For \(1\le k<n\) with \(H_n-H_k>1\), define
\[
\varepsilon_k=\frac{H_n-H_k-1}{H_n-H_k+k-1}.
\]
These positive transition values strictly decrease with \(k\); adjacent candidate quotients are equal exactly at \(\varepsilon=\varepsilon_k\), increase across \(k\to k+1\) for smaller \(\varepsilon\), and decrease for larger \(\varepsilon\). Thus optimal support ranks form an exact descending staircase as \(\varepsilon\) increases, with only adjacent ties at the transitions. For \(n\le3\), the optimal rank is always one. For \(n\ge4\), the rank can exceed one; for \(n=4\) the transition is exactly \(1/13\).

As \(\varepsilon\downarrow0\), the leading correction selects a rank maximizing \(k(H_n-H_k)\). Any maximizing rank \(k_n\) satisfies \(k_n/n\to 1/e\) as \(n\to\infty\).

## Assumptions and scope

All vectors are real, dimensions are finite, \(n\ge2\), \(t\in[0,1]\), and \(\varepsilon\in(0,1]\). The norm is the sum of the endpoint norms, not the maximum or an interpolation functor norm. The generalized Cesàro convention is one-indexed, with \(0^0=1\) on diagonal entries. No claim about equality cases other than the displayed norming indicator vectors is required.

## Proof

**Indicator reduction.** Positivity gives \(|C_t x|\le C_t|x|\) coordinatewise, and \(N_\varepsilon\) is monotone on the positive cone. Sort the nonnegative values of \(|x|\) as \(a_1\ge\cdots\ge a_n\ge0\), set \(a_{n+1}=0\), and let \(S_k\) index the largest \(k\) values. Then
\[
|x|=\sum_{k=1}^n(a_k-a_{k+1})\mathbf1_{S_k},\quad
N_\varepsilon(x)=\sum_{k=1}^n(a_k-a_{k+1})[1+\varepsilon(k-1)].
\]
The equality on the right uses \(\|x\|_\infty=a_1\) and \(\|x\|_1=\sum_{k}k(a_k-a_{k+1})\). Triangle inequality therefore reduces the operator norm to the supremum of the ratios for nonempty support indicators.

**Initial support is optimal.** Fix a support \(S\) of size \(k\). Every coordinate of \(C_t\mathbf1_S\) is between zero and one: its numerator has at most \(i\) summands, each at most one. Hence \(\|C_t\mathbf1_S\|_\infty\le1\). For its \(\ell_1\)-norm,
\[
\|C_t\mathbf1_S\|_1=\sum_{j\in S}c_j(t).
\]
The numbers \(c_j(t)=\sum_{d=0}^{n-j}t^d/(j+d)\) strictly decrease in \(j\) for \(0\le t\le1\). Therefore the latter sum is at most \(\sum_{j=1}^k c_j(t)\). The initial support \(S=\{1,\ldots,k\}\) makes both inequalities equalities, since its first output coordinate is one. Dividing by the support-independent input norm \(1+\varepsilon(k-1)\) proves the exact formula.

**Harmonic simplification and thresholds.** For \(t=1\), \(c_j(1)=H_n-H_{j-1}\); summing \(j=1,\ldots,k\) gives \(\sum_{j=1}^k c_j(1)=k[1+H_n-H_k]\). The rank-\(k\) quotient is thus \(r_k=1+\varepsilon k(H_n-H_k)/[1+\varepsilon(k-1)]\). Writing \(h=H_n-H_k\), direct cross multiplication yields
\[
\operatorname{sgn}(r_{k+1}-r_k)=\operatorname{sgn}[(h-1)-\varepsilon(h+k-1)]
\]
for positive \(\varepsilon\). For \(h\le1\) this sign is negative. When \(h>1\), its zero is \(\varepsilon_k\). Since \(h\) strictly decreases and \(k\) increases, \((h-1)/(h+k-1)\) strictly decreases: it is increasing in \(h>1\) and decreasing in \(k\). These ordered adjacent comparisons show that the candidate sequence has a single peak, except for an adjacent tie at a transition. The inequality \(H_n-H_1>1\) is equivalent to \(n\ge4\). For \(n=4\), \(H_4-H_1=13/12\), whence \(\varepsilon_1=1/13\).

**Small-mixture rank.** For fixed \(n\), the derivative at \(\varepsilon=0^+\) of \(r_k\) is \(B_k=k(H_n-H_k)\). For any sequence of ranks with \(k/n\to u\in(0,1]\), harmonic-sum estimates give \(B_k/n\to u\log(1/u)\); if \(k/n\to0\), the ratio tends to zero by the same standard upper bound \(H_n-H_k\le\log(n/k)+1/k\). The function \(u\log(1/u)\) has the unique maximum at \(u=e^{-1}\), which proves the asserted convergence of maximizing ranks.

## Verification

The standalone Python file `verify_cesaro.py` uses exact rational arithmetic. It compares the proposed value with every nonempty binary support in 128 separate parameter/dimension cases, verifies 16,192 support evaluations, checks 3,885 adjacent threshold comparisons, and confirms the \(n=4\) rational threshold. Running `python verify_cesaro.py` prints a single PASS line. These checks test the formulas and conventions; they are finite diagnostics, not the unrestricted proof.

## Relationship to prior work

Curbera and Ricker's generalized Cesàro operator study [1] provides the matrix definition and broad Banach-lattice compactness/spectral results. Its Theorem 3.9 gives a space-independent upper estimate \(\|C_t\|\le(1-t)^{-1}\) on rearrangement-invariant sequence spaces for \(0\le t<1\); its later operator-norm results treat other sequence lattices. The present exact finite-dimensional formula and its harmonic support-rank transitions are more specialized in the normed space and sharper in the conclusion, and are not immediate numerical instances of that upper estimate. Albanese, Bonet and Ricker [2] focus on spectrum and linear dynamics in nonnormable sequence spaces; no finite mixed-endpoint norm formula is asserted there. Jameson and Lashkaripour [3] address lower bounds rather than the upper operator norm calculated here. Standard finite majorization and indicator decomposition are used without novelty claims.

## Limitations

This is not a statement about all Lorentz weights, all positive matrices, or infinite-dimensional extensions. The operator \(C_t\) at \(t=1\) on infinite-dimensional \(\ell_1\) is not covered. The literature review cannot exclude an equivalent formula in older specialized matrix-inequality or endpoint interpolation literature, and independent verification has not been performed. The rank staircase concerns norming support indicators; it does not classify all possible norming vectors.

## References

1. G. P. Curbera and W. J. Ricker, *Fine spectra and compactness of generalized Cesàro operators in Banach lattices in* \(\mathbb C^{\mathbb N_0}\), arXiv:2302.08750v1 (first arXiv submission 2023-02-17); especially formula (1.1), Theorem 3.9, Remark 3.10, Proposition 4.15 and Remark 4.16. https://arxiv.org/abs/2302.08750
2. A. A. Albanese, J. Bonet, and W. J. Ricker, *Spectral properties of generalized Cesàro operators in sequence spaces*, arXiv:2305.04805v1 (2023-05-08). https://arxiv.org/abs/2305.04805
3. G. J. O. Jameson and R. Lashkaripour, *Lower bounds of operators on weighted \(\ell_p\) spaces and Lorentz sequence spaces*, Glasgow Math. J. 42 (2000), 211–223. https://doi.org/10.1017/S0017089500020061
