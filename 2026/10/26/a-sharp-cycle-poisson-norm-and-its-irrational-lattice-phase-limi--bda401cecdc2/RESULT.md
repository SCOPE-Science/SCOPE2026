# A sharp cycle Poisson norm and its irrational lattice-phase limit law

## Finding
For the unit-edge cycle \(C_n\) with \(n\ge3\), put \(G_n=L_n^\dagger\), where \(L_n\) is the unnormalized combinatorial graph Laplacian. Write
\[
 t_n=\sqrt{\frac{n^2+2}{3}},\qquad
 r_n=\frac{n-t_n}{2},\qquad m_n=\lfloor r_n\rfloor,\qquad u_n=r_n-m_n\in[0,1).
\]
The sharp endpoint norm \(N_n=\|G_n\|_{\ell^1\to\ell^1}=\|G_n\|_{\ell^\infty\to\ell^\infty}\) is exactly
\[
 N_n=\frac{(2m_n+1)(n^2-1)}{6n}-m_n(m_n+1)
      +\frac{m_n(m_n+1)(2m_n+1)}{3n}.
\]
A more revealing *exact* expression is
\[
 N_n=\frac{(n^2-1)t_n}{18n}
       +\frac{t_n}{n}u_n(1-u_n)
       +\frac{u_n(1-u_n)(2u_n-1)}{3n}.
\]
Consequently, uniformly for integers \(n\ge3\),
\[
 N_n=\frac{\sqrt3}{54}n^2+\frac{u_n(1-u_n)}{\sqrt3}+O(n^{-1}).
\]
The constant-order remainder has no limit. Instead, its **complete limiting empirical law** is
\[
 \lim_{M\to\infty}\frac1M\sum_{n=3}^{M+2}\Phi\!\left(N_n-\frac{\sqrt3}{54}n^2\right)
 =\int_0^1\Phi\!\left(\frac{v(1-v)}{\sqrt3}\right)\,dv
\]
for every bounded continuous real function \(\Phi\). Equivalently, the limiting cumulative distribution function is
\[
 F(s)=\begin{cases}
 0,&s<0,\\
 1-\sqrt{1-4\sqrt3\,s},&0\le s\le1/(4\sqrt3),\\
 1,&s>1/(4\sqrt3).
 \end{cases}
\]
The exact set of accumulation points of the centered remainder is \([0,1/(4\sqrt3)]\). This is a sharp norm theorem and a second-order arithmetic law; the Green matrix entries themselves are classical.

## Assumptions and scope
Vertices are \(\mathbb Z/n\mathbb Z\); each of the two cycle edges incident to a vertex has unit conductance, including the ordinary triangle at \(n=3\). We use the **unnormalized** Laplacian
\[
 (L_nf)(j)=2f(j)-f(j-1)-f(j+1).
\]
The Moore–Penrose inverse \(G_n\) is the unique symmetric operator satisfying \(L_nG_n=G_nL_n=I-J/n\) and \(G_n\mathbf1=0\). Endpoint norms are matrix operator norms on *all* real \(\ell^1\) and \(\ell^\infty\) inputs with counting measure; neither is restricted to the subspace of mean-zero inputs. Every maximization is attained at a sign-valued input, with sign choices at zero entries immaterial.

## Proof
**1. The known Green kernel and its verification.** Set
\[
 g_n(k)=\frac{n^2-1}{12n}-\frac{k(n-k)}{2n},\qquad k=0,1,\ldots,n-1.
\]
Then \(g_n(n-k)=g_n(k)\) and \(\sum_{k=0}^{n-1}g_n(k)=0\), because \(\sum_{k=0}^{n-1}k(n-k)=n(n^2-1)/6\). Its circular second difference satisfies
\[
 2g_n(k)-g_n(k-1)-g_n(k+1)=\mathbf1_{k=0}-\frac1n,
\]
with indices modulo \(n\). Therefore \((G_n)_{ij}=g_n(i-j\bmod n)\), by the Moore–Penrose characterization. This quadratic kernel is established background and is not asserted to be new.

**2. Sign boundary and sharp norm.** Directly,
\[
 g_n(k)\ge0\quad\Longleftrightarrow\quad
 6k(n-k)\le n^2-1.
\]
On \(0\le k\le n/2\) this is equivalent to \(k\le r_n\). Thus the nonnegative entries in each row consist of the center and the \(m_n\) nearest points on either side; exact zeros may occur on the boundary. As rows sum to zero and are translates,
\[
 \|G_n\|_{\infty\to\infty}=\sum_{k=0}^{n-1}|g_n(k)|
 =2\bigl(g_n(0)+2\sum_{k=1}^{m_n}g_n(k)\bigr).
\]
Evaluating \(\sum k\) and \(\sum k^2\) yields the displayed polynomial in \(m_n\). Symmetry gives the same \(\ell^1\) norm. At any fixed row \(i\), the input \(f(j)=\operatorname{sign}(G_n)_{ij}\) achieves its absolute row sum (choose either sign at a zero).

**3. Exact phase correction.** Substitute \(m_n=(n-t_n)/2-u_n\) into the polynomial norm and simplify using \(3t_n^2=n^2+2\). This gives exactly
\[
 N_n=\frac{(n^2-1)t_n}{18n}
 +\frac{t_n}{n}u_n(1-u_n)
 +\frac{u_n(1-u_n)(2u_n-1)}{3n}.
\]
Since \(t_n/n=1/\sqrt3+O(n^{-2})\), while \(0\le u_n<1\), the expansion in the Finding follows with a uniform \(O(n^{-1})\) error.

**4. Irrational equidistribution and distribution law.** Put \(c=(1-1/\sqrt3)/2\), which is irrational. The phase before taking fractional parts obeys
\[
 r_n=cn+O(n^{-1}).
\]
For every fixed nonzero integer \(h\), the average of \(\exp(2\pi i h r_n)\) differs by \(o(1)\) from the average of \(\exp(2\pi i hcn)\). The latter tends to zero by the geometric-series formula and irrationality of \(c\). Weyl's criterion therefore makes \(u_n=\{r_n\}\) equidistributed in \([0,1]\). The continuous map \(v\mapsto v(1-v)/\sqrt3\), together with the uniform norm error, gives the claimed empirical integral. For \(s\in[0,1/(4\sqrt3)]\), the condition \(v(1-v)/\sqrt3\le s\) holds on two intervals of combined length \(1-\sqrt{1-4\sqrt3 s}\); this proves the CDF. Density of the phases, continuity, and vanishing error show that *every* value in \([0,1/(4\sqrt3)]\), and no value outside it, is an accumulation point. In particular the remainder cannot converge to a single constant.

## Verification
The accompanying self-contained `check.py` uses only the Python standard library. It checks exact row-zero and Laplacian identities, the sign cutoff and sharp polynomial norm for all 248 cycle sizes \(3\le n\le250\), and reconstructs the inverse independently by exact rational Gauss–Jordan elimination for \(3\le n\le12\). It also checks the radical rearrangement numerically as a separate consistency test. The program records **64,381 successful assertions**. The limiting distribution and universal identities are mathematical deductions above, not consequences of these finite tests.

## Relationship to prior work
The explicit cycle Green kernel, the resistance-distance formulas, and the general Green-inverse construction are background. Zhang and Yang (first publicly released September 5, 2006) derived resistance and Kirchhoff-index formulas for circulant graphs, including cycles. Bendito and collaborators' work develops Green representations for singular symmetric M-matrices; their 2008 accessible lecture manuscript concerns general Green inverses and weighted paths. Ranjan, Zhang and Boley (2013) give general Laplacian pseudoinverse algorithms. Van Mieghem, Devriendt and Cetinay (2017) display a closed cycle pseudoinverse in their Appendix, a close full-text source. None of these inspected materials directly supplies the sharp absolute-row-sum norm **and** its irrational, nonconvergent second-order empirical law. This is a best-knowledge originality assessment, not a priority certificate.

## Limitations
The result applies to unit-weight cycles only, not arbitrary conductance perturbations, other graph families, or arbitrary \(\ell^p\) exponents. The sharp endpoint norm is over all inputs; it is not claimed to be sharp for the restricted mean-zero input unit ball. The finite checker proves no infinite-dimensional or asymptotic statement. Some older relevant full texts remain inaccessible, leaving residual historical-priority risk, especially possible equivalent statements under Green-function, deviation-matrix, or periodic Poisson terminology. No independent audit has been performed.

## References
1. H. Zhang and Y. Yang, *Resistance distance and Kirchhoff index in circulant graphs*, International Journal of Quantum Chemistry 107 (2007), 330–339, first online September 5, 2006. DOI: `10.1002/qua.21068`.
2. E. Bendito, A. Carmona, A. M. Encinas, J. M. Gesto and M. Mitjana, *On the Generalized Inverses of Symmetric M-matrices*, public lecture slides, December 1–4, 2008, `https://mapthe.upc.edu/en/congresses/docs/congresses_2008_on-the-generalized-inverses-of-symmetric-m-matrices.pdf`.
3. E. Bendito, A. Carmona, A. M. Encinas and M. Mitjana, *Generalized inverses of symmetric M-matrices*, Linear Algebra and its Applications 432 (2010), 2438–2454. DOI: `10.1016/j.laa.2009.11.008`.
4. G. Ranjan, Z.-L. Zhang and D. Boley, *Incremental Computation of Pseudo-Inverse of Laplacian: Theory and Applications*, arXiv:1304.2300 (first submitted April 8, 2013).
5. P. Van Mieghem, K. Devriendt and H. Cetinay, *Pseudoinverse of the Laplacian and best spreader node in a network*, Physical Review E 96 (2017), 032311. DOI: `10.1103/PhysRevE.96.032311`.
