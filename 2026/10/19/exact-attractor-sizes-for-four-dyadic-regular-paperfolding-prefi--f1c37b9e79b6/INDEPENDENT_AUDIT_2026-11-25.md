# Independent mathematical audit

## correctness

PASS

Independently reconstructed the word by p(2j)=p(j), p(2j+1)=j mod 2, and matched the first sixteen bits and the frozen zero-based witnesses. Used lossless integer keys (leading 1 followed by the bits) to enumerate every substring and test for an occurrence meeting the witness. For each weighted factor, exact overlapping matches and a difference array reconstructed the union of occurrence spans without counting multiple occurrences at a position twice. Every attractor hits each such union, so summing weights over its positions bounds the numerator total by denominator times attractor size. Independent replay rows (length, distinct factors, witness size, weighted factors, numerator sum, denominator, maximum load): (128,6479,5,5,5,1,1), (256,25775,6,11,11,2,2), (512,102767,6,12,12,2,2), (1024,410351,7,21,51,8,8). Taking ceilings gives the same four sizes as the witnesses.

## originality

PASS

The strongest indexed comparison gives bounds on exactly these four instances rather than their minima. The inspected primary results neither resolve those gaps nor supply a stronger evaluated theorem implying the four values. The pass is limited to the finite exact values, not the factor counts, word definition, earlier dyadic minima, or general certificate method.

## value

PASS

The four canonical dyadic folding scales are the already identified open rows of a natural benchmark, not chosen after finding favorable numerical outcomes. Exact optima with reusable upper witnesses and weighted lower certificates give a reference for checking algorithms and testing proposed attractor-profile bounds for this automatic word. The contribution is finite and claims no growth law.

The dated certificate retains the supplied scientific assessment, sources and limitations.
