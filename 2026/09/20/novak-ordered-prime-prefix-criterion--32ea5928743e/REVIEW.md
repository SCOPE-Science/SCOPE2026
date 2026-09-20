# Same-model review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

PASS.

The ordered-prime necessity argument was rederived from multiplicative orders. If p divides a Novák number n and t=ord_p(2), then 2^n=-1 mod p implies t=2d with d|n; because t|p-1, every prime divisor of d is smaller than p. For the least prime factor this forces d=1 and p=3. For any later prime p_i, d divides the preceding increasing-prime prefix, whose quotient by d is odd, giving p_i | 2^{N_{i-1}}+1.

The converse was checked separately by induction with odd-power divisibility and LTE: adjoining any positive power of a new prime p dividing 2^M+1 to a Novák prefix M preserves the defining divisibility. This also proves that all increasing-prime prefixes are Novák.

The primitive two-prime criterion was checked against the Bailey--Smyth definition. Exponent b>1 is reducible to a smaller Novák number with the same prime support. For b=1, reducibility is equivalent to q having appeared at an earlier 3-power level. For q>3, the first-occurrence condition is equivalent to q dividing Phi_{2*3^a}(2), since the gcd of the successive quotient x^2-x+1 and x+1 divides 3. The resulting order is exactly 2*3^a.

For infinitude, v_3(Phi_{2*3^a}(2))=1 and the cyclotomic value exceeds 3 for every a>=2, so there is always a prime q>3 at each level. The elementary size estimate used for P_2(x) was checked at the smallest level a=2 and is monotone thereafter.

The bounded verification in `artifacts/verify.py` found zero mismatches both for every odd n<=10^6 and for 431,568 two-prime parameter triples.

## Originality

PASS, qualified as to the best of our knowledge.

The closest source is Bailey--Smyth, *Primitive solutions of n | 2^n + 1*. Its complete two-page note was inspected. It proves the least-prime result, gives a restriction based on the exact 3-adic exponent, defines primitive solutions, and develops finite divisibility filters, but it does not state the full ordered-prime prefix iff criterion or an infinitude theorem for primitive two-prime solutions.

Kalmynin, *On Novák numbers* (arXiv:1611.00417; Sbornik Math. 2018), was inspected in full HTML. Lemma 5 proves the forward extension mechanism used in the sufficiency direction, while the paper's main results concern counting Novák numbers, Novák primes, and Novák-Carmichael numbers. No ordered-prefix converse or two-prime primitive classification was located.

OEIS A006521, A136473, and A136475 were checked. A136475 explicitly tabulates prime factors of the successive quotients Phi_{2*3^a}(2) and explains their usefulness for fast generation. Thus the cyclotomic factors themselves and their computational role are known; the claimed new content is the exact structural characterization and its primitive/infinite consequences, not the factor table.

Searches also covered synonymous formulations based on "solutions of n dividing 2^n+1", ordered prime factors, two-prime support, primitive solutions, cyclotomic quotients, and later recurrence-divisibility literature. No equivalent theorem or stronger directly specializing theorem was located. The current SCOPE archive was searched for Novák/Novak, A006521, and n|2^n+1 terminology, with no overlap found.

Residual risk remains from Břetislav Novák's original and older Czech/recreational literature, which was not fully inspected, and from general results on self-divisibility in recurrence sequences that could encode the same prefix statement in a different language. Because the proof is elementary, this hidden-prior-art risk is material enough to state explicitly, but no concrete evidence of prior coverage was found.

## Value

PASS.

The main theorem converts a global congruence modulo n into a canonical chain of local congruences attached to the increasing prime-power prefixes of n. It shows that every Novák number has all of those prefixes inside the Novák set and gives a unique recursive generation rule by increasing prime support. The two-prime specialization is complete for all exponents and yields an unconditional infinite family of primitive solutions, together with a simple explicit lower bound for their counting function. These conclusions are structural rather than a new finite numerical record.
