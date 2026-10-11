# Exact endpoint norms of single Peter--Weyl blocks on \(SU(2)\)
## Finding
Let \(\pi_r\) be the irreducible representation of \(SU(2)\) of highest weight \(r\ge0\), and write \(m=r+1\) for its dimension. Let \(H_r\) be the full matrix-coefficient space of \(\pi_r\), and let \(P_r:L^2(SU(2))\to H_r\) be the orthogonal Peter--Weyl projection. Haar measure is normalized to total mass one.

For the trivial block, \(m=1\),
\[
\|P_0\|_{L^1\to L^1}=\|P_0\|_{L^\infty\to L^\infty}=1.
\]
For every \(m\ge2\),
\[
\boxed{
\|P_r\|_{L^1\to L^1}=\|P_r\|_{L^\infty\to L^\infty}
=\frac{4m^2}{\pi(m^2-1)}\cot\!\left(\frac{\pi}{2m}\right)
}.
\]
In particular,
\[
\frac{\|P_r\|}m\longrightarrow\frac8{\pi^2},
\]
so a single nonabelian Fourier block already has endpoint amplification linear in its representation dimension. Since \(\dim H_r=m^2\), this is equivalently
\[
\|P_r\|\sim\frac8{\pi^2}\sqrt{\dim H_r}.
\]

## Assumptions and scope
The group is the compact Lie group \(SU(2)\) with normalized Haar measure. The projection is onto one complete Peter--Weyl isotypic block, not a partial sum of several highest weights. The endpoint norms are the ordinary operator norms on \(L^1(SU(2))\) and \(L^\infty(SU(2))\). No claim is made here about intermediate \(L^p\) norms, filtered sums of blocks, or higher-rank compact Lie groups.

## Proof
For an irreducible representation of dimension \(m\), the central idempotent kernel of the corresponding Peter--Weyl projection is
\[
K_r(g)=m\,\chi_r(g),
\]
where \(\chi_r\) is the irreducible character. Thus
\[
P_r f=f*K_r.
\]
Convolution by an integrable kernel has both endpoint norms equal to its \(L^1\) mass. For \(L^\infty\), equality is obtained by a bounded phase-sign of the translated kernel; for \(L^1\), a normalized approximate identity converges to the kernel in \(L^1\). Hence
\[
\|P_r\|_{L^1\to L^1}=\|P_r\|_{L^\infty\to L^\infty}
=m\int_{SU(2)}|\chi_r(g)|\,dg.
\]

Write a conjugacy class by \(0\le\theta\le\pi\). The Weyl character formula and Weyl integration formula give
\[
\chi_r(\theta)=\frac{\sin(m\theta)}{\sin\theta},
\qquad
\int_{SU(2)}F(g)\,dg=\frac2\pi\int_0^\pi F(\theta)\sin^2\theta\,d\theta
\]
for central \(F\). Therefore
\[
\|P_r\|=\frac{2m}\pi I_m,
\qquad
I_m=\int_0^\pi |\sin(m\theta)|\sin\theta\,d\theta.
\]
The case \(m=1\) gives \(I_1=\pi/2\). Assume \(m\ge2\), and split the integral at the zeros \(j\pi/m\). On the \(j\)-th interval the sign of \(\sin(m\theta)\) is \((-1)^j\). An antiderivative of \(\sin(m\theta)\sin\theta\) is
\[
F_m(\theta)=\frac{\sin((m-1)\theta)}{2(m-1)}-\frac{\sin((m+1)\theta)}{2(m+1)}.
\]
Alternating the interval contributions and using \(F_m(0)=F_m(\pi)=0\) yields
\[
I_m=2\sum_{j=1}^{m-1}(-1)^{j-1}F_m\!\left(\frac{j\pi}m\right).
\]
At these grid points,
\[
F_m\!\left(\frac{j\pi}m\right)
=(-1)^{j+1}\frac{m}{m^2-1}\sin\!\left(\frac{j\pi}m\right),
\]
so
\[
I_m=\frac{2m}{m^2-1}\sum_{j=1}^{m-1}\sin\!\left(\frac{j\pi}m\right)
=\frac{2m}{m^2-1}\cot\!\left(\frac{\pi}{2m}\right).
\]
Substitution gives the displayed norm formula. Finally, \(\cot x=x^{-1}+O(x)\) as \(x\to0\), which gives \(\|P_r\|/m\to8/\pi^2\).

## Verification
The standalone script `verify_su2_projection.py` independently evaluates the piecewise-signed integral from its antiderivative for \(2\le m\le500\), compares it with the closed cotangent formula, and performs direct midpoint quadrature for selected dimensions. It also checks the asymptotic ratio numerically. The finite checks corroborate the algebraic proof; they are not used to infer the universal statement.

## Relationship to prior work
Hare's 1997 paper treats exactly the Peter--Weyl decomposition \(L^2(SU(2))=\bigoplus_r H_r\), with \(H_r\) the matrix-coefficient space of the irreducible representation of degree \(r+1\), and develops Littlewood--Paley estimates for lacunary sums of these blocks. The inspected full text, especially Section 2(4), does not state the endpoint norm of one block, the \(L^1\)-character integral above, or the cotangent closed form.

Giulini and Travaglini study Lebesgue constants for spherical and polyhedral Dirichlet kernels on compact connected semisimple Lie groups and establish sharp-order estimates for multi-block partial sums. That broader partial-sum theory does not supply the exact norm of a single \(SU(2)\) isotypic block. Meaney likewise studies unbounded Lebesgue constants arising from decompositions of the dual of a compact group rather than this single-block closed form.

Targeted searches were made under the equivalent descriptions “single irreducible Fourier projection,” “single Peter--Weyl block,” “\(L^1\) norm of an \(SU(2)\) character,” and the cotangent formula. No source located in those searches states the displayed all-dimension identity. This is evidence for originality, not a proof that an older equivalent elementary integral has never appeared.

## Limitations
The theorem is specific to \(SU(2)\) and to one complete irreducible block. The exact evaluation uses the rank-one Weyl character and integration formulas and does not automatically extend to higher-rank compact groups. A residual bibliographic risk is that the same character \(L^1\)-norm evaluation appears in older representation-theory or approximation literature under terminology not retrieved by the searches. No independent audit has been performed.

## References
1. K. E. Hare, “A General Approach to Littlewood--Paley Theorems for Orthogonal Families,” *Canadian Mathematical Bulletin* 40 (1997), 296--308, DOI 10.4153/CMB-1997-036-1. Primary MSC 42B25; issue date 1997-09-01.
2. S. Giulini and G. Travaglini, “Sharp estimates for Lebesgue constants on compact Lie groups,” *Journal of Functional Analysis* 68 (1986), 106--116, DOI 10.1016/0022-1236(86)90059-5.
3. C. Meaney, “Unbounded Lebesgue Constants on Compact Groups,” *Monatshefte für Mathematik* 91 (1981), 119--130, DOI 10.1007/BF01295142.
