# Same-model review

## Correctness

PASS. The source's \(d=4\) Hypercube polynomial is specialized to the full coordinate-permutation-and-complementation invariant cone. Exact enumeration of all \(4368\) five-vertex subsets gives the displayed polynomial \(P\). The symmetry gives \(T=2S\) and makes all eight facet sums equal \(S=a+4b+3c\). The identity
\[
6\left(105S^5-1024P\right)
=
(a-b)^2A+(b-c)^2B+(a-c)^2C
\]
was checked coefficient by coefficient with exact integers. Every coefficient of \(A,B,C\) is positive. For a nonzero nonnegative triple, \(B\) and \(C\) are strictly positive, so equality forces \(a=b=c\). This yields the sharp ratio \(105/128\) and the sharp relative gap \(23/128\).

## Originality

PASS. The primary paper proves only \(d=3\), explicitly leaves \(d=4\) open, and says the unrestricted \(d=4\) polynomial has sixteen variables, degree eight, and roughly \(400000\) terms. Its full text contains no Hamming-weight specialization or coordinate-permutation-plus-complementation invariant slice. Targeted published-record and web searches found no \(105/128\) bound or equivalent statement. The closest prior finding concerns a different, already-false full log-submodularity inequality.

## Value

PASS. This gives a sharp theorem in the first open dimension on a canonical symmetry cone, not an arbitrary numerical slice. The exact best constant and unique symmetric extremizer provide a quantitative benchmark for the open unrestricted Hypercube inequality and show that this large natural cone stays uniformly away from failure.

Same-model review: passed. Independent audit: not yet performed.

## Closest literature and limitations

The closest source is Averkov--von Dichter--Soprunov, arXiv:2608.14909v1, which defines the Hypercube inequality, proves \(d=3\), and leaves \(d=4\) open. Contemporary Rayleigh/log-submodularity counterexamples concern a distinct stronger conjecture and do not cover this partial-polymatroid inequality.

The result is limited to weights satisfying
\[
x_v=x_{\pi(v)}=x_{\mathbf1-v}
\]
for all coordinate permutations \(\pi\). The unrestricted sixteen-variable \(d=4\) problem remains open.
