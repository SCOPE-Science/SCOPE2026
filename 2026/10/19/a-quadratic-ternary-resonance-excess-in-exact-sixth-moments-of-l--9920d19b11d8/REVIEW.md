# Independent mathematical audit

## correctness

PASS

The frozen RESULT.md line 28 and SLOGAN.txt are false: at n=2 the actual moments are 1301 and 1001, giving 300, not 540. The complete replacement files in /workspace/repairs/5/ retain the correct moments and give E_3(n)-E_6(n)=60(4n^2-5n-1) for n>=2, with zero excess at n=1. Independently, six-term zero sums have net digits m_j=q k_j-k_{j-1} with initial and terminal carry zero. Their l1 cost is at least (q-1) times the sum of absolute carries plus twice the sum of absolute closing carries of nonzero blocks. Thus q>=6 permits only zero carries; q=4,5 permit one signed unit carry, of cost 5,6, giving 60 and 12 ordered tuples per adjacent pair, respectively. At q=3 the only possibilities are one signed unit carry of cost 4 or two consecutive same-sign unit carries of cost 6. For a singleton, the remaining slots comprise two zeros or an opposite-sign pair: for each sign the weights are 60 (zeros), 30 and 60 (pair at the carry's two positions), and 120 per other position. The two-carry block gives 60 tuples per sign. For n>=2 this totals 2(n-1)(120n-90)+120(n-2), exactly the repaired excess. Zero carries give 120n^3+20n+1 by multinomial counting of up to three cancelling pairs and zeros. The frozen top-frequency expansion and initial conditions agree with these identities. Ordered triple-sum multiplicities were also directly squared and summed for q=3 through 8 and n=1 through 6 (python3 /tmp/opencode/frozen_math_reproduction.py); that finite check is corroboration only. The supplied verifier was inspected, not executed, and its separate moment checks do not test the erroneous frozen subtraction.

## originality

PASS

Pass is for the repaired exact ternary ordered-energy law and its quadratic excess, not priority for the known exceptional carries, the stable collision pattern, or the related Fourier-extension problem. The inspected prior results do not give the weighted-by-permutations count with all cancellations and finite endpoints included.

## value

PASS

The finite ordered count measures precisely the unweighted collisions in the critical integer-ratio ternary spectrum already identified in sharp Fourier-extension work. The repaired excess remains positive and quadratic for n>=2, unlike the linear excess for four and five, and its exact constant and boundary correction give a useful comparison for truncations. This is not a claim about the weighted extension conjecture.

The dated certificate retains the supplied scientific assessment, sources and limitations.
