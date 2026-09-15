# Two-sided diffeomorphism classification of manifolds homeomorphic to HP^4

## Context

Let HP^4 be quaternionic projective 4-space, a closed simply connected
16-manifold with integral cohomology ring Z[u]/(u^5), |u|=4, and
<u^4,[HP^4]>=+1. Let Theta_16 = Z/2 = {[S^16],[Sigma^16]} be the
Kervaire-Milnor group of homotopy 16-spheres. For a closed smooth
16-manifold M, write C(M) for concordance classes of pairs (N,f) with
f:N->M a homeomorphism, and I(M), Ih(M), Ic(M) for the inertia,
homotopy inertia, and concordance inertia groups. In dimension >= 5,
Kirby-Siebenmann-Sullivan theory gives C(M)=[M,Top/O] and the set of
diffeomorphism types of manifolds homeomorphic to M is the orbit space
of the action of self-homeomorphisms by precomposition. The published
input used here is the Basu-Kasilingam computation (Forum Math. 2022,
Thm 3.1(ii)): f^*:Theta_16->C(HP^4) is an isomorphism, so
C(HP^4)={[HP^4,Id],[HP^4#Sigma^16,h_can]}=Z/2 and Ic(HP^4)=0, where
h_can:HP^4#Sigma^16->HP^4 is the canonical homeomorphism.

## Definitions

- HP^4: quaternionic projective 4-space, dim 16, H^*(HP^4;Z)=Z[u]/(u^5).
- Theta_16: group of h-cobordism classes of homotopy 16-spheres, Z/2.
- h_can: canonical homeomorphism HP^4#Sigma->HP^4, identity outside disc.
- C(HP^4): concordance classes of smoothings; C(HP^4)=Z/2 by input.
- MCG^+(HP^4), MCG^pm(HP^4): orientation-preserving resp. all
  self-homeomorphisms modulo isotopy, acting on C(HP^4) by pullback.

## Result

Let M^16 be closed smooth oriented and homeomorphic to HP^4. Then M is
orientation-preservingly diffeomorphic to exactly one of HP^4 or
HP^4#Sigma^16, and these two are not orientation-preservingly
diffeomorphic; hence I(HP^4)=0. Every self-homeomorphism (hence every
self-diffeomorphism) of HP^4 is orientation-preserving, so the
unoriented classification coincides: exactly two diffeomorphism types.
The actions of orientation-preserving and of all self-homeomorphisms on
C(HP^4) are trivial, so both C(HP^4)/MCG^+(HP^4) and
C(HP^4)/MCG^pm(HP^4) consist of two singleton orbits. In particular
HP^4#Sigma^16 is diffeomorphic to HP^4 neither orientation-preservingly
nor after allowing orientation reversal.

## Proof / evidence

Lemma (degree rigidity): if h:HP^4->HP^4 is a homeomorphism or homotopy
equivalence, h^*(u)=k u with k=+-1; by ring naturality h^*(u^4)=k^4 u^4
=u^4, while pairing with the fundamental class gives deg h=k^4=+1. So
no orientation-reversing self-homeomorphism or diffeomorphism exists.
Proposition (trivial action): with f:HP^4->S^16 degree-one,
[HP^4,S^16]=Z by degree since the 12-skeleton maps null-homotopically
into S^16; as deg h=+1, f o h ~= f, hence h^* o f^*=f^*, and since f^*
is an isomorphism h^*=id on C(HP^4). Main step: if
psi:HP^4#Sigma^16->HP^4 were a diffeomorphism, the Lemma forces
deg psi=+1, so h=h_can o psi^{-1} lies in Homeo(HP^4) and
(HP^4#Sigma^16,h_can) is concordant to (HP^4,h), i.e. x1=h.x0; the
Proposition gives h.x0=x0, so x1=x0, contradicting C=Z/2 with
x1=f^*([Sigma^16])!=0. Hence I(HP^4)=0. Conversely every M homeomorphic
to HP^4 defines a class in C(HP^4) and is concordant, hence
diffeomorphic, to one of the two representatives. Finite group steps
(k^4=+1, trivial Z/2 action gives two singleton orbits, ker f^*=0)
were machine-checked in output/artifacts/verify_orbits.py.

## Limitations

The concordance isomorphism C(HP^4)=Z/2 (exact sequence, James
attaching maps, Madsen-Milgram splitting, Toda-bracket computation) is
taken from the cited published proof as re-verified from the full
text, not re-derived from first principles. The verification script
checks only the finite group-theoretic and degree-arithmetic steps.
Uses high-dimensional smoothing theory (dim 16, simply connected);
does not extend to dimension 4.

## Reproducibility

Cohomology-ring and degree argument is elementary; orbit contradiction
uses only C=Z/2 and the trivial action. Re-run
`python3 output/artifacts/verify_orbits.py` for the finite checks.
Primary inputs: Kervaire-Milnor (Theta values), Kirby-Siebenmann
(C(M)=[M,Top/O] and orbit bijection), Basu-Kasilingam arXiv:1708.06582
Thm 3.1(ii) and cofibre sequence (3.1).

## References

- Kervaire-Milnor, Groups of homotopy spheres I, Ann. of Math. 77 (1963).
- Kirby-Siebenmann, Foundational essays, Ann. Math. Stud. 88 (1977).
- Basu-Kasilingam, Inertia groups and smooth structures on quaternionic
  projective spaces, Forum Math. 34 (2022); arXiv:1708.06582.
- Kramer-Stolz, Diffeomorphism classification of manifolds like
  projective planes, J. Diff. Geom. 77 (2007) (broader census checked,
  excludes HP^4 by homology rank).
