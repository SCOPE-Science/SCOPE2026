# Independent mathematical audit

## correctness

PASS

For the stipulated on-chain X packet, multiplication by the weight-d logical X cancels the packet sites and leaves d−n sites. Multiplication by a logical Pauli preserves the syndrome. With g=−log p_gate>0, the assumed independent-edge sum is (d−n)g, while −log p_net≤g. For n≤d−2 the second inequality is strict; for n=d−1 equality occurs exactly at p_net=p_gate, including the central case d=3, n=2. At n=d the packet has zero syndrome and is not part of this comparison. Read RESULT.md lines 4–46 and VERIFICATION.md lines 18–32; this proof is analytic, so no simulation or certificate is needed. In the conclusion, ‘favored’ is weak preference, subject to the explicit tie.

## originality

PASS

The primary source compares these two costs at the central packet size, not for all packet sizes, and warns that the full decoding rule is heuristic. The distinct result is a source-specific limitation on that rationale, not the monotonicity of −log or a new matching theorem. No inspected statement establishes the same limitation. The comparison to the source-specific public commentary is access-limited.

## value

PASS

The ceiling is a central design rule of the source. Showing that its local justification fails to change sign anywhere below d identifies exactly what the global decoder analysis must add. For instance at d=7, n=5 the packet still strictly beats the length-two complement even at equal probabilities. This is a motivated model-boundary correction, not a claim of full decoder performance or fault tolerance past half distance.

The dated certificate retains the supplied scientific assessment, sources and limitations.
