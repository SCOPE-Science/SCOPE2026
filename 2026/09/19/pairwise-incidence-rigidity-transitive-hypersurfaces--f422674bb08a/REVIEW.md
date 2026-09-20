# Review

## Correctness

**PASS.** The proof separates a local first-jet argument from a global
continuation argument.

For distinct family members, tangency at a common point would give the same
point-hyperplane pair in the hyperplane Grassmann bundle, contradicting the
defining uniqueness of the transitive family. Thus every existing pair
intersection is transverse.

At a fixed member \(\Sigma_\sigma\), the tangent space \(T_\sigma P\) maps to
normal variation sections. Local graph coordinates for the Legendrian
foliation identify the transverse derivative with the complete normal
first jet, giving an isomorphism
\[
T_\sigma P\cong
N_x\Sigma_\sigma\oplus
(T_x^*\Sigma_\sigma\otimes N_x\Sigma_\sigma)
\]
at every point. Hence every nonzero infinitesimal normal section is
transverse to zero. In the two-sided case, a basis of parameter variations
gives a normalized map \(\Sigma_\sigma\to S^n\) with everywhere invertible
differential; using \(\Sigma_\sigma\cong S^n\) and \(n\ge2\), this is a
diffeomorphism, so each nonzero section has an equatorial \(S^{n-1}\) zero
set. In the one-sided case, the same construction on the normal orientation
double cover is antipodal-equivariant and descends to
\(\Sigma_\sigma\cong\mathbb{RP}^n\), giving an
\(\mathbb{RP}^{n-1}\) zero set. The implicit function theorem transfers this
standard zero set to intersections with sufficiently nearby family members.

For the global step, the pair-incidence space over
\(P\setminus\{\sigma\}\) is smooth and its projection is a submersion by
transversality. It is proper because \(\Sigma_\sigma\) is compact and the
universal family over a compact parameter set is compact. Therefore its image
is both open and closed. Since \(P\) is a connected \((n+1)\)-manifold and
\(n\ge2\), the punctured parameter space is connected; the nearby nonempty
fiber forces surjectivity. Ehresmann's theorem then makes all pair
intersections diffeomorphic and isotopic to the nearby standard fiber.

Stress checks included the possibility of disjoint members, disconnected
intersections, and topology change under variation. These are precisely
excluded by the nonempty local fiber plus proper-submersion continuation.
The proof does not use minimality, so it correctly applies to the underlying
unoriented transitive family before specializing to hypersurface Zoll
families.

## Originality

**PASS, to the best of our knowledge.** Martins' September 2026 preprint was
inspected around the definition of transitive families, its double-fibration
description, and its topology theorems. It proves that the ambient manifold
and individual family members have sphere/projective-space topology and
develops the infinitesimal normal-variation machinery, but no theorem
classifying every pairwise intersection or the proper pair-incidence bundle
was located.

The literature check also covered combinations of “Zoll family”, “transitive
family”, “minimal hypersurface”, “pairwise intersection”, “incidence”,
“transverse intersection”, “sphere”, and “projective hyperplane”, together
with the current construction papers of Ambrozio--Marques--Neves and
Ambrozio--Guajardo and the transitive-family framework of Gálvez--Mira. No
matching global pairwise-incidence theorem was located. The broader oriented
transitive-family notion is not a substitute: standard oriented examples can
have disjoint members, so the result genuinely uses the closed embedded
unoriented setting classified by Martins.

No specifically identified inaccessible source gives concrete evidence of
prior coverage. The principal residual risk is the extreme recency of
arXiv:2609.20689: a later version or an unindexed parallel observation may
make the pairwise incidence consequence explicit.

An archive overlap check against the current SCOPE archive found no record
indexed by the motivating arXiv identifier, hypersurface Zoll intersections,
transitive-family pairwise incidence, or equivalent projective-hyperplane
terminology.

## Value

**PASS.** The result upgrades a classification of individual hypersurfaces to
a global incidence law for the whole family. It proves, without a curvature or
minimality calculation, that every two distinct members must meet, that the
meeting is always transverse and connected, and that its topology cannot
bifurcate as the second member moves. The proper-submersion formulation also
packages all intersections with one fixed member into a smooth fiber bundle.

For hypersurface Zoll geometry this supplies a concrete analogue of the
classical incidence of great spheres/projective hyperplanes. In dimension
three it gives the especially transparent consequence that every two
distinct Zoll minimal surfaces meet in one embedded circle.

## Limitations

The theorem is restricted to unoriented transitive families of closed
embedded hypersurfaces in dimensions \(n+1\ge3\). It does not cover arbitrary
oriented transitive families, simultaneous intersections of three or more
members, quantitative intersection angles, or the intrinsic geometry of the
intersection. The \(n=1\) case is not treated. The motivating paper is very
recent, leaving a residual originality risk from later revisions or
unindexed parallel work.

**Same-model review: passed. Independent audit: not yet performed.**
