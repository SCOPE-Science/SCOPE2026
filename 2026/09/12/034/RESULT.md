# Double-relative K2 of the split node over F7 contains Z/48

## Setup

Let `F=F_7`, `B=F[t]`, and

`A = F[x,y]/(y^2-x^3-x^2) -> B`,  `x=t^2-1`,  `y=t(t^2-1)`.

Put `J=(t^2-1)B`. Then

`A = {f in F[t] : f(1)=f(-1)} = F + J`,

and `J` is the conductor `I` of `A` in `B`. Hence

`A/I ≅ F`,  `B/I ≅ F×F`,

with `A/I -> B/I` the diagonal map. This is the conductor (Milnor) square for the split node.

## Result

The birelative group `K_2(A,B,I)` is nonzero. More precisely, the Mayer–Vietoris boundary contains a subgroup isomorphic to `Z/48`.

Thus the proposed vanishing statement is false. The nonzero class is a boundary class from the conductor square; it is not detected by the literal Dennis–Stein/dlog route proposed in the original target.

## Proof

### 1. The conductor

Every element of `A` has the form `c+(t^2-1)g(t)`: writing `g(t)=g_0(t^2)+t g_1(t^2)` gives

`(t^2-1)g(t) = x g_0(x+1) + y g_1(x+1)`.

Conversely `F+J` plainly has equal values at `t=1` and `t=-1`, so `A=F+J={f:f(1)=f(-1)}`.

If `fB⊂A`, then both `f` and `tf` lie in `A`. Therefore

`f(1)=f(-1)` and `f(1)=-f(-1)`.

Because `2≠0` in `F_7`, both values are zero, so `(t^2-1)` divides `f`. Thus the conductor is exactly `I=J`. Chinese remainders give `B/I≅F×F`, while `A/I≅F` maps diagonally.

### 2. The K3 corners

Quillen’s calculation for finite fields gives

`K_3(F_7) ≅ Z/(7^2-1) ≅ Z/48`.

Homotopy invariance gives `K_3(B)≅K_3(F_7)`. The two evaluations `B -> F_7` at `t=±1` are both retractions of the constant inclusion, hence induce the same identification on `K_3`. Therefore the map

`K_3(B) ⊕ K_3(A/I) -> K_3(B/I) ≅ (Z/48)^2`

has diagonal image. With one conventional sign it is `(u,v) -> (u-v,u-v)`; changing the Mayer–Vietoris sign convention does not change the image.

The cokernel of the diagonal subgroup in `(Z/48)^2` is `Z/48`, for example by `(x,y) -> x-y`.

### 3. Boundary injection

The birelative Mayer–Vietoris exact sequence contains

`K_3(B) ⊕ K_3(A/I) -> K_3(B/I) -> K_2(A,B,I)`.

Exactness therefore identifies the image of the boundary with the preceding cokernel, giving an injection

`Z/48 -> K_2(A,B,I)`.

No computation of the full group `K_2(A,B,I)` is asserted.

### 4. Why the literal Dennis–Stein/dlog route does not certify this class

The elements `t-1` and `t+1` do not lie in `A`, and `1+(t-1)(t+1)=t^2` is not a unit in `F_7[t]`, so the literal pair is not a Dennis–Stein symbol in the required rings. Moreover the exhibited boundary subgroup has order 48, coprime to 7. A characteristic-7 Hochschild/cyclic target is an `F_7`-vector space, so every homomorphism from this 48-torsion subgroup to such a target is zero. The Mayer–Vietoris boundary, not a Dennis/dlog trace, is the appropriate certificate.

## Reproducibility

Run `python3 artifacts/verify.py`. The script checks the finite-field orders, diagonal cokernel, conductor identities, unit obstruction, and the prime-to-7 trace obstruction. The independent audit separately reconstructed the conductor-square and exact-sequence argument.

## Limitations

This result exhibits a `Z/48` subgroup only. It does not compute all of `K_2(A,B,I)` and does not classify other singular curves or other finite fields.

## References

- D. Quillen, *On the cohomology and K-theory of the general linear groups over a finite field*, Ann. of Math. 96 (1972).
- S. Geller and C. Weibel, *K(A,B,I): II*, K-Theory 2 (1989), 753–760, https://doi.org/10.1007/BF00538431.
- B. A. Magurn, *Birelative K2 of groups of square-free order*, Canad. J. Math. 45 (1993), 369–379, https://doi.org/10.4153/CJM-1993-018-x.
- M. Morrow, *K-theory of one-dimensional rings via pro-excision*, arXiv:1211.1533.
