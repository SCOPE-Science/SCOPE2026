# Simultaneous near-edge Dirichlet poles and oscillation in sum-system counts

## Finding
For a fixed integer \(m\ge3\), let \(\mathcal N_m(n)\) count labelled \(m\)-part sum systems with every component set of cardinality at least two, whose Minkowski sum is \(\{0,1,\ldots,n-1\}\), each represented exactly once. Set \(\mathcal N_m(1)=0\), and let
\[
 A_m(X)=\sum_{1\le n\le X}\mathcal N_m(n),\qquad
 F_m(s)=\sum_{n\ge1}\frac{\mathcal N_m(n)}{n^s}.
\]
For each \(j\in\{1,\ldots,m-1\}\), let \(\rho_j>1\) be the unique real number satisfying \(\zeta(\rho_j)=1+1/j\). Define the explicit nonzero real numbers
\[
 R_{m,j}=\frac{m!\,j^{-m}}{-j\zeta'(\rho_j)
       \prod_{\substack{1\le h\le m-1\\h\ne j}}(1-h/j)}.
\]
**Simultaneous pole replication.** There exist real \(T_k\to+\infty\) and, for each \(j\), distinct simple nonreal poles \(s_{j,k}\) of \(F_m\) with
\[
 s_{j,k}-(\rho_j+iT_k)\longrightarrow0,
 \qquad \operatorname{Res}_{s=s_{j,k}}F_m(s)\longrightarrow R_{m,j}.
\]
Thus all \(m-1\) real pole levels are simultaneously reproduced near the **same** unbounded sequence of imaginary heights, including their individual residues. In particular, the rightmost real pole is \(r_m=\rho_{m-1}\), and the supremum of the real parts of nonreal poles is exactly \(r_m\), although no nonreal pole lies on that boundary line.

**Sharp obstruction to power savings.** Put
\[
 C_m=\frac{m}{(m-1)^2r_m[-\zeta'(r_m)]}>0.
\]
Then for every fixed \(\varepsilon>0\),
\[
 \boxed{\displaystyle
 A_m(X)-C_mX^{r_m}=\Omega_\pm(X^{r_m-\varepsilon}).}
\]
Here \(\Omega_\pm\) means that, for some positive constant depending on \(m,\varepsilon\), the indicated positive and negative deviations occur for arbitrarily large real \(X\). Consequently, for no \(\delta>0\) can this difference satisfy \(O(X^{r_m-\delta})\). The leading asymptotic itself is previously available; the finding concerns the pole replication and unavoidable **two-sided** near-leading-size errors.

## Assumptions and scope
The parameter \(m\ge3\) is fixed as \(X\to\infty\). Labels distinguish the \(m\) component sets. The Riemann zeta function is understood via its absolutely convergent series in \(\operatorname{Re}s>1\), with its usual meromorphic continuation elsewhere. The statement is independent of the locations of zeta zeros in the critical strip. No bound uniform in increasing \(m\) is asserted. The \(\Omega_\pm\) assertion concerns the ordinary unsmoothed summatory function.

## Proof
**1. Exact meromorphic function.** Huxley–Lettington–Schmidt [1, Theorem 5.3] provide, for \(\operatorname{Re}s>r_m\), the nonnegative Dirichlet expansion
\[
 F_m(s)=\sum_{L\ge1}m!\,S(L-1,m-1)[\zeta(s)-1]^L.
\]
The classical Stirling generating identity (set \(z=\zeta(s)-1\)) evaluates it to
\[
 \boxed{\displaystyle
 F_m(s)=\frac{m!z^m}{\prod_{j=1}^{m-1}(1-jz)}.}
\]
This rational expression extends meromorphically to the complex plane. At \(s=\rho_j\), one and only one denominator factor vanishes. Since \(\zeta'(\rho_j)=-\sum_{n\ge2}(\log n)n^{-\rho_j}<0\), the pole is simple and has residue \(R_{m,j}\) displayed above. At the rightmost such point, the formula simplifies to
\[
 R_{m,m-1}=\frac{m}{(m-1)^2[-\zeta'(r_m)]}=r_mC_m.
\]

**2. Common vertical almost periods.** For every compact set \(K\subset\{\operatorname{Re}s>1\}\) there exists a sequence \(T_k\to+\infty\) such that
\[
 \sup_{s\in K}|\zeta(s+iT_k)-\zeta(s)|\longrightarrow0.
\]
Indeed, select a finite prime set so that the Dirichlet series tail over integers with a prime factor outside that set, together with the remaining large-integer tail, is uniformly small on \(K\). Simultaneous Diophantine recurrence gives arbitrarily large positive \(T_k\) for which \(p^{-iT_k}\) is arbitrarily close to one for each selected prime. The finitely many retained terms then recur, while the uniformly absolutely convergent tails remain small. A diagonal sequence works on every fixed compact; Cauchy's integral formula also gives local uniform convergence of derivatives. Equivalently, this is the usual vertical almost-periodicity of absolutely convergent Dirichlet series, specialized to \(\zeta\) in \(\operatorname{Re}s>1\).

Choose pairwise disjoint small closed discs around all the \(\rho_j\), entirely in \(\operatorname{Re}s>1\), on each of which \(\zeta(s)-(1+1/j)\) has its single simple zero at the centre. On the boundary circle its modulus has a strictly positive minimum. Uniform approximation of \(\zeta(s+iT_k)\) and Rouché's theorem imply that \(\zeta(s+iT_k)-(1+1/j)\) has exactly one zero \(u_{j,k}\) in that disc. Shrinking the discs and taking a diagonal subsequence yields \(u_{j,k}\to\rho_j\), simultaneously for all \(j\). Thus \(s_{j,k}=u_{j,k}+iT_k\) are simple nonreal poles of the same rational expression, and \(\zeta'(s_{j,k})\to\zeta'(\rho_j)\). Substituting in the simple-pole residue formula proves simultaneous residue convergence. This argument reconstructs the nonreal-pole and residue conclusion; no finite search for complex roots is used as an infinite proof.

**3. The exact right edge.** If \(\operatorname{Re}s>r_m\), absolute convergence gives
\[
 |\zeta(s)-1|\le\zeta(\operatorname{Re}s)-1<\frac1{m-1}.
\]
No denominator factor of \(F_m\) can vanish there. If \(s=r_m+it\) with \(t\ne0\), equality in the triangle inequality would require all \(n^{-it}\), \(n\ge2\), to have the same phase. Comparing \(n=2\) and \(n=4\) forces \(2^{-it}=1\); comparison with \(n=3\) then forces \(3^{-it}=1\). Irrationality of \(\log2/\log3\) implies \(t=0\), a contradiction. Hence \(|\zeta(r_m+it)-1|<1/(m-1)\) for \(t\ne0\). The highest real pole is \(r_m\); the nonreal poles in Step 2 approach this real part from below.

**4. Two-sided errors.** Apply the general nonreal-pole oscillation theorem of Lowry-Duda [2, Theorem 2] to the meromorphic Dirichlet series \(F_m(s)\) and the Perron weight \(1/s\). Its nonreal poles have real-part supremum \(r_m\), and the only real pole of \(F_m(s)/s\) with real part at least \(r_m\) is at \(r_m\). Its residue contributes exactly \(C_m X^{r_m}\), by Step 1. The theorem gives two-sided \(\Omega(X^{r_m-\varepsilon})\) deviations for the half-weighted summatory function, for every \(\varepsilon>0\). At an integer, the half-weighted value is the mean of the left and right limits of the ordinary step function, so both signs of unbounded deviations persist for the ordinary sum by choosing the appropriate side of the jump. This yields the claimed \(\Omega_\pm\).

For completeness, a direct argument establishes the weaker no-power-saving conclusion without [2]. If \(A_m(X)-C_mX^{r_m}=O(X^{r_m-\delta})\), partial summation would extend
\[
 F_m(s)-\frac{C_ms}{s-r_m}
 =s\int_1^\infty[A_m(x)-C_mx^{r_m}]x^{-s-1}\,dx
\]
analytically throughout \(\operatorname{Re}s>r_m-\delta\) (apart from removable matters at the lower integration endpoint). That would exclude every nonreal pole in that half-plane, contradicting Step 2.

## Verification
The standalone `verify.py` independently checks the rational Stirling generating-function identity and compares its associated formal Dirichlet coefficients with a direct finite convolution expansion. It uses exact integers. These are finite algebraic checks, not a computational proof of vertical recurrence, Rouché's theorem, or oscillatory asymptotics. The latter follow from the explicit complex-analytic argument and the cited general oscillation theorem [2].

## Relationship to prior work
Huxley, Lettington and Schmidt [1] supply the source series, implicit rightmost root, and underlying sum-system counts; the rational Stirling evaluation is elementary and is not claimed new. Previous sum-system work [3] gives the corresponding counting framework. Hwang and Janson [4, Section 2] cover a related family of ordered factorization Dirichlet series, including the two-part zeta-root analogy and leading asymptotics; this is not the claim here. Arias de Reyna and van de Lune [5, Sections 2–3] investigate extremal \(\zeta(s)=a\) points for positive \(a\), providing a close antecedent of the zeta-value location argument, but do not state the simultaneous residue ladder for the sum-system series. Lowry-Duda [2] establishes the **general** pole-to-oscillation implication, not the specific verification of its near-edge pole hypothesis for these counting functions. The contribution here is the simultaneous evaluated pole-and-residue structure and its resulting all-\(m\) sharp error obstruction, not the general theorems being used. An unindexed equivalent application remains a historical-priority risk.

## Limitations
No explicit lower bound on the magnitude of the oscillation constant, no effective location or spacing of replicated poles, and no uniformity in \(m\) are supplied. This does not improve the previously known leading asymptotic or establish an upper error bound. The two-sided asymptotic obstruction is derived using a published general theorem whose full assumptions are checked above. Prior art may contain an equivalent application despite targeted searches; independent assessment has not been performed.

## References
1. M. N. Huxley, M. C. Lettington, K. M. Schmidt, *On Divisor Function Polynomials and Dirichlet Series*, arXiv:2610.13864v1 (first posted 2026-10-09), especially Theorem 5.3 and Section 5. https://arxiv.org/abs/2610.13864.
2. D. Lowry-Duda, *Non-real Poles and Irregularity of Distribution*, arXiv:1910.09969 (2019), especially Theorem 2 and its proof. https://arxiv.org/abs/1910.09969.
3. M. C. Lettington, K. M. Schmidt, *Divisor Functions and the Number of Sum Systems*, arXiv:1910.02455 (2019). https://arxiv.org/abs/1910.02455.
4. H.-K. Hwang, S. Janson, *Delange's Tauberian theorem and asymptotic normality of random ordered factorizations of integers*, arXiv:0902.3419 (2009), especially Section 2. https://arxiv.org/abs/0902.3419.
5. J. Arias de Reyna, J. van de Lune, *Some bounds and limits in the theory of Riemann's zeta function*, arXiv:1107.5134 (2011), especially Theorem 3.1. https://arxiv.org/abs/1107.5134.
