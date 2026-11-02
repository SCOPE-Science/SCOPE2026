# Review of the modulus-sixteen Apéry–Almkvist–Zudilin bridge

## Correctness

PASS. The exact second binomial expansion comes from Chan–Zudilin, Corollary 4.3 (also Sun, equation (5.2)). Legendre's formula leaves only power-of-two summands for both sequences modulo sixteen. Lucas's parity theorem converts each survivor to a binary expression. Direct Boolean algebra yields the identity \(2H(n)\equiv n+\beta(n)\pmod4\). The nonperiodicity argument constructs arbitrarily large unequal residues at an even multiple of each proposed period. Endpoint \(n=0\), normalizations, and finite-support conventions are handled. The independent program tests both binomial representations and the binary formulas, but the infinite proof is algebraic rather than computational.

## Originality

PASS under available evidence, with explicit residual priority risk. Chan–Zudilin prove exact hypergeometric and generating-function transformations, not the stated same-index modulus-sixteen congruence. Sun reproduces their alternate expansion and focuses on prime congruences. Rowland–Yassawi prove the Apéry binary formula and nonperiodicity, which are expressly credited here. Malik–Straub prove Almkvist–Zudilin periodicity only modulo eight, not the modulus-sixteen coefficientwise comparison. The new valuation-filtered comparison requires a nontrivial binary carry identity; the prior results, as stated, do not directly resolve it. Relevant earlier results and their stronger algebraic connection are not concealed. An unlocated explicit mod-sixteen specialization remains possible.

## Mathematical value

PASS. The relationship compares two naturally distinguished Apéry-like sequences with different recurrences, resolves their exact first nonperiodic two-power layer, and exhibits a remarkably simple generating-function difference \(8x/(1-x)^2\pmod{16}\). This is an all-index arithmetic law rather than a small finite table, and it explains why the two sequences agree modulo eight but diverge in a controlled way one power higher. It does not imply further congruences modulo thirty-two or general cross-sequence relations.

## Closest literature and limitations

The closest comparison is Chan–Zudilin (2010), Theorem 2.2 and Corollary 4.3; Rowland–Yassawi (2013), Theorems 3.28–3.29; Sun (2013), equation (5.2); Malik–Straub (2015), Theorem 5.3. Liu (2024) classifies individual Apéry-like sequences modulo optimal exponential-power congruence moduli, not cross-sequence same-index values. The proof adopts previously known identities and reuses the known Apéry block formula without claiming either as new. Complete historical priority cannot be certified from this source sample; independent mathematical validation has not been performed.

Self-review: passed. Independent audit: not yet performed.
