# Independent mathematical audit

## correctness

PASS

Replacing each ordered prime by the corresponding first-seven prime at fixed exponents weakly increases sigma(n)/n and strictly decreases C_7 if any prime changes. The reduced integer remains above 5040 because the seven-prime primorial is already above it. C_7 is strictly increasing (positive argument and positive derivative of P_7). The Euler-factor bound is 17017/3072; the independent interval evaluation gives C_7(52000000000)>5.7095380290666298, larger than that bound plus 0.1691. I independently enumerated the reduced candidates by starting at the primorial and adjoining prime factors in nondecreasing order; unique factorization gives exactly one visit to each tuple up to the cutoff. An integer fixed-point replay, /workspace/branches/review-4-integer-replay.py, uses rational Euler–Maclaurin bounds at N=4096, logarithms by the atanh series with power-of-two reduction and a geometric tail bound, and a bounded exponential series. It verifies all 2596 tuples: the candidate gap is enclosed between 0.1690334982267305186 and 0.1690334982267306759, the ratio is exactly 62496/12155, and every other reduced tuple has lower interval endpoint above 0.1691 (the smallest such endpoint exceeds 0.18329). Together with the strict support reduction and tail, this proves the global unique minimum. The frozen checker and recorded output were inspected, not executed.

## originality

PASS

The supported distinct result is the sharp uniform additive gap and its unique optimizer at exactly seven distinct prime factors. The parent inequality and the optimizer's appearance under other divisor-extremal criteria are not new. The inspected statements do not supply or mechanically imply the sharp gap for the stated objective.

## value

PASS

Seven is the first support size beyond the predecessor's analytic small-support range, so the slice is motivated by the existing argument. The exact worst case gives a certified uniform additive allowance for this truncation in that layer, not just a sign or a numerical estimate at a famous integer. A researcher comparing truncations or improving the finite checks can use both the tolerance and its unique obstruction. No wider Robin or Riemann-hypothesis implication is asserted.

The dated certificate retains the supplied scientific assessment, sources and limitations.
