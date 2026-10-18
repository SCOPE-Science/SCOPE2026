# Fastest mixing among two-periodic chains on even cycles

## Finding

For every even integer \(N\ge4\), consider nearest-neighbor, doubly stochastic Markov chains on the cycle \(C_N\) whose symmetric edge-transition rates alternate between two values and whose antisymmetric circulation is constant. Among **all** such two-periodic chains, the smallest nonstationary eigenvalue modulus is
\[
\rho_N^*=\frac{1+\cos(2\pi/N)}{3-\cos(2\pi/N)}.
\]
It is attained by the homogeneous reversible chain with every neighbor-transition probability
\[
q_N^*=\frac{1}{3-\cos(2\pi/N)}
\]
and every holding probability \(1-2q_N^*\).

For \(N\ge6\), this is the **unique** optimal chain in the stated two-periodic class. For \(N=4\), the complete optimal family instead satisfies
\[
a+b=\frac23,\qquad (a-b)^2=4r^2.
\]
In particular, \(a=5/12\), \(b=1/4\), \(r=1/12\) gives a nonreversible, inhomogeneous optimal chain with nonstationary eigenvalues \(-1/3,1/3,1/3\). Its repeated eigenvalue \(1/3\) has a nontrivial Jordan block. Thus optimal asymptotic eigenvalue modulus does **not** require a reversible or diagonalizable transition matrix on the four-cycle.

## Assumptions and scope

Label the vertices by \(i\in\mathbb Z/N\mathbb Z\), with \(N=2m\ge4\). Write \(w_i=a\) when \(i\) is even and \(w_i=b\) when \(i\) is odd. The transition matrix is
\[
P_{i,i+1}=w_i+r,\qquad P_{i,i-1}=w_{i-1}-r,\qquad P_{ii}=1-a-b,
\]
with all other entries zero. Admissible parameters are precisely
\[
a,b\ge |r|,\qquad a+b\le1.
\]
These conditions make \(P\) nonnegative and both row- and column-stochastic. The oriented offset \(r\) is the same around every edge; \(r=0\) is the reversible case. The two-periodic assumption constrains the symmetric edge rates but does not remove the simultaneous occurrence of inhomogeneity and circulation.

Define the optimized quantity by \(\rho_\perp(P)=\rho(P|_{\mathbf1^\perp})\), the spectral radius on the invariant subspace orthogonal to the constant vector. This convention counts any additional eigenvalue \(1\) of a reducible chain, so it is defined even on the boundary of the parameter domain. The theorem concerns asymptotic spectral convergence, not a fixed-time total-variation mixing constant.

## Proof

Put \(c=a+b\), \(d=a-b\), and \(s=1-c\). Group the vertices as pairs \((2j,2j+1)\), indexed by \(j\in\mathbb Z/m\mathbb Z\). On the Fourier mode with \(z=e^{2\pi i k/m}\), the transition matrix reduces to
\[
B_k=\begin{pmatrix}
s&(a+r)+(b-r)z^{-1}\\
(a-r)+(b+r)z&s
\end{pmatrix},
\]
so its eigenvalues are \(s\pm\sqrt{Z_k}\), where
\[
Z_k=\bigl((a+r)+(b-r)z^{-1}\bigr)
\bigl((a-r)+(b+r)z\bigr).
\]
At \(k=0\), these are exactly \(1\) and \(1-2c\).

For \(N\ge6\), use \(k=1\) and put \(\theta=2\pi/N\in(0,\pi/2)\). Direct multiplication gives
\[
Z_1=X+Y+4irc\sin\theta\cos\theta,\qquad
X=c^2\cos^2\theta,\qquad Y=(d^2-4r^2)\sin^2\theta.
\]
The key **exact identity** is
\[
|Z_1|^2-(X-Y)^2=4Xd^2\sin^2\theta\ge0.
\]
Take the square root with nonnegative real part. Since
\[
\bigl(\operatorname{Re}\sqrt{Z_1}\bigr)^2
=\frac{|Z_1|+X+Y}{2}\ge X,
\]
one nonstationary eigenvalue has modulus at least
\[
|s+\sqrt{Z_1}|\ge s+c\cos\theta
=1-c(1-\cos\theta).
\]
Together with the \(k=0\) eigenvalue this yields
\[
\rho_\perp(P)\ge
\max\{1-c(1-\cos\theta),\ |1-2c|\}.
\]
For \(0\le c\le1\), the first expression decreases in \(c\) and the second branch relevant above \(1/2\) increases. Their unique minimax intersection is
\[
c_*=\frac{2}{3-\cos\theta},\qquad
\rho_N^*=\frac{1+\cos\theta}{3-\cos\theta}.
\]
The homogeneous reversible choice \(a=b=c_*/2\), \(r=0\) attains this bound: its nonstationary eigenvalues are \(1-c_*+c_*\cos(2\pi j/N)\), and their largest absolute values occur at the first nonconstant mode and the alternating mode.

The equality case is rigid for \(N\ge6\). If \(d\ne0\), the key identity is strict because \(X>0\) and \(\sin\theta>0\), making \(\operatorname{Re}\sqrt{Z_1}>c\cos\theta\). If \(d=0\) but \(r\ne0\), then \(\sqrt{Z_1}=c\cos\theta+2ir\sin\theta\), and \(|s+\sqrt{Z_1}|>s+c\cos\theta\). A value \(c\ne c_*\) makes the scalar minimax bound strict. Therefore only \(a=b=c_*/2\), \(r=0\) is optimal.

For \(N=4\), the only nonconstant Fourier block has \(z=-1\), so the three nonstationary eigenvalues are
\[
1-2c,\qquad 1-c\pm\sqrt{d^2-4r^2}.
\]
Since \(1-c\ge0\), the larger absolute modulus of the last two is at least \(1-c\), with equality exactly when \(d^2=4r^2\). Hence
\[
\rho_\perp(P)\ge\max\{|1-2c|,1-c\}\ge\frac13,
\]
with equality precisely for \(c=2/3\) and \(d^2=4r^2\). Admissibility then permits \(|r|\le1/6\) with either \(a=1/3+r,\ b=1/3-r\) or \(a=1/3-r,\ b=1/3+r\). When \(r\ne0\), the double \(1/3\) eigenvalue has geometric multiplicity one: in the two-dimensional Fourier block its nilpotent part is nonzero and squares to zero. This proves the claimed defective optimal equality family.

## Verification

Run `python verify.py` with Python, SymPy and NumPy installed. The included checker reconstructs four independent algebraic identities (including the four- and six-vertex characteristic polynomials and the critical square-root inequality), checks the nonnormal four-vertex witness exactly, and tests \(2275\) explicitly enumerated admissible rational-grid choices on cycles with \(4,6,8,10,12\) vertices. Its output is

`VERIFY_OK symbolic_identities=4 defective_four_cycle=1 finite_parameter_checks=2275`

Only the analytical Fourier argument proves the assertion for every even order and every admissible real parameter. The finite checks are corroborating, not an exhaustive search of the continuous feasible set.

## Relationship to prior work

Boyd, Diaconis and Xiao formulate fastest-mixing graph design as spectral-radius minimization in the **symmetric/reversible** setting [1]. Gerencsér, Hendrickx and Van Dooren [2] establish the homogeneous cycle benchmark; prove global non-improvement for inhomogeneity or circulation considered **separately**; and show local optimality under their combination. They describe unrestricted simultaneous inhomogeneity and nonreversibility as an open global comparison. The present statement supplies a **global** comparison only on the natural two-periodic mixed-perturbation subfamily, together with its sharp equality cases. It does not assert the unrestricted conjecture.

## Limitations

The theorem does not cover arbitrary edge-by-edge inhomogeneity, nonuniform stationary distributions, additional shortcuts, odd cycles, or time-varying transition matrices. Spectral-radius equality is not equality of finite-time mixing behavior: the defective four-cycle cases can acquire a polynomial prefactor in powers of the transition matrix. Historical priority of an equivalent two-periodic calculation has not been independently established.

## References

[1] S. Boyd, P. Diaconis and L. Xiao, *Fastest Mixing Markov Chain on a Graph*, SIAM Review 46 (2004), 667–689, DOI:10.1137/S0036144503423264. First electronically published 2004-10-29. https://web.stanford.edu/~boyd/papers/pdf/fmmc.pdf

[2] B. Gerencsér, J. Hendrickx and P. Van Dooren, *Spectral gap of Markov chains on a cycle*, European Control Conference (2015), 765–769, DOI:10.1109/ECC.2015.7330635. Lawful full text: https://real.mtak.hu/173919/1/cycle_spectral_gap.pdf
