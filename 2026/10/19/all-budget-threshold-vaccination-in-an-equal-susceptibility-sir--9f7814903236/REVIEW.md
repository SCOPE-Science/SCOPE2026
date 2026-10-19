# Scientific review: all-budget threshold vaccination

## Correctness — PASS

For the precisely specified equal-susceptibility, heterogeneous-infectiousness SIR equations, time-integration gives the exact scalar final-size equation \(H=B+T(1-e^{-H})\) with \(B>0\). The proof checks existence and uniqueness of the **physical positive root** and shows \(1-Te^{-H}>0\) for every \(T\geq0\), including below and at the reproduction threshold. Its derivative yields strict improvement when weighted unvaccinated exposure decreases. A separate dose-saturation inequality proves that every fixed-budget maximizer uses the entire supply. An elementary threshold-exchange inequality then characterizes **all** optimizers, including ties, for every \(K\in[0,S]\). The rearrangement formula proves the full optimal survivor curve, its derivative where defined, and the endpoint cases. The 125-point rational-grid comparison and two independent numerical SIR integrations in `verify.py` check finite instances only and are not relied upon for the general conclusion.

## Originality — PASS, with residual risk

Almeida, Ducasse and Paparelli's Theorem 4 [1] proves the priority ordering only under an explicit upper bound on the vaccination budget; their Remark 1.4 specifically leaves removal of that bound for further work. Their Theorem 3 already proves dynamic/static supremum equivalence for all budgets, so that equivalence is **not** asserted to be new. Their proof also notes that tied priority levels can be treated; that observation likewise is **not** new. The new statement is that the threshold allocation is optimal for *all* budgets, together with the exact entire survivor curve and valid subcritical derivative. The full primary paper was examined at the theorem, assumptions, prior comparison and proof.

A particularly relevant earlier paper by Duijzer, van Jaarsveld, Wallinga and Dekker [2] uses a greedy ordering under separable mixing, but for an **unconstrained vaccine-quantity** optimization targeting the critical reproduction threshold. Its statement does not optimize final survivors at each prescribed budget in the presence of a strictly positive initial infectious seed. Penn and Donnelly [3] analyze small-supply asymptotics in a different group model; Gavish and Katriel [4] study imperfect (leaky) vaccination, which can have the opposite prioritization at high reproduction numbers. The rank-one final-size reduction and rearrangement arguments themselves are standard techniques. A specialized older fixed-budget result not located in the investigated literature could subsume the present statement; this is the principal originality risk.

## Mathematical value — PASS

The result closes an **explicitly identified unresolved budget range** in a recent mathematical epidemiology model, rather than changing a numerical constant or applying a cosmetic parameter substitution. It supplies a constructive global policy for every possible available quantity, characterizes ties and endpoint allocations, and produces an exact monotone all-budget survival frontier with a usable marginal-dose formula. A finite infected seed ensures this frontier passes smoothly through the critical reproduction level, addressing the mathematical obstacle that restricted the motivating proof. The example with \(K=1.5\) falls strictly outside the published small-budget condition \(K<1.25\), illustrating the newly established regime.

## Scope and residual limits

The theorem assumes identical susceptibility, perfect immediate vaccination of initially susceptible individuals, equal cost per dose, strictly positive initial infection, and deterministic SIR dynamics. It does not cover leaky vaccines, susceptibility heterogeneity, weighted clinical outcomes, or supply delivery-rate constraints. It yields the optimum for initial vaccination and, only by [1, Theorem 3], the **supremum** for time-varying controls. No independent assessment is claimed. Relevant older specialized vaccine-optimization literature may still contain a stronger all-budget implication not identified here.

Self-review: passed. Independent audit: not yet performed.

## Sources

[1] Almeida, Ducasse, Paparelli, *Optimizing vaccine allocation in an age-structured SIR model*, arXiv:2605.18256v1, 18 May 2026. https://arxiv.org/abs/2605.18256 .

[2] Duijzer, van Jaarsveld, Wallinga, Dekker, *The most efficient critical vaccination coverage and its equivalence with maximizing the herd effect*, Mathematical Biosciences 282 (2016), 68–81. https://repub.eur.nl/pub/79912/EI2016-06.pdf .

[3] Penn, Donnelly, *Asymptotic Analysis of Optimal Vaccination Policies*, Bulletin of Mathematical Biology 85 (2023), article 15. https://doi.org/10.1007/s11538-022-01114-3 .

[4] Gavish, Katriel, *Optimal vaccination at high reproductive numbers: sharp transitions and counter-intuitive allocations*, arXiv:2202.03909v1. https://arxiv.org/abs/2202.03909 .
