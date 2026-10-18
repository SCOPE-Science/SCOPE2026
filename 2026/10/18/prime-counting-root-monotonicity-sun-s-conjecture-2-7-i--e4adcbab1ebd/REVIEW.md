# Scientific review: Sun's prime-count root monotonicity

## Correctness — PASS

All quantifiers are specified: \(n\ge5\) integer, \(1\le k\le n\) integer. The interval bound \(B-A\le2n/\log n\) from Montgomery–Vaughan and the strict lower bound \(A>kn/\log(kn)\) from Rosser–Schoenfeld yield \(k\log(B/A)<2\log(kn)/\log n\le4\). Because \(A\ge\pi(300)=62>e^4\), this proves the strict target for \(n\ge300\). The exact bounded complement is \(44\,840\) pairs; the provided checker directly verifies each integer-power inequality, and two independent methods compute \(\pi(j)\) for every required argument \(j\le89\,700\). All critical steps and finite checks were reconstructed. Risks: the analytic inequalities are accepted as classical published theorems, not independently reproved.

## Originality — PASS, subject to residual literature risk

Sun's original Section 2 Conjecture 2.7(i) (arXiv:1402.6641, first posted February 25, 2014) states exactly this question and provides no proof. Its part (ii) is separate. Sun–Zhao, arXiv:2004.01080, studies arithmetic values of \(\pi(kn)\) but not the normalized root inequalities. The original 1962 and 1973 explicit counting bounds are distinct ingredients, not statements of the conjecture. Multiple full-wording and equivalent integer-power literature searches plus targeted mathematical-results searches found no dominating theorem; other results involving \(\pi\), factorial valuations, or root monotonicity do not imply the simultaneous \(\pi(kn)\) comparison. Residual risk: a later proof or a stronger but differently indexed counting inequality may have been missed; absence of a search hit is not proof of priority.

## Value — PASS

The result settles the whole first part of an explicitly posed 2014 conjecture, not an arbitrary finite slice or a mere reparametrization. It establishes a new uniform global monotonicity statement for the prime-counting function on all admissible integer arguments. The finite computer certificate resolves only the small range, complemented by a separate analytic proof for the infinite range. The related square-count question in Conjecture 2.7(ii) remains untouched.

## Sources and limitations

Primary problem: Sun, *Problems on combinatorial properties of primes* (2014), arXiv:1402.6641, Conjecture 2.7(i). Analytic inputs: Montgomery–Vaughan (1973), doi:10.1112/S0025579300004708; Rosser–Schoenfeld (1962), doi:10.1215/ijm/1255631807. Closest later related primary paper examined: Sun–Zhao (2020), arXiv:2004.01080. Historical priority remains provisional without independent expert audit, and the explicit analytic inputs are taken as established literature.

Self-review: passed. Independent audit: not yet performed.
