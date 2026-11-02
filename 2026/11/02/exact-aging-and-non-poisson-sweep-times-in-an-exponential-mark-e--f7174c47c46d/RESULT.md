# Exact aging and non-Poisson sweep times in an exponential-mark envelope

## Finding
Let \(\mathcal P\) be a Poisson point process on \([0,\infty)\times\mathbb R\) with intensity \(dx\,e^{-y}dy\). For each \(t>0\), let \((X_t,Y_t)\) be the (almost surely unique at deterministic \(t\)) point maximizing \(ty-x\). Let \(N(s,t)\), for \(0<s<t<\infty\), count changes of that maximizing point at times strictly between \(s\) and \(t\). Endpoint ties have probability zero. Then:

1. The unique maximizer exists at every deterministic positive time. The number of changes on each compact positive-time interval is finite almost surely, and
\[
\boxed{\mathbb E N(s,t)=\tfrac12\log(t/s).}
\]
2. If \(R_s\) is the time from \(s\) until the next change, then, conditional on the maximizer at \(s\),
\[
\boxed{\Pr(R_s>h\mid X_s,Y_s)=\exp(-h e^{-Y_s}),\qquad h\ge0.}
\]
In particular, its conditional distribution is exponential with rate \(e^{-Y_s}\) (and the rate does not depend on \(X_s\)).
3. Let \(E_1,E_2\) be independent rate-one exponential variables and let \(U\) be uniform on \((0,1)\), independently. The age-dependent hazard is distributed as
\[
\boxed{e^{-Y_s}\ \stackrel{d}{=}\ s^{-1}E_1 U.}
\]
For every \(0<s<t\), the precise probability that the same point leads throughout \([s,t]\) is
\[
\boxed{\Pr\{(X_s,Y_s)=(X_t,Y_t)\}=\Pr(R_s>t-s)=\frac{s}{t-s}\log\frac ts.}
\]
Furthermore, \(\mathbb E R_s=\infty\) for every \(s>0\).
4. Successive fitness increments at leader switches are independent \(\operatorname{Gamma}(2,1)\) variables. Conditional on the current fitness \(y\), the next holding time is exponential with rate \(e^{-y}\), independent of the fitness increment. In particular, for any fixed \(s>0\),
\[
\boxed{\frac{N(s,t)}{\log t}\longrightarrow\frac12\quad\text{almost surely as }t\to\infty.}
\]
5. After logarithmic time change, the set of leader-switching times is stationary with intensity \(1/2\), but is **not** a homogeneous Poisson process. Its void probability on any log-time interval of length \(a>0\) is
\[
\boxed{\frac{a}{e^a-1},}
\]
not the Poisson void probability \(e^{-a/2}\).

These statements are properties of the specified *limiting Poisson envelope*, not assertions of a path-level limit theorem for the underlying finite branching populations.

## Assumptions and scope
The spatial coordinate \(x\) is nonnegative; the mark \(y\) is real; the intensity \(dx\,e^{-y}dy\) is locally finite and infinite on the entire half-strip. The parameter \(t\) is strictly positive. A leader is defined by the global maximum of the linear score \(ty-x\). At random tie times the upper envelope has exactly two leaders almost surely; switch times mean those ties, and the leader is unambiguously defined immediately to either side. We always take \(0<s<t<\infty\). No assumption about a finite-population trajectory limit is needed.

## Proof
**Existence and the one-time Palm law.** The intensity of points with score \(ty-x>m\) is exactly
\[
\int_0^\infty\int_{(m+x)/t}^\infty e^{-y}\,dy\,dx=t e^{-m/t}.
\]
Therefore the maximum is finite and attained, unique almost surely at every fixed \(t>0\). Put \(Z_s=Y_s-X_s/s\). By the Poisson void probability, \(\Pr(Z_s\le z)=\exp(-s e^{-z})\). The Campbell--Mecke formula yields the joint density of \((X_s,Z_s)\):
\[
 e^{-z-x/s}\exp(-s e^{-z})\,dx\,dz.
\]
It factors: \(X_s/s\) is rate-one exponential, independent of \(Z_s-\log s\), which has the standard Gumbel distribution. If \(G\) is standard Gumbel and \(E_2\) is independent rate-one exponential, then \(Y_s\stackrel d=\log s+G+E_2\). Since \(e^{-G}\stackrel d=E_1\) is rate-one exponential and \(e^{-E_2}\stackrel d=U\) is uniform \((0,1)\), the asserted hazard-mixture law follows.

**Exact first-switch survival.** Condition on the leader \((X_s,Y_s)=(x,y)\), in the Palm sense. All other points form a Poisson process conditioned to avoid the region \(\{s y'-x'>s y-x\}\). For \(t>s\), precisely the points able to overtake this leader by time \(t\) without having overtaken it at \(s\) lie in
\[
\{x'>x,\ y+(x'-x)/t<y'\le y+(x'-x)/s\}.
\]
Their intensity is
\[
\int_x^\infty e^{-y}\big(e^{-(x'-x)/t}-e^{-(x'-x)/s}\big)\,dx'
=e^{-y}(t-s).
\]
Since each score is affine in time, a leader that is overtaken cannot regain leadership. The conditional probability of no change through \(t\) is the void probability \(\exp[-e^{-y}(t-s)]\). It follows that \(R_s\) is exponential conditional on the present leader. Integrating over the independent \(E_1,U\) gives, for \(h>0\),
\[
\mathbb E e^{-hE_1U/s}=\int_0^1\frac{du}{1+hu/s}
=\frac{s}{h}\log(1+h/s).
\]
This gives the announced persistence formula with \(h=t-s\), and its asymptotic \(\Pr(R_s>h)\sim(s/h)\log(h/s)\) makes \(\mathbb E R_s=\infty\).

**Switch-count intensity and local finiteness.** Every leader switch at a positive time is a tie of two distinct affine scores at the upper envelope. Almost surely there are no triple score ties. Parameterize an ordered tied pair at time \(t\) by a point \((x,y)\), a slope increment \(v>0\), and the second point \((x+tv,y+v)\). The Jacobian of the second spatial coordinate with respect to \(t\) is \(v\). The second-order Campbell--Mecke formula says that the expected switching intensity is
\[
\begin{aligned}
\int_0^\infty\!\int_{\mathbb R}\!\int_0^\infty
 &v e^{-2y-v}\exp[-t e^{-y+x/t}]\,dv\,dy\,dx\\
&=\int_0^\infty\frac{e^{-2x/t}}{t^2}\,dx
=\frac1{2t}.
\end{aligned}
\]
The exponential factor is the probability that no third point is above the tied score at time \(t\). Integrating on \((s,t)\) proves \(\mathbb E N(s,t)=\tfrac12\log(t/s)\) and, since an integer-valued random variable with finite expectation is finite almost surely, local finiteness.

**The marked replacement chain and almost-sure sweep frequency.** Given the entire observed leader history through time \(s\), the potential future overtakers lie below the current winning line at \(s\), have slope \(y+v\) with \(v>0\), and have position \(x+(s+h)v\) for \(h>0\). No such point could have beaten any earlier leader: because its slope exceeds that of the current leader and its score is below the current line at \(s\), it was even farther below that line at each earlier time, when the actual leader scored at least as high. Thus the previously exposed exclusion regions do not restrict this future-overtaker set. The Poisson property and the Jacobian \(dx\,dy=v\,dh\,dv\) yield its conditional marked intensity
\[
 e^{-y}\,dh\,v e^{-v}dv.
\]
Here \(\int_0^\infty v e^{-v}dv=1\). Hence the first prospective crossing is the actual next switch, its waiting time is exponential with rate \(e^{-y}\), and its independent fitness increment has the \(\operatorname{Gamma}(2,1)\) law. At a switch, every prospective overtaker of the new leader is below the common tied score at that instant, and lies among the old leader's as-yet-unexposed prospective overtakers with crossing time later than the observed first crossing. Independence of disjoint Poisson arrival-time strips therefore renews the same marked intensity. Iterating gives independent gamma increments and independent rate-one exponential multipliers in successive holding times. Label the successive switching times after a fixed starting \(s>0\) by \(T_k\), with \(T_0=s\), and let \(Y_k\) be the fitness of the champion just after \(T_k\). Then
\[
Y_k=Y_0+\sum_{j=1}^k V_j,\qquad T_{k+1}-T_k=e^{Y_k}E_k,
\]
with iid \(V_j\sim\operatorname{Gamma}(2,1)\), iid \(E_k\sim\operatorname{Exp}(1)\), and the two sequences independent. The strong law gives \(Y_k/k\to2\), while Borel--Cantelli gives \(\log E_k/k\to0\) and \(\log\max_{j<k}E_j/k\to0\). Comparing \(T_k\) with its last summand and with \(k e^{Y_{k-1}}\max_{j<k}E_j+s\) yields \(\log T_k/k\to2\) almost surely. Inversion of the increasing sequence of switch times proves \(N(s,t)/\log t\to1/2\) almost surely.

**Log-time stationarity and non-Poisson character.** For every \(a>0\), the map \((x,y)\mapsto(x/a,y-\log a)\) preserves the Poisson intensity. The winner process at time \(at\) transforms to \((aX_t,Y_t+\log a)\) in distribution, simultaneously for all times. Consequently its switching point process is stationary under time multiplication, equivalently under translation of \(\log t\). Its expected count in a log interval of length \(b\) is \(b/2\). By the persistence formula, the probability of no switch in such an interval is \(b/(e^b-1)\), which differs from \(e^{-b/2}\), for instance at \(b=\log2\). Thus the switch process is not homogeneous Poisson.

## Verification
The companion `verify.py` is standalone Python using NumPy and SciPy. It independently integrates the one-point Campbell formula at five time pairs, verifies the hazard-mixture formula and the integrated crossing intensity, simulates a finite-window restriction of the planar Poisson process, and checks two large gamma-renewal samples against the logarithmic frequency coefficient. All 17 checks pass with the recorded fixed seed; `verification_output.txt` records the result. These finite numerical checks are illustrative only. The displayed intensity calculations, Palm identity and Poisson void probability give the exact infinite-process proof.

## Relationship to prior work
Fontes and Schinazi (2026, arXiv:2610.29759v1, Section 3, especially equations (10)--(14)) introduce this specific planar Poisson limit as an envelope of selective-sweep genotypes and state fixed-time and finite-dimensional behavior. Their text does not provide the exact conditional reign law, two-time leader persistence, expected number of actual leader changes, or the non-Poisson log-time comparison established here. The point process of *candidate mutations* is Poisson; the derived set of **actual leader-switch times** need not be.

The classical Poisson mapping/void/Mecke principles used in the proof are existing mathematics. Boettcher, Robe and Sibani (2018, arXiv:1803.06580) study Poisson behavior in logarithmic time for a different record-driven aging model, rather than this envelope and its non-Poisson switching law. Groeneboom (2011, arXiv:1111.2504) studies a homogeneous quadrant Poisson convex hull selected by linear forms \(x+az\). Under \(z=e^{-y}\) the present envelope minimizes \(x+t\log z\), **not** \(x+az\); its hull jump results therefore do not directly state the present identities. Related Poisson-hull methods remain a possible route to broader deductions.

## Limitations
The theorem treats only the continuum limiting point process; it does not prove convergence of the discrete selective-sweep counting process, any path-space topology for empirical measures, or finite-size error bounds. The exact values require the exponential mark intensity and linear score on the half-strip. Broader Poisson-envelope literature could implicitly subsume individual formulas; independent priority assessment remains unperformed. The numerical verifier samples a truncated Poisson window and cannot establish exact identities in the infinite process.

## References
1. L. R. Fontes and R. B. Schinazi, *A branching model for selective sweeps*, arXiv:2610.29759v1, first public 2026-10-21, https://arxiv.org/html/2610.29759v1.
2. S. I. Resnick, *Extreme Values, Regular Variation, and Point Processes*, Springer (1987; 2008 reprint), standard Poisson point-process methods.
3. S. Boettcher, D. M. Robe and P. Sibani, *Aging is a (log-)Poisson Process, not a Renewal Process*, arXiv:1803.06580, https://arxiv.org/html/1803.06580v2.
4. P. Groeneboom, *The remaining area of the convex hull of a Poisson process*, arXiv:1111.2504, https://arxiv.org/abs/1111.2504.
