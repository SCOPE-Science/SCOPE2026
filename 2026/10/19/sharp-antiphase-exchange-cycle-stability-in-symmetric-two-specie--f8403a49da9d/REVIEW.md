# Scientific review

## Correctness — PASS

The theorem applies only to strictly positive exchange orbits of the symmetric competitive Ricker map. Subtracting and adding the two exact logarithmic exchange equations forces \(0<a<1\) and uniquely parametrizes each exchange orbit by \(z=\log(X/Y)>0\). The scalar relation \(\rho=(1+a)C(z)/(1-a)\) is strictly increasing, covering precisely the stated existence range. For stability, the two-step monodromy is \((PM)^2\), where \(P\) interchanges species, \(M\) is the one-step Jacobian, and the real quadratic for \(PM\) is \(\lambda^2+aS\lambda-D\). The strict Jury test is exactly the pair of inequalities stated in RESULT.md. The monotonicities of \(C\), \(J\), and \(A\) establish both the unique attraction interval and the unique universal coupling ceiling. The exact rational witness is reproduced by the standalone checker. The proof does not claim boundary nonlinear stability or any statement about nonexchange periodic orbits.

## Originality — PASS, with residual risk

The September 2026 motivating paper already studies the general competitive Ricker map and generic period-two stability inequalities. Kulakov, Neverova, and Frisman (2022) already discuss antiphase two-cycles and bifurcations. Ryashko, Otman, and Bashkirtseva (2025) also study symmetric competitive Ricker multirhythmicity. Those phenomena are credited explicitly. The present restricted statement is the complete **analytic** attraction classification of positive *exchange* two-cycles and its unique sharp universal coupling ceiling. Comparison of their relevant material identified numerical bifurcation diagrams and general Jacobian criteria but not the specific boundary equations or ceiling proved here. A potentially equivalent older closed-form specialization, including Russian-language or inaccessible older text, remains an unresolved literature risk.

## Value — PASS

The phase-exchange mode is a natural ecological antiphase state, not an arbitrary constructed slice: it is explicitly studied in prior two-species Ricker competition literature. Its coexistence with other rhythms makes a sharp **coupling-strength upper bound** and exact growth-window endpoints useful. The theorem distinguishes the existence of the exchange cycle from its genuine exponential attraction, resolves a whole positive coupling/growth parameter region, and provides a compact algebraically certified example. It does not purport to classify other asynchronous cycles.

## Closest literature and limitations

Goldar et al., 2026, doi:10.1155/ddns/7255117; Kulakov, Neverova and Frisman, 2022, doi:10.3390/math10071076; Ryashko, Otman and Bashkirtseva, 2025, doi:10.3390/math13050857; Luís, Elaydi and Oliveira, 2011, doi:10.1080/17513758.2011.581764. The last older publisher manuscript could not be fully inspected. No guarantee of historical uniqueness is inferred merely from database search. All conclusions are local deterministic spectral ones.

Self-review: passed. Independent audit: not yet performed.
