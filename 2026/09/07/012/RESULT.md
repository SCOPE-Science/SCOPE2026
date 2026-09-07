# Stem 2-step nilpotent Lie algebras of dimension 7 with 3-dimensional derived algebra over Q: nine explicit types, Pfaffian invariants, and infinitude

## Context

Small nilpotent Lie algebras bridge textbook Heisenberg examples and wild classification.
Dimension 7 is the first dimension where 2-step types proliferate yet remain describable
by alternating forms. Derivation dimensions control rigidity, degenerations and
automorphism-group dimensions. The stratum with `V=g/[g,g]` of dimension 4 and
`W=[g,g]` of dimension 3, with `Z(g)=[g,g]` (stem `(7,3)`), corresponds to nets of
`4x4` skew forms up to `GL(4)xGL(3)` and is checkable by rational linear algebra.
Over algebraically closed fields the dimension-7 classification is finite (Gong);
over `Q` arithmetic (isotropy, square classes) creates infinitely many forms.
This record certifies nine explicit `Q`-witnesses, their exact invariants, and the
consequent impossibility of any finite complete census.

## Definitions

Fix `Q`-basis `e1..e7`. Put `V=span(e1..e4)`, `W=span(e5,e6,e7)`.
For a triple of `4x4` skew-symmetric rational matrices `(A5,A6,A7)` define

```
[ei,ej] = sum_{k=5..7} (Ak)_{ij} e_k  for 1<=i,j<=4,
```

all other brackets zero, so `W` is central by construction.
Write each skew matrix by its upper triangle `(a12,a13,a14,a23,a24,a34)`.
Then `Pf(A)=a12*a34-a13*a24+a14*a23` and for `x=(x1,x2,x3)`,

```
f(x) = Pf(x1*A5+x2*A6+x3*A7)
```

is a ternary quadratic form (Pfaffian net) with Gram matrix `G`.

Since `[g,g] subset W` and `W` central, `[[g,g],g]=0`; Jacobi holds automatically
(also brute-force checked). Derived algebra is the image of `wedge^2 V -> W`;
`dim[g,g]=3` iff the three 6-vectors are linearly independent (rank 3).
`x=v+w` is central iff `v` is in the common radical
`Rad={v: Ak v=0 forall k}`; hence `dim Z=3+dim Rad`.
Stem (`Z=[g,g]`, dim 3) iff `Rad=0` and derived rank 3.
Any isomorphism preserves characteristic ideals `Z` and `[g,g]`, hence induces
`Q:W->W'` and `Pbar:g/W->g'/W'`; writing `P` for a lift, the `W`-component drops
by centrality and `phi'(Pbar u ^ Pbar v)=Q phi(u^v)`.

Derivations: `D([x,y])=[Dx,y]+[x,Dy]`, 49 unknowns, 147 equations `i<j,p`;
`dim Der=49-rank(A)`. Trivial-coefficient Chevalley-Eilenberg:
`d1:C^1(7)->C^2(21)`, `d1[(i,j),k]=-c[i,j,k]`; `d2:C^2(21)->C^3(35)`,
`(d beta)(i,j,k)=-beta([ei,ej],ek)-cyc`; `H1=7-r1`, `H2=21-r2-r1` where
`r1=rank d1`, `r2=rank d2`. All ranks over `QQ` by exact elimination, no floats.

## Catalog (explicit integer structure constants)

`[ej,ei]=-[ei,ej]`; unlisted pairs zero; `e5,e6,e7` central.

- **G1 (aniso, rank 3):** `(1,0,0,0,0,1),(0,1,0,0,-1,0),(0,0,1,1,0,0)`.
  `[e1,e2]=e5,[e3,e4]=e5; [e1,e3]=e6,[e2,e4]=-e6; [e1,e4]=e7,[e2,e3]=e7.`
  `f=x1^2+x2^2+x3^2`.
- **G2 (iso, rank 3):** `(1,0,0,0,0,1),(0,1,0,0,1,0),(0,0,1,1,0,0)`.
  Same except `[e2,e4]=+e6`. `f=x1^2-x2^2+x3^2`.
- **G3..G7 (rank 2, t=1,2,3,5,7):** `A5=(1,0,0,0,0,1)`, `A6(t)=(0,1,0,0,t,0)`,
  `A7=(0,0,1,0,0,0)`. `[e1,e2]=e5,[e3,e4]=e5; [e1,e3]=e6,[e2,e4]=t*e6; [e1,e4]=e7.`
  `f=x1^2-t*x2^2`, Gram `diag(1,-t,0)`.
- **G8 (rank 1):** `(1,0,0,0,0,1),(0,1,0,0,0,0),(0,0,1,0,0,0)`.
  `[e1,e2]=e5,[e3,e4]=e5; [e1,e3]=e6; [e1,e4]=e7.` `f=x1^2`.
- **G9 (rank 0):** `(1,0,0,0,0,0),(0,1,0,0,0,0),(0,0,1,0,0,0)`.
  `[e1,e2]=e5; [e1,e3]=e6; [e1,e4]=e7.` `f=0`.

Stem certificates: derived rank 3 because columns 1,2,3 of the `3x6` matrix are
the identity (det 1). For G1..G8,
`A5=[[0,1,0,0],[-1,0,0,0],[0,0,0,1],[0,0,-1,0]]` has det 1, invertible, so
`Rad=0`. For G9, `A5v=(v2,-v1,0,0)`, `A6v=(v3,0,-v1,0)`, `A7v=(v4,0,0,-v1)`;
joint zero forces `v=0`. Hence `Z=W`, `dim Z=3=dim[g,g]`.

Invariant table (exact-machine, replayed):

| name | Pf | Pf-rank | dim Der | H1 | H2 | (r1,r2) |
|---|---|---|---|---|---|---|
| G1 | x1^2+x2^2+x3^2 | 3 | 19 | 4 | 11 | (3,7) |
| G2 | x1^2-x2^2+x3^2 | 3 | 19 | 4 | 11 | (3,7) |
| G3(t=1) | x1^2-x2^2 | 2 | 20 | 4 | 11 | (3,7) |
| G4(t=2) | x1^2-2x2^2 | 2 | 20 | 4 | 11 | (3,7) |
| G5(t=3) | x1^2-3x2^2 | 2 | 20 | 4 | 11 | (3,7) |
| G6(t=5) | x1^2-5x2^2 | 2 | 20 | 4 | 11 | (3,7) |
| G7(t=7) | x1^2-7x2^2 | 2 | 20 | 4 | 11 | (3,7) |
| G8 | x1^2 | 1 | 22 | 4 | 11 | (3,7) |
| G9 | 0 | 0 | 25 | 4 | 12 | (3,6) |

Most rigid observed `G_min=G1` (also G2), `dim Der=19` (hence
`dim H^1(ad)=15` since `dim Inn=g-Z=4`); least rigid `G_max=G9`, `dim Der=25`.

## Result

**Theorem 1 (nine pairwise non-isomorphic stem types).**
`G1..G9` above are stem 2-step Lie algebras over `Q` (dim 7,
`dim[g,g]=dim Z=3`) and pairwise non-isomorphic over `Q`.

**Theorem 2 (infinitude; no finite complete census).**
For each `t in Q*` let `g_t` be as in G3..G7 (`[e2,e4]=t e6`,
`f_t=x1^2-t x2^2`). Each is stem. If `g_t cong g_s` over `Q` then
`t/s in (Q*)^2`. Taking `t=p` prime gives infinitely many distinct square
classes, hence infinitely many pairwise non-isomorphic stem `(7,3)` Q-algebras.
No finite list is complete; completeness must be moduli (families).

**Lemma (Pfaffian transformation law) and corollaries.**
With notation above, `P^T A'(y) P = A(Q*y)` and
`det(P) Pf(A'(y))=Pf(A(Q*y))`, i.e. `f'(y)=lambda f(Q*y)` with
`lambda=det(P)^-1`. Hence up to nonzero scale and `GL(3,Q)` change, `f` is a
Q-isomorphism invariant. Preserved: (a) Gram rank (`G'=lambda Q^T G Q`);
(b) isotropy; (c) for rank-2 family the square class below.

## Proof / evidence

*Lemma proof.* `u^T A(x) v=x(phi(u^v))` by definition.
`y(phi'(Pbar u,Pbar v))=y(Q phi(u,v))=(Q*y)(phi(u,v))`.
LHS `=(Pbar u)^T A'(y)(Pbar v)=u^T P^T A'(y)P v`; RHS `=u^T A(Q*y)v` for all
`u,v`, giving matrix identity. Take `Pf` and use
`Pf(P^TBP)=det(P)Pf(B)` (4x4 identity `Pf=a12a34-a13a24+a14a23`, checked by
expansion and random integer trials). The lift's `W`-component drops because
`W'` is central.

*Rank 3 aniso vs iso.* `f1=x1^2+x2^2+x3^2` anisotropic: if `a^2+b^2+c^2=0`
rationally, scale to coprime integers; squares mod 4 are 0,1, so sum 0 mod 4
forces `a,b,c` even, contradicting coprimality unless zero.
`f2=x1^2-x2^2+x3^2` isotropic at `(1,1,0)`. Since G1,G2 share rank 3 and
Der/H2, only arithmetic separates them.

*Rank 2 square class.* If `f_s(y)=lambda f_t(Qy)`, write `G_t=diag(H_t,0)`,
`H_t=diag(1,-t)`. Then `G_s=lambda Q^T G_t Q`. Radicals are `span e3`, so
`Q span e3=span e3`; with `Q=[[A,b],[c^T,d]]`, `Qe3=(b,d)` in `span e3` gives
`b=0`, `d!=0`, `det Q=det A*d` so `A in GL2(Q)`. Then
`Q^T G_t Q=[[A^T H_t A,0],[0,0]]`, so `A^T H_t A=lambda^-1 H_s`.
Determinants: `det(A)^2(-t)=lambda^-2(-s)`, so `s/t=(lambda det A)^2` is a
square. For positive integers `t/s` square iff `t*s` square (differ by `s^2`).
With `T={1,2,3,5,7}`, the 10 products `2,3,5,7,6,10,14,15,21,35` are squarefree
>1, hence nonsquare by unique factorization (checked via `isqrt`); so
G3..G7 pairwise distinct. Cross-rank pairs separated by rank. This gives all
36 pairs. Der/H2/Pf-rank alone do not separate within same rank-3 or rank-2
classes.

*Infinitude.* Same stem check for all `t!=0` (A5 invertible, identity minor).
Square-class lemma gives `t/s` square necessary. Distinct primes give distinct
classes (`p/q` has odd exponents, cannot be a square; `p b^2=q a^2` forces
`p=q`). Over `C` they merge: with `l=sqrt(t/s)`, `P=diag(l,l^-1,1,1)` gives
`P^T A5 P=A5`, `P^T M2(t)P=l M2(s)` (since `t/l=l s`), `P^T M3 P=l M3`,
absorbed by `Q=diag(1,l,l)` on `W`. Similarly `G1 cong G2` over `Q(i)` via
`P=diag(i,1,i,1)`: sends G2 6-vectors to `i*v1,-v2,i*v3`. Thus 9 Q-types lie
over <=4 Pf-rank levels; Pf-rank completeness over C not claimed.

*Machine evidence.* `output/artifacts/verify_partial.py` (sympy over QQ +
stdlib, no floats) hardcodes 9 integer triples and rechecks Jacobi enumeration,
derived 3, stacked-12x4 rank 4 (radical 0), `dim Der` via `49-rank`, CE ranks,
Pf polys/ranks, isotropy witness and 10 `isqrt` checks: ALL PASS in ~1s
(Der nullspaces 0.77s). Auditor independently recomputed with `Fraction`
elimination (no sympy): same dims/ranks.

## Limitations

- Partial only; finite completeness disproved, not achieved.
- Der/H2 are exact-machine ranks, not hand-derived bases in full (bases for
  G1,G9 stored in input catalog; dims cross-checked with two implementations).
- Decomposability not tested; presented as stem only.
- `Der` 19 minimal only among observed catalog, not proved globally minimal.
- C-orbit classification (Pf-rank sufficiency), orbit closures/degenerations,
  adjoint cohomology over Q remain open.
- Originality web re-check failed with transport errors; comparison to
  Gong/Magnin/Burde is from brief + cutoff knowledge, confidence capped; no
  priority claim if prior Q-census exists.

## Reproducibility

Run `python3 output/artifacts/verify_partial.py` (requires `sympy`, stdlib
only). Expected: `derived=3 center=3 radical=0` for all 9,
`Der` 19,19,20x5,22,25, `H2` 11x8,12, Pf ranks 3,3,2x5,1,0, isotropy and 10
square-class passes, `ALL PASS` in seconds.

## References (nearest known, from brief)

- S.-C. Gong, Classification of nilpotent Lie algebras of dimension 7, PhD
  thesis Univ. Waterloo 1998. https://uwspace.uwaterloo.ca/handle/10012/133
- L. Magnin, Adjoint and trivial cohomology tables for indecomposable
  nilpotent Lie algebras of dim <=7 over C (2008), arXiv:0805.3380.
  https://arxiv.org/abs/0805.3380
- D. Burde, Degenerations of 7-dimensional nilpotent Lie algebras (2007),
  arXiv:math/0703802. https://arxiv.org/abs/math/0703802
