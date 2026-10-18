# Independent mathematical audit

## correctness

PASS

Wythoff lower-set indicator A(m)=floor((m+1)α)-floor(mα) equals 1 for {mα}≥β, and complementary upper-set B(n-m)=1 iff {(n-m)α}<β. For θ={nα}, the convolution r(n)=sum_{m=1}^{n-1}A(m)B(n-m) is a golden rotation count in the circle interval K_θ=[β,1)∩{y:{θ-y}<β}, whose length is the stated piecewise Λ(θ). Golden α has all bounded partial quotients, and each convergent Fibonacci-denominator block has O(1) interval discrepancy uniformly in start; an Ostrowski/Fibonacci expansion uses O(log n) blocks, giving r(n)=nΛ({nα})+O(log n) uniformly. Irrational equidistribution and the continuous Λ give weak pushforward measure density 2 on (0,β) and an atom 1-2β at β. Abel summation plus bounded-variation discrepancy gives Σr(n)=(β-β²)N²/2+O(N log N). Independent high-precision direct Wythoff convolution over n<=4000 agreed with the phase to max absolute error about 1.82 and sum ratio about 0.23598 versus β-β²≈0.23606798. Infinite bound derives from continued-fraction argument, not the regression.

## originality

PASS

Shallit established an exact Fibonacci-linear representation for the *same* sequence; therefore all individual r(n) are algorithmically determined in prior work. However his inspected sections do not provide the simple golden-rotation asymptotic profile, a limiting density plus atom, or the sharp quadratic summatory coefficient. Ashburn treats exact exceptional small values only. Novelty is the quantitative global law, not the raw representation function.

## value

PASS

An exact sequence representation alone leaves the scale and distribution of its large fluctuations opaque. The natural lower+upper Wythoff convolution has a nontrivial triangular plateau distribution, including a positive atom at the maximal density, plus an explicit leading quadratic summatory term with O(N log N) error. These quantify a motivated classical Beatty sumset problem beyond the exceptional-values census.

The dated certificate retains the supplied scientific assessment, sources and limitations.
