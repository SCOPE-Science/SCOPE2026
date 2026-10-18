# Independent mathematical audit

## correctness

PASS

PASS: Independent combinations-counting (not source saved log) confirms 10-letter u=0101010001 and v=1000101010 are distinct factors of σ⁴(0)=0100010101000100 at offsets 4,1 and have identical subsequence counts for every binary word of length 1..3, while binom(u,0001)=21 versus binom(v,0001)=15. For any morphism h and target subsequence length ≤k, group an occurrence across its r≤k nonempty source blocks, showing binom(h(w),x) is an integer linear combination of binom(w,y) with |y|≤k. Hence k-binomial equivalence is preserved. σ(0)=01, σ(1)=00 is injective and 2-uniform, so distinct factors persist under iteration at lengths 10·2^t for all t≥0. The certificate.json seed values were inspected independently of the proof, and the checker directly counted small images.

## originality

PASS

PASS: Rigo–Stipulanti–Whiteland explicitly present strict third-order period-doubling binomial complexity as a COMPUTER EXPERIMENT observation while proving a second-order theorem; their inspected article does not give the 10-letter seed pair or an infinite constructive proof. General Thue–Morse morphism-preservation tools are prior. An unindexed equivalent seed pair remains possible.

## value

PASS

PASS: A published statement previously supported by experiments becomes an unconditional infinite family of concrete third-order collisions, addressing a natural complexity gap in an extensively studied automatic word. This is not merely a finite table and does not overclaim the complete third-order function.

The dated certificate retains the supplied scientific assessment, sources and limitations.
