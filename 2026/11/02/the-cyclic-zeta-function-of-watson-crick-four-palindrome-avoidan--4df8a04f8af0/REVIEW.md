# Scientific review: the cyclic zeta function of Watson–Crick four-palindrome avoidance

## Correctness — PASS

The claim has an exact, completely specified domain: labeled four-base circular words, each of whose cyclic four-windows is outside the sixteen reverse-complement palindromes, for every positive length. The triple-state overlap graph is in bijection with indexed periodic words, including periods shorter than four. The full characteristic polynomial of its 64-state adjacency matrix is established by Newton identities using all 64 exact integer traces; this is a finite symbolic determinant certificate rather than an extrapolation from checked coefficients. The formal determinant/logarithm identity proves the zeta function to all orders. Möbius inversion proves the primitive-necklace formula. Exact graph reachability and the self-loop give the Perron-Frobenius hypothesis for the asymptotic capacity. Replaying `verify.py` returned `VERIFY_OK`. Limited tests of short words are independent cross-checks, not the basis for the general proof.

## Originality — PASS, qualified

The known binary alternate-complement transformation and the general de Bruijn transfer construction are credited and are not claimed as discoveries. The published secondary-structure-avoidance results of Chu, Wang, and Zhang concern a strictly stronger constraint forbidding remotely separated reverse-complementary factors and do not evaluate this local circular-word determinant. Lamprea-Burgunder, Ludin, and Mäser identify the sixteen four-mer palindromes empirically rather than enumerate all admissible circular words. The closest related cyclic palindrome study by Simpson maximizes distinct palindrome complexity, not this avoidance zeta function. Comparison by statements and implications finds no inspected result stating this four-base cyclic factorization or all-period primitive-necklace formula. The standard transfer method can in principle compute the special case and an unindexed prior explicit computation remains possible; the originality claim is therefore qualified rather than absolute.

## Mathematical value — PASS

Avoidance of all sixteen Watson–Crick palindromic tetranucleotides is a canonical finite-alphabet constrained language with an empirical genomic motivation. Its exact cyclic period spectrum and complete primitive-orbit enumeration are meaningful invariants for circular DNA and symbolic coding. The non-obvious factorization of a 64-state system yields all lengths at once and an exact rate, rather than a small-table extension. The answer is deliberately restricted to local four-mer avoidance, which is not a model of all stem-loop secondary structures.

## Closest literature and limitations

See the References in `RESULT.md`. The strongest potential prior overlap is the generic transfer-matrix prescription in the April 2023 MathOverflow discussion; it does not itself give the evaluated quaternary cyclic determinant. The 2023 SSA paper's full accessible mathematical sections were compared for the same constraint and capacity, and the 2011 genome-frequency article's motif definition and counting sections were inspected. A previously unindexed equivalent evaluated factorization cannot be categorically excluded. The present review does not constitute independent external validation.

Self-review: passed. Independent audit: not yet performed.
