# Scientific review

## Correctness — PASS
The inverse-image proof treats every possible reset word, not just the displayed witness. A shortest inverse route omits nonexpanding reverse-collapse steps because set preimages are monotone. After its first useful collapse, the missing interval is \([1,n-k-1]\). A subsequent useful collapse necessarily follows at least \(n-k\) inverse rotations; it removes at most \(k\) missing states. Those two independent lower bounds yield \(1+\lfloor(n-2)/k\rfloor(n-k+1)\). The proposed word attains equality by successively advancing the missing interval's lower endpoint by \(k\). The proof covers the boundary \(k=n-2\) and all larger parameters without a computation cutoff. Executable finite tests use subset BFS and exhaustive interval cases but are not treated as infinite proof.

## Originality — PASS (limited bibliographic claim)
The closest inspected material includes Volkov's 2023 unimodal-letter results (synchronizability for one large kernel class), Rystsov–Szykuła's 2023 semiconstant primitivity/synchronization result, and their 2023 generic quadratic one-point bound. The exact threshold for the designated cyclic permutation and a simultaneously collapsing *consecutive* block is not entailed by those statements. The classical Černý single-merge family has only one moved state. Published finite automaton censuses and Černý avoidance studies concern different transition structures or different optimization objectives. A preexisting unindexed equivalent formula remains possible; the review is not a priority certificate.

## Value — PASS
This provides a closed-form optimal reset threshold and explicit shortest word for an infinite, structurally natural rank-deficiency family, not just an example, an upper bound, or a finite census. It gives a transparent transition from quadratic to linear synchronization cost as the consecutive collapsed block grows. The proof identifies the exact cyclic-interval bottleneck controlling all competing words, a reusable idea for related circular synchronization questions.

Self-review: passed. Independent audit: not yet performed.
