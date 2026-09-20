# Review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

**Assessment: PASS.**

The target value follows from the exact maximisation formula of Caro--Škrekovski--Zarb: for delta=1 and k=1, their parameter satisfies 2x=d-1, so the maximised bound is ceil(n/d). The obstruction at n=2d is immediate from the universal sp(G,1)>=3 theorem, and the parameter class at that order is explicitly shown to be nonempty.

The upper constructions were checked by three independent mathematical mechanisms across the relevant ranges. For 2d+1<=n<3d, the stated centered step-two perturbation of 1,2,...,2d-1 has the required sum and window number, and a direct Erdős--Gallai slack calculation covers every index. The n=3d endpoint is checked at the Tripathi--Vijay breakpoints. For 3d<n<4d-2, the centered doubled subset gives a positive gap-free list to which the Barrus--Hartke--Jao--West length theorem applies. For n>=4d-2, Cloteaux's sum-sensitive graphicality inequality reduces exactly to n>=4d-2. In all cases the minimum degree remains exactly one and the degree sum is nd.

A standalone finite check independently verified the displayed constructions with the full Erdős--Gallai criterion for every admissible pair 2<=d<=100 and 2d+1<=n<=8d, 22,797 pairs in total. This computation is supporting evidence only; the general result rests on the proof.

Adversarial checks included the parity condition nd even, the small case d=2, the endpoint n=3d, empty intermediate ranges for small d, the maximum-degree constraint, and the transition at n=4d-2. No hidden exception was found.

## Originality

**Assessment: PASS, to the best of our knowledge.**

The motivating source is Caro--Škrekovski--Zarb, arXiv:2609.19762, submitted 17 September 2026. Its Problem 22 explicitly asks for the smallest onset n0(delta,k,d) and says the data suggest 2d+O(k+1), while Theorem 13 supplies only a general quadratic sufficient threshold. The paper's Proposition 4, Theorem 8, Theorem 10, Theorem 13, and concluding Problem 22 were inspected. No exact evaluation of n0(1,1,d) is stated there.

The earlier Caro--Lauri--Zarb paper was checked for the spread definition and universal sp(G,k)>=k+2 result. The graphicality literature used in the proof was also checked: Barrus--Hartke--Jao--West for gap-free lists, Cloteaux for the sum-sensitive condition, and Tripathi--Vijay for reduced Erdős--Gallai checking. These results supply tools but do not state the present onset theorem.

Searches covered exact and synonymous formulations including "n0(1,1,d)", "sp(G,1)", "2d+1", "spread of degrees", "two consecutive degrees", "window number", "minimum degree 1", and combinations with the motivating preprint and its Problem 22. No prior statement equivalent to n0(1,1,d)=2d+1 was found, nor a stronger theorem implying it directly.

No specific inaccessible paper was identified as especially likely to overturn the originality claim. The main residual risk is unindexed or simultaneous work because the motivating preprint is only one day old. The Barrus--Hartke--Jao--West exact gap-free theorem statement was available from the authors' public copy/abstract, although its full proof was not needed for this review.

## Value

**Assessment: PASS.**

The result exactly solves an infinite specialization of a newly stated threshold problem, rather than merely improving a constant in the general sufficient bound. It confirms the suggested linear scale in the concrete case h=2 with the sharp value 2d+1, and provides explicit optimal degree-sequence families covering every admissible order above the obstruction.

## Limitations

The theorem is restricted to delta=1, k=1, and integer average degree d>=2, with thresholds understood over orders for which nd is even. It does not resolve nonintegral fixed average degrees, larger minimum degree, or wider windows. Originality is to the best of our knowledge, and independent audit has not been performed.
