# Independent mathematical audit

## correctness

PASS

A square cannot use a letter appearing once in its ambient arc. This gives ordinary squarefreeness by deleting the middle letter and inducting. In the doubled word, a square using the largest letter must use the two listed copies at separation exactly |Z_m|, so it is the whole doubled word; one avoiding that letter must occur in the central doubled Z_{m-1}, since the outer blocks are squarefree. In a circle restricted to one traversal, the largest letter cannot appear twice; the remaining arc is exactly doubled Z_{n-1}. Translating starts gives N_n-(2^k-1). The next symbol is k+1 rather than the first symbol 1; any longer periodic factor would extend its square prefix, so none has exponent >2. For a seam-crossing square of half-length L, exactly the cuts in [L,N_n-L] retain it, including both endpoints. Those intervals are nested, and differ in size by 2^{k+1}; the last interval contains two cuts. The rank-one word and the empty starting-cut class are handled separately. A separate bit-parallel test checked all starts and allowed periods, their extensions, and all cuts through n=13, reproducing the entire histogram.

## originality

PASS

The supported distinct claim is the exact cyclic occurrence inventory and associated finite-conjugate histogram, including absence of extensions within one traversal. Linear Zimin squarefreeness is known. No inspected result states or yields the joint inventory and histogram by direct specialization; the conclusion is limited to the materials compared.

## value

PASS

Finite Zimin words are a canonical recursively defined squarefree family. Closing the seam changes what repetitions occur, and the complete inventory quantifies that change precisely; the cut distribution further tells which linear conjugates are squarefree or have any given square count. This is exact data for arbitrary rank rather than a single rank check, a restatement of squarefreeness, or an extremal bound.

The dated certificate retains the supplied scientific assessment, sources and limitations.
