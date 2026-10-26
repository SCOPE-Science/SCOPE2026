# Review

## Correctness — PASS

The residue map modulo 5 has exactly the 4-cycle \(0\to1\to2\to4\to0\) and the fixed residue 3. Hensel’s lemma gives the unique fixed point \(\alpha\in3+5\mathbb Z_5\). The fourth-return derivative satisfies \(g'(\alpha)\equiv16\pmod{25}\), and the chain-rule recurrence gives \(g''(\alpha)\equiv0\pmod5\). These imply \(\nu_5(g(x)-x)=k+1\) on the shell \(\nu_5(x-\alpha)=k\), and the Taylor period-lifting lemma proves the exact period \(4\cdot5^{n-k-1}\) at every level \(n>k\). Each shell has exactly that many residue classes, so it is one cycle at every finer level and is minimal. The finite script checks levels 1 through 5 only; the infinite claim is proved in RESULT.md.

## Originality — PASS

The closest primary literature is Fan–Liao’s general minimal-decomposition theorem and their separate classification of the square map. The general theorem covers the qualitative periodic/minimal/basin framework and odometer structure, but neither source identifies the residue decomposition or the exact shell-period law for \(x^3+1\) on \(\mathbb Z_5\). published-finding corpus searches for the exact cubic, the residue-3 fixed point, and the all-level shell-period formula produced no exact match. Related p-adic records concern different quadratic or rational maps. This is a bounded best-knowledge comparison, not a proof that no unindexed equivalent exists.

## Value — PASS

The result gives a complete, explicit decomposition for a simple cubic map outside the quadratic examples emphasized in the general literature. It simultaneously quantifies an attracting basin of measure \(4/5\), one fixed point, countably many minimal shells, and every finite-level cycle length. The vanishing of the second derivative of the fourth return modulo 5 is the structural feature that makes the exact period-lifting law possible.

Self-review: passed. Independent audit: not yet performed.
