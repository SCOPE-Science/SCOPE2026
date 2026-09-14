# Wagner M8 edge ideal: Waldschmidt constant 8/5, initial degrees, and I^(4) subset I^3

## Context

Let G be the Wagner graph M8, the 8-vertex Mobius ladder: vertices 0..7 with cycle edges (i,i+1 mod 8) plus antipodal edges (i,i+4). It is cubic with 12 edges, triangle-free, nonplanar, and non-bipartite. Let k be any field, R=k[x_0,...,x_7], and I=I(G) its edge ideal, with symbolic powers defined by minimal primes (minimal vertex covers). The target asked for the exact Waldschmidt constant, exact resurgence and asymptotic resurgence, and the containment decision I^(4) vs I^3.

## Definitions

Minimal vertex covers C_1..C_8 give the cover matrix C. A monomial x^a lies in I^(m) iff C a >= m coordinate-wise. It lies in I^r iff its exponent dominates the vertex-load of some multiset of r edges. The initial degree alpha_m is the minimum degree of a monomial in I^(m). The Waldschmidt constant is hat(I)=lim alpha_m/m = inf alpha_m/m. Resurgence rho(I)=sup{m/r : I^(m) not subset I^r}.

## Result

For the Wagner M8 edge ideal I:
- Waldschmidt constant hat(I) = 8/5 exactly.
- Initial degrees alpha(I^(m)) = 2,4,5,7,8 for m=1,2,3,4,5, each sharp.
- Containment I^(4) subset I^3 HOLDS, with a complete finite certificate.
- Companion containments (2,2),(3,2),(4,2),(4,3),(5,2),(5,3),(5,4) hold; (3,3) and (4,4) fail via explicit witnesses.
- Resurgence satisfies rho(I) >= 5/4. Equality rho = rho_a = 5/4 is a conjecture with computational support, not a theorem.

## Proof and evidence

Cover structure: brute-force enumeration over all 2^8 subsets shows 8 maximal independent sets, hence 8 minimal vertex covers, all of size 5, with every vertex in exactly 5 covers. Thus each column sum of C is 5.

Waldschmidt: summing the 8 cover inequalities gives 5 deg(a) >= 8m for any x^a in I^(m), so alpha_m >= 8m/5 and hat >= 8/5. Diagonal monomials (k,...,k) have every cover sum 5k and degree 8k, so lie in I^(5k) with alpha_{5k} <= 8k, forcing hat <= 8/5. Hence hat = 8/5.

Initial degrees: lower bounds alpha_m >= ceil(8m/5) follow from the averaging inequality. Sharp witnesses: m=1: any edge (deg 2); m=2: square of an edge (deg 4); m=3: [0,0,0,1,1,1,1,1] (deg 5, all cover sums in {3,4}); m=4: [0,0,0,1,1,1,2,2] (deg 7, all cover sums >= 4); m=5: (1,...,1) (deg 8, all cover sums 5). Exhaustive composition search confirms no smaller degrees occur.

Containment I^(4) subset I^3: box-reduction lemma: minimal monomial generators of I^(m) have all entries <= m, since if a_v >= m+1 then a-e_v still satisfies every cover inequality containing v while covers avoiding v are untouched. Hence only {0..4}^8 (390625 vectors) need be checked. Exact enumeration finds 358134 vectors in I^(4); every one dominates at least one of the 316 unique 3-edge load patterns, so all lie in I^3. Zero counterexamples.

Companions: same box method gives the stated holds; failures use the degree witnesses above (deg 5 < 6 for (3,3); deg 7 < 8 for (4,4)), since every I^r monomial generator has degree exactly 2r.

Resurgence lower bound: diagonal monomials (k,...,k) lie in I^(5k) with degree 8k, hence not in I^{4k+1} (minimum degree 8k+2), realizing ratios 5k/(4k+1) -> 5/4. Random search found no violation of rho <= 5/4, supporting the conjecture.

## Limitations

Exact equality rho = rho_a = 5/4 is NOT proved; the upper bound needs containments for all pairs with 4m > 5r and its descent induction was not completed. The I^(4) subset I^3 certificate is computational (exhaustive but finite and rerunnable) rather than a short human-readable Rees argument. All statements hold over any field with symbolic powers defined by minimal primes.

## Reproducibility

Pure numpy plus itertools scripts rerun bit-identically: output/artifacts/compute.py (cover matrix, 358134 count), output/artifacts/witness.py (domination vs 316 loads, zero counterexamples), output/artifacts/table.py (companion pairs), output/artifacts/alpha.py (initial degrees). Independent audit recomputation confirmed all counts and witnesses.

## References

- Nguyen-Pham-Vu, Regularity of powers and symbolic powers of edge ideals of cubic circulant graphs, arXiv:2409.20161.
- Gu-Ha-O'Rourke-Skelton, Symbolic powers of edge ideals of graphs, arXiv:1805.03428.
- Villarreal, A duality theorem for the ic-resurgence of edge ideals, arXiv:2203.01268.
- Bocci et al., The Waldschmidt constant for squarefree monomial ideals, J. Algebraic Combin. 44 (2016).
