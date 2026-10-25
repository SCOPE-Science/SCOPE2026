# An exact integer-composition penalty for cross-habitat metapopulation rescue

## Finding

Fix an integer \(N\ge2\), positive within-class colonization weights \(a,b\), and a positive local-extinction benchmark \(\delta\) with
\[
\delta>a(N-1),\qquad \delta>b(N-1).
\]
For each integer \(1\le k\le N-1\), partition \(N\) habitat patches into \(k\) patches of class 1 and \(N-k\) of class 2. Give every distinct same-class pair weight \(a\) or \(b\), respectively, and every cross-class pair weight \(c>0\). Let \(M_k(c)\) be the symmetric, zero-diagonal colonization matrix. Define capacity-supercriticality by \(\rho(M_k(c))>\delta\), where \(\rho\) is spectral radius. This is the standard linearization threshold in a deterministic patch-occupancy approximation, not a claim of nonextinction for a finite absorbing stochastic process.

Write
\[
U=\delta+a,\quad V=\delta+b,\quad
B=\delta-a(N-1),\quad C=\delta-b(N-1),
\]
\[
s_0=\sqrt{\frac{UC}{BV}},\qquad k_0=\frac{Ns_0}{1+s_0},\qquad
R_0=\frac{\bigl(\sqrt{UV}+\sqrt{BC}\bigr)^2}{N^2}.
\]
For every integer \(1\le k\le N-1\), its exact required squared cross-class rate is
\[
R(k)=\frac{[\delta-a(k-1)][\delta-b(N-k-1)]}{k(N-k)}
=R_0+\frac{\sqrt{UBVC}\,(k-k_0)^2}{k\,k_0\,(N-k)(N-k_0)}.
\]
In the square root, \(\sqrt{UBVC}=\sqrt{U B V C}\), so the four positive factors are unambiguous. The second equality is an **exact rounding-penalty identity**, not an asymptotic estimate. Among all integer compositions, the minimum of \(R(k)\) is attained among the feasible members of \(\{\lfloor k_0\rfloor,\lceil k_0\rceil\}\). Hence the exact finite-patch rescue threshold is
\[
\boxed{\displaystyle c_{\mathrm{crit}}=
\sqrt{\min_{k\in\{\lfloor k_0\rfloor,\lceil k_0\rceil\}\cap\{1,\ldots,N-1\}}R(k)}.}
\]
At least one integer habitat composition is capacity-supercritical **if and only if** \(c>c_{\mathrm{crit}}\). At equality no composition is strictly supercritical. In particular \(c_{\mathrm{crit}}\ge\sqrt{R_0}\), with strict inequality whenever \(k_0\) is not an admissible integer. Thus a continuous relaxation can declare a positive-width rescue window even though no integer patch allocation is viable.

An exact illustration is \(N=5\), \(a=b=1\), \(\delta=5\). The relaxed threshold is \(\sqrt{R_0}=7/5\), attained at \(k_0=5/2\). The only minimizing integer counts are \(k=2,3\), for which \(R(k)=2\), so \(c_{\mathrm{crit}}=\sqrt2\). Any \(7/5<c\le\sqrt2\) is therefore a strict relaxed-versus-discrete discrepancy except that at the right endpoint the best finite matrices are exactly critical. For instance \(c=141/100\) is above \(7/5\) but below \(\sqrt2\): the algebraic continuous relaxation crosses the threshold, while every actual five-patch arrangement remains subcritical.

## Assumptions and scope

All weights \(a,b,c,\delta\) are positive and common within the specified edge classes. The inequality \(\delta>\max\{a(N-1),b(N-1)\}\) guarantees that both homogeneous \(N\)-patch networks are strictly below the spectral threshold. The matrix has no self-colonization entries, and each patch can colonize each other patch according to its pair class. No Euclidean geometric embedding, finite-distance dispersal kernel, asymmetric transfer, patch-specific extinction, or stochastic perpetual survival is assumed. The optimization is over *integer counts* \(k\), not coordinates or geometrically feasible layouts.

## Proof

**Step 1: Exact spectral reduction.** For \(m=N-k\), the matrix \(M_k(c)\) has constant off-diagonal \(a\) on the first \(k\)-block, \(b\) on the remaining \(m\)-block, and cross-block weight \(c\). The two-dimensional subspace of vectors constant on each block is invariant. In its orthonormal block-indicator basis, the restriction is
\[
T_k=\begin{pmatrix}a(k-1)&c\sqrt{km}\\ c\sqrt{km}&b(m-1)\end{pmatrix}.
\]
All orthogonal within-block fluctuation eigenvectors have eigenvalues \(-a\) or \(-b\), if their multiplicity is nonzero. Since \(c>0\), the Perron eigenvector is strictly positive and constant on each block. Its eigenvalue is the larger eigenvalue of \(T_k\) and equals the spectral radius of \(M_k(c)\).

**Step 2: The sharp threshold at a fixed composition.** Both diagonal elements of \(T_k\) are strictly less than \(\delta\). Thus its larger eigenvalue exceeds \(\delta\) exactly when \(\det(\delta I-T_k)<0\). Explicitly,
\[
\rho(M_k(c))>\delta
\iff c^2>\frac{[\delta-a(k-1)][\delta-b(m-1)]}{km}=R(k).
\]
At equality the larger eigenvalue equals \(\delta\). This implication also holds for \(k=1\) or \(m=1\); absent fluctuation eigenvectors are simply omitted.

**Step 3: A one-dimensional continuous relaxation.** Put \(s=k/(N-k)>0\), so \(k=Ns/(1+s)\). Then direct algebra gives
\[
R(s)=\frac{UC/s+BV s+UV+BC}{N^2}.
\]
Since \(U,V,B,C>0\), its derivative is \((BV-UC/s^2)/N^2\), which is strictly negative for \(s<s_0\) and strictly positive for \(s>s_0\). The unique positive relaxed optimizer is therefore \(s_0=\sqrt{UC/(BV)}\); substituting yields \(R_0=(\sqrt{UV}+\sqrt{BC})^2/N^2\). The map \(k\mapsto k/(N-k)\) is strictly increasing, so the best integer composition must be one of the admissible floor/ceiling counts of \(k_0\).

**Step 4: Exact integer-granularity penalty.** Set \(H=\sqrt{UBVC}\). Completing the square shows
\[
R(s)-R_0=\frac{H}{N^2}\left(\frac{s}{s_0}+\frac{s_0}{s}-2\right).
\]
For \(s=k/(N-k)\) and \(s_0=k_0/(N-k_0)\), the bracket equals
\[
\frac{N^2(k-k_0)^2}{k\,k_0\,(N-k)(N-k_0)}.
\]
The claimed identity follows. Every denominator is positive for the stipulated range, so the penalty vanishes only at an admissible integer \(k=k_0\). Combining Step 2 with the exact integer minimum proves the if-and-only-if rescue threshold and the equality boundary.

**Step 5: Exact five-patch discrepancy.** For \((N,a,b,\delta)=(5,1,1,5)\), \((U,V,B,C)=(6,6,1,1)\), giving \(k_0=5/2\) and \(R_0=49/25\). Direct substitution gives \(R(1)=R(4)=5/2\) and \(R(2)=R(3)=2\). As \(49/25<(141/100)^2<2\), the stated example follows. No numerical or approximate argument is required.

## Verification

The accompanying `check.py` implements the exact threshold and penalty independently of the block-reduction proof, and constructs each full \(N\times N\) symmetric matrix. A standard-library Jacobi diagonalizer checks its largest eigenvalue against the two-dimensional formula and the predicted threshold. With fixed pseudorandom seed 450624, 1,200 random parameter configurations produced 21,309 direct eigenvalue comparisons, all passing. The exact five-patch comparison uses rational arithmetic for the squared thresholds. These computations are consistency checks, not an exhaustive proof over all real parameters or all integers \(N\); the proof above supplies the universal statements. Run with `python3 check.py`.

## Relationship to prior work

The spectral-capacity criterion is established in Ovaskainen and Hanski (2001). Grilli, Barabás and Allesina (2015) analyze spectral persistence in randomly fragmented landscapes and distinguish finite stochastic absorption from deterministic occupancy approximations. Equitable quotient theory yields the two-class matrix reduction, and the two-group reproduction-number formula appearing in Choe and Lee (2015) is a closely related spectral calculation. None of these ingredients alone is new. The result isolated here is the **all-integer-compositions** minimization, the two-candidate rule, and the exact positive rounding penalty with its finite five-patch false-positive interval. The inspected accessible full texts do not state that combined integer result. A general equitable-partition theorem permits spectral reduction but does not itself evaluate the integer threshold or the rounding cost.

## Limitations

The law is an exact theorem for block-constant undirected colonization weights, not a guarantee for a spatially embedded or randomly located landscape. Infinite-horizon survival of a finite stochastic colonization-extinction process is impossible without immigration because extinction is absorbing. The mathematical interpretation of \(\rho>\delta\) is a deterministic linearized persistence-capacity threshold. The result does not optimize habitat placement, uneven patch quality, changing numbers of patches, or costs of building cross-class links. Historical-priority uncertainty remains because complete texts of some early primary spectral-metapopulation studies were inaccessible; general matrix theory supplies part of the derivation. The simple fixed-composition eigenvalue formula is explicitly prior-covered; the claim of novelty is limited to the discrete optimizing classification and penalty.

## References

1. Ovaskainen, O., and Hanski, I. (2001). *Spatially Structured Metapopulation Models: Global and Local Assessment of Metapopulation Capacity*. Theoretical Population Biology 60, 281–302. DOI: 10.1006/tpbi.2001.1548.
2. Grilli, J., Barabás, G., and Allesina, S. (2015). *Metapopulation Persistence in Random Fragmented Landscapes*. PLOS Computational Biology 11, e1004251. DOI: 10.1371/journal.pcbi.1004251. Public release May 20, 2015.
3. Choe, S., and Lee, S. (2015). *Modeling optimal treatment strategies in a heterogeneous mixing model*. Theoretical Biology and Medical Modelling 12, 28. DOI: 10.1186/s12976-015-0026-x.
4. Theodorou, K., Souan, H., and Couvet, D. (2009). *Metapopulation persistence in fragmented landscapes: significant interactions between genetic and demographic processes*. Journal of Evolutionary Biology 22, 152–162. DOI: 10.1111/j.1420-9101.2008.01634.x (full-text comparison unavailable).
5. *Spectra of generalized compositions of graphs and hierarchical networks* (2010). Discrete Mathematics. DOI: 10.1016/j.disc.2010.06.019 (accessible abstract and bibliographic material only).
