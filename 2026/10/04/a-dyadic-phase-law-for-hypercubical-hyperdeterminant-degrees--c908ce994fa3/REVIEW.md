# Same-model review

## Correctness
PASS. The exact coefficient identity
\[
H_d
=
d!\sum_{j=0}^{d}(d-j+1)\frac{(-2)^j}{j!}
\]
is stated in the inspected full-text source. Legendre's identity gives
\[
\nu_2\!\left(\frac{2^j}{j!}\right)=s_2(j).
\]
For even \(d\), only the \(j=0\) term survives modulo \(2\), proving equality with the factorial valuation. For odd \(d\), every \(j\ge2\) term vanishes modulo \(4\), so the normalized factor is congruent to \(1-d\) modulo \(4\). This proves exact excess one for \(d\equiv3\pmod4\) and excess at least two for \(d\equiv1\pmod4\). The Frobenius ED degree \(d!\) is independently stated in the same source.

The bundled checker independently replays the recurrence, coefficient formula, and valuation cases over finite ranges, but those checks are not used as an infinite proof.

## Originality
PASS. The closest full-text literature gives the complete degree generating function and studies asymptotics; the public sequence record supplies the exact recurrence and a weaker permanent divisibility theorem. Neither inspected source states the residue-sensitive \(2\)-adic phase law. Searches using geometric, sequence, parity, divisibility, and factorial-baseline formulations found no covering statement.

The original 1992 hyperdeterminant article could not be inspected in full and is therefore retained as a genuine residual risk rather than being asserted not to cover the claim.

## Value
PASS. The result concerns a canonical projective-dual invariant of a fundamental tensor variety and directly compares it with another natural geometric invariant, the Frobenius ED degree. It identifies exactly when the two have the same dyadic valuation, when the hyperdeterminant has one extra factor of two, and when at least two extra factors are forced.

Same-model review: passed. Independent audit: not yet performed.
