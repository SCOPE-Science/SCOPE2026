# Independent mathematical audit

## correctness

PASS

The prefix recurrence splits admissible tuples according to whether they use the last index; a nonempty preceding prefix pattern can extend only from the prefix two positions back, with no such contribution at the first index. I independently reproduced the complete census in audit_deck.py using a different signature. For each pattern length k, count tuples whose designated slots are all ones, leaving other slots unconstrained. These 2^k moment counts are the Boolean zeta transform of the exact pattern counts and can be inverted, so grouping by these moments preserves the fibers. Zero-based admissible indices i_j arise bijectively from increasing indices m_j in range(n−k+1) by i_j=m_j+j. For all 2^n words at each n=1,…,13, exact integer grouping gives the sole length-two collision {01,10}, injectivity for 3≤n≤12, and 8184 singleton plus four doubleton fibers at n=13. The discovered doubletons agree word for word with the frozen table; each consists of two reversals and complementation interchanges pairs in two distinct orbits. A maximum labeled code chooses one word per fiber, so its size is 8188 and its count is 2⁴=16.

## originality

PASS

The separation-two deck through length three is exactly the deck of Golm et al. for k=3. Their nondegenerate threshold 13 and their example, the last pair in the frozen table, are prior work; the table explicitly labels its pairs as examples. The distinct content supported here is the complete length-13 histogram and exact list of all four classes, not the threshold or the known example. These are fully duplicated in a later Resultary catalogue record, also including the codebook consequences. The later-dated overlap is not evidence of earlier priority, and dates and matching statements alone do not establish provenance.

## value

PASS

Length 13 is motivated by the published first nondegenerate loss of reconstruction, not an arbitrary cutoff. The complete census determines precisely how badly reconstruction fails at that boundary: only eight words are affected, there are no higher-multiplicity obstructions, and the four pairs show the exact symmetry of the failures. The fiber census also gives the sharp zero-error code size and choices of optimum codebook. These last deductions are simple consequences, not a separate structural contribution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
