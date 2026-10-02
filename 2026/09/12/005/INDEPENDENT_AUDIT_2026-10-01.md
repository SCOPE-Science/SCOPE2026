# Independent mathematical audit — SCOPE-20260912-005

Outcome: **PASSED**.

## Correctness

**PASS** — The projection class computation gives M=(-3,2,-3), with Euler square -2. At beta=-1/2 the imaginary part is 10 n1+5 n0, hence always in 5Z, while Im(M)=5. A finite-slope Jordan-Hoelder decomposition would require two strictly positive imaginary parts summing to 5, impossible. I independently recomputed the HRR scalar, class, Euler pairing and divisibility argument.

## Originality

**PASS** — Resultary returned this record but no earlier SCOPE statement with the same line-projection class and beta=-1/2 numerical divisibility exclusion. The primary GM stability literature inspected develops the Kuznetsov lattice and wall-crossing framework, but the searched full texts did not state this exact numerical ray exclusion or a theorem whose implication is precisely this no-numerical-splitting statement.

Equivalent formulations: At beta=-1/2, the imaginary-part homomorphism on the integral numerical lattice is 5 times an integer and M has minimal positive value 5.

Broader coverage: No inspected source gave a stronger theorem implying this exact no-numerical-splitting ray.

Database/table comparison: Resultary top-30 semantic search: exact record only among directly matching GM line-wall statements.

Claim-vs-prior implication: Resultary returned this record but no earlier SCOPE statement with the same line-projection class and beta=-1/2 numerical divisibility exclusion. The primary GM stability literature inspected develops the Kuznetsov lattice and wall-crossing framework, but the searched full texts did not state this exact numerical ray exclusion or a theorem whose implication is precisely this no-numerical-splitting statement.

## Value

**PASS** — Although short, the lemma removes an entire vertical numerical wall ray for the natural line-projection class and is directly motivated by Bridgeland stability calculations. It is a reusable boundary check rather than an arbitrary arithmetic slice; the result carefully stops short of claiming object existence or global stability.

## Source inspections

- **Jacovskis-Liu-Zhang, Brill--Noether theory for Kuznetsov components..., arXiv:2207.01021** — Material read: full HTML, especially numerical Grothendieck lattice and wall-computation sections. Finding: establishes the GM/Fano Kuznetsov lattice and related wall machinery; no exact M=(-3,2,-3), beta=-1/2 divisibility exclusion located.
- **Jacovskis-Lin-Liu-Zhang, Categorical Torelli theorems for Gushel-Mukai threefolds, arXiv:2108.02946v4** — Material read: full HTML, stability-condition and beta=-1/2 passages. Finding: contains Serre-invariant stability arguments in the same GM setting, but not the exact numerical line-projection ray statement.
- **Resultary semantic search** — Material read: top 30 results for GM numerical wall exclusions. Finding: exact hit was this record; no prior SCOPE hit with the same statement/implication.

## Residual risks

- No exact phrase match in the primary literature was treated as novelty proof; originality rests on statement/implication comparison plus Resultary and full-text inspection.
- The claim remains only a numerical wall exclusion; object existence and Bridgeland transfer are not proved by this lemma.
