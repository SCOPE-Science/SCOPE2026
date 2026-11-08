# Independent mathematical audit

## correctness

PASS

For m>=1 the outward-star HK presentation has canonical normal forms u_U or u_P c u_Q with P cap Q empty, and exactly 2^(m+1) idempotents u_U and c u_U. Images of generators must be idempotents; source leaves commute and center-leaf arrow relations impose coordinatewise inclusion constraints. For a fixed set I of a leaves whose image contains target c, at one target leaf coordinate the choices for leaf images are K=2^a+2^(m−a)−1. A center-containing f(c) allows 2^m K^m choices; center-free f(c) gives (K+2^(m−a))^m. Summing binom(m,a) gives exact E_m; direct independently implemented relation enumeration for m=1,2,3 yields 15,339,22233 and formula produces 4780047,4058199945 at m=4,5. Three disjoint a=0,b0=0; a=0,b0=1; a=m,b0=1 families each contain 2^(m(m+1)); all other strata have aggregate O(2^(m(m+1))m2^(−m)) by endpoint/tail bounds, so E_m~3·2^(m(m+1)) and each family probability tends 1/3. Finite enumeration is not used as proof for growing m.

## originality

PASS

Andrenšek 2026 establishes a general Boolean classification of endomorphisms of HK monoids, which implicitly decides each fixed oriented-star case. The present uniform evaluated m-binomial count and asymptotic three equally likely image-family concentration are not stated in inspected general-classification theorems. Aragona–D’Andrea normal forms are classical input and not original. A general fixed-size decision theorem is not automatically a closed m-variable asymptotic census.

## value

PASS

The source objects form a canonical infinite family of finitely presented monoids. Exact counts, an unexpectedly three-modal dominating partition and limiting probabilities supply nontrivial global structure beyond brute-force enumeration; highly useful if studying typical HK self-maps or growth of endomorphism monoids.

The dated certificate retains the supplied scientific assessment, sources and limitations.
