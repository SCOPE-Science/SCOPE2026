# Independent mathematical audit

## correctness

PASS

The stabilizer H has order q dividing 4; quotienting by H produces 4/q positive hypotheses at every query and n/q distinct translates. q=4 leaves one positive hypothesis so Ldim=1; q=2 gives exactly two positive and at least two negative, yielding depth 2 but forbidding 3. If q=1, every root positive branch contains four hypotheses and negative contains n-4>=4, forcing Ldim<=3 and >=2. To shatter depth three the four-element positive space must split 2/2 on its second query, equivalently a nonzero overlap lambda_A(t)=2. Conversely a split of size 2 yields all four second-level cells cardinalities 2,2,2,n-6>=2 and a third separating query in each, so Ldim=3. Explicit difference lists for A and overlap for B show the infinite equal-size contrast. Fresh independent recursion over actual Boolean incidence tables confirms all 1,231 four-subsets for n=8..12 and both n=15 witnesses. Finite tests do not establish n unbounded; analytic version-space argument does.

## originality

PASS

Best-of-knowledge sharp Littlestone dimension trichotomy not implied by general closure theorems, unions-of-translates literature, or published four-point Fourier/difference-set classifications. Their different statements and objects are explicitly distinguished. Specialized older combinatorial-learning results may still hide an equivalent, a residual risk.

## value

PASS

Complete all-n structural classification of a natural online-learning invariant for cyclic translate hypothesis classes. The criterion links adaptively shattered trees to one elementary autocorrelation multiplicity and distinguishes Sidon supports from intervals even when hypothesis count and support size agree.

The dated certificate retains the supplied scientific assessment, sources and limitations.
