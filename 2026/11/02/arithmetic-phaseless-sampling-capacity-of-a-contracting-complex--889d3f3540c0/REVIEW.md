# Scientific review

## Correctness — PASS

The claim is proved for every real angular increment and every contraction factor strictly between zero and one. Dividing out the common zero order and comparing the first different Taylor coefficient gives a nonzero real harmonic that must tend to zero along the prescribed phases. Density of an irrational rotation rules this out. For a rational increment \(\theta/\pi=p/q\), the same harmonic is periodic, and its values one step apart have nonzero determinant whenever its order is less than \(q\). The explicit pair \(1+iz^q\) and \(1-iz^q\) proves sharp failure above the degree cutoff. The \((d+1)^2\) lifted bases are pairwise distinct for degree \(d<q\); their square complex Vandermonde matrix is invertible. Nonzero Hermitian rank-one Gram matrices determine coefficient vectors uniquely up to phase. The real dimension of Hermitian matrices proves the stated *linear-lifting* lower bound. The proof does not infer an infinite theorem from finite tests.

## Originality — PASS, subject to historical-priority risk

Perez, arXiv:2009.02061, Theorem 2.1 addresses two whole intersecting line segments and uses local Taylor harmonics; the current object is a single contracting spiral with only one sample per radius. Liehr, arXiv:2308.05722, Theorem 1.1 concerns complete families of parallel lines; its sampling hypothesis does not follow from the spiral data. Grohs–Liehr–Rathmair, arXiv:2308.00385, Theorem 2.4 deals with separated Fock-space uniqueness sets and does not supply an interior accumulation point, the exact polynomial denominator cutoff or the consecutive-sample Vandermonde lift. Przybylek–Siedlecki, arXiv:1907.09371, Theorem 4.2 treats polynomial recovery from separately selected sampling points but does not state the sharp condition for a fixed complex geometric progression. Earlier and published related results were compared by their hypotheses and conclusions, not merely title.

The main residual risk is an older general theorem on uniqueness sets or complex-exponential interpolation that subsumes the special spiral statement. The novelty determination is best-knowledge, not a priority certificate; an independent expert comparison remains outstanding.

## Mathematical value — PASS

A contracting geometric spiral is a single, explicitly specified phaseless sampling family, natural for geometrically scaled observations. The exact reduced-denominator threshold classifies which polynomial degrees the spiral can distinguish, while the irrational case yields uniqueness for arbitrary holomorphic germs. The finite Vandermonde reconstruction is an explicit information-theoretic recovery result, rather than a mere nonconstructive uniqueness criterion. The \((d+1)^2\) lower bound is meaningful only in the fully lifted linear model; no claim of minimal nonlinear or robust recovery is made.

## Reproducibility and limitations

`verify_spiral.py` requires only the Python standard library and passes 335 supplementary finite assertions, including exact arithmetic for the degree-one phase-lift determinant. The proof, rather than numerical tests, establishes the quantified conclusions. Exponentially shrinking nodes may make reconstruction ill-conditioned, and the result assumes exact moduli at exact locations. Full priority, stability and independent validation are unresolved.

Self-review: passed. Independent audit: not yet performed.
