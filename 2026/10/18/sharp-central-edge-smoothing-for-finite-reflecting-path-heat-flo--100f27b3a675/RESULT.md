# Sharp central-edge smoothing for finite reflecting path heat flows

## Finding

Let \(Q_n\) be the unweighted, continuous-time random-walk generator on the vertices \(\{0,\ldots,n-1\}\) of a path, with jump rate one along each existing edge, and set \(H_n(t)=e^{tQ_n}\). For \(n\ge2\) and \(t>0\), define its sharp bounded-input spatial smoothing constant by
\[
C_n(t)=\sup_{\|f\|_{\ell^\infty}\le1}\max_{1\le i<n}|(H_n(t)f)(i)-(H_n(t)f)(i-1)|.
\]
Let \(A_n\) be the \((n-1)\)-by-\((n-1)\) Dirichlet tridiagonal matrix with diagonal entries \(-2\) and entries \(1\) on each first off-diagonal. Put \(K_t=e^{tA_n}\). For every \(n\ge2\) and \(t>0\),
\[
\boxed{C_n(t)=2\max_{1\le i<n}K_t(i,i)
=\frac4n\sum_{k=1}^{n-1}e^{-4t\sin^2(\pi k/(2n))}
\sin^2\left(\frac{\pi k\lfloor n/2\rfloor}{n}\right).}
\]
Indices of \(K_t\) run from \(1\) to \(n-1\). If \(n\) is even, the only maximizing evaluation edge is \(i=n/2\); if \(n\) is odd, the only maximizers are \(i=(n-1)/2\) and \(i=(n+1)/2\). For each maximizing edge \(i\), the input \(f(j)=-1\) when \(j<i\) and \(f(j)=1\) when \(j\ge i\) attains the bound. The function \(t\mapsto C_n(t)\) is strictly decreasing.

Let \(I_0\) and \(I_1\) denote modified Bessel functions. Every finite path obeys the *strict* free-lattice bound
\[
\boxed{C_n(t)<2e^{-2t}I_0(2t),\qquad n\ge2,\ t>0,}
\]
with equality in the limit \(n\to\infty\) for each fixed \(t>0\). The sharp, dimension-uniform time-weighted smoothing constant is
\[
\boxed{\sup_{n\ge2,\,t>0}\sqrt t\,C_n(t)
=2\sqrt{t_*}\,e^{-2t_*}I_0(2t_*)
=0.6630149334909870\ldots,}
\]
where \(t_*=0.3949892106717839\ldots\) is the unique positive solution of
\[
\frac{I_1(2t_*)}{I_0(2t_*)}=1-\frac{1}{4t_*}.
\]
The supremum is approached as \(n\to\infty\) and \(t\to t_*\) but is **not attained by any finite path at any positive time**.

For each fixed \(s>0\), the diffusive scaling limit is
\[
\boxed{\lim_{n\to\infty}nC_n(sn^2)=4\sum_{\substack{k\ge1\\k\text{ odd}}}e^{-\pi^2 k^2s}.}
\]

## Assumptions and scope

The vertex graph is the connected unweighted path with \(n\ge2\) vertices, endowed with counting measure and nearest-neighbor jump rate one. Specifically,
\[
(Q_nf)(j)=\sum_{\substack{0\le k<n\\|k-j|=1}}(f(k)-f(j)).
\]
No factor of \(1/2\) is used in the generator. The input and output are real-valued sequences (the operator norms agree for complex-valued inputs by total-variation duality). The output seminorm uses unweighted adjacent differences; it is not a derivative in continuous space. The graph and time parameters range over *all* integers \(n\ge2\) and all real \(t>0\). The infinite-lattice and diffusive limits are distinct: the former holds at fixed \(t\), while the latter holds at \(t=sn^2\).

## Proof

**1. Difference–Dirichlet intertwining.** Define \(E:\mathbb R^n\to\mathbb R^{n-1}\) by \((Ef)(i)=f(i)-f(i-1)\) for \(1\le i<n\). Directly checking the two boundary rows and each interior row gives \(EQ_n=A_nE\). Exponentiation therefore gives the exact identity
\[
EH_n(t)=K_t E.
\]
Extend each row \(K_t(i,j)\) by the Dirichlet conventions \(K_t(i,0)=K_t(i,n)=0\). The coefficient of input coordinate \(f(j)\) in the edge difference \((EH_n(t)f)(i)\) is \(K_t(i,j)-K_t(i,j+1)\). Hence the sharp norm of evaluation at edge \(i\) equals
\[
R_i(t)=\sum_{j=0}^{n-1}|K_t(i,j+1)-K_t(i,j)|.
\]

**2. Unimodality, not merely positivity.** For fixed \(i\), set \(u_j(t)=K_t(i,j)\) with \(u_0=u_n=0\) and \(w_j=u_{j+1}-u_j\) for \(0\le j<n\). The Dirichlet heat equation gives \(w'(t)=Q_n w(t)\) and \(w(0)=e_{i-1}-e_i\); thus \(w_j(t)=H_n(t)_{j,i-1}-H_n(t)_{j,i}\). Every \(2\)-by-\(2\) minor of \(H_n(t)\) with row and column indices in increasing order is nonnegative. To verify this without invoking an unproved variation-diminishing theorem, write \(Q_n\) as the sum of the elementary adjacent-edge generators. The exponential of one such generator is the identity off a neighboring \(2\)-by-\(2\) block, whose entries are \((1\pm e^{-2s})/2\); because that block acts on *adjacent* coordinates and has positive determinant, all its ordered minors are nonnegative. Products preserve nonnegative minors by the Cauchy–Binet formula, and the Lie–Trotter limit proves the assertion for \(H_n(t)\). All entries of \(H_n(t)\) are strictly positive for \(t>0\) by irreducibility. Consequently, for row indices \(r<s\),
\[
\frac{H_n(t)_{r,i-1}}{H_n(t)_{r,i}}
\ge\frac{H_n(t)_{s,i-1}}{H_n(t)_{s,i}}.
\]
It follows that the sequence \(w_j\) has at most one sign change, from nonnegative to nonpositive. Since \(\sum_jw_j=u_n-u_0=0\), the positive and negative variations agree and the row rises to a single possibly flat maximum before falling. Therefore
\[
\boxed{R_i(t)=2\max_{1\le j<n}K_t(i,j).}
\]
Thus unimodality is what makes the sharp bounded-input gradient norm a diagonal-kernel problem; kernel positivity alone would not suffice.

**3. Reduction to the diagonal and exact maximizing edges.** Because \(A_n\) is real symmetric,
\[
K_t(i,j)=\langle e^{tA_n/2}e_i,e^{tA_n/2}e_j\rangle.
\]
Cauchy–Schwarz gives \(K_t(i,j)\le\sqrt{K_t(i,i)K_t(j,j)}\); the inequality is strict if \(i\ne j\), since \(e^{tA_n/2}\) is invertible and sends distinct basis vectors to linearly independent vectors. Hence \(\max_{i,j}K_t(i,j)=\max_iK_t(i,i)\), and no off-diagonal entry is a global maximizer.

For completeness, the classical discrete Dirichlet image formula (recorded in Dowker, Section 7) gives
\[
K_t(i,i)=q_t(0)-q_t(2i),\quad
q_t(r)=\sum_{m\in\mathbb Z}e^{-2t}I_{|r+2nm|}(2t),
\]
where \(q_t\) is the heat kernel on the cycle with \(2n\) vertices. Regard \(q_t(r)\) as a function of cycle distance \(0\le r\le n\) and write \(v_r=q_t(r)-q_t(r+1)\) for \(0\le r<n\). Subtracting consecutive cycle heat equations shows that the vector \(v\) solves a linear tridiagonal system with off-diagonal entries \(+1\), internal diagonal entries \(-2\), and end diagonal entries \(-3\), starting from \(v(0)=(1,0,\ldots,0)\). For \(n=2\), both diagonals are \(-3\). This irreducible Metzler system makes every \(v_r(t)>0\) for \(t>0\). Hence \(q_t(r)\) is strictly decreasing in cycle distance. The argument \(2i\) has cycle distance \(2\min\{i,n-i\}\), maximal only at the stated central index or pair. This proves the uniqueness of the maximizing edge locations. For such an index \(i\), strict off-diagonal Cauchy–Schwarz ensures that the unique maximum of row \(i\) occurs at column \(i\); therefore the displayed step input agrees with the coefficient signs and attains \(R_i(t)=2K_t(i,i)\).

**4. Spectral formula and monotonicity in time.** The Dirichlet matrix has orthonormal sine eigenvectors \(\sqrt{2/n}\sin(\pi kj/n)\), with eigenvalues \(-4\sin^2(\pi k/(2n))\), for \(1\le k,j<n\). Expanding \(K_t(i,i)\) gives the asserted finite sum. Since all these eigenvalues are strictly negative and the squared sine coefficients sum to one, each \(K_t(i,i)\) is strictly decreasing in time. The maximum equals a central diagonal for every time, and thus \(C_n(t)\) is strictly decreasing.

**5. Sharp free-lattice comparison.** A killed continuous-time nearest-neighbor walk on the positive Dirichlet interval has return probability \(K_t(i,i)\). The unrestricted lattice walk has return probability \(p_t(0)=e^{-2t}I_0(2t)\). At every positive time, paths that exit the interval before returning have positive probability, so \(K_t(i,i)<p_t(0)\). On a central vertex the distance to the absorbing boundary tends to infinity with \(n\); bounding exit by the Poisson tail for the number of attempted jumps gives \(K_t(\lfloor n/2\rfloor,\lfloor n/2\rfloor)\to p_t(0)\) for every fixed \(t>0\). This proves the strict bound and its sharpness in the size limit.

**6. Unique time optimizer.** Consider \(g(t)=2\sqrt t\,e^{-2t}I_0(2t)\). Put \(z=2t\) and \(r(z)=I_1(z)/I_0(z)\). The critical-point equation is \(r(z)=1-1/(2z)\). Using the standard Bessel differential identities gives
\[
r'(z)=1-r(z)^2-\frac{r(z)}z.
\]
At *every* positive intersection of \(r(z)\) with \(1-1/(2z)\), the derivative of their difference is \(-1/(4z^2)<0\). A continuous differentiable function whose zeros all have strictly negative derivative has at most one zero. The difference is positive near zero, and its standard large-argument expansion is \(-1/(8z^2)+O(z^{-3})<0\). Hence a single intersection exists, and it is the global maximum of \(g\): \(g(t)\to0\) as \(t\downarrow0\), whereas \(g(t)\to1/\sqrt\pi\) from above as \(t\to\infty\). For every finite \(n\), strictness in Step 5 gives \(\sqrt t\,C_n(t)<g(t)\le g(t_*)\). Taking \(n\to\infty\) at \(t_*\) proves that the displayed constant is sharp but unattained for any finite path. The decimal approximations are numerical evaluations of this exact characterization, not assumptions in the proof.

**7. Diffusive scaling.** Set \(t=sn^2\) in the finite sine formula, with the central index \(i=\lfloor n/2\rfloor\). For each fixed positive integer \(k\), the factor \(\sin^2(\pi ki/n)\) tends to \(1\) if \(k\) is odd and to \(0\) if \(k\) is even. Further,
\[
4n^2\sin^2\left(\frac{\pi k}{2n}\right)\ge4k^2
\quad (1\le k<n),
\]
by \(\sin u\ge 2u/\pi\) on \([0,\pi/2]\). Hence the summands are dominated by the summable sequence \(e^{-4sk^2}\), and dominated convergence yields \(\lim_n n C_n(sn^2)=4\sum_{k\text{ odd}}e^{-\pi^2k^2s}\).

## Verification

The accompanying `check.py` constructs the vertex and Dirichlet matrices directly from their definitions and their matrix exponentials, checks the intertwining identity, compares the matrix row-variation norm against the central Dirichlet diagonal and spectral formula, tests row unimodality and symmetry, evaluates the Bessel critical-point condition, and checks sample diffusive limits. With NumPy and SciPy, running `python check.py` produced **4,029 passing finite assertions**. These numerical tests do not replace the all-size, all-time proofs above. The only nontrivial analytic inputs are finite-matrix positivity, the Dirichlet images/sine expansion, elementary Bessel identities and their large-argument asymptotic, all explicitly used above.

## Relationship to prior work

Dowker, *Heat-kernels on the discrete circle and interval* (2012), Sections 2, 7 and 8, provides the free Bessel heat kernel, discrete Dirichlet image representation and trigonometric eigenfunction expansion used here as inputs. Those formulas do not, by themselves, optimize the \(\ell^\infty\)-to-edge-Lipschitz norm, identify the central maximizing edge at every time, or determine the universal time-weighted constant. Wang and Yan (2010) prove Neumann heat-gradient estimates on smooth compact domains for a different input norm, \(L^1\)-to-\(L^\infty\). Münch and Wojciechowski (2017) study curvature-driven Lipschitz-to-Lipschitz contraction of graph heat flow; the input seminorm and optimized quantity differ. Abadias and de León-Contreras (2021), Section 2, prove order-of-magnitude bounds on sums of lattice heat-kernel differences, not the finite-path sharp constant or edge-location rigidity. De Ponti and Stefani (2024), Sections 1, 3–5, study general consequences of bounds of the form \(L^\infty\)-to-Lipschitz but do not give this finite-path evaluation. These are implication-level distinctions: a general bound lacking an optimized constant does not imply the strict finite-size formula or its optimizer.

## Limitations

The theorem concerns **unweighted one-dimensional paths with reflecting graph endpoints** and jump rates exactly one per edge. It does not assert analogous central-edge rigidity for arbitrary weighted paths, trees or general graphs, nor does it establish any sharp constant for a continuous spatial derivative or an infinite-dimensional uniformly timed operator in a different normalization. The explicit finite-path kernel identities are classical; the asserted contribution is their sharp norm optimization, location rigidity, strict boundary deficit and time/diffusive asymptotics. Some older related birth–death-chain literature may use equivalent coupling or total-variation formulations; historical novelty remains subject to independent review. No independent proof audit has been performed.

## References

1. F.-Y. Wang and L. Yan, *Gradient Estimate on the Neumann Semigroup and Applications*, arXiv:1009.1965 (first posted 2010-09-10).
2. J. S. Dowker, *Heat-kernels on the discrete circle and interval*, arXiv:1207.2096 (first posted 2012-07-09), particularly formulas (29)–(31).
3. F. Münch and R. K. Wojciechowski, *Ollivier Ricci curvature for general graph Laplacians: Heat equation, Laplacian comparison, non-explosion and diameter bounds*, arXiv:1712.00875 (2017).
4. L. Abadias and M. de León-Contreras, *Discrete Hölder spaces, their characterization via semigroups associated to the discrete Laplacian and kernels estimates*, arXiv:2107.06778 (2021), Section 2, particularly Lemma 2.6.
5. N. De Ponti and G. Stefani, *Properties of Lipschitz smoothing heat semigroups*, arXiv:2403.00620 (first posted 2024-03-01), Sections 1, 3–5.
