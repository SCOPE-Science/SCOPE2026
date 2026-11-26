# Independent mathematical audit

## correctness

PASS

Each admissible four-word is a single arc, and cyclic tours using every arc once give exactly the claimed words modulo rotation. For the spectral calculation A=JD−R; R permutes triples in three-cycles and (xI+R)⁻¹=(x²I−xR+R²)/(x³+1). The determinant lemma gives the stated rank reduction. In the reduced pair space, DJg=r_c−g(c,b), DRJg=c_b−g(c,b), and DR²Jg=(n−2)g(b,c). Thus the row/column-zero part splits under transpose; the symmetric and skew parts have the stated dimensions from the complete graph unsigned and signed incidence ranks n and n−1, respectively. The complementary row-plus-column space splits into constants and two copies of mean-zero vectors (the row/column map on those copies has determinant n(n−2)). The constant block gives (x−d)(x²−x+1). Substituting the two mean-zero coefficient vectors gives the 2×2 matrix in the result, with determinant (x³+1)(x³+x²+dx+d²). Together these give exponent N/3−(n−1)² and account for every dimension; the rational-function calculation gives a polynomial identity including at the exceptional roots. At x=d the remaining factors are positive (d≥2), and relabeling makes every directed tree cofactor equal. The derivative coefficient is their sum. Anchoring the cyclic tour at one fixed arc removes rotational multiplicity; BEST then supplies the per-root tree cofactor times ((n−4)!)^N, without any reflection or relabeling division. Substitution at n=5 agrees with the shorthand value; at n=6 it gives the arborescence factors 2^51·3^43·5^8·7^16, and the factorial factor adds 2^120. The supplied script was inspected, not executed: its finite exact cofactor tests and sample determinant evaluations corroborate, but do not prove, the all-n spectrum.

## originality

PASS

The distinct claim is the explicit k=4 characteristic polynomial and the resulting evaluated product for labeled alphabets of arbitrary n≥5. The same underlying digraph, the generic tree/BEST expression, existence, and the shorthand value at n=5 are already known and are not counted as new. No inspected result evaluates this spectrum or implies the product without a new spectral calculation.

## value

PASS

The spectrum is computed for a canonical transition graph in the next window length beyond the known evaluated k=2,3 cases. It replaces graph-size determinants by bounded-degree factors with explicit multiplicities, resolving the natural universal-cycle count and supplying spectral information beyond that count.

The dated certificate retains the supplied scientific assessment, sources and limitations.
