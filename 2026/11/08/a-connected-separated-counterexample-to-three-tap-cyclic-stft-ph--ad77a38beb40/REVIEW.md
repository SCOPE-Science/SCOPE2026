# Independent mathematical audit

## correctness

PASS

At t modulo 3 the three-term STFT polynomials reduce, up to unit phases, to A+Bz, B+Az^2 and z(A+Bz); all measured intensities depend only on S=|A|^2+|B|^2 and P=A conjugate(B), including frequencies where the polynomial pair differs. With d>=6 Fourier inversion of the t=0 intensity uniquely gives S and P, and conversely S,P determine all rows. For positive a,b the swap leaves S,P invariant but changes site magnitudes, ruling out global-phase equality. The nonzero cyclic gaps alternate lengths 1,2, hence support is 2-connected and there is a zero every block (1-separated). The quadratic X^2-SX+|P|^2 has exactly two positive ordered magnitude pairs unless equal; P fixes relative phase after a common phase gauge, proving ONLY the restricted fiber statement. Independently reconstructed full complex spectrograms over all d^2 time-frequency pairs for d=6,9,12 with (2,3,0) vs (3,2,0): maximum squared-intensity difference was zero to floating error; exact autocorrelation proof handles every d=3m.

## originality

PASS

The counterexample contradicts the unconditional cyclic short-window connectedness direction of Bartusel 2024 Theorem 7.2.12(b) under the theorem’s stated L=2, ceil(L/2)=1 separation, while it is not the lone-occupied-index-per-(L+1) exceptional support of part(a). The 2023 article has stronger L-separation hypotheses; previously published three-tap full-support fibers concern nowhere-zero signals and different arithmetic, not the present sparse period-3 amplitude swap. Genuine best-of-knowledge novelty is qualified by possible unindexed counterexamples.

## value

PASS

An explicit all-multiples-of-three counterexample pinpoints a false support-connectivity sufficiency theorem at its claimed half-window separation threshold, and the exact restricted phase-fiber classification identifies the underlying amplitude-exchange obstruction. This informs the correct hypotheses for finite STFT recovery and is a motivated nonroutine exception.

The dated certificate retains the supplied scientific assessment, sources and limitations.
