# Same-model scientific review

## Correctness
PASS. The equilibrium computation starts from the three vector-field equations and explicitly checks the singular value \(x=-1\) before dividing by \(1+x\). The factorization at \(a=1\) is exact. The key identity uses the polynomial
\[
F=x^2-2x-2y+2z
\]
and gives exactly
\[
\dot F=-2(x^2-x-b).
\]
For compactly supported invariant probability measures, integrating this Lie derivative is legitimate and gives the stated moment shell. The variance factorization and endpoint rigidity are exact. The crossing statement is restricted to non-equilibrium ergodic measures and nonconstant periodic orbits, avoiding the false extension to arbitrary mixtures of equilibrium measures; it also distinguishes the algebraic level \(x_-=-1\) from an equilibrium level at \(b=2\).

## Originality
PASS with residual bibliographic risk. The source full text was inspected at the model/equilibrium section: it gives \(y=x/(1+x)\), \(z=x^2/(1+x)\), the cubic \(ax^3-(b+1)x-b=0\), and the three-fixed-point statement, but it does not treat the singular \(a=1\) factor or stationary invariant-measure moments. Exact-title, DOI, \(a=1\), \(x^2-x-b\), invariant-measure, and stationary-moment searches did not locate the same theorem. Closest database records use analogous moment-balance methods for different chaotic flows and do not imply the Ray–Ghosh identity. A later five-dimensional hyperchaotic extension cites the source but studies a modified system and does not cover this claim in its accessible abstract.

## Value
PASS. The result repairs an equilibrium-count singularity exactly on a structurally distinguished constant-divergence slice and simultaneously produces a global, measure-level restriction on every compact recurrent statistical state. The shell and sign-crossing law constrain periodic or chaotic recurrence without relying on a numerical attractor computation, and the exceptional case \(b=2\) changes the actual equilibrium count from the cubic-root count in a concrete way.

## Closest literature and limitations
The primary source is Ray–Ghosh, arXiv:1911.11429v1 / doi:10.1142/S0218127420501618. Closest retrieved comparison records include exact stationary-moment or recurrence identities for the Rössler, Shimizu–Morioka, Rabinovich–Fabrikant, Burke–Shaw, and Rucklidge systems; these concern different vector fields. The search is not a proof that no unindexed statement exists. The theorem does not assert existence of a non-equilibrium compact invariant set at \(a=1\).

Same-model review: passed. Independent audit: not yet performed.
