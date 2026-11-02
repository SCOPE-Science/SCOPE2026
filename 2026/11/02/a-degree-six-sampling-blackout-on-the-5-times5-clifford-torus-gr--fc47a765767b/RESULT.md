# A degree-six sampling blackout on the \(5\times5\) Clifford-torus grid

## Finding

Let \(X\subset S^3\) be the 25-point Cartesian product of the fifth roots of unity on the equal-radius Clifford torus. The exact-degree spherical harmonic evaluation map \(E_\ell:\mathcal H_\ell(S^3)\to\mathbb C^{25}\) has ranks
\[
\operatorname{rank}E_\ell=\begin{cases}
1&\ell=0,\\
4&\ell=1,\\
8&\ell=2,\\
16&\ell=3,\\
21&\ell=4,\\
25&\ell=5,\\
24&\ell=6,\\
25&\ell\ge7.
\end{cases}
\]
In degree six the image consists **exactly** of the 24-dimensional subspace of sample data summing to zero. Hence exact-degree interpolation is possible at degree five, fails in precisely the constant-data direction at degree six, and is possible in every degree from seven onward. This nonmonotone defect occurs despite \(\dim\mathcal H_6(S^3)=49>25\).

## Assumptions and scope

Identify \(\mathbb R^4\) with \(\mathbb C^2\), and equip \(S^3\) with its standard round metric and surface measure of area \(2\pi^2\). Let \(\zeta=e^{2\pi i/5}\), and write
\[
X=\left\{\frac{(\zeta^j,\zeta^k)}{\sqrt2}:0\le j,k<5\right\}.
\]
The space \(\mathcal H_\ell(S^3)\) consists of restrictions of complex homogeneous harmonic polynomials of total degree exactly \(\ell\) on \(\mathbb R^4\), with its usual \(L^2(S^3)\) inner product. Evaluation is \((E_\ell f)_{j,k}=f((\zeta^j,\zeta^k)/\sqrt2)\). The result is not a statement about harmonics of degree at most \(\ell\), and makes no claim for arbitrary nearby sampling nodes.

## Proof

**Step 1 (Gram diagonalization).** The spherical addition formula in dimension four gives
\[
E_\ell E_\ell^*=\frac{\ell+1}{2\pi^2}\big[U_\ell(\langle x,y\rangle)\big]_{x,y\in X},
\]
where \(U_\ell\) is the Chebyshev polynomial of the second kind normalized by \(U_\ell(1)=\ell+1\), \(U_0(t)=1\), \(U_1(t)=2t\), and \(U_{\ell+1}(t)=2tU_\ell(t)-U_{\ell-1}(t)\). The positive prefactor does not affect rank. The matrix is circulant on \((\mathbb Z/5\mathbb Z)^2\) since
\[
\big\langle x_{j,k},x_{r,s}\big\rangle=
\tfrac12\left(\cos\tfrac{2\pi(j-r)}5+\cos\tfrac{2\pi(k-s)}5\right).
\]
Thus its 25 eigenvectors are the full two-dimensional discrete Fourier basis, indexed by \((u,v)\in\{0,\ldots,4\}^2\), with real eigenvalues
\[
\Lambda_{\ell;u,v}=\sum_{j,k=0}^4
U_\ell\!\left(\tfrac{\cos(2\pi j/5)+\cos(2\pi k/5)}2\right)
\cos\left(\tfrac{2\pi(uj+vk)}5\right).
\]
Their nonnegativity follows independently from the Gram representation. They lie in \(\mathbb Q(\sqrt5)\), since the only cosine values are \(1\), \((\sqrt5-1)/4\), and \(-(\sqrt5+1)/4\).

**Step 2 (complete finite spectral certificate).** The bundled `check.py` uses exact rational-pair arithmetic in \(\mathbb Q(\sqrt5)\), exact sign comparisons, and the three-term Chebyshev recurrence to compute all 25 eigenvalues for **every** integer degree \(0\le\ell\le47\), without floating-point rank decisions. It verifies that the ranks through degree six are \(1,4,8,16,21,25,24\), and that all degrees \(7\le\ell\le47\) have rank 25. In degree six the unique vanishing eigenvalue is Fourier index \((u,v)=(0,0)\). As extra exact consistency checks, at degree five the eigenvalue multiset is \(125/16\) (four times), \(125/8\) (four), \(225/32\) (four), \(25/8\) (five), and \(25/16\) (eight). At degree six it is \(0\) (once), \(125/16\) (four), \(25/64\) (four), \(725/64\) (four), \(75/16\) (four), and \(625/64\) (eight). These are the eigenvalues of the *unscaled* Chebyshev Gram matrix.

**Step 3 (analytic infinite tail).** For two distinct nodes \(x,y\), the geometry gives
\[
|\langle x,y\rangle|\le\frac{1+\sqrt5}{4}<\frac{\sqrt3}{2}.
\]
Writing \(\langle x,y\rangle=\cos\theta\), we therefore have \(\sin\theta>1/2\). The identity \(U_\ell(\cos\theta)=\sin((\ell+1)\theta)/\sin\theta\) implies \(|U_\ell(\langle x,y\rangle)|<2\) on every off-diagonal entry, while \(U_\ell(1)=\ell+1\). Hence each absolute off-diagonal row sum is strictly less than \(24\cdot2=48\). For every \(\ell\ge48\), the diagonal is at least 49; strict diagonal dominance of this real symmetric Gram matrix proves positive definiteness and rank 25. This completes the all-degree classification.

**Step 4 (interpretation of the defect).** The two-torus Fourier decomposition of degree-six spherical harmonics has character frequencies \((a,b)\) with \(|a|+|b|\le6\) and even total parity. Averaging over the fifth-root grid annihilates every nonzero residue pair modulo five. The only potentially surviving character is \((0,0)\), whose degree-six, torus-invariant mode is proportional to the Legendre polynomial \(P_3(\cos 2\eta)\) in the Hopf latitude \(\eta\). At the Clifford torus \(\eta=\pi/4\), this equals \(P_3(0)=0\). Thus every degree-six harmonic has zero grid sum. Step 2 shows no further independent sample identity, establishing the exact mean-zero image.

## Verification

Execute `python3 check.py` using Python 3.9 or later. It requires only the standard library. The script prints the ranks for degrees zero through seven and 47, tests exact eigenvalues and degree-six Fourier nullspace, and confirms all 25 eigenvalues for each of the 48 finite degrees. The bound in Step 3, not the finite test, handles infinitely many remaining degrees. This work includes no independent external validation.

## Relationship to prior work

Marzo and Pridhnani (2013, arXiv:1302.6730) prove general sampling/interpolation criteria for **cumulative** spherical polynomial spaces under density and separation hypotheses. Their criteria do not determine ranks of a **single exact degree** on this fixed 25-point grid. Cohl and Palmer (2014, arXiv:1405.4847) provide hyperspherical Fourier and Gegenbauer expansions, supporting the addition-formula framework but not this finite evaluation classification. McEwen and collaborators (2015, arXiv:1508.03101) establish bandlimited sampling on \(SO(3)\) with different grids and transform spaces. None of the inspected relevant sections supplies the isolated degree-six defect or its complete rank sequence. Earlier harmonic restriction formulas may imply special cases upon nontrivial specialization; this remains an originality limitation, not a proof of uniqueness.

## Limitations

The theorem is about this particular 25-node equal-radius configuration, complex-valued exact-degree spherical harmonics, and linear-algebraic interpolation/rank. It does not determine optimal interpolation condition numbers across all degrees, stability under perturbations, or higher-order Clifford grids. The exact checker and analytical proof have not undergone independent audit. The literature comparison is bounded and cannot exclude unindexed equivalent treatments.

## References

- J. Marzo and B. Pridhnani, *Sufficient conditions for sampling and interpolation on the sphere*, arXiv:1302.6730, first version 2013-02-27.
- H. S. Cohl and R. M. Palmer, *Fourier and Gegenbauer expansions for a fundamental solution of Laplace's equation in hyperspherical geometry*, arXiv:1405.4847, first version 2014-05-19.
- J. D. McEwen et al., *A novel sampling theorem on the rotation group*, arXiv:1508.03101, first version 2015-08-13.
