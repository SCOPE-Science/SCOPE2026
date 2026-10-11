# Sharp fourth-moment extension and phase tori for the parabola modulo a prime cube

## Finding

For every odd prime \(p\), let \(R=\mathbb Z/p^3\mathbb Z\) and define
\[
Tf(u,v)=\sum_{t\in R} f(t)\exp(2\pi i(ut+vt^2)/p^3).
\]
Equip the input with counting-measure \(\ell^2(R)\) and the output with probability-measure \(L^4(R^2)\). Then
\[
\boxed{\|T\|_{\ell^2\to L^4}^{4}=2p-1.}
\]

The complete nonzero extremizers are the functions supported on one residue class modulo \(p\), which on that class have the form
\[
\boxed{f(r+pu+p^2\ell)=c_u\exp(2\pi i\xi\ell/p),\quad
r,u,\ell,\xi\in\mathbb F_p,\quad |c_u|=a>0,}
\]
where \(r\) and \(\xi\) are fixed but the phases of the \(p\) coefficients \(c_u\) are arbitrary. Outside that residue class \(f\) vanishes. After quotienting by nonzero complex scalars, the extremizers form \(p^2\) disjoint tori, each of real dimension \(p-1\). In particular, the sharp fourth-power constant and extremizer geometry at the first odd prime-power exponent differ from the prime-square case.

For an arbitrary complex input the exact nonnegative deficit in the theorem below measures leakage between the \(p\) coarse residue classes, disagreement of fine-scale Fourier frequencies, and imbalance across middle-digit blocks. No asymptotic limiting operation is used.

## Assumptions and scope

The prime \(p\) is odd; \(r,u,\ell\) always range independently over \(\mathbb F_p=\{0,\ldots,p-1\}\). Each element \(t\in R\) has a unique representation \(t=r+pu+p^2\ell\). Write
\[
g_{r,u}(\ell)=f(r+pu+p^2\ell),\quad
\widehat g_{r,u}(\xi)=\sum_{\ell\in\mathbb F_p}g_{r,u}(\ell)e^{-2\pi i\xi\ell/p},
\]
\[
A_{r,u}(\xi)=|\widehat g_{r,u}(\xi)|^2,\quad
S_r(\xi)=\sum_{u\in\mathbb F_p}A_{r,u}(\xi),\quad
m_r=\sum_{u,\ell}|g_{r,u}(\ell)|^2.
\]
Thus \(\sum_r m_r=\|f\|_2^2\) and \(\sum_{\xi}S_r(\xi)=p m_r\). The notation \(\sum_{\xi\ne\eta}\) denotes **ordered** pairs of different frequencies.

**Exact deficit identity.** For every complex \(f:R\to\mathbb C\),
\[
\begin{aligned}
&(2p-1)\|f\|_2^4-\|Tf\|_4^4\\
&\quad=(4p-6)\sum_{r<s}m_rm_s\\
&\qquad+\frac{2p-1}{p^2}\sum_r\sum_{\xi\ne\eta} S_r(\xi)S_r(\eta)\\
&\qquad+\frac1p\sum_{r,\xi}\left(\sum_u A_{r,u}(\xi)^2-\frac{S_r(\xi)^2}{p}\right).
\end{aligned}
\]
All three summands are nonnegative for odd \(p\). The last parenthesis is the exact variance \(\sum_u(A_{r,u}(\xi)-S_r(\xi)/p)^2\).

## Proof

**Step 1 (orthogonality and fibers).** Character orthogonality on \(R^2\) gives
\[
\|Tf\|_4^4=\sum_{s,z\in R}\left|\sum_{\substack{x+y=s\\x^2+y^2=z}}f(x)f(y)\right|^2.
\]
For a pair \((x,y)\) of distinct coarse residues modulo \(p\), the difference \(x-y\) is a unit. Any other pair in the same fiber has the same sum and the same squared difference, since \((x-y)^2=2(x^2+y^2)-(x+y)^2\). A unit has exactly two square roots, differing by sign, in \(R\): starting with two simple roots modulo \(p\), Hensel lifting is unique at each higher digit because \(2(x-y)\) is invertible. Thus such a fiber consists of the two orientations \((x,y)\) and \((y,x)\). The contribution of all mixed coarse classes is exactly \(4\sum_{r<s}m_rm_s\).

**Step 2 (block-convolution formula).** For a pair in the same coarse residue \(r\), write \(x=r+pu+p^2\ell\) and \(y=r+pv+p^2h\). Its sum modulo \(p^3\) records \(u+v\) modulo \(p\) and the fine-digit sum \(\ell+h\) modulo \(p\), up to a fixed carry depending on \(r,u,v\). Its squared difference modulo \(p^3\) is \(p^2(u-v)^2\). Because \(p\) is odd, the sum \(u+v\) and squared difference \((u-v)^2\) determine precisely the *unordered* pair \(\{u,v\}\). Consequently the contribution from a diagonal block \(u=v\) is \(\|g_{r,u}*g_{r,u}\|_{\ell^2(\mathbb F_p)}^2\); for \(u<v\), the two orientations yield \(4\|g_{r,u}*g_{r,v}\|_{\ell^2(\mathbb F_p)}^2\). Carry shifts merely permute convolution coordinates. Summing gives the exact identity
\[
\begin{aligned}
\|Tf\|_4^4={}&4\sum_{r<s}m_rm_s\\
&+\sum_r\left(\sum_u\|g_{r,u}*g_{r,u}\|_2^2
+4\sum_{u<v}\|g_{r,u}*g_{r,v}\|_2^2\right),
\end{aligned}
\]
where convolution on \(\mathbb F_p\) is unnormalized.

**Step 3 (small Fourier transform).** Parseval and the convolution theorem on \(\mathbb F_p\) imply
\[
\|g_{r,u}*g_{r,v}\|_2^2=\frac1p\sum_{\xi} A_{r,u}(\xi)A_{r,v}(\xi).
\]
Therefore, writing \(E_r\) for the parenthesized energy of coarse class \(r\),
\[
E_r=\frac1p\sum_{\xi}\left(2S_r(\xi)^2-\sum_u A_{r,u}(\xi)^2\right).
\]
Subtract this expression from \((2p-1)m_r^2=(2p-1)p^{-2}(\sum_\xi S_r(\xi))^2\). Rearrangement yields
\[
(2p-1)m_r^2-E_r
=\frac{2p-1}{p^2}\sum_{\xi\ne\eta}S_r(\xi)S_r(\eta)
+\frac1p\sum_{\xi}\left(\sum_u A_{r,u}(\xi)^2-\frac{S_r(\xi)^2}p\right).
\]
Combining with \(\|f\|_2^4=(\sum_r m_r)^2\) proves the displayed three-part deficit identity.

**Step 4 (nonnegativity, sharpness, and all equality cases).** The coarse-class term is nonnegative because \(4p-6>0\); the different-frequency term is nonnegative because each \(S_r(\xi)\ge0\); the block term is \(\frac1p\sum_{r,\xi,u}(A_{r,u}(\xi)-S_r(\xi)/p)^2\). Equality for nonzero \(f\) forces exactly one \(m_r\) to be positive. On that class it forces a unique nonzero \(S_r(\xi)\), and then equality of the \(p\) nonnegative numbers \(A_{r,u}(\xi)\). Fourier inversion gives \(g_{r,u}(\ell)=c_u e^{2\pi i\xi\ell/p}\) with all \(|c_u|\) equal and nonzero. Conversely, these functions make all three deficits zero. They give the constant \(2p-1\), proving optimality and the complete classification. Distinct \((r,\xi)\) components are disjoint, and their \(p\) free coefficient phases modulo global phase form \((S^1)^{p-1}\).

## Verification

The standalone script `artifacts/verify.py` recomputes the full two-coordinate pair-sum fibers using Gaussian-integer arithmetic. It compares them exactly with the derived block-convolution identity, tests the sharp inequality and equality packets at primes \(3,5,7\), and numerically cross-checks the displayed frequency-side deficit for random complex integer inputs. Executing `python3 artifacts/verify.py` produced:

`VERIFY_OK Gaussian_integer_fiber_cases=23 exact_extremizer_packets=15 strict_nonextremizers=3 spectral_deficit_checks=23`

The finite checks test the implementation and representative cases; the proof of the statement for all odd primes is the preceding algebraic argument.

## Relationship to prior work

Mockenhaupt and Tao initiated finite-field restriction theory and its character-orthogonality framework [1]. Hickman and Wright introduced systematic restriction theory and wave-packet descriptions over residue-class rings, but their statements concern ranges of exponents and qualitative or uniform estimates, not the exact finite-modulus fourth-power constant and complete equality set here [2]. González-Riquelme and Oliveira e Silva obtained sharp finite-*field* extension inequalities for different surfaces and normalizations; their base rings have no nilpotent elements [3]. The current computation uses two adjacent nilpotent scales and produces a distinct family of arbitrary middle-digit phases. Generic wave-packet constructions give candidates but not the necessity or the exact deficit identity.

## Limitations

The theorem concerns the modulus \(p^3\), with \(p\) an odd prime, and the specific quadratic graph with input counting measure and output normalized averaging. It does not assert a corresponding sharp constant for \(p=2\), higher prime powers, arbitrary quadratic forms, or other \(L^q\) exponents. It does not claim an optimal global distance-to-extremizers stability coefficient. An equivalent rephrasing in earlier congruence-energy or local harmonic-analysis literature remains a potential priority risk.

## References

[1] G. Mockenhaupt and T. Tao, *Restriction and Kakeya phenomena for finite fields*, arXiv:math/0204234, first posted 2002-04-18. https://arxiv.org/abs/math/0204234

[2] J. Hickman and J. Wright, *The Fourier Restriction and Kakeya Problems over Rings of Integers Modulo N*, arXiv:1801.03176, 2018. https://arxiv.org/abs/1801.03176

[3] C. González-Riquelme and D. Oliveira e Silva, *Sharp extension inequalities on finite fields*, arXiv:2405.16647, 2024. https://arxiv.org/abs/2405.16647
