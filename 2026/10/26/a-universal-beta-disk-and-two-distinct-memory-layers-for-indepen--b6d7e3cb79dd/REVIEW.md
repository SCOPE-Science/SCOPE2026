# Independent mathematical audit

## correctness

PASS

Position reset rate r=ck with orientation clock independent: in stationarity Y_k(t)=k int_0^{A_k(t)}exp(-ks)U_{t-s}ds where A_k~Exp(ck) independent of orientation history. Freezing heading yields Z_k=U_t(1-exp(-k A_k)), and angular chord estimates give L2 error <=(2D_R+4h)/k. Scaling E=k A_k~Exp(c) shows radial R=1-exp(-E) has Beta(1,c) law and is independent of U_t; stationary orientation Fourier coefficients h/(h+D_R j²). On fast times s/k the age PDMP R_s has Cov(R0,Rs)=nu exp(-(1+c)s), with mu=1/(1+c), nu=c/((1+c)^2(2+c)); at fixed physical times recent reset ages become independent, giving mu²[m²+(1-m²)exp(-(h+D_R)t)], m=h/(h+D_R). Different zero-lag limits differ by nu>0. Exact symbolic stationary generator equations and k→infinity moment limits independently checked.

## originality

PASS

Shee 2024 harmonic trapped ABP paper shares position+heading reset **at the same events**, unlike two independent clocks; its full primary PDF was examined for reset protocol. Kumar–Sadekar–Basu 2020 studies position-only versus orientation-only resetting in free ABP rather than simultaneous independent clocks with harmonic stiffness and distinct fast/slow time layers. Other known Beta laws for run-and-tumble in traps concern different angular dynamics. Resultary returned unrelated reset oscillator and Jacobi process, no dominating same mathematical model theorem. Generic switching-process results could mechanically imply portions; residual risk recorded.

## value

PASS

Identifies a natural singular limit of two independent physical timescales with an explicit full polar law, central and edge density behavior, and noncommuting lag/confinement limits; the positive memory gap nu measures a meaningful nonuniform covariance effect. Beta distribution alone is not claimed novel.

The dated certificate retains the supplied scientific assessment, sources and limitations.
