# Review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

The inertia proof has two independent interlacing directions. Chen and Li give \(\operatorname{In}(W_k)=(\binom{k}{2}+1,0,k-1)\). Deleting \(t\) point vertices can reduce the positive inertia by at most \(t\) and cannot increase the negative inertia, so the point-deleted graph has at least \(\binom{k}{2}+1-t\) positive and at most \(k-1\) negative eigenvalues. The untouched 2-subset vertices induce \(KG(k,2)\), whose incidence-matrix decomposition gives exactly \(k-1\) negative eigenvalues. Interlacing from this induced subgraph supplies the reverse negative-inertia inequality. Counting the remaining eigenvalue slots then forces the positive count and zero nullity exactly.

The Kneser inertia is derived within the record from \(K=J+I-C^{\mathsf T}C\) and \(CC^{\mathsf T}=(k-2)I+J\), avoiding dependence on a spectral table. Connectivity and reducedness are checked directly from the Kneser and incidence neighborhoods. The finite verification artifact independently reconstructs all 51 graphs with \(5\le k\le10\) and all admissible deletion counts, confirming the theorem numerically in those cases; this corroboration is not used as a substitute for the general proof.

## Originality

Akbari--Elphick--Kumar--Pragada--Tang Problem 3.3 explicitly asks whether infinitely many reduced graphs attain equality in their proposed inertia bound. Chen and Li later construct the reduced graphs \(W_k\) with inertia \((\binom{k}{2}+1,0,k-1)\), thereby disproving that bound, and analyze the single deletion \(W_5-a_1\) to obtain inertia \((10,0,4)\).

The checked primary statements and targeted searches under graph inertia, reduced equality graphs, point/vertex deletion, \(W_k-a_i\), Kneser and Johnson terminology did not locate the general theorem \(\operatorname{In}(W_k-R)=(\binom{k}{2}+1-|R|,0,k-1)\), its full interval realization consequence, or the infinite one-point-deletion equality family. Recent work on non-positive inertia addresses a different asymptotic extremal question. Originality is therefore assessed as **to the best of our knowledge**. The main residual risk is very recent, unindexed, or differently termed work exploiting the same Chen--Li construction.

## Value

The result gives an exact \((k+1)\)-step inertia ladder inside a concrete recent family rather than a single isolated deletion. It answers the explicit infinite-family side of Problem 3.3 and, for each \(q\ge4\), realizes every nonsingular inertia \((p,0,q)\) with \(\binom q2\le p\le\binom{q+1}{2}+1\) by a connected reduced graph. The one-point deletion sits exactly on the former proposed boundary for every \(q\ge4\), while the undeleted Chen--Li graph lies one positive eigenvalue above it.

## Limitations

The theorem does not restore an extremal upper bound after the original conjecture was disproved, does not determine the true maximum positive inertia for fixed negative inertia, and does not classify all reduced equality graphs. No uniqueness is claimed for the point-deletion construction. The numerical census is only corroborative. The originality claim remains to the best of our knowledge.
