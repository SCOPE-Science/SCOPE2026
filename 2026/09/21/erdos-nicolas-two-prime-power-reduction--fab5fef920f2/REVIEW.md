# Same-model review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

PASS.

The four structural statements were rederived from the ordered divisor geometry of \(2^a p^b\).

For \(b=1\), grouping a prefix into the pure powers of two and the \(p\)-multiple layer yields
\[
p=\frac{2^{r+1}-1}{2^a-2^{s+1}+1},\qquad s<r.
\]
The cases \(r\le a-2\), \(r=a-1\), and \(r=a\) were checked separately. Only the Mersenne-perfect branch \(p=2^{a+1}-1\) and the exceptional solution \((a,p)=(3,3)\) remain. Boundary cases \(s=0\) and \(s=a-1\) were explicitly included.

For \(b=2\), parity forces exactly two nonempty \(p\)-adic layers. The cutoff is therefore below \(p^2\), and a sharp layer-sum bound forces \(a=1\); the remaining four possible proper divisors sum to less than \(2p^2\).

For \(p>2^a\), the divisor layers are separated into complete blocks. Reduction modulo \(p\) forces \(p=2^{a+1}-1\); a size comparison forces the prefix to reach the top \(p\)-block, and divisibility of the lower full-block contribution excludes \(b\ge2\).

For \(b\ge3\), the proof that the entire pure-2 layer must be included was checked in both cases for the highest included \(p\)-exponent. The valuation argument establishing \(h<v_p(2^{a+1}-1)\), the strict descent of binary exponents after the last full layer, the estimate forcing the top \(p^b\)-layer to occur when \(a\ge4\), and the parity condition forcing odd \(b\) are mutually consistent. The special cases \(a=1,2,3\) were checked separately.

The standalone exact program directly tests 383,640 \((a,b,p)\) triples for \(b=1,2\), finding zero mismatches. It also factors \(2^{a+1}-1\) by exact trial division for \(a\le30\), enumerates all 661 higher-exponent candidates allowed by the proved reduction, and finds zero hits.

## Originality

PASS, qualified as to the best of our knowledge.

The original Erdős--Nicolas paper was inspected at the section where the defining equality and the examples below \(10^6\) are stated. It gives the definition and a finite list, not the \(2^a p^b\) structural classification proved here. The current A064510 and A194472 entries were checked, including their comments, cross-references, and programs. De Koninck's 2009 treatment was checked through the Erdős--Nicolas entries available in searchable text.

Searches used the object name and synonyms: Erdős--Nicolas numbers, A064510, A194472, partial sums of divisors, initial divisors, sums of the first \(k\) divisors, the forms \(2^a p\) and \(2^a p^b\), prime-square odd part, and Mersenne specializations. The SCOPE archive was also searched immediately before publication using the same object and claim-family terms. No exact theorem, equivalent reformulation, or stronger result implying Theorems 1--4 was located.

There is neighboring literature on semiperfect/pseudoperfect numbers of the form \(2^a p\), but that permits arbitrary subsets of proper divisors and is strictly weaker than the ordered-prefix condition here; it does not imply this classification.

Residual originality risk remains because the Erdős--Nicolas literature is sparse and an elementary special-case theorem could have appeared in older problem collections or poorly indexed notes under different terminology. No concrete source suggesting prior coverage was found.

## Value

PASS.

The result does more than identify a new example: it completely resolves the natural prime and prime-square odd-part slices, isolates 24 as the unique genuine Erdős--Nicolas number in the first slice, proves a global large-prime obstruction for every exponent, and reduces every higher-exponent case to a finite list for fixed \(a\). The mechanism combines divisor ordering, parity, elementary divisibility, and a short \(p\)-adic valuation argument. The exact reduction also makes substantial bounded searches mathematically exhaustive rather than heuristic.

## Limitations

The theorem does not rule out all \(b\ge3\) cases. It leaves a finite candidate set for each fixed \(a\), and the supplied exact computation exhausts that set only through \(a=30\). Originality remains a to-the-best-of-our-knowledge assessment rather than an exhaustive bibliographic guarantee.
