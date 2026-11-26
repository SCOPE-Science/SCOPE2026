# Independent mathematical audit

## correctness

PASS

The independent-digit product converges locally uniformly, including in complex neighborhoods; its tail is nonzero near any fixed real frequency once the finitely many vanishing factors are removed, since the deviations from 1 are uniformly summable. The real mask zeros require two opposite nontrivial cube roots. At (2u/3,2v/3), factor j vanishes exactly when 2^(j-1) divides both u and v, because division by 2 modulo 3 interchanges the two residue orientations. The r vanishing factors have linear terms proportional to L and its conjugate in alternation, with L(h)=exp(-2 pi i/3)h1+exp(2 pi i/3)h2 for residue (1,2) at the first level. Its real determinant is -sqrt(3)/2, and |L(h)| is at least |h|/sqrt(2). The leading product has exact degree r and stays nonzero on small circles relative to the Taylor remainder; degree additivity gives index -1 for odd r in that residue, +1 in the other, and 0 for even r. The examples u=-v=2^(r-1) realize every r. The order-at-least-r locus is 2^(r-1)Z, giving exact disk count subtraction. Two cosets of 2 Z^2 have combined density 1/2; summing the rescaled lattice estimate gives weighted density 2/3 (times disk area) and a summed O(R+1) error, as only O(log(R+2)) scales can contribute. Summing exact-order differences over even orders gives 1/5 of all zeros; swapping the coordinates pairs the two odd index signs in each disk. The proof replays from RESULT.md sections 1–3. The packaged checker in check_sierpinski_vortices.py was inspected, not run; its finite disk counts and sampled truncated-product windings are supplementary, not proof of any unrestricted claim.

## originality

PASS

The exact support is already obtained by specializing Chen–Ai, and the known infinite-product representation is not a novelty. The supported distinct content is the exact local Taylor and phase classification and its rescaling and census consequences. The closest indexed result treats a different ternary carpet; no inspected result covers the dyadic local classification. This is a best-of-knowledge comparison, not a priority certificate.

## value

PASS

The canonical gasket's zero locations already encode Fourier orthogonality, but do not distinguish orders of cancellation or local phase winding. A complete local classification is independently useful when a zero is perturbed or when comparing phase and amplitude: arbitrarily high order coexists with uniformly bounded index, and even-order zeros have no winding. The exact lattice census gives the prevalence of each behavior over the whole frequency plane and is not a finite sample or a claim about spectrality.

The dated certificate retains the supplied scientific assessment, sources and limitations.
