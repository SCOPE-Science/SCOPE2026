# Independent mathematical audit

## correctness

PASS

The cases n=1 and n=2 give respectively (0,1) and (1,1) for the aliquot sums. Mixed prime/composite entries cannot agree because primes have aliquot sum 1 whereas composites have a proper divisor greater than 1; (2,3) is the only pair of adjacent primes. Independently, if both entries are composite with Ω=2, the even entry cannot be 4, whose neighbours are prime. It is thus 2q with q an odd prime and s(2q)=q+3 even. An odd squarefree semiprime has odd aliquot sum, so the odd member must be an odd prime square p². Equal sums give p=q+2, but p²−2q=q²+2q+4>1, excluding either orientation. This verifies the frozen unbounded theorem independently of its algebraic case split. A separate replay (python /workspace/checks/adjacent_audit.py) accumulated proper divisors by their multiples and counted Ω via prime powers. For 1≤n≤200000 it found 8042 eligible pairs and only n=2 with equality, matching the packaged output; this is corroboration only.

## originality

PASS

No inspected claim gives the unrestricted-in-size low-multiplicity classification for proper divisor sums. The same-equation sources give the unrestricted question or longer-run statements; the nearest same-depth classifications use different arithmetic functions. The inaccessible MathOverflow discussion remains an explicit risk rather than negative evidence.

## value

PASS

The paper explicitly isolates the unrestricted consecutive aliquot-sum question. This result excludes an entire natural first multiplicative layer, including prime squares and repeated factors, at every size. A researcher looking for further solutions can therefore rule out both-low-depth candidates on structural rather than numerical grounds.

The dated certificate retains the supplied scientific assessment, sources and limitations.
