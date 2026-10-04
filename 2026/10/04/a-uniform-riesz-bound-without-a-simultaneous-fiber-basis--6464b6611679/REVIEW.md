# Same-model review

## Correctness
PASS. The explicit frequency set has \(2p\) distinct characters. After blockwise Hadamard and Fourier unitaries, the evaluation matrix becomes \(\mathcal T=\begin{pmatrix}I&K\\0&I-K\end{pmatrix}\) with \(\|K\|^2=(p+1)/(2p)\le2/3\). The Neumann bound makes \(I-K\) invertible, and the displayed block-norm estimates give \(\rho(E_p,B_p)<251\). The universal proof is analytic; finite checks are auxiliary.

## Originality
PASS. The closest primary source is Ferguson–Mayeli–Sothanaphan, arXiv:1904.04487. It introduces this exact family, notes that its three translated fibers have no simultaneous basis, and states that boundedness of the condition number independent of \(p\) was unknown. Searches for the exact family, equivalent simultaneous-basis language, and broader finite multi-tiling/Riesz statements found no covering result. The own ledger contains related finite-group results but not this claim.

## Value
PASS. The claim resolves the source’s explicit boundedness uncertainty for the family and disproves the proposed necessity of the simultaneous-fiber-basis hypothesis in this instance. The construction also identifies a reusable two-channel mechanism: frequency-dependent fiber characters can replace a single simultaneous fiber basis.

## Closest literature and limitations
The primary source’s general theorem supplies uniform bounds only under a simultaneous-basis hypothesis. The new construction lies outside that hypothesis. The constant \(251\) is not optimized, and the argument does not remove the hypothesis from the theorem in full generality. Search coverage cannot rule out differently indexed later work.

Same-model review: passed. Independent audit: not yet performed.
