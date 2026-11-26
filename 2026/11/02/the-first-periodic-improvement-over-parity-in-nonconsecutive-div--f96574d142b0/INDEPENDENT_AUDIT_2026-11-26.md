# Independent mathematical audit

## correctness

PASS

For fixed m, count pairs ab <= X with ab congruent to r modulo m by the divisor hyperbola split. For a <= sqrt(X), the count in b is X gcd(a,m)/(am) + O(1) if gcd(a,m) divides r, and zero otherwise. Doubling this count and subtracting the common square costs O(X) outside the main term. The harmonic sum of the periodic function gcd(a,m) times the divisibility indicator has leading coefficient its mean. The resulting X log X weight is m^(-2) times the sum of gcd(a,m) over a modulo m for which gcd(a,m) divides r. CRT factors this mean. For p^a the terms with valuation k<a each contribute a total p^(a-1)(p-1) when k <= v_p(r), and the zero class contributes p^a if p^a divides r. This proves precisely the two frozen weights and handles the infinite-limit step without a tail interchange. In the finite optimization, conditioning on the first vertex ensures the end constraint is checked, and the last-selected/not-selected recurrence exhausts the remaining path choices; for m=1 the cyclic rule forbids the sole vertex. Independent exact calculation through 90 confirms no strict gain for m<90 and optimum 2040/2700 at 90, with the stated swap (63-24-24) improving 2025 to 2040. The finite reproduction and analytic asymptotic are separate checks.

## originality

PASS

The analytic divisor weights and cycle optimization are standard, but the inspected closest work does not determine the first exact period crossing or its optimum. Pass is limited to that fixed-period extremum, not a historical priority claim.

## value

PASS

Parity supplies a canonical selector and a natural mass benchmark. The theorem identifies the minimum cyclic period needed to improve it, and an explicit local exchange explaining how the first improvement occurs. This sharp barrier is necessary information for optimizing simple periodic constructions and is more than a small numerical gain or an arbitrary finite slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
