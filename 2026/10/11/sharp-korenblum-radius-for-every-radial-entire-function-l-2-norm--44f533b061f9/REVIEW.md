# Same-model mathematical review

## Correctness — PASS

The norm is the coefficient norm \(\sum m_j|a_j|^2\), by radial orthogonality. Cauchy–Schwarz proves \(m_j^2\le m_{j-1}m_{j+1}\), making the backward coefficient shift \(R_WB\) a contraction at \(R_W^2=m_1/m_0\). Exterior domination makes the meromorphic quotient \(f/g\) rational with all poles strictly inside the comparison circle and with modulus at most one outside. The reversed-polynomial identity gives \(Q(R_WB)f=P(R_WB)g\), with \(Q\) zero-free on the closed unit disk; rational von Neumann functional calculus proves the norm inequality. The test pair \(f\equiv c,g(z)=z\) for \(R_W<c<S\) eliminates every larger radius \(S\). These steps do not require that multiplying an entire function by a polynomial preserve the weighted norm: the reverse-polynomial equation is justified coefficientwise. `CHECK.py` was executed successfully using exact fractions, independently testing key finite identities. The proof—not its finite tests—covers all moments and all entire pairs.

## Originality — PASS

Wikström, arXiv:2609.39622v1, proves the exact radius for Gaussian, nonincreasing radial weights, and Gamma weights only up to the threshold \(\beta\le5.4475\ldots\). Its Question 7.4 expressly leaves the large-Gamma and narrow-ring weights unresolved, even though its Propositions 7.2 and 7.3 disprove applicability of a particular sufficient moment-measure criterion. Those examples are covered here by a genuinely different, universally valid backward-shift contraction argument. Wee–Le (2022/2023) supplies upper bounds rather than the universal sharp lower bound. Efraimidis–Llinares–Vukotić treats disk functions with a weaker annular domination condition, so it does not imply the entire-function statement. The relevant published mathematical search records inspected concern other operators (such as \(\ell_p\) shifts) or analytic inequalities and do not establish this Korenblum radius. An earlier mathematical claim classifies equality pairs only under the source's decreasing-weight hypothesis; the present all-weight sharp-radius theorem neither repeats nor requires that equality classification. Search coverage cannot exclude an unindexed earlier proof.

## Value — PASS

This directly resolves both classes asked about in Question 7.4, including arbitrarily large Gamma exponents and radially concentrated ring weights for which the source's measure criterion fails, and proves a complete all-radial theorem. The replacement proof exposes a structural Hilbert-contraction mechanism, so the result is not a mere numerical improvement or routine special case. The distinction from weaker disk-annulus domination remains essential.

## Closest sources and limitations

Most relevant primary source: Frank Wikström, *The sharp radius in Korenblum's maximum principle for the Fock space*, arXiv:2609.39622v1, notably Theorems 1.2–1.3, Corollary 1.4, Propositions 7.1–7.3 and Question 7.4. Additional references: Wee–Le, *Korenblum constants for various weighted Fock spaces* (2023); Efraimidis–Llinares–Vukotić, *Korenblum's Principle for Bergman Spaces with Radial Weights* (2025). The theorem is confined to Hilbert \(p=2\) entire-function spaces and domination on the full exterior. Risk: possible unindexed equivalent operator-theoretic proof. Independent review has not been conducted.

Same-model review: passed. Independent audit: not yet performed.
