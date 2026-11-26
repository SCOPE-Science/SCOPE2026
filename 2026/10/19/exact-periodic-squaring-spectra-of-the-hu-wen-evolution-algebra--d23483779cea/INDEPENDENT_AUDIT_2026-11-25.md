# Independent mathematical audit

## correctness

PASS

Original basis multiplication gives E²=span(e1+e3,e2+e3), with products 0,u,−u+lambda v as stated. All periodic points lie there. Writing c=lambda b, the c=0 fiber maps to the origin. On c≠0 use z=a/c: the map is the direct product (c,z)→(c²,(2/lambda)z−1/lambda²). This independently verifies both iterate formulas. At lambda≠2 the affine factor has one fixed center and acts about it by multiplication by t; its m-th iterate fixes q points if t^m=1 and one otherwise. At lambda=2 it is translation by −1/4, whose m-th iterate fixes q points exactly when p divides m. The scalar power factor fixes gcd(2^m−1,q−1) nonzero values. Squaring is a permutation exactly on the odd-order subgroup among the periodic c values, and the affine factor is a permutation, giving 1+qh. The two factors' least periods combine by lcm: at lambda=2 any point over c≠0 has period lcm(k,p), with k the c-period, so the k-step fiber return may be the identity if p divides k. Möbius inversion and the cycle factors yield the stated zeta, and the small-field examples follow. RESULT.md line 73 means the exceptional (second), not the first, displayed count. Independent original-table enumeration matched 270 fixed-iterate comparisons and 20 periodic-locus counts over F3, F5, F7 and F9 with the irreducible relation theta²=2 over F3. The checks are finite; the product argument gives the unrestricted result.

## originality

PASS

The algebra, its stable square and idempotents are already known, and scalar power-map periodicity is standard. The supported contribution is the complete, field- and parameter-dependent nonlinear iterate spectrum, obtained by separating the base power map from affine fiber resonance. Neither the power-map method nor the idempotent-free exception alone is new.

## value

PASS

Hu–Wen's idempotent-free, non-solvable example naturally raises the question of what survives under repeated squaring over finite fields. The explicit exact cycle multiplicities distinguish base arithmetic from multiplicative or additive fiber periods, and show that identical total periodic-locus sizes can hide very different spectra. This resolves a motivated entire-family invariant rather than merely exhibiting the simple exceptional p-cycle or applying a scalar gcd formula to a single example.

The dated certificate retains the supplied scientific assessment, sources and limitations.
