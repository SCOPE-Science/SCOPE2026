# Exact balanced-versus-clustered roughness law for a two-stiffness harmonic ring

## Finding
Fix integers \(n\ge3\) and \(1\le m\le n-1\), a base resistance \(a>0\), and contrast \(\delta>0\). Give the edges of a cyclic harmonic chain the resistances \(r_i=a+\delta b_i\), where \(b_i\in\{0,1\}\) and \(\sum_i b_i=m\). Let \(c_i=1/r_i\) be their stiffnesses and put \(R=na+m\delta\), \(g=\gcd(n,m)\). For the temperature-one Gaussian harmonic field with its spatial mean constrained to zero, its mean-square stationary width \(W^2=n^{-1}\sum_i\mathbb E[h_i^2]\) obeys the *sharp* inequalities

\[
\boxed{\frac{R(n^2-1)}{12n^2}-\frac{\delta^2m(n-m)[m(n-m)+2]}{12n^2R}\ \le\ W^2\ \le\ \frac{R(n^2-1)}{12n^2}-\frac{\delta^2(n^2-g^2)}{12n^2R}.}
\]

The left equality holds precisely for a single contiguous run of the \(m\) edges having resistance \(a+\delta\) (up to cyclic rotation); the right equality holds precisely for cyclic rotations of the balanced binary word
\[
 b_i=\left\lfloor\frac{(i+1)m}{n}\right\rfloor-\left\lfloor\frac{im}{n}\right\rfloor.
\]
When \(2\le m\le n-2\) the two values are distinct; when \(m=1\) or \(m=n-1\), every admissible arrangement is a rotation of both. The exact positive difference of the two extremal widths is
\[
\frac{\delta^2\{m(n-m)[m(n-m)+2]-(n^2-g^2)\}}{12n^2R}.
\]
In particular, a fixed inventory of soft springs gives *least* Gaussian roughness when clustered and *greatest* roughness when distributed evenly.

## Assumptions and scope
The vertices are \(\mathbb Z/n\mathbb Z\). Let \(L\) be the weighted graph Laplacian associated with \(c_i\) on edge \(i\leftrightarrow i+1\). The Gaussian probability density on \(\{h\in\mathbb R^n:\sum_i h_i=0\}\), with respect to its induced Euclidean volume, is proportional to
\[
 \exp\left(-\tfrac12\sum_{i=0}^{n-1}c_i(h_{i+1}-h_i)^2\right).
\]
Its covariance is \(L^+\), the Moore--Penrose pseudoinverse of \(L\); thus \(W^2=n^{-1}\operatorname{tr}L^+\). The same covariance is stationary for the projected Edwards--Wilkinson dynamics \(dh=-Lh\,dt+\sqrt2 P\,dB_t\), where \(P\) projects onto mean-zero vectors. No dynamics or Gaussian-width formula with nonunit noise strength is asserted. On \(n=3\) the cycle is a simple triangle; all formulas use positive edge stiffnesses.

## Proof
**Step 1: electrical reduction.** On any connected \(n\)-vertex graph, the Kirchhoff index \(K=\sum_{i<j}\mathcal R_{ij}=n\operatorname{tr}L^+\). Therefore \(W^2=K/n^2\). For a weighted ring, the two resistor arcs between vertices \(i,j\) are in parallel. If one arc has resistance \(s\) and the total resistance is \(R\), then \(\mathcal R_{ij}=s(R-s)/R\). Write \(S_{i,\ell}=\sum_{k=0}^{\ell-1}r_{i+k}\), with cyclic subscripts. Each unordered vertex pair occurs twice among all oriented proper arcs, so
\[
 W^2=\frac1{2n^2R}\sum_{\ell=1}^{n-1}\sum_{i=0}^{n-1}S_{i,\ell}(R-S_{i,\ell}). \tag{1}
\]
No zero-resistance limit or continuum approximation is used.

**Step 2: isolate the arrangement.** Set \(C_{i,\ell}=\sum_{k=0}^{\ell-1}b_{i+k}\). Since \(S_{i,\ell}=\ell R/n+\delta(C_{i,\ell}-\ell m/n)\) and \(\sum_i C_{i,\ell}=\ell m\), the terms linear in the centered counts vanish on summation. The homogeneous term of (1) is \(R(n^2-1)/(12n^2)\), giving
\[
 W^2=\frac{R(n^2-1)}{12n^2}-\frac{\delta^2}{2n^2R}\sum_{\ell=1}^{n-1}\sum_{i=0}^{n-1}\left(C_{i,\ell}-\frac{\ell m}{n}\right)^2. \tag{2}
\]
This exact identity also proves that at fixed total resistance, nonuniformity cannot *increase* the width above the uniform-resistance width.

**Step 3: sharp maximum and equality.** For each \(\ell\), divide \(\ell m=nq_\ell+s_\ell\), \(0\le s_\ell<n\). Among \(n\) integers with sum \(\ell m\), the least sum of squared deviations from their mean occurs exactly when \(n-s_\ell\) counts equal \(q_\ell\) and \(s_\ell\) counts equal \(q_\ell+1\). Its value is \(s_\ell(n-s_\ell)/n\). The displayed balanced mechanical word realizes this simultaneous minimum for *every* \(\ell\). As \(\ell\) runs from \(1\) to \(n-1\), the residues \(s_\ell\) run through the multiples of \(g\), each with multiplicity \(g\), except the zero residue with its appropriate multiplicity. Consequently
\[
 \sum_{\ell=1}^{n-1}\frac{s_\ell(n-s_\ell)}n=\frac{n^2-g^2}{6}.
\]
Insert this into (2) to obtain the right equality value. Equality requires every cyclic interval count to be one of those nearest two integers. To prove uniqueness, extend \(A(k)=\sum_{i=0}^{k-1}b_i\) periodically via \(A(k+n)=A(k)+m\), and put \(T_k=A(k)-km/n\). The interval-count condition forces \(\max_kT_k-\min_kT_k<1\): for every pair of indices, their difference is either minus the fractional part of the relevant rational mean, or one minus that fractional part, and is zero when the mean is integral. Choose \(\theta\in[\max T_k,\min T_k+1)\). Then \(A(k)=\lfloor km/n+\theta\rfloor\) for all \(k\), so \(b_k=\lfloor(k+1)m/n+\theta\rfloor-\lfloor km/n+\theta\rfloor\). Varying \(\theta\) only cyclically rotates the canonical balanced word, since the set of fractional parts of \(km/n\) is one cyclic subgroup. Hence these rotations are the only maximizers.

**Step 4: pair-interaction formula and sharp minimum.** Let \(B=\{i:b_i=1\}\). Counting the proper oriented arcs containing a given pair \(i<j\) gives \(n(n-1)/2-(j-i)(n-j+i)\). Expanding \(\sum C_{i,\ell}^2\) in singletons and distinct pairs in (2) yields
\[
 W^2=\frac{R(n^2-1)}{12n^2}-\frac{\delta^2m^2(n^2-1)}{12n^2R}+\frac{\delta^2}{n^2R}\Phi(B),\quad
 \Phi(B)=\sum_{i<j\in B}(j-i)(n-j+i). \tag{3}
\]
Order the \(m\) marked edges cyclically, and denote their \(m\) positive integer successive gaps by \(u_1,\ldots,u_m\), so \(\sum u_i=n\). If \(f(s)=s(n-s)\), then \(\Phi=\sum_{1\le i<j\le m}f(u_i+\cdots+u_{j-1})\). Viewed as a function on the real simplex \(u_i\ge1\), \(\sum u_i=n\), this function is strictly concave in the independent coordinates \(u_1,\ldots,u_{m-1}\): every summand is concave, and the adjacent-pair summands \(-u_i^2+nu_i\) make the Hessian negative definite. Every nonvertex of this simplex therefore has strictly larger \(\Phi\) than the smallest vertex value. Its vertices have all but one gap equal to one, i.e. the marked sites are consecutive. These configurations all give the same value
\[
 \Phi_{\mathrm{cluster}}=\sum_{d=1}^{m-1}(m-d)d(n-d)=\frac{m(m^2-1)(2n-m)}{12}.
\]
Substitute into (3) to obtain the left equality value and the complete equality classification. This is valid for \(m=1\) as the trivial one-point simplex. Finally the two configurations are different (even up to rotation) exactly when \(2\le m\le n-2\), which makes the gap strictly positive.

## Verification
Run `python roughness_checker.py` with Python 3 and SymPy available. The program evaluates both independent exact arc and pair formulas, checks sharp extremizers over all binary edge inventories for \(3\le n\le10\), two rational resistance contrasts, and compares to an independently inverted Gaussian Laplacian for \(3\le n\le7\). Its observed results are 4,048 exact-rational identity checks, 4,048 global bound/equality checks, and 238 matrix-covariance checks, all passing. These finite checks corroborate but are not the proof for unbounded \(n\); the proof is in the preceding section.

## Relationship to prior work
Edwards and Wilkinson introduced a foundational stochastic-interface fluctuation model (1982). The harmonic Gaussian-field/Laplacian description and the identity between total effective resistance and the Laplacian pseudoinverse are established background; see Ellens et al. (2011). Zhang and Yang (2007) give formulas for unweighted circulant graphs, including cycles. Deng, Chang and Yang (2026) derive weighted-cycle Kirchhoff-index updates and noisy-consensus coherence for **adding one chord**, not for permuting a fixed binary edge inventory. The present contribution is the sharp *all-inventory* arrangement theorem and its closed extremal-width formulas, not the general electrical-resistance identity. Classical equidistribution and cyclic rearrangement principles are related; a more general historical optimization theorem could imply this specialization and remains an originality risk.

## Limitations
Only a finite, massless, mean-zero scalar Gaussian field with positive cyclic nearest-neighbor spring strengths and exactly two resistance values is covered. The theorem concerns mean-square width, not higher moments (Gaussianity determines those once the full covariance is known), relaxation times, arbitrary multisets of spring strengths, nonlinear surface dynamics, or dimensions above one. Independent assessment of novelty and correctness has not been performed.

## References
1. S. F. Edwards and D. R. Wilkinson, *The surface statistics of a granular aggregate*, Proc. R. Soc. Lond. A 381 (1982), 17–31, DOI: 10.1098/rspa.1982.0056 (published 1982-05-08).
2. W. Ellens, F. M. Spieksma, P. van Mieghem, A. Jamakovic, and R. E. Kooij, *Effective graph resistance*, Linear Algebra Appl. 435 (2011), 2491–2506, DOI: 10.1016/j.laa.2011.02.024.
3. H. Zhang and Y. Yang, *Resistance distance and Kirchhoff index in circulant graphs*, Int. J. Quantum Chem. 107 (2007), 330–339, DOI: 10.1002/qua.21068.
4. J. Deng, L. Chang, and Q. Yang, *Single-Chord Augmentation of Weighted Cycles for Algebraic Connectivity and Network Coherence*, arXiv:2605.24479 (2026). This later comparison is not the archived source defining the research context.
