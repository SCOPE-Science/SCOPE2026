# Independent audit — 2026-09-29

Record: `2026/09/11/058`  
Audited tree: `8656a4e4563222f099af5c73ae415faa0e175646`  
Disposition: **repaired**

## Correctness

I independently checked that `1031` is prime with `1031 ≡ 3 mod 4` and directly
counted `#E(F_1031)=1032` for `E:y^2=x^3+x`, hence trace zero and supersingularity.
The standard `j=1728` maximal order for this model has basis
`1, i, (1+k)/2, (i+j)/2` with `j` the Frobenius and `k=ij`, matching the cited
Stange note. In that basis
`4N(alpha)=(2x1+x3)^2+(2x2+x4)^2+p(x3^2+x4^2)`.
If `(x3,x4) != (0,0)`, integrality forces `N(alpha) >= ceil(p/4)=258`, with equality
at `(i+j)/2`. A based 2-isogeny loop of length at most 8 has degree at most 256,
so it lies in the commutative `Q(i)` subfield. The non-commuting generating pair
requested by the target is therefore impossible.

The record's mathematics is sound, but its Definitions introduced Frobenius as `pi`
and then used an undefined quaternion generator `j` in the main basis. The staged
repair explicitly sets `j := pi` and makes the relations consistent.

## Originality

The maximal-order description is standard. The contribution is the explicit
`p=1031`, length-8 norm-gap specialization and target disproof.

## Scientific value

The sharp `258 > 256` obstruction is a concise and reusable diagnostic for why
the requested short-loop generator construction cannot exist at this vertex.

Sources: https://github.com/SCOPE-Science/SCOPE2026/tree/e9ed144c13b7834896a844cc4f9cac3c25a168a6/2026/09/11/058 ; https://math.colorado.edu/~kstange/papers/1728.pdf
