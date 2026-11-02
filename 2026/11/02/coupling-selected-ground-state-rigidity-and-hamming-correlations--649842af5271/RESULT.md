# Coupling-selected ground-state rigidity and Hamming correlations on weighted folded hypercubes

## Finding

For every integer \(d\ge 2\), every nearest-neighbor antiferromagnetic strength \(J>0\), and every real antipodal exchange \(K\), consider the zero-field classical Ising system defined below. Set \(\eta=(-1)^dK/J\). Its exact minimum energy is
\[
E_{\min}=2^{d-1}J\left[-d+\min\{\eta,2-\eta\}\right].
\]
The *complete set* of labelled ground states, not just a family of minimizing examples, consists of the following functions and their global negatives:
\[
\begin{array}{c|c|c}
\text{regime}&\text{positive representatives}&\text{number of labelled ground states}\\
\eta<1&\chi_D&2\\
\eta=1&\chi_D,\ \chi_{D\setminus\{j\}}\ (j\in D)&2(d+1)\\
\eta>1&\chi_{D\setminus\{j\}}\ (j\in D)&2d.
\end{array}
\]
Here \(D=\{1,\ldots,d\}\), and \(\chi_S\) is the binary Walsh character \(\chi_S(x)=(-1)^{\sum_{j\in S}x_j}\). In particular, for even \(d\) and positive \(K\), the single exact crossing is \(K=J\): below it the two Néel states minimize energy, at it \(2(d+1)\) states coexist, and above it exactly \(2d\) single-direction domain-wall states minimize energy. For odd \(d\) the same crossing occurs at the ferromagnetic antipodal coupling \(K=-J\).

In the uniform probability measure on labelled ground states, for every pair of sites at Hamming distance \(r\in\{0,\ldots,d\}\), the exact zero-temperature two-spin correlation is
\[
\left\langle\sigma_x\sigma_y\right\rangle=
(-1)^r\begin{cases}
1,&\eta<1,\\
1-\dfrac{2r}{d+1},&\eta=1,\\
1-\dfrac{2r}{d},&\eta>1.
\end{cases}
\]
The one-site mean vanishes. These statements are exact in each finite dimension, with no thermodynamic limit.

## Assumptions and scope

The sites form \(G=(\mathbb Z/2\mathbb Z)^d\) with \(N=2^d\) labelled positions \(x=(x_1,\ldots,x_d)\). Each site carries one spin \(\sigma_x\in\{-1,+1\}\). Write \(e_j\) for the \(j\)-th coordinate vector and \(\mathbf 1=(1,\ldots,1)\). The energy is
\[
\mathcal H(\sigma)=
J\sum_{j=1}^d\ \sum_{x:x_j=0}\sigma_x\sigma_{x\oplus e_j}
+K\sum_{x:x_1=0}\sigma_x\sigma_{x\oplus\mathbf 1}.
\]
Every undirected cube bond and antipodal bond occurs exactly once. As \(d\ge2\), no antipodal edge equals a coordinate edge. Positive \(J\) favors antialignment; positive or negative \(K\) favors antialignment or alignment, respectively. There is no applied field, disorder, or quantum term. Distinct global sign configurations are counted separately.

## Proof

**1. Exact Fourier diagonalization and attainable lower bound.** Let \(B\) be the real symmetric adjacency-weight operator
\[
(Bf)(x)=J\sum_{j=1}^d f(x\oplus e_j)+Kf(x\oplus\mathbf1).
\]
Then \(\mathcal H(\sigma)=\frac12\langle\sigma,B\sigma\rangle\) with unnormalized Euclidean inner product, while \(\|\sigma\|_2^2=N\). Each Walsh character \(\chi_S\) is an eigenvector with eigenvalue
\[
\lambda_{|S|}=J(d-2|S|)+K(-1)^{|S|}.
\]
For fixed parity of \(k\), \(\lambda_k-\lambda_{k+2}=4J>0\). Thus the only candidate lowest levels are \(k=d\) and \(k=d-1\), whose eigenvalues are respectively
\[
J(-d+\eta),\qquad J(-d+2-\eta).
\]
The Rayleigh bound \(\mathcal H\ge\frac N2\min\{\lambda_d,\lambda_{d-1}\}\) gives the claimed energy. At least one Walsh character in the minimizing level is a genuine \(\pm1\) spin configuration, so equality is *attained* for every real \(K\). Hence this spectral inequality is exactly sharp and equality holds precisely when the spin vector lies in the lowest eigenspace.

**2. All binary-valued lowest eigenvectors are characters.** Multiplication by \(\chi_D\) is an invertible sign transformation of the set of Boolean configurations. Put \(z_j=(-1)^{x_j}\). A spin in the minimizing eigenspace, after multiplication by \(\chi_D\), is a real function of the form
\[
f(z)=a_0+\sum_{j=1}^d a_jz_j,
\]
where \(a_0=0\) unless \(\eta\le1\), and \(a_j=0\) for all \(j\) unless \(\eta\ge1\). Since the original spins and \(\chi_D\) are signs, \(f(z)^2=1\) at every \(z\in\{-1,1\}^d\). Expanding the square in the orthogonal Walsh basis, each coefficient of \(z_j\) equals \(2a_0a_j\) and each coefficient of \(z_iz_j\) for \(i\ne j\) equals \(2a_ia_j\); all must vanish. Thus no two distinct coefficients among \(a_0,a_1,\ldots,a_d\) can be nonzero. The constant coefficient of \(f^2\) gives \(a_0^2+\sum_j a_j^2=1\), so its sole nonzero coefficient is \(+1\) or \(-1\). This proves the classification and the exact counts, including the crossing. No non-character spin configuration can saturate the bound.

**3. Two-point law.** Every ground state has total spin zero, because the character indexing set is nonempty for \(d\ge2\), and its global negative is also a ground state. For a fixed pair \((x,y)\) with Hamming distance \(r\), \(\chi_D(x)\chi_D(y)=(-1)^r\). For \(S=D\setminus\{j\}\),
\[
\chi_S(x)\chi_S(y)=(-1)^r(-1)^{x_j+y_j}.
\]
Exactly \(r\) of the \(d\) coordinate factors on the right equal \(-1\). Therefore the uniform mean over the \(d\) direction-indexed states gives \((-1)^r(d-2r)/d\), while adding the \(\chi_D\) family at coexistence gives \((-1)^r(d+1-2r)/(d+1)\). Global spin reversal does not alter pair products, completing the formula.

## Verification

The included standard-library checker \(`reproduce.py`\) independently constructs the actual edge lists, enumerates every possible spin assignment for \(d=2,3,4\) at 11 integer or half-integer coupling ratios in each dimension, and compares **both** the exact minimum energy and the *entire set* of minimizers with the theorem. It checks all 132 distance-specific correlations against the direct census. Separately it forms the weighted adjacency action and checks every Walsh eigenvector and the two-level minimum in 35 dimension/coupling cases with \(2\le d\le8\). All checks passed: 33 exhaustive spin-census cases spanning 723,888 evaluated spin assignments, 132 correlation cases, and 35 exhaustive Walsh-spectrum cases. The checker verifies finite cases; the proof above, not the finite census, establishes all dimensions and all real couplings.

Run \(`python3 reproduce.py`\) with standard Python 3.10+; no third-party dependencies. The file \(`check_results.txt`\) contains the observed per-case output.

## Relationship to prior work

Franco and Cannas (2003) studied Ising spins at hypercube vertices with Hamming-distance couplings \(J(r)=1/\binom dr\) on *all* shells \(1\le r\le d/2\), and described configurations consisting of two opposed antiferromagnetic domains, including a \(2d\) degeneracy in the dimensions considered. That important domain pattern is **not claimed as new**. The present Hamiltonian is different: it contains only the distance-one and distance-\(d\) shells, with an independent real ratio \(K/J\). Their particular shell-weight vector therefore does not specialize to the family here for general \(d\), and it does not state the coupling threshold or the pair-correlation law above.

Mirafzal (2011) identifies the same underlying folded-hypercube Cayley graph and its automorphism group; this establishes geometry but not its weighted zero-temperature Ising extremizers. Van Dam and Sotirov (2015) review sharp spectral bounds for maximum cuts in Hamming association schemes and determine the relevant eigenvalue methods. The energy-lower-bound method belongs to that tradition, but the present statement adds the complete Boolean-equality classification, the coupling-driven crossing, and correlations. Chen, Naserasr and Sarti (2026) analyze signed projective cubes and switching/homomorphism structures; their inspected work does not state a real two-shell coupling phase classification. These are implications assessed from the specified source content, not a claim that all possible earlier literature has been exhausted.

## Limitations

The result is for classical binary Ising spins on a finite, uniformly weighted cube-plus-antipodes network at zero field. It does not provide finite-temperature behavior, excitation gaps, spontaneous dynamics, quantum correlations, or robustness to arbitrary bond disorder. The degeneracy grows only linearly with \(d\) at the crossing, so the residual entropy per site vanishes as \(d\to\infty\); the exact finite-size level crossing must not be described as a demonstrated bulk thermal phase transition. Historical priority has not been independently certified.

## References

1. L. Franco and S. A. Cannas, *Non glassy ground-state in a long-range antiferromagnetic frustrated model in the hypercubic cell* (first posted 2003-02-20), https://arxiv.org/abs/cond-mat/0302412 .
2. S. M. Mirafzal, *Some other algebraic properties of folded hypercubes* (first posted 2011-03-22), https://arxiv.org/abs/1103.4351 .
3. E. R. van Dam and R. Sotirov, *New bounds for the max-k-cut and chromatic number of a graph* (first posted 2015-03-23), https://arxiv.org/abs/1503.06595 .
4. M. Chen, R. Naserasr and A. Sarti, *Signed Projective Cubes, a Homomorphism Point of View* (first published 2026-04-21), https://doi.org/10.1002/jgt.70046 .
5. M.-J. Ma and J.-M. Xu, *Algebraic Properties and Panconnectivity of Folded Hypercubes*, Ars Combinatoria 95 (2010), 179–186, https://combinatorialpress.com/ars-articles/volume-095-ars-articles/algebraic-properties-and-panconnectivity-of-folded-hypercubes/ .
