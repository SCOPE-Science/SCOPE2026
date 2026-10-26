# A sharp stationary-concentration threshold for three-state mutation spectra

## Finding

Consider a mutation kernel on three alleles, required to change the allele at each mutation. Fix its strictly positive stationary probabilities \(\pi=(\pi_1,\pi_2,\pi_3)\), with \(\sum_i\pi_i=1\) and \(p:=\max_i\pi_i<1/2\). For a row-stochastic \(3\times3\) matrix \(P\) satisfying \(P_{ii}=0\) and \(\pi P=\pi\), write \(R(P)\) for the maximum modulus of its two nonstationary eigenvalues, counted algebraically. The sharp optimum is

\[
\boxed{\inf_P R(P)=\begin{cases}\frac12,&p\le\frac49,\\[3pt]\frac{1+\sqrt{9-4/p}}{2},&\frac49<p<\frac12.\end{cases}}
\]

The optimum is attained; all optimizers are specified below. Moreover, the family contains a transition matrix with a nonreal conjugate pair precisely when \(p<4/9\). Thus a distribution-free spectral lower bound of \(1/2\) is achievable up to the *sharp stationary-concentration frontier* \(p=4/9\), but strictly not beyond it.

## Assumptions and scope

Fix \(\pi_i>0\), \(\sum_i\pi_i=1\), and \(p=\max_i\pi_i<1/2\). The index set is \(\{1,2,3\}\), with oriented cycle \(1\to2\to3\to1\). Let
\[
u=\pi_1\pi_2\pi_3,\quad \ell_i=1-2\pi_i>0,\quad g=u-\ell_1\ell_2\ell_3,\quad J=1-2p.
\]
The letter \(j\) below is a real circulation, not an index. For \(-J\le j\le J\), the unique admissible transition matrix with circulation \(j\) is given by
\[
\begin{aligned}
\pi_1P_{12}&=(\ell_3+j)/2,&\pi_2P_{21}&=(\ell_3-j)/2,\\
\pi_2P_{23}&=(\ell_1+j)/2,&\pi_3P_{32}&=(\ell_1-j)/2,\\
\pi_3P_{31}&=(\ell_2+j)/2,&\pi_1P_{13}&=(\ell_2-j)/2,
\end{aligned}
\]
with \(P_{ii}=0\). This is a classification of **all** eligible matrices, including possibly periodic matrices at endpoint circulations. Every minimizing matrix is irreducible and aperiodic; no mutation-branching-process conditioning, population-size asymptotics, or mixing-time minimax assertion is assumed or concluded.

## Proof

**1. One-dimensional stationary-flow polytope.** Put \(f_{ab}=\pi_aP_{ab}\). The stationary row/column marginal equations imply \(f_{12}+f_{21}=\ell_3\), \(f_{23}+f_{32}=\ell_1\), \(f_{31}+f_{13}=\ell_2\). Conservation at each vertex gives the same antisymmetric flow \(j=f_{12}-f_{21}=f_{23}-f_{32}=f_{31}-f_{13}\). Solving gives the displayed six entries. All flows are nonnegative exactly when \(|j|\le\min_i\ell_i=J\). Thus no other kernel can improve the claimed bound.

**2. Exact spectrum.** Every admissible \(P\) has an eigenvalue \(1\) and trace zero, hence its other eigenvalues have sum \(-1\). Since its only nonzero permutation-product terms in the determinant are the two oriented triangles,
\[
\det P=\frac{(\ell_1+j)(\ell_2+j)(\ell_3+j)+(\ell_1-j)(\ell_2-j)(\ell_3-j)}{8u}
=\frac{\ell_1\ell_2\ell_3+j^2}{4u}.
\]
Here the middle equality uses \(\ell_1+\ell_2+\ell_3=1\). The reduced characteristic polynomial is \(z^2+z+\det P\). Consequently
\[
\boxed{\lambda_\pm(j)=\frac{-1\pm\sqrt{(g-j^2)/u}}2.}
\]
In particular, at \(j=0\) the kernel is reversible with respect to \(\pi\), so its eigenvalues are real. Therefore \(g\ge0\). If \(g=0\), then the reversible matrix has the repeated eigenvalue \(-1/2\), and self-adjointness in \(L^2(\pi)\) makes it diagonalizable. Its spectral projection onto the stationary eigenvector is \(\mathbf1\pi\), forcing \(P=-I/2+3\mathbf1\pi/2\). Since the diagonal vanishes, \(\pi_i=1/3\) for every \(i\). Conversely this uniform law has \(g=0\).

**3. Location of the conjugate-pair frontier.** Choose a coordinate with \(\pi_1=p\) and write the remaining masses as \(q,r\). Direct expansion, using \(q+r=1-p\), yields the crucial identity
\[
\boxed{J^2-g=qr(4-9p)=\frac{u}{p}(4-9p).}
\]
Thus there exists an allowed \(j\) with \(j^2>g\), and hence a nonreal pair, if and only if \(p<4/9\). At equality, the extreme allowed circulations have a repeated real pair; for \(p>4/9\), both nonstationary eigenvalues are real for every allowed circulation.

**4. Sharp optimization and equality cases.** If \(0\le j^2\le g\), both nonstationary eigenvalues are real and negative; their maximum modulus is
\[
R(j)=\frac{1+\sqrt{(g-j^2)/u}}2,
\]
which decreases strictly as \(|j|\) approaches \(\sqrt g\). If \(j^2\ge g\), they form a conjugate pair (including the repeated-real endpoint), and
\[
R(j)=\sqrt{\det P}=\sqrt{\frac{\ell_1\ell_2\ell_3+j^2}{4u}},
\]
which increases strictly as \(|j|\) increases beyond \(\sqrt g\). Hence for \(p<4/9\) the two minimizers correspond to \(j=\pm\sqrt g\), coinciding at \(j=0\) precisely for uniform \(\pi\). At \(p=4/9\), they correspond to \(j=\pm J=\pm\sqrt g\). At \(p>4/9\), they correspond to \(j=\pm J\), and the identity in step 3 gives the displayed formula. Each optimum has at least one directed triangle and at least one two-cycle with positive transition weights (or has all six directed edges positive), so is primitive.

**5. Jordan-boundary refinement.** For any nonuniform \(\pi\) with \(p\le4/9\), the optimal matrix has eigenvalues \(1,-1/2,-1/2\) and cannot be diagonalizable: diagonalizability would give \(P=-I/2+3\mathbf1\pi/2\), contradicting \(P_{ii}=0\) unless \(\pi\) is uniform. The repeated nonstationary eigenvalue therefore has a single Jordan block. The uniform optimizer is diagonalizable. This matters because a Jordan factor of order \(n\) can occur in transient matrix-power bounds, despite identical asymptotic eigenvalue modulus. This theorem optimizes the **spectral modulus**, not each finite-time total-variation distance.

## Verification

The standalone dependency-free Python program `verify.py` exactly enumerates all strictly feasible rational stationary triples with denominators from \(7\) through \(35\), and tests five rational circulation levels for each. It checks the stationary equations, nonnegativity, matrix trace/determinant and quadratic eigenvalue identities in rational arithmetic; it also checks the threshold identity and optimal-envelope values. Execution yields **93,708 successful assertions/checks**. The exhaustive quantifiers are justified by the algebra in the proof, not by the finite computation. Run with `python3 verify.py`.

## Relationship to prior work

Blancas, Fittipaldi and Hernández-Torres (2026, Section 2.2) explicitly introduce finite-allele mother-dependent mutation matrices with diagonal zero, and identify their invariant type distribution. Their main results concern conditional branching laws, size-biased genealogies, and population asymptotics; they do not assert the fixed-invariant-three-state spectral-concentration classification proved here. This result studies the mutation kernel alone and does not claim a new Q-process theorem.

Ran and Teng (2024, Proposition 6) already determine the possible nonstationary eigenvalue pairs for three-state matrices with **zero diagonal but unrestricted stationary distribution**; in particular the universal \(1/2\) lower bound on the maximum modulus follows immediately from their fixed trace. That fact is **not** claimed as new here. Their spectral-realization theorem does not fix \(\pi\), and therefore does not give the sharp \(4/9\) stationary-concentration frontier or classify optimizers for each prescribed \(\pi\). Kirkland (2023) characterizes aspects of spectra for stochastic matrices with a **prescribed stationary vector**, but the family permits self-loops and the three-state explicit results address reversible matrices; these do not impose the zero-diagonal constraint. Boyd, Diaconis and Xiao (2004) formulate spectral optimization for *symmetric/reversible* walks, typically allowing self-loops, and discuss reversible prescribed-invariant extensions. Reversibility is not imposed here: indeed, away from the uniform stationary law the best \(1/2\)-rate kernels are necessarily nonreversible and defective. Verbeken and Ginis (2026) analyze forward-cycle stochastic matrices with holding entries, rather than the bidirectional no-holding fixed-stationary family. Guerry (2022) studies three-state stochastic **roots/embeddability** with complex spectra; only the institutional abstract could be inspected. No exact fixed-stationary zero-diagonal extremal statement was identified in the accessible material, but uninspected full text and broader older spectral-optimization literature remain originality risks.

## Limitations

The theorem requires exactly three states, prohibits holding transitions, and assumes a fixed strictly positive stationary distribution with largest coordinate less than \(1/2\). It optimizes nonstationary spectral radius, not maximal finite-time mixing, mean-square error, conditioned-branching convergence, or arbitrary-dimensional kernels. Although the proof is complete under these hypotheses, older equivalent representations of the result may exist; independent validation has not been performed.

## References

1. A. Blancas, M. C. Fittipaldi and S. Hernández-Torres, *The Q-process for the general mother-dependent multitype branching process*, arXiv:2610.20896v1, 14 October 2026, esp. §2.2. https://arxiv.org/pdf/2610.20896
2. S. Boyd, P. Diaconis and L. Xiao, *Fastest mixing Markov chain on a graph*, SIAM Review 46 (2004), 667–689. https://www.microsoft.com/en-us/research/wp-content/uploads/2016/02/SIREV042326-1.pdf
3. A. C. M. Ran and Z. E. Teng, *The nonnegative inverse eigenvalue problem with prescribed zero patterns in dimension three*, Electronic Journal of Linear Algebra 40 (2024), 506–537, especially Proposition 6. https://doi.org/10.13001/ela.2024.7965
4. S. Kirkland, *Eigenvalues for stochastic matrices with a prescribed stationary distribution*, Electronic Journal of Linear Algebra 39 (2023), 556–571. https://journals.uwyo.edu/index.php/ela/article/download/7971/6411/18315
5. B. Verbeken and V. Ginis, *On the spectral region of n-cycle stochastic matrices*, arXiv:2606.10143 (2026). https://arxiv.org/pdf/2606.10143
6. M.-A. Guerry, *Matrix roots and embedding conditions for three-state discrete-time Markov chains with complex eigenvalues*, Communications in Mathematics and Statistics 10 (2022), 435–450. https://doi.org/10.1007/s40304-020-00226-3
7. J. A. Fill and J. Kahn, *Comparison inequalities and fastest-mixing Markov chains*, arXiv:1109.6075 (2011). https://arxiv.org/abs/1109.6075
