# Scientific review of the degree-three tangent-filling curve over \(\mathbb F_7\)

## Correctness — PASS

The partial derivatives of the displayed cubic have no common geometric projective zero: the case \(X=0\) forces all coordinates to vanish, and after setting \(X=1\), the three equations force incompatible values \(Z^3=4\) and \(Z^3=3\). The point/tangent table is an exhaustive finite-field calculation independently reproduced by the included pure Python verifier. The twelve distinct tangents multiply to the Fermat/triangle arrangement polynomial; their vanishing at every rational plane point follows from the elementary fact that nonzero cubes in \(\mathbb F_7\) are \(\{1,-1\}\). The dual-conic no-three-concurrent argument gives a sharp bound of 36 covered points for any smooth conic, and reducible quadrics cannot cover the whole plane by tangents.

## Originality — PASS, with residual risk

Asgarli–Ghioca, arXiv:2302.13420, ask for the minimum tangent-filling degree in Question 1.5. Their degree-six construction for large fields does not include \(q=7\); their Remark 3.7 proves the failure of one model there, not a lower bound for cubics. Asgarli–Ghioca–Yip, arXiv:2208.13299, exclude a cubic's *own points* from being a blocking set for \(q\ge5\), which does not exclude a blocking family of *tangents*. They also describe classical projective-triangle configurations; novelty is not asserted for the twelve-line configuration in isolation. Targeted indexed searches for equivalent cubic realizations, Fermat/Ceva aliases, and general dominating theorems found no equivalent coverage. An unindexed antecedent remains possible.

## Mathematical value — PASS

The result gives the exact minimum of a naturally posed plane-curve degree invariant at the prime field of order seven. The realization by a geometrically smooth genus-one cubic, together with the impossibility of every degree-one or degree-two candidate, completes the case; the numerical incidence spectrum is supporting information rather than a substituted contribution.

## Limits

The theorem does not classify all smooth tangent-filling cubics, generalize to other fields, or establish priority against unindexed literature. No independent audit has been performed.

Self-review: passed. Independent audit: not yet performed.
