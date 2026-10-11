# Sharp Turán mass and the nonradial resonance of nonbinary Hamming weight-two shells

## Finding
Let \(q\ge3\) be a prime power and \(d\ge2q\) be an integer. On \(G=\mathbb F_q^d\), let \(\Omega=\{0\}\cup\{x:\operatorname{wt}(x)=2\}\). Among all complex-valued positive-definite functions \(f\) with \(f(0)=1\) and \(\operatorname{supp}f\subseteq\Omega\), the exact maximum of the counting mass \(\sum_{x\in G}f(x)\) is
\[
\boxed{\tau_{q,d}=1-\frac{\binom d2(q-1)^2}{\mu_{q,d}}},\qquad
\mu_{q,d}=\min_{0\le t\le d}K_2(t)<0,
\]
where the explicit degree-two \(q\)-ary Krawtchouk eigenvalue is
\[
K_2(t)=\frac{[d(q-1)-qt]^2-(q-2)[d(q-1)-qt]-d(q-1)}2.
\]
Thus \(\mu_{q,d}\) is determined simply by the integer or two adjacent integers nearest the vertex \(d(q-1)/q-(q-2)/(2q)\).

**Every extremizer, including all nonradial ones, is classified.** If \(d\not\equiv2\pmod q\), the extremizer is unique, with Fourier transform
\[
\widehat f_\star(\xi)=1-\frac{K_2(\operatorname{wt}(\xi))}{\mu_{q,d}}.
\]
If \(d\equiv2\pmod q\), set \(k=1+(d-2)(q-1)/q\), an integer. Then
\[
\mu_{q,d}=-\frac{d(q-1)}2,\qquad \tau_{q,d}=1+(d-1)(q-1).
\]
All extremizers in this congruence class, with no exceptions, are precisely the inverse Fourier transforms of
\[
\widehat f_a(\xi)=1-\frac{K_2(t)}{\mu_{q,d}}
 +(t-k)\sum_{i:\xi_i\ne0}a_i,\qquad t=\operatorname{wt}(\xi),
\]
where \(a=(a_1,\ldots,a_d)\in\mathbb R^d\) satisfies \(\sum_i a_i=0\) and the following explicit finite family of subset inequalities:
\[
1-\frac{K_2(|A|)}{\mu_{q,d}}+(|A|-k)\sum_{i\in A}a_i\ge0
\quad\text{for every } A\subseteq\{1,\ldots,d\}.
\]
The allowed parameters form a full-dimensional convex polytope in the \((d-1)\)-dimensional zero-sum hyperplane, so genuinely nonradial extremizers exist in every resonant dimension. For example, \(\tau_{3,8}=15\) and \(\tau_{4,10}=28\).

## Assumptions and scope
Use counting measure on \(G\) and the unnormalized Fourier transform \(\widehat f(\xi)=\sum_{x\in G}f(x)\psi(\langle x,\xi\rangle)\) for any fixed nontrivial additive character \(\psi\) of \(\mathbb F_q\). A function is positive definite exactly when its Fourier transform is real and nonnegative at every character. Thus \(f(0)=1\) is equivalent to \(q^{-d}\sum_{\xi}\widehat f(\xi)=1\). All extremizer descriptions refer to this normalization and include complex-valued \(f\), not just real radial functions. The dimension condition \(d\ge2q\) makes every minimizing Hamming layer interior, with at least two active and two inactive coordinates, which is used in the equality classification.

## Proof
**1. Eigenvalues and sharp upper bound.** Fix a frequency \(\xi\) of weight \(t\). The character sum over all weight-two vectors in \(G\) is
\[
\sum_{x:\operatorname{wt}(x)=2}\psi(\langle x,\xi\rangle)
=K_2(t),
\]
since the nonzero-character sum in one coordinate is \(q-1\) when that frequency coordinate is zero and \(-1\) otherwise. Expanding the product of two such coordinate sums gives the displayed polynomial. Write \(V_2=\binom d2(q-1)^2=K_2(0)\). Averaging \(\widehat f\) over all frequencies of weight \(t\) gives exactly
\[
\mathbb E_{\operatorname{wt}(\xi)=t}\widehat f(\xi)
=1+\frac{K_2(t)}{V_2}\bigl(\widehat f(0)-1\bigr).
\]
This follows by coordinate permutations and nonzero-coordinate rescalings: for every fixed weight-two \(x\), the spherical average of its character equals \(K_2(t)/V_2\). Choose a minimizing layer \(t\). Since \(\widehat f\ge0\) and \(\mu_{q,d}<0\), the average yields \(\widehat f(0)\le1-V_2/\mu_{q,d}\). Strict negativity holds because \(K_2\) has mean zero over the full character group while \(K_2(0)>0\).

**2. Attainment.** Define \(g_\star(\xi)=1-K_2(\operatorname{wt}(\xi))/\mu_{q,d}\). This is nonnegative by definition of the minimum. Its average is one because every nontrivial character has mean zero. Its inverse Fourier transform is supported at weight zero or two, because \(K_2\) is the transform of the weight-two indicator. Hence it is admissible and attains the upper bound. At any optimal \(g=\widehat f\), the sharp spherical-average inequality forces \(g\) to vanish at **every** frequency whose weight minimizes \(K_2\).

**3. Linear equality kernel.** Put \(\Delta=g-g_\star\). It is real, has mean zero, has Fourier support only at weight two, and vanishes on every minimizing Hamming layer. For a single frequency coordinate write \(u_i=\mathbf1_{\{\xi_i\ne0\}}\), \(p=(q-1)/q\), and \(h_i=u_i-p\). Every mean-zero one-coordinate function splits uniquely into a multiple of \(h_i\) plus a function \(v_i\) vanishing at zero and summing to zero over nonzero coordinate values. Accordingly, the Fourier-weight-two space decomposes into \(h_i h_j\), \(h_i v_j\), \(v_i h_j\), and products of two such contrast functions, for \(i<j\).

Fix a minimizing weight \(k\). Because \(d\ge2q\), all minimizing weights belong to \(\{2,\ldots,d-2\}\). For any \(k\)-subset of active coordinates, vary the nonzero labels independently. Projecting the equation \(\Delta=0\) onto two-coordinate contrast functions first eliminates every \(v_i v_j\) component. Projecting onto one-coordinate contrasts then gives, for each \(i\) and every \(k\)-subset \(A\) containing \(i\),
\[
\sum_{j\ne i}\bigl(\mathbf1_{\{j\in A\}}-p\bigr)v_{ij}=0.
\]
Swapping the other active positions shows \(v_{ij}=v_i\) independently of \(j\), and hence \((k-1-p(d-1))v_i=0\). A minimizing layer with nonzero prefactor always exists: if \(k=1+p(d-1)\) minimizes the quadratic, its vertex is \(k-1/2\), so \(k-1\) is also a minimizing layer and has nonzero prefactor. Thus all one-coordinate contrasts vanish. It follows that
\[
\Delta(\xi)=\sum_{i<j}b_{ij}h_i h_j
\]
for real coefficients \(b_{ij}\).

For any four distinct indices \(i,j,\ell,m\), choose a disjoint \((k-2)\)-subset \(T\). The alternating sum of the four zero equations on \(T\cup\{i,j\}\), \(T\cup\{\ell,m\}\), \(T\cup\{i,\ell\}\), and \(T\cup\{j,m\}\) implies
\[
b_{ij}+b_{\ell m}=b_{i\ell}+b_{jm}.
\]
These four-cycle identities imply \(b_{ij}=a_i+a_j\): one may solve for \(a_1,a_2,a_3\) from three edges and use the identities to recover every other edge. Set \(S=\sum_i a_i\). At a binary support indicator of weight \(t\), direct expansion yields
\[
\Delta(A)=\bigl[p^2(d-1)-pt\bigr]S+
\bigl[t-1-p(d-2)\bigr]\sum_{i\in A}a_i.
\]
If any minimizing layer has \(k-1-p(d-2)\ne0\), subtracting zero equations for \(k\)-subsets differing by one index makes all \(a_i\) equal. Then \(\Delta\) is a multiple of \(K_2\), but it vanishes where \(K_2=\mu_{q,d}\ne0\); thus \(\Delta=0\).

If instead \(k=1+p(d-2)\), integrality is equivalent to \(d\equiv2\pmod q\), and the strictly convex quadratic \(K_2\) has that integer as its **unique** minimizing weight: the vertex lies \((q-2)/(2q)<1/2\) to its right. The zero equation reduces to \(-pS/q=0\), hence \(S=0\), and the displayed expansion becomes \(\Delta(A)=(|A|-k)\sum_{i\in A}a_i\). Conversely, each such zero-sum perturbation has mean zero, Fourier support only at weight two, vanishes at weight \(k\), and preserves the objective; its admissibility is exactly the displayed subset inequalities. This proves exhaustive equality classification.

**4. Resonance and dimension.** For \(d\equiv2\pmod q\), substituting \(k=1+p(d-2)\) into \(K_2\) gives \(\mu_{q,d}=-d(q-1)/2\) and the integer formula for \(\tau_{q,d}\). The radial spectrum factors as
\[
g_\star(t)=\frac{q^2}{d(q-1)}(t-k)\left(t-k-\frac{q-2}{q}\right).
\]
Consequently, choosing \(a_1=\varepsilon\), \(a_2=-\varepsilon\), all other \(a_i=0\), with \(0<\varepsilon\le q/[d(q-1)]\), makes the spectrum nonnegative and nonradial. Indeed \(g_\star(t)/|t-k|\ge2q/[d(q-1)]\) for all integer \(t\ne k\). The parameter inequalities therefore contain a neighborhood of the origin in the zero-sum hyperplane. The Fourier terms \(h_i h_j\) are linearly independent, so these parameters give \(d-1\) genuine affine degrees of freedom.

## Verification
The standalone `checker.py` uses only Python's standard library. Running `python checker.py` prints:

`VERIFY_OK radial_exact=17 slice_ranks_mod_1000003=14 ternary_fourier=10 edge_identities=2`

It checks exact integral Krawtchouk values and nonnegative resonant candidate spectra for 17 parameter pairs, calculates slice-evaluation ranks modulo a prime for 14 selected parameter pairs, and independently inverts the ternary Fourier transform at ten chosen frequencies over dimensions \(6\) and \(8\). The rank and numerical Fourier checks corroborate the general decomposition proof; modular ranks and finitely many tests are not used as a proof for unrestricted \(q,d\).

## Relationship to prior work
Berdysheva and Révész formulate the positive-definite Turán/Delsarte problem on locally compact abelian groups and derive general packing-type bounds, but do not evaluate the nonbinary weight-two Hamming shell or classify its optimizer face [1]. The Krawtchouk spectrum of \(q\)-ary Hamming distance graphs is classical, and van Dam–Sotirov explicitly use these eigenvalues for graph max-cut/chromatic SDP bounds [2]; thus the **numerical constant** can be viewed as a standard least-eigenvalue/Hoffman-type calculation. The distinct assertion is the complete, unrestricted equality classification and its congruence-controlled nonradial polytope.

A published Boolean-shell result resolves the \(q=2\) problem, where parity controls nonradial equality [3]. Its theorem assumes \(q=2\), so does not imply the nonbinary resonance \(d\equiv2\pmod q\). Li's binary Delsarte code-distance linear program examines a different feasible set and does not give these equality cases [4]. Related q-ary Hamming **ball** optimizations permit weight-one Fourier coefficients and therefore do not determine the shell-restricted optimizer face; neither their larger-support constants nor their radial equality statements imply the present result. No claim of novelty is made for Krawtchouk eigenvalues or generic symmetrization.

## Limitations
The equality theorem is restricted to \(d\ge2q\), the interior-layer regime. Smaller dimensions can have additional kernel directions and are not classified. Only translation-invariant positive-definite functions with the stated support are considered, not all optimizers of arbitrary graph semidefinite programs. The sharp scalar is a known-type spectral computation; the all-extremizer resonance classification is the substantive assertion. An equivalent older result in association-scheme, theta-body, or graph spectral equality literature remains possible; absence of a retrieved equivalent is not proof of priority.

## References
1. E. E. Berdysheva and S. Gy. Révész, *Delsarte's Extremal Problem and Packing on Locally Compact Abelian Groups*, arXiv:1904.03614, first public 2019-04-07, https://arxiv.org/html/1904.03614v4.
2. E. R. van Dam and R. Sotirov, *New bounds for the max-\(k\)-cut and chromatic number of a graph*, arXiv:1503.06595, first public 2015-03-23, https://arxiv.org/html/1503.06595v2, Section 4.3.
3. *Sharp Turán constant and all extremizers for the weight-two Boolean Hamming shell*, published 2026-10-04, published-finding corpus record `e912a3cb52c4`.
4. R. Li, *Unique Optima of the Delsarte Linear Program*, arXiv:2204.06090, first public 2022-04-12, https://arxiv.org/html/2204.06090v2.
