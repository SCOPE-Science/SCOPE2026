# Independent mathematical audit

## correctness

PASS

For every q>=3,k>=2,2<=L<=k, and n>=q(k-1), the receiver k*e_i bounds heavy x_i>=k codewords by L, so total heavy incidences <=qL. Above n=q(k-1) pigeonholing forces every word heavy; at equality only F=(k-1,...,k-1) can be nonheavy. Construct cyclic X_{i,j}=(n-j)e_i+j e_{i+1} for 0<=j<L: n-j>= (q-1)(k-1)>=k, j<k, so exactly one heavy coordinate and all X distinct. Two distinct cycle-edge groups meet on at most one symbol; any potential shared k-descendant would be k times that symbol, but this symbol is light (<k) in at least one group. Thus a k-descendant has <=L codeword parents. At n=q(k-1), adding F is safe because every descendant y<=F is nonmonochromatic and cannot descend from any j=0 pure word; it can have <=L-1 cyclic parents. Incidence equality forces F in every boundary extremizer, each remaining word with exactly one heavy coordinate, and exactly L codewords heavy in each coordinate. At later n, all words have unique heavy coordinates and each occurs exactly L times. No claim for q=2, L=1, L>k or n<q(k-1). This is a complete uniform finite-combinatorial proof, not based on finite enumeration.

## originality

PASS

In the examined relevant primary and published same-object record, exact parent-list capacities for unordered q-ary multiset deletion with L>=2 are not implied. Earlier q/k extremal heavy-coordinate incidence for unique decoding and cyclic Sidon codes are genuine related prior art; originality is confined to the uniform L>=2 sharp plateau, cyclic list-attaining construction and saturation profile, subject to possible unindexed hypergraph packing equivalence.

## value

PASS

In an established unordered deletion channel, the maximal number of messages compatible with bounded receiver ambiguity is a natural exact coding-theoretic invariant. The theorem solves an infinite q,k,L regime, identifies a sharp n=q(k-1) to n=q(k-1)+1 one-message transition, and provides both a uniform list-achieving cyclic construction and an equality-saturation structural restriction. Though the heavy-incidence upper bound is elementary and known in L=1 guise, attaining it for every L>=2 including the exceptional light word is a motivated useful exact capacity fact, not just a computed table or arbitrary slice. No general graph/hypergraph breakthrough or full maximizer classification is claimed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
