# A sharp adsorption-allocation reversal and an exact iso-gap surface in a five-state diffusion chain

## Finding

For a reversible five-state continuous-time diffusion-and-adsorption chain with a fixed total surface adsorption rate, the allocation that most rapidly relaxes to equilibrium changes at one explicit interior storage capacity. Equal coating is uniquely **slowest** below this capacity, uniquely **fastest** above it, and **every positive coating split gives precisely the same spectral gap** at the threshold.

Precisely, take any total adsorption intensity \(B>0\), common desorption rate \(d>0\), and central storage capacity \(M>0\). The left and right adsorption rates obey \(a,b>0\) and \(a+b=B\). Set

\[
\ell=\frac{2+2d+B-\sqrt{(2+2d+B)^2-16d}}4,
\qquad M_c=\frac2\ell.
\]

Let \(\lambda(a,b;M,d)\) be the smallest positive eigenvalue of the negative Markov generator, i.e. its reversible \(L^2\) relaxation rate. Then:

1. If \(0<M<M_c\), \(\lambda\) increases strictly with \(|a-b|\). Equal allocation \(a=b=B/2\) uniquely **minimizes** the gap.
2. If \(M>M_c\), \(\lambda\) decreases strictly with \(|a-b|\). Equal allocation uniquely **maximizes** the gap.
3. If \(M=M_c\), \(\lambda(a,B-a;M_c,d)=\ell\) for every \(0<a<B\). The gap is completely independent of allocation.

The exact transition value also has the equivalent expression

\[
M_c=\frac{2+2d+B+\sqrt{(2+2d+B)^2-16d}}{2d}.
\]

At equal allocation, the gap is \(\ell\) for **all** \(M>0\). The change of optimizer therefore reflects how unequal coating couples the slow antisymmetric mode to the central storage compartment, not a shift in the equal-coating gap.

## Assumptions and scope

The five states, in path order, are a left adsorbed state \(0\), three bulk states \(1,2,3\), and a right adsorbed state \(4\). All parameters \(a,b,d,M\) are finite and strictly positive. The nonzero transition rates are

\[
q_{01}=q_{43}=d,\quad q_{10}=a,\quad q_{34}=b,\quad
q_{12}=q_{32}=1,\quad q_{21}=q_{23}=M^{-1}.
\]

There are no jumps between nonadjacent states. A central capacity \(M\) changes both departures from the middle compartment and its equilibrium mass; the two neighbouring bulk compartments have unit capacity and unit connecting conductance. The stationary reversible weights, prior to normalization, are

\[
\mu=(a/d,\,1,\,M,\,1,\,b/d),
\]

whose sum \(2+M+B/d\) does not depend on the adsorption split. The four edge conductances are \((a,1,1,b)\). Thus the generalised graph-Laplacian problem is

\[
Kf=\lambda Wf,\qquad W=\operatorname{diag}(\mu),
\]

with \(K\) the conductance Laplacian of this weighted path. Reversibility makes all five eigenvalues real; connectedness makes the zero eigenvalue simple. The theorem is for the *first positive* eigenvalue, not for every eigenvalue or the full mixing-time profile.

## Proof

**Step 1: spectral reduction and the range of the gap.** For functions of weighted mean zero, the Rayleigh quotient is

\[
\mathcal R(f)=\frac{a(f_0-f_1)^2+(f_1-f_2)^2+(f_2-f_3)^2+b(f_3-f_4)^2}{(a/d)f_0^2+f_1^2+Mf_2^2+f_3^2+(b/d)f_4^2}.
\]

Choose a nonzero test function supported at states \(0,4\), with \((a/d)f_0+(b/d)f_4=0\). Its quotient is exactly \(d\), so the gap does not exceed \(d\). Strict inequality follows because this test function is not an eigenvector: its bulk equations would require both \(af_0=0\) and \(bf_4=0\), contrary to nonzero support. By the equality condition for the smallest Rayleigh quotient on the orthogonal complement of constants,

\[
0<\lambda_1<d.
\]

For \(0<\lambda<d\), the equations on states \(0,4\) yield

\[
f_0=\frac{d}{d-\lambda}f_1,\qquad f_4=\frac{d}{d-\lambda}f_3.
\]

Eliminating these variables gives a three-by-three symmetric system for \((f_1,f_2,f_3)\):

\[
\begin{pmatrix}
1-\lambda-\gamma a&-1&0\\
-1&2-M\lambda&-1\\
0&-1&1-\lambda-\gamma b
\end{pmatrix}
\begin{pmatrix}f_1\\f_2\\f_3\end{pmatrix}=0,
\qquad \gamma=\frac{\lambda}{d-\lambda}.
\]

Put \(P=ab\) while holding \(B=a+b\) fixed. Its determinant is

\[
F(\lambda,P)=(2-M\lambda)\big[(1-\lambda)^2-\gamma B(1-\lambda)+\gamma^2P\big]
-\big[2(1-\lambda)-\gamma B\big].
\tag{1}
\]

For \(0<\lambda<d\), the roots of \(F\) are exactly the eigenvalues of the five-state problem in that interval. Moreover,

\[
F(0,P)=0,\qquad \partial_\lambda F(0,P)=-(M+2+B/d)<0.
\]

The symmetric weighted path is an irreducible Jacobi eigenproblem, so all its eigenvalues are simple. Consequently the first positive root \(\lambda_1\) of \(F\) is crossed from negative to positive, and \(\partial_\lambda F(\lambda_1,P)>0\).

**Step 2: an allocation-invariant balanced eigenmode.** At \(a=b=B/2\), take the antisymmetric vector \(f=(h,1,0,-1,-h)\). The end-state equations give \(h=d/(d-\lambda)\), while the first bulk equation becomes

\[
(1-\lambda)(d-\lambda)=\frac{B\lambda}{2}.
\tag{2}
\]

There is exactly one root \(\ell\) of (2) in \((0,\min\{1,d\})\): the left side is strictly decreasing there and the right side strictly increasing. The displayed quadratic formula for \(\ell\) follows. This eigenvector has exactly one sign change along the path (ignoring its zero middle coordinate); the discrete Sturm oscillation theorem identifies it as the first positive eigenmode. Therefore

\[
\lambda(B/2,B/2;M,d)=\ell
\quad\text{for every }M>0.
\tag{3}
\]

**Step 3: exact critical plateau.** Define \(M_c=2/\ell\). At \(\lambda=\ell\), (2) is equivalent to \(2(1-\ell)=\gamma B\). At \(M=M_c\), both the factor \(2-M\ell\) and the final bracket of (1) vanish. Thus \(F(\ell,P)=0\) for *all* \(0<P\le B^2/4\). To verify directly that this eigenvalue remains the gap, set \(f_1=1\), \(f_3=-1\),

\[
f_2=1-\ell-\gamma a=\gamma b-(1-\ell),\qquad
f_0=\frac d{d-\ell},\qquad f_4=-\frac d{d-\ell}.
\]

The three bulk equations and both surface equations hold. Since \(f_0,f_1>0\) and \(f_3,f_4<0\), this vector has exactly one sign change regardless of the sign of \(f_2\); Sturm oscillation makes it the first positive eigenvector. Hence \(\lambda_1=\ell\) for every positive split at \(M_c\).

**Step 4: strict monotonicity and orientation.** Differentiating (1) at its simple first positive root gives

\[
\frac{\partial\lambda_1}{\partial P}
=-\frac{(2-M\lambda_1)\gamma(\lambda_1)^2}{\partial_\lambda F(\lambda_1,P)}.
\tag{4}
\]

The denominator is strictly positive. For fixed \(M\ne M_c\), the factor \(2-M\lambda_1\) cannot vanish at any allocation: if it did, (1) would force \(2(1-\lambda_1)=\gamma B\), whose only solution in \((0,d)\) is \(\lambda_1=\ell\), hence \(M=2/\ell=M_c\), a contradiction. Therefore its sign is constant as the split varies. At the balanced split, (3) makes that sign equal to the sign of \(2-M\ell\). Finally

\[
P=\frac{B^2-(a-b)^2}{4}
\]

strictly decreases with \(|a-b|\). Equation (4) now proves both strict monotonicity directions and uniqueness of the balanced extremum. Together with Step 3 this proves all three alternatives. \(\square\)

## Verification

The standalone `gap_phase_checker.py` independently constructs the five-by-five weighted Laplacian and solves its generalized symmetric eigenproblem. It checks the full five-state determinant identity symbolically with SymPy and checks the secular equation, all three allocation regimes over randomized physically admissible parameters, the balanced-gap formula, and the entire critical iso-gap curve at six widely separated parameter pairs. Run `python3 gap_phase_checker.py` with NumPy, SciPy and SymPy. A successful tested execution completed 4,106 individual matrix/secular and phase comparisons. The proof above, not these finite checks, establishes the theorem for all positive parameters.

For orientation, at \(B=1\), \(d=3\), the balanced rate is \(\ell\simeq0.8138593384\) and the critical capacity is \(M_c\simeq2.4574271078\). Moving from equal rates to the split \((a,b)=(0.1,0.9)\) raises the gap when \(M=1\), lowers it when \(M=5\), and leaves it fixed at \(M=M_c\).

## Relationship to prior work

Levesque, Bénichou and Rotenberg (2012) developed diffusion between adsorbing and desorbing walls and its time-dependent transport observables. Bou-Rabee and Holmes-Cerfon (2019) developed sticky boundary diffusions and Markov-jump approximations. Castillo and Zaballa (2019) studied general eigenvalue dependence in birth–death matrices, including cases where familiar monotonicity criteria fail. The present result addresses a different joint question: at fixed *total* adsorption intensity with a variable central storage capacity, which coating allocation optimizes the **reversible relaxation spectral gap**, and when is that gap exactly allocation-invariant? The general Jacobi framework supports the spectral arguments, but does not itself assert the explicit model-specific three-regime criterion. The original wall-diffusion paper was not fully accessible for comparison, so historical priority is not guaranteed.

## Limitations

The conclusion applies only to the specified irreducible five-state reversible chain with a common desorption rate and exactly three bulk compartments, two of which have unit capacity. It makes no assertion for continuum geometries, additional compartments, asymmetric bulk rates, variable desorption, one-sided limiting rates equal to zero, total-variation mixing times, or all higher spectral modes. A microscopic continuum derivation of this compartment coarse graining and robust noisy-parameter inference are not proved. Priority remains uncertain owing to incomplete access to one relevant original article and the possibility of unrecognized special cases in general tridiagonal spectral literature.

## References

1. M. Levesque, O. Bénichou, B. Rotenberg, *Molecular diffusion between walls with adsorption and desorption*, arXiv:1212.6547 (first submitted 2012-12-28); *J. Chem. Phys.* **138**, 034107 (2013), DOI 10.1063/1.4775742.
2. N. Bou-Rabee, M. C. Holmes-Cerfon, *Sticky Brownian Motion and its Numerical Solution*, arXiv:1906.06803 (2019).
3. K. Castillo, I. Zaballa, *On variation of eigenvalues of birth and death matrices and random walk matrices*, arXiv:1906.08644 (2019).
