# Magic positivity for all three-dimensional generalized parking-function polytopes

> **Review status: same-model review.** Correctness, originality and value were assessed by the same-model review, not an independent reviewer. Originality is claimed only to the best of our knowledge; consult `REVIEW.md` for search limitations. Publication is not peer review or a guarantee of priority.

## Claim

Let `a,b,c` be positive integers. Then the generalized parking-function polytope `X_3(a,b,c)` is magic positive.

Consequently, Conjecture 8.1 of Hill--Luo--Trinh--Vindas-Meléndez holds for every parameter vector of length three.

## Derivation

Write `L(b_1,...,b_n)=|X_n(b) ∩ Z^n|`. Hill et al.'s lattice-slice recursion gives in dimension two

`L_2(x,y) = (x+y)^2 - y(y+1)/2`.

In dimension three it specializes to

`L_3(x,y,z) = x L_2(x+y,z) + sum_{r=1}^y L_2(x+y-r,z+r) + sum_{r=1}^z L_2(x,y+z-r)`.

Expanding,

`6 L_3(x,y,z) = 6x^3 + 18x^2y + 18x^2z + 18xy^2 + 36xyz + 9xz^2 - 9xz + 5y^3 + 12y^2z - 3y^2 + 6yz^2 - 12yz - 2y + z^3 - 3z^2 + 2z`.

The Ehrhart polynomial is obtained from

`x=1+(a-1)t, y=bt, z=ct`.

Write the resulting cubic in the magic basis

`ehr(t) = mu_0(t+1)^3 + mu_1 t(t+1)^2 + mu_2 t^2(t+1) + mu_3 t^3`.

Put `A=a-1`, `B=b-1`, `C=c-1`, so `A,B,C >= 0`. Exact expansion gives

`mu_0 = 1`,

`6 mu_1 = 18A + 16B + 11C + 9`,

`6 mu_2 = 18A^2 + 36AB + 27AC + 27A + 15B^2 + 24BC + 22B + 6C^2 + 14C + 9`,

and

`6 mu_3 = 6A^3 + 18A^2B + 18A^2C + 18A^2 + 18AB^2 + 36ABC + 36AB + 9AC^2 + 27AC + 18A + 5B^3 + 12B^2C + 12B^2 + 6BC^2 + 12BC + 7B + C^3 + 3C^2 + 2C`.

Every displayed coefficient is nonnegative for `A,B,C >= 0`. Hence all four magic coefficients are nonnegative.

## Reproducibility

`artifacts/verify.py` derives `L_3` symbolically from the published recursion, performs the Ehrhart substitution, changes to the degree-three magic basis, and verifies the displayed shifted formulas exactly.

It also performs an independent lattice-point enumeration from the defining inequalities for every `1 <= a,b,c <= 5` and `1 <= t <= 4`, for 500 parameter/dilation cases, with no discrepancy.

The script additionally recovers the published spot check

`ehr_{X_3(3,2,2)}(t) = 172t^3 + 84t^2 + 15t + 1`

with magic coefficients `(1,12,57,102)`, and the coefficients `(1,59/6,115/3,54)` for `(a,b,c)=(2,3,1)`.

## Prior work and scope

The primary source is Hill--Luo--Trinh--Vindas-Meléndez, arXiv:2607.15503. Their paper proves the special two-parameter family `X_n(a,b,...,b)`, leaves arbitrary parameter vectors open, reports computational checks for all triples with coordinates in `{1,2,3,4}`, and states Conjecture 8.1 asserting magic positivity in general.

The source report also checked neighboring results on stable partial permutohedra, Pitman--Stanley polytopes, and sufficiently-large type-Y generalized permutohedra. None was found to imply the arbitrary three-parameter theorem.

To the best of the same-model review's searches through 17 September 2026, no subsequent proof of the complete length-three case was found.

## Consequence and value

This replaces finitely checked triples in the first open dimension by all positive triples. The source report also noted the standard consequence that magic positivity implies real-rootedness of the corresponding `h*`-polynomial, hence log-concavity and unimodality in this family.

## Limitations

The originality assessment is qualified. Because the proof is short once the dimension-three recursion is written down, independent discovery in a recent unindexed manuscript or private draft is plausible. No independent review is claimed.
