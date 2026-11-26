# Independent mathematical audit

## correctness

PASS

With independent samples, exponential memorylessness gives iid E_i=n(M_i−μ_i)/σ of rate 1 and V=S/σ∼Gamma(K,1) independent of the minima, with EV=K and EV²=K(K+1). These moments give both stated unselected corrections. Let M=max_{i<k} E_i, E=E_k, and D=M−E. The selected scaled overshoot A obeys nA=E+D·1_{D>t} (ties have probability zero). Conditioning on E shows P(D>s)=∑_{j=1}^{k−1}(−1)^{j+1} binom(k−1,j)e^(−js)/(j+1) for s≥0. Tail integration yields the stated H. Expanding E[(A−cV)²] and subtracting at the two c's cancels E[A²] and gives exactly (1−2KH)/(n²K(K+1)). H(0) is the harmonic number at k minus 1, at least 1/2, whereas 1/(2K)≤1/4. H tends to zero and H'(t)=−t f_D(t)<0 for t>0 because the convolution density is positive there, proving the unique crossing and its sign. An independent 60-digit root computation for H₂(t)=1/[6(n−1)] gave 4.1114506064200021, 4.9611811353194030, 5.9230058153332692 and 6.4367530360963220, with residuals below 2×10⁻⁶². The frozen VERIFICATION.md and verify.py were inspected, not executed; they describe finite quadrature, risk-algebra and bisection checks, not the proof.

## originality

PASS

The distinct claim supported by this review is the k≥3 exact one-versus-tied-rest risk law and crossover. The k=2 result is fully implied by the earlier exact two-population risk formula, not just illustrated in previous numerics. Vellaisamy's general-k selected-quantile article is a plausible broader overlap, but the inspected accessible material does not establish the implication.

## value

PASS

These two fixed corrections come from the same standard unselected estimation problem. The one-best against symmetric competitors geometry is a natural way to vary selection bias while controlling all other parameters, and the exact crossover identifies when the preferable correction reverses. It gives an analytically usable benchmark for genuinely multiple competitors without claiming either rule is optimal after selection.

The dated certificate retains the supplied scientific assessment, sources and limitations.
