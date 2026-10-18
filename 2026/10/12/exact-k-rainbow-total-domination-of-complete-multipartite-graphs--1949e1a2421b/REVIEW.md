# Independent mathematical audit

## correctness

PASS

For connected complete multipartite graph with r>=2 positive parts, N total, s=min n_i and k>=2, the formula gamma_krt=min{N,2k,k if s<=floor(k/2) else s+floor(k/2)+1} has explicit constructions. Lower bound: W<N forces an empty vertex; W<2k forces a fully labeled part A (otherwise each color must occur in two other parts relative to some empty). With a=|A| and p singleton vertices, support requirements imply W>=k+p and W>=2a-p+1. For a>floor(k/2) their integer minimax gives a+floor(k/2)+1, while the small-part case needs at least k incidences. This covers all boundary cases, including k odd. Fresh independent definition-level exhaustive checks over several profiles through order 6 for k=2,3 agree; source supplied larger checks were not accepted as proof.

## originality

PASS

The 2021 Ojakian–Škrekovski–Tepeh full primary paper Proposition 3 establishes the complete bipartite r=2 case and matches its specialization, but a two-part theorem does not cover r>=3. The 2026 same-invariant primary paper proves complexity/general bounds without an arbitrary multipartite exact theorem in inspected text. A closely named 2-rainbow domination result in Resultary lacks the singleton-support condition. Generalized-prism total domination was searched as an equivalent formulation. No covering higher-part theorem identified; residual indexing risk remains.

## value

PASS

An exact formula for a recognized computationally difficult domination invariant over the entire natural class of complete multipartite graphs, all k>=2, strictly extends the established biclique slice. The fact that only N and minimum part size control the optimum follows from a nontrivial singleton-support structural argument and is useful for generalized-prism total domination; this is more than an arbitrary finite census.

The dated certificate retains the supplied scientific assessment, sources and limitations.
