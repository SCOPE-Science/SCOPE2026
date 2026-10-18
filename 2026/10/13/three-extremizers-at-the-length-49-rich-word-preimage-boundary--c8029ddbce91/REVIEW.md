# Independent mathematical audit

## correctness

PASS

For f(0)=0,f(1)=01,f(2)=011 and required ternary prefix 0121012, consider all preimages u for which f(u) is palindromically rich and avoids every exponent >=14/5. Both properties are hereditary under taking prefixes: forbidden powers persist and palindromic defect is nondecreasing under appending a letter. Every extension therefore belongs to a finite prefix tree whose root is 0121012 and alphabet branches 0,1,2, and pruning never removes a valid descendant. Independently written incremental palindrome-suffix and forbidden new-suffix tests produced level survivor counts n=47:11,48:6,49:3,50:0, proving the maximum 49 and the exact three stated words with common 47-letter prefix. Independent final full palindrome-factor and period tests found binary image lengths 94,95,96, all rich, with critical exponents 46/17,46/17,95/34 (each <14/5). The complete level-by-level enumeration through 50, not an arbitrary cutoff or timeout, certifies the exhaustiveness, subject to the elementary hereditary proof.

## originality

PASS

Currie–Mol–Rampersad (2020) Table 1 already gives the numerical maximal length 49 for the exact prefix 0121012 in their infinite-rich-word obstruction analysis; that scalar cutoff is explicitly prior. The later Currie–Rampersad 2024 proof, Lemma 5, reuses the same forbidden factor among backtracking exclusions with length-50 cutoff. Accessible primary pages include the 2020 Table 1 and 2024 Lemma 5 and show no complete identities/multiplicity of the length-49 surviving preimages. New content is the three-word equality-case census and common-prefix rigidity, not the cutoff, theorem on infinite rich words or a new repetition threshold. Searches for exact full strings and alias eligibility terminology found no published equality table, but unpublished authors' search outputs remain a material priority risk.

## value

PASS

This finite equality-case classification is naturally motivated: the length-49 row is the *largest* finite obstruction length in a published structure-theorem proof, so every longest legal preimage at that bottleneck has structural significance. The three explicit maximizers and their forced common 47-letter prefix refine a published bound by uniquely identifying how boundary obstruction manifests. Value does not depend on extending the overall infinite repetition-threshold theorem, and the exhaustive certificate is nontrivial rather than a tiny arbitrary binary-word census.

The dated certificate retains the supplied scientific assessment, sources and limitations.
