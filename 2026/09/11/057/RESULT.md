# Non-Golod certificate for the facet-glued stacked-plus-octahedron 9-sphere

## Context

The admitted target claimed that for G9, the 9-vertex 2-sphere obtained as the
facet connected sum of a 6-vertex stacked 2-ball block with the octahedron
boundary along a common triangular facet, all products in
Tor_{k[v]}(k[G9],k) vanish and every defined higher Massey product contains
zero via exhibited bounding cochains, hence k[G9] is Golod with a complete
per-bidegree trivialization ledger. Prior literature (flag characterizations,
Taylor-minimal criteria, multiwedge families, BBCG splitting) did not name or
certify this specific non-flag facet gluing.

## Definitions

Let S be the 6-vertex stacked 2-sphere on {0,...,5} with facets
012,123,014,034,134,025,035,235, and O the octahedron boundary on
{0,1,2,6,7,8} with opposite pairs (0,6),(1,7),(2,8) and facets
012,018,027,078,126,168,267,678. Fix gluing facet F=012 and form
G9 = (S \ {F}) union (O \ {F}), i.e. delete the interior gluing triangle:

G9 = <014,018,025,027,034,035,078,123,126,134,168,235,267,678>,

14 facets on 9 vertices. Work over k=Q in the Koszul-type dga
R(K) = Lambda[u_1,...,u_m] tensor k[K], |u_i|=(-1,2e_i), |v_i|=(0,2e_i),
d(u_i)=v_i, whose cohomology is Tor_{k[v]}(k[K],k) = H*(Z_K). In multidegree
J the cochain piece C(J) has basis e_L = u_{J\L} v_L over faces L of J in K,
with Baskakov product e_L . e_M = +/- e_{L disjoint-union M} when the union
is a face, 0 otherwise.

## Result

For the named G9 above, the Tor-algebra product
H^3(Z_G9) x H^3(Z_G9) -> H^6(Z_G9) is nonzero. The missing-edge classes
[{0,6}] and [{1,7}] satisfy [{0,6}] cup [{1,7}] = [{0,1,6,7}] != 0, the
edge-monomial e_01 over the hollow 4-cycle K_{0167}. Hence Q[G9] is NOT
Golod and the target universal-vanishing claim is false. The same C4
mechanism produces a verified nonzero missing-edge x missing-edge product
for every facet-sum of a stacked 6-vertex block with the octahedron (all 3
stacked-facet orbits x all 6 octahedron bijections, 18 complexes).

## Proof / evidence

G9 is a triangulated 2-sphere: V-E+F = 9-21+14 = 2, every edge lies in
exactly 2 facets, every vertex link is a cycle, simplicial homology
(H0,H1,H2)=(1,0,1). Missing edges include {06} and {17}; K_{0167} is the
hollow 4-cycle 0-1-6-7-0 (cycle edges 01,07,16,67 present; diagonals 06,17
missing; no triangle and no S-facet inside). Classes a=[e_0] in C({06}) and
b=[e_1] in C({17}) are closed and non-exact. Their product is
[e_0].[e_1]=[e_{01}] (shuffle +1), closed since neither 016 nor 017 is a
face. With d(e0)=e01+e07, d(e1)=e01-e16, d(e6)=-e16+e67, d(e7)=e07+e67,
e01 = d(sum c_v e_v) would require c0+c1=1, c0+c7=0, c1+c6=0, c6+c7=0,
whose alternating sum gives 0=1; the exact rational column-space rank test
confirms non-exactness. Thus [e_{01}] != 0 generates H~^0(K_{0167}), a
nonzero H^6(Z_G9) class. By Berglund-Jollenbeck-Katthan, nonzero Tor product
implies non-Golodness. The dga model is certified: d^2=0 on all 512
multidegree pieces, Leibniz rule on all 6799 small disjoint-support pairs.
Corroboration: 24 nonzero disjoint missing-edge-pair products, Tor^+ dim
227 over 205 multidegrees, Poincare pairings of missing edges with
complementary cycles into the (9,3) top class. The integral 0=1 obstruction
is unsolvable over any field (checked GF(2,3,5,7,101)), so the product is
nonzero over any field. Reproduction: `python3 output/artifacts/verify.py`
prints VERIFY_OK; fixed-loop rerun of the enumeration over all 18 gluings
finds a C4 witness in each.

## Limitations

Machine certificate is over Q; transfer to arbitrary fields uses freeness
of full-subcomplex homology of an S^2 triangulation plus the integral 0=1
system, not a separate machine run per field. Only the 6+6-3=9
stacked-plus-octahedron facet sums are covered; larger stacked blocks are
conjectured analogous but not claimed. The archived enumerate_check.py has
an indentation bug testing 3 of 18 gluings as written; the universal claim
was independently re-verified for all 18 with a corrected loop.

## Reproducibility

- output/artifacts/verify.py -> VERIFY_OK (sphere, homology, d^2,
  Leibniz, missing edges, C4, closedness, non-exactness, 24-scan, Tor
  snapshot, Poincare pairings).
- output/artifacts/enumerate_check.py -> ENUMERATE_OK as archived (covers
  3 representatives due to loop-indent bug); corrected full 18-case loop
  re-run: all sphere-ok with C4 witness.

## References

- K. Iriye, D. Kishimoto, Golodness and polyhedral products for two
  dimensional simplicial complexes, arXiv:1506.08970 (surface triangulation
  Golod iff 1-neighborly; chordality/non-Golod mechanism).
- L. Katthan, A non-Golod ring with a trivial product on its Koszul
  homology, arXiv:1511.04883 (dim<=3 Golod iff Koszul product trivial).
- A. Berglund, M. Joellenbeck, On the Golod property of Stanley-Reisner
  rings, J. Algebra 315 (2007), 249-273 (chordless-cycle criterion).
- S. Amelotte, Connected sums of sphere products and minimally non-Golod
  complexes; F. Fan, X. Wang, Moment-angle manifolds and connected sums of
  simplicial spheres; V. Kovyrshina, T. Panov, Moment-angle manifolds for
  3-dimensional spheres (connected-sum background; none names G9).
