# Same-model review

## Correctness — PASS
The claim reduces deletion correction to the exact intersection condition \(\iota(x,y)\le2\). The heavy-coordinate lemma is immediate: a shared coordinate of multiplicity at least three forces intersection at least three. For \(n\ge7\), pigeonhole forces every composition to have a heavy coordinate, so pairwise disjoint nonempty heavy sets give at most three codewords. The exceptional heavy-free compositions at \(n=5,6\) are fully classified, and the stated witnesses attain the resulting upper bounds. The embedded verifier independently exhausts the two exceptional finite cases.

## Originality — PASS
The closest primary source is arXiv:2601.05636v2. Its Section 4.4 gives the same intersection formulation but only the certificate bound \(S_q(n,n-3)\le q+\binom q2\) for \(n\ge q+2\), which specializes to six for \(q=3\). Its exact ternary section concerns one deletion, not \(t=n-3\). The foundational Kovačević–Tan multiset-code paper supplies the discrete-simplex framework and general bounds rather than this exact ternary extremal classification. Searches under deletion, intersection, discrete-simplex, and minimum-distance aliases found no stronger statement implying the piecewise formula. Residual risk: an older equivalent lattice-code result may exist under notation not retrieved by the searches.

## Value — PASS
This is a natural complete classification for the first nontrivial fixed-output extremal deletion regime over the smallest nonbinary alphabet. It sharpens a recent general upper bound from six to the exact values four and three, and it identifies the sharp threshold \(n=7\) at which only three codewords are possible. The proof is structural rather than a table recomputation.

Same-model review: passed. Independent audit: not yet performed.
