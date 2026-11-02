# Scientific review

## Correctness — PASS

The sixth-order character indicator selects precisely the nonsquare cubes for every admissible prime power. The fully expanded product has one main term, 15 one-factor terms, 75 two-factor terms and 125 three-factor terms; their complete character sums are controlled respectively by zero, the one-root Weil bound and the two-root Weil bound. Excluding the three forbidden zero-shift points contributes the explicit correction \(15\cdot2+75\), proving \(216N(q)\ge q-108-325\sqrt q\). Strict positivity at and above \(105841\) is verified by exact squaring. The finite checker validates all 5037 relevant primes and 77 relevant nonprime powers below the cutoff; missing prime powers are explicitly detected, and every negative case is exhaustively checked. This is a genuine proof of an infinite statement, not a numerical extrapolation. Risks: implementation trust for the finite remainder and reliance on the standard Weil bound, as disclosed.

## Originality — PASS, subject to priority risk

Cohen (2026, full article Sections 1, 5 and 7) classifies pairs and poses the triple NSNP problem. The 1962 Lehmer et al. theorem treats triples of cubic residues but not the nonsquare sixth-coset condition or extensions; \(q=97\) shows the strict gap. Gun et al. (2007, full article Theorem 1) prove asymptotic existence for the broader non-square/non-primitive class at primes, not an exact exception list for this coset. Searches for sixth-power coset triplets and corresponding exceptional fields found no equivalent published-finding corpus record or accessible published table. Residual risk: the Buell--Hudson (1986) article on even-power-residue runs could imply some cases, and its full text was not accessible. At orders \(q\equiv7\pmod{12}\), negation explicitly identifies the NS3 coset with sixth powers; this possible partial overlap is acknowledged, not treated as disproved. No independence or unqualified priority is asserted.

## Mathematical value — PASS

A complete all-prime-power existence classification for a prescribed natural sixth-power coset answers a sharper structural question motivated by Cohen's exact pair theorem and his explicit triple question. It distinguishes stronger NS3 constraints from cubic-residue triples and from generic NSNP triples. The 35 exceptional orders include seven proper extensions and are proved complete, not merely observed; this exact classification and uniform analytic tail are a natural finite-field arithmetic invariant. The result makes no claims about the remaining NSNP triples or counts of witnesses.

## Closest literature and limitations

- Cohen (arXiv:2604.21429v1): exact pairs, not NS3 triples.
- Lehmer et al. (1962): cubic-residue triples, weaker membership predicate and prime fields only.
- Gun et al. (2007): general QNRNP strings for sufficiently large primes, not this exact sextic coset census.
- Buell--Hudson (1986): plausible older partial or stronger implication; only abstract accessed.

The theorem and verifier are reproducible. Priority remains open to independent checking and the finite-field verifier is not a formal independent audit.

Self-review: passed. Independent audit: not yet performed.
