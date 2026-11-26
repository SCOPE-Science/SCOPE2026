# Independent mathematical audit

## correctness

PASS

For the revised claim in /workspace/repairs/1/RESULT.md, rotation commutes with T_f and its constant fixed set and 30-state nonconstant complement are invariant under a bijection, giving the upper bound. A 30-cycle therefore consumes exactly the nonconstant sector. On the six size-five rotation classes it induces a six-cycle, and after six steps the phase on a given class is a power of the rotation by commutation. This power has order 1 or 5, giving period 6 or 30 respectively. The repaired orbit-test justification now explicitly requires the image class to have size five before inferring injectivity on that class. An independent, complete 65,536-table census constructed all 32 images and directly decomposed every accepted permutation. It confirmed 28 profiles, 96 period-30 rules split 32/64 by profile, and 4/16/76 by ANF degree. The degree restriction also follows from balance: each four-bit input appears twice at any coordinate, so a reversible truth table has eight ones and vanishing top ANF coefficient. Replay: /workspace/branches/4aea6f5b-cf4e-4979-a5fe-67d16e6a2191/reproduce_census.py. The frozen VERIFY.py and VERIFICATION.md were inspected, not executed or altered. This is a proof and reproduction for five labeled sites, not any other ring length.

## originality

PASS

The 472-rule count in the frozen theorem is explicitly covered in Dennunzio–Gadouleau–Mariot §4 for exactly the same family and does not pass as a distinct claim. The corrected RESULT.md removes it from the claimed contribution, attributes it and retains it only as context and a replay consistency check. On reassessment, the distinct surviving claim is the exact temporal cycle census: maximum 30, exact tally of maximizing rules, split by profile and degree, and 28 total profiles. The inspected primary sections and bounded catalogue comparisons did not establish equivalent coverage of these temporal results. This is an assessment of the supported remainder, not a pass for the original combined statement or a priority certificate.

## value

PASS

This is the first diameter admitting nonlinear diagonal-transversal examples in the motivating bipermutive setting, so the five-site family is not an arbitrary sample. Iterating the resulting diagonal permutation asks whether the full nonconstant sector can lie in one orbit, and if so how often and at what degrees. The exact census proves that the rotation bound is attained and identifies the frequencies, including many genuinely nonlinear maximizers and both types of constant-state dynamics. The known reversible-rule count is not part of this value judgment.

The dated certificate retains the supplied scientific assessment, sources and limitations.
