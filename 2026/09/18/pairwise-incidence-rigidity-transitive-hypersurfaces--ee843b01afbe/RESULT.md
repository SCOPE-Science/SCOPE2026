# Global pairwise incidence rigidity for transitive hypersurface families

## Statement

Let \(M^{n+1}\), \(n\ge 2\), carry an unoriented transitive family
\[
\mathscr Z=\{\Sigma_\sigma:\sigma\in P\}
\]
of closed embedded hypersurfaces in the sense of Martins. Put
\[
F_2(P)=\{(\sigma,\tau)\in P\times P:\sigma\ne\tau\}
\]
and define the ordered pair-incidence space
\[
\mathcal J^{(2)}=
\{(x,\sigma,\tau)\in M\times F_2(P):x\in\Sigma_\sigma\cap\Sigma_\tau\}.
\]

Then the projection
\[
q:\mathcal J^{(2)}\longrightarrow F_2(P),\qquad
q(x,\sigma,\tau)=(\sigma,\tau),
\]
is a smooth proper locally trivial fiber bundle. Its fiber is
\[
\Sigma_\sigma\cap\Sigma_\tau\cong
\begin{cases}
\mathbb S^{n-1},&M\cong\mathbb S^{n+1},\\
\mathbb R\mathbb P^{n-1},&M\cong\mathbb R\mathbb P^{n+1}.
\end{cases}
\]

Consequently, every two distinct members of the family intersect, and they always
intersect transversely. For each fixed \(\sigma\), all submanifolds
\(\Sigma_\sigma\cap\Sigma_\tau\subset\Sigma_\sigma\), \(\tau\ne\sigma\), are smoothly
ambient-isotopic. Under Martins' identification of \(\Sigma_\sigma\) with
\(\mathbb S^n\) in the two-sided case, this isotopy class is that of an equator;
in the one-sided case, under the identification with \(\mathbb R\mathbb P^n\),
it is that of a projective hyperplane.

Thus, in the spherical case, \(\Sigma_\sigma\setminus\Sigma_\tau\) has two
components, each an open \(n\)-ball. In the projective case,
\(\Sigma_\sigma\setminus\Sigma_\tau\) is an open \(n\)-ball.

The same conclusions apply in particular to hypersurface Zoll families of minimal
hypersurfaces. In dimension three, any two distinct members of a surface Zoll
family meet in one embedded transverse circle, both on \(\mathbb S^3\) and on
\(\mathbb R\mathbb P^3\).

## Context

Martins proves that an unoriented transitive family in ambient dimension at least
three forces \(M\) to be diffeomorphic to \(\mathbb S^{n+1}\) or
\(\mathbb R\mathbb P^{n+1}\), with members respectively diffeomorphic to
\(\mathbb S^n\) or \(\mathbb R\mathbb P^n\). He also proves a local infinitesimal
incidence theorem: at a fixed member, the zero sets of nonzero infinitesimal
variations are carried to equators in the two-sided case and to projective
hyperplanes in the one-sided case.

The global family need not be simultaneously straightenable: Martins records
examples, originating in work of Ambrozio and Guajardo, of transitive sphere
families that cannot be sent to the full family of round equators by one
diffeomorphism. The theorem above shows that this global nonlinearity is invisible
to the topology and isotopy class of every two-member intersection.

## Proof

### 1. Distinct members are transverse whenever they meet

Suppose \(x\in\Sigma_\sigma\cap\Sigma_\tau\) and
\(T_x\Sigma_\sigma=T_x\Sigma_\tau=\Pi\). The defining transitivity condition says
that through each \((x,\Pi)\in G_n(M)\) there is a unique member of \(\mathscr Z\)
tangent to \(\Pi\) at \(x\). Hence \(\sigma=\tau\), a contradiction. Therefore
distinct members cannot be tangent at a common point. Since they are hypersurfaces,
every nonempty intersection is transverse and is a smooth codimension-two
submanifold of \(M\).

### 2. The pair-incidence projection is a submersion

The universal incidence
\[
\mathcal I=\{(x,\sigma)\in M\times P:x\in\Sigma_\sigma\}
\]
is smooth. One way to see this is to use Martins' double fibration
\[
G_n(M)\xrightarrow{\mu}M,\qquad G_n(M)\xrightarrow{\nu}P:
\]
the map \((\mu,\nu)\) identifies \(G_n(M)\) smoothly with \(\mathcal I\).

Near \((x,\sigma)\in\mathcal I\), choose a local defining function
\(F(x,\sigma)\) for the family, with \(d_xF\ne0\). Near a point of
\(\mathcal J^{(2)}\), the latter is cut out by
\[
F(x,\sigma)=0,\qquad F(x,\tau)=0.
\]
For \(\sigma\ne\tau\), Step 1 says that the two \(x\)-covectors
\(d_xF(\cdot,\sigma)\) and \(d_xF(\cdot,\tau)\) are linearly independent. Given
arbitrary parameter velocities \((\dot\sigma,\dot\tau)\), one can therefore choose
\(\dot x\in T_xM\) solving the two linearized incidence equations. Thus \(dq\) is
onto everywhere, so \(q\) is a submersion.

### 3. Every distinct pair intersects

By Martins' classification, \(M\) is compact. Hence \(q\) is proper: the preimage
of a compact subset \(K\subset F_2(P)\) is a closed subset of \(M\times K\).

The image of \(q\) is open because \(q\) is a submersion and closed because \(q\)
is proper. It is nonempty. Indeed, fix \(\sigma\), choose \(x\in\Sigma_\sigma\),
and choose a hyperplane \(\Pi\subset T_xM\) different from
\(T_x\Sigma_\sigma\). Transitivity supplies the unique member \(\Sigma_\tau\)
tangent to \(\Pi\) at \(x\); necessarily \(\tau\ne\sigma\), and
\(x\in\Sigma_\sigma\cap\Sigma_\tau\).

Martins proves that \(P\) is a connected closed smooth \((n+1)\)-manifold and,
topologically, \(P\) is \(\mathbb R\mathbb P^{n+1}\) in both cases relevant here.
Since \(n+1\ge3\), the ordered configuration space \(F_2(P)\) is connected.
Therefore the nonempty clopen image of \(q\) is all of \(F_2(P)\).

The proper surjective submersion theorem now makes \(q\) a smooth locally trivial
bundle. In particular, all pairwise intersections have the same diffeomorphism
type.

### 4. Identification of the fiber

Fix \(\sigma\in P\) and a nonzero \(\zeta\in T_\sigma P\), and take a smooth
curve \(\sigma(t)\) with \(\sigma(0)=\sigma\) and \(\dot\sigma(0)=\zeta\). For
sufficiently small \(t\), the nearby member \(\Sigma_{\sigma(t)}\) is the normal
graph over \(\Sigma_\sigma\) of a smooth normal section \(u_t\), with
\[
t^{-1}u_t\longrightarrow\bar\zeta
\]
smoothly, where \(\bar\zeta\) is the infinitesimal normal variation associated
with \(\zeta\).

Martins' first-order evaluation theorem implies that \(0\) is a regular value of
every nonzero infinitesimal variation. In the two-sided case, Proposition 2.7
identifies \(\bar\zeta^{-1}(0)\) with an equator
\(\mathbb S^{n-1}\subset\mathbb S^n\). In the one-sided case, the corresponding
construction identifies it with a projective hyperplane
\(\mathbb R\mathbb P^{n-1}\subset\mathbb R\mathbb P^n\).

Regular zero sets are stable under sufficiently small smooth perturbations. Hence,
for small nonzero \(t\),
\[
\Sigma_\sigma\cap\Sigma_{\sigma(t)}=u_t^{-1}(0)
\]
is respectively diffeomorphic to \(\mathbb S^{n-1}\) or
\(\mathbb R\mathbb P^{n-1}\). Since all fibers of \(q\) are diffeomorphic, this
identifies every pairwise intersection.

### 5. The embedding type inside either member is standard

Fix \(\sigma\). Consider
\[
q_\sigma:
\{(x,\tau):\tau\ne\sigma,\ x\in\Sigma_\sigma\cap\Sigma_\tau\}
\longrightarrow P\setminus\{\sigma\}.
\]
The same transversality and compactness argument makes \(q_\sigma\) a proper
submersion. The base \(P\setminus\{\sigma\}\) is path connected. Pulling
\(q_\sigma\) back along a path from a nearby parameter to any prescribed
\(\tau\ne\sigma\) gives a smooth isotopy of the intersection submanifold inside
the fixed \(\Sigma_\sigma\). The isotopy extension theorem promotes it to an
ambient isotopy of \(\Sigma_\sigma\).

For a nearby parameter, Step 4 identifies the intersection with the regular zero
set of an infinitesimal variation, and Martins' local classification makes that
zero set an equator or a projective hyperplane. This proves the claimed standard
embedding type and the statements about complements.

## Checks and scope

- The round equator family in \(\mathbb S^{n+1}\) and the hyperplane family in
  \(\mathbb R\mathbb P^{n+1}\) realize the two conclusions exactly.
- The proof uses only transitivity and closed embeddedness; minimality is not
  required. Minimal hypersurface Zoll families are a corollary.
- No statement is made about triple or higher intersections. Pairwise
  transversality does not force three or more normal directions to be independent,
  so higher incidence topology can change.
- The theorem does not assert that the entire family is globally conjugate to
  round equators or projective hyperplanes. Such a statement is false in the
  spherical case by examples cited by Martins.
- The result is stated for ambient dimension at least three. The two-dimensional
  projective-geodesic theory of LeBrun and Mason is not part of the originality
  claim.

## Relation to prior literature

The principal input is Gustavo Martins, *Topological and spectral rigidity of
hypersurface Zoll manifolds*, arXiv:2609.20689 (2026). Theorems A and B classify
the ambient manifold and parameter space; Proposition 2.7 and the one-sided
construction in Section 2.2 classify infinitesimal nodal hypersurfaces. The paper
also constructs a special one-parameter comparison in which intersections are
spheres, but does not state an arbitrary-pair incidence theorem.

The earlier papers by Ambrozio--Marques--Neves on Zoll families of minimal
hypersurfaces (arXiv:2112.01448, published in *Journal of Differential Geometry*
in 2025) and Ambrozio--Guajardo on equivariant constructions
(arXiv:2501.16032) provide the underlying examples and deformation theory.
Searches of these papers and of the surrounding literature found no statement that
every two distinct members of an arbitrary unoriented transitive family must
intersect transversely with the standard codimension-two topology, nor the
configuration-space bundle formulation above.

To the best of our knowledge, the arbitrary-pair globalization and its isotopy
consequence are new.

## References

1. G. Martins, *Topological and spectral rigidity of hypersurface Zoll manifolds*,
   arXiv:2609.20689, 2026.
2. L. Ambrozio, F. C. Marques, A. Neves, *Riemannian metrics on the sphere with
   Zoll families of minimal hypersurfaces*, *Journal of Differential Geometry*
   130 (2025), 269--341; arXiv:2112.01448.
3. L. Ambrozio, D. Guajardo, *Equivariant constructions of spheres with Zoll
   families of minimal spheres*, arXiv:2501.16032.
4. C. LeBrun, L. J. Mason, *Zoll manifolds and complex surfaces*, *Journal of
   Differential Geometry* 61 (2002), 453--535.
