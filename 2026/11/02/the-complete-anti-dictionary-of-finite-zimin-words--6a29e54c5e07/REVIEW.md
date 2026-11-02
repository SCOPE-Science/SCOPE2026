# Scientific review of the complete Zimin anti-dictionary

## Correctness

**PASS.** The claim concerns literal contiguous factors in \(Z_n\) over exactly \(\Sigma_n\), for every integer \(n\ge1\). The ruler-position lemma fixes the starts of embedded \(Z_m\); it yields a complete prefix-continuation classification and a complete border classification. Uniqueness of the highest letter then exhausts every possible new minimal absent factor as the alphabet grows. The proof counts disjoint endpoint pairs and derives both the sparse length spectrum and the cubic total. The checker independently constructs all proper-factor-supported absent words through rank nine and compares their full sets with the proposed classification. Finite checks are not used as the infinite proof.

## Originality

**PASS, subject to historical-priority risk.** Głowinski and Rytter (arXiv:1307.1560) give a general membership criterion for factors of Zimin words and compressed pattern-matching methods, not an explicit closed list of minimally missing literal factors. Rytter and Shur (arXiv:1409.8235) establish Zimin-type and pattern-searching results rather than the literal anti-dictionary. Barton et al. (2014, DOI 10.1186/s12859-014-0388-9) give general minimal-absent-word enumeration algorithms, not the Zimin-specific index-pair formula or counts. Search variants using “anti-dictionary,” “minimal absent word,” and “minimal forbidden factor” revealed no directly covering statement. The broad factor-membership criterion could be used to *derive* the present classification and remains the closest potential implicit coverage; an unlocated equivalent result remains possible.

## Value

**PASS.** Minimal absent factors are the canonical obstruction set for the factor language of a finite word. The Zimin family is highly self-similar, uses a growing alphabet, and has exponentially increasing host lengths. The theorem determines that its entire obstruction set admits a succinct three-index description, is supported on precisely the lacunary lengths \(2^m+1\), and has an exact cubic count in rank. It supplies a nontrivial all-level structural benchmark for factor-recognition and compressed anti-dictionary algorithms rather than a single finite census.

## Scope and risks

The theorem is about finite linear words with literal, rank-dependent alphabets, not homomorphic Zimin-pattern matching. A related general factor criterion makes the originality judgment sensitive to possible earlier specializations; the inspected literature does not establish that this exact classification was previously recorded. No independent audit has been performed.

Self-review: passed. Independent audit: not yet performed.
