# Independent mathematical audit

## correctness

PASS

Any nonempty cross-bifix-free family has one common endpoint orientation because all first/last bits differ and mixed orientations cause length-one conflict. Reversing if needed, every word has interior ones i<j and a final one. If a=min i and b=min j over the family, overlap constraints imply a+b>n: if not, prefix 0^(a-1)1 of a witness equals suffix of another ending at its second interior one. Conversely when a+b>n, every prefix ending at its first/second interior one has fewer 1s than the corresponding suffix (1 versus ≥2, or 2 versus 3); prefixes ending in zero cannot match a suffix ending in one. Every valid family is contained in the threshold family F_{n,a}, whose size (a-1)(2n-3a)/2 is a concave quadratic, giving exact maximum and forcing equality with full F. Integer vertex a=n/3+1/2 gives ties only when n=3m and the stated four (else two) labeled optima after reversal. Independent exhaustive oriented subset enumeration at n=4..8 returned sizes 1,2,3,5,7 and oriented maximizer counts 1,1,2,1,1.

## originality

PASS

Wang–Wang's q-ary generating-function work derives general non-overlapping code constructions/sizes, while Qin–Chen–Luo discusses non-expandability and other Wang–Wang work treats variable lengths. They do not state the exact all-n constant-weight-3 optimum and complete labeled maximizer classification in inspected results. Classical construction principles may contain this as a special case and are included as a residual risk.

## value

PASS

Fixed-weight-3 synchronization codes form a natural first nontrivial sparse binary layer. The theorem gives infinite-length exact zero-error capacity, all labeled optimum codebooks and a residue-three rigidity phenomenon; it is neither a tiny isolated case nor ordinary unrestricted-code size.

The dated certificate retains the supplied scientific assessment, sources and limitations.
