# Exact approximate-square complexity and dimension rigidity for column-tree moving holes

## Finding
Let \(Q_k(F)\) count the nonempty *symbolic approximate squares* with \(k\) prescribed column digits and \(\theta_k=\lfloor k\log m/\log n\rfloor\) prescribed full digit pairs. For every deterministic column-tree forbidden-symbol environment, independently of how its labels vary,
\[
Q_k(F)=(A-1)^{\theta_k}B^{k-\theta_k}\quad(k\ge0).
\]
The corresponding planar survivor set has exactly determined lower and upper box-counting dimensions and packing dimension:
\[
\dim_{\mathrm P}K_F=\underline{\dim}_{\mathrm B}K_F=\overline{\dim}_{\mathrm B}K_F=s,
\qquad s=\frac{\log B}{\log m}+\frac{\log((A-1)/B)}{\log n}.
\]
For the independent forbidden labels of Kong, Ma and Simon (2026), the almost-sure Hausdorff dimension is strictly smaller than \(s\), except for a sharp explicit equality case described below. In particular, the counting/packing conclusion is **deterministic for every environment**, not merely almost sure.

## Assumptions and scope
Let \(2\le m<n\) be integers, and let \(\mathcal A\subseteq\{0,\ldots,m-1\}\times\{0,\ldots,n-1\}\) be a finite digit set. Its occupied column alphabet is \(\mathcal B=\{i:(i,j)\in\mathcal A\text{ for some }j\}\); write \(A=|\mathcal A|\), \(B=|\mathcal B|\), and \(\ell_b=|\{j:(b,j)\in\mathcal A\}|\). Assume \(B\ge2\) and \(\ell_b\ge2\) for every \(b\in\mathcal B\).

An **environment** is any map \(F:\mathcal B^*\to\mathcal A\), including arbitrary nonrandom maps. A sequence of digits \(d=(d_t)_{t\ge1}\in\mathcal A^{\mathbb N}\) survives when, for every \(t\ge0\), its next symbol satisfies \(d_{t+1}\ne F(\tau(d_1)\cdots\tau(d_t))\), where \(\tau(i,j)=i\). Let \(\Sigma_F\) denote the closed set of surviving sequences, and let \(K_F\) be its image under \(\Pi(d)=(\sum_{t\ge1}i_t m^{-t},\sum_{t\ge1}j_t n^{-t})\).

Put \(\lambda=\log m/\log n\in(0,1)\). An approximate square of order \(k\) is indexed by the first \(k\) column digits and first \(\theta_k=\lfloor\lambda k\rfloor\) full pairs. Its geometric rectangle has horizontal width \(m^{-k}\) and vertical height \(n^{-\theta_k}\). Count distinct *symbolically indexed* rectangles meeting \(K_F\) (possible shared boundary codings do not change the count).

For the probabilistic comparison only, let the labels \(F(v)\) be iid with symbol distribution \(\pi=(\pi_\gamma)_{\gamma\in\mathcal A}\), set \(\rho_b=\sum_{\tau(\gamma)=b}\pi_\gamma\), and use the almost-sure Hausdorff-dimension identity proved in the cited 2026 source.

## Proof
**1. Exact complexity.** A surviving full-pair prefix of length \(t\) has exactly \(A-1\) surviving choices for its next full pair: only the single label \(F(v)\) indexed by its column prefix \(v\) is excluded. Hence there are exactly \((A-1)^t\) allowed full-pair prefixes of length \(t\). Fix one of length \(\theta_k\). At any subsequent column-prefix vertex, every prescribed column \(b\) has at least \(\ell_b-1\ge1\) allowed rows, so *every* one of the \(B\) columns is extendible. By induction, there are exactly \(B^{k-\theta_k}\) column-word continuations to depth \(k\). All such finite patterns extend to infinite survivors by the same inequality \(\ell_b-1\ge1\). Conversely every surviving approximate square arises uniquely from this data. Multiplication proves the exact formula, including \(k=0\).

**2. Lower and upper box dimensions.** For \(r_k=m^{-k}\), we have \(r_k\le n^{-\theta_k}<n r_k\). The rectangles indexed above are distinct axis-aligned grid cells, with sides comparable to \(r_k\) uniformly in \(k,F\). Their number is \(Q_k(F)\). Covering the intersection of each cell with \(K_F\) by a bounded number (depending only on \(n\)) of radius-\(r_k\) balls gives \(N_{r_k}(K_F)\le C Q_k(F)\). Conversely, each radius-\(r_k\) ball meets at most a constant number of cells in this grid (at most a fixed number of neighboring column/row bins), hence \(N_{r_k}(K_F)\ge c Q_k(F)\). Shared coding boundaries do not affect these comparisons. Therefore
\[
\lim_{k\to\infty}\frac{\log N_{r_k}(K_F)}{-\log r_k}
=\frac{\lambda\log(A-1)+(1-\lambda)\log B}{\log m}=s.
\]
Since successive scales have fixed ratio \(m\), the same limit holds over all \(r\downarrow0\), proving both box dimensions.

**3. Packing dimension.** Fix a permitted full-pair prefix \(w\) of length \(t\). The set of surviving infinite continuations after \(w\) is a translated affine image (diagonal scaling by \(m^{-t}\) and \(n^{-t}\)) of a survivor set of the same kind, for the restricted column-subtree environment \(F_w(v)=F(\tau(w)v)\). This affine map is bi-Lipschitz, so the prefix-cylinder image has upper box dimension \(s\) by Step 2. Every nonempty relatively open subset of \(K_F\) contains one such cylinder image: take a coded point inside it and choose a sufficiently long prefix so the whole cylinder lies in the prescribed open ball.

For completeness, consider any countable cover \(K_F\subseteq\bigcup_{j\ge1}E_j\). By compactness, \(K_F\) is a complete metric space. Applying Baire's theorem to the closed sets \(K_F\cap\overline{E_j}\), some \(\overline{E_j}\) contains a nonempty relatively open part of \(K_F\), and hence a cylinder image of upper box dimension \(s\). Since closing a bounded set leaves its upper box dimension unchanged, \(\overline{\dim}_{\mathrm B}E_j\ge s\). The countable-cover characterization of packing dimension implies \(\dim_{\mathrm P}K_F\ge s\). The universal inequality \(\dim_{\mathrm P}K_F\le\overline{\dim}_{\mathrm B}K_F=s\) gives equality.

**4. Exact criterion for an almost-sure gap.** Let \(L_b(F(\varepsilon))=\ell_b-\mathbf1_{\{\tau(F(\varepsilon))=b\}}\), so \(\sum_bL_b=A-1\) for every root label. The 2026 Hausdorff theorem gives almost surely
\[
h_\pi=\frac1{\log m}\log\mathbb E_\pi\left[\sum_{b\in\mathcal B}L_b^\lambda\right].
\]
Strict concavity of \(z\mapsto z^\lambda\) and the fixed sum \(\sum_bL_b=A-1\) yield the sharp pointwise inequality
\[
\sum_bL_b^\lambda\le B^{1-\lambda}(A-1)^\lambda,
\]
with equality exactly when all \(L_b\) are equal. Taking expectations proves \(h_\pi\le s\). Equality of expectations requires equality at *every root symbol* having positive probability. Two distinct forbidden columns cannot both yield constant vectors: moving the single subtracted unit between two positions changes their difference by two. Thus the forbidden column must almost surely be some fixed \(J\), and equality then requires \(\ell_J-1=\ell_b\) for all \(b\ne J\). Conversely that condition makes all root survivor counts equal almost surely, and the source formula gives \(h_\pi=s\). This establishes the stated if-and-only-if; outside that case strict inequality holds.

## Verification
The self-contained Python 3 script `check.py` exhaustively counts legal finite histories and distinct approximate-square grid indices for eight independently generated finite column-tree environments: four environments for \((m,n,A,B)=(3,4,7,3)\) to depth five, and four for \((2,5,4,2)\) to depth six. It independently checks the exact finite count \(Q_k\) and numerical instances of the strict-concavity equality criterion. The invocation `python3 check.py` produces `ALL_CHECKS_PASS`. These are finite diagnostic checks; all unbounded-depth and dimension claims follow analytically from the proof above.

For the seven-digit example in the source paper, \((m,n,A,B)=(3,4,7,3)\), the deterministic packing and box dimension is exactly \(s=3/2\), while the source's almost-sure Hausdorff dimension under uniform deletion is approximately \(1.49239\). The gap is approximately \(0.00761\).

## Relationship to prior work
Kong, Ma and Simon, *Random Survivor Sets with Moving Holes in Bedford–McMullen Carpets* (arXiv:2610.31440v1, 22 October 2026), introduce precisely the column-prefix forbidden-symbol model and prove its almost-sure Hausdorff-dimension identity. The deterministic full-environment exact approximate-square complexity, box/packing formula and resulting sharp equality classification stated here are not part of their main theorem. Their introduction quotes the classical box/packing dimension formula for a **fixed** Bedford–McMullen digit set, which we use as a methodological comparator, not a new fact.

Kong, Sun and Wang, *Open dynamical systems with a moving hole* (arXiv:2505.02336), treat temporally imposed cylinder holes in expanding systems; their restrictions do not vary with the preceding column word of a planar carpet. Gui and Li (2008) treat patterns shared across all rectangles at a level. Ferguson, Jordan and Rams (arXiv:1206.2219) consider fixed Markov holes. Those models differ from the present column-tree process. 

## Limitations
The exact box/packing assertions require at least two initially allowed pairs **in every** occupied column; if an entire column can disappear, the counting identity is not asserted. The result describes a symbolic/geometric survivor construction, not an autonomous smooth dynamical flow. The packing-dimension statement is for the geometric attractor; the exact integer \(Q_k\) counts symbolically indexed approximate squares, which may share boundary points. No optimality of the assumption is claimed.

The Hausdorff conclusion is almost sure and uses the *published* 2026 Hausdorff formula; it is not an environmentwise Hausdorff classification. Full-text historical coverage was not obtainable for some older studies of randomly generated carpets and fixed Markov holes, so broader historical priority remains a genuine uncertainty. No independent mathematical audit has been performed.

## References
1. D. Kong, C.-Y. Ma, K. Simon, *Random Survivor Sets with Moving Holes in Bedford–McMullen Carpets*, arXiv:2610.31440v1 (posted 22 October 2026), https://arxiv.org/html/2610.31440v1.
2. D. Kong, L. Sun, Y. Wang, *Open dynamical systems with a moving hole*, arXiv:2505.02336 (2025), https://arxiv.org/abs/2505.02336.
3. A. Ferguson, T. Jordan, M. Rams, *The dimension of self-affine sets with holes*, arXiv:1206.2219 (2012), https://arxiv.org/abs/1206.2219.
4. J. Gui, W. Li, *A random version of McMullen–Bedford general Sierpinski carpets and its application*, 2008, as cited and distinguished in reference 1.
5. K. Falconer, *Fractal Geometry*, standard box and packing dimension definitions and the countable-cover characterization of packing dimension.
