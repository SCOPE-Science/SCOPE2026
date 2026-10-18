# Exact cyclic-sweep spectrum and sharp finite-population stabilization under complete mean coupling

## Finding
For every integer \(N\ge1\), consider a real \(C^1\) map \(f\) on a neighborhood of \(s\) with \(f(s)=s\) and \(f'(s)=-\alpha\), where \(\alpha>0\). Replace coordinate \(i\) by the *current* complete mean \(N^{-1}\sum_{j=1}^{N}f(x_j)\), retaining other coordinates, and repeat for coordinates \(1,\ldots,N\) exactly once in this deterministic order. Let \(\Phi\) be the resulting full-sweep map and let \(M=D\Phi(s,\ldots,s)\).

The exact monic characteristic polynomial is
\[
P_{N,\alpha}(z)=\det(zI-M)=\frac{z^{N+1}-\big((1-\alpha/N)z+\alpha/N\big)^N}{z-1}.
\]
The quotient is a polynomial; its value at \(z=1\) is \(1+\alpha\), so \(1\) is not a multiplier. The spectrum has the sharp trichotomy

1. If \(0<\alpha<N\), all multipliers satisfy \(|z|<1\), and the homogeneous equilibrium is locally exponentially attracting.
2. If \(\alpha=N\), then \(P_{N,N}(z)=1+z+\cdots+z^N\), so the multipliers are precisely the nontrivial \((N+1)\)-st roots of unity; moreover \(M^{N+1}=I\) and \(I+M+\cdots+M^N=0\). This is a *linear* resonance classification, not a nonlinear stability claim.
3. If \(\alpha>N\), at least one multiplier has \(|z|>1\), and the homogeneous equilibrium is linearly unstable.

The conclusions persist under every *fixed* ordering of the \(N\) sites. For the logistic map \(f(x)=4x(1-x)\), the nonzero fixed point \(s=3/4\) has \(\alpha=2\): every \(N\ge3\) is locally attracting under a fixed cyclic sweep, \(N=2\) has the cubic-root resonance, and \(N=1\) is unstable. In contrast, synchronous full-mean updating has eigenvalues \(-\alpha,0,\ldots,0\), and is unstable when \(\alpha>1\).

## Assumptions and scope
The mean contains *all* \(N\) sites, including the site being updated. Updated coordinates feed immediately into all subsequent mean evaluations in the sweep. The same fixed permutation is used on every sweep; randomly ordered sweeps, partial coupling and exclusion of self from the mean are different models. The map is examined locally near its homogeneous fixed point; no global attraction, basin estimate, mixing result, or nonlinear stability conclusion on the unit-circle boundary is asserted. The scalar function needs to be \(C^1\) only locally; the nonlinear map need not be globally invariant on any particular box.

## Proof
Write \(c=\alpha/N>0\). At a perturbation input \(x=(x_1,\ldots,x_N)\), let \(y=Mx\) be the perturbation after one sweep. When site \(i\) is updated, the already updated sites contribute \(y_j\) for \(j<i\), and the not-yet-updated sites contribute \(x_j\) for \(j\ge i\). Consequently,
\[
y_i=-c\left(\sum_{j<i}y_j+\sum_{j\ge i}x_j\right).
\]
Let \(L\) be the strictly lower-triangular matrix having every lower entry equal to \(1\), and let \(U\) be the upper-triangular matrix, including its diagonal, having every upper entry equal to \(1\). Then \(L+U={\bf1}{\bf1}^{\mathsf T}\) and
\[
(I+cL)y=-cUx,\qquad M=-c(I+cL)^{-1}U.
\]
Both triangular matrices have diagonal entries \(1\); thus \(\det M=(-c)^N\). Furthermore,
\[
P_{N,\alpha}(z)=\det\big(z(I+cL)+cU\big)
=\det\big(zI+c(z-1)L+c{\bf1}{\bf1}^{\mathsf T}\big).
\]
For \(z\ne0,1\), set \(A=zI+c(z-1)L\). Its determinant is \(z^N\), and the matrix determinant lemma gives \(P_{N,\alpha}(z)=z^N(1+c{\bf1}^{\mathsf T}A^{-1}{\bf1})\). To calculate the last factor, let \(w=A^{-1}{\bf1}\) and \(S_i=\sum_{j\le i}w_j\), with \(S_0=0\). The triangular system reads
\[
S_i=(1-c+c/z)S_{i-1}+1/z.
\]
Summing this geometric recurrence yields
\[
cS_N=\frac{1-(1-c+c/z)^N}{z-1},
\]
whence
\[
P_{N,\alpha}(z)=\frac{z^{N+1}-((1-c)z+c)^N}{z-1}.
\]
The equality of polynomials extends to \(z=0\) and \(z=1\). Its numerator vanishes at \(z=1\), and differentiation there gives \(P_{N,\alpha}(1)=1+Nc=1+\alpha>0\).

Suppose \(0<c<1\). If \(z\) were a multiplier with \(|z|\ge1\), then \(z\ne1\) and the characteristic equation would imply
\[
z=((1-c)+c/z)^N.
\]
But \(|(1-c)+c/z|\le1-c+c/|z|\le1\), with strict inequality when \(|z|>1\), and also strict inequality when \(|z|=1\) and \(z\ne1\), by the equality case of the triangle inequality. Thus \(|z|<1\), a contradiction. Hence every multiplier lies in the open unit disk. A \(C^1\) fixed point whose derivative has spectral radius less than one is locally exponentially attracting.

For \(c=1\), the characteristic polynomial is \((z^{N+1}-1)/(z-1)=\sum_{j=0}^N z^j\). Its \(N\) roots are distinct, equal to the nonidentity \((N+1)\)-st roots of unity. Cayley–Hamilton implies \(\sum_{j=0}^N M^j=0\), while the root description gives \(M^{N+1}=I\). As the primitive \((N+1)\)-st root occurs, the matrix has exact linear period \(N+1\). No higher-order nonlinear terms are controlled at this boundary.

For \(c>1\), the determinant has modulus \(c^N>1\); the product of multiplier moduli is greater than one, so one multiplier lies strictly outside the unit disk, proving instability. Any other fixed scan permutation merely conjugates the full sweep by the corresponding permutation matrix, preserving the characteristic polynomial.

For \(f(x)=4x(1-x)\), the point \(s=3/4\) satisfies \(f'(s)=-2\), so the classification gives the claimed threshold. In synchronous full-mean updating, every site receives the same mean computed from the *old* configuration; the Jacobian is \(-\alpha{\bf1}{\bf1}^{\mathsf T}/N\), with eigenvalues \(-\alpha\) and \(N-1\) zeros (for \(N=1\), just \(-\alpha\)).

## Verification
The included `verify.py` uses SymPy exact rational arithmetic to reconstruct products of the individual coordinate-update Jacobians. It compares their characteristic polynomials with the quotient above and checks determinants for every integer \(1\le N\le8\) and several rational slopes, including all three stability regimes. At the critical parameter it verifies exactly \(M^{N+1}=I\) and \(\sum_{j=0}^{N}M^j=0\). The checker prints `VERIFY_OK` when these tests pass. These finite computations corroborate, but do not replace, the all-dimension algebraic proof.

## Relationship to prior work
Abramson and Zanette (1998, arXiv:chao-dyn/9805015v1) introduced the same complete-mean nonlinear coupling and studied asynchronous updating, but randomize site order within each pass or select sites randomly. Their article derives ensemble-level behavior and a large-population approximation, not the fixed-order, exact finite-dimensional sweep spectrum above. Jiang, Antillón and Escalona (1999, 2000) studied sequential globally coupled logistic maps numerically; their abstracts do not supply this all-population-degree spectral classification, although their full articles were unavailable for a decisive complete comparison. Atmanspacher, Filk and Scheingraber (2004/2005, arXiv:nlin/0407014), Section 4, derive a general product-of-coordinate-Jacobians formulation but explicitly use a heuristic random-update argument rather than an exact arbitrary-population fixed cyclic spectral polynomial. Deshmukh, Matte and Gade (2019) analyze sequential *sublattice* updates on nearest-neighbor coupled lattices; their two-sublattice resonances are related but involve a different coupling matrix and update block structure. None of these cited antecedents is claimed as new.

## Limitations
Local rather than global stability is proved. The unit-circle case is spectrally neutral and has exact *linear* finite order; nonlinear attraction/repulsion there is left open. Random schedules, general coupling weights and higher-period cycles are outside the theorem. The two earlier Jiang articles and the complete 2019 sublattice article could not be examined in full; despite statement-level searches and inspection of other relevant primary sources, unknown equivalences or earlier special cases remain a bibliographic risk. Independent scientific audit has not been performed.

## References
1. G. Abramson and D. H. Zanette, *Globally coupled maps with asynchronous updating*, arXiv:chao-dyn/9805015v1 (first public 1998-05-14), https://arxiv.org/abs/chao-dyn/9805015.
2. Y. Jiang, A. Antillón and J. Escalona, *Globally coupled maps with sequential updating*, Physics Letters A **262** (1999), 403–408, doi:10.1016/S0375-9601(99)00663-5.
3. Y. Jiang, A. Antillón and J. Escalona, *Numerical studies on the dynamics of the globally coupled maps with sequential updating*, Physical Review E **61** (2000), 4614–4617, doi:10.1103/PhysRevE.61.4614.
4. H. Atmanspacher, T. Filk and H. Scheingraber, *Stability analysis of coupled map lattices at locally unstable fixed points*, arXiv:nlin/0407014 (first public 2004-07-07), https://arxiv.org/abs/nlin/0407014; European Physical Journal B **44** (2005), 229–239.
5. A. D. Deshmukh, M. B. Matte and P. M. Gade, *Emergence of long range order for sublattice update in coupled map lattices*, European Physical Journal B **92** (2019), doi:10.1140/epjb/e2019-100078-1.
