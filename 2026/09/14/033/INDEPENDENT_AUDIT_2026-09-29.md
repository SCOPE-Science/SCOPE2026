# Independent audit — 2026-09-29

Record: `2026/09/14/033`  
Audited source tree: `fba87d5115e152faccb8e11182376b51887242e9`  
Disposition: **repaired**

## Correctness

The archived PARI values do certify the nonzero cyclotomic 5-adic regulator of 37a1 over Q: R_5((0,0))=5+5^2+5^3+3*5^6+4*5^7+5^9+5^10+O(5^11), hence valuation 1; the ordinary p-adic L derivative also has valuation 1, while the -11 twist has rank zero and unit p-adic BSD value. Since 5 and 37 split in K=Q(sqrt(-11)), the standard ordinary factorization of the cyclotomic Rankin p-adic L-function gives a simple zero with nonzero derivative, and the ordinary split p-adic Gross-Zagier formula then yields nonzero cyclotomic height of the discriminant -11 Heegner class. The original record made two factual overclaims: 37a1 is nonsplit, not split, multiplicative at 37; and PARI ellheegner(E)=[0,0] does not identify the discriminant -11 Heegner point. The repair removes both errors and does not use [0,0] as the D=-11 point.

## Originality

The 5-adic regulator of 37a1 at p=5 is already a documented example in Sage and in published Iwasawa-theoretic literature, so that computation is not new. The surviving contribution is the explicit assembly of the K=Q(sqrt(-11)) split ordinary Rankin/Heegner nonvanishing check. No priority claim is made for the triple without an exhaustive literature proof.

## Scientific value

After repair, the record is a concrete, reproducible specialization of ordinary p-adic Gross-Zagier at a small conductor/prime/CM field, with independent nonzero factors on the E and twist sides. It is valuable as a worked verification, not as a new p-adic Gross-Zagier theorem or a proof of the full p-adic BSD formula.

## Limitations

- The numerical p-adic values rely on PARI/GP's p-adic height and p-adic L-function implementations with tracked precision; the audit did not formally verify those libraries.
- The repaired argument uses the standard factorization/base-change normalization of the ordinary cyclotomic p-adic L-function up to a nonzero local unit.
- The D=-11 Heegner point is not assigned the coordinate [0,0]; its nonzero p-adic height is inferred from the Rankin derivative through the cited p-adic Gross-Zagier theorem.
- The conclusion is a nonvanishing/simple-zero consequence, not a proof of all parts of p-adic BSD.
- The original artifact inventory had the stale prefix output/artifacts/; the actual archived files are under artifacts/.

## Sources checked

- https://github.com/SCOPE-Science/SCOPE2026/tree/e9ed144c13b7834896a844cc4f9cac3c25a168a6/2026/09/14/033
- https://arxiv.org/abs/1510.02114
- https://arxiv.org/abs/2001.00045
- https://doc.sagemath.org/html/en/reference/arithmetic_curves/sage/schemes/elliptic_curves/heegner.html
- https://doc.sagemath.org/html/en/reference/arithmetic_curves/sage/schemes/elliptic_curves/ell_rational_field.html
- https://doi.org/10.1017/S000497272200082X
