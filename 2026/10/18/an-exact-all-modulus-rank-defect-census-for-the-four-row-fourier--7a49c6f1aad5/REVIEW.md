# Scientific review of the Fourier rank-defect census

## Correctness — PASS
The statement is precise for every integer \(N\ge5\), four distinct columns, and unnormalized complex Fourier rows \(\{0,1,3,4\}\). A generalized Vandermonde factorization reduces singularity to a six-root vanishing sum. The complete minimal-root classification of Poonen and Rubinstein yields only the three partitions \(2+2+2\), \(3+3\), and primitive \(6\). Graph-edge incidence forces the first two configurations, while a unique opposite-edge matching in the primitive relation leaves exactly two thirtieth-root translation orbits. Inclusion-exclusion gives the all-order formula, and a degree-four polynomial argument shows every singular minor has rank three. The verifier additionally checks the determinant polynomial identity; exact cyclotomic verification covers nineteen finite orders; it is evidence, not an infinite proof.

## Originality — PASS (best-knowledge comparison)
The 2021 continuous-array paper by Matter and collaborators already studies this exact Schur polynomial and the root-sum families, including eight normalized primitive exceptional configurations. The determinant and continuous ambiguity mechanisms are **not original** here. The narrower accepted claim is the all-\(N\) arithmetic census of unordered Fourier-column selections, overlap correction at \(4\mid N\) and \(6\mid N\), the isolated \(30\mid N\) contribution \(2N\), and rank-three completeness. The closest known published same-row theorem decides full spark, not positive defect counts; the row pattern \(\{0,1,2,4\}\) has a different enumeration. A previously unindexed count extracted from the continuous paper is the main residual bibliographic risk.

## Mathematical value — PASS
The fixed pattern is already a standard counterexample to divisor-uniformity sufficiency for full spark. Computing how many four-column apertures fail, rather than merely whether one fails, provides a natural exact reliability invariant of that harmonic frame. Its unexpected primitive-thirtieth-root jump and precise cross-family overlaps are not obtainable from the binary full-spark criterion. The theorem is a natural complete classification and exact enumeration, not an arbitrary parameter slice or minor numeric increment.

## Limitations and evidence
Sources: Poonen–Rubinstein, arXiv:math/9508209, Theorem 3; Matter–Fischer–Pesavento–Pfetsch, arXiv:2110.10756, Example V.1; Alexeev–Cahill–Mixon, arXiv:1110.3548, composite-order counterexample; subsequent published same-row full-spark and different-row defect results. The verifier performs exact integer arithmetic but covers only its listed orders. An independent literature or mathematical audit remains outstanding.

Self-review: passed. Independent audit: not yet performed.
