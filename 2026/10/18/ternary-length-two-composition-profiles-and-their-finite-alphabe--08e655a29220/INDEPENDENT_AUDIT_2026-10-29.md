# Independent mathematical audit

## correctness

PASS

All claims were reconstructed from the actual RESULT.md and seven frozen Git blobs (tree SHA independently recomputed). The observed length-one counts and length-two unordered adjacent-pair multiplicities correspond to undirected looped Euler trails. Euler existence holds exactly when positive-degree support is connected and odd-degree count 0 or 2. The identity 2*v_i=d_i+t_i proves one singleton profile for two odd endpoints and exactly |S| for all-even degrees, including loops and n=1 boundary q. For q=3, partition by positive support size 1,2,3; the cross-edge count is (3z^2-2z^3)/(1-z)^3, all-even cross-edge series (z^3+3z^4-2z^6)/(1-z^2)^3, and free loops supply (1-z)^(-3). Their symbolic sum equals the claimed rational series. For fixed q, E unordered edge types give binomial(m+E-1,E-1) vectors, any missing edge is O(m^(E-2)), and nonzero cut characters of the even-parity degree group have at least one (1+z) and one (1-z) factor, leading to O(m^(E-2)) cancellation in each character. The full-support parity-weight sum q+choose(q,2)=E gives E/[2^(q-1)(E-1)!]. An independent checker separately enumerated literal word profiles and looped-multigraph multiplicity vectors at q=2 n<=10, q=3 n<=9, q=4 n<=7, q=5 n<=5, all q=3 graph counts n<=15, and symbolic generating-function/pole identities; the value P3(28)=282873 was recovered. Finite checks corroborate but are not substituted for the all-n Euler-trail/parity proof.

## originality

PASS

Best-of-knowledge original for the exact ternary all-length composition-profile generating function and sharp fixed-q asymptotic constant. The primary same-observable Ye–Elishco paper gives coding constructions, not this quotient enumeration; the complete public binary result explicitly excludes q>=3. Ordered substring spectra and directed cyclic Markov types have different observables and cannot imply the unordered linear Euler-trail count without an additional nontrivial quotient/endpoint analysis. No examined primary theorem, public result, or table implies the full pair of claims. This is not proof of global priority.

## value

PASS

The minimum nontrivial observation length in substring-composition reconstruction is r=2. Counting distinct observation classes equals the exact maximum zero-error code size, a natural invariant with genuine information-theoretic motivation. The first nonbinary q=3 case is classified for every blocklength by an explicit rational generating function; fixed-q asymptotic growth has an exact constant for all finite alphabets. The Euler-trail endpoint contribution makes the enumeration fundamentally different from merely counting nonnegative edge-multiplicity vectors and from the previously classified binary run count. This supplies reusable exact benchmarks and a structural asymptotic result, not a tiny instance, a change of notation, or a table recomputation. No novelty or downstream theorem beyond the explicitly proved finite-alphabet law is claimed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
