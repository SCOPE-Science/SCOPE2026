# Self-review

## Correctness

PASS. At a positive equilibrium the source's equilibrium formula makes the normalized state fractions \(w_i\) positive with \(\sum_iw_i=1\). Rewriting the printed rank-one Jacobian with
\[
r=-\frac{N_0\beta'(N_0)}{\beta(N_0)}
\]
reduces its secular factor to
\[
\sum_iw_i\frac{\lambda+r\gamma_i}{\lambda+\beta(N_0)+\gamma_i}.
\]
For \(r>0\), every summand has strictly positive real part whenever \(\operatorname{Re}\lambda\ge0\), so the Jacobian is Hurwitz. The cases \(r=0\) and \(r<0\) respectively produce a zero root and a positive real root. An exact three-state replay independently verifies a mixed-sign example.

## Originality

PASS. Rank-one determinant formulas are standard. The accepted content is the source-specific theorem that the extra same-sign condition in the published finite-\(n\) stability result is unnecessary, giving the exact criterion \(\beta'(N_0)<0\) for every finite number of states. Searches by DOI, theorem number, feedback sign, mixed-sign aliases, and rank-one terminology found no equivalent published refinement. The earlier stem-cell control and Markov state-transition literature does not imply this Jacobian result.

## Value

PASS. The removed hypothesis is restrictive precisely in heterogeneous systems, because different state-specific removal rates can make the source's row-feedback quantities have different signs. The theorem converts the paper's conditional multi-state stability statement into a complete finite-state local classification and supplies an explicit three-state case newly covered by the sharper result.

## Closest literature and limitations

The earlier Lei–Levin–Nie framework studies feedback control and robust stem-cell regeneration, while Gupta and coauthors model phenotypic equilibrium through stochastic state conversion. Neither contains the rank-one local-stability classification of the later reduced ODE.

The result is local and applies after assumptions (A1)–(A3). It does not establish global attraction or cover the mother-state-dependent transition matrix before the reduction.

Self-review: passed. Independent audit: not yet performed.
