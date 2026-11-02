# Independent mathematical audit

## correctness

PASS

PASS: The actual two-cell periodic ODE has positive initial masses a,b and transfer fluxes K_{3/2}=y_1+C, K_{5/2}=y_2+C, C>=0. Their difference is independent of C, whereas the production/destruction split retains C. Independently reduce the signed Gauss-Lobatto mPDeC stage equation to a positive 2x2 linear exchange system: x_1=(a+h(a+b)R_+)/(1+h(R_++R_-)), x_2=a+b-x_1. R_+,R_- >=0, so all finite stages strictly positive and conservative. Induct on fixed correction count m: previous stages approach a,b at O(C^-1), rates have leading multiples C; stage difference satisfies x_1-a=[m eta_ell/B_ell]*ab(b-a)/[(a+b)C]+O(C^-2) with B_ell=sum|theta|, eta_ell=sum theta. The last Gauss-Lobatto stage has eta=B=1, giving M ab(b-a)/[(a+b)C]. The true flow at fixed h moves by (b-a)(1-exp(-2h))/2; if a!=b and h>0, nonzero true drift survives while the numerical map freezes as C grows. Exact one-correction identity and 16 fresh rational configurations independently checked. Finite samples cannot establish uniform asymptotic induction.

## originality

PASS

PASS (qualified): The authors of the motivating 2026 flux-globalized mPDeC paper construct the rates by sign-splitting face fluxes and prove positivity/well-balancing. Their primary full text (arXiv:2610.21857v1, §§3.2, 4, Theorem 4.4) does not analyze arbitrary additive face-flux gauges, the fixed-M large-gauge limit, or its exact 1/C coefficient. Traditional mPDeC and stability results use specified production/destruction representations; those results neither state nor logically imply this sharp representation-sensitivity theorem. The claim is for this two-cell periodic example, not for failure of their chosen gauge-fixed shallow-water implementation. Unindexed prior stability or invariance analysis remains a priority risk.

## value

PASS

PASS: Flux differences govern the conservative semidiscretization, so an arbitrary additive flux constant should leave the underlying ODE unchanged. The theorem exhibits and quantifies loss of this invariance in a standard nonlinear positive linearly implicit splitting, through every fixed finite correction budget. It distinguishes conservation/positivity and fixed-representation order from genuinely gauge-uniform accuracy, providing a concrete mathematical motivation for flux normalization. This is not a mere notational reparametrization, as the numerical solution changes.

The dated certificate retains the supplied scientific assessment, sources and limitations.
