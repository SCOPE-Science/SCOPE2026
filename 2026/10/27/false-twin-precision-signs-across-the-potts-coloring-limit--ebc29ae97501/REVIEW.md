# Scientific review — false-twin precision signs

## Correctness: PASS
The conditional coloring factorization is exact because false twins are nonadjacent with the same neighbor multiset. Conditioning on the entire coloring of other vertices produces two iid Bernoulli variables with random success probability. The covariance Schur complement gives exactly \(Q_{uv}=-R/[S(S+2R)]\), and positive definiteness ensures denominators and inversion are valid. At positive weight, two positive-probability neighbor-color assignments with identical fixed-color indicators but different conditional success probabilities prove strictness when the common neighborhood contains at least two vertices; the exceptional cases are affine. At zero weight, a clique neighborhood yields an explicit affine conditional probability. A nonclique admits two proper extensions with identical indicator vector and distinct numbers of neighbor colors when the palette has at least as many colors as vertices. Exact rational enumeration independently verified 588 cases including boundaries. Finite checks do not serve as an infinite proof.

## Originality: PASS, with priority uncertainty
The inspected Potts spatial-mixing papers concern decay, contraction, and influences of conditional distributions, rather than this exact inverse covariance entry and its positive-temperature versus proper-coloring clique criterion. The spectral-independence influence matrix is not the precision matrix of the projected one-color field. The previously available proper-cycle precision calculation is a symmetric special family and does not imply the all-graph false-twin statement or temperature classification. General Schur complements and conditional-iid regression identities are recognized classical ingredients, not original components. No direct equivalent or broader theorem was identified in the searches and source passages read; earlier implicit statistical-mechanics treatments remain a material priority risk.

## Value: PASS
The result connects a natural graph neighborhood invariant (clique versus nonclique) to an exact zero pattern of an observable precision matrix. In particular a shared clique of size at least two causes a zero at the proper-coloring limit and a strictly negative entry at every nonunit positive temperature; this is a nontrivial structural boundary for projecting a categorical Gibbs field onto one-color indicators. The complete graph-independent sign bound and sharp temperature classification go beyond a numerical example or a direct parameter substitution.

## Literature and limits
- Bencs–Berrekkal–Regts (2023), arXiv:2310.04338: antiferromagnetic Potts mixing on trees, not this precise twin-precision sign theorem in inspected sections.
- Chen–Liu–Mani–Moitra (2023), arXiv:2304.01954: spatial mixing and algorithmic colorings, not a full inverse covariance identity for a fixed color.
- Chen–Galanis–Štefankovič–Vigoda (2020), arXiv:2007.08058: spectral independence and mixing, with a different influence operator.
- General Schur complements are standard; the historical existence of a specialized equivalent remains unresolved. The zero-temperature iff criterion is restricted to palettes of size at least the vertex count.

Self-review: passed. Independent audit: not yet performed.
