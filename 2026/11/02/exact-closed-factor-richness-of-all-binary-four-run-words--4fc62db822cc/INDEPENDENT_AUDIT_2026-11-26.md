# Independent mathematical audit

## correctness

PASS

This passes for the corrected RESULT.md under repairs/5, not the frozen proof as written. The frozen line 43 asserted that different endpoint letters preclude a border, which is false (0101 has border 01); the frozen four-run argument also omitted why the suffix of a proper border cannot start inside the first run. The replacement proves the needed transition lemma: such a suffix includes the first transition but shortens the initial run, whereas a matching prefix with a transition includes the whole initial run. The suffix must start in a later run of the initial letter. For two runs there is none; for three runs the border is unary and is closing exactly when the outer run lengths coincide; for four runs the only possible border of 0^i1^b0^c1^j is 0^i1^j, occurring exactly at the two 01 transitions if i<=c and j<=b. Including the unary powers and empty word gives n+1+xy. Maximizing xy over positive integers with sum at most floor(n/2) forces the largest allowed sum and balanced pairs (strict increase of floor(s^2/4) for s>=2); the residual is zero or one and all placements are accounted for, including n=4. The ordered length-pair weight for a fixed minimum is z^(2x)(1+z)/(1-z), giving the bivariate series and, by differentiation in u at one, z^4/((1-z)^6(1+z)^2). This analytic argument covers all lengths. The supplied verifier was inspected but not executed; its finite comparisons are diagnostic and neither needed for the general theorem nor a substitute for the repaired proof.

## originality

PASS

The corrected theorem retains the all-positive four-run case, with exact counts, maximizers and multiplicities, and both formal series. The closest exact Resultary comparison covers only the boundary with exactly two occurrences of one letter, and is now credited explicitly. The classical four-block construction gives a lower bound, and the known unrestricted asymptotic and short tables do not imply the exact restricted formula or equality cases. Pass is for the all-positive classification and its consequences, not historical priority for the boundary or the balancing and series algebra in isolation.

## value

PASS

Exactly four linear runs is the first binary run class beyond the bitonic CR-poor regime, not an arbitrary slice. The theorem measures how the positive excess begins, classifies the closed factors responsible for it at every run profile, and determines exact maximizers and their frequencies. The contrast between the four-run leading coefficient 1/16 and the unrestricted 1/6 makes the restricted result useful even though it does not solve the unrestricted problem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
