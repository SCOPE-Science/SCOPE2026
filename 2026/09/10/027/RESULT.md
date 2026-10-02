# Envelope-closure threshold correction for the H^1 Koranyi spectral-transfer route

## Context

The Heisenberg-Falconer program asks for dimensional thresholds guaranteeing that the Koranyi distance set of a compact set in the first Heisenberg group has positive Lebesgue measure. A proposed spectral-transfer route used the natural homogeneous-dimension boundary \(\dim_K>3\), with homogeneous dimension \(Q=4\), together with Koranyi spherical group-Fourier decay. The cited Raani-Singh result proves a positive-upper-density large-distance theorem and supplies the high-frequency coefficient decay used here; it does not itself prove the compact-set threshold considered below.

## Definitions

Let \(H^1=\mathbb C\times\mathbb R\) with its standard Heisenberg law and Koranyi norm. Write \(\mu=2(2k+1)\) for the spectral parameter at \(n=1\). The cited input is the envelope

\[
|R_k(\lambda r^2,\sigma)|\le C_0\min\{1,(|\lambda|r^2\mu)^{-1/4}\}.
\]

Set \(t=|\lambda|\mu\), fix \(R_0>0\), and define

\[
M(t)=\int_0^{R_0}r^6\min\{1,(tr^2)^{-1/2}\}\,dr.
\]

For a Riesz weight exponent \(\alpha=4-s'\), this route requires a uniform comparison \(M(t)\le C_1t^{-\alpha}\).

## Result

For \(\alpha\in[0,4]\), the uniform comparison \(M(t)\le C_1t^{-\alpha}\) for all \(t>0\) holds if and only if \(\alpha\le 1/2\). Equivalently, this envelope bookkeeping closes exactly for \(s'\ge 7/2\). In particular, the proposed \(s'=3\) boundary does not close: \(M(t)/t^{-1}\) grows like \(t^{1/2}\).

The same calculation gives the useful generic rule \(s'\ge Q-2\beta\) for envelopes with decay exponent \(0<\beta<7/4\). At the endpoint \(\beta=7/4\) a logarithmic factor appears; for \(\beta>7/4\) the small-radius contribution saturates the decay at order \(t^{-7/2}\). Thus, in the regime relevant to improving the present \(\beta=1/4\) estimate, reaching \(s'>3\) by this bookkeeping requires \(\beta>1/2\).

## Proof

Put \(r_*=t^{-1/2}\). If \(r_*\ge R_0\), then \(M(t)=R_0^7/7\). If \(r_*<R_0\), split the integral at \(r_*\):

\[
M(t)=\frac{t^{-7/2}}7+t^{-1/2}\frac{R_0^6-t^{-3}}6
     =\frac{R_0^6}{6}t^{-1/2}-\frac1{42}t^{-7/2}.
\]

Therefore \(M(t)t^\alpha\) is bounded at large \(t\) exactly when \(\alpha\le1/2\); small \(t\) is harmless for \(\alpha\ge0\). This proves the stated iff. The generic \(\beta\) qualification follows by splitting

\[
\int_0^{R_0}r^6\min\{1,(tr^2)^{-2\beta}\}\,dr
\]

at the same crossover. For \(0<\beta<7/4\), the large-radius term has leading order \(t^{-2\beta}\); at \(\beta=7/4\) it is \(t^{-7/2}\log t\); above that point the crossover contribution has order \(t^{-7/2}\).

## Limitations

- The high-frequency coefficient decay is cited from Raani-Singh and is not re-proved here.
- No positive-Lebesgue-measure theorem is proved at \(\dim_K>3\) or at \(7/2\); the full Frostman-energy argument remains open.
- The iff concerns this radial spectral-transfer bookkeeping. Other methods are not ruled out.

## Reproducibility

Run `python3 artifacts/threshold_closure.py` and `python3 artifacts/check_Rk_decay.py`. The first script checks the closed-form threshold arithmetic. The second is a numerical consistency check of the cited coefficient decay and is not a proof of that cited input.

## References

- K. S. S. Raani and R. K. Singh, *Distances in sets of positive Koranyi upper density in Heisenberg Group*, arXiv:2507.14917.
- B. Liu, *Group actions, the Mattila integral and applications*, Proc. Amer. Math. Soc. (2018), doi:10.1090/proc/14406.
