# Scientific review

## Correctness — PASS

Every \(\mathbb F_q\)-linear derivation on a full matrix algebra is reconstructed from matrix units as an inner derivation. Its scalar-generator ambiguity is proved, so counting conjugacy classes of matrices without quotienting by scalars is explicitly avoided. In odd characteristic, opposite differences of generator eigenvalues force a single eigenvalue, whose nilpotent residue makes the idempotent derivation vanish. In characteristic two, the exact identity \(\operatorname{ad}(A)^2=\operatorname{ad}(A^2)\) reduces idempotence to \(A^2+A=cI\), followed by a disjoint Artin–Schreier split/nonsplit dichotomy. The projections are counted by image/complement, with a two-to-one correction only at middle rank. The nonsplit conjugacy orbit is counted by its \(\mathrm{GL}_m(q^2)\) centralizer, with the separate two-to-one scalar correction. Direct finite-field brute-force verification on six matrix spaces agrees with all displayed coefficients. The proof, not the finite tests, supports the unrestricted claim.

## Originality — PASS, with residual risk

A source-focused comparison against Ashraf–Ansari–Akhter [1], Bai–Gao–Li [2], classical projection enumeration, and relevant published mathematical-result records found neither the stated finite-field derivation rank polynomial nor its nonsplit orbit interpretation. [1] explicitly assumes two-torsion-freeness, and [2] works over \(\mathbb C\), so their theorem statements cannot imply the characteristic-two branch. The result does rely on the standard innerness and finite-field conjugacy machinery; those ingredients are not claimed as new. The literature search is nonexhaustive, and an alternate description through semisimple adjoint operators could predate this formula.

## Value — PASS

The composition-idempotent condition is intrinsic to the derivation algebra, and its complete finite-field rank distribution distinguishes odd characteristic (only zero), the characteristic-two split matrix-projection sector, and the quadratic-extension sector that exists precisely in even matrix sizes. The exceptional sector has an explicit Frobenius-semilinear image of dimension half the algebra and contributes a quantitatively nontrivial count; this is a structural classification of a natural operation space, not a single arbitrary parameter computation. The finite-field formula applies in every matrix dimension.

## Limitations

The classification is for associative linear derivations, not all Lie derivations of \(\mathfrak{gl}_n\). The checker verifies selected small fields and cannot establish an infinite statement. Published work not indexed under the same terminology may contain an equivalent classification. Independent review has not occurred.

Self-review: passed. Independent audit: not yet performed.
