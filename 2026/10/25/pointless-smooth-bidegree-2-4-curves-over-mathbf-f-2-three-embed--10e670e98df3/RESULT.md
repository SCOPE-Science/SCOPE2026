# Pointless smooth bidegree-\((2,4)\) curves over \(\mathbf F_2\): three embedded orbits

## Finding

Among the 64 fixed-coordinate bidegree-\((2,4)\) equations on \(\mathbf P^1_{\mathbf F_2}\times\mathbf P^1_{\mathbf F_2}\) with no \(\mathbf F_2\)-rational points, exactly 33 define geometrically smooth curves of genus three. Under factorwise \(\mathrm{PGL}_2(\mathbf F_2)\times\mathrm{PGL}_2(\mathbf F_2)\), these 33 equations form exactly three orbits of sizes 9, 18, and 6. The two first orbits have Jacobian \(2\)-rank 3, the third has \(2\)-rank 1. This counts embedded equations, not abstract curve isomorphism classes.

Choose coordinates \(([s:t],[u:v])\), and express each bihomogeneous form as
\[
F(s,t;u,v)=A(u,v)t^2+B(u,v)st+C(u,v)s^2,
\]
where \(A,B,C\) are binary forms of degree four. Let \(x=u/v\) and denote the dehomogenizations by \(a,b,c\). The complete set of smooth pointless equations is represented by the following three orbits, with their indicated representatives:

| Coefficient triple \((a,b,c)\), binary bit encoding | Orbit size | Stabilizer order | Jacobian \(2\)-rank |
| --- | ---: | ---: | ---: |
| \((21,19,19)\), code 20085 | 9 | 4 | 3 |
| \((25,19,19)\), code 20089 | 18 | 2 | 3 |
| \((25,21,19)\), code 20153 | 6 | 6 | 1 |

Here an integer \(m\in\{0,\ldots,31\}\) encodes \(\sum_{i=0}^4 ((m\!\gg\! i)\mathbin{\&}1)x^i\). Equivalently, the only quartics used are
\[
q_{19}=x^4+x+1,\quad q_{21}=x^4+x^2+1,\quad
q_{25}=x^4+x^3+1,\quad q_{31}=x^4+x^3+x^2+x+1.
\]
All coefficients and counts are over \(\mathbf F_2\); the scalar normalization is unique because its unit group is trivial.

## Assumptions and scope

A curve is *pointless* if it has no \(\mathbf F_2\)-point, and *smooth* means geometrically nonsingular. All equations have bidegree exactly \((2,4)\) as divisors. The equivalence group consists of independent changes of coordinates on the two factors, of total order \(6\cdot6=36\); swapping the factors does not preserve the chosen bidegree. Every smooth divisor in this ample class is geometrically integral and has genus \((2-1)(4-1)=3\) by adjunction. Projection to the second factor has degree two and is separable for the smooth curves considered.

## Proof

**Pointlessness reduces to 64 forms.** On each of the three rational base points of the second \(\mathbf P^1\), the fiber is a homogeneous binary quadratic. Over \(\mathbf F_2\), the unique binary quadratic without a rational zero is \(s^2+st+t^2\). Consequently all three quartics \(a,b,c\) must take value one at each of \(x=0,1,\infty\). Among the 32 binary quartics these are exactly \(q_{19},q_{21},q_{25},q_{31}\), leaving \(4^3=64\) possibilities. The converse is immediate from the three fibers.

**Geometric smoothness test.** Because every such \(b\) has leading coefficient one, there are no singularities over \(x=\infty\). At any finite point with \(b(x)\ne0\), at least one partial derivative in \(s,t\) is nonzero. At a geometric root \(\xi\) of \(b\), the partials in \(s,t\) vanish simultaneously and the fiber has the single geometric point \([s:t]\) with \(s^2=c(\xi)\), \(t^2=a(\xi)\). Squaring the remaining derivative shows that its vanishing is equivalent to \(\Delta(\xi)=0\), where
\[
\Delta(x)=\bigl(a'(x)c(x)+a(x)c'(x)\bigr)^2+b'(x)^2a(x)c(x).
\]
Thus geometric smoothness holds precisely when \(\gcd(b,\Delta)=1\) in \(\mathbf F_2[x]\). This also excludes a geometrically entire degenerate fiber: if \(a=b=c=0\), then \(\Delta=0\). Evaluating this exact polynomial criterion for the 16 coefficient pairs \((a,c)\) for each \(b\) gives smooth counts \(9,6,9,9\) for \(b=q_{19},q_{21},q_{25},q_{31}\), respectively. The four explicit Boolean matrices are in `pointless_64_out.json` and a self-contained checker in `pointless_64.py`; their sum is 33. An independent field-extension Jacobian test in `field_verify.py` confirms these values as part of an exhaustive smooth-form enumeration.

**Orbit calculation.** Every factor has six projective invertible coordinate matrices. `pointless_orbits.py` substitutes all 36 matrix pairs into each of the 33 coefficient triples and produces three disjoint orbits of sizes \(9,18,6\). The separate `independent_orbit_check.py` recomputes all substitutions by evaluating bihomogeneous forms at 15 points over \(\mathbf F_8\) and independently matches their signatures to the 33 coefficient triples. It gives the same three orbits, and their sizes sum to 33. Orbit–stabilizer yields stabilizer sizes \(4,2,6\). These are embedded automorphism stabilizers, not necessarily full abstract automorphism groups.

**Jacobians.** For a smooth separable characteristic-two hyperelliptic curve, the Deuring–Shafarevich formula says that the Jacobian \(2\)-rank is one less than the number of distinct geometric branch points of the degree-two projection. Here these branch points are exactly the distinct roots of the degree-four binary coefficient \(B\). The quartic \(q_{21}=(x^2+x+1)^2\) has two distinct geometric roots and yields \(2\)-rank one. Each of \(q_{19},q_{25},q_{31}\) is irreducible of degree four and yields \(2\)-rank three. These ranks agree with the independently coded extension-field root census `field_verify.py`.

## Verification

Run with Python 3 from the directory containing the included files:

```sh
python3 pointless_64.py
python3 count_genus3.py
python3 field_verify.py
python3 pointless_orbits.py
python3 independent_orbit_check.py
```

Reference JSON outputs with corresponding stems are included, together with `pointless_all_33.json`, an independently replayable list of all 33 integer-encoded forms. The two all-form checks enumerate \(31\cdot32^2=31,744\) triples with nonzero \(b\), and the 64-case test needs only the four specified quartics. All finite-field operations and group substitutions are exact and require no third-party library.

## Relationship to prior work

Pogildiakov (2017) studies the existence threshold for pointless hyperelliptic curves, including even characteristic; its genus and field variation does not give the exact fixed-embedding census here. Howe–Lauter–Top established existence and constraints for pointless genus-three curves; that existence theorem alone does not count equations of a specified bidegree. Nart–Sadornil (2004) supplies a much broader **abstract isomorphism classification** of genus-three hyperelliptic curves in characteristic two, organized by Artin–Schreier ramification types. This result does **not** reclaim that classification: its new target is an exact count and orbit classification of equations in a fixed split-quadric linear system under its **factorwise** projective group. An indirect derivation from the older abstract classification is possible in principle and remains a publication-priority risk.

## Limitations

This is a complete finite computation for a specific embedded linear system, not a classification of all genus-three curves, all possible genus-three hyperelliptic embeddings, or all abstract isomorphism classes. It makes no claim of independent review. The projective-group classification is not equivalent to the complete abstract \(\mathbf F_2\)-isomorphism classification. The main novelty risk is unindexed embedded-model tables or a previously worked-out consequence of the Nart–Sadornil normal forms. The correctness proof is computer-assisted, using explicit short exhaustive checkers.

## References

- I. Pogildiakov, *On the linear bounds on genera of pointless hyperelliptic curves* (first public 2017-03-24), arXiv:1703.08312, https://arxiv.org/abs/1703.08312.
- E. Nart and D. Sadornil, *Hyperelliptic curves of genus three over finite fields of even characteristic*, Finite Fields Appl. 10 (2004), 198–220, doi:10.1016/j.ffa.2003.08.002.
- E. W. Howe, K. E. Lauter, and J. Top, *Pointless curves of genus three and four*, arXiv:math/0403178, https://arxiv.org/abs/math/0403178.
