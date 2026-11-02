# Scientific review — maximal repetitions of finite Cantor words

## Correctness — PASS
The paired-one residue argument excludes all nonconstant square periods except \(2\cdot3^j\). The complete classification follows by proving that every higher-period maximal repetition has ternary-block-aligned endpoints and descends to a predecessor run, while each predecessor run inflates maximally. At the base, exactly one period-two run belongs to each `101` image block. The ternary-carry zero-gap law supplies all period-one runs. These lemmas prove the exact multiplicities, \(3\cdot2^{k-1}-3\) runs, and total run length \(4\cdot3^k-13\cdot2^{k-1}+1\). An independent brute-force checker confirms all run triples through level six, but finite checking is not substituted for proof.

## Originality — PASS (qualified)
Baturo–Piątkowski–Rytter (2013, DOI 10.37236/2473), inspected in the primary full PDF, prove a run-count formula for standard Sturmian words. Glen–Simpson (2013, arXiv:1301.6568), inspected in primary full HTML, give general extremal and average results for total run length. Neither paper implies the displayed located Cantor-morphism classification. The k-Abelian-Cantor comparison in arXiv:1809.09047 addresses a different equivalence invariant. Direct research-record and comparison with earlier scientific claims found no explicit counterpart. Residual risk: historical equivalent formulations and less accessible papers cannot be excluded.

## Value — PASS
The all-scale, exact period-and-length spectrum answers a natural maximal-repetition question for a classical sparse automatic word. It reveals \(\rho(C_k)/|C_k|\to0\) but \(\operatorname{TRL}(C_k)/|C_k|\to4\), contrasting counting density with accumulated periodicity. The theorem gives explicit locations, not merely an aggregate formula, and is relevant to structural repetition analysis in compressed strings.

## Limits
Only complete finite Cantor iterates with ordinary contiguous periodicity are covered. No claims about arbitrary prefixes, generalized powers, or global historical uniqueness are made. Independent validation is outstanding.

Self-review: passed. Independent audit: not yet performed.
