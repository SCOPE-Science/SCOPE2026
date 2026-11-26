# Independent mathematical audit

## correctness

PASS

Reconstructed both the local normal form and the composition argument. For an ordinary RB map, downward induction in the square identities shows that column i is supported in indices >=i: R(e_i^2) has support in >=i+1, and the first nonzero coefficient below the annihilator in R(e_i) would contribute its nonzero square one position later. A vanishing diagonal forces the entire column into the annihilator by independence of e_1^2 through e_{n-1}^2. A nonzero diagonal at i forces d_{i+1}=d_i/2 by comparing the leading coefficient (using c_n as the last diagonal); the mixed square identities then eliminate any off-diagonal entry below the annihilator. Each long-range coefficient from a nonzero-diagonal source would force d_j=d_i/2 at j>i+1, contradicting the chain ratios, so the threshold k must exceed r. Conversely an ordinary map for k>r has free last-row entries c_1 through c_k, zero c_{k+1} through c_{n-1}, and c_n=d_{n-1}/2. Testing a local map on basis vectors and on e_i+e_j forces the common-ratio final interval; locally matching x with an ordinary map at the first nonzero tail coordinate uses its free last-row entry, and if there is none an annihilator-valued map suffices. Composition multiplies the diagonals with threshold equal to the maximum and ratio 2 to the product length, and prescribing the last row in the last factor while all earlier last rows are e_n^T keeps it free. The infinitely many ratios 2^ell are Zariski dense: a Laurent polynomial vanishing on all such ratios for every nonzero scale must vanish coefficient by coefficient. Rescaling gives the standard rational-normal-curve parametrization. Monomial straightening by the stated minors preserves degree and index sum and decreases the sum of squared indices, producing the unique balanced monomial; hence the listed minors generate the toric ideal. At the first zero of a component tail the successive square minors force all but the last diagonal to vanish. This gives the claimed pairwise intersection and noncontainment, including the case of one component and the two-coordinate cone (a plane). Closure is stable under multiplication by separate continuity of multiplication and density. An independent exact bounded replay, `python3 /workspace/reviews/replay_finite.py 3`, checked 2,403 local witnesses via the original bilinear identities on six algebras in dimensions 3–5; it supplements rather than proves the theorem. The frozen verification program was inspected, not executed.

## originality

PASS

The support-and-ratio classification of individual local maps and the use of toric methods for cyclic matrix closures are known. The supported distinct claim is the complete algebraic multiplicative envelope of the whole local family, including its exact finite-product description, the dimensions and every component intersection. No identified prior statement establishes that combination; in particular the final-row freedom and multiple threshold supports are not hypotheses or conclusions of the cyclic theorem.

## value

PASS

The multiplier question tests how far a nonlinear local-operator class is from multiplicative closure. The result gives both all attainable products and all added algebraic boundary points, and explains why the obstruction index controls reducibility while the free row and the shared intersection persist. The shape and dimension jump provide information beyond the original individual-map classification or a nonclosure witness.

The dated certificate retains the supplied scientific assessment, sources and limitations.
