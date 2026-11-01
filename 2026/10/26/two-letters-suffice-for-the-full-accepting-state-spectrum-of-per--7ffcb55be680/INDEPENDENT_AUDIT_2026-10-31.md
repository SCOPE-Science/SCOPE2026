# Independent mathematical audit

## correctness

PASS

The binary witness has a k-cycle a paired with counter increment 1 and a transposition b with increment 0, with k=alpha+1, h=n+1. The generated permutation projection is S_k. Identity-permutation words a^k and (ab)^(k−1) increment the counter by coprime k and k−1, hence the generated group is S_k×Z/h, INCLUDING k=2, and every B state is reachable/distinguishable. Accepted B words project precisely onto the stabilizer of k. Therefore the quotient final set is all k−1 nonfixed states, and symmetric-group transitivity yields quotient DFA minimality and asc=alpha. All alpha≥m are obtained; the published unary interval 1..mn provides alpha<m; no nonempty K,L can give empty right quotient since permutation transitions are invertible. Independent BFS enumerated the entire action for all 12 (k,h) with 2≤k≤5, 2≤h≤4 and 30 stabilizer/quotient cases. The infinite result follows from the group proof.

## originality

PASS

Existing ternary full spectrum and unary finite interval do not alone imply binary sufficiency. The two coupled generators with coprime null-permutation counter words supply that exact missing implication.

## value

PASS

Alphabet-size optimality is a natural sharp refinement of the existing unary-to-nonunary dichotomy. Explicit two-generator group control replaces a previously independent third letter, and the unary interval proves sharpness, so this is structural rather than a renaming of the unrestricted theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
