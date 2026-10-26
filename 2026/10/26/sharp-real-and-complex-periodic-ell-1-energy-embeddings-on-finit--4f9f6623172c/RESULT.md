# Sharp real and complex periodic \(\ell^1\)--energy embeddings on finite cycles

## Finding
Let \(N\ge3\) be an integer and let \(x=(x_j)_{j\in\mathbb Z/N\mathbb Z}\) be a real- or complex-valued sequence with \(\sum_jx_j=0\). Put \(E_N(x)=\sum_{j=0}^{N-1}|x_{j+1}-x_j|^2\) (indices modulo \(N\)) and \(m=\lfloor N/2\rfloor\). The *sharp* constants in
\[
\sum_{j=0}^{N-1}|x_j|\le C_N^{\mathbb F}\sqrt{E_N(x)}
\qquad(\mathbb F\in\{\mathbb R,\mathbb C\})
\]
are
\[
\boxed{(C_N^{\mathbb R})^2=\frac{m(N-m)\,[m(N-m)+2]}{3N}},
\qquad
\boxed{C_N^{\mathbb C}=\frac{\sqrt N}{2\sin(\pi/N)}}.
\]
For real nonzero \(x\), equality holds precisely when \(x\) is a nonzero real multiple of \(Gs\), where \(G\) is the Moore--Penrose inverse of the unnormalized cycle Laplacian and \(s\) is \(+1\) on one contiguous cyclic interval of length \(m\) or \(N-m\) and \(-1\) elsewhere. For complex nonzero \(x\), equality holds precisely for single first-frequency Fourier modes \(x_j=c\exp(\pm 2\pi i j/N)\) when \(N\ne4\); at \(N=4\), all extremizers have the form \((a,b,-a,-b)\) with \(|a|=|b|>0\).

The real constant is strictly smaller than the complex one for every \(N\ge3\) except \(N=4\), when they coincide. Moreover
\[
\lim_{N\to\infty}\frac{C_N^{\mathbb R}}{C_N^{\mathbb C}}=\frac{\pi}{2\sqrt3}<1.
\]

## Assumptions and scope
The cyclic graph has \(N\ge3\) vertices, *unweighted* adjacent edges, and the unnormalized energy displayed above. There is no boundary extension: the first and last vertices are adjacent. All vectors have zero ordinary sum, not merely zero weighted average. The constants apply to the full real and complex mean-zero sequence spaces separately. No statement is made here for higher differences, weighted cycles, or nonzero prescribed means.

## Proof
Write \(L=2I-S-S^*\), where \((Sx)_j=x_{j-1}\), and let \(G=L^+\). Then \(E_N(x)=\langle Lx,x\rangle\), \(G\mathbf1=0\), and \(LG=I-N^{-1}\mathbf1\mathbf1^*\). The cyclic Green entries are
\[
G_{ij}=\frac{N^2-1}{12N}-\frac{d(N-d)}{2N},\qquad d=(j-i)\bmod N\in\{0,\ldots,N-1\}.
\]
The displayed matrix has zero row sums and satisfies the defining pseudoinverse identities; hence the formula also follows directly by solving the second-difference equation. It is consistent with the cycle Green formula in Ellis (2003), once his normalized Laplacian is converted to the unnormalized one.

**Real case.** Since \(x\) is real, \(\|x\|_1=\max_{s\in\{-1,1\}^N}s^Tx\). By Cauchy--Schwarz on the orthogonal complement of constants,
\[
s^Tx=\langle G^{1/2}s,L^{1/2}x\rangle\le\sqrt{s^TGs}\sqrt{E_N(x)}.
\]
Conversely, for each nonconstant sign vector \(s\), taking \(x=Gs\) shows the supremum of \(\|x\|_1/\sqrt{E_N(x)}\) is at least \(\sqrt{s^TGs}\). Thus its square equals \(\max_{s\in\{\pm1\}^N}s^TGs\).

Let \(A\) be the \(+1\) set of \(s\) and \(|A|=k\). The identities \(G\mathbf1=0\) and \(s=2\mathbf1_A-\mathbf1\) imply \(s^TGs=4\mathbf1_A^TG\mathbf1_A\). For the occupied vertices in clockwise order, let their \(k\) successive cyclic gaps be \(g_1,\ldots,g_k\ge1\), with \(\sum_i g_i=N\). For each ordered pair of occupied indices \(i<j\), write \(t_{ij}=g_i+\cdots+g_{j-1}\). The Green formula gives
\[
\mathbf1_A^TG\mathbf1_A=\frac{k^2(N^2-1)}{12N}-\frac1N\sum_{i<j}t_{ij}(N-t_{ij}).
\]
For fixed \(k\), the last sum is *strictly concave* in the free gaps \((g_1,\ldots,g_{k-1})\): its Hessian is minus twice a sum of squared linear forms; the adjacent-pair terms already contain every free coordinate with a strictly negative square. On the simplex \(g_i\ge1\), \(\sum_i g_i=N\), a strictly concave function is strictly larger at any nonvertex than the minimum of its values at vertices. Thus the sum is minimized only at vertices, where all but one gap are \(1\). Precisely these vertices describe contiguous cyclic intervals \(A\) (the \(k=1\) case is immediate). The constant-sign cases \(k=0,N\) have zero energy in the dual and cannot maximize.

For a consecutive interval of size \(k\), its unordered separations are \(d=1,\ldots,k-1\), with multiplicity \(k-d\). Therefore
\[
\sum_{i<j}t_{ij}(N-t_{ij})
=\sum_{d=1}^{k-1}(k-d)d(N-d)
=\frac{k(k^2-1)(2N-k)}{12},
\]
so
\[
s^TGs=\frac{k(N-k)\,[k(N-k)+2]}{3N}.
\]
This is strictly increasing as a function of \(k(N-k)\ge0\), which is maximal exactly when \(k=m\) or \(k=N-m\). Equality in energy Cauchy--Schwarz forces \(x\) to be a real multiple of \(Gs\), and the sign-maximizing argument proves that every vector of this form does attain equality, completing the real extremizer classification.

**Complex case.** The Cauchy--Schwarz inequality \(\|x\|_1\le\sqrt N\|x\|_2\) and the cycle spectral gap \(E_N(x)\ge4\sin^2(\pi/N)\|x\|_2^2\) give the complex constant. Equality holds for any first-frequency complex Fourier character. Every extremizer must belong to the first eigenspace \(x_j=a\zeta^j+b\zeta^{-j}\), \(\zeta=e^{2\pi i/N}\), and have constant \(|x_j|\). Expanding gives \(|x_j|^2=|a|^2+|b|^2+2\operatorname{Re}(a\bar b\zeta^{2j})\). When \(N\ne4\), the order of \(\zeta^2\) is at least \(3\), so constancy forces \(a\bar b=0\). When \(N=4\), the first eigenspace is exactly \((a,b,-a,-b)\), with constant magnitude precisely when \(|a|=|b|\).

**Field gap and asymptotics.** If a nonzero real vector achieved the complex constant, it would have constant entry magnitudes and belong to the complex first eigenspace. For \(N\ne4\), the classification above would make it a single complex Fourier character, which cannot be real at every vertex for \(N\ge3\). For \(N=4\), the real vector \((1,1,-1,-1)\) achieves both constants. Finally \(m(N-m)=N^2/4+O(1)\) and \(\sin(\pi/N)=\pi/N+O(N^{-3})\) yield the stated ratio.

## Verification
The independent, standalone diagnostic `check.py` uses exact rational arithmetic for the cycle Green matrix, checks its defining identities, exhaustively enumerates every sign vector for \(3\le N\le11\), compares each maximum with the proposed real formula, and checks that maximizing signs are exactly the interval patterns. It also compares the real and complex constants numerically on those dimensions. Run: `python3 check.py`. All exact finite checks passed. This finite computation does not verify the all-\(N\) proof; the strict-concavity and Fourier arguments above establish the universal claims.

## Relationship to prior work
Hindov--Nitzan--Olsen--Rydhe (2026, arXiv:2610.19010v1) solve the sharp \(\ell^1\)--difference \(\ell^2\) problem for *zero-extended finite sequences*, including higher differences. Their boundary operator differs from the cyclic difference acting on mean-zero periodic vectors; their extremizer theorem therefore does not imply either present periodic constant. Frank--Ivanisvili (2026, arXiv:2605.29035v1) establish sharp logarithmic and cubic Sobolev inequalities on finite cycles, using a cycle spectral-gap input, but do not determine the present real \(\ell^1\)--energy constant or its sign-block equality classification. Ellis (2003, arXiv:math/0309080v2) gives the previously known exact Green kernel for cycles, which is used here; the additional signed quadratic maximization, complete extremizers, and scalar-field separation are separate steps.

## Limitations
This is a sharp finite-cycle result for the unweighted first difference with a zero-mean constraint; no weighted or higher-order extension is asserted. The novelty comparison includes accessible primary texts and mathematical research-index searches, but unlocated older graph-Sobolev or resistance-energy literature could contain an equivalent formula. No independent audit or publication-priority certification has been performed.

## References
1. R. Hindov, S. Nitzan, J.-F. Olsen, E. Rydhe, *A sharp discrete Sobolev inequality and left inverses of higher order differences*, arXiv:2610.19010v1, publicly posted 13 October 2026. https://arxiv.org/html/2610.19010v1
2. R. L. Frank, P. Ivanisvili, *The sharp log Sobolev inequality on finite cycles*, arXiv:2605.29035v1, 27 May 2026. https://arxiv.org/html/2605.29035v1
3. R. B. Ellis, *Discrete Green's functions for products of regular graphs*, arXiv:math/0309080v2 (first public version September 2003). https://arxiv.org/html/math/0309080v2
