# Self-review

## Correctness — PASS

The theorem is quantified for every prime, extension exponent, and odd index. The integer \(b=(q^{n-1}-1)/(q+1)\) is integral, and \(b\equiv-1\pmod p\). The pole-weight inequality explicitly establishes that the witness is a regular differential. The Cartier formula follows by expanding \(y^{j_0}=(y^{q^2}-x^m)^{j_0}\), with the unique nonzero binomial term selected by the exponent congruence; the coefficient of every transition in the witness chain is a nonzero unit. The calculation produces \(\mathcal C^{tn-1}(\omega)=-dx\ne0\). The upper bound uses maximality of the stated family and Garcia--Tafazolian Theorem 3.3, both stated with their exact extension field. The completed checker verifies the rules and chain on multiple finite cases, but numerical checks are explicitly not proofs of infinite quantified claims. Risks: the upper bound depends on the cited maximality theorem, not a new elementary computation; there is no claim about intermediate ranks.

## Originality — PASS (historical priority qualified)

Shafighi's original full manuscript gives a basis and computes the single Cartier rank (equivalently the \(a\)-number), not the last nonzero iterate. Garcia--Tafazolian gives \(\mathcal C^{tn}=0\) for maximal curves but no matching nonvanishing. The explicit witness establishes the missing converse for this family. The 2026 work of Almeida Filho--Tafazolian--Vieira does compute sharp nilpotency but for a different family \(y^p-y=xR(x)\), not \(y^{q^2}-y=x^m\); Groen's Artin--Schreier cover results similarly concern degree-\(p\) coverings. Published-record searches for equation aliases, nilpotency, higher Cartier powers and exact Serre-type indexes found no equivalent or stronger covering result. No finite search can prove global priority. Residual risk: a general theorem for monomial additive covers or a reinterpretation of an earlier Cartier calculation could imply the result without matching terminology.

## Mathematical value — PASS

The exact nilpotency exponent is a global geometric invariant of the Cartier action, finer than the already known \(a\)-number and a direct sharpness test for the field-of-maximality bound. The formula is uniform in all primes, all powers of the characteristic, and all allowed odd indices; it supplies a canonical explicit terminal differential rather than an isolated computational example. It also gives a nonzero last higher Cartier rank in a natural family of maximal curves, aligning with questions currently studied in higher-Cartier-rank literature.

## Scope and closest literature

Sources: Shafighi, arXiv:2610.15266v1 (full manuscript, definition, basis, Cartier rule and main a-number result); Garcia--Tafazolian, *Acta Arith.* 135 (2008), Theorem 3.3 (full article); Almeida Filho--Tafazolian--Vieira, arXiv:2610.17476v1 (full introductory and main-results sections); Groen, arXiv:2208.06504 (higher Cartier-power statements). The source on maximality is Abdón--Bezerra--Quoos (2009), as cited by Shafighi. The result has not undergone independent validation.

Self-review: passed. Independent audit: not yet performed.
