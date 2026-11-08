# Independent mathematical audit

## correctness

PASS

For length four DNA words, Watson–Crick reverse complement is an involution with 16 fixed words and 120 two-word orbits. Every orbit is internally deletion-shadow compatible. The 136-vertex weighted compatibility graph has disjoint-shadow edges, vertex weights 1 or 2; its cliques correspond bijectively to all strand-closed one-deletion codes. The weighted independent-coloring prefix bound used for branch-and-bound is valid for every residual clique; the recursive traversal checks all include/exclude branches, with pruning by a rigorous upper bound. An independent implementation from all 256 DNA words reproduced weight maximum 24 and exactly 160 optimizers; removing fixed-word vertices gave maximum 22 and 44 optimizers. It also reproduced exact fixed-word distribution (2:4,4:44,6:76,8:36) and the published 136 orbit vertex counts. The stated 28 symmetry orbits follow from action of eight complement-preserving relabelings; this orbit count was examined against source algorithm, though an independent second census of the symmetry classes was not separately run. No larger-blocklength conclusion is inferred.

## originality

PASS

Known single-deletion shadow-disjointness and DNA reverse-complement Hamming separation are different from the simultaneous closure-plus-deletion restriction. Other primary literature studies binary deletion codes, different q/n deletion spectra, and quaternary single-indel constructions without this complete nonlinear fixed-length RC-closed code census. Resultary yielded ternary/quinary length-four deletion optima but no 24/160/22/44 strand-closed quadrinary match. A hidden small-code table or equivalent orbit-census publication remains an unexcluded priority risk.

## value

PASS

Four-letter DNA words are a canonical finite coding benchmark. Exact sharp capacity, complete labeled optimizer inventory, symmetry collapse to 28 types and the two-codeword penalty for excluding self-reverse-complement strands are natural boundary facts for combining strand symmetry and one-deletion correction. No biological stability or general asymptotic capacity is claimed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
