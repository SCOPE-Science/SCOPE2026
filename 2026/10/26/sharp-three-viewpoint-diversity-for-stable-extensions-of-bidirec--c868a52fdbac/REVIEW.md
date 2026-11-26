# Independent mathematical audit

## correctness

PASS

Bidirectionality identifies stable extensions with maximal independent sets. Such nonempty path sets have first and last selections within one vertex of the ends and successive gaps 2 or 3. Each membership column contributes at most two to the sum of three pair distances, giving the stated upper bound. The six bases satisfy independence and domination; inserting the three singleton columns adds two to every distance. In the order-nine family the first A,BC replacement leaves A,C at the anchor; subsequent steps use the A,C rule with the same inserted block and the unchanged fourth column B. The complete order-six gap list gives the five-cycle at distance at least four; a triple attains three. Orders one to three have counts 1,2,2. Independent gap enumeration and forward-bitset triangle detection reproduce the exact optima for orders 4–20 (python /workspace/independent_checks.py 1); this finite check is separate from the insertion proof.

## originality

PASS

The supported distinction is the exact bidirected-path invariant and order-six exception, not invention of maximin Hamming diversity. Closest same-day three-extension record concerns a disjoint domain; the closest exact path enumeration only gives a pair statistic.

## value

PASS

Three viewpoints are the first case where a maximally distant pair does not solve the packing problem. Knowing exactly when stability imposes a loss relative to the unrestricted binary bound gives a complete natural benchmark, and the unique exception is analytically explained rather than tabulated.

The dated certificate retains the supplied scientific assessment, sources and limitations.
