# Balanced erasures uniquely optimize a two-modulation cyclic Gabor frame

## Finding
Let \(N\ge3\), let \(\ell\in\{1,\ldots,N-1\}\) with \(2\ell\not\equiv0\pmod N\), and put \(q=|\cos(\pi\ell/N)|\in(0,1)\). In \(\mathbb C^N\), choose the unnormalized two-tap window \(g=e_0+e_1\), cyclic translation \(T_kg(j)=g(j-k)\), and modulation \(M_sg(j)=e^{2\pi isj/N}g(j)\). For an erasure set \(E\subset\mathbb Z_N\), retain the two Gabor atoms \(M_0T_kg\) and \(M_\ell T_kg\) for each \(k\notin E\). Let \(A(E)\) and \(B(E)\) denote the **optimal** lower and upper squared-analysis frame bounds on \(\mathbb C^N\).

Fix an integer \(1\le h\le\lfloor N/2\rfloor\) and require \(|E|=h\). Write the erased indices in cyclic order, and let \(m_1,\ldots,m_h\) be the numbers of retained translation indices in the successive cyclic gaps. Then \(\sum_jm_j=N-h\); a zero gap makes the family non-spanning. For each positive integer \(m\), define the real symmetric \((m+1)\)-by-\((m+1)\) path matrix
\[
H_m(q)=\begin{pmatrix}
1&q&&&\\q&2&q&&\\&q&\ddots&\ddots&\\&&\ddots&2&q\\&&&q&1
\end{pmatrix},
\qquad \alpha_m(q)=\lambda_{\min}(H_m(q)),\quad \beta_m(q)=\lambda_{\max}(H_m(q)).
\]
(For \(m=1\), the two diagonal entries are both \(1\).) When all gaps are positive, the **complete frame spectrum** is the multiset union of the spectra of \(2H_{m_j}(q)\), and consequently
\[
\boxed{A(E)=2\alpha_{\min_jm_j}(q),\qquad B(E)=2\beta_{\max_jm_j}(q).}
\]
Both \(\alpha_m(q)\) and \(\beta_m(q)\) are strictly increasing in \(m\). The lower eigenvalue is explicitly specified by the unique \(t_m>0\) satisfying
\[
q\left(\cosh t_m+\sinh t_m\tanh\frac{mt_m}{2}\right)=1,\qquad
\boxed{\alpha_m(q)=2-2q\cosh t_m.}
\]
The upper eigenvalue \(\beta_m(q)\) is the largest root of the characteristic recurrence described in the proof.

Set \(a=\lfloor(N-h)/h\rfloor\), \(b=\lceil(N-h)/h\rceil\), and \(r=N-h-ah\in\{0,\ldots,h-1\}\). **Among all \(h\)-element erasure sets, precisely the evenly spaced configurations with every retained gap of length \(a\) or \(a+1\) attain the minimum finite squared-analysis condition number.** Its exact value and the number of distinct labeled optimal erasure sets are
\[
\boxed{\min_{|E|=h}\frac{B(E)}{A(E)}=\frac{\beta_b(q)}{\alpha_a(q)},\qquad
\#\{E:\,|E|=h,\ E\text{ optimal}\}=\frac Nh\binom hr.}
\]
Each balanced configuration attains simultaneously the largest possible lower bound \(2\alpha_a(q)\) and the smallest possible upper bound \(2\beta_b(q)\). If \(h>\lfloor N/2\rfloor\), every erasure set of size \(h\) makes the two-modulation family non-spanning. The theorem includes the boundary cases \(h=1\) and \(h=\lfloor N/2\rfloor\).

## Assumptions and scope
The ambient inner product on \(\mathbb C^N\) is the usual Euclidean one; no unit-norm scaling is applied to the two-tap window. The squared-analysis frame operator is \(S_E=\sum_{k\notin E}\sum_{s\in\{0,\ell\}}(M_sT_kg)(M_sT_kg)^*\), so the frame bounds are its extremal eigenvalues. Erasures remove whole translation pairs, never just one modulation atom. The two modulations are distinct, and the antipodal case \(2\ell\equiv0\pmod N\) is excluded: in that case \(q=0\), and strict monotonicity and uniqueness of the balanced design can fail. A non-spanning set has \(A(E)=0\) and infinite condition number. All cyclic positions are labeled, so cyclic rotations count as different erasure subsets unless they coincide.

## Proof
**1. Exact local frame operator.** An unmodulated atom at translation \(k\) is supported on vertices \(k,k+1\), with both coordinates equal to \(1\). The \(\ell\)-modulated atom has coordinates \(e^{2\pi i\ell k/N}\) and \(e^{2\pi i\ell(k+1)/N}\). Their two rank-one operators contribute diagonal entries \(2\) at each endpoint and the off-diagonal complex conjugate pair \(1+e^{\pm2\pi i\ell/N}\). The off-diagonal modulus is \(2q\). Hence \(S_E\) is supported on the graph whose retained edges are exactly \(\{k,k+1\}\) for \(k\notin E\). An isolated vertex gives an immediate zero eigenvalue. Every connected component with \(m\ge1\) consecutive retained edges is a path with \(m+1\) vertices, whose diagonal of \(S_E\) is \((2,4,\ldots,4,2)\) and whose adjacent off-diagonal entries have modulus \(2q\). A diagonal unitary gauge along each path makes all off-diagonals real and positive without changing the spectrum. Consequently the component is unitarily equivalent to \(2H_m(q)\). Since \(h\ge1\), there are no unbroken cycle components. A cyclic gap of length zero gives an isolated vertex; otherwise the gaps give exactly all path components. This proves the claimed exact spectral decomposition and finite-frame criterion.

**2. Strict growth of the lower eigenvalue.** Let \(D_m\) be the diagonal of \(H_m(q)\) and let \(Q_m\) be the signless path Laplacian: \(Q_m=D_m+A_m\) where \(A_m\) is the zero-diagonal adjacency matrix. Then
\[
H_m(q)=(1-q)D_m+qQ_m.
\]
As \(Q_m\succeq0\) and the smallest degree is one, \(H_m(q)\succeq(1-q)I\), hence \(\alpha_m(q)>0\). Conjugating by the alternating-sign diagonal matrix changes the off-diagonal entries to \(-q\); its smallest eigenvector can be taken strictly positive by applying Perron–Frobenius to the irreducible nonnegative matrix \(2I-\operatorname{diag}((-1)^j)H_m(q)\operatorname{diag}((-1)^j)\).

For \(t>0\), the strictly positive symmetric vector \(v_j=\cosh(t(j-m/2))\), \(0\le j\le m\), satisfies the interior eigenvalue equation for \(D_m-qA_m\) with eigenvalue \(2-2q\cosh t\). Its endpoint equation \((1-\alpha)v_0=qv_1\), with \(v_1/v_0=\cosh t-\sinh t\tanh(mt/2)\), reduces exactly to
\[
q[\cosh t+\sinh t\tanh(mt/2)]=1.
\]
For fixed \(m\) the left side is strictly increasing from \(q<1\) to infinity, so a unique positive \(t_m\) exists. The resulting strictly positive eigenvector is the lowest eigenvector by the preceding Perron argument. For fixed \(t>0\), the left side is **strictly increasing in \(m\)**, so \(t_{m+1}<t_m\). Because \(\alpha_m=2-2q\cosh t_m\), it follows that \(\alpha_{m+1}>\alpha_m\).

**3. Strict growth of the upper eigenvalue and its exact recurrence.** Each \(H_m(q)\) is irreducible and entrywise nonnegative, so a top eigenvector has all coordinates strictly positive. The leading \((m+1)\)-by-\((m+1)\) principal submatrix of \(H_{m+1}(q)\) differs from \(H_m(q)\) only by increasing its last diagonal entry by one. Extend the positive top eigenvector of \(H_m\) by a zero final coordinate. Its Rayleigh quotient for \(H_{m+1}\) is \(\beta_m+|v_m|^2/\|v\|^2>\beta_m\), proving \(\beta_{m+1}>\beta_m\).

For a reproducible exact specification of \(\beta_m\), let \(p_0(X)=1\), \(p_1(X)=X-1\), recursively \(p_j(X)=(X-2)p_{j-1}(X)-q^2p_{j-2}(X)\) for \(2\le j\le m\), and finally \(p_{m+1}(X)=(X-1)p_m(X)-q^2p_{m-1}(X)\). Expansion of the tridiagonal determinant gives \(p_{m+1}(X)=\det(XI-H_m(q))\). Its largest real root is \(\beta_m(q)\). This applies without exception to \(m=1\).

**4. Sharp arrangement theorem and equality count.** The \(h\) nonnegative gap lengths have mean \((N-h)/h\). If any is zero the frame does not span. Otherwise, since both eigenvalue sequences increase strictly, every admissible gap list has \(\min_jm_j\le a\) and \(\max_jm_j\ge b\), hence
\[
\frac{B(E)}{A(E)}=\frac{\beta_{\max_jm_j}}{\alpha_{\min_jm_j}}\ge\frac{\beta_b}{\alpha_a}.
\]
Equality in this bound forces \(\min_jm_j=a\) and \(\max_jm_j=b\) by strict monotonicity. Because the gaps are integers, this is equivalent to the balanced gap multiset of exactly \(h-r\) entries \(a\) and \(r\) entries \(a+1\). Such gap configurations exist and attain equality. This proves the exact optimum, its **if-and-only-if** equality classification, and the simultaneous extremality of both frame bounds.

For the count, choose a distinguished erased index in \(N\) ways and choose which \(r\) of the \(h\) successive gaps have length \(a+1\) in \(\binom hr\) ways. The choices determine a unique cyclic erasure subset with a marked erased index. Conversely every balanced unmarked erasure set has exactly \(h\) marks, giving \((N/h)\binom hr\) distinct optimal subsets. Finally, if \(h>\lfloor N/2\rfloor\), the erased edges cannot be pairwise nonadjacent on an \(N\)-cycle; two adjacent erased edges isolate their intervening vertex and force \(A(E)=0\). This proves the sharp survival threshold.

## Verification
The supplementary standalone Python/NumPy checker `CHECK.py` builds the original complex frame operator for every cyclic erasure mask with \(3\le N\le11\), all non-antipodal nonzero modulation indices, and every permissible erasure size. It compares the full-spectrum extremal values against the block-path matrices, tests the global best condition number and **all** balanced optimal mask counts, and separately tests the hyperbolic spectral equation and eigenvalue monotonicity for multiple coefficients and path sizes. The completed checker reports `PASS: 4126 numerical spectral comparisons across 190 parameter families; monotonicity and hyperbolic root tests.` This is finite numerical corroboration; the unrestricted theorem is proved by the exact matrix decomposition, analytic eigenvalue monotonicity, and counting argument. Run `python CHECK.py` with Python 3 and NumPy.

## Relationship to prior work
Asipchuk, De Carli and Rodriguez, *Block-equivalent finite Gabor frames* (arXiv:2605.16139v1, May 15, 2026), establish algebraic block structure when a time-frequency index set has suitable subgroup form and develop general matrix sparsity conditions. Their accessible full manuscript does not establish the exact paired-translation erasure spectrum or the globally optimal placement and census of erased translations for this sparse two-modulation design.

Salanevich and Strachan, *Robustness to noise and erasures of Gabor frames in finite dimensions* (arXiv:2509.01325v1, September 1, 2025), study general and random finite Gabor systems and uniform erasure guarantees, including Alltop windows; their inspected full text does not treat the deterministic two-tap, two-modulation block-path condition number or optimize the spacing of erasure pairs.

Two published mathematical findings concerning superficially similar structures have distinct objects and quantifiers: *Exact adversarial-erasure spectra for two-character cyclic harmonic frames* optimizes **individual erasures of a two-dimensional harmonic-frame analysis operator** with circular phase rearrangement, whereas the present frame acts on \(\mathbb C^N\), erases **two modulation atoms as a pair at each translation**, and is governed by path Jacobi spectra. *Exact local conditioning and optimal weighting for two-tap cyclic spectrograms* optimizes the **real Jacobian of a nonlinear full-modulation intensity map at a flat signal**, not the linear frame operator after translation erasures. Neither implies the new simultaneous extremal frame bounds or the unique balanced design classification. A further published theorem, *Sharp Riesz conditioning for consecutive triples on finite cycles*, also has balanced cyclic gaps, but optimizes an entirely different three-by-three Vandermonde Gram matrix over three chosen **frequency** nodes, not the frame condition number after erasing translation pairs from a two-modulation, two-tap Gabor family. The eigenvalue and graph-connectivity tools themselves are classical and are not claimed new.

## Limitations
The theorem assumes a fixed equal-weight two-tap window, exactly two modulation indices, and erasures in complete translation pairs. The antipodal modulation case is excluded. No optimality is claimed among all windows, non-paired erasure patterns, irregular multi-modulation systems, or arbitrary translated tap separations. The count concerns labeled cyclic positions, not rotation equivalence classes. Equivalent coverage in incompletely indexed frame-design literature remains a residual originality risk; finite numerical checks alone do not establish an all-order theorem. Independent mathematical audit has not been performed.

## References
1. O. Asipchuk, L. De Carli, L. Rodriguez, *Block-equivalent finite Gabor frames*, arXiv:2605.16139v1 (first public 2026-05-15), https://arxiv.org/abs/2605.16139 and full text https://arxiv.org/html/2605.16139v2 .
2. P. Salanevich, N. Q. D. Strachan, *Robustness to noise and erasures of Gabor frames in finite dimensions*, arXiv:2509.01325v1 (first public 2025-09-01), https://arxiv.org/abs/2509.01325 .
3. B. G. Bodmann, V. I. Paulsen, *Frames, Graphs and Erasures*, arXiv:math/0406134v1 (2004), https://arxiv.org/abs/math/0406134 .
4. *Exact adversarial-erasure spectra for two-character cyclic harmonic frames*, published mathematical finding (2026), https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-exact-adversarial-erasure-spectra-for-two-character-cyclic-harmo--e1e03f96b6f0 .
5. *Exact local conditioning and optimal weighting for two-tap cyclic spectrograms*, published mathematical finding (2026), https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-exact-local-conditioning-and-optimal-weighting-for-two-tap-cycli--52be44b25eaa .
6. *Sharp Riesz conditioning for consecutive triples on finite cycles*, published mathematical finding (2026), https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-sharp-riesz-conditioning-for-consecutive-triples-on-finite-cycle--1200745c9cae .
