# Independent mathematical audit

## correctness

PASS

Scaling by d multiplies G by d^k, and p|A forces p∤B, so normalized values have no such prime factors. For active p, valuation is sum_{j<=e}(m_j-1), since p^j>k divides at most one progression term; m_j=floor((k+1)/p^j)+carry_j(n+BA^-1-1), with carry_j in {0,1} from base-p adding N=k+1. Each 2x2 transfer matrix correctly weights the outgoing carry, row sum p; the initial zero carry and final sum give the exact local PGF. If p^e divides N, all local carries vanish; otherwise the top carry is a proper nonempty residue interval and its p^e period cannot be canceled by lower carries with shorter period. Chinese remainder independence over the product of active prime-power periods yields the entire value PGF, moments and invariance under B. The k=0, noncoprime and constant-local-factor cases are explicitly consistent. Independently computed 436 complete-period direct LCM histograms for k<=12, a<=6, b<=5 and matched all probabilities; the general transfer/CRT proof handles arbitrary parameters.

## originality

PASS

Qualified best-of-knowledge PASS limited to explicit full joint value frequencies, compact carry-matrix PGFs, moments and progression-offset independence. Hong–Qian 2009 Eq.(3.2) already gives the prime-local excess-divisibility formula and Proposition 3.8 the least period; Ji–Ji 2009 generalize periodicity to polynomial progressions. These are strong relevant premises fully credited. Neither inspected open primary PDF states the carry-transfer value-frequency polynomial or global exact histogram/offset-invariance. The new result is a mathematically direct extension, so originality is incremental and could be superseded by an unindexed Farhi-function distribution study.

## value

PASS

The quotient of products by the lcm is a classical arithmetic function; its entire value law across a complete least period is a natural invariant beyond knowing the period. The transfer product is uniformly evaluable without enumerating a potentially huge period, yields exact moments and a nontrivial universality with respect to starting offsets and progression factors. This is a motivated complete distribution formula, not arbitrary parameter sampling.

The dated certificate retains the supplied scientific assessment, sources and limitations.
