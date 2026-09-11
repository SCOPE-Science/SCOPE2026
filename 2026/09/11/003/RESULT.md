# Strictly-defined non-zero 4-fold Massey product on the single-vertex-doubled dodecahedron moment-angle manifold

## Context

Moment-angle manifolds $Z_P$ over Pogorelov polytopes (simple flag
3-polytopes without 3- or 4-belts; includes the dodecahedron and fullerenes)
are a recognized frontier for Massey order, formality, and LS-category.
Zhuravleva constructed nontrivial triple Massey products for every Pogorelov
polytope (degrees $(4,n-2,3)$, $n\\ge 5$; dodecahedron $H^4\\times H^3\\times
H^3\\to H^9$) and noted there are no triples of 3-dimensional classes in this
class. Whether Massey order grows to 4 under the natural vertex-doubling
(simplicial wedge / J-construction) operation was open.

## Definitions

Let $P_0$ be the dodecahedron and $P_1$ the polytope from a single
facet-doubling at the recorded vertex. Its nerve $K_1$ is the 13-vertex flag
triangulation of $S^2$ in `complexes.json` (36 edges, 30 triangles, 5
tetrahedra, $\\chi=2$, induced-$C_4$-free; doubling locus $D=\\{0,1\\}$).
Work over $\\mathbb{Q}$ in the Koszul model
$R=\\mathbb{Q}[u]\\otimes \\mathbb{Z}[K]/(v^2,uv)$, $du=v$, with multidegree
$J$ tracking the $v$-support. A degree-3 class on a nonedge $\\{p,q\\}$ is the
cocycle $u_p v_q$ (total degree $2|J|-|L|=3$).

## Result

Let $Z=Z_{P_1}$ and

- $a=(3,9),\\quad b=(2,7),\\quad c=(8,10),\\quad d=(4,11) \\in H^3(Z;\\mathbb{Q})$,
- support $S=\\{2,3,4,7,8,9,10,11\\}$, disjoint from $D$.

Then:

1. All six pairwise cup products vanish via the recorded bounding cochains
   $d(x)+P=0$ (ordered product; see table in DRAFT/certificate.json).
2. Both inner triples vanish coherently: $t_{abc}=x_{ab}c-ax_{bc}=0$
   ($y_{abc}=0$); $t_{bcd}=x_{bc}d-bx_{cd}$ is the single term
   $-3/4\\,(24810)$ killed by the recorded 6-term $y_{bcd}$.
3. The 4-fold representative in multidegree
   $J_w=(2,3,4,7,8,9,10,11)$ (total degree 10),
   `w = -7/16 (2347810) + 5/16 (23471011) + 3/16 (2348910) - 1/16 (34791011) - 1/16 (37891011) + 5/8 (23481011)`,
   satisfies $d(w)=0$ exactly.
4. $[w]\\ne 0$ in $H(J_w)$, and $w$ lies outside the exactly computed
   54-column indeterminacy span (cup-choice with re-solved triple killings,
   killing-choice, $aH+Hd$, second-order $z_{ab}z_{cd}$), by exact RREF.

Hence $\\langle a,b,c,d\\rangle$ is strictly defined and does not contain
zero: $Z_{P_1}$ has Massey order at least 4 — the first order-4 Massey datum
on a Pogorelov manifold.

## Proof / evidence

Exact rational linear algebra over $\\mathbb{Q}$ (`Fraction`), per
multidegree: $d^2=0$ checks, recomputed ordered cup products, triple
representatives and killings, $w$ recomputed from $(x,y)$ data, non-exactness,
and indeterminacy non-membership. Independently replayed from scratch:

```text
python3 output/artifacts/verify.py   # -> VERIFY_OK (gates V0--V8)
```

## Limitations

Only $P_1$ non-vanishing is machine-checked. Propagation to $P_n$ ($n\\ge 2$)
is a stated sketch (support avoids the doubling locus), not a checked proof.
Indeterminacy non-membership is relative to the stated 54-column exact model.

## Reproducibility

`output/artifacts/complexes.json` (nerve adjacency), `output/artifacts/certificate.json`
(exact quad, cups, triple killings, $w$), `output/artifacts/verify.py`
(independent from-scratch replay, stdlib only).

## References

- Zhuravleva, Massey products for Pogorelov polytopes, arXiv:1707.07365.
- Beben–Grbic, LS-category and higher Massey products, arXiv:1601.06297.
- Limonchenko–Millionshchikov, Higher order Massey products and applications, arXiv:2002.10050.
- Grbic–Linton, Non-trivial higher Massey products, arXiv:1911.07083.
- Limonchenko, Topology of polyhedral products over multiwedges, arXiv:1711.00461.
- Baralic–Grbic–Limonchenko–Vucic, Toric objects associated with the dodecahedron, Filomat 2020.
