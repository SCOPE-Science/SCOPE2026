# Universal Fourier spectral transfer under pendant-colour amplification

## Finding

Let \(H\) be any finite simple graph with \(n\ge1\) vertices and at least one proper colouring by \(q\ge3\) colours. For every integer \(s\ge1\), form \(H^{[s]}\) by attaching \(s\) independent pendant leaves to *each* vertex of \(H\). Sample proper \(q\)-colourings uniformly, and consider the constant function together with every nontrivial one-site additive character \(\chi_{v,a}(x)=\exp(2\pi i a x_v/q)\), where \(1\le a\le q-1\). All Gram matrices below are normalized by the uniform probability measure, not by the unnormalized counting measure.

Let \(C\) be the \(n\)-by-\(n\) Gram matrix of a fixed nonzero colour frequency on \(H\), and write its eigenvalues with multiplicities as \(c_1,\ldots,c_n\ge0\). Set \(r=(q-1)^{-1}\), \(\delta=1-r^2>0\), and
\[
\lambda_{\pm}(c;s)
=\frac{\delta+(1+s r^2)c\ \pm\sqrt{[\delta+(1+s r^2)c]^2-4\delta c}}{2}.
\]
Then the **full probability-normalized Gram spectrum** on \(H^{[s]}\) consists precisely of the eigenvalue \(1\) once and, repeated independently for each of the \(q-1\) nonzero colour frequencies, the numbers
\[
\{\lambda_-(c_j;s),\lambda_+(c_j;s):1\le j\le n\}
\quad\text{and}\quad
\{\delta\}^{n(s-1)}.
\]
This is an exact multiset statement even when \(C\) is singular or eigenvalues coincide. The nullity is exactly \((q-1)\dim\ker C\), independent of the number of attached leaves. When \(C\) is invertible, the determinant of the entire one-frequency Gram block equals \(\delta^{ns}\det C\).

If \(C\) is positive definite, let \(a=\lambda_{\min}(C)>0\) and \(b=\lambda_{\max}(C)\). The **sharp** lower and upper bounds of the entire constant-plus-characters Gram matrix on \(H^{[s]}\) are, respectively, \(\lambda_-(a;s)\) and \(\lambda_+(b;s)\). Hence its squared singular-value conditioning constant is
\[
\boxed{\kappa_s^2=\frac{\lambda_+(b;s)}{\lambda_-(a;s)}.}
\]
It is strictly larger than the corresponding core value \(b/a\), and **strictly increases with \(s\)**. Furthermore, for every fixed colour palette and fixed core graph satisfying \(C>0\),
\[
\boxed{\kappa_s^2=\frac{b r^4}{1-r^2}\,s^2+O_{H,q}(s).}
\]
The leading coefficient depends on the core only through its largest one-frequency Gram eigenvalue \(b\), not its smallest eigenvalue \(a\).

For the explicit natural family \(H=K_n\), \(n\ge3\), \(q\ge n\), the core spectrum is \((q-n)/(q-1)\) once and \(q/(q-1)\) with multiplicity \(n-1\). Consequently the decorated sampling system has exactly \(q-1\) dependencies when \(q=n\), regardless of \(s\), and it is linearly independent for every \(q\ge n+1\), with sharp constants obtained by substituting these two eigenvalues into the displayed transfer formula.

## Assumptions and scope

A proper colouring is a map \(x:V(H)\to\mathbb Z/q\mathbb Z\) assigning different colours at adjacent vertices. All colourings have equal mass. The added leaves are pairwise nonadjacent, including leaves with the same parent. The core is allowed to be disconnected, and \(q\ge3\) is essential: with two colours a pendant colour is deterministic, the conditional variance \(\delta\) vanishes, and the assertion of rank persistence in its stated form can fail. If the core has no proper \(q\)-colouring, none of the probability-normalized matrices is defined. The conditioning statement requires \(C\) positive definite; no positive lower Riesz bound is claimed for singular cores.

For a collection \(f_1,\ldots,f_M\) the Gram entry is \(\mathbb E[f_i\overline{f_j}]\). This convention fixes all scaling, conjugation, and eigenvalue multiplicities. The squared singular-value condition number is the ratio of the maximum and minimum positive Gram eigenvalues only when the sampled system is linearly independent; a singular system is reported separately by nullity.

## Proof

**1. Reduction to one colour frequency.** Simultaneous addition of any colour \(t\in\mathbb Z/q\mathbb Z\) preserves proper colourings and their uniform law. Thus \(\chi_{v,a}\) has mean zero for nonzero \(a\), and two functions with distinct colour frequencies are orthogonal. Each of the \(q-1\) nonzero-frequency Gram matrices is identical: because the colouring law is invariant under every permutation of the \(q\) colour labels, for distinct vertices \(u,v\) the pair \((x_u,x_v)\) assigns equal pairs uniformly within the diagonal and unequal pairs uniformly off it. Hence \(\mathbb E\chi_{u,a}\overline{\chi_{v,a}}\) is real and independent of nonzero \(a\), with value \([q\Pr(x_u=x_v)-1]/(q-1)\) (and value \(1\) when \(u=v\)). This is the common real symmetric positive-semidefinite matrix \(C\). The constant contributes one orthogonal unit eigenvalue.

**2. Conditional lift.** Each colouring of \(H\) has exactly \((q-1)^{ns}\) proper extensions to \(H^{[s]}\). Thus the core retains its uniform law. Given the core colouring, distinct leaves are conditionally independent and each leaf at parent \(v\) is uniform among the \(q-1\) other colours. For nonzero \(a\),
\[
\mathbb E[\chi_{\mathrm{leaf},a}\mid x_{\mathrm{parent}}]
=-r\chi_{\mathrm{parent},a},
\qquad
\mathbb E\bigl[|\chi_{\mathrm{leaf},a}+r\chi_{\mathrm{parent},a}|^2\mid x_{\mathrm{parent}}\bigr]=\delta.
\]
Every pair of distinct conditional leaf residuals has zero conditional covariance. If \(R\) is the \(n\)-by-\(ns\) matrix whose column for a leaf is the unit vector of its parent, the full one-frequency Gram matrix is exactly
\[
G_s=\begin{pmatrix}
C&-rCR\\
-rR^{\mathsf T}C&\delta I_{ns}+r^2R^{\mathsf T}CR
\end{pmatrix}.
\]
This identity uses the conditional law of the *colouring model*, not an adjacency, Laplacian, or distance matrix of the corona graph.

**3. Complete invariant-space decomposition.** Within the \(s\) leaf coordinates at each core vertex, split off the normalized all-ones vector and its \((s-1)\)-dimensional orthogonal complement. The contrasts at all \(n\) vertices contribute \(\delta\) with multiplicity \(n(s-1)\). On the remaining \(2n\)-dimensional core-plus-mean-leaf space, the matrix becomes
\[
\begin{pmatrix}
C&-r\sqrt s\,C\\
-r\sqrt s\,C&\delta I_n+s r^2 C
\end{pmatrix}.
\]
Diagonalizing \(C\) gives precisely the two-by-two blocks
\[
B_s(c)=\begin{pmatrix}c&-r\sqrt s\,c\\-r\sqrt s\,c&\delta+s r^2 c\end{pmatrix}
=\begin{pmatrix}0&0\\0&\delta\end{pmatrix}
+c\begin{pmatrix}1\\-r\sqrt s\end{pmatrix}
\begin{pmatrix}1&-r\sqrt s\end{pmatrix}.
\]
Each block has trace \(\delta+(1+s r^2)c\) and determinant \(\delta c\). Its roots are the displayed \(\lambda_\pm(c;s)\). Since \(\delta>0\), every block has zero eigenvalue if and only if \(c=0\), and then it has exactly one such eigenvalue. Counting frequency sectors proves the full spectrum and nullity. The product of all block determinants and contrast eigenvalues gives \(\det G_s=\delta^{ns}\det C\), without a need to divide by \(C\) in the singular case.

**4. Exact extrema and strict conditioning.** Suppose \(C>0\). For every \(c>0\), \(B_s(c)\) has a nonzero off-diagonal entry. Its Rayleigh quotients and determinant imply
\[
0<\lambda_-(c;s)<\min(c,\delta),
\qquad
\lambda_+(c;s)>\max(c,\delta).
\]
Both eigenvalues are strictly increasing functions of \(c>0\): from the rank-one representation above, the derivative of either simple eigenvalue is the squared inner product of its normalized eigenvector with \((1,-r\sqrt s)\). That inner product is nonzero, because a vector orthogonal to this rank-one direction would have to be an eigenvector of the diagonal matrix \(\operatorname{diag}(0,\delta)\), whose two coordinate eigenvectors are not orthogonal to that direction. As \(C\) has unit diagonal, \(a\le1\le b\). Thus the orthogonal constant eigenvalue and the leaf-contrast value \(\delta\) cannot be extremal: the least and greatest full Gram eigenvalues are respectively \(\lambda_-(a;s)\) and \(\lambda_+(b;s)\). The inequalities \(\lambda_-(a;s)<a\), \(\lambda_+(b;s)>b\) prove strict deterioration relative to the undecorated core.

For fixed \(c>0\), the determinant \(\delta c\) is independent of \(s\), while the trace \(\delta+(1+s r^2)c\) strictly increases with \(s\). Because the eigenvalues are distinct and positive, their sum increasing at fixed product makes \(\lambda_+(c;s)\) strictly increase and \(\lambda_-(c;s)\) strictly decrease. Therefore \(\kappa_s^2\) is strictly increasing for positive integers \(s\).

**5. Sharp asymptotic and clique example.** At each fixed \(c>0\), trace and determinant yield
\[
\lambda_+(c;s)=s r^2 c+O_{c,r}(1),
\qquad
\lambda_-(c;s)=\frac{\delta}{s r^2}+O_{c,r}(s^{-2}).
\]
Substitute \(c=b\) in the first formula and \(c=a\) in the second to obtain the claimed \(s^2\) coefficient and the remainder \(O_{H,q}(s)\). For \(H=K_n\), every two distinct core vertices have distinct colours, so \(C_{ii}=1\), \(C_{ij}=-r\) for \(i\ne j\). The matrix \(C=(1+r)I_n-rJ_n\) has eigenvalues \(1-(n-1)r=(q-n)/(q-1)\) and \(1+r=q/(q-1)\), with the stated multiplicities. This finishes the classification.

## Verification

A standalone Python 3 program, `check.py`, reconstructs uniform colouring measures for six finite core/decoration/palette cases (triangle with three or four colours, path and cycle with three colours, edgeless graph, and four-clique), compares the directly enumerated complex Fourier Gram matrix to the proposed real block formula, and independently compares its eigenvalues with the predicted two-by-two roots. It also checks nullities, sharp extrema, strict conditioning deterioration, and large-leaf asymptotics. The program passed **228 assertion groups**. Its exhaustive enumeration covers only the specified small instances: the proof of the all-graph, all-palette theorem is the exact conditional-moment and orthogonal-decomposition argument above, not extrapolation from experiments.

## Relationship to prior work

Proper colourings are a special case of the hard-constraint \(H\)-colouring framework described by Engbers and Galvin; their results concern colourings on tori and asymptotic colour distributions. Furmańczyk and Kubale study equitable chromatic numbers and algorithms for graph coronas, not Gram operators of uniformly sampled colourings. Liu and Zhou, and Lu and Miao, give graph adjacency/Laplacian spectral transfer results for *neighbourhood* and *subdivision* coronas. Those graph-matrix results neither identify the present conditional colouring Gram matrix nor imply the rank, all-frequency Riesz bounds, or quadratic conditioning coefficient; the current proof is based instead on colouring conditional independence. The two-by-two block technique itself is standard matrix analysis and is **not** claimed as a new general algebraic principle.

Other earlier first-coordinate Fourier computations for particular proper-colouring ensembles, such as cycles, complete bipartite graphs and complete multipartite graphs, furnish possible inputs \(C\) but do not establish the universal pendant transfer for arbitrary core graphs. Comparisons were made at the level of the mathematical statements, including possible reductions through earlier spectral-corona formulas. A previously published Potts-covariance or conditional-variance treatment could in principle contain the full result in another vocabulary; this residual originality risk remains.

## Limitations

This is a finite-graph, proper-colouring, first-coordinate Fourier theorem. It does not cover higher character degrees, non-uniform Gibbs weights, arbitrary attachments with edges between new vertices, or two-colour deterministic leaves. Except for the complete-graph example, the theorem transfers rather than explicitly evaluates the core Gram spectrum; computing that spectrum can be difficult. An earlier generic conditional-covariance theorem may contain an implicit version of the transfer, and novelty should be independently checked against that wider literature. The exact asymptotic is for fixed finite core and fixed palette as the number of leaves increases; no uniform joint growth theorem in the graph order or palette size is asserted.

## References

1. J. Engbers and D. Galvin, *H-coloring tori*, arXiv:1101.0840v1, first posted 2011-01-04. https://arxiv.org/abs/1101.0840
2. H. Furmańczyk and M. Kubale, *Equitable coloring of corona products of cubic graphs is harder than ordinary coloring*, arXiv:1409.0650v1, first posted 2014-09-02. https://arxiv.org/abs/1409.0650
3. X. Liu and S. Zhou, *Spectra of the neighbourhood corona of two graphs*, arXiv:1209.5906v1, first posted 2012-09-26. https://arxiv.org/abs/1209.5906
4. P. Lu and Y. Miao, *Spectra of the subdivision-vertex and subdivision-edge coronae*, arXiv:1302.0457v1, first posted 2013-02-03. https://arxiv.org/abs/1302.0457
