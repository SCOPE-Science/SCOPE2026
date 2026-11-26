# Independent mathematical audit

## correctness

PASS

Reconstructed the proof in RESULT.md lines 39–110. The normalized negative-binomial law yields G; single and double silence probabilities u=G(1−h), v=G(1−2h) give the correctly normalized Q_B=(N−1)(v−u²)/[u(1−u)], with positive denominator. Log(v/u²)=B−m(A−B). B is strictly increasing in β, with B(0)=0 and B(β*)=A, so the strict integer threshold and equality rules follow (at β=β* all finite orders have positive Q_B). Inverting via βh/(1+βh) gives β_m. The derivative ratio (∂_h B)/A' decreases strictly at fixed positive β, so its A'-weighted mean B/A decreases and each β_m increases in h. Taylor expansion uniformly for the bounded cutoff near h=0 gives √[m/(m+1)]; expanding 1−√(1−e^{−mA/(m+1)}) near h=1/2 gives the stated coefficient. At ideal h=1/2, v=G(0)=0 so the witness is strictly negative for every finite β and m≥1. For fixed h<1/2 and β below ceiling, u=wλ^m. Negative contrast is positive for some order and tends to zero at large m, ensuring a finite maximum. With Δ=A−B and t=B/Δ, the upper bound (N−1)wλ^t/h follows from u≤1−h; the lower bound at m=floor(t)+2 is (N−1)wλ^{t+2}(1−e^{−Δ}). The printed upper estimate at line 90 is only finite as written for β>0, because w=1 and t=0 for β=0; the uniform estimate above avoids that removable proof-line issue and the asserted theorem is unaffected. Differentiating B gives c_h=2h²(1−2h)/(1−h), so for ε=β*−β, εt→A/c_h and λ→1−2h; ε log(1−e^{−Δ})→0. The two bounds give the stated exponent. Read VERIFICATION.md and artifacts/verify.py without running the uploaded script. Its finite candidate window is corroboration, not a proof of global optimality; that comes from the analytic bounds.

## originality

PASS

The established counting law and click moment identity directly give the sign expression, and the ceiling/cutoff algebra starts from those known ingredients. Credit the distinct claim for the integer-order optimized population contrast and its sharp essential exponent, with a complete strict ceiling classification, not for the witness or photon-counting law themselves.

## value

PASS

For a standard detector witness the natural question is not only whether any amount of photon addition works, but whether the best possible population contrast remains appreciable near the cutoff. The optimized exponent shows it collapses faster than any power, even after choosing the order; mere negativity or a fixed-order formula would miss this obstruction. This is not a statement about experimental sample complexity, alternative statistics, or classicality of the state.

The dated certificate retains the supplied scientific assessment, sources and limitations.
