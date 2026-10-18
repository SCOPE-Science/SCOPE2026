# Independent mathematical audit

## correctness

PASS

Binary first-symbol+XOR-derivative representation is bijective; one tandem repetition duplicates a bit and inserts a 0 into the derivative. For a fixed first bit and derivative weight w, length-five derivative corresponds to zero-bin composition b of 5−w into w+1 bins; two-repeat descendant intersections iff Σ max(b,b′)≤7−w, equivalently ||b−b′||₁≤4. Distinct two-repeat balls iff distance ≥6. Weight-layer maxima reconstructed as (1,2,3,1,1,1); equality counts (1,3,1,10,5,1). Sum=9 and product=150 for each first-bit sector; two disjoint first-bit sectors give 18 optimum and 150²=22,500 labeled maxima. Exactly-two disjointness implies exactly-one correction (and zero trivially); independent direct descendant construction and finite exhaustive layer clique checks reproduce each optimum/equality count and verify 142/256 length-eight coverage. Finite result, no assertion for n>6.

## originality

PASS

Dolecek–Anantharam studies precisely repetition errors and maps them to inserted derivative zeros, so derivative reduction is not novel. Their full-text 2010 work gives explicit constructions/prefixing and asymptotic bounds, not the six-layer equality census at n=6, t=2. Jain–Farnoud–Schwartz–Bruck provides more general fixed-length tandem duplication code machinery, with conditional ℓ1 viewpoint, but no specific 18/22500 layer-optimal classification found. The published Resultary palindromic length-two duplication code censuses use a different duplication operator, not length-one repetition. No claim that reduction itself is new.

## value

PASS

The complete equality classification of a natural small binary multiple-repeat channel determines all 22,500 maxima and their uncorrected output-space density rather than a mere lower-bound instance. The six-layer decomposition gives an exact reusable benchmark for constrained ℓ1/zero-insertion codes; the finite result is self-contained and can inform validation of bounded-duplication constructions.

The dated certificate retains the supplied scientific assessment, sources and limitations.
