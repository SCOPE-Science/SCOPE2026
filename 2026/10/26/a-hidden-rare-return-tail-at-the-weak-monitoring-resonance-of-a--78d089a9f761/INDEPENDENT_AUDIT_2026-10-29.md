# Independent mathematical audit

## correctness

PASS

For 0<ε<1, Kε=diag(sqrt(1−ε),1)exp(−iεκ_ε σ_x) and survival P(Nε>n)=||Kε^n e0||². When κ_ε→κ finite, the matrix expansion Kε=I+εGκ+o(ε), Gκ=[[-1/2,−iκ],[−iκ,0]], gives compact-time Euler-product weak convergence. Direct squaring of Gκ+I/4 gives (1−16κ²)I/16 and the displayed hyperbolic survival including the double eigenvalue κ=1/4. For fixed κ>0 the limiting Gκ is Hurwitz; integrated density equations give ∫(x,y,c)dt=(1,1,0), ∫t(x,y,c)dt=(2,2+1/(4κ²),−1/(2κ)), hence E Zκ=2 and Var Zκ=4+1/(2κ²), with uniform integrability from a Lyapunov bound. For nonresonant finite-step rotation, X=sum K^n|e0><e0|(K*)^n=I/ε by the exact Stein equation K K*=I−εP and spectral radius<1, so ε E Nε=Tr(εX)=2, vs exactly 1 at zero rotation. In joint κ_ε→0+, the roots of λ²−(1+sqrt(1−ε))cos(εκ)λ+sqrt(1−ε)=0 obey 1−λslow~2εκ², 1−λfast~ε/2; the slow projection norm²~4κ² yields survival/(4κ²)→e^(−4u) on n~u/(εκ²) and variance~1/(2κ²). Independent evaluation compared 30 continuous Gκ matrix exponentials with the closed formula (max absolute error 3.33e−16). Finite checks corroborate and do not replace joint spectral asymptotics. Scope is the stated two-site initial-return rank-one detector, no unbounded κ limit.

## originality

PASS

Best-of-knowledge assessment: earlier weak-measurement two-level work already establishes exact finite-strength spectral first-return expressions, a mean discontinuity and resonant variance peaks. The assessed claim is the simultaneous ε-small/angle-small probability-law family, its κ=1/4 exceptional-point transition and the quantitatively normalized κ→0 rare tail with nonuniform-integrability explanation. Full text of Ziegler–Heine–Tornow (2026), §§2.2–2.4 and Appendix A, was examined: its Eq. (28) supplies the finite-step eigenvalues, but the inspected statement does not identify the double scaling / rare tail as an explicit theorem. The exact formulas could yield these results by additional nontrivial singular asymptotics; this is a material implication/priority risk, not a claim of literature-wide uniqueness.

## value

PASS

The rare long return component explains why weak convergence to Exp(1) at κ=0 loses a full unit of the discrete rescaled mean. The exceptional point and all-moment regime give natural, physically motivated finite-time detection statistics in a fixed minimal quantum-walk model, not an arbitrary parameter slice. The exact tiny rare mass 4κ² and long clock 1/(εκ²) are independent informative quantitative invariants; no many-site generalization is claimed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
