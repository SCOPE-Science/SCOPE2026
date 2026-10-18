# Independent mathematical audit

## correctness

PASS

Direct induction yields F_L^n x_i=x_{i+rn}+n (mod q). Translation by rn on the L-ring has d=gcd(L,rn) cycles of length L/d; fixed points require n L/d=0 mod q and allow q independent choices per spatial cycle, giving exactly q^d or zero. A factor from a finite permutation to cyclic +1 mod q exists iff every orbit length is divisible by q: necessity from one orbit, sufficiency by labeling each orbit in order, giving surjectivity. All orbit lengths divisible by q iff no F^n fixed point for q not dividing n. For any p|q with a=v_p(q), b=v_p(L), c=v_p(|r|), compute v_p(n L/gcd(L,rn))=max(v_p(n),b-c). If b-c<a for every p, a n with q not dividing n cannot satisfy all divisibilities; if some b-c>=a, choose n=q/p to produce a fixed point with q not dividing n. This establishes the prime-adic iff including composite q and L=1. On the bi-infinite lattice construct a fixed configuration with x_{i+r}=x_i-1, so no equivariant scalar clock; constant configurations still cycle with exact period q. If gcd(L,rq)=1, h=L^-1 sum_i x_i is an equivariant surjection mod q; any other h obeys h(F^q x)=h(x), and F^q is a generating spatial rotation. Transitivity forces the essential support of a nonconstant h to be all L sites. Independently enumerated q=2..4, L=1..4 and r=+/-1,+/-2, checking 274 exact fixed-point, finite factor and global-sum assertions. Finite cases support but do not prove universal result; the symbolic cycle/valuation argument does.

## originality

PASS

Gwóźdź derives necessary period divisibility for infinite spatial clock factors and constant-cycle obstructions, but no iff criterion for finite traveling affine scalar clocks or full-support lower bound. Hudcová--Krásenský’s affine cellular-automaton simulation theorem concerns intrinsic simulation over finite fields and a different morphism; it does not imply the valuation criterion for composite q. Elementary orbit-counting is acknowledged as old, and new finite-vs-infinite factor alias plus sharp nonlocal scalar-observer support are distinguished from the stronger spatial-clock factor question. Priority in older permutation literature remains residual.

## value

PASS

The dynamics of a canonical reversible affine automaton naturally motivates whether scalar cyclic observations persist under finite periodic approximation. The exact prime-valuation boundary shows many finite rings admit a clock even though the bi-infinite system admits none, while the sharp all-site observation lower bound quantifies precisely why such finite clocks cannot be uniform local factors. These are exact classification and nonlocality facts of natural dynamical objects beyond a single small count. Elementary permutation techniques are credited, not themselves offered as mathematical value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
