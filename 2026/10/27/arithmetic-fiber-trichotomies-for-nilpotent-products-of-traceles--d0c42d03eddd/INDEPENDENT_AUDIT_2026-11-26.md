# Independent mathematical audit

## correctness

PASS

By Cayley–Hamilton in both characteristics, AB is nilpotent iff tr(AB)=0 and det(A)det(B)=0; no tacit trace constraint on AB is needed. Each nonzero nilpotent B has image=kernel a line L, and each of the q+1 lines supports q−1 such B. Thus the cone including 0 has q² elements. For invertible A, write B=u⊗ℓ with ker ℓ=L=span(u) for each nonzero candidate. Then tr(AB)=ℓ(Au)=0 precisely when A leaves L invariant. The fiber size is 1+(q−1) times the number of invariant lines (where the 1 counts B=0), i.e. 2q−1/1 for odd split/nonsplit and q²/q for even scalar/nonscalar. In characteristic two the unique square root of −det(A) gives the repeated eigenvalue, with one eigenline for a nonscalar; in odd characteristic, at fixed nonzero s=−det A the equation a²+bc=s gives q(q−1) solutions with b≠0, plus 2q or 0 with b=0 for square or nonsquare s. Multiplying by (q−1)/2 proves both odd multiplicities without centralizer tables. A=0 has q³ choices; for nonzero nilpotent A=E₁₂ the nontrivial linear trace condition is B₂₁=0, giving q² and annihilator size q. The two trace-zero, at-least-one-nilpotent incidences each have size H=q³+(q²−1)q² and overlap I=q²+(q²−1)q. Then 2H−I gives the common polynomial. Summing annihilator sizes over zero, nonzero nilpotent and invertible A gives 3q³−q²−q; subtraction factors as stated and any nonzero nilpotent 2×2 matrix has square zero. An independent exact enumeration in GF(8), using (AB)²=0 on 262144 ordered pairs, yielded 8520 nilpotent and 1464 zero products, with fiber multiplicities 441,70,1 at sizes 8,64,512. This is supplementary; the proof is for every prime power. The supplied checker was inspected, not executed.

## originality

PASS

Credit the trace-conditioned pair census and its complete characteristic-dependent fibers, not the nilpotent cone size, orbit types, determinant criterion, or whole-ring probabilities. The strongest inspected sources cover uniform whole-ring sampling or pairs of individually nilpotent factors. The latter overlaps an exact intersection subcount but not the mixed-factor incidence and complete tables.

## value

PASS

The trace-zero slice is the canonical trace kernel and, in dimension two, is exactly where nilpotent factors coincide with the singular ones. It is not an arbitrarily chosen matrix subset. The exact conditional incidence reveals strong arithmetic heterogeneity, including forced zero as the only right factor for nonsplit invertible A in odd characteristic, while the aggregate nilpotent probability is uniform as a polynomial across characteristics. Separating actually zero products from nonzero nilpotent outcomes makes the census usable as a finite-field calibration and not a recomputation of whole-ring probabilities.

The dated certificate retains the supplied scientific assessment, sources and limitations.
