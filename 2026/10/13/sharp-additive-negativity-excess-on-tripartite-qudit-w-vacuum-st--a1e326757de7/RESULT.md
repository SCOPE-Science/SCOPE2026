# Sharp additive-negativity excess on tripartite qudit W-vacuum states

## Finding

Let \(D\ge2\) be an integer, \(r=D-1\), and let
\[
|\Psi\rangle=w|000\rangle+\sum_{j=1}^{r}\bigl(a|j0j\rangle+b|jj0\rangle\bigr),
\qquad w,a,b\ge0,\quad w^2+r(a^2+b^2)=1.
\]
With \(N(\rho)=\|\rho^{T_A}\|_1-1\), denote by \(N_{A|B},N_{A|C},N_{A|BC}\) the corresponding bipartite negativities. Define
\[
G_D=N_{A|B}+N_{A|C}-N_{A|BC}.
\]
For \(w,a,b>0\), the excess is positive, zero, or negative according as \(w^2\) is greater than, equal to, or less than \(1/D\). The excess vanishes if \(w=0\), \(ab=0\), or \(w=1\).

Put \(k=rw^2/(1-w^2)\) for \(0\le w<1\) and \(F(k)=\sqrt{1+8k}-1-2\sqrt{k}\). At fixed \(w\), the maximal excess over nonnegative \(a,b\) is
\[
\max_{a,b}G_D=\begin{cases}
0,&0\le w^2\le1/D,\\
\dfrac r{r+k}F(k),&1/D<w^2<1.
\end{cases}
\]
The second line has the unique maximizing allocation \(a=b>0\); at \(w=1\) the excess is zero. Globally, there is one number \(k_r>1\) solving
\[
(r+k)\left(\frac4{\sqrt{1+8k}}-\frac1{\sqrt{k}}\right)
=\sqrt{1+8k}-1-2\sqrt{k},
\]
and the **unique** global maximizing amplitudes are
\[
w^2=\frac{k_r}{r+k_r},\qquad
 a^2=b^2=\frac1{2(r+k_r)}.
\]
Consequently the exact dimension-dependent maximum and its sharp scaling are
\[
M_D=\frac r{r+k_r}F(k_r)>0,
\qquad\lim_{D\to\infty}\frac{M_D}{\sqrt{D-1}}=\sqrt2-1.
\]
The maximum is taken only over the displayed state family; it is not a universal bound on all tripartite states.

## Assumptions and scope

Each local Hilbert space is \(\mathbb C^D\), with computational basis indexed by \(0,1,\ldots,D-1\). Amplitudes are real and nonnegative; local diagonal phase changes absorb the corresponding phases of the symmetric family. Negativity is normalized **without** an extra factor \(1/2\). All partial transposes act on Alice. No convex-roof extension of negativity is used. The zero-coefficient and zero-vacuum boundaries are included explicitly. Primary classification: MSC2020 81P42.

## Proof

**Exact partial-transpose spectra.** Let \(s=a^2+b^2\). Tracing out subsystem \(C\) gives
\[
\rho_{AB}=|\phi\rangle\langle\phi|+a^2\sum_{j=1}^{r}|j0\rangle\langle j0|,
\quad |\phi\rangle=w|00\rangle+b\sum_{j=1}^{r}|jj\rangle.
\]
The partial transpose on \(A\) has, for each \(j\ge1\), a block on \(\{|0j\rangle,|j0\rangle\}\) with matrix
\[
\begin{pmatrix}0&wb\\wb&a^2\end{pmatrix},
\]
and, for each \(1\le i<j\le r\), a block on \(\{|ij\rangle,|ji\rangle\}\) with off-diagonal entries \(b^2\) and zero diagonal. The remaining blocks are positive. Summing twice the absolute values of negative eigenvalues yields
\[
N_{A|B}=r\bigl(\sqrt{a^4+4b^2w^2}-a^2\bigr)+r(r-1)b^2.
\]
Interchanging \(a,b\) gives
\[
N_{A|C}=r\bigl(\sqrt{b^4+4a^2w^2}-b^2\bigr)+r(r-1)a^2.
\]
The nonzero eigenvalues of \(\rho_A\) are \(w^2\) once and \(s\) repeated \(r\) times. The pure-state identity \(N_{A|BC}=(\operatorname{Tr}\sqrt{\rho_A})^2-1\) therefore gives
\[
N_{A|BC}=2rw\sqrt{s}+r(r-1)s.
\]
No assumption about the sign of the excess has been used.

**Exact sign and fixed-mass optimization.** If \(s>0\), write \(t=a^2/s\in[0,1]\), \(k=w^2/s\ge0\), and \(u=\sqrt{k}\). Normalization implies \(rs=r/(r+k)\). The preceding formulas simplify exactly to
\[
G_D=\frac r{r+k}\,\Bigl[
\sqrt{t^2+4(1-t)k}+\sqrt{(1-t)^2+4tk}-1-2\sqrt{k}\Bigr].
\tag{1}
\]
The elementary identity
\[
\bigl(t+2(1-t)u\bigr)^2-\bigl(t^2+4(1-t)u^2\bigr)
=4t(1-t)u(1-u)
\]
and its image under \(t\mapsto1-t\) establish the strict sign asserted whenever \(0<t<1\) and \(u>0\): each square-root summand is larger than the corresponding linear summand precisely for \(u>1\). The sign of \(k-1\) is that of \(Dw^2-1\). If \(t=0\) or \(t=1\), or if \(k=0\), equation (1) vanishes. If \(s=0\), the state is a product vacuum and the excess is zero.

For \(k>0\) and \(f_k(t)=\sqrt{t^2+4(1-t)k}\), direct differentiation gives
\[
f_k''(t)=\frac{4k(1-k)}{[t^2+4(1-t)k]^{3/2}}.
\]
For \(k>1\), the bracket in (1) is strictly concave, invariant under \(t\mapsto1-t\), and thus uniquely maximized at \(t=1/2\). Its value there is \(\sqrt{1+8k}-1-2\sqrt{k}=F(k)\). For \(0<k<1\), it is strictly convex, and its maximum is its zero endpoint value. At \(k=1\) it vanishes identically. This proves the fixed-mass statement, including its endpoint behavior.

**Global maximum and uniqueness.** On \(k>1\), write \(h_r(k)=rF(k)/(r+k)\) and
\[
H_r(k)=(r+k)F'(k)-F(k).
\]
Here
\[
F'(k)=\frac4{\sqrt{1+8k}}-\frac1{\sqrt{k}},\qquad
F''(k)=-\frac{16}{(1+8k)^{3/2}}+\frac1{2k^{3/2}}<0
\quad (k\ge1).
\]
Indeed, \(1+8k\le9k\) shows the magnitude of the first term in \(F''\) exceeds \(16/(27k^{3/2})>1/(2k^{3/2})\). Therefore \(H_r'(k)=(r+k)F''(k)<0\). Also \(H_r(1)=(r+1)/3>0\), and \(H_r(k)\to-\infty\) as \(k\to\infty\). There is exactly one root \(k_r>1\), and \(h_r'(k)=rH_r(k)/(r+k)^2\) changes from positive to negative at that root. Since \(h_r(k)\to0\) at both ends and is positive inside, this root produces the unique global maximum.

**Sharp scaling.** For every \(k\ge0\),
\[
F(k)\le(2\sqrt2-2)\sqrt{k}
\]
by \(\sqrt{1+8k}\le1+2\sqrt2\sqrt{k}\). Since \(\sqrt{k}/(r+k)\le1/(2\sqrt r)\), it follows that
\[
M_D\le(\sqrt2-1)\sqrt r.
\]
Selecting the admissible balanced state \(k=r\) gives
\[
M_D\ge\frac12\bigl(\sqrt{1+8r}-1-2\sqrt r\bigr).
\]
After division by \(\sqrt r\), the two bounds converge to \(\sqrt2-1\), completing the proof.

## Verification

A concrete qutrit witness is \(D=3\), \(w=3/5\), \(a=b=2/5\). Direct substitution gives
\[
N_{A|B}=N_{A|C}=\frac{8\sqrt{10}}{25},\quad
N_{A|BC}=\frac{16+24\sqrt2}{25},
\]
so
\[
G_3=\frac{16\sqrt{10}-24\sqrt2-16}{25}>0.
\]
The strict inequality reduces after squaring to \(3/2>\sqrt2\). The accompanying `verify.py` independently constructs the finite-dimensional density matrices, takes partial transposes, and checks exact eigenvalue expressions in dimensions \(2\), \(3\), \(4\), and \(5\); it also checks the concavity identity and numerical optimality bounds. Run with `python verify.py` using SymPy. The dimension-uniform theorem and asymptotic limit are supplied by the analytic proof, not inferred from finite computations.

## Relationship to prior work

Allen and Meyer introduce the tripartite qudit family and its partial-transpose block structure, analyze the achievable negativity surface, and give leading-dimensional negativity formulas [1]. The family and the spectral ingredients are therefore **not** claimed as novel. The contribution here is the complete sharp maximization of the **unsquared, additive** negativity excess within that family, including the exact optimizer, the threshold for its sign, and the sharp \(\sqrt D\) dimension coefficient. Their leading-order expansion does not fix this optimized subleading scale. The squared-negativity monogamy framework of Ou and Fan [2] does not imply an upper bound on the sum of unsquared negativities. Choi and Kim [3] and Liang–Zheng–Zhu [4] analyze generalized W states using squared convex-roof extended negativity, concurrence, or Rényi entropy; those are different optimization functionals. No claim of global novelty beyond the surveyed literature or independent validation is made.

## Limitations

The result optimizes only the displayed real-amplitude W-vacuum family, not all three-qudit states, and does not resolve the conjecture that Allen and Meyer's higher-dimensional surface is the entire achievable region. The exact \(k_r\) is specified implicitly as the unique root of a one-variable equation, not by radicals. For small dimensions the asymptotic approximation is not exact. Literature equivalence under other parameterizations remains possible. Computational spot checks do not certify the analytic statement for untested dimensions.

## References

[1] G. W. Allen and D. A. Meyer, *Polynomial Monogamy Relations for Entanglement Negativity*, arXiv:1502.04807 (first public version 17 February 2015); Phys. Rev. Lett. 118, 080402 (2017), doi:10.1103/PhysRevLett.118.080402.

[2] Y.-C. Ou and H. Fan, *Monogamy inequality in terms of negativity for three-qubit states*, Phys. Rev. A 75, 062308 (2007), doi:10.1103/PhysRevA.75.062308.

[3] J. H. Choi and J. S. Kim, *Negativity and strong monogamy of multi-party quantum entanglement beyond qubits*, arXiv:1508.07673 (2015).

[4] Y. Liang, Z.-J. Zheng and C.-J. Zhu, *Monogamy and polygamy for generalized W-class states using Rényi-α entropy*, Phys. Rev. A 102, 062428 (2020), doi:10.1103/PhysRevA.102.062428.
