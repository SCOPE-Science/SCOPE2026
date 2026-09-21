# Same-model review

## Correctness

**PASS.** The proof reduces each decoded data bit to a Boolean function on a small linear quotient. For a recovery set I, the decoded bit is constant on the kernel of the coordinate projection of the linear associated code, namely the orthogonal complement of the span of the generator columns indexed by I. With t disjoint recovery sets, the decoded bit therefore factors through a quotient whose dimension is the dimension of the intersection of those t column spans.

The dimension estimate is exact at the needed level: if that intersection has dimension d, then the span of the t recovery-set column spaces has dimension at most the sum of their dimensions minus (t-1)d. Adding the columns outside the recovery sets and using rank k gives k <= n-(t-1)d, hence d <= floor((n-k)/(t-1)). When n-k <= 3t-4, d <= 2. Every coordinate of a bijection of F_2^k is balanced, and every balanced Boolean function on a quotient of dimension at most two is affine. Thus the entire inverse labeling is affine with invertible linear part. Translating the message labels then gives a linear encoder onto the same code and preserves every recovery set up to a fixed output-bit complement.

For the length-11, size-2^7 corollary, k=7 and r=4, so the theorem applies for t=3. A linear 3-PIR encoder would contradict the known bound binom(r,2) >= k because binom(4,2)=6<7.

## Originality

**PASS, to the best of our knowledge.** Hollmann and Luhaäär explicitly distinguish nonlinear associated codes from nonlinear encoders onto linear associated codes, and they leave the existence of a binary 3-PIR code of length 11 and size 2^7 open. Their paper proves a special no-encoder theorem for Hamming codes, but does not state the general low-redundancy affine-linearization result above. The linear redundancy bound used in the corollary is known and is not claimed as new.

Searches covered the exact open parameters and synonymous formulations involving PIR codes, batch codes, nonlinear encoders, nonlinear labelings, linear associated codes, affine encoders, recovery sets, and low redundancy. Relevant later literature through 2026, including work on unequal-data-demand PIR codes and all-symbol PIR/batch codes, was also checked at the level needed to identify its scope; no theorem located there subsumes this nonlinear-on-linear reduction.

The principal residual originality risk is that an equivalent Boolean-function or coding-theoretic linearization lemma may exist under terminology not indexed as PIR or batch coding. No concrete source suggesting such prior coverage was found.

## Value

**PASS.** The theorem removes an entire mechanism by which nonlinear PIR codes might beat linear ones in a natural low-redundancy regime. It also gives a direct structural sharpening of the first unresolved small binary 3-PIR parameter identified by Hollmann and Luhaäär: a length-11, size-2^7 solution, if it exists, cannot merely relabel a linear code nonlinearly; its associated code itself must be nonlinear. This materially narrows both theoretical and computational searches for the open case.

## Scientific limitations

The result is specific to the binary alphabet at the affine-forcing step. The bound r<=3t-4 is sufficient and is not claimed optimal. Once the quotient dimension can be three, balanced nonlinear Boolean functions exist, so the proof does not extend automatically. The theorem does not decide whether the length-11, size-2^7 binary 3-PIR code exists.

Same-model review: passed. Independent audit: not yet performed.
