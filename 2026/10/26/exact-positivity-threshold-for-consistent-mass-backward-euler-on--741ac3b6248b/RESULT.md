# Exact positivity threshold for consistent-mass backward Euler on a periodic linear finite-element mesh

## Finding

Consider the heat equation on a circle discretized by continuous piecewise-linear (\(P_1\)) finite elements on a uniform periodic mesh with \(n\ge3\) nodes and spacing \(\ell>0\). Let \(M\) and \(K\) be the consistent mass and stiffness matrices, and define
\[
T_\tau=(M+\tau K)^{-1}M,\qquad r=\frac{\tau}{\ell^2},\qquad \tau\ge0.
\]
The exact entrywise-positivity classification is:
- For \(n=3\), \(T_\tau\) is entrywise nonnegative for every \(\tau\ge0\).
- For every \(n\ge4\), \(T_\tau\) is entrywise nonnegative if and only if \(\tau=0\) or \(r\ge\frac16\).

For \(n\ge4\) and every \(0<\tau/\ell^2<1/6\), the entry joining a node to the node two edges away is strictly negative. Thus the threshold \(\tau=\ell^2/6\) is sharp, with no intervening positive timestep window. The transition preserves constants, \(T_\tau\mathbf1=\mathbf1\), even when it fails to preserve entrywise nonnegativity.

## Assumptions and scope

The mesh is a periodic circle with \(n\ge3\) equally spaced nodes, element length \(\ell\), and the standard continuous piecewise-linear finite-element basis. The mass matrix is the consistent mass matrix, not a lumped mass matrix. The stiffness matrix corresponds to the unit-diffusivity operator \(-u_{xx}\). With \(A_n\) the adjacency matrix of the cycle,
\[
M=\frac{\ell}{6}(4I+A_n),\qquad K=\frac1{\ell}(2I-A_n).
\]
Entrywise nonnegative means every matrix entry is at least zero. The theorem concerns the nodal update for one backward-Euler step. It does not address nonuniform meshes, higher spatial dimensions, different time integrators, or mass lumping.

## Proof

Set \(\bar M=6M/\ell=4I+A_n\), \(\bar K=\ell K=2I-A_n\), and \(B_r=\bar M+6r\bar K\). Then
\[
T_\tau=B_r^{-1}\bar M,\qquad B_r=(4+12r)I+(1-6r)A_n.
\]
If \(r=0\), then \(T_\tau=I\). If \(r\ge1/6\), then \(B_r\) has positive diagonal, nonpositive off-diagonal entries, and strict diagonal-dominance margin
\[
(4+12r)-2|1-6r|=6.
\]
It is therefore a nonsingular \(M\)-matrix, so \(B_r^{-1}\ge0\) entrywise. Since \(\bar M\ge0\), this gives \(T_\tau\ge0\).

For \(n=3\), the cycle adjacency matrix has eigenvalues \(2,-1,-1\). Consequently the eigenvalues of \(T_\tau\) are \(1\) and \(1/(1+6r)\) (twice), so
\[
T_\tau=\frac13\mathbf1\mathbf1^{\mathsf T}+\frac1{1+6r}\left(I-\frac13\mathbf1\mathbf1^{\mathsf T}\right).
\]
Its diagonal and off-diagonal entries are nonnegative for every \(r\ge0\).

It remains to prove failure for \(n\ge4\) and \(0<r<1/6\). Write \(a=4+12r\), \(b=1-6r>0\), and
\[
q=\frac{a-\sqrt{a^2-4b^2}}{2b}\in(0,1),\qquad c=\frac1{\sqrt{a^2-4b^2}}.
\]
The inverse of \(B_r=aI+bA_n\) is circulant. Its entry at cyclic displacement \(k\), for \(0\le k\le n\), is
\[
G_k=c\,\frac{(-q)^k+(-q)^{n-k}}{1-(-q)^n}.
\]
This follows by solving \(bG_{k-1}+aG_k+bG_{k+1}=0\) away from the source node and imposing periodicity. The formula gives \(G_1<0\) and \(G_2>0\) for every \(n\ge4\). It also gives \(G_3=G_1<0\) for \(n=4\), \(G_3=G_2>0\) for \(n=5\), and \(G_3<0\) for every \(n\ge6\).

Because \(\bar M=B_r-6r\bar K\),
\[
T_\tau=I-6rB_r^{-1}(2I-A_n).
\]
For \(n\ge4\), the displacement-two entry of \(I\) is zero, so
\[
(T_\tau)_{0,2}=-6r(2G_2-G_1-G_3).
\]
The bracket is strictly positive: for \(n=4\) it is \(2(G_2-G_1)\); for \(n=5\) it is \(G_2-G_1\); and for \(n\ge6\) all three sign facts give \(2G_2-G_1-G_3>0\). Thus \((T_\tau)_{0,2}<0\) throughout \(0<r<1/6\). Together with the sufficient condition above, this proves the classification.

## Verification

The standalone script `verify.py` uses exact rational arithmetic to invert the scaled matrices for 48 finite combinations of mesh size and timestep. It checks row-sum preservation, nonnegativity at \(r=0,1/6,1/3\), the negative displacement-two entry for three rational values below the threshold when \(n\ge4\), and the three-node exception. These finite checks are reproducibility checks only; the proof above establishes the result for all \(n\) and all \(\tau\).

## Relationship to prior work

Chatzipantelidis, Horváth, and Thomée studied positivity preservation for fully discrete piecewise-linear finite-element approximations of the heat equation, including standard Galerkin and lumped-mass methods, under homogeneous Dirichlet boundary conditions. Their work discusses positivity thresholds and sufficient timestep conditions. A related 2015 preprint by Jin, Lazarov, Thomée, and Zhou gives a general sufficient positivity threshold for non-diagonal mass matrices, again in a bounded-domain Dirichlet setting. These results motivate the question but do not state the exact necessary-and-sufficient classification for the uniform periodic one-dimensional mesh proved here. The decisive additional step is the sign of the exact cyclic Green-function combination at displacement two.

## Limitations

The classification is specific to the uniform periodic one-dimensional piecewise-linear (\(P_1\)) discretization with a consistent mass matrix. It does not classify nonuniform periodic meshes, bounded-domain Dirichlet matrices, higher-dimensional triangulations, or other time-stepping methods. The full text of the closest 2015 heat-equation article was not retrievable; its accessible abstract and metadata confirm the general setting but cannot rule out every unindexed special-case discussion. The related subdiffusion preprint was read in full for its finite-element positivity statements. No independent mathematical audit has been performed.

## References

1. P. Chatzipantelidis, Z. Horváth, and V. Thomée, “On Preservation of Positivity in Some Finite Element Methods for the Heat Equation,” *Computational Methods in Applied Mathematics* 15(4) (2015), 417–437. DOI: 10.1515/cmam-2015-0018. Public publication record dated 2015-10-01: https://papers.sze.hu/research-portal/publications/10.1515/cmam-2015-0018.
2. B. Jin, R. Lazarov, V. Thomée, and Z. Zhou, “On Nonnegativity Preservation in Finite Element Methods for Subdiffusion Equations,” arXiv:1510.02825 (first public 2015-10-09), https://arxiv.org/abs/1510.02825.
3. V. Thomée and L. B. Wahlbin, “On the Existence of Maximum Principles in Parabolic Finite Element Equations,” *Mathematics of Computation* 77(261) (2008), 11–19. DOI: 10.1090/S0025-5718-07-02021-2.
