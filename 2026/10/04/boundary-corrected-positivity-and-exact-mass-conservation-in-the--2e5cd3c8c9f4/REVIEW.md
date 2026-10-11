# Independent mathematical audit

## correctness

PASS

The forward step was reconstructed algebraically from the frozen formula rather than inferred from the saved checker. Writing \(F=h\beta^kS^{k+1}I^k/N^k\), \(G=h\epsilon^kE^{k+1}\), and \(H=h(\gamma^k+\mu^k)I^{k+1}\), all updated components are nonnegative because their denominators are \(1+hq>0\) with nonnegative numerators. The five increments are \(-F\), \(F-G\), \(G-H\), \(h\gamma^kI^{k+1}\), and \(h\mu^kI^{k+1}\); the last two sum to \(H\), so total \(S+E+I+R+D\) is conserved exactly. At \((S,E,I,R,D)=(N,0,0,0,0)\) every transfer is zero, so the update fixes the state and disproves the printed componentwise strict-positivity implication. The bundled rational checker was inspected only as corroboration, not as proof.

## originality

PASS

Best-of-knowledge originality survives. The source paper motivates equation (3.1) as unconditionally positivity preserving, while the submitted result sharpens that statement at the boundary and adds an exact conserved quantity for this particular semi-implicit step. Targeted Resultary, SCOPE and web searches found general positivity/NSFD epidemic schemes but no statement of this exact Liu--Tian telescoping invariant or its disease-free counterexample. General mass-conserving epidemic discretization theory does not imply the specific identity without checking the actual update.

## value

PASS

The result corrects a mathematically false strict-positivity formulation at a natural invariant boundary and supplies an exact implementation-level conservation law for the same published numerical step. This is a motivated structural correction, not an arbitrary normalization check: it identifies the correct invariant cone boundary behavior and a conservation test that future implementations can use.

The dated certificate retains the supplied scientific assessment, sources and limitations.
