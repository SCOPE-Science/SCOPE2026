# Scientific review: maximal algebraic degree for Nash facility optima

## Correctness

**PASS.** The degree upper bound follows from the rational derivative on each smooth cell. The constructed two-cluster profiles force the unique global optimum into the central gap by strict log-concavity and opposite derivative signs. The all-degree lower bound relies on an explicit finite-field identity: the complete set of \(n\)-th roots of unity modulo a prime \(p\equiv1\pmod n\) yields \(F'(Y)\equiv nY^{n-1}\pmod p\). Nonzero variation of the next-to-last elementary symmetric function permits choosing the constant coefficient to have exact \(p\)-adic valuation one. Eisenstein irreducibility and Rolle's theorem then yield algebraic degree exactly \(n-1\) and all-real conjugates. Arbitrarily fine choices of rational lifts prove density. Exact checks in `verify_degree.py` confirm 19 finite cases including a separately stated four-agent certificate. The finite cases are not used as proof of the unbounded assertion.

## Originality

**PASS, with limited external priority assurance.** The closest relevant primary paper is Lam, Aziz and Walsh, *Nash Welfare and Facility Location*, COMSOC-2021 and arXiv:2310.04102. Its Theorem 1 proves that three rational input locations can yield an irrational optimizer, and its Theorem 2 approximates the placement. It does not establish maximal irreducible degree for all input sizes nor density in two clustered rational populations. The 2025 broader facility-welfare formulation *FLIGHT* includes precisely the logarithmic Nash transformation, but its examined propositions concern concavity, shift properties, approximation and stochastic asymptotics, not irreducible critical polynomials. Searches for degree, irreducibility, related aliases, and stronger coverage found no directly equivalent claim in the inspected papers; this negative observation is not a uniqueness certificate. Possible specialist algebraic-geometry literature and unpublished variants are the main residual priority risks. Classical Dirichlet and Eisenstein theorems, uniqueness/concavity, and the original irrationality example are not claimed as discoveries.

## Value

**PASS.** The exact Nash optimal coordinate is a natural invariant of a standard one-dimensional allocation model. Existing work's irrational three-agent example motivates asking whether the polynomial degree bound reflects genuinely necessary algebraic complexity as the number of agents grows. The present theorem answers that complete all-size question sharply and robustly in a simple geographically interpretable two-cluster family. The degree is an exact descriptive measure of the output, not an unsupported lower bound on computational running time or radical solvability.

## Sources and limitations

Primary sources: https://comsoc-community.org/assets/proceedings/comsoc-2021/LamEtAl.pdf (relevant full-text sections, including exact irrational example) and https://arxiv.org/html/2310.04102 (sections 3–4 and theorem inventory). Broader comparison: https://arxiv.org/pdf/2502.14732 (sections 4–5 and contribution inventory). The 2021 workshop was held June 7–10 (https://comsoc2021.net.technion.ac.il/program/). Exact upload time for the workshop manuscript is not established. The claimed density is not openness or almost-sure behavior. No claim about multiple facilities, computational complexity or general utility is made.

Self-review: passed. Independent audit: not yet performed.
