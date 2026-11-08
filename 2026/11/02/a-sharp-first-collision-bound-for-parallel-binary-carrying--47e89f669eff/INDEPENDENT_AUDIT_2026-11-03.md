# Independent mathematical audit

## correctness

PASS

For finite nonnegative integer coefficient sequence c, simultaneous carry update conserves N=sum 2^j c_j. If c_j(t+1)>=2, c_{j-1}(t)>=2 since c_j(t) mod2<=1; hence any collision at round t must lie at index >=r+t where r is first initial collision. At t=floor(log2 N)-r, a coefficient >=2 at such an index would contribute >=2^(floor(log2 N)+1)>N, impossible. Binary product convolution has c_0<=1, so if collision occurs r>=1, giving T<=max(0,floor(log2(ab))-1), which implies Iizumi bound. For odd k>=3, a=3, b=(2^k+1)/3 has a carry wave travelling positions 1...k-1, attaining T=k-1. All quantifiers and zero-collision convention explicitly addressed.

## originality

PASS

PASS for a direct proof of Iizumi 2026 Question 9.5.3 and a strictly stronger universally sharp product-bit bound. The same simultaneous update, the conjectured upper bound and exact infinite sharpness example are already explicitly present in Iizumi Definition 4, Remark 6, Proposition 1 and Question 9.5.3, and are credited. Iizumi proves qualitative termination but explicitly states the upper bound as empirical/open; finite tests are not his proof. Izsak–Pippenger 2011 studies probabilistic carry propagation in multiplication by constants under a different algorithm. An unindexed earlier deterministic parallel carry-wave theorem remains possible.

## value

PASS

Closes a concrete published open question in arithmetic combinatorics and gives the sharper exact bit-length bound for any finite nonnegative coefficient normalization. The natural first-collision index is the mechanism and the known infinite family proves exact optimality, not a textbook inequality alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
