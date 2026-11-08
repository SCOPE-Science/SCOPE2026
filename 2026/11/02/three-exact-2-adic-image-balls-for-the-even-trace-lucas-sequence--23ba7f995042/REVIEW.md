# Independent mathematical audit

## correctness

PASS

For U_{n+2}=P U_{n+1}−U_n, P≠0, v2(P)=h≥2, the standard companion recurrence gives v2(V_{2j})=1, v2(V_{2j+1})=h, and v2(U_{2j})=h+v2(j) for j>0. Same-parity Lucas difference identity then proves index isometries of even, 1 mod4, and 3 mod4 subsequences at scales 2^h, 2^{2h}, 2^{2h}. Each induces a permutation on every Z/2^N, hence its completed image is one whole 2-adic ball; disjointness at precision≥2 produces exact count 2^max(0,N−h)+min(2,2^{N−1})2^max(0,N−2h) and Haar proportion 2^{−h}+2^{1−2h}. The actual verifier script checks entire finite recurrence orbits over 12 signed P parameters and N≤11, but the stated identities prove all P,N.

## originality

PASS

Related de Clercq et al. 2020 Theorem 5 classifies complete residue permutations when P≡2 mod4, a different regime. By U_{2a}(P)=P U_a(P²−2), their theorem already covers the even-index ball; this part is explicitly not new. No inspected theorem implies the two odd-index balls or exact union for P≡0 mod4. Other Resultary Lucas period equality for q=−1 uses the companion valuations but not exact residue closure. Older recurrence image literature could contain an equivalent formulation.

## value

PASS

Naturally completes the complementary trace class excluded by the known dyadic permutation theorem: full image topology, canonical isometric parametrizations, exact residue counts at every modulus and Haar density; not an arbitrary fixed-modulus example.

The dated certificate retains the supplied scientific assessment, sources and limitations.
