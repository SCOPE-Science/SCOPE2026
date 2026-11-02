# An exact one-mode spectral exchange for first-Hermite disk localization

## Finding

Consider the true first-excited Landau/Fock level \(\mathcal L_1\) and disk concentration \(T_x\) specified below. Its complete eigenvalues \(a_j(x)\) obey the **new exact nearest-neighbor rule**
\[
 a_{j+1}(x)-a_j(x)=-e^{-x}\frac{x^j}{(j+1)!}(x-j)(x-j-1),\qquad j\ge0,\ x>0.
\]
At each positive integer radius parameter \(x=k\) the eigenvalues at indices \(k-1,k,k+1\) coincide, form exactly the three-dimensional eigenvalue at the canonical rank-\(k\) cutoff, and are strictly separated from all other eigenvalues. If \(k<x<k+1\) for an integer \(k\ge0\), then the **unique** subspace of dimension \(N=\lceil x\rceil=k+1\) that maximizes the disk concentration trace is
\[
 E_x=\operatorname{span}\{v_0,\ldots,v_{k-1},v_{k+1}\};
\]
for \(k=0\) the prefix is empty. In particular, compared with the conventional first-\(N\)-mode subspace \(F_N=\operatorname{span}\{v_0,\ldots,v_k\}\), the top-energy selection exchanges **exactly one** basis vector. The gain in concentration trace is
\[
 \operatorname{tr}(P_{E_x}T_x)-\operatorname{tr}(P_{F_N}T_x)
 =e^{-x}\frac{x^k}{(k+1)!}(x-k)(k+1-x)>0.
\]
The two rank-\(N\) projections satisfy, for every noninteger \(x>0\),
\[
 \|P_{E_x}-P_{F_N}\|=1,\qquad
 \|P_{E_x}-P_{F_N}\|_{S^1}=2,\qquad
 \|P_{E_x}-P_{F_N}\|_{S^2}=\sqrt2.
\]
This is an exact constant bound, sharpening the known general \(O(\sqrt N)\) trace-norm comparison for this first-Hermite disk case. For fixed \(0<\delta<1\), at \(x=k+\delta\) the trace gain has the uniform large-\(k\) law
\[
 \frac{\delta(1-\delta)}{\sqrt{2\pi}\,k^{3/2}}
 \bigl(1+O(k^{-1})\bigr),
\]
with the relative error uniform over \(\delta\in(0,1)\). Hence the two projectors remain a trace distance \(2\) apart even as the energy gain tends to zero. A further sharp consequence is
\[
\|T_x\|=
\begin{cases}
 1-e^{-x}(1+x^2),&0<x\le1,\\
 1-e^{-x}(1+x),&x\ge1,
\end{cases}
\]
with a three-dimensional maximizing eigenspace exactly at \(x=1\).

## Assumptions and scope

Use the Gaussian Fock probability measure \(d\mu(z)=\pi^{-1}e^{-|z|^2}\,dA(z)\) on \(\mathbb C\). Set
\[
 v_0(z)=\overline z,\qquad
 v_j(z)=\frac{(j-|z|^2)z^{j-1}}{\sqrt{j!}}\quad(j\ge1),
 \qquad \mathcal L_1=\overline{\operatorname{span}}\{v_j:j\ge0\}\subset L^2(d\mu).
\]
The \(v_j\) are an orthonormal basis (angular orthogonality and elementary Gamma integrals). The space \(\mathcal L_1\) is the true first-excited Landau level: its basis is obtained by one Gaussian polyanalytic raising operation on the analytic Fock monomials, up to harmless unit-modulus constants. Let \(P_1\) denote its orthogonal projection and define the positive compact operator \(T_x=P_1M_{\mathbf1_{\{|z|^2<x\}}}|_{\mathcal L_1}\) for \(x>0\). The parameter is **the square of the disk radius in Fock coordinates**; in unit-density time-frequency coordinates, a disk of radius \(R\) corresponds to \(x=\pi R^2\). All index sets and rank counts concern exactly this normalization.

Write the lower-incomplete-Gamma ratio \(G_j(x)=1-e^{-x}\sum_{r=0}^{j-1}x^r/r!\) for integers \(j\ge1\). The full positive spectrum, with multiplicities and without relying on any ordering convention, is
\[
 a_0(x)=1-e^{-x}(1+x),\quad
 a_j(x)=G_j(x)+e^{-x}\frac{x^j}{j!}(j-1-x),\quad j\ge1.
\]
The \(v_j\) diagonalize \(T_x\); the eigenvalues are in \((0,1)\), tend to zero as \(j\to\infty\), and \(\sum_{j\ge0}a_j(x)=x\). The radial eigenvalue integral and diagonalization are already known; the claimed contribution is the complete spectral ordering at the finite-ensemble cutoff and its sharp consequences.

## Proof

**Step 1: Diagonalization and normalization.** Every \(v_j\) has pure angular frequency \(j-1\), including \(v_0\) with frequency \(-1\). Both Gaussian and disk measures are radial, so the disk form is diagonal in the \(v_j\) basis. For \(j\ge1\), putting \(t=|z|^2\) gives
\[
 a_j(x)=\frac1{j!}\int_0^x (j-t)^2t^{j-1}e^{-t}\,dt,
\]
whereas \(a_0(x)=\int_0^x te^{-t}\,dt\). The normalization identity
\[
 \frac1{j!}\int_0^\infty (j-t)^2t^{j-1}e^{-t}\,dt=1
\]
follows from \(\Gamma(j+1)=j\Gamma(j)\) and \(\Gamma(j+2)=(j+1)j\Gamma(j)\). The recurrence \(\gamma(j+1,x)=j\gamma(j,x)-x^je^{-x}\) reduces the finite-radius integral to the displayed formula for \(a_j\). Summing diagonal entries yields \(\sum_j a_j=x\) by the constant diagonal of the first-excited Landau reproducing kernel (equivalently, by the Gaussian Laguerre completeness identity). Thus \(T_x\) is positive trace class.

**Step 2: The exact increment.** Subtract the incomplete-gamma expressions, using \(G_{j+1}(x)=G_j(x)-e^{-x}x^j/j!\) and collecting the remaining powers. For every integer \(j\ge1\) this gives
\[
 a_{j+1}-a_j=-e^{-x}\frac{x^j}{(j+1)!}(x-j)(x-j-1).
\]
At \(j=0\) the same identity follows directly from \(a_1=1-e^{-x}(1+x^2)\) and \(a_0=1-e^{-x}(1+x)\). The sign is negative except when \(j<x<j+1\), when it is positive, and it vanishes when \(x=j\) or \(x=j+1\).

**Step 3: All radii and exact cutoff.** For integer \(x=k\ge1\), the adjacent gaps vanish precisely at \(j=k-1,k\) and all other adjacent gaps are strictly negative. Hence the eigenvalue at indices \(k-1,k,k+1\) has multiplicity exactly three and lies immediately after the \(k-1\) larger eigenvalues at indices \(0,\ldots,k-2\). The optimal rank-\(k\) projectors are exactly the identity on the span of those first \(k-1\) modes, plus an arbitrary rank-one projection within the triple eigenspace.

For noninteger \(x\in(k,k+1)\), where \(k\ge1\), every adjacent gap is strictly negative except \(a_{k+1}-a_k>0\). The nonadjacent comparison is essential: adding the two neighboring increments gives
\[
 a_{k+1}-a_{k-1}
 =e^{-x}\frac{x^{k-1}}{k!}(x-k)
 \left(k-1-\frac{x^2}{k+1}\right)<0.
\]
Indeed \(x>k\) and \(k-1-k^2/(k+1)=-1/(k+1)<0\). Therefore all \(k\) modes at indices \(0,\ldots,k-1\) have eigenvalues strictly above \(a_{k+1}\), and every other mode has smaller eigenvalue. The case \(k=0\) follows from the single positive gap \(a_1-a_0\) and the strictly decreasing tail after \(a_1\). The Hilbert-space min–max principle proves the asserted **unique** optimal rank-\(k+1\) subspace. The special integer cutoff is treated separately, so no uniqueness is spuriously claimed at ties.

**Step 4: Exact improvement and asymptotics.** Replacing \(v_k\) by \(v_{k+1}\) changes the trace by exactly \(a_{k+1}-a_k\), which by the increment formula is the stated positive expression. Because the two selected modes are orthogonal, the difference of projectors has precisely two nonzero eigenvalues, \(+1\) and \(-1\), yielding the three asserted operator/Schatten norms. For \(x=k+\delta\) one has uniformly over \(0\le\delta\le1\)
\[
 e^{-(k+\delta)}\frac{(k+\delta)^k}{k!}
 =\frac1{\sqrt{2\pi k}}\left(1+O(k^{-1})\right)
\]
by Stirling's formula and \(k\log(1+\delta/k)-\delta=O(k^{-1})\). Substitution into the exact trace gain, with \((k+1)^{-1}=k^{-1}(1+O(k^{-1}))\), proves the uniform asymptotic. Finally the ordering shows that the maximal mode is \(v_1\) for \(0<x<1\), \(v_0\) for \(x>1\), and the triple eigenspace at \(x=1\), yielding the piecewise norm formula.

## Verification

The included self-contained Python script `check_selection.py` computes \(1-e^{-x}b_j(x)\) in **exact rational arithmetic after the common factor** \(e^{-x}\) is removed. It checks the adjacent increment identity, the full finite modal rankings, integer triple ties, the selected mode exchange and its gain over many rational values of \(x\); it also checks several large-index Stirling approximations. Its successful execution yielded 6,234 supplementary finite assertions. These computations test implementations and finite instances only. Completeness, all real radii, the min–max statement and the asymptotic theorem are established by Steps 1–4, not by finite enumeration.

## Relationship to prior work

Abreu, Gröchenig and Romero (arXiv:1704.03042, first released 2017-04-10; *Journal of Statistical Physics* 174, 2019) prove Hermite-window radial diagonalization and the integral eigenvalue formula (Sect. 4.1–4.2, Proposition 4.1 and Lemma 4.2); their Remark 4.3 exhibits one crossing by a figure. The same paper constructs the canonical rank-\(\lceil\pi R^2\rceil\) finite Weyl–Heisenberg ensemble (Definition 1.3) and bounds the trace norm of its difference from the conventional finite pure polyanalytic Ginibre projection by a quantity of order \(\sqrt N\) (Theorem 1.6). The present **all-radii rank-cutoff classification** computes the exact discrepancy \(2\) away from integer-area ties, the entire threefold tie rule at integer areas, and the exact concentration-energy gain, neither of which is asserted in the inspected relevant sections of the source. The result is an explicit sharp refinement **for the first excited level only**, not a claim about other Landau levels.

Keller and Luef (arXiv:1905.07741; *Journal of Fourier Analysis and Applications* 27, 2021) develop the general polyanalytic Toeplitz and symbolic calculus framework, but not this finite-disk eigenvalue ranking. Known diagonalization is fully credited; the novelty claim concerns the new ordering and projection selection, not the integral spectrum itself.

## Limitations

The result concerns only the first excited Landau level, centered round disks, exact Gaussian normalization and finite rank \(\lceil x\rceil\). A higher Landau level or a nonradial domain is not covered. At integer \(x\), the canonical top-rank projection is nonunique, so the constant trace-norm \(2\) is **not** asserted there; one allowed tie-breaking choice reproduces the conventional initial-index projection. Other accidental degeneracies away from the selection cutoff are not classified. The source-integral formula is prior art, and an independently undiscovered earlier treatment of the exact selection rule remains a historical-priority risk. No independent validation is claimed.

## References

1. L. D. Abreu, K. Gröchenig, J. L. Romero, *Harmonic analysis in phase space and finite Weyl–Heisenberg ensembles*, arXiv:1704.03042 (first public preprint 2017-04-10), *J. Stat. Phys.* 174 (2019), 1104–1136, DOI:10.1007/s10955-019-02226-2. Relevant: Definition 1.3, Theorem 1.6, Proposition 4.1, Lemma 4.2, Remark 4.3.
2. J. Keller, F. Luef, *Polyanalytic Toeplitz operators: isomorphisms, symbolic calculus and approximation of Weyl operators*, arXiv:1905.07741 (2019), *J. Fourier Anal. Appl.* 27 (2021), 47, DOI:10.1007/s00041-021-09843-0.
3. Mathematics Subject Classification 2020, MSC `42C15`, *General harmonic expansions, frames*. (Classification reference, not scientific priority evidence.)
