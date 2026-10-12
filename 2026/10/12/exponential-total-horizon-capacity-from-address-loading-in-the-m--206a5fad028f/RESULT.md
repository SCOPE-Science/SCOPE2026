# Exponential total-horizon capacity from address loading in the measured dephasing family
## Finding
Fix \(0<\gamma\le 1/16\), \(0\le p\le 1/4\), and an integer \(K\ge2\). For the measured-address dephasing family of Wang, let \(h\) loading transitions store an address of dimension \(R=2^h\), let \(T\ge1\) be the number of noisy phase transitions, and impose the total-horizon constraint \(h+T=K\). Define
\[
\mathfrak C_\gamma(K,p)=\max_{h,T:\,h\ge0,\,T\ge1,\,h+T=K}\operatorname{sfat}_\gamma\mathcal N_{2^h,T,p}.
\]
Then
\[
\frac{\log_2 3}{32}\,2^K\le \mathfrak C_\gamma(K,p)\le \frac{\kappa_\gamma\log_2 3}{2}\,2^K,
\]
where \(\kappa_\gamma\) is the source's uniform constant. Thus \(\mathfrak C_\gamma(K,p)=\Theta_\gamma(2^K)\) uniformly for the entire noise interval \(0\le p\le1/4\). A fixed two-slot phase segment, \(T=2\) and \(h=K-2\), already attains the lower exponential order.

The dimensionless comparison profile inherited from the source upper bound,
\[
f(T)=\frac{T}{2^T}\log_2(1+T),
\]
has the unique integer maximizer \(T=2\). This is a statement about the theorem's uniform order profile; the unknown multiplicative constants do not justify claiming that \(T=2\) exactly maximizes the true capacity.
## Assumptions and scope
The process family, tester model, dephasing convention, and sequential fat-shattering dimension are exactly those of arXiv:2610.02068v1, Theorem V.1. The margin \(\gamma\) is fixed in \((0,1/16]\), the known dephasing parameter obeys \(p\in[0,1/4]\), and the address is fully charged: loading \(h\) bits consumes \(h\) of the \(K\) transitions. The result optimizes only over the source's measured-address dephasing subfamily; it does not determine the optimal duration-memory law for the full class of finite-memory quantum processes.
## Proof
The source proves uniformly in \(R=2^h\), \(T\ge1\), and \(p\in[0,1/4]\) that
\[
\frac{RT}{16}\log_2\!\bigl(1+\min(T,1/p)\bigr)
\le \operatorname{sfat}_\gamma\mathcal N_{R,T,p}
\le \kappa_\gamma RT\log_2\!\bigl(1+\min(T,1/p)\bigr),
\]
with \(1/0=\infty\). Since \(R=2^{K-T}\), choosing \(T=2\) gives \(R=2^{K-2}\). Because \(p\le1/4\), one has \(1/p\ge4\) when \(p>0\), and the same minimum equals \(2\) at \(p=0\). Therefore
\[
\operatorname{sfat}_\gamma\mathcal N_{2^{K-2},2,p}
\ge \frac{2^{K-2}\cdot2}{16}\log_2 3
=\frac{\log_2 3}{32}2^K.
\]

For the upper bound, \(\min(T,1/p)\le T\), so every split satisfies
\[
\operatorname{sfat}_\gamma\mathcal N_{2^{K-T},T,p}
\le \kappa_\gamma 2^K f(T),\qquad
f(T)=\frac{T}{2^T}\log_2(1+T).
\]
Now \(f(1)=1/2\), \(f(2)=(\log_2 3)/2\), and \(f(3)=3/4<f(2)\). For every integer \(T\ge3\),
\[
\frac{f(T+1)}{f(T)}
=\frac{T+1}{2T}\frac{\ln(T+2)}{\ln(T+1)}<1.
\]
Indeed, \((T+1)/(2T)\le2/3\), while \(T+2<(T+1)^{3/2}\) gives \(\ln(T+2)/\ln(T+1)<3/2\). Hence \(f\) decreases strictly from \(T=3\) onward, and its unique integer maximum is \(f(2)=(\log_2 3)/2\). Maximizing over all splits yields the stated upper bound.
## Verification
The algebra above is exact. The accompanying verifier checks the finite profile values, the strict ratio inequality on a long integer range, and the lower/upper constants used in the displayed sandwich. Those computations are corroborative; the monotonicity argument in the proof is the infinite-range certificate.
## Relationship to prior work
Wang introduced this measured-address family, explicitly charges the loading horizon through \(K=h+T\), and proves the uniform \(\Theta_\gamma(RT\log_2(1+\min(T,1/p)))\) law. The paper discusses growing memory and notes that the optimal joint duration-memory-margin dependence for the full process class remains open, but it does not collapse the measured-address theorem to a total-horizon-only optimization or state the uniform exponential sandwich above. Raza, Caro, Eisert, and Khatri study online learning of quantum processes and provide broad multitime-process learning bounds, but their work predates this measured-address family and does not contain this loading-versus-phase allocation result.
## Limitations
This is an optimization consequence for one structured family, not a solution of the source's open problem for all finite-memory processes. The constants in Theorem V.1 are comparison constants, so the theorem proves the exponential total-horizon order and the unique maximizer of its comparison profile, not the exact split maximizing the true capacity. No claim is made outside \(0<\gamma\le1/16\) and \(0\le p\le1/4\).
## References
1. Y. Wang, “Sequential Capacity of Quantum Processes with Finite Memory,” arXiv:2610.02068v1 (2026).
2. A. Raza, M. C. Caro, J. Eisert, and S. Khatri, “Online learning of quantum processes,” arXiv:2406.04250v1 (2024).
