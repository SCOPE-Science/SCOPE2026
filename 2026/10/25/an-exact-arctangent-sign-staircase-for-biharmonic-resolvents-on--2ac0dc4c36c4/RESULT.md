# An exact arctangent sign staircase for biharmonic resolvents on Boolean cubes

## Finding
For the fourth-order resolvent on the Boolean cube, the antipodal Green function changes sign exactly \(\lfloor d/2\rfloor\) times as the regularization parameter varies. These crossings have a one-dimensional monotone phase characterization, and the final crossing grows on a squared-logarithmic dimension scale.

**Theorem.** Let \(d\ge2\) be an integer and let \(Q_d\) have vertex set \(\{0,1\}^d\). Write \(L_d=dI-A_d\) for its unnormalized graph Laplacian, and \(R_d(t)=(I+tL_d^2)^{-1}\) for \(t>0\). For any antipodal vertices \(x,\bar x\), define
\[
a=\frac1{2\sqrt t},\qquad \Theta_d(a)=\sum_{j=1}^d\arctan\!\left(\frac aj\right).
\]
Then
\[
2^dR_d(t)_{x,\bar x}
=\left(\prod_{j=1}^d\frac{j}{\sqrt{j^2+a^2}}\right)\cos\Theta_d(a).
\]
For each integer \(m\) satisfying \(0\le m<\lfloor d/2\rfloor\), there is exactly one \(a_m>0\) satisfying
\[
\Theta_d(a_m)=\left(m+\frac12\right)\pi.
\]
These are all the positive zeros: the corresponding \(t_m=1/(4a_m^2)\) are strictly decreasing in \(m\), each is simple, and the antipodal kernel alternates sign across them. In particular, its largest zero \(T_d=t_0\) is followed by a strictly positive antipodal response for all larger \(t\), while the response is strictly negative for \(t<T_d\) sufficiently close to \(T_d\).

Writing \(H_d=\sum_{j=1}^d1/j\) and \(H_d^{(3)}=\sum_{j=1}^dj^{-3}\),
\[
T_d=\frac{H_d^2}{\pi^2}-\frac{H_d^{(3)}}{6H_d}+O(H_d^{-3})\qquad(d\to\infty).
\]
In particular, \(T_d\sim(\log d)^2/\pi^2\). The number of antipodal sign reversals grows unboundedly with dimension even though the last crossing occurs at a finite parameter for every fixed cube.

## Assumptions and scope
The vertex inner product is the standard counting inner product; graph edges have unit weight; \(L_d\) is not divided by the degree. The operator \(R_d(t)\) is an invertible, self-adjoint, constant-preserving matrix for every \(t>0\). Positivity refers to the single entry joining vertices at Hamming distance \(d\), not to all matrix entries. The zero count includes only finite strictly positive parameters \(t\); the endpoint \(t=0\), where the off-diagonal entry is zero, is excluded. Every formula holds for every integer \(d\ge2\) and every \(t>0\).

## Proof
**1. Fourier diagonalization.** Each Walsh character \(\chi_S(x)=(-1)^{\sum_{j\in S}x_j}\) has \(L_d\chi_S=2|S|\chi_S\). At antipodes \(x,\bar x\), \(\chi_S(x)\chi_S(\bar x)=(-1)^{|S|}\). Hence the resolvent entry is exactly
\[
2^dR_d(t)_{x,\bar x}=\sum_{k=0}^d\frac{(-1)^k\binom dk}{1+4tk^2}=a^2\sum_{k=0}^d\frac{(-1)^k\binom dk}{k^2+a^2}.
\]
**2. A rational partial-fraction identity.** For \(z\notin\{0,-1,\ldots,-d\}\), direct partial fractions of the rational function \(d!/[z(z+1)\cdots(z+d)]\) give
\[
\sum_{k=0}^d\frac{(-1)^k\binom dk}{z+k}=\frac{d!}{\prod_{j=0}^d(z+j)}.
\]
Indeed the residue at \(z=-k\) of the right side is \(d!/[(-1)^k k!(d-k)!]=(-1)^k\binom dk\), and the difference has no poles and vanishes at infinity. Use \(1/(k^2+a^2)=[1/(k-ia)-1/(k+ia)]/(2ia)\), with \(i^2=-1\). Denote \(S(a)=\sum_k(-1)^k\binom dk/(k+ia)\). Then the antipodal sum is \(-a\operatorname{Im}S(a)\). The partial-fraction identity yields
\[
S(a)=\frac{d!}{ia\prod_{j=1}^d(j+ia)}
=\frac{d!}{a\prod_{j=1}^d\sqrt{j^2+a^2}}\exp\!\left[-i\left(\frac\pi2+\Theta_d(a)\right)\right].
\]
Taking the imaginary part proves the asserted product-and-cosine formula, including its positive prefactor.

**3. Every zero and its multiplicity.** We have \(\Theta_d'(a)=\sum_{j=1}^dj/(j^2+a^2)>0\), and \(\Theta_d(a)\) increases continuously from \(0\) to \(d\pi/2\) as \(a\) increases from \(0\) to infinity. Thus \(\cos\Theta_d(a)=0\) at exactly the phase levels \((m+1/2)\pi<d\pi/2\), namely \(m=0,\ldots,\lfloor d/2\rfloor-1\). At each root the derivative \(-\sin\Theta_d(a)\Theta_d'(a)\) is nonzero; the positive prefactor also cannot vanish. Since \(a\mapsto t=1/(4a^2)\) is a smooth decreasing bijection, all corresponding finite positive \(t\)-zeros are simple. The sign alternation and large-\(t\) positivity follow immediately.

**4. Final crossing asymptotics.** Put \(p=\pi/2\) and \(H=H_d\). The smallest phase root \(a_0\) solves \(\Theta_d(a_0)=p\). As \(d\to\infty\), comparison of \(\arctan u\) with \(u\) shows \(a_0\sim p/H\) and in particular \(a_0=O(H^{-1})\). Taylor's formula, with a remainder bounded by a constant multiple of \(a_0^5\sum_jj^{-5}\), gives
\[
p=Ha_0-\frac{H_d^{(3)}}3a_0^3+O(a_0^5).
\]
Solving this identity iteratively yields \(a_0=p/H+H_d^{(3)}p^3/(3H^4)+O(H^{-6})\); the sums \(H_d^{(3)}\) and \(\sum_jj^{-5}\) are uniformly bounded. Expanding \(T_d=1/(4a_0^2)\) gives
\[
T_d=\frac{H^2}{4p^2}-\frac{H_d^{(3)}}{6H}+O(H^{-3})
=\frac{H^2}{\pi^2}-\frac{H_d^{(3)}}{6H}+O(H^{-3}).
\]
Since \(H_d=\log d+\gamma+o(1)\), the leading squared-logarithmic law follows.

## Verification
The accompanying `check.py` performs direct resolvent-matrix inversions on cubes through dimension six, matches the rational Walsh spectral sum and the trigonometric product, and checks all predicted root levels and sign reversals for dimensions two through eighty. It also tests the leading asymptotic error against the claimed order. It reports **5,099 passed assertions**. These finite checks are diagnostics; the proof is given above for all dimensions.

## Relationship to prior work
Daners, Glück and Kennedy (2015 preprint, published 2016) develop qualitative theory of eventual positivity for semigroups and fourth-order generators. Their finite-dimensional analysis does not assert the exact antipodal sign count, rational-resolvent phase identity, or squared-logarithmic final-crossing law for Boolean cubes. Gazzola and Grunau (2007 online publication) study eventual local positivity for a biharmonic heat equation on Euclidean space, with different spatial and operator settings. Earlier hypercube results for the *exponential* \(e^{-tL_d^2}\) characterize heat-flow positivity, not the resolvent \((I+tL_d^2)^{-1}\); the latter is a Laplace mixture of heat operators, and its multiple antipodal sign reversals do not follow from the earlier heat positivity-threshold statement. A separate finite-cycle *resolvent* result concerns periodic geometry and does not determine the Boolean-cube binomial phase.

## Limitations
This theorem does **not** characterize entrywise positivity of the complete resolvent matrix, its endpoint operator norm, or any entry other than antipodal ones. Therefore \(T_d\) is a necessary lower bound for any eventual full-matrix positivity cutoff, not an asserted exact full-matrix cutoff. The bibliographic comparison is not an independent priority certification; equivalent formulas under different Green-function terminology remain possible.

## References
1. D. Daners, J. Glück and J. B. Kennedy, *Eventually and asymptotically positive semigroups on Banach lattices*, preprint arXiv:1511.05294v1, first public 2015-11-17; journal version, *Journal of Differential Equations* 261 (2016), 2607–2649. https://arxiv.org/abs/1511.05294
2. F. Gazzola and H.-C. Grunau, *Eventual local positivity for a biharmonic heat equation in* \(\mathbb R^N\), *Discrete and Continuous Dynamical Systems Series S* 1 (2008), 83–87, online December 2007. https://doi.org/10.3934/dcdss.2008.1.83
