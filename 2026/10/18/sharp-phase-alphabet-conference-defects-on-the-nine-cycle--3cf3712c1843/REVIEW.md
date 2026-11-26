# Independent mathematical audit

## correctness

PASS

Verified the exact reductions in RESULT.md lines 37–71. A common alphabet phase gives exactly one f(1)=1 representative per orbit, so the q^7 remaining tuples exhaust all candidates with no parity restriction. Power-basis residue coordinates in the four cyclotomic rings vanish exactly for zero mean. At the four positive lags the summands are 1 plus the seven cyclic products, and conjugate pairing doubles the sum of their norm squares. The sextic-alphabet norm a²+ab+b² and octary norm a²+b²+c²+d²+[a(b−d)+c(b+d)]√2 follow by taking real parts of products of powers; integer square comparisons are exact by irrationality. An independent exhaustive replay (python3 /workspace/branches/c109caee-1500-4b9e-8902-ee70aba4b617/independent_check.py) reproduced all feasible counts (35,1225,9135,23765), minima (16,16,4,24−16√2), and normalized minimizer counts (12,84,6,6). It reproduced all six explicit octary tuples, the next distinct value 40−24√2, and equality between the optimizer set and the normalized orbit of one seed under dilation and conjugation, giving 48 before normalizing. All minima are positive. Parseval uses the target autocorrelation 9δ_0−1 and yields exactly the stated spectral formula. If one uses the full unnormalized 9-by-9 circulant Gram error, its Frobenius norm squared is 9 times the defect; the equivalence is up to this constant. The frozen verifier and notes are evidence, not the reproduction. This proves only the four finite alphabets and the specified zero and zero-mean constraints.

## originality

PASS

There is real overlap with the unrestricted conference-signal framework and with the exact even quartic slice of a later dated record. The supported distinct result is the all-parity, four-alphabet exact defect and optimizer census, especially the exact six- and eight-phase minima and octary gap and orbit. The closest inspected sources do not settle that result.

## value

PASS

Nine is an already studied small conference-signal order with unrestricted zero-defect examples; common phase alphabets are a natural restriction of that design problem. Exact positive margins distinguish what several phase quantizations can achieve, including no improvement from two to four phases and a strictly smaller octary than sextic margin. The exact next distinct octary level and single optimizer orbit give reproducible separation and classification benchmarks, not just candidate waveforms or a routine check of the continuous examples. The value is finite and specific to this order.

The dated certificate retains the supplied scientific assessment, sources and limitations.
