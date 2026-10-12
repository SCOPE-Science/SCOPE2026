# Scientific review: exact normalized Jacobsthal quotient gcd

## Correctness — PASS

A complete algebraic proof is given in `RESULT.md`. The identities \(J_{3n}=J_nC\), \(J_{9n}=J_{3n}E\), and \(J_{27n}=J_{9n}F\) follow by difference of cubes. For \(3\nmid n\), \((-8)^n\) is a nontrivial third root of unity modulo \(19\), so \(57\mid E\); and \(3\mid C,F\). Substituting proves that both normalized quotients are integers and share \(H_n=E/57\) as a factor. The exact congruence \(F\equiv3\pmod C\) forces \(\gcd(C,F)=3\), so their remaining factors are coprime and the gcd is exactly \(H_n\). The unbounded index restriction and \(n=1\) boundary are explicit. Reproducible exact-arithmetic checks of 267 admissible indices supplement the symbolic proof, not replace it.

## Originality — PASS, subject to stated bibliographic risk

Panraksa--Tangboonduangjit (2022), equation (4) and Theorem 7, study the same normalized quotient, but the strong-divisibility theorem requires indices coprime to the discriminant \(9\). The pair \((n,3n)\) lies outside that hypothesis. Yildiz (2022) covers divisibility of Jacobsthal terms, not this quotient gcd. Sanna (2016) supplies broader valuation machinery, and Ballot (2018) treat Lucasnomial quotients, but neither inspected source presents the explicit coprime factorization or exact \(n\)-versus-\(3n\) gcd. OEIS A396358 concerns a different quotient. The residual risks are an unindexed equivalent and possible implicit derivation from general term-valuation formulas; the checked statements do not directly cover the specific formula.

## Mathematical value — PASS

The result completes the exact gcd for an infinite, natural first-excluded family of the focal almost-strong-divisibility theorem, not a deliberately chosen finite slice. It proves a structural coprime decomposition with an explicit common factor and pinpoints the exact factor that disappears at the next local index layer. The result establishes universal failure of \(T_n\mid T_{3n}\) for every admissible \(n\ge2\), rather than an isolated negative example. No extension to arbitrary pairs or other Lucas families is asserted.

## Remaining scientific limits

The theorem is confined to the Jacobsthal specialization and the index pair \((n,3n)\) with \(3\nmid n\). The standalone verifier performs finite exact checks, not external or independent certification. A fully independent audit has not been performed.

Self-review: passed. Independent audit: not yet performed.
