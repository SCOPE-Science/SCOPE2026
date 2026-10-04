# Same-model review

## Correctness
PASS. The proof reduces the entire cell by an explicit Sylvester gauge to \(\operatorname{diag}(\tau,0,\kappa)\), proves the three possible values of \(\alpha\) by direct rank arguments, and obtains \(\gamma\) from Roth's zero-case equivalence plus the explicit rank-one normalized witness. The argument is characteristic-free. `verify.py` independently exhausts the effective residual variables over four prime fields and checks the normalized intertwiner matrix.

## Originality
PASS with stated residual risk. The 7 September 2026 primary source proves only the normalized point and explicitly names precise strictness characterization as a remaining problem. Searches of published-finding corpus and the web using the exact Jordan type, the \(\alpha,\gamma\) notation, diagonal perturbations, and Roth rank minimization found no equivalent or stronger cell classification. Ferrante--Wimmer's sufficient spectral theorem does not cover this Jordan type. The full 2013 article was not openly available in the inspected sources, so an equivalent unstated observation there remains a residual risk.

## Value
PASS. The result is a complete, invariantly motivated classification on \(\operatorname{Diag}_3(K)+\operatorname{im}\delta_A\), not an arbitrary parameter slice. It identifies a sharp algebraic boundary between equality and strictness and shows the recent counterexample is generic on this cell; over finite fields it also gives the exact strict count \(q^4(q-1)^2\).

## Closest literature and limitations
Closest is Shi--Zhang--Zhang, arXiv:2609.07113v1, which supplies the normalized point \(C=\operatorname{diag}(1,0,1)\) and the explicit rank-one intertwiner. The present result does not classify the three remaining quotient coordinates \(c_{21},c_{23},c_{31}\), and makes no arbitrary-field dimensional-minimality claim.

Same-model review: passed. Independent audit: not yet performed.
