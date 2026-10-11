# Independent mathematical audit

## correctness

PASS

The one-variable antiderivative generator tests give the three conditional laws. Stationarity of (x^2+y^2)/2 gives aE[x^2-xy]−bE[y^2]=0, which factors because k_+−k_-=1 and k_+k_-=b/a. If the factor polynomial vanishes on invariant support, a bounded complete nonorigin trajectory cannot pass through x=y=0 and must stay in one plane x=ky. Tangency there, using ak^2-ak-b=0, forces z=a(k-1), then ydot=0 and the remaining equation makes the trajectory an equilibrium. Thus non-equilibrium stationary measures must charge both signs. Writing X=E[x^2],Y=E[y^2],C=E[xy] gives C/Y=R^2-b/a; Cauchy--Schwarz yields k_-<=R<=k_+, and equality forces x=k_+y or x=-k_-y almost surely, reducing to the corresponding equilibrium mixtures. The inspected exact verifier correctly certifies the generator/factor algebra and source-parameter slopes.

## originality

PASS

The full foundational Wang paper gives the exact quadratic flow, all five equilibria and the multi-scroll/bifurcation phenomenology, but not invariant-probability conditional laws, stationary cone balances or RMS bounds. Resultary searches located only analogous stationary laws for other flows, not a same-object theorem or a generic theorem implying the equilibrium-cone rigidity. The audited factorization and equality analysis therefore remain best-of-knowledge original.

## value

PASS

The theorem turns the canonical five-equilibrium geometry of a named multiscroll flow into a sharp all-stationary-state constraint, including a sign-straddling law, a quantitatively sharp RMS interval and exact equality cases. Those are natural structural diagnostics for recurrent regimes rather than a tiny numerical check.

The dated certificate retains the supplied scientific assessment, sources and limitations.
