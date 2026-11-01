# Exact sign memory and vanishing diffusion in a fixed-point-free four-branch family

## Finding

For each integer \(k\ge3\), define \(T_k:[-k,k]\to[-k,k]\), up to the immaterial assignment of interval-boundary values, by
\[
T_k(x)=\begin{cases}
(x+1)/(k-1),&-k\le x\le-1,\\
k(x+1),&-1<x<0,\\
k(x-1),&0\le x<1,\\
(x-1)/(k-1),&1\le x\le k.
\end{cases}
\]
This is a subfamily of the fixed-point-free maps of García-Grimaldo and Campos-Cantón. Set \(I_A=[-k,-1)\), \(I_B=[-1,0)\), \(I_C=[0,1)\), and \(I_D=[1,k]\). Then the probability density
\[
\rho_k(x)=\frac{1}{2(2k-1)}\begin{cases}
1,&x\in I_A\cup I_D,\\
k,&x\in I_B\cup I_C
\end{cases}
\]
is invariant under \(T_k\). With initial state distributed according to this density, the cell process \(Q_n\in\{A,B,C,D\}\) is a stationary, irreducible, aperiodic **first-order Markov chain** with transition matrix and stationary law
\[
P_k=\begin{pmatrix}
0&1&0&0\\
0&0&1/k&(k-1)/k\\
(k-1)/k&1/k&0&0\\
0&0&1&0
\end{pmatrix},\qquad
\pi_k=\frac{(k-1,k,k,k-1)}{2(2k-1)}.
\]
The partition is generating modulo the invariant density, so this invariant dynamical system is mixing.

For the sign observable \(s(x)=-1\) on \(I_A\cup I_B\), \(s(x)=+1\) on \(I_C\cup I_D\), write \(C_n=\mathbb{E}_{\rho_k}[s(X_0)s(X_n)]\). It has mean zero and the **complete exact covariance generating function**
\[
\boxed{\sum_{n=0}^{\infty}C_n z^n
=\frac{k(2k-1)+(k-1)z}{(2k-1)[k+z+(k-1)z^2]}}
\quad (|z|<1).
\]
In particular, \(C_0=1\), \(C_1=-1/(2k-1)\), \(C_2=-(2k-3)/(2k-1)\), and
\[
\boxed{\lim_{N\to\infty}\frac1N\operatorname{Var}\!\left(\sum_{j=0}^{N-1}s(X_j)\right)
=\frac{k-1}{k(2k-1)}},
\qquad
\boxed{\frac{1}{\sqrt N}\sum_{j=0}^{N-1}s(X_j)
\Longrightarrow\mathcal N\!\left(0,\frac{k-1}{k(2k-1)}\right)}.
\]
The nontrivial Markov eigenvalues are \(-(k-1)/k\) and the roots of \(k\lambda^2+\lambda+k-1=0\). Their maximal modulus is \(\sqrt{(k-1)/k}\), which tends to one as \(k\to\infty\), even as the sign-diffusion coefficient tends to zero like \(1/(2k)\). Thus the exact sign diffusion becomes small while the symbolic mixing rate becomes slow.

## Assumptions and scope

The integer parameter obeys \(k\ge3\); the initial law is precisely \(\rho_k(x)\,dx\). Assertions involving itineraries, derivatives, and signs are modulo the countable set of branch boundaries and their iterated preimages, which has zero invariant measure. The central slope is \(k\) and the outer slope is \(1/(k-1)\), the natural Markov-alignment relation \((k-1)\cdot(1/(k-1))=1\). This differs from the reciprocal-slope subfamily with outer slope \(1/k\).

The original four-branch family has dimensionful inner breakpoint \(a=b_1/m_1\) and domain endpoint \(b_2=m_2a\); rescaling by \(x/a\) and taking \(m_2=k\), \(m_1=1/(k-1)\) gives the displayed map. The result is about the stated exact subfamily, not all slope pairs, arbitrary starting measures, or all real-valued observables.

## Proof

**1. Exact Markov structure and stationary measure.** The four affine branch images, ignoring measure-zero endpoint conventions, are \(T(I_A)=I_B\), \(T(I_B)=I_C\cup I_D\), \(T(I_C)=I_A\cup I_B\), and \(T(I_D)=I_C\). Their lengths are \(k-1,1,1,k-1\), respectively. On a source cell with a uniform conditional law, its image is uniform; when conditioned on a target cell it remains uniform on that entire target cell. Therefore induction over every admissible past word proves the *full* Markov property of the cell process, not just its one-step marginals. Taking fractions of image lengths gives \(P_k\) above. Direct multiplication gives \(\pi_kP_k=\pi_k\), and dividing each stationary cell mass by its cell length produces \(\rho_k\); hence \(T_k\) preserves this probability.

The directed graph is irreducible; the return words \(B\to C\to B\) and \(B\to D\to C\to B\) have lengths two and three and positive probability. Thus \(P_k\) is primitive and the stationary cell chain mixes. Along every branch-regular itinerary, no two consecutive map branches can both be outer branches. Consequently for every regular two-step itinerary, \(|(T_k^2)'|\ge k/(k-1)>1\). All \(n\)-cylinder diameters tend uniformly to zero by the two-step expansion (each cylinder is an affine monotonicity interval of an iterate), so the four-cell partition is generating almost everywhere. Mixing of the stationary chain therefore extends to the interval transformation.

**2. Exact covariance and spectrum.** Set \(f=(-1,-1,1,1)^{\mathsf T}\), \(W=\operatorname{diag}(\pi_k)\). Then \(\pi_k f=0\) and \(C_n=f^{\mathsf T}WP_k^n f\). Direct elimination of the four-by-four resolvent gives
\[
f^{\mathsf T}W(I-zP_k)^{-1}f
=\frac{k(2k-1)+(k-1)z}{(2k-1)[k+z+(k-1)z^2]},
\]
initially for \(|z|<1\). Similarly, direct determinant expansion gives
\[
\det(\lambda I-P_k)=\frac{(\lambda-1)(k\lambda+k-1)(k\lambda^2+\lambda+k-1)}{k^2}.
\]
For \(k\ge3\), the quadratic roots are nonreal conjugates of absolute value \(\sqrt{(k-1)/k}<1\); the other nontrivial eigenvalue has smaller modulus \((k-1)/k\). Hence all covariance sums converge absolutely. Evaluating the displayed generating function at \(z=1\) yields \(G_k(1)=(2k^2-1)/(2k(2k-1))\), and therefore the Green–Kubo variance \(C_0+2\sum_{n\ge1}C_n=2G_k(1)-1=(k-1)/[k(2k-1)]\).

**3. Central limit theorem.** The explicit centered Poisson solution
\[
h=\frac{1}{2k}(-2k-1,-1,1,2k+1)^{\mathsf T}
\]
satisfies \((I-P_k)h=f\) and \(\pi_k h=0\). For the stationary chain let \(D_{j+1}=h(Q_{j+1})-(P_kh)(Q_j)\). Then \(D_{j+1}\) are bounded martingale differences and
\[
\sum_{j=0}^{N-1}f(Q_j)=h(Q_0)-h(Q_N)+\sum_{j=0}^{N-1}D_{j+1}.
\]
The stationary ergodic theorem applied to their conditional variances gives the limit
\[
\sum_i\pi_i\big((P_k h^2)_i-((P_kh)_i)^2\big)
=\sum_i\pi_i\big(h_i^2-((P_kh)_i)^2\big)
=\frac{k-1}{k(2k-1)}>0.
\]
Bounded martingale increments satisfy the Lindeberg condition; the martingale central limit theorem and bounded endpoint correction establish the claimed Gaussian limit. Absolute covariance summability also gives the asymptotic variance through \(\operatorname{Var}(\sum_{j<N}f(Q_j))=NC_0+2\sum_{n=1}^{N-1}(N-n)C_n\).

## Verification

Run `python verification.py` with `sympy`. The included exact verifier checks the four images, normalization, stationary matrix equation, characteristic polynomial, covariance resolvent, Green–Kubo and Poisson/martingale variance identities symbolically. It also evaluates 48 integer parameter values from 3 through 50 using rational arithmetic; each tests primitivity and the first 15 covariance coefficients, totalling 720 exact coefficient comparisons. All checks passed. Universal conclusions rest on the proof above, not on finitely many parameter tests.

## Relationship to prior work

García-Grimaldo and Campos-Cantón introduced this four-branch fixed-point-free family and studied fixed-point exclusion, Lyapunov exponents, and chaotic examples [1]. García-Grimaldo and collaborators reproduced its formula and examined numerical bifurcation behavior and hardware realization [2]. Both definitions and the fixed-point-free property are credited. This note adds the all-integer Markov-alignment subfamily, its normalized stationary density, exact full sign-memory generating function, and Gaussian diffusion law. The 2023 full text [2] was inspected for the same map, including its dynamical-analysis section; it does not state these exact conclusions. The full original 2021 article [1] could not be read beyond its publisher preview, so an unexamined equivalent result remains a residual priority risk. Work on constructing maps with prescribed piecewise-constant stationary densities [3] does not give the exact sign autocorrelation and shrinking diffusion for this fixed-point-free family. In the reciprocal-slope slice \(m_1=1/k\) the dynamics can instead be eventually periodic, so that slice does not imply the present stationary mixing statistics.

## Limitations

These formulas apply to the indicated invariant absolutely continuous probability and the central/outer Markov-aligned integer slice. They do not classify all invariant Borel probabilities, all other parameters, or other observables. The strong mixing statement is with respect to this invariant probability, not for every initial condition. Some boundary orbits are periodic and have different statistics. This is an analytical result with exact finite-parameter checks, not an independent mathematical certification. The original 2021 full text was not available for whole-paper priority comparison.

## References

[1] C. García-Grimaldo and E. Campos-Cantón, *Chaotic Features of a Class of Discrete Maps without Fixed Points*, International Journal of Bifurcation and Chaos **31** (2021), 2150200. DOI: 10.1142/S021812742150200X. First verified public source date: 2021-10-26 (MaRDI record).

[2] C. García-Grimaldo, C. F. Bermúdez-Márquez, E. Tlelo-Cuautle, and E. Campos-Cantón, *FPGA Implementation of a Chaotic Map with No Fixed Point*, Electronics **12** (2023), 444. DOI: 10.3390/electronics12020444.

[3] Z. Wang, J. Ding, and N. Rhee, *Piecewise Monotonic Maps with a Common Piecewise Constant Stationary Density*, Journal of Statistical Physics (2023). DOI: 10.1007/s10955-023-03143-1.
