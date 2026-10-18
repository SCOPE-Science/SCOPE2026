# Independent mathematical audit

## correctness

PASS

For affine trial U containing x0, exact minimization of G(x)=||S(Tx−c)||² yields sketched normal-equation orthogonality <Sz,Sh>=0 with z=r(xhat), h=r(x0)−r(xhat). On residual span W, squared-norm 1±ε embedding with ε<1 makes S invertible onto SW; its inverse pullback metric M has eigenvalue interval [1/(1+ε),1/(1−ε)]. For G(xhat)>0 the sketched residuals Sz and Sh are orthogonal with ||Sh||²=δ||Sz||². Restriction to their 2D span makes normalized true change tr(MK), K=[[0,sqrt(δ)],[sqrt(δ),δ]], whose signed eigenvalues λ±=(δ±sqrt(δ(δ+4)))/2. Minimizing over all metrics in spectral box assigns max metric to negative eigendirection and min to positive, yielding exact lower envelope [δ−ε sqrt(δ(δ+4))]/(1−ε²). A two-row construction with S=M^-1/2 and r(x)=M^1/2(1,x sqrt δ) attains equality for EVERY ε,δ>0; rearrangement gives universal no-ascent threshold δ>=4ε²/(1−ε²). At δ=0, Sh=0 and embedding injectivity forces h=0; if G optimum=0 then F optimum=0. Independent exact rational two-row witness at ε=4/5,δ=9/4 yielded Ghat=1, G0=13/4, Fhat=37/9, F0=73/36, and F0−Fhat=−25/12, confirming sharp possible true ascent. Finite witness checks are not the all-ε,δ proof.

## originality

PASS

Sabaté Landman--Nakatsukasa arXiv:2510.11237 Proposition 1 proves a sufficient linear-in-ε descent test δ>=2ε/(1−ε) for sketch-and-solve via independent norm inequalities at incumbent/new point; it does not use exact minimizer orthogonality and does not establish necessity or a sharp lower envelope. The submitted deterministic 2D spectral optimization sharpens this to 4ε²/(1−ε²) with matching worst-case constructions. Epperly--Webber arXiv:2605.19096 analyzes distributional and expected error for randomized embeddings, not a deterministic observed-δ acceptance threshold relative to x0; theorem 2.1/2.2 and proof context in full arXiv rendered text were inspected. Nakatsukasa--Tropp quasi-optimality is a different error bound. Classical spectral rearrangement is prior and not claimed new; its application to an incumbent-conditioned exact sketch acceptance is the contribution.

## value

PASS

In sketched quadratic minimization, a practitioner observes only a sketched decrease and wants a guaranteed true-objective decrease. The exact two-parameter, sharp and realized acceptance frontier gives a genuinely stronger guarantee than the existing linear-in-distortion sufficient test and supplies explicit ascent counterexamples when below threshold. This is a motivated optimal control diagnostic for iterative sketch-and-solve, not merely a restatement of norm equivalence.

The dated certificate retains the supplied scientific assessment, sources and limitations.
