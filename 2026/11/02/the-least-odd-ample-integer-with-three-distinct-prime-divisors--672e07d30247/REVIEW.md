# Scientific review: least odd three-support ample integer

## Correctness — PASS
The theorem is global, not a finite observation: (i) each exponent vector has the same recursive-divisor count for every choice of distinct prime bases; (ii) the canonical bases 3, 5, 7 minimize the integer within the odd three-prime class; (iii) any smaller ample integer would produce a smaller canonical ample integer; (iv) exact integer enumeration of all 4,649 canonical candidates below the asserted threshold excludes every one; and (v) exact evaluation at the remaining candidate proves strict abundance. The exponent bounds are derived from the threshold. The standalone verifier constructs each tabulated value twice through algebraically different recurrences, independently checks 343 small entries through direct divisor summation, and matches seven closed-form evaluations. The deficit lemma excludes odd supports of size one or two. No heuristic computation is promoted into an infinite proof.

Scientific risk: an error in the finite cutoff or program would be consequential, hence all bounds, assertions, full code, and the independent cross-checks are provided for replay. This is exact integer arithmetic, not a bounded trial presented as an infinite computation.

## Originality — PASS within checked evidence
The exact *least odd ample three-support integer* and uniqueness are not implied by Fink's 2020 recursive-divisor definitions, formulas, or first low-support examples, nor by Fink's 2023 Dirichlet/convolution treatment. The later published proof of existence on any sufficiently abundant finite prime set covers the existence of an ample integer on \(\{3,5,7\}\) but expressly declines to give an effective least-witness bound: its existence result cannot imply the claimed sharp integer. Searches for synonyms (recursively abundant, ample, least odd, exactly three prime divisors), explicit exponents, and the 21-digit threshold did not locate a covering theorem or table. A published result on odd almost-practical three-prime numbers studies a different arithmetic predicate. Earlier accessible results on the least total prime-factor multiplicity of odd ample numbers and on exponent-balancing provide related structural context, but neither determines the least three-prime-support integer.

Residual risk: absence from indexed searches is not proof of global novelty; an overlooked earlier computation of the same least witness would cover the result, and the independent audit remains outstanding.

## Mathematical value — PASS
Prime-support cardinality three is the **sharp smallest possible** for an odd ample number, as supports one and two are always deficient. The precise initial threshold in that extremal class is a canonical natural invariant, not an arbitrary exponent slice. The unexpectedly large least witness, its uniqueness, and the rigorous finite reduction answer the exact minimum question left unquantified by existence results. These results make future quantitative investigations of rare recursively abundant odd numbers possible without mistaking an arbitrary sample for the first example.

Limits: this does not yield asymptotics or classify all odd ample three-prime integers. Reproducible correctness and plausible originality, alone, would not justify value; the substantive motivation is the canonical extremal support boundary and its exact least realization.

Self-review: passed. Independent audit: not yet performed.
